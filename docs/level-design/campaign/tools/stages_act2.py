from stages_act1 import STAGES

STAGES['x6_turtloid'] = dict(
 title='Đền Inami', boss='Rainy Turtloid', theme='nature', act='Act II · X6',
 concept='Ngôi đền cổ dưới cơn mưa axit xanh: đứng ngoài mưa mất máu từ từ, 8 mái che trụ đá là điểm an toàn. Có lối rẽ Nightmare Zero.',
 refs='X6 Inami Temple (mưa axit), X4 Web Spider (rừng/đền), X8 Bamboo Pandamonium (lối phụ).',
 rooms=[
  ('R1','Cổng đền',50,18,'R',3,'Mưa axit bắt đầu; mái che đầu tiên dạy cách trú.','S D','mưa axit'),
  ('R2','Sân đá',70,20,'R',4,'Chạy giữa các mái che trụ đá; Nightmare Virus bay chậm.','D D R','mưa axit'),
  ('R3','Bậc đền',30,30,'U',4,'Leo bậc đá có mái hiên; bắn công tắc #1 mở cổng đền.','K S','mưa axit'),
  ('MID','Chính điện',30,17,'R',2,'Trong nhà, hết mưa; checkpoint.','C',''),
  ('R4','Mái đền',60,18,'R',5,'Đi trên mái tầng 2 X=3740: capsule Shadow Body phía trên Heart Tank.','D A H','mưa axit'),
  ('R5','Hành lang tượng',50,16,'R',4,'Tượng đá phun axit theo nhịp; cổng Alt Path dẫn tới Nightmare Zero.','S B R','axit phun'),
  ('R6','Hồ sen',30,16,'R',2,'Phòng nghỉ, Sub-Tank dưới mặt hồ, cửa boss.','T R',''),
  ('BOSS','Rainy Turtloid',30,17,'A',6,'Mưa axit trong đấu trường theo đợt; mai rùa phản đạn khi thu mình.','*','mưa axit'),
 ],
 secrets=[('Capsule Shadow Body','R4','Mái đền tầng cao.'),('Heart Tank','R4','Dưới mái, cạnh capsule.'),('Sub-Tank','R6','Dưới mặt hồ sen.'),('Alt Path Nightmare Zero','R5','Cổng tím cuối hành lang.')],
 newMech=['Mưa axit gây sát thương theo thời gian','Mái che an toàn'],
 art='terrain-nature, prop-nature, mmx6_totem_gate cho cổng, mưa vẽ bằng hạt.')

STAGES['x6_sheldon'] = dict(
 title='Viện Laser', boss='Shield Sheldon', theme='shadow', act='Act II · X6',
 concept='Viện nghiên cứu băng-laser: sàn kính trơn, tia laser phản xạ qua gương, tường giả giấu đường lên tầng trên.',
 refs='X6 Laser Institute, X5 Shining Firefly (gương), X4 Frost Walrus (sàn trơn).',
 rooms=[
  ('R1','Sảnh kính',50,16,'R',3,'Sàn kính trơn (gia tốc thấp), gương chiếu laser chéo.','S D','sàn trơn'),
  ('R2','Phòng gương',60,22,'R',4,'Đẩy hướng tia bằng cách bắn xoay gương để mở cửa X=2950.','K D R','laser gương'),
  ('R3','Hành lang trần gai',60,14,'R',5,'Trần gai thấp + sàn trơn: không được nhảy cao.','B','gai trần'),
  ('MID','Phòng làm lạnh',24,17,'R',2,'Checkpoint.','C',''),
  ('R4','Bệ kính cao',30,34,'U',5,'Leo bệ kính băng X=4380; tường giả đi xuyên được → Shadow Head.','D A','sàn trơn'),
  ('R5','Phòng thí nghiệm',50,16,'R',4,'Kính bảo vệ phản đạn; Heart Tank sau tấm kính phải bắn đạn nạp.','S S H T','laser'),
  ('BOSS','Shield Sheldon',30,17,'A',6,'Boss phản đạn bằng khiên; gương ở 4 góc khiến đạn dội lại.','*',''),
 ],
 secrets=[('Capsule Shadow Head','R4','Xuyên tường giả ở tầng trên.'),('Heart Tank','R5','Sau kính, cần đạn nạp đầy.'),('Sub-Tank','R5','Hốc trên kệ kính.')],
 newMech=['Tường giả đi xuyên được','Gương xoay bằng đạn'],
 art='native-ice cho sàn kính, mmx6_shieldsheldonplatforms cho bệ, X6ShelldonBG cho nền.')

STAGES['x6_mijinion'] = dict(
 title='Trung tâm vũ khí', boss='Infinity Mijinion', theme='metal', act='Act II · X6',
 concept='Trung tâm thử vũ khí ở Tây Úc. Siêu phi thuyền Illumina lượn trên đầu và khóa tâm ngắm vào người chơi. Giữa màn là vực với 7 bệ treo dây cáp.',
 refs='X6 Weapon Center (Illumina), X8 Dark Mantis (lẩn tránh), X3 Gravity Beetle (nhà máy vũ khí).',
 rooms=[
  ('R1','Bãi thử',60,16,'R',3,'Illumina lượn trên trời, vòng ngắm đỏ bám theo; đứng dưới mái che khi vòng chuyển đỏ đậm.','S D','tâm ngắm'),
  ('R2','Khu chứa',60,18,'R',4,'Thùng vũ khí phát nổ khi bị bắn (dùng để diệt Brute).','B S R','thùng nổ'),
  ('MID','Lõi cáp Illumina',30,17,'A',5,'Sub-boss: phá 3 lõi cáp Illumina. Checkpoint.','M C',''),
  ('R3','Vực dây cáp',80,24,'R',6,'7 bệ treo dây cáp đung đưa; bắn đứt dây → bệ rơi.','D D R','vực'),
  ('R4','Bệ cáp cuối',30,20,'R',4,'Capsule Blade Head trên bệ cuối.','A H',''),
  ('R5','Hầm thử nghiệm',40,16,'R',3,'Phòng nghỉ, Sub-Tank, cửa boss.','T R',''),
  ('BOSS','Infinity Mijinion',30,17,'A',6,'Boss nhân bản khi trúng đạn; diệt bản gốc bằng đạn nạp.','*',''),
 ],
 secrets=[('Capsule Blade Head','R4','Bệ cáp cuối Area 2.'),('Heart Tank','R4','Trên dây cáp cao nhất.'),('Sub-Tank','R5','Hầm thử nghiệm.')],
 newMech=['Vòng ngắm Illumina','Bệ treo cáp đung đưa','Thùng nổ'],
 art='terrain-metal, mmx6-platform cho bệ, native-deck, Illumina sprite có sẵn (sub illumina).')

STAGES['x6_yammark'] = dict(
 title='Khu Amazon', boss='Commander Yammark', theme='nature', act='Act II · X6',
 concept='Rừng mưa 2 tầng tách nhánh ở checkpoint giữa: nhánh trên (tán cây) có Blade Foot, nhánh dưới (hang) có Heart Tank.',
 refs='X6 Amazon Area, X4 Web Spider, X8 Bamboo Pandamonium (rẽ nhánh).',
 rooms=[
  ('R1','Bìa rừng mưa',60,18,'R',2,'Côn trùng máy bay theo đàn, cây gãy làm cầu.','D D S',''),
  ('R2','Bờ sông',60,18,'R',3,'Khúc gỗ trôi trên sông làm bệ di động.','D R','sông'),
  ('MID','Ngã ba',30,17,'R',2,'Checkpoint. Lối lên (tán cây) và lối xuống (hang).','C',''),
  ('R3a','Nhánh trên: tán cây',70,20,'R',5,'Lá lớn làm bệ nảy, gió lay cành; capsule Blade Foot X=4550.','D A','vực'),
  ('R3b','Nhánh dưới: hang',70,16,'R',4,'Hang tối, côn trùng phát sáng; Heart Tank cuối hang.','S B H','tối'),
  ('R4','Đền lá',30,16,'R',2,'Hai nhánh nhập lại; Sub-Tank, Reploid, cửa boss.','T R R',''),
  ('BOSS','Commander Yammark',30,17,'A',6,'Boss gọi 3 chuồn chuồn vệ tinh xoay quanh.','*',''),
 ],
 secrets=[('Capsule Blade Foot','R3a','Nhánh trên.'),('Heart Tank','R3b','Nhánh dưới.'),('Sub-Tank','R4','Đền lá.')],
 newMech=['Nhánh đường đi tách đôi','Khúc gỗ trôi'],
 art='terrain-nature, prop-nature, bg-nature; lá nảy dùng bounce zone có sẵn.')

STAGES['x6_shark'] = dict(
 title='Phòng thí nghiệm tái chế', boss='Metal Shark Player', theme='metal', act='Act II · X6',
 concept='Nhà máy tái chế phế liệu: 4 trần máy ép thủy lực, Ride Armor đục bãi rác, cuối màn là đường hầm tự cuộn bị tường ép đuổi.',
 refs='X6 Recycle Lab, X4 Split Mushroom (máy kẹp), X8 Earthrock Trilobite (bị đuổi).',
 rooms=[
  ('R1','Bãi phế liệu',60,16,'R',3,'Khối sắt rơi từ băng tải trên cao.','S D','khối rơi'),
  ('R2','Hành lang máy ép',70,16,'R',5,'4 trần máy ép thủy lực theo nhịp lệch pha, hốc an toàn giữa.','B D R','máy ép'),
  ('MID','Trạm Ride Armor',30,17,'R',2,'Checkpoint + Ride Armor Pod X=3240.','C V',''),
  ('R3','Bãi rác nén',60,18,'R',4,'Đục thủng 2 tường rác bằng Ride Armor; tường thứ 2 X=4950 giấu Shadow Foot.','A H','tường rác'),
  ('R4','Đường hầm ép',90,14,'R',6,'Tường ép đuổi từ trái (tự cuộn 120px/s); khối sắt chắn phải bắn vỡ.','D','tường ép'),
  ('R5','Lò nung',30,16,'R',2,'Phòng nghỉ, Sub-Tank, cửa boss.','T R',''),
  ('BOSS','Metal Shark Player',30,17,'A',6,'Boss lặn dưới nền phế liệu, khối sắt rơi từ trần.','*','khối rơi'),
 ],
 secrets=[('Capsule Shadow Foot','R3','Sau tường rác thứ 2.'),('Heart Tank','R3','Trên đống rác cao.'),('Sub-Tank','R5','Lò nung.')],
 newMech=['Tường ép đuổi tự cuộn','Tường rác phá bằng Ride Armor'],
 art='terrain-metal, mmx5_spikeplat cho máy ép, mmx6-block cho khối sắt, x6_catapiride cho Ride Armor.')

STAGES['x6_heatnix'] = dict(
 title='Khu dung nham', boss='Blaze Heatnix', theme='fire', act='Act II · X6',
 concept='Khu núi lửa hoạt động: 3 cỗ máy vòng lửa Nightmare Donut, bệ phản lực Thruster, cuối màn là trục leo dọc dung nham. Dùng lại bộ element màn Lò Nham Thạch nhưng nhịp khác.',
 refs='X6 Magma Area, X4 Magma Dragoon (nham dâng), màn mẫu Lò Nham Thạch.',
 rooms=[
  ('R1','Miệng hố',60,18,'R',3,'Mưa đá lửa nhỏ, hố nham. Dạy bệ Thruster đầu tiên.','S D','nham'),
  ('R2','Donut #1',40,18,'A',4,'Nightmare Donut #1 bắn vòng lửa; bệ Thruster ở hai bên.','M R',''),
  ('R3','Sông nham',70,18,'R',5,'Bệ đá trôi trên sông nham, cột lửa phun theo nhịp.','D D','nham'),
  ('MID','Hang mát',24,17,'R',2,'Checkpoint.','C',''),
  ('R4','Donut #2',40,18,'A',5,'Donut #2 + đá lăn.','M H',''),
  ('R5','Trục leo dung nham',24,50,'U',6,'Leo trục X=5250, nham dâng chậm; Donut #3 ở giữa trục. Shadow Arm ở đỉnh.','M A','nham dâng'),
  ('R6','Đỉnh núi',30,16,'R',2,'Phòng nghỉ, Sub-Tank, cửa boss.','T R',''),
  ('BOSS','Blaze Heatnix',30,17,'A',6,'Nham lấp nửa dưới đấu trường ở pha 2.','*','nham'),
 ],
 secrets=[('Capsule Shadow Arm','R5','Đỉnh trục leo dung nham.'),('Heart Tank','R4','Sau Donut #2.'),('Sub-Tank','R6','Đỉnh núi.')],
 newMech=['Bệ phản lực Thruster','Vòng lửa Donut'],
 art='Toàn bộ element màn Lò Nham Thạch (terrain-fire, lv-fireball, lv-crusher...), sub "donut" có sẵn.')

STAGES['x6_wolfang'] = dict(
 title='Bắc Cực', boss='Blizzard Wolfang', theme='ice', act='Act II · X6',
 concept='Area 1 là chặng Ride Chaser trượt dốc tuyết bị tuyết lở đuổi; Area 2 là vách băng cao, sàn trơn và băng rơi.',
 refs='X6 North Pole Area, X4 Frost Walrus, X8 Avalanche Yeti (bản demake làm lại thành màn chơi thường).',
 rooms=[
  ('R1','Trạm trượt',30,16,'R',1,'Lên Ride Chaser.','V',''),
  ('R2','Dốc tuyết lở',130,22,'D',5,'Ride Chaser xuống dốc dài; tuyết lở đuổi phía sau, nhảy qua khe băng, né cây thông đổ.','D D R','tuyết lở'),
  ('MID','Trạm khí tượng',24,17,'R',2,'Checkpoint, xuống xe.','C',''),
  ('R3','Vách băng cao',24,46,'U',5,'Bám tường băng X=3850 (trơn, trượt nhanh hơn); Blade Body ở hốc cao.','D A','băng rơi'),
  ('R4','Hồ băng',60,16,'R',4,'Sàn băng trơn, băng nhọn rơi từ trần theo nhịp; Heart Tank trên tảng băng trôi.','S B H','sàn trơn'),
  ('R5','Hang băng',30,16,'R',2,'Phòng nghỉ, Sub-Tank, cửa boss.','T R',''),
  ('BOSS','Blizzard Wolfang',30,17,'A',6,'Sàn đấu đóng băng dần (trơn), sói phóng băng.','*','sàn trơn'),
 ],
 secrets=[('Capsule Blade Body','R3','Vách băng cao.'),('Heart Tank','R4','Tảng băng trôi.'),('Sub-Tank','R5','Hang băng.')],
 newMech=['Tường băng trượt nhanh','Tuyết lở đuổi khi đang cưỡi Ride Chaser'],
 art='terrain-ice/cap-ice, native-ice, mmx6-ice, mmx6_invertediceblocks.')

STAGES['x6_scaravich'] = dict(
 title='Bảo tàng Trung tâm', boss='Ground Scaravich', theme='metal', act='Act II · X6',
 concept='Bảo tàng ban đêm: đèn pha an ninh quét, bị phát hiện thì cửa sập khóa phòng và gọi lính. Hai cụm phòng nối bằng 4 cổng dịch chuyển, cột Totem chặn ở giữa màn.',
 refs='X6 Central Museum, X8 Dark Mantis (lẩn tránh), X4 Bio Lab.',
 rooms=[
  ('R1','Sảnh trưng bày',60,18,'R',3,'Đèn pha quét đầu tiên; bị phát hiện → báo động + 2 Drone.','S D','đèn pha'),
  ('R2','Phòng hóa thạch',60,20,'R',4,'Đi trên khung xương khủng long; đèn pha quét chéo.','D R','đèn pha'),
  ('MID','Đại cột Totem',30,17,'A',5,'Phá cột Totem chặn đường; checkpoint.','M C',''),
  ('R3','Cụm phòng Cell 1',40,24,'R',4,'4 cổng dịch chuyển nối 2 cụm phòng; mỗi phòng 1 tủ trưng bày (Heart Tank ở một tủ).','D H','cổng'),
  ('R4','Cụm phòng Cell 2',40,24,'R',5,'Hốc cao Cell 2: capsule Blade Arm X=4840.','S A T','cổng'),
  ('R5','Kho lưu trữ',30,16,'R',2,'Phòng nghỉ, Reploid, cửa boss.','R R',''),
  ('BOSS','Ground Scaravich',30,17,'A',6,'Bọ hung lăn tảng đá khổng lồ; cổng dịch chuyển trong đấu trường.','*',''),
 ],
 secrets=[('Capsule Blade Arm','R4','Hốc cao Cell 2.'),('Heart Tank','R3','Tủ trưng bày Cell 1.'),('Sub-Tank','R4','Phòng cuối Cell 2.')],
 newMech=['Báo động khi bị đèn pha phát hiện','Cột Totem chặn đường'],
 art='terrain-metal, mmx6_totem_gate / mmx6_totem_exit, mmx6_probe_8201-u_type cho đèn pha, native-portal.')

STAGES['x6_f1_nzero'] = dict(
 title='Không gian ác mộng', boss='Nightmare Zero', theme='shadow', act='Phòng thí nghiệm Gate',
 concept='Không gian nhiễu tối: tầm nhìn bị thu hẹp quanh nhân vật, đèn quét tạo ảo ảnh (bệ giả), bệ nhấp nháy và đảo trọng lực.',
 refs='X6 Nightmare stages, X8 Dark Mantis (tối), X5 Zero Space 3.',
 rooms=[
  ('R1','Hành lang nhiễu',60,16,'R',5,'Tầm nhìn bán kính 220px; bệ ảo ảnh (viền nhấp nháy) không đứng được.','D','tối'),
  ('R2','Bệ nhấp nháy',70,22,'R',6,'Bệ đổi pha trên vực, đèn quét làm lộ bệ thật.','D S','vực'),
  ('MID','Điểm dừng',24,17,'R',2,'Checkpoint.','C',''),
  ('R3','Đảo trọng lực',60,20,'R',6,'Đi trên trần qua gai.','D','gai, đảo trọng lực'),
  ('BOSS','Nightmare Zero',30,17,'A',7,'Bản sao Zero dùng Genmu Zero; đánh bại để mở khóa Zero thật.','*',''),
 ],
 secrets=[], newMech=['Tầm nhìn hạn chế','Bệ ảo ảnh'],
 art='bg-shadow tối, mmx6_cyberblock, vòng tối vẽ bằng mặt nạ canvas.')

STAGES['x6_f2_nmother'] = dict(
 title='Phòng thí nghiệm Gate 1', boss='Nightmare Mother', theme='fire', act='Phòng thí nghiệm Gate',
 concept='Tầng 1 phòng thí nghiệm: biển gai với bệ di động, rồi trục leo dọc có dung nham dâng (khó hơn Lò Nham Thạch).',
 refs='X6 Gate Lab 1, X4 Magma Dragoon, màn mẫu Lò Nham Thạch (R6).',
 rooms=[
  ('R1','Biển gai',70,18,'R',6,'Bệ di động ngang/dọc trên sàn gai.','D D','gai'),
  ('R2','Bệ xoay',40,20,'R',6,'Bệ xoay quanh trục, gai ở cả trên và dưới.','D','gai'),
  ('MID','Điểm dừng',24,17,'R',2,'Checkpoint.','C',''),
  ('R3','Trục nham dâng',24,56,'U',7,'Dung nham dâng 70→90 px/s, không có kệ dừng; gai trên tường trái.','D S','nham dâng, gai'),
  ('BOSS','Nightmare Mother',30,17,'A',7,'Khối Nightmare lơ lửng, 4 lõi nguyên tố đổi màu.','*',''),
 ],
 secrets=[], newMech=['Bệ xoay quanh trục'],
 art='Element màn Lò Nham Thạch + native-panel.')

STAGES['x6_f3_highmax'] = dict(
 title='Phòng thí nghiệm Gate 2', boss='High Max', theme='core', act='Phòng thí nghiệm Gate',
 concept='Vực gai toàn khu vực, chuỗi bệ nhỏ có cột Totem chặn, băng chuyền laser.',
 refs='X6 Gate Lab 2, X5 Zero Space 2.',
 rooms=[
  ('R1','Bệ nhỏ',70,20,'R',6,'Bệ 2×1 ô trên vực gai; cột Totem trên bệ phải phá mới đứng được.','D','gai'),
  ('R2','Băng chuyền laser',60,16,'R',6,'Băng chuyền chạy nhanh dưới laser quét.','S D','laser'),
  ('MID','Điểm dừng',24,17,'R',2,'Checkpoint.','C',''),
  ('R3','Tháp totem',24,40,'U',7,'Leo giữa các totem bắn đạn.','D','gai'),
  ('BOSS','High Max',30,17,'A',7,'Khiên bất khả xâm phạm; dùng Charge Saber của Blade (giữ ↑ rồi thả) để làm choáng.','*',''),
 ],
 secrets=[], newMech=['Totem chặn bệ'],
 art='terrain-core, mmx6_totem_gate, fx-laser.')

STAGES['x6_f4_gate'] = dict(
 title='Phòng thí nghiệm Gate 3', boss='Gate', theme='core', act='Phòng thí nghiệm Gate',
 concept='Vùng đảo trọng lực giấu Secret Ultimate Armor trên trần biển gai; đấu trường Gate có vực thẳm giữa sàn.',
 refs='X6 Gate Lab 3, X5 Zero Space 3 (đảo trọng lực).',
 rooms=[
  ('R1','Biển gai trần',60,20,'R',6,'Vùng đảo trọng lực X=1150: đi trên trần; Secret Ultimate Armor X=1850.','D A','gai, đảo trọng lực'),
  ('R2','Hành lang tinh thể',60,16,'R',6,'Tinh thể Nightmare nổ khi bị bắn.','D S','gai'),
  ('MID','Điểm dừng',24,17,'R',2,'Checkpoint.','C',''),
  ('R3','Thang máy dữ liệu',24,40,'U',6,'Bệ nâng chậm, Drone bao quanh.','D D',''),
  ('BOSS','Gate',30,17,'A',8,'Sàn có vực giữa; Gate dùng quả cầu Nightmare.','*','vực'),
 ],
 secrets=[('Secret Ultimate Armor','R1','Trần biển gai trong vùng đảo trọng lực.')],
 newMech=['Tinh thể Nightmare nổ'],
 art='terrain-core, native-cyberblock.')

STAGES['x6_f5_bossrush'] = dict(
 title='Phòng thí nghiệm cuối', boss='8 boss → Hell Sigma', theme='core', act='Phòng thí nghiệm Gate',
 concept='Trục rơi đầy gai và băng chuyền dẫn tới trung tâm 8 cổng Boss Rush; xong 8 trận là Hell Sigma.',
 refs='X5/X6 Boss Rush, X4 Final Weapon.',
 rooms=[
  ('R1','Trục rơi',24,60,'D',7,'Rơi xuống, gai hai bên và gai nhô ra theo nhịp; lướt ngang để né.','D','gai'),
  ('R2','Băng chuyền đáy',60,16,'R',6,'Băng chuyền + laser.','S D','laser'),
  ('MID','Điểm dừng',24,17,'R',2,'Checkpoint.','C',''),
  ('R3','Trung tâm Boss Rush',40,24,'R',7,'8 cổng dịch chuyển (2 hàng × 4), mỗi cổng một boss Act II.','M',''),
  ('BOSS','Hell Sigma',30,17,'A',9,'3 pha, sàn sụp và virus.','*','sàn sụp'),
 ],
 secrets=[], newMech=['Gai nhô theo nhịp trong trục rơi'],
 art='terrain-core, native-portal.')
