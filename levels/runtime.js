// Bộ chạy màn theo dữ liệu (data-driven) cho 25 màn thiết kế lại.
// Dữ liệu: levels/data/<id>.js (LEVEL_DATA[id]) — sinh từ docs/level-design/campaign/tools/export_levels.py.
// Đơn vị trong dữ liệu là ô 32px; hàm build đổi sang pixel thế giới. Lò Nham Thạch (x5_dinorex) giữ builder riêng.
(function(){
const T=32,DATA=()=>window.LEVEL_DATA||{};
const SUBSIZE={donut:[110,110],truck:[170,60],submarine:[180,130],illumina:[140,130]};
const cyc=(t,on,off,ph)=>((t+ph)%(on+off))<on;
const inBox=(o,b)=>o.x+o.w>b.x&&o.x<b.x+b.w&&o.y+o.h>b.y&&o.y<b.y+b.h;
const onTop=pl=>p.ground&&Math.abs(p.y+p.h-pl.y)<4&&p.x+p.w>pl.x&&p.x<pl.x+pl.w;
const px=b=>({...b,x:b.x*T,y:b.y*T,w:b.w*T,h:b.h*T});

function build(s,L){
 const D={L,t:0,slopes:[],haz:[],zones:[],conv:[],crumbles:[],turrets:[],mines:[],sw:[],safe:null,gate:null,orbs:0,rooms:L.rooms,theme:L.theme,pal:L.palette||{}};
 const W={width:L.width*T,height:L.height*T,floor:L.floorBoss*T,platforms:[],hazards:[],enemies:[],bullets:[],particles:[],items:[],
  checkpoints:L.checkpoints.map(c=>({x:c.x*T,y:c.y*T})),boss:null,zones:[],walls:[],switches:[],vehicles:[],portals:[],searchlights:[],subs:[],
  gravityScale:1,warning:0,ready:1.2,clock:0,elapsed:0,damage:0,rush:0,camY,data:D,bossGate:L.bossGateX*T,areaMarks:(L.areaMarks||[]).map(x=>x*T)};
 W.platforms.push({x:-99999,y:-99999,w:0,h:0,kind:'datalayer',layer:'back'});
 const solid=(b,extra={})=>{const pl={x:b.x*T,y:b.y*T,w:b.w*T,h:b.h*T,kind:'ground',area:b.area||1,...extra};W.platforms.push(pl);return pl;};
 for(const b of L.solids)solid(b);
 // dốc: bề mặt một chiều + cột đặc ngay dưới (giống Lò Nham Thạch)
 for(const sl of L.slopes){D.slopes.push({x0:sl.x0*T,y0:sl.y0*T,x1:sl.x1*T,y1:sl.y1*T,bottom:sl.bottom*T,area:sl.area});
  for(let x=Math.floor(sl.x0);x<Math.ceil(sl.x1);x++){const f=v=>sl.y0+(sl.y1-sl.y0)*(v-sl.x0)/(sl.x1-sl.x0),ya=f(Math.max(x,sl.x0)),yb=f(Math.min(x+1,sl.x1));
   solid({x:Math.max(x,sl.x0),y:Math.max(ya,yb)+.45,w:Math.min(x+1,sl.x1)-Math.max(x,sl.x0),h:sl.bottom-Math.max(ya,yb)-.45,area:sl.area},{under:true});}}
 for(const l of L.ledges){const base={x:l.x*T,y:l.y*T,w:l.w*T,h:16,baseX:l.x*T,baseY:l.y*T,move:0,style:l.kind};let pl;
  if(l.kind==='holo'||l.kind==='holoB')pl={...base,kind:'phase',phase:l.kind==='holo'?0:2.2};
  else if(l.kind==='thrust')pl={...base,kind:'lift',move:3*T};
  else if(l.kind==='move')pl={...base,kind:'ledge',move:3*T};
  else pl={...base,kind:'ledge'};
  if(l.kind==='safe')pl.safe=true;W.platforms.push(pl);
  if(l.kind==='break')D.crumbles.push({pl,delay:.5,respawn:4});
  if(l.kind==='bounce')D.zones.push({type:'bounce',x:pl.x,y:pl.y-10,w:pl.w,h:14,pl});}
 for(const c of L.conveyors)D.conv.push({x:c.x*T,y:c.y*T,w:c.w*T,speed:c.speed});
 for(const h of L.hazards){const z=px(h);z.type=h.type;z.on=h.on;z.off=h.off;z.phase=h.phase||0;z.column=h.column;
  if(h.type==='mine')D.mines.push({x:z.x,y:z.y,w:Math.max(z.w,24),h:Math.max(z.h,24),armed:true,back:0});else D.haz.push(z);}
 for(const z0 of L.zones){const z=px(z0);z.type=z0.type;z.dx=z0.dx||0;z.dy=z0.dy||0;z.strength=z0.strength||70;z.label=z0.label||'';D.zones.push(z);
  if(z.type==='flip'||z.type==='flipcycle'){const g={type:'gravity',x:z.x,y:z.y,w:z.w,h:z.h,src:z};W.zones.push(g);z.base=g;
   for(const pl of W.platforms)if(pl.kind==='ground'&&pl.x<z.x+z.w&&pl.x+pl.w>z.x&&Math.abs(pl.y+pl.h-z.y)<T*1.2)W.platforms.push({x:pl.x,y:pl.y,w:pl.w,h:pl.h,kind:'ceiling',area:pl.area,ghost:true});}
  if(z.type==='alarm')z.alert=0;}
 // tường: phá được (stone/steel), cổng công tắc (laser/gate), cổng quả năng lượng (orbgate)
 L.walls.forEach(w=>{W.walls.push({...px(w),type:w.type==='gate'||w.type==='orbgate'?w.type:w.type,hp:w.type==='steel'?24:w.type==='stone'?16:999,dead:false});});
 L.switches.forEach(sw=>{const o={x:sw.x*T,y:sw.y*T,w:32,h:32,on:false,gate:-1,targets:sw.targets};W.switches.push(o);});
 // địch, vật phẩm, xe, cổng dịch chuyển, tháp pháo
 const hpE=10+Math.floor(s.index/4);
 for(const e of L.enemies){const o={x:e.x*T,y:e.y*T-48,w:32,h:48,type:e.type,max:hpE,hp:hpE,cool:1+Math.random(),inv:0,t:Math.random()*3,dir:-1,dead:false};o.startX=o.x;o.startY=o.y;W.enemies.push(o);}
 let rq=0;for(const it of L.items){const X=it.x*T,Y=it.y*T;
  if(it.type==='rescue'){const id=it.id;W.items.push({id,x:X,y:Y-48,w:32,h:48,type:'rescue',variant:(rq++)%6,got:save.rescues.includes(id)});}
  else if(it.type==='relic')W.items.push({id:it.id,type:'relic',x:X,y:Y-28,w:28,h:28,got:save.relics.includes(it.id)});
  else if(it.type==='tank')W.items.push({id:it.id,type:'tank',x:X,y:Y-30,w:25,h:30,got:false});
  else if(it.type==='capsule')W.items.push({id:it.id,type:'capsule',armor:it.armor,part:it.part,x:X,y:Y-70,w:44,h:70,got:(save.parts[it.armor]||[]).includes(it.part)});
  else if(it.type==='orb'){W.items.push({type:'orb',x:X,y:Y,w:16,h:16,got:false});D.orbs++;}}
 for(const v of L.vehicles)W.vehicles.push(v.type==='mech'?{type:'mech',x:v.x*T,y:v.y*T-70,w:65,h:70}:{type:'chaser',x:v.x*T,y:v.y*T-45,w:90,h:45});
 L.portals.forEach(po=>{const o={x:po.x*T,y:po.y*T-80,w:45,h:80};if(po.rush!=null){o.rush=po.rush;}W.portals.push(o);});
 L.portals.forEach((po,i)=>{if(po.to!=null){W.portals[i].tx=W.portals[po.to].x+60;W.portals[i].ty=W.portals[po.to].y+20;}});
 if(s.id==='x6_f5_bossrush'){W.rushList=STAGES.slice(13,21).map(s=>s.id);for(const po of W.portals){po.tx=L.bossGateX*T+120;po.ty=W.floor-90;}}
 for(const t of L.turrets)D.turrets.push({x:t.x*T,y:t.y*T,w:32,h:32,hp:t.hp,cool:1+Math.random()*1.5});
 if(L.subBoss){const sb=L.subBoss,[w,h]=SUBSIZE[sb.id]||[110,110];W.subs.push({id:sb.id,x:sb.x*T,y:sb.y*T,w,h,hp:sb.hp,max:sb.hp,inv:0,cool:1.4,dead:false});
  D.gate=solid({...sb.gate,area:2},{gate:true});}
 W.platforms.push({x:-99999,y:-99999,w:0,h:0,kind:'datalayer',layer:'front'});
 W.boss={x:W.width-250,y:W.floor-120,w:80,h:120,vx:0,vy:0,dir:-1,max:140+s.index*5,hp:140+s.index*5,inv:0,t:0,state:0,action:0,attackAt:1.2,slow:0};
 return W;}

// ---------- cập nhật ----------
function zonesAt(type){const D=world.data;return D.zones.filter(z=>z.type===type&&inBox(p,z));}
function before(){const D=world.data;if(!D||!p)return;const th=D.theme;
 // vật lý nước/băng của game gốc dựa vào stage.theme: chỉ bật khi đang ở trong vùng tương ứng (trả lại ngay sau bước vật lý)
 stage.theme=zonesAt('water').length?'water':zonesAt('ice').length?'ice':th==='water'||th==='ice'?'_'+th:th;
 if(zonesAt('lowgrav').length)world.gravityScale=.42;
 for(const z of D.zones)if(z.type==='flipcycle'&&z.base)z.base.type=Math.floor(D.t/4)%2?'gravity_off':'gravity';
 if(zonesAt('mud').length||zonesAt('slow').length)world.playerSlow=Math.max(world.playerSlow||0,.05);}
function kill(){p.inv=0;hurt(999);}
function toSafe(dmg){const S=world.data.safe;p.inv=0;hurt(dmg);if(p.hp>0&&S){p.x=S.x;p.y=S.y;p.vx=0;p.vy=0;p.inv=1.2;}}
function update(dt){const D=world.data;if(!D)return;stage.theme=D.theme;if(!p||p.hp<=0)return;D.t+=dt;const t=D.t;
 if(p.ground&&!world.platforms.some(pl=>pl.style==='break'&&onTop(pl)))D.safe={x:p.x,y:p.y};
 // dốc
 const cx=p.x+p.w/2;for(const s of D.slopes){if(cx<s.x0||cx>s.x1)continue;const sy=s.y0+(s.y1-s.y0)*(cx-s.x0)/(s.x1-s.x0),feet=p.y+p.h;if(p.vy>=0&&feet>=sy-6&&feet<=sy+26){p.y=sy-p.h;p.vy=0;p.ground=true;p.airDash=true;}}
 // băng chuyền
 for(const c of D.conv)if(p.ground&&Math.abs(p.y+p.h-c.y)<T*.7&&p.x+p.w>c.x&&p.x<c.x+c.w)p.x+=c.speed*dt;
 // bẫy
 for(const h of D.haz){h.active=h.on==null||cyc(t,h.on,h.off,h.phase);if(!h.active||!inBox(p,h))continue;
  switch(h.type){case 'lava':if(h.column)hurt(5);else{hurt(6);p.vy=-720;p.ground=false;}break;
   case 'acid':hurt(7);p.vy=-680;p.ground=false;break;
   case 'void':toSafe(6);break;
   case 'spike':case 'thorn':hurt(h.type==='thorn'?3:5,(p.x<h.x+h.w/2?-1:1)*160,'spikes');if(p.hp>0&&p.inv>0&&p.vy>=0){p.vy=-420;p.ground=false;}break;
   case 'trash':hurt(4,(p.x<h.x+h.w/2?-1:1)*220);break;
   default:hurt(4,(p.x<h.x+h.w/2?-1:1)*140);}}
 // mìn / tinh thể nổ
 for(const m of D.mines){if(!m.armed){m.back-=dt;if(m.back<=0)m.armed=true;continue;}
  const hit=world.bullets.find(b=>!b.enemy&&overlap(b,m));const near=Math.hypot(p.x+p.w/2-m.x-m.w/2,p.y+p.h/2-m.y-m.h/2)<T*1.1;
  if(hit||near){if(hit)hit.life=0;m.armed=false;m.back=4;particle(m.x+m.w/2,m.y+m.h/2,'#ffb070',26,220);beep(90,.25,'sawtooth',.05,40);
   if(Math.hypot(p.x+p.w/2-m.x-m.w/2,p.y+p.h/2-m.y-m.h/2)<T*2.2)hurt(5,(p.x<m.x?-1:1)*260);
   for(const o of D.mines)if(o!==m&&o.armed&&Math.hypot(o.x-m.x,o.y-m.y)<T*3){o.armed=false;o.back=4.3;particle(o.x+12,o.y+12,'#ffb070',18,180);}}}
 // vùng
 for(const z of D.zones){if(z.type==='bounce'){if(inBox(p,z)&&p.vy>=0){p.vy=held.has('jump')?-1020:-900;p.ground=false;beep(350,.1,'triangle',.03,800);}continue;}
  if(!inBox(p,z))continue;
  if(z.type==='wind'||z.type==='current'){let k=1;if(/giật/.test(z.label))k=((t%5)<2)?1.4:0;if(/đổi chiều/.test(z.label))k=Math.floor(t/4)%2?-1:1;
   p.x+=z.dx*z.strength*k*dt*(p.ground&&z.type==='wind'?.7:1);if(z.dy)p.vy+=z.dy*z.strength*6*k*dt;}
  else if(z.type==='updraft'){p.vy=Math.max(-430,p.vy-2600*dt);}
  else if(z.type==='well'){const cxz=z.x+z.w/2,cyz=z.y+z.h/2,dx=cxz-(p.x+p.w/2),dy=cyz-(p.y+p.h/2),d=Math.max(40,Math.hypot(dx,dy));p.x+=dx/d*90*dt;p.vy+=dy/d*500*dt;}
  else if(z.type==='rain'){const m=/(\d+)s mưa \/ (\d+)s tạnh|mưa (\d+)s \/ tạnh (\d+)s/.exec(z.label)||[];const on=+(m[1]||m[3]||3),off=+(m[2]||m[4]||7);z.raining=cyc(t,on,off,0);
   if(z.raining){const roof=world.platforms.some(pl=>pl.kind==='ground'&&!pl.under&&pl.y+pl.h<=p.y+2&&pl.y>z.y-T&&p.x+p.w/2>pl.x&&p.x+p.w/2<pl.x+pl.w);if(!roof){z.tick=(z.tick||0)-dt;if(z.tick<=0){z.tick=.5;hurt(1);}}}}
  else if(z.type==='alarm'){const beam=z.x+z.w/2+Math.sin(t*1.1+z.x)*(z.w/2-T);z.beam=beam;if(Math.abs(p.x+p.w/2-beam)<T*1.2){z.seen=(z.seen||0)+dt;if(z.seen>.5&&z.alert<=0){z.alert=3;toast('ALERT / ĐÈN PHA',1.2);for(let i=0;i<3;i++)enemyShot(beam,z.y+8,(i-1)*90,320,13,'#ff7c8d');}}else z.seen=0;}
  else if(z.type==='elec'&&cyc(t,1.5,1.5,0))hurt(3);}
 for(const z of D.zones)if(z.type==='alarm'){z.alert=Math.max(0,z.alert-dt);if(z.beam==null)z.beam=z.x+z.w/2;else if(!inBox(p,z))z.beam=z.x+z.w/2+Math.sin(t*1.1+z.x)*(z.w/2-T);}
 // sàn sập
 for(const k of D.crumbles){const pl=k.pl;if(pl.broken){k.back-=dt;if(k.back<=0){pl.broken=false;k.timer=null;}continue;}
  if(k.timer==null&&onTop(pl))k.timer=k.delay;if(k.timer!=null){k.timer-=dt;pl.shake=k.timer>0;if(k.timer<=0){pl.broken=true;k.back=k.respawn;k.timer=null;particle(pl.x+pl.w/2,pl.y,'#c09070',10,120);}}}
 // tháp pháo
 for(const q of D.turrets){if(q.hp<=0)continue;for(const b of world.bullets)if(!b.enemy&&overlap(b,q)){q.hp-=b.power===2?6:b.power?3:1;b.life=0;if(q.hp<=0)particle(q.x+16,q.y+16,'#ffd27a',20,160);}
  q.cool-=dt;if(q.cool<=0&&Math.abs(p.x-q.x)<520&&Math.abs(p.y-q.y)<360){q.cool=2.2;const a=Math.atan2(p.y+20-q.y-16,p.x+14-q.x-16);enemyShot(q.x+16,q.y+16,Math.cos(a)*230,Math.sin(a)*230,11,'#ffb04a');}}
 // công tắc → nhiều mục tiêu; cổng mini-boss; cổng quả năng lượng
 for(const sw of world.switches)if(sw.on&&sw.targets)for(const i of sw.targets)if(world.walls[i]&&!world.walls[i].dead){world.walls[i].dead=true;particle(world.walls[i].x+8,world.walls[i].y+40,'#ffe080',14,140);}
 for(const w of world.walls)if(!w.dead&&w.type==='laser'&&overlap(p,w)&&p.inv<=0)hurt(4,(p.x<w.x?-1:1)*200);
 if(D.orbs){const got=world.items.filter(i=>i.type==='orb'&&i.got).length;D.orbGot=got;if(got>=D.orbs)for(const w of world.walls)if(w.type==='orbgate'&&!w.dead){w.dead=true;toast('ĐỦ '+D.orbs+' QUẢ NĂNG LƯỢNG · CỬA ĐÃ MỞ',2);}}
 if(D.gate&&!D.gate.broken&&world.subs.length&&world.subs.every(s=>s.dead)){D.gate.broken=true;toast('CỔNG AREA 2 ĐÃ MỞ',1.6);}
 // Ride Chaser chạy tự do (không tự cuộn): nhanh hơn, nhảy xa hơn; rời xe ở cuối Area 1
 if(p.vehicle==='chaser'){p.x+=p.vx*(held.has('dash')?1.1:.7)*dt;if(world.areaMarks[0]&&p.x>world.areaMarks[0]-2*T){p.vehicle=null;toast('RIDE CHASER · HẾT ĐƯỜNG ĐUA',2);}}
 unstick();}
function unstick(){for(const pl of world.platforms){if(pl.kind!=='ground'||pl.broken||!overlap(p,pl))continue;
  const l=p.x+p.w-pl.x,r=pl.x+pl.w-p.x,u=p.y+p.h-pl.y,d=pl.y+pl.h-p.y,m=Math.min(l,r,u,d);
  if(m===u){p.y=pl.y-p.h;p.vy=Math.min(0,p.vy);p.ground=true;}else if(m===l)p.x=pl.x-p.w;else if(m===r)p.x=pl.x+pl.w;else{p.y=pl.y+pl.h;p.vy=Math.max(0,p.vy);}}}

// ---------- vẽ ----------
const PAT={};function pat(n){if(PAT[n]!==undefined)return PAT[n];const im=A[n];return PAT[n]=im?ctx.createPattern(im,'repeat'):null;}
function wfill(x,y,w,h,n,c){ctx.save();ctx.translate(-camera.x,-camera.y);ctx.fillStyle=pat(n)||c;ctx.fillRect(x,y,w,h);ctx.restore();}
function strip(n,x,y,w,h,sy=0,sh){const im=A[n];if(!im)return false;sh=sh||im.height;for(let xx=0;xx<w;xx+=im.width){const ww=Math.min(im.width,w-xx);ctx.drawImage(im,0,sy,ww,sh,Math.round(x+xx-camera.x),Math.round(y-camera.y),ww,h);}return true;}
function cell(n,frames,i,x,y,w,h,alpha=1){const im=A[n];if(!im)return false;const cw=im.width/frames;ctx.globalAlpha=alpha;ctx.drawImage(im,(i%frames)*cw,0,cw,im.height,Math.round(x-camera.x),Math.round(y-camera.y),w,h);ctx.globalAlpha=1;return true;}
// lát ngang giữ đúng tỉ lệ khung gốc (sprite X5/X6 vẽ 1:1); khung cuối bị cắt chứ không bóp méo
function tile(n,frames,i,x,y,w,h,alpha=1){const im=A[n];if(!im)return false;const cw=im.width/frames,tw=Math.max(4,cw*h/im.height);ctx.save();ctx.beginPath();ctx.rect(Math.round(x-camera.x),Math.round(y-camera.y),w,h);ctx.clip();for(let xx=0;xx<w;xx+=tw)cell(n,frames,i,x+xx,y,tw,h,alpha);ctx.restore();return true;}
function vtile(n,frames,i,x,y,w,h){const im=A[n];if(!im)return false;const cw=im.width/frames,th=im.height*w/cw;ctx.save();ctx.beginPath();ctx.rect(Math.round(x-camera.x),Math.round(y-camera.y),w,h);ctx.clip();for(let yy=0;yy<h;yy+=th)cell(n,frames,i,x,y+yy,w,th);ctx.restore();return true;}
function rr(x,y,w,h,c){rect(x-camera.x,y-camera.y,w,h,c);}
const vis=(x,y,w,h)=>x+w>camera.x-40&&x<camera.x+1000&&y+h>camera.y-40&&y<camera.y+580;
function back(){const D=world.data,pal=D.pal;stage.theme=D.theme;
 for(const r of D.rooms){const X=r.x*T,Y=r.y*T,W=r.w*T,H=r.h*T;if(!vis(X,Y,W,H))continue;const c=r.kind==='boss'?'#4e1c28':r.kind==='mini'?'#421e34':(r.area===2?pal.bg2:pal.bg1)||'#202030';
  rr(X,Y,W,H,c+(r.area===2||r.kind!=='room'?'d8':'70'));text(r.code+' '+r.name,X+10-camera.x,Y+20-camera.y,11,'#ffe3a088','left');}
 const th=D.theme;for(const s of D.slopes){if(s.x1<camera.x-40||s.x0>camera.x+1000)continue;ctx.save();ctx.beginPath();ctx.moveTo(s.x0-camera.x,s.y0-camera.y);ctx.lineTo(s.x1-camera.x,s.y1-camera.y);ctx.lineTo(s.x1-camera.x,s.bottom-camera.y);ctx.lineTo(s.x0-camera.x,s.bottom-camera.y);ctx.closePath();ctx.clip();
  ctx.translate(-camera.x,-camera.y);ctx.fillStyle=pat('terrain-'+th)||'#5c4a40';ctx.fillRect(s.x0,Math.min(s.y0,s.y1),s.x1-s.x0,s.bottom-Math.min(s.y0,s.y1));ctx.restore();
  const cap=A['cap-'+th],len=Math.hypot(s.x1-s.x0,s.y1-s.y0);ctx.save();ctx.translate(s.x0-camera.x,s.y0-camera.y);ctx.rotate(Math.atan2(s.y1-s.y0,s.x1-s.x0));if(cap)for(let xx=0;xx<len;xx+=cap.width){const ww=Math.min(cap.width,len-xx);ctx.drawImage(cap,0,0,ww,cap.height,xx,-6,ww,cap.height);}ctx.restore();}
 // vùng phía sau (nước, gió, trọng lực...)
 const t=D.t;for(const z of D.zones){if(!vis(z.x,z.y,z.w,z.h))continue;
  if(z.type==='water'){rr(z.x,z.y,z.w,z.h,'#2a6ab855');tile('el-water',4,Math.floor(t*6),z.x,z.y-6,z.w,12,.9);}
  else if(z.type==='wind'||z.type==='current'){ctx.globalAlpha=.35;for(let i=0;i<z.w*z.h/9000;i++){const u=(i*97.3%z.w+t*z.dx*180+z.w*10)%z.w,v=(i*53.7)%z.h;line(z.x+u-camera.x,z.y+v-camera.y,z.x+u-camera.x-z.dx*22,z.y+v-camera.y-z.dy*22,z.type==='wind'?'#d8f0ff':'#9fe6ff',1);}ctx.globalAlpha=1;}
  else if(z.type==='updraft'){ctx.globalAlpha=.25;rr(z.x,z.y,z.w,z.h,'#a0f0c8');ctx.globalAlpha=.5;for(let k=0;k<6;k++){const v=(t*240+k*z.h/6)%z.h;line(z.x+z.w*(k+.5)/6-camera.x,z.y+z.h-v-camera.y,z.x+z.w*(k+.5)/6-camera.x,z.y+z.h-v-20-camera.y,'#e0fff0',2);}ctx.globalAlpha=1;}
  else if(['flip','flipcycle','lowgrav','well'].includes(z.type)){const off=z.base&&z.base.type!=='gravity';rr(z.x,z.y,z.w,z.h,off?'#ff78dc12':'#ff78dc26');if(z.type==='well'){ctx.globalAlpha=.4;for(let k=1;k<5;k++){ctx.beginPath();ctx.arc(z.x+z.w/2-camera.x,z.y+z.h/2-camera.y,k*30+(t*25)%30,0,7);ctx.strokeStyle='#ff9ae8';ctx.stroke();}ctx.globalAlpha=1;}}
  else if(z.type==='slow')rr(z.x,z.y,z.w,z.h,'#b08cff22');
  else if(z.type==='mud')tile('el-mud',1,0,z.x,z.y,z.w,z.h);
  else if(z.type==='ice')rr(z.x,z.y,z.w,z.h,'#b8e8ffaa');}}
function front(){const D=world.data,t=D.t;
 for(const c of D.conv){if(!vis(c.x,c.y,c.w,20))continue;rr(c.x,c.y,c.w,8,'#5a5e70');for(let i=((t*Math.abs(c.speed))%24);i<c.w;i+=24)text(c.speed<0?'←':'→',c.x+(c.speed<0?c.w-i:i)-camera.x,c.y+7-camera.y,11,'#ffd27a','center');}
 for(const h of D.haz){if(!vis(h.x,h.y,h.w,h.h))continue;const warn=h.on!=null&&!h.active&&((t+h.phase)%(h.on+h.off))>h.on+h.off-.45;
  switch(h.type){
   case 'lava':if(h.column){if(h.active){rr(h.x,h.y,h.w,h.h,'#ff6e1e');rr(h.x+h.w*.3,h.y,h.w*.3,h.h,'#ffd27a');}else rr(h.x,h.y+h.h-8,h.w,8,warn?'#ffd27a':'#a84018');}
    else{rr(h.x,h.y,h.w,h.h,'#ff6e1e');for(let x=h.x;x<h.x+h.w;x+=24)rr(x,h.y+Math.sin(t*4+x)*2,14,3,'#ffd27a');}break;
   case 'acid':rr(h.x,h.y,h.w,h.h,'#6ad040cc');for(let x=h.x;x<h.x+h.w;x+=22)rr(x,h.y+Math.sin(t*3+x)*2,12,3,'#d0ff90');break;
   case 'void':rr(h.x,h.y,h.w,h.h,'#05060c');break;
   case 'spike':tile('el-spike',1,0,h.x,h.y+h.h-22,h.w,22)||rr(h.x,h.y,h.w,h.h,'#dde');break;
   case 'thorn':tile('el-thorn',1,0,h.x,h.y+h.h-22,h.w,22)||rr(h.x,h.y,h.w,h.h,'#c48');break;
   case 'elec':if(h.column){if(h.active)vtile('el-laser',1,0,h.x+h.w/2-10,h.y,20,h.h);else if(warn)rr(h.x+h.w/2-1,h.y,2,h.h,'#a8e8ff');cell('el-turret',5,0,h.x+h.w/2-15,h.y-26,31,31);}
    else if(h.active)tile('el-elec',5,Math.floor(t*12),h.x,h.y+h.h-18,h.w,18);else rr(h.x,h.y+h.h-3,h.w,3,warn?'#a8e8ff':'#2a4a66');break;
   case 'laser':if(h.active){ctx.globalAlpha=.9;ctx.filter='hue-rotate(150deg) saturate(1.6)';vtile('el-laser',1,0,h.x+h.w/2-10,h.y,20,h.h);ctx.filter='none';ctx.globalAlpha=1;}else if(warn)rr(h.x+h.w/2-1,h.y,2,h.h,'#ff9aa0');cell('el-turret',5,2,h.x+h.w/2-15,h.y-24,31,31);break;
   case 'fire':case 'steam':if(h.active){rr(h.x,h.y,h.w,h.h,h.type==='fire'?'#ff9a3c99':'#ffffff66');for(let k=0;k<3;k++)cell('el-fireball',3,(k+Math.floor(t*10))%3,h.x+h.w/2-14,h.y+((t*240+k*h.h/3)%h.h)-14,28,28);}else rr(h.x,h.y+h.h-6,h.w,6,warn?'#ffe0a0':'#6a4a3a');break;
   case 'trash':rr(h.x,h.y,h.w,h.h,'#7a6c58');for(let y=h.y;y<h.y+h.h;y+=12)rr(h.x,y,h.w,4,'#e0b030');break;
   default:rr(h.x,h.y,h.w,h.h,'#ff60a0aa');}}
 for(const m of D.mines)if(vis(m.x,m.y,m.w,m.h)){const cx=m.x+m.w/2,cy=m.y+m.h/2;if(m.armed)cell('el-mine',6,Math.floor(t*6),cx-16,cy-16,32,32);else if(m.back>3.4){const k=Math.min(4,Math.floor((4-m.back)/.12));cell('el-explode',5,k,cx-40,cy-40,80,80);}}
 for(const q of D.turrets)if(q.hp>0&&vis(q.x,q.y,32,32))cell('el-turret',5,Math.floor(t*5),q.x,q.y,31,31);
 for(const w of world.walls)if(!w.dead&&vis(w.x,w.y,w.w,w.h)){
  if(w.type==='gate')vtile('el-gate',1,0,w.x+w.w/2-16,w.y,32,w.h);
  else if(w.type==='orbgate'){vtile('el-orbgate',1,0,w.x+w.w/2-20,w.y,40,w.h);text((D.orbGot||0)+'/'+D.orbs,w.x+w.w/2-camera.x,w.y-8-camera.y,12,'#ffe080','center');}
  else if(w.type==='steel')vtile('el-wall-steel',1,0,w.x,w.y,w.w,w.h);
  else if(w.type==='stone')vtile('el-wall-stone',1,0,w.x-8,w.y,w.w+16,w.h);
  else if(w.type==='laser'){ctx.filter='hue-rotate(150deg) saturate(1.6)';vtile('el-laser',1,0,w.x+w.w/2-10,w.y,20,w.h);ctx.filter='none';}}
 for(const sw of world.switches)if(vis(sw.x,sw.y,40,40))cell('el-switch',3,sw.on?2:Math.floor(t*4)%2,sw.x-4,sw.y-6,40,50);
 for(const po of world.portals)if(vis(po.x,po.y,po.w,po.h)){cell('el-teleporter',3,Math.floor(t*8),po.x+po.w/2-21,po.y+po.h-72,42,72);if(Math.abs(p.x-po.x)<140)text('E',po.x+po.w/2-camera.x,po.y-14-camera.y,12,'#bfe8ff','center');}
 for(const z of D.zones){if(!vis(z.x,z.y,z.w,z.h))continue;
  if(z.type==='rain'&&z.raining){ctx.globalAlpha=.55;for(let i=0;i<z.w*z.h/2500;i++){const u=(i*71.3+t*60)%z.w,v=(i*37.9+t*620)%z.h;line(z.x+u-camera.x,z.y+v-camera.y,z.x+u-6-camera.x,z.y+v+14-camera.y,'#a8f070',1);}ctx.globalAlpha=1;}
  else if(z.type==='alarm'){const b=z.beam??z.x+z.w/2;ctx.globalAlpha=z.alert>0?.35:.2;polygon([[b-6-camera.x,z.y+30-camera.y],[b+6-camera.x,z.y+30-camera.y],[b+T*1.4-camera.x,z.y+z.h-camera.y],[b-T*1.4-camera.x,z.y+z.h-camera.y]],z.alert>0?'#ff5060':'#fff0b0');ctx.globalAlpha=1;cell('el-probe',3,Math.floor(t*6),b-15,z.y-4,29,60);}
  else if(z.type==='dark'){const g=ctx.createRadialGradient(p.x+p.w/2-camera.x,p.y+p.h/2-camera.y,40,p.x+p.w/2-camera.x,p.y+p.h/2-camera.y,8*T);g.addColorStop(0,'rgba(0,0,0,0)');g.addColorStop(1,'rgba(4,2,10,.88)');ctx.save();ctx.beginPath();ctx.rect(z.x-camera.x,z.y-camera.y,z.w,z.h);ctx.clip();ctx.fillStyle=g;ctx.fillRect(z.x-camera.x,z.y-camera.y,z.w,z.h);ctx.restore();}
  else if(z.type==='elec'&&cyc(t,1.5,1.5,0))tile('el-elec',3,Math.floor(t*14),z.x,z.y+z.h-16,z.w,16);}
 if(D.orbs&&p.vehicle==='chaser')text('QUẢ NĂNG LƯỢNG '+(world.items.filter(i=>i.type==='orb'&&i.got).length)+'/'+D.orbs,480,90,13,'#ffe080','center');}
function drawPlatform(pl){const D=world.data;if(pl.kind==='datalayer'){pl.layer==='back'?back():front();return;}
 if(pl.broken||pl.ghost)return;const x=pl.x-camera.x,y=pl.y-camera.y;if(x>1000||x+pl.w<-40||y>580||y+pl.h<-40)return;
 const shake=pl.shake?Math.sin(time*60)*2:0,th=D.theme,t=D.t;
 if(pl.kind==='phase'){const on=stablePlatform(pl),n=pl.phase?'el-holob':'el-holo';if(!tile(n,2,on?0:1,pl.x,pl.y,pl.w,18,on?1:.4))rect(x,y,pl.w,12,on?'#80d0ff':'#80d0ff44');return;}
 if(pl.kind==='lift'){cell('el-thruster',3,Math.floor(t*12),pl.x,pl.y-2,pl.w,36*pl.w/46)||rect(x,y,pl.w,16,'#ffc860');return;}
 if(pl.kind==='ledge'){if(pl.style==='bounce'){cell('el-bounce',1,0,pl.x-4,pl.y-10,pl.w+8,pl.w*.5)||rect(x,y,pl.w,16,'#ff8cdc');return;}
  if(pl.style==='break'){if(tile('el-crumble',1,0,pl.x+shake,pl.y-2,pl.w,22))return;}
  if(pl.move){if(tile('el-platform',1,0,pl.x,pl.y-2,pl.w,20))return;}
  if(!strip('native-deck',pl.x+shake,pl.y-2,pl.w,18,0,40))rect(x+shake,y,pl.w,pl.h,'#c8aa78');
  if(pl.safe)rect(x+shake,y+14,pl.w,4,'#4fd08a');if(pl.move)text('↔',x+pl.w/2,y-4,10,'#9fe6ff','center');
  if(pl.style==='break'){ctx.globalAlpha=.55;rect(x+shake,y,pl.w,16,'#b07a4a');ctx.globalAlpha=1;for(let i=10;i<pl.w;i+=26)line(x+shake+i,y+2,x+shake+i+8,y+14,'#2a1a14',2);}return;}
 if(pl.gate){if(!vtile('el-gate',1,0,pl.x+pl.w/2-16,pl.y,32,pl.h)){rect(x,y,pl.w,pl.h,'#d24a5a');}return;}
 if(pl.area===2){wfill(pl.x+shake,pl.y,pl.w,pl.h,'native-panel','#4e5462');ctx.globalAlpha=.45;rect(x+shake,y,pl.w,pl.h,'#141824');ctx.globalAlpha=1;if(!pl.under)strip('native-deck',pl.x+shake,pl.y-3,pl.w,14,0,30);}
 else{wfill(pl.x+shake,pl.y,pl.w,pl.h,'terrain-'+th,'#5c4a40');if(!pl.under)strip('cap-'+th,pl.x+shake,pl.y-6,pl.w,24)||rect(x,y,pl.w,3,'#a08a70');}}
function camY(){const D=world.data,cx=p.x+p.w/2,cy=p.y+p.h/2;const r=D.rooms.filter(r=>cx>=r.x*T&&cx<(r.x+r.w)*T&&cy>=r.y*T&&cy<(r.y+r.h)*T).sort((a,b)=>a.w*a.h-b.w*b.h)[0];
 if(!r)return clamp(p.y-300,0,world.height-540);const top=r.y*T,bot=(r.y+r.h)*T;if(bot-top<=540)return clamp(bot-540,0,world.height-540);return clamp(p.y-300,top,bot-540);}

// ---------- móc vào game ----------
const baseBuild=buildWorld;buildWorld=function(id){const L=DATA()[id];if(L&&id!=='x5_dinorex'){const s=STAGES.find(s=>s.id===id);return build(s,L);}return baseBuild(id);};
const baseBefore=blueprintBefore;blueprintBefore=function(dt){const r=baseBefore(dt);if(world&&world.data&&p)before();return r;};
const baseAfter=blueprintAfter;blueprintAfter=function(dt){baseAfter(dt);if(world&&world.data&&p)update(dt);};
const baseItem=itemDraw;itemDraw=function(it){if(it.type==='orb'&&world&&world.data){if(!it.got)cell('el-orb',4,Math.floor(time*8),it.x-6,it.y-4,28,26);return;}return baseItem(it);};
const basePD=platformDraw;platformDraw=function(pl){if(world&&world.data)return drawPlatform(pl);return basePD(pl);};
for(const id of Object.keys(DATA())){const st=STAGES.find(s=>s.id===id);if(st&&DATA()[id].name)st.tag='BẢN DỰNG MỚI · '+DATA()[id].name+' (dữ liệu từ kịch bản thiết kế)';}
window.LEVEL_RUNTIME={build,DATA};
})();
