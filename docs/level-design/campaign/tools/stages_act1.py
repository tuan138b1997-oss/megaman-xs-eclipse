# Thiết kế 25 màn còn lại — dữ liệu nguồn cho sơ đồ + kịch bản.
# Phòng: (mã, tên, rộng, cao, hướng, độ khó, mô tả, biểu tượng, bẫy)
#  hướng: R = đi sang phải, U = leo lên, D = rơi/đi xuống, A = đấu trường
#  biểu tượng: S sniper · D drone · B brute · M mini-boss · * boss · R reploid · H heart tank · T sub-tank
#              A capsule giáp · C checkpoint · V xe (Ride Armor / Ride Chaser) · K công tắc
# CHUẨN KÍCH THƯỚC (theo màn mẫu Lò Nham Thạch, bản đã duyệt):
#  khung hình 640×360 px = 20×11.25 ô · hành lang trần→sàn 9 ô · phòng nhảy bệ/vực/nước 11 ô ·
#  phòng 2 tầng 17 ô · đấu trường cao 11 ô, rộng 20–30 ô · giếng rộng 12–20 ô ·
#  nhảy thường cao ~2.6 ô (vy 520), xa ~5 ô: gờ đường chính ≤ 2.5 ô, hố ≤ 4 ô; cao/xa hơn = đá tường, giáp hoặc bí mật.
STAGES = {}

STAGES['intro'] = dict(
 title='Cao tốc Neo Arcadia', boss='1D-1000 → High Max', theme='intro', act='Mở đầu',
 concept='Màn dạy chơi trên cao tốc đổ nát 2 tầng lúc hoàng hôn. Mỗi phòng dạy đúng một kỹ năng: chạy, bắn, lướt, đá tường, cưỡi Ride Armor. Kết thúc bằng con nhện 1D-1000 rồi High Max xuất hiện.',
 refs='X4/X5 intro (dạy 1 kỹ năng/đoạn, boss kích thước lớn), X8 intro (màn duy nhất chơi "thẳng", không gimmick nặng).',
 rooms=[
  ('R1','Làn đường sập',50,9,'R',1,'Đường thẳng an toàn, vài khối bê tông thấp để dạy nhảy và bắn. Bảng chỉ dẫn hiện nút.','S S',''),
  ('R2','Cầu vượt gãy',60,9,'R',2,'Hai hố nhỏ trên cầu gãy (rơi = mất máu, không chết). Drone bay ngang dạy bắn chéo.','D S R','hố'),
  ('R3','Trụ cầu',18,34,'U',2,'Giếng leo ngắn giữa hai trụ cầu, dạy đá tường. Có kệ nghỉ mỗi 8 ô.','D',''),
  ('R4','Tầng trên cao tốc',70,9,'R',3,'Ô tô cháy làm vật che, Brute đứng chặn. Lướt dưới biển báo thấp.','B S D C','lửa xe'),
  ('R5','Bãi Ride Armor',40,9,'R',3,'Ride Armor Pod đậu ở đầu phòng. Dùng nó đấm vỡ tường bê tông tầng 2 → lối lên capsule Fourth Armor.','V A R','tường phá'),
  ('R6','Đường hầm đèn vàng',60,9,'R',3,'Hầm tối, đèn trần chớp; Drone lao từ hai đầu. Heart Tank sau khe thông gió (lướt + nhảy).','D D H',''),
  ('R7','Lối ra cao tốc',30,9,'R',2,'Phòng nghỉ, Reploid cuối, cửa boss.','R',''),
  ('BOSS','1D-1000 / High Max',30,11,'A',4,'Nhện 1D-1000 bám trần và hai tường, thả bom; sau đó High Max đáp xuống (không thể thắng, chuyển cảnh).','*',''),
 ],
 secrets=[('Capsule Fourth Armor','R5','Dùng Ride Armor đấm vỡ tường tầng 2.'),('Heart Tank','R6','Khe thông gió trên trần: lướt rồi nhảy.')],
 newMech=['Bảng chỉ dẫn nút','Tường bê tông phá bằng Ride Armor'],
 art='terrain-intro / cap-intro, native-deck cho cầu, mmx5_destructablewalls cho tường bê tông, x5-hovermech cho Ride Armor.')

STAGES['x5_grizzly'] = dict(
 title='Tàu bọc thép', boss='Crescent Grizzly', theme='metal', act='Act I · X5',
 concept='Đoàn tàu 8 toa chạy giữa sa mạc. Người chơi chạy dọc nóc và xuyên qua bên trong toa, gió ngược đẩy lùi khi ở trên nóc. Toa sau tách ra khỏi đoàn theo thời gian.',
 refs='X5 Crescent Grizzly (tàu bọc thép), X8 Earthrock Trilobite (bị đuổi bởi vật thể lớn), X2 Overdrive Ostrich (tốc độ).',
 rooms=[
  ('R1','Toa hàng 1–2',70,9,'R',2,'Nóc toa có gió ngược (-55px/s); xuống trong toa thì hết gió nhưng trần thấp và có Sniper.','S S D','gió ngược'),
  ('R2','Khớp nối toa',30,9,'R',3,'Khớp nối tách ra sau 6 giây đứng gần: phải nhảy qua khe đang rộng dần.','D R','khớp tách'),
  ('R3','Toa pháo',60,9,'R',3,'Tháp pháo trên nóc bắn đạn cong; chui vào trong toa né. Băng chuyền hàng hóa chạy ngược.','S B','băng chuyền'),
  ('MID','Đầu máy phụ',30,11,'A',5,'Sub-boss Đầu máy (truck) chặn đường; hạ nó mới mở toa tiếp. Checkpoint sau trận.','M C',''),
  ('R4','Toa Ride Armor',50,9,'R',4,'Ride Armor Pod; đấm vỡ thùng hàng thép mở khoang băng chuyền phía dưới.','V R','thùng thép'),
  ('R5','Khoang băng chuyền',60,9,'R',4,'Đi bên trong toa 5–6 bằng Ride Armor; capsule Falcon Foot ở toa 6.','A T','băng chuyền'),
  ('R6','Nóc toa đầu',60,9,'R',5,'Gió mạnh nhất, đường hầm đá phía trước: phải nằm xuống/lướt dưới khi tàu chui hầm (cảnh báo chớp đỏ).','D D H','hầm thấp'),
  ('R7','Toa chỉ huy',30,9,'R',2,'Phòng nghỉ, Reploid, cửa boss.','R',''),
  ('BOSS','Crescent Grizzly',30,11,'A',6,'Đấu trên nóc toa chỉ huy có gió ngang đổi chiều mỗi pha.','*','gió'),
 ],
 secrets=[('Capsule Falcon Foot','R5','Cần Ride Armor từ R4.'),('Heart Tank','R6','Nóc toa đầu, nhảy khi tàu ra khỏi hầm.'),('Sub-Tank','R5','Cuối khoang băng chuyền.')],
 newMech=['Khớp nối toa tách theo thời gian','Hầm thấp quét qua nóc tàu (phải cúi/lướt)'],
 art='terrain-metal/cap-metal, native-deck cho nóc toa, mmx5_truckbackgroundtiles cho nền tàu chạy, mmx5_destructablewalls cho thùng hàng.')

STAGES['x5_makkoeen'] = dict(
 title='Căn cứ đáy biển', boss='Tidal Makkoeen', theme='water', act='Act I · X5',
 concept='Căn cứ chìm dưới biển: phần lớn màn ngập nước (trọng lực nhẹ, nhảy cao). Có đoạn mực nước rút/dâng theo công tắc, và tàu ngầm U-555 truy đuổi ở giữa màn.',
 refs='X5 Tidal Makkoeen, X Launch Octopus/X3 Toxic Seahorse (nước + nhảy cao), X8 Bamboo Pandamonium (lối phụ cần thiết bị).',
 rooms=[
  ('R1','Bến tàu',50,11,'R',2,'Trên mặt nước, sóng đẩy nhẹ. Nhảy xuống nước để thấy trọng lực nhẹ.','S D',''),
  ('R2','Hành lang ngập',70,11,'R',3,'Dưới nước: nhảy siêu cao lên kệ trần, cá máy (Drone nước) bơi zigzag.','D D R','dòng chảy'),
  ('R3','Trụ tường cao',20,40,'U',3,'Giếng nước dọc; trọng lực nhẹ giúp đá tường lên trụ X=2350 → hốc trần chứa Falcon Head.','A',''),
  ('MID','Hầm tàu ngầm',30,11,'A',5,'Sub-boss U-555 bắn ngư lôi; mực nước hạ dần để lộ điểm yếu.','M C',''),
  ('R4','Phòng bơm',50,11,'R',4,'Bắn 2 công tắc bơm để rút nước → lối đi dưới đáy lộ ra (Sub-Tank). Rút nước thì mất nhảy cao.','K K T','mực nước'),
  ('R5','Đường ống áp lực',60,11,'R',4,'Ống xả bọt nước đẩy ngang; gai trên trần (nhảy cao quá là trúng).','D S H','gai trần'),
  ('R6','Cửa cống',30,9,'R',2,'Phòng nghỉ, Reploid, cửa boss.','R R',''),
  ('BOSS','Tidal Makkoeen',30,11,'A',6,'Đấu trường nửa ngập: Makkoeen trượt trên mặt nước, pha 2 nước dâng ngập toàn sân.','*','nước'),
 ],
 secrets=[('Capsule Falcon Head','R3','Đá tường trong nước lên hốc trần.'),('Sub-Tank','R4','Đáy lộ ra sau khi rút nước.'),('Heart Tank','R5','Khe giữa hai dải gai trần — nhảy thấp.')],
 newMech=['Công tắc rút/dâng mực nước','Dòng chảy ngang dưới nước'],
 art='terrain-water/cap-water, native-ice cho kệ kính, bg-water; bọt nước dùng lại fx-water.')

STAGES['x5_kraken'] = dict(
 title='Nhà máy điện', boss='Volt Kraken', theme='volt', act='Act I · X5',
 concept='Nửa đầu là chặng Ride Chaser tốc độ cao xuyên nhà máy, nửa sau leo tháp tụ điện bằng bệ đẩy và đá tường.',
 refs='X5 Volt Kraken (Ride Chaser), X2 Overdrive Ostrich, X8 Gigabolt Man-O-War (tránh lỗi: không auto-scroll, người chơi điều tốc độ).',
 rooms=[
  ('R1','Bãi xuất phát',30,9,'R',1,'Lên Ride Chaser; bảng hướng dẫn nhảy/bắn khi đang chạy.','V',''),
  ('R2','Đường băng điện',120,9,'R',4,'Ride Chaser: dốc nhảy, cột điện phóng tia ngang (hồ quang), Drone lao từ phía sau. Vòng tăng tốc trên mặt đường.','D D D R','hồ quang'),
  ('R3','Cầu sập',60,9,'R',5,'Ride Chaser: cầu sập dần sau lưng, phải giữ tốc độ; nhảy cuối cầu để vào nhà máy.','D','cầu sập'),
  ('MID','Trạm biến áp',30,9,'R',2,'Xuống xe, checkpoint. Heart Tank trên nóc trạm (đá tường).','C H',''),
  ('R4','Tháp tụ điện',20,50,'U',5,'Leo tháp: bệ đẩy Thruster bật theo nhịp, tia điện quét ngang mỗi tầng. Falcon Arm ở đỉnh tháp.','D S A','tia điện'),
  ('R5','Phòng cuộn dây',50,9,'R',4,'Sàn nhiễm điện bật/tắt theo nhịp 1.2s; Reploid kẹt giữa hai cuộn dây.','S B R','sàn điện'),
  ('R6','Hành lang lõi',30,9,'R',2,'Phòng nghỉ, Sub-Tank trong hốc tường, cửa boss.','T R',''),
  ('BOSS','Volt Kraken',30,11,'A',6,'Đấu trường có 4 cột thu sét; pha 2 Kraken nạp điện các cột thành bẫy.','*','cột điện'),
 ],
 secrets=[('Capsule Falcon Arm','R4','Đỉnh tháp tụ điện.'),('Heart Tank','MID','Nóc trạm biến áp.'),('Sub-Tank','R6','Hốc tường cần lướt vào.')],
 newMech=['Ride Chaser chạy tự do (không tự cuộn)','Sàn điện theo nhịp','Bệ đẩy Thruster'],
 art='terrain-volt/cap-volt, x5_hoverbike cho Ride Chaser, mmx5_cyberblock cho bệ đẩy, fx-volt cho hồ quang.')

STAGES['x5_hotarunicus'] = dict(
 title='Phòng thí nghiệm Laser', boss='Shining Hotarunicus', theme='volt', act='Act I · X5',
 concept='Viện nghiên cứu quang học: tia laser đỏ chặn lối, phải bắn công tắc quang học để tắt. Nửa sau là bệ hologram nhấp nháy trên băng chuyền.',
 refs='X5 Shining Firefly (laser + gương), X6 Shield Sheldon (laser phản xạ), X4 Cyber Peacock (bệ ảo).',
 rooms=[
  ('R1','Sảnh viện',50,9,'R',2,'Laser đỏ quét chậm theo chiều dọc, dạy canh nhịp.','S D','laser quét'),
  ('R2','Khoang quang học #1',40,9,'R',3,'Bắn công tắc #1 tắt cửa laser đầu tiên. Gương xoay đổi hướng tia.','K S R','gương'),
  ('R3','Khoang quang học #2',20,30,'U',4,'Leo bệ cao X=2150 bắn công tắc #2 → tường laser tắt → buồng Falcon Body.','K A','laser'),
  ('R4','Khoang quang học #3',40,9,'R',4,'Công tắc #3 phải bắn khi đứng trong vùng an toàn giữa 2 tia quét.','K D H','laser quét'),
  ('MID','Trạm làm mát',24,9,'R',2,'Checkpoint.','C',''),
  ('R5','Bệ Hologram',70,11,'R',5,'Bệ hologram hiện/tắt 2 pha (xanh/tím) trên vực; băng chuyền ở hai đầu.','D D R','bệ nhấp nháy'),
  ('R6','Dây chuyền thấu kính',50,9,'R',4,'Băng chuyền đôi chạy ngược chiều nhau, thấu kính rơi từ trần.','S B T','băng chuyền'),
  ('BOSS','Shining Hotarunicus',30,11,'A',6,'Đấu trường tối; boss tạo phân thân ánh sáng, gương ở 2 góc phản xạ đạn của người chơi.','*',''),
 ],
 secrets=[('Capsule Falcon Body','R3','Sau công tắc quang học #2.'),('Heart Tank','R4','Trên cụm gương, bắn công tắc từ dưới.'),('Sub-Tank','R6','Cuối băng chuyền đôi.')],
 newMech=['Công tắc quang học','Gương xoay đổi hướng tia','Bệ hologram 2 pha'],
 art='terrain-volt, native-cyberblock + mmx5_cyberblock cho bệ hologram, fx-laser cho tia, gương vẽ mới (2 khung).')

STAGES['x5_rosered'] = dict(
 title='Rừng đột biến', boss='Spike Rosered', theme='nature', act='Act I · X5',
 concept='Rừng nấm khổng lồ 2 tầng. Nấm đàn hồi bật người chơi lên tầng tán cây. Sub-boss dây leo chặn giữa màn, cuối màn leo thân cây cổ thụ.',
 refs='X4 Web Spider (rừng, dây leo đu), X5 Spike Rosered, X6 Commander Yammark (2 tầng tách nhánh).',
 rooms=[
  ('R1','Bìa rừng',60,9,'R',2,'Nấm đàn hồi đầu tiên (bật cao 900px/s), dạy nảy lên tầng trên.','S D','nấm bật'),
  ('R2','Tầng nấm',70,17,'R',3,'Hai tầng song song: dưới nhiều địch, trên ít địch nhưng nhiều khe. Gai dây leo dưới đáy.','D D R','gai'),
  ('R3','Dây leo đu',50,11,'R',4,'Dây leo đu qua vực (giữ nút nhảy để bám, thả để bay).','D','vực'),
  ('MID','Lõi dây leo',30,11,'A',5,'Sub-boss Dây leo: 3 bông hoa phun gai, phải bắn theo thứ tự. Checkpoint sau trận.','M C',''),
  ('R5','Đầm lầy',60,11,'R',4,'Bùn làm chậm 40%; bệ gỗ nổi chìm dần khi đứng lâu.','S B H','bùn'),
  ('R6','Thân cây cổ thụ',20,44,'U',5,'Leo thân cây X=4850 bằng đá tường + nấm; tán cây có capsule Gaea Foot.','D A T','gai'),
  ('R7','Vườn hoa',30,9,'R',2,'Phòng nghỉ, 2 Reploid, cửa boss.','R R',''),
  ('BOSS','Spike Rosered',30,11,'A',6,'Sàn có bụi gai mọc lại sau 4 giây; boss treo trên dây leo trần.','*','gai'),
 ],
 secrets=[('Capsule Gaea Foot','R6','Tán cây cổ thụ (Falcon bay hoặc nấm + lướt trên không).'),('Heart Tank','R5','Trên bệ gỗ cao nhất trước khi chìm.'),('Sub-Tank','R6','Hốc thân cây giữa giếng.')],
 newMech=['Dây leo đu','Bùn làm chậm','Bệ gỗ chìm dần'],
 art='terrain-nature/cap-nature, prop-nature, nấm và dây leo vẽ mới; bụi gai dùng hazard spikes.')

STAGES['x5_necrobat'] = dict(
 title='Đài thiên văn', boss='Dark Necrobat', theme='shadow', act='Act I · X5',
 concept='Đài thiên văn bỏ hoang trong đêm, trọng lực vũ trụ nhẹ (0.42), vùng làm chậm thời gian và cổng dịch chuyển giữa các vòm.',
 refs='X5 Dark Necrobat, X8 Gravity Antonion (gimmick trọng lực được khen là "làm đúng"), X4 Cyber Peacock.',
 rooms=[
  ('R1','Sân đài',50,9,'R',2,'Trọng lực nhẹ: nhảy rất cao, rơi chậm; dơi máy bay theo đàn.','D D',''),
  ('R2','Vòm kính',60,11,'R',3,'Khối nổi trôi chậm làm bệ; Time Zone (tím) làm chậm mọi thứ kể cả đạn địch.','S D R','time zone'),
  ('R3','Phòng kính viễn vọng',20,30,'U',4,'Leo lên dọc ống kính khổng lồ đang xoay; chạm thấu kính sáng bị đẩy lùi.','D','thấu kính'),
  ('R4','Đỉnh đài',40,11,'R',4,'Cuối Area 1: bệ trôi + Time Zone → Gaea Head ở đỉnh.','A H',''),
  ('MID','Phòng điều khiển',24,9,'R',2,'Checkpoint.','C',''),
  ('R5','Hành lang cổng',70,9,'R',5,'4 cổng dịch chuyển nối 2 tầng; một cổng dẫn vào phòng kín có Sub-Tank.','D S R T','cổng'),
  ('R6','Vòm sao băng',50,11,'R',5,'Thiên thạch nhỏ rơi theo nhịp từ trần kính vỡ; bệ trôi.','D B R','thiên thạch'),
  ('BOSS','Dark Necrobat',30,11,'A',6,'Trọng lực nhẹ trong sân đấu; dơi con hút máu khi bám người.','*',''),
 ],
 secrets=[('Capsule Gaea Head','R4','Đỉnh đài thiên văn cuối Area 1.'),('Heart Tank','R4','Bệ trôi phía trên Time Zone.'),('Sub-Tank','R5','Phòng kín sau cổng thứ 3.')],
 newMech=['Khối nổi trôi chậm','Thấu kính đẩy lùi'],
 art='terrain-shadow, native-portal cho cổng, mmx5_moon cho nền, bg-shadow.')

STAGES['x5_pegacion'] = dict(
 title='Không quân', boss='Spiral Pegacion', theme='wind', act='Act I · X5',
 concept='Chiến dịch trên không: nhảy giữa 4 chiến hạm đang bay, quạt khí nâng giữa các hạm, pháo đài bay hộ tống làm sub-boss.',
 refs='X5 Spiral Pegacion, X2 Wire Sponge/X3 Blast Hornet (trên cao), X8 Optic Sunflower (bệ di động).',
 rooms=[
  ('R1','Đường băng cất cánh',50,9,'R',2,'Gió ngang nhẹ, máy bay địch cất cánh lao thấp.','S D',''),
  ('R2','Chiến hạm 1',60,17,'R',3,'Boong có tháp pháo; cuối hạm là quạt nâng (updraft) đưa sang hạm 2.','D S R','updraft'),
  ('R3','Giữa trời',50,17,'R',4,'Khối mây cứng trôi + updraft; rơi = mất một mạng nên có lưới an toàn ở đoạn đầu.','D D','vực'),
  ('MID','Pháo đài hộ tống',30,11,'A',5,'Sub-boss pháo đài bay; Heart Tank X=3950 ở boong sau khi hạ. Checkpoint.','M C H',''),
  ('R4','Chiến hạm 3',60,9,'R',5,'Boong nghiêng theo nhịp (nhân vật trượt nhẹ); khối blocks rơi.','S B R','boong nghiêng'),
  ('R5','Chiến hạm 4',60,11,'R',5,'Cưỡi quạt nâng lên boong trên cùng: capsule Gaea Body cuối hạm.','D A T','updraft'),
  ('R6','Cầu chỉ huy',30,9,'R',2,'Phòng nghỉ, Reploid, cửa boss.','R R',''),
  ('BOSS','Spiral Pegacion',30,11,'A',6,'Đấu trên boong mở, gió xoáy đẩy người chơi về mép.','*','gió'),
 ],
 secrets=[('Capsule Gaea Body','R5','Boong trên cùng chiến hạm 4.'),('Heart Tank','MID','Boong pháo đài sau khi hạ sub-boss.'),('Sub-Tank','R5','Dưới cánh hạm, cần lướt trên không.')],
 newMech=['Boong nghiêng theo nhịp','Khối mây cứng trôi'],
 art='terrain-wind/cap-wind, mmx5_spiralpegacionplane cho chiến hạm nền, mmx6-platform cho bệ trôi.')

STAGES['x5_f1_dynamo'] = dict(
 title='Zero Space 1', boss='Dynamo', theme='shadow', act='Pháo đài Act I',
 concept='Pháo đài Sigma: 6 cụm laser tử thần quét toàn màn hình, buộc người chơi chạy giữa các hốc trú ẩn. Băng chuyền tốc độ cao làm khó canh nhịp.',
 refs='X5 Zero Space 1, X4 final stages (laser quét màn hình), X8 Jakob (trần ép).',
 rooms=[
  ('R1','Cổng pháo đài',40,9,'R',3,'Laser quét #1 chậm, có 3 hốc trú ẩn gần nhau để làm quen.','S','laser màn'),
  ('R2','Hành lang băng chuyền',70,9,'R',5,'Băng chuyền nhanh (200px/s) và laser quét #2–#3; hốc trú ẩn xa nhau hơn.','D B','laser màn'),
  ('R3','Giếng tia',20,40,'U',5,'Leo lên trong khi laser quét dọc theo chiều cao.','D','laser dọc'),
  ('MID','Điểm dừng',24,9,'R',2,'Checkpoint, nạp năng lượng.','C',''),
  ('R4','Hành lang cuối',70,9,'R',6,'Laser #5–#6 phối hợp nhịp khác nhau; khối blocks chặn hốc trú ẩn phải bắn vỡ.','D S','laser màn'),
  ('BOSS','Dynamo',30,11,'A',7,'Đấu trường trống, Dynamo ném boomerang và gọi mạch nước nóng.','*',''),
 ],
 secrets=[], newMech=['Laser quét toàn màn hình + hốc trú ẩn'],
 art='terrain-shadow, native-panel, fx-laser phóng to cho laser màn hình, mmx5_v-block cho khối chặn hốc.')

STAGES['x5_f2_shadow'] = dict(
 title='Zero Space 2', boss='Shadow Devil', theme='shadow', act='Pháo đài Act I',
 concept='Toàn màn là vực không đáy; đường đi duy nhất là chuỗi 10 bệ hologram 2 pha và quạt nâng.',
 refs='X5 Zero Space 2, X4 Cyber Peacock (bệ ảo), X8 Optic Sunflower.',
 rooms=[
  ('R1','Rìa vực',40,11,'R',3,'Bệ 2 pha đầu tiên đổi mỗi 2 giây, có bệ cứng xen giữa.','D','vực'),
  ('R2','Chuỗi hologram',80,11,'R',6,'10 bệ đổi pha; quạt nâng giữa chuỗi để vượt khe lớn.','D D','vực, bệ 2 pha'),
  ('MID','Điểm dừng',24,9,'R',2,'Checkpoint.','C',''),
  ('R3','Cầu bóng tối',60,11,'R',6,'Bệ di chuyển ngang trên vực + Drone ném bom.','D S','vực'),
  ('BOSS','Shadow Devil',30,11,'A',7,'Khối thạch đen ghép lại thành boss; mắt đỏ là điểm yếu (Tri-Thunder).','*',''),
 ],
 secrets=[], newMech=['Chuỗi bệ đổi pha dài'],
 art='native-cyberblock, mmx6_cyberblock cho bệ 2 pha, bg-shadow.')

STAGES['x5_f3_rangda'] = dict(
 title='Zero Space 3', boss='Rangda Bangda W', theme='shadow', act='Pháo đài Act I',
 concept='Biển gai trên sàn; vùng đảo trọng lực cho phép đi trên trần. Capsule bí mật Ultimate X5 / Black Zero nằm trong hốc trần.',
 refs='X5 Zero Space 3, X4 Cyber Peacock nửa sau (chống trọng lực), X8 Gravity Antonion.',
 rooms=[
  ('R1','Hành lang gai',50,9,'R',4,'Gai sàn rải rác, kệ một chiều phía trên.','S D','gai'),
  ('R2','Vùng đảo trọng lực',80,11,'R',6,'Bước vào vùng tím: trọng lực đảo, đi trên trần qua biển gai 1650px; gai trên trần có khe.','D','gai, đảo trọng lực'),
  ('R3','Hốc trần bí mật',20,11,'R',3,'Trong vùng đảo trọng lực: Secret Capsule (Ultimate X5 cho X / Black Zero cho Zero).','A',''),
  ('MID','Điểm dừng',24,9,'R',2,'Checkpoint.','C',''),
  ('R4','Giếng xoay',20,40,'U',6,'Trọng lực đổi chiều mỗi 3 giây trong giếng; gai hai bên tường.','D','gai'),
  ('BOSS','Rangda Bangda W',30,11,'A',7,'Tường ép vào giữa, 2 mắt và mũi là điểm yếu.','*','tường ép'),
 ],
 secrets=[('Secret Capsule Ultimate X5 / Black Zero','R3','Hốc trần trong vùng đảo trọng lực.')],
 newMech=['Trọng lực đổi chiều theo nhịp trong giếng'],
 art='native-panel, gai từ hazard spikes, vùng trọng lực tô tím như hiện tại.')

STAGES['x5_f4_sigma'] = dict(
 title='Zero Space Final', boss='Final Sigma W', theme='core', act='Pháo đài Act I',
 concept='Màn cuối Act I gom các cơ chế đã gặp: bệ di động, trọng lực biến thiên, laser, rồi phòng quyết chiến Sigma.',
 refs='X5 Final Sigma W, X4/X6 final (hành lang tổng hợp + boss nhiều pha).',
 rooms=[
  ('R1','Tổng hợp 1',60,11,'R',5,'Bệ di động trên vực + laser quét (nhắc Zero Space 1–2).','D S','vực, laser'),
  ('R2','Tổng hợp 2',20,40,'U',6,'Giếng trọng lực biến thiên + gai (nhắc Zero Space 3).','D','gai'),
  ('MID','Cổng quyết chiến',24,9,'R',2,'Checkpoint, phòng nạp đầy năng lượng.','C',''),
  ('R3','Hành lang Sigma',50,9,'R',4,'Virus Sigma bay theo người chơi, vùng làm chậm.','D D','time zone'),
  ('BOSS','Final Sigma W',30,11,'A',8,'Hai pha: thân Sigma + đầu Sigma khổng lồ; sàn sụp từng mảng ở pha 2.','*','sàn sụp'),
 ],
 secrets=[], newMech=['Sàn sụp từng mảng trong trận boss'],
 art='terrain-core, native-cyberblock, mmx5 virus sprites có sẵn.')
