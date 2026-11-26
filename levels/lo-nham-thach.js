// Prototype stage "Lò Nham Thạch" (replaces x5_dinorex terrain). Grey-box build:
// every surface is a flat colour block so the layout can be play-tested before art.
// Units below are 32px tiles; the builder converts them to world pixels.
(function(){
const T=32,ID='x5_dinorex';
const COL={rock:'#5c4034',rockTop:'#8a6450',steel:'#4e5462',steelTop:'#7a8294',ledge:'#c8aa78',crumble:'#b07a4a',safe:'#4fd08a',
 cart:'#9a7a58',gate:'#d24a5a',cracked:'#8f7b6a',lava:'#ff6e1e',lavaTop:'#ffd27a',vent:'#ffb03c',press:'#9aa0b4'};
const ROOMS=[['R1 BÃI ĐÁP',0,30,60,60,'#2a1c1e'],['R2 SƯỜN ĐÁ LĂN',60,30,140,62,'#2c1e1e'],['R3 GIẾNG THÔNG HƠI',140,6,160,62,'#2e2022'],
 ['R4 ĐƯỜNG RAY QUẶNG',160,3,230,24,'#301e1c'],['MINI-BOSS',230,3,260,24,'#3a1a24'],['R5 LÒ ÉP',260,4,304,24,'#22262e'],
 ['R6 GIẾNG NHAM DÂNG',302,4,334,76,'#341c1a'],['R7 KÊNH XỈ',334,4,394,24,'#24242e'],['R8 CỔNG',394,4,424,24,'#24242e'],['BOSS',424,4,454,24,'#3c1a22']];

function build(s){
 const W={width:454*T,height:78*T,floor:18*T,platforms:[],hazards:[],enemies:[],bullets:[],particles:[],items:[],checkpoints:[{x:3*T,y:52*T},{x:162*T,y:14*T},{x:337*T,y:16*T}],
  boss:null,zones:[],walls:[],switches:[],vehicles:[],portals:[],searchlights:[],subs:[],gravityScale:1,warning:0,ready:1.2,clock:0,elapsed:0,damage:0,rush:0,
  camY,proto:{rooms:ROOMS,slopes:[],lava:[],vents:[],falls:[],presses:[],boulders:[],carts:[],crumbles:[],riser:null,cracked:[],gate:null,t:0},
  bossGate:424*T+40,areaMarks:[230*T,260*T]};
 const P=W.proto;
 W.platforms.push({x:-99999,y:-99999,w:0,h:0,kind:'proto',layer:'back'});
 const solid=(x0,y0,x1,y1,area='rock',extra={})=>{const pl={x:x0*T,y:y0*T,w:(x1-x0)*T,h:(y1-y0)*T,kind:'ground',area,...extra};W.platforms.push(pl);return pl;};
 const ledge=(x,y,w,extra={})=>{const pl={x:x*T,y:y*T,w:w*T,h:16,kind:'ledge',baseX:x*T,baseY:y*T,move:0,...extra};W.platforms.push(pl);return pl;};
 // Walkable slope: a one-way surface plus solid columns kept just under it.
 const slope=(x0,y0,x1,y1,bottom,area='rock')=>{P.slopes.push({x0:x0*T,y0:y0*T,x1:x1*T,y1:y1*T,area,bottom:bottom*T});
  for(let x=x0;x<x1;x++){const ya=y0+(y1-y0)*(x-x0)/(x1-x0),yb=y0+(y1-y0)*(x+1-x0)/(x1-x0);solid(x,Math.max(ya,yb)+.45,x+1,bottom,area,{under:true});}};
 const lava=(x0,y0,x1,y1,mode='bounce')=>P.lava.push({x:x0*T,y:y0*T,w:(x1-x0)*T,h:(y1-y0)*T,mode,baseX:x0*T,baseW:(x1-x0)*T});
 const enemy=(type,x,y)=>{const e={x:x*T,y:y*T-48-(type==='drone'?0:0),w:32,h:48,type,max:10+Math.floor(s.index/4),hp:10+Math.floor(s.index/4),cool:1+Math.random(),inv:0,t:Math.random()*3,dir:-1,dead:false};e.startX=e.x;e.startY=e.y;W.enemies.push(e);};
 let rq=0;const rescue=(x,y)=>{const j=rq++;W.items.push({id:ID+':reploid:'+j,x:x*T,y:y*T-48,w:32,h:48,type:'rescue',variant:j%6,got:save.rescues.includes(ID+':reploid:'+j)});};

 // ---------- AREA 1 · R1 Bãi đáp ----------
 solid(-1,20,0,60);solid(0,52,18,60);slope(18,52,26,49,60);solid(26,49,34,60);
 solid(34,58,38,60);lava(34,55,38,58);solid(38,50,50,60);solid(50,52,60,60);
 ledge(29,44,4);enemy('sniper',30,49);enemy('sniper',45,50);enemy('drone',40,44);rescue(55,52);
 // ---------- R2 Sườn đá lăn ----------
 const ly=x=>52+(x-70)*6/50;
 solid(60,52,70,62);slope(70,52,87,ly(87),62);solid(87,ly(87)+3,90,62);slope(90,ly(90),103,ly(103),62);
 solid(103,ly(103)+2.6,106,62);slope(106,ly(106),120,58,62);solid(120,58,140,62);
 for(const [x,y,w] of [[74,44,5],[84,40,4],[96,37,4],[108,34,6]])ledge(x,y,w);
 W.items.push({id:ID+':heart',type:'relic',x:110.5*T,y:34*T-34,w:28,h:28,got:save.relics.includes(ID+':heart')});
 P.boulderLine={x0:70*T,x1:139*T,y:x=>(x<120*T?ly(x/T):58)*T};P.boulderTimer=1;
 enemy('brute',127,58);enemy('sniper',64,52);
 // ---------- R3 Giếng thông hơi (wall-kick shaft) ----------
 solid(140,6,160,8);solid(140,8,142,54);solid(158,14,160,58);solid(140,58,160,62);
 [['L',50],['R',44],['L',38],['R',32],['L',26],['R',20]].forEach(([sd,y],i)=>P.vents.push({x:(sd==='L'?142:154)*T,y:y*T,w:4*T,h:1.4*T,on:1.2,off:1.6,phase:i*.55,dir:sd==='L'?1:-1}));
 for(const [x,y,w] of [[146,46,3],[150,34,3],[146,22,3]])ledge(x,y,w);
 // ---------- R4 Đường ray quặng ----------
 solid(160,3,230,4);solid(160,14,168,24);solid(168,22,222,24);lava(168,20,222,22);
 solid(184,16,187,22);solid(204,16,207,22);solid(222,14,230,24);
 for(let i=0;i<4;i++){const c=ledge(164+i*15.5,12,4,{cart:true,area:'cart'});P.carts.push(c);}
 P.cartSpan=[160*T,226*T];P.cartSpeed=110;
 enemy('drone',180,9);enemy('drone',195,8);enemy('drone',211,9);
 ledge(195,18.6,4);W.items.push({id:ID+':tank',type:'tank',x:196.6*T,y:18.6*T-30,w:25,h:30,got:false});
 // ---------- Mini-boss: arena + gate ----------
 solid(230,3,260,4);solid(230,16,260,24);
 P.gate=solid(258,4,260,16,'gate',{gate:true});
 W.subs.push({id:'donut',x:242*T,y:9*T,w:110,h:110,hp:45,max:45,inv:0,cool:1.4,dead:false});
 // ---------- AREA 2 · R5 Lò ép ----------
 solid(260,4,312,6,'steel');const belt=solid(260,18,304,24,'steel',{belt:-120});P.belt=belt;
 [270,278,286,294].forEach((x,i)=>P.presses.push({x:x*T,top:6*T,w:4*T,low:16.2*T,phase:i*.45,y:6*T}));
 enemy('sniper',291,18);rescue(282,18);
 for(let x=304;x<312;x+=2)P.crumbles.push({pl:solid(x,18,x+2,19,'steel',{crumble:true}),delay:.5,respawn:5});
 solid(312,6,313,18,'steel');
 // ---------- R6 Giếng nham dâng (rising lava climb) ----------
 solid(302,19,304,76);solid(332,16,334,76);solid(304,72,332,76);
 const R6=[[308,66,4,'safe0'],[322,60,4,'c'],[310,54,4,'safe'],[324,48,4,'c'],[308,42,4,'safe'],[322,36,4,'c'],[310,30,4,''],[324,24,4,'c'],[318,18,6,'']];
 for(const [x,y,w,t] of R6){const pl=ledge(x,y,w,{area:t==='safe'?'safe':t==='c'?'crumble':'ledge'});if(t==='c')P.crumbles.push({pl,delay:.4,respawn:3});if(t==='safe')pl.safe=true;}
 P.riser={x:304*T,w:28*T,bottom:74*T,top:74*T,stop:19.5*T,active:false,pause:0};
 enemy('drone',306,38);enemy('drone',327,28);
 // ---------- R7 Kênh xỉ ----------
 solid(334,4,394,6,'steel');solid(334,16,380,24,'steel');solid(380,22,384,24,'steel');lava(380,19,384,22);solid(384,16,388,24,'steel');solid(390,16,394,24,'steel');
 const crack=solid(388,16,390,17,'cracked',{cracked:true});P.cracked.push(crack);
 solid(386,19,394,20,'steel');solid(386,20,394,24,'steel');
 W.items.push({id:ID+':gaea:arm',type:'capsule',armor:'gaea',part:'arm',x:391.2*T,y:19*T-70,w:44,h:70,got:(save.parts.gaea||[]).includes('arm')});
 [346,358,370].forEach((x,i)=>P.falls.push({x:x*T,y:6*T,w:2*T,h:10*T,on:1.5,off:1.5,phase:i*.9}));
 P.vents.push({x:352*T,y:12*T,w:1.6*T,h:4*T,on:1.0,off:1.4,phase:0,dir:0,hp:6,turret:true,label:'up'});
 P.vents.push({x:366*T,y:6*T,w:1.6*T,h:4*T,on:1.0,off:1.4,phase:.7,dir:0,hp:6,turret:true,label:'down'});
 rescue(364,16);enemy('drone',375,10);
 // ---------- R8 Cổng + BOSS ----------
 solid(394,4,424,6,'steel');solid(394,16,424,24,'steel');rescue(404,16);
 solid(424,18,454,24);lava(424,17,427,18,'boss');lava(451,17,454,18,'boss');P.bossLava=P.lava.slice(-2);
 W.platforms.push({x:-99999,y:-99999,w:0,h:0,kind:'proto',layer:'front'});
 W.boss={x:W.width-250,y:W.floor-120,w:80,h:120,vx:0,vy:0,dir:-1,max:140+s.index*5,hp:140+s.index*5,inv:0,t:0,state:0,action:0,attackAt:1.2,slow:0};
 return W;
}

const cyc=(t,on,off,ph)=>((t+ph)%(on+off))<on;
const onTop=pl=>p.ground&&Math.abs(p.y+p.h-pl.y)<4&&p.x+p.w>pl.x&&p.x<pl.x+pl.w;
function kill(){p.inv=0;hurt(999);}
function protoUpdate(dt){const P=world.proto;if(!P||!p||p.hp<=0)return;P.t+=dt;const t=P.t;
 // reverse conveyor in R5 (stops at its left edge so it never pushes into the step)
 if(P.belt&&onTop(P.belt)&&p.x>P.belt.x+6)p.x=Math.max(P.belt.x+6,p.x+P.belt.belt*dt);
 // slopes: snap feet to the surface while descending/walking
 const cx=p.x+p.w/2;for(const s of P.slopes){if(cx<s.x0||cx>s.x1)continue;const sy=s.y0+(s.y1-s.y0)*(cx-s.x0)/(s.x1-s.x0),feet=p.y+p.h;if(p.vy>=0&&feet>=sy-6&&feet<=sy+26){p.y=sy-p.h;p.vy=0;p.ground=true;p.airDash=true;}}
 // static lava: hurt + bounce out; boss lava widens in phase 2
 if(bossActive&&world.boss&&world.boss.hp<world.boss.max*.5&&P.bossLava){P.bossLava[0].w=4*T;P.bossLava[1].x=450*T;P.bossLava[1].w=4*T;}
 for(const L of P.lava){if(p.x+p.w>L.x&&p.x<L.x+L.w&&p.y+p.h>L.y+4){if(p.inv<=0){hurt(6);}p.vy=-720;p.ground=false;}}
 // vents / turrets / lava falls
 for(const v of P.vents){if(v.hp!=null&&v.hp<=0)continue;v.active=cyc(t,v.on,v.off,v.phase);
  if(v.hp!=null)for(const b of world.bullets)if(!b.enemy&&overlap(b,{x:v.label==='up'?v.x:v.x,y:v.label==='up'?v.y+v.h-24:v.y,w:v.w,h:24})){v.hp-=b.power===2?6:b.power?3:1;b.life=0;if(v.hp<=0)particle(v.x+v.w/2,v.y+v.h/2,'#ffd27a',20,160);}
  if(v.active&&overlap(p,v))hurt(4,(v.dir||(p.x<v.x+v.w/2?-1:1))*200);}
 for(const f of P.falls){f.active=cyc(t,f.on,f.off,f.phase);if(f.active&&overlap(p,f))hurt(5);}
 // presses: wait 1.4s, slam .25s, lift .6s
 for(const q of P.presses){const c=(t+q.phase)%2.25;q.y=c<1.4?q.top:c<1.65?q.top+(q.low-q.top)*((c-1.4)/.25):q.low-(q.low-q.top)*((c-1.65)/.6);
  const box={x:q.x,y:q.top,w:q.w,h:q.y-q.top+28};if(overlap(p,box)){if(c>=1.4&&c<1.75&&p.ground)kill();else{p.x=p.x+p.w/2<q.x+q.w/2?q.x-p.w:q.x+q.w;}}}
 // rolling boulders in R2
 if(P.boulderLine){P.boulderTimer-=dt;if(P.boulderTimer<=0&&p.x>60*T&&p.x<140*T){P.boulderTimer=2.2;P.boulders.push({x:P.boulderLine.x0,v:120,r:22});}
  for(const b of P.boulders){b.v=Math.min(330,b.v+dt*90);b.x+=b.v*dt;b.y=P.boulderLine.y(b.x)-b.r;if(Math.hypot(p.x+p.w/2-b.x,p.y+p.h/2-b.y)<b.r+18)hurt(5,220);}
  P.boulders=P.boulders.filter(b=>{if(b.x>P.boulderLine.x1){particle(b.x,b.y,'#c09070',14,140);return false;}return true;});}
 // ore carts loop along the rail and carry the player
 for(const c of P.carts){const ride=onTop(c),dx=P.cartSpeed*dt;c.x+=dx;if(c.x>P.cartSpan[1])c.x=P.cartSpan[0];if(ride)p.x+=dx;}
 // crumbling floors
 for(const k of P.crumbles){const pl=k.pl;if(pl.broken){k.back=(k.back||0)-dt;if(k.back<=0){pl.broken=false;k.timer=null;}continue;}
  if(k.timer==null&&onTop(pl))k.timer=k.delay;if(k.timer!=null){k.timer-=dt;pl.shake=k.timer>0;if(k.timer<=0){pl.broken=true;k.back=k.respawn;k.timer=null;particle(pl.x+pl.w/2,pl.y,'#c09070',10,120);}}}
 // cracked floor over the Gaea capsule: needs a full-charge shot
 for(const pl of P.cracked)if(!pl.broken)for(const b of world.bullets)if(!b.enemy&&b.power===2&&overlap(b,{x:pl.x,y:pl.y-40,w:pl.w,h:pl.h+40})){pl.broken=true;b.life=0;particle(pl.x+pl.w/2,pl.y,'#d8c0a0',24,180);toast('TƯỜNG NỨT ĐÃ VỠ',1.4);}
 // mini-boss gate opens when the sub-boss is down
 if(P.gate&&!P.gate.broken&&world.subs.every(s=>s.dead)){P.gate.broken=true;toast('CỔNG AREA 2 ĐÃ MỞ',1.6);}
 // rising lava shaft (R6)
 const R=P.riser;if(R){const inShaft=p.x+p.w>R.x&&p.x<R.x+R.w&&p.y>20*T;
  if(!R.active&&inShaft&&p.y>60*T){R.active=true;R.top=R.bottom+2*T;R.pause=1.5;toast('WARNING · NHAM ĐANG DÂNG',1.8);}
  if(R.active){const safe=world.platforms.find(pl=>pl.safe&&!pl.used&&onTop(pl));if(safe){safe.used=true;R.pause=2;}
   if(R.pause>0)R.pause-=dt;else R.top=Math.max(R.stop,R.top-(R.top<40*T?75:55)*dt);
   if(inShaft&&p.y+p.h>R.top+8)kill();
   if(!inShaft&&p.x>334*T){R.active=false;}}
  if(!inShaft&&p.x<304*T){R.active=false;R.top=R.bottom;for(const pl of world.platforms)if(pl.safe)pl.used=false;}}
}
function unstick(){for(const pl of world.platforms){if(pl.kind!=='ground'||pl.broken||!overlap(p,pl))continue;
  const l=p.x+p.w-pl.x,r=pl.x+pl.w-p.x,u=p.y+p.h-pl.y,d=pl.y+pl.h-p.y,m=Math.min(l,r,u,d);
  if(m===u){p.y=pl.y-p.h;p.vy=Math.min(0,p.vy);p.ground=true;}else if(m===l)p.x=pl.x-p.w;else if(m===r)p.x=pl.x+pl.w;else{p.y=pl.y+pl.h;p.vy=Math.max(0,p.vy);}}}
function rr(x,y,w,h,c){rect(x-camera.x,y-camera.y,w,h,c);}
function protoBack(){const P=world.proto;for(const [n,x0,y0,x1,y1,c] of P.rooms){rr(x0*T,y0*T,(x1-x0)*T,(y1-y0)*T,c+'d0');text(n,x0*T+10-camera.x,y0*T+22-camera.y,11,'#ffe3a0aa','left');}
 for(const s of P.slopes){const col=COL[s.area]||COL.rock;polygon([[s.x0-camera.x,s.y0-camera.y],[s.x1-camera.x,s.y1-camera.y],[s.x1-camera.x,s.bottom-camera.y],[s.x0-camera.x,s.bottom-camera.y]],col);line(s.x0-camera.x,s.y0-camera.y,s.x1-camera.x,s.y1-camera.y,COL.rockTop,3);}
 line(160*T-camera.x,12*T-camera.y,226*T-camera.x,12*T-camera.y,'#9a9aa6',2);}
function protoFront(){const P=world.proto,t=P.t;
 for(const L of P.lava){rr(L.x,L.y,L.w,L.h,COL.lava);for(let x=L.x;x<L.x+L.w;x+=24)rr(x,L.y+Math.sin(t*4+x)*2,14,3,COL.lavaTop);}
 for(const v of P.vents){if(v.hp!=null&&v.hp<=0){rr(v.x,v.label==='up'?v.y+v.h-14:v.y,v.w,14,'#3a3a3a');continue;}
  if(v.turret)rr(v.x,v.label==='up'?v.y+v.h-14:v.y,v.w,14,'#c86a2a');
  else rr(v.dir>0?v.x-10:v.x+v.w,v.y+6,10,v.h-12,'#6a5a50');
  if(v.active){ctx.globalAlpha=.75;rr(v.x,v.y,v.w,v.h,COL.vent);ctx.globalAlpha=1;}else if(((t+v.phase)%(v.on+v.off))>v.on+v.off-.45){ctx.globalAlpha=.35;rr(v.x,v.y,v.w,v.h,'#ffe0a0');ctx.globalAlpha=1;}}
 for(const f of P.falls){if(f.active){rr(f.x,f.y,f.w,f.h,COL.lava);rr(f.x+6,f.y,6,f.h,COL.lavaTop);}else{rr(f.x,f.y,f.w,10,'#ff8a3a');if(((t+f.phase)%(f.on+f.off))>f.on+f.off-.45)rr(f.x+f.w/2-3,f.y+10,6,30,'#ffd27a88');}}
 for(const q of P.presses){rr(q.x+q.w/2-6,q.top,12,q.y-q.top,'#5a5e6a');rr(q.x,q.y,q.w,28,COL.press);rr(q.x,q.y+24,q.w,4,'#ff5a5a');}
 for(const b of P.boulders){ctx.fillStyle='#8a6a52';ctx.beginPath();ctx.arc(b.x-camera.x,b.y-camera.y,b.r,0,Math.PI*2);ctx.fill();ctx.strokeStyle='#c8a080';ctx.lineWidth=2;ctx.stroke();}
 const R=P.riser;if(R&&R.active){rr(R.x,R.top,R.w,R.bottom+2*T-R.top,COL.lava+'e8');for(let x=R.x;x<R.x+R.w;x+=26)rr(x,R.top+Math.sin(t*5+x)*3,16,4,COL.lavaTop);}
}
const basePD=platformDraw;
platformDraw=function(pl){if(!world.proto)return basePD(pl);
 if(pl.kind==='proto'){pl.layer==='back'?protoBack():protoFront();return;}
 if(pl.broken)return;const x=pl.x-camera.x,y=pl.y-camera.y;if(x>1000||x+pl.w<-40||y>560||y+pl.h<-40)return;
 const shake=pl.shake?Math.sin(time*60)*2:0;
 if(pl.kind==='ledge'){const c=pl.cart?COL.cart:pl.area==='safe'?(pl.used?'#2f7a54':COL.safe):pl.area==='crumble'?COL.crumble:COL.ledge;rect(x+shake,y,pl.w,pl.cart?1.6*T:pl.h,c);rect(x+shake,y,pl.w,3,'#ffffff55');if(pl.cart){rect(x+8,y+1.6*T-6,12,12,'#333');rect(x+pl.w-20,y+1.6*T-6,12,12,'#333');}return;}
 const c=pl.area==='gate'?COL.gate:pl.area==='cracked'?COL.cracked:COL[pl.area]||COL.rock;rect(x+shake,y,pl.w,pl.h,c);
 if(!pl.under)rect(x+shake,y,pl.w,3,pl.area==='steel'?COL.steelTop:COL.rockTop);
 if(pl.cracked){for(let i=8;i<pl.w;i+=16)line(x+i,y+2,x+i+6,y+pl.h-2,'#3a2a20',2);}
 if(pl.belt){for(let i=((time*120)%24);i<pl.w;i+=24)text('←',x+pl.w-i,y+18,12,'#ffd27a','center');}
 if(pl.crumble){line(x+4,y+4,x+pl.w-4,y+pl.h-2,'#2a1a14',1);}};
function camY(){const cx=p.x+p.w/2,cy=p.y+p.h/2;let r=world.proto.rooms.filter(([n,x0,y0,x1,y1])=>cx>=x0*T&&cx<x1*T&&cy>=y0*T&&cy<y1*T).sort((a,b)=>(a[3]-a[1])*(a[4]-a[2])-(b[3]-b[1])*(b[4]-b[2]))[0];
 if(!r)return clamp(p.y-300,0,world.height-540);const top=r[2]*T,bot=r[4]*T;if(bot-top<=540)return clamp(bot-540,0,world.height-540);return clamp(p.y-300,top,bot-540);}
LEVELS_PROTO={};LEVELS_PROTO[ID]=build;
const st=STAGES.find(s=>s.id===ID);if(st){st.tag='MÀN MẪU · LÒ NHAM THẠCH: dốc đá lăn, giếng hơi nóng, xe quặng, lò ép, giếng nham dâng. Bản khối màu để chơi thử.';}
const baseBuild=buildWorld;buildWorld=function(id){const s=STAGES.find(s=>s.id===id);return LEVELS_PROTO[id]?LEVELS_PROTO[id](s):baseBuild(id);};
const baseAfter=blueprintAfter;blueprintAfter=function(dt){baseAfter(dt);if(world.proto&&p){protoUpdate(dt);unstick();}};
})();
var LEVELS_PROTO;
