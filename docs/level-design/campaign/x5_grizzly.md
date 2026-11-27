# Tàu bọc thép — Boss Crescent Grizzly

`x5_grizzly` · chủ đề `metal` · Act I · X5 · tổng ~346×36 ô (11072×1152 px)

![Sơ đồ](maps/x5_grizzly.png)

## Ý tưởng
Đoàn tàu bọc thép 8 toa lao qua sa mạc. Area 1 chạy trên nóc toa trong gió ngược, nhảy qua các khớp nối đang tách; Area 2 chui vào khoang hàng có băng chuyền, cưỡi Ride Armor đục vách toa 6 lấy Falcon Foot, rồi lên nóc đầu tàu né các hầm đá.

## Tham khảo
X5 Crescent Grizzly (tàu bọc thép), X8 Earthrock Trilobite (bị vật lớn đuổi), X2 Overdrive Ostrich (tốc độ, nền trôi).

## Chuẩn kích thước
Khung hình 640×360 px = 20×11.25 ô. Hành lang: trần 1 ô, trong lòng 9 ô, khối trần luôn nằm trong khung; phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô; đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô. X nhảy cao ~2.6 ô, xa ~5 ô: trên đường chính gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô (lướt-nhảy ≤ 7 ô); cao/xa hơn chỉ bằng đá tường, giáp hoặc cơ chế của màn, và dùng cho bí mật.

## Cấu trúc

- **Area 1** (R1 → R2 → R3 → R4): sa mạc, nóc tàu, gió ngược
- **Mid** (MID): mini-boss xe tải bọc thép
- **Area 2** (R5 → R6 → R7): khoang hàng và đầu tàu
- **Boss** (BOSS): nóc toa chỉ huy

## Nhịp màn (độ khó)
R1 (2) → R2 (3) → R3 (4) → R4 (4) → MID (5) → R5 (5) → R6 (7) → R7 (2) → BOSS (6)

## Kịch bản từng phòng

### R1 – Sân ga · đi ngang · độ khó 2
*x 0–37, y 22–34 (37×12 ô) · vào ở sàn y 32, ra ở sàn y 30* · Area 1 · nóc tàu

Tàu khởi hành sau 3 giây: sân ga đứng yên, nền parallax bắt đầu trôi. Dạy nhảy lên thùng hàng và bắn Sniper đứng trên nóc toa đầu.
- **Thông số:** tàu khởi hành sau 3 s; nền parallax trôi 240 px/s
- **Địa hình:** khối x 14–17, y 30–32
- **Thực thể:** Sniper (11, 32); Drone (36, 27)
- **Đường chính dùng:** nhảy, rơi xuống

### R2 – Nóc toa 1–3 · đi ngang · độ khó 3
*x 37–99, y 20–32 (62×12 ô) · vào ở sàn y 30, ra ở sàn y 30* · Area 1 · nóc tàu

Gió ngược −55 px/s trên nóc. Ba khớp nối có khe 2–3 ô; Sniper ở cuối mỗi toa. Thùng hàng là vật che đạn.
- **Thông số:** gió ngược −55 px/s (chạy còn 195 px/s); khe khớp nối 2–3 ô
- **Địa hình:** vùng gió x 37–53, y 21–30 (← gió −55 px/s); hố vực (rơi = mất mạng) x 53–55 (rộng 2 ô); vùng gió x 56–70, y 21–30; khối x 70–72, y 28–30; hố vực (rơi = mất mạng) x 74–77 (rộng 3 ô); vùng gió x 78–90, y 21–30; hố vực (rơi = mất mạng) x 90–92 (rộng 2 ô)
- **Thực thể:** Sniper (45, 30); Drone (63, 27); Sniper (82, 30); Reploid cứu (86, 30)
- **Đường chính dùng:** nhảy, rơi xuống

### R3 – Khớp nối tách · đi ngang · độ khó 4
*x 99–140, y 20–32 (41×12 ô) · vào ở sàn y 30, ra ở sàn y 30* · Area 1 · nóc tàu

Đứng gần khớp nối 6 s thì khe mở rộng dần từ 0 lên 6 ô (đèn đỏ chớp 1 s trước khi mở). Khe đã mở quá 5 ô phải lướt-nhảy. Drone bay ngang thả bom đúng khe.
- **Thông số:** khe 0→6 ô trong 6 s, chớp đỏ 1 s trước khi mở; Drone thả bom mỗi 2.5 s
- **Địa hình:** hố vực (rơi = mất mạng) x 107–111 (rộng 4 ô); hố vực (rơi = mất mạng) x 118–123 (rộng 5 ô); hố vực (rơi = mất mạng) x 132–135 (rộng 3 ô)
- **Thực thể:** Sniper (103, 30); Drone (118, 27)
- **Đường chính dùng:** nhảy

### R4 – Toa cần cẩu · leo dọc · độ khó 4
*x 140–154, y 2–32 (14×30 ô) · vào ở sàn y 30, ra ở sàn y 12* · Area 1 · nóc tàu

Toa chở cần cẩu: leo lên đỉnh cần cẩu bằng các bệ hàng treo (lắc nhẹ theo tàu). Reploid bị kẹt ở bệ giữa. Từ đỉnh cần cẩu nhìn thấy đầu máy phía trước.
- **Thông số:** bệ treo lắc ±0.5 ô theo nhịp 2 s
- **Địa hình:** khối x 149–152, y 12–13; bệ treo cáp x 144–147, y 27.5; bệ treo cáp x 148–151, y 25; bệ treo cáp x 144–147, y 22.5; bệ treo cáp x 148–151, y 20; bệ treo cáp x 144–147, y 17.5; bệ treo cáp x 148–151, y 15; bệ treo cáp x 144–147, y 12.5
- **Thực thể:** Reploid cứu (149.5, 20); Drone (145.5, 9.5)
- **Đường chính dùng:** nhảy

### MID – Xe tải bọc thép · đấu trường · độ khó 5
*x 154–184, y 2–14 (30×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Mid

Mini-boss: xe tải (truck) chạy song song trên toa sàn phẳng, bắn pháo cong và lao húc. Hạ xong: checkpoint 1 và cửa Area 2 mở.
- **Thông số:** pháo cong mỗi 1.8 s; húc ngang mỗi 6 s (cảnh báo khói 1 s)
- **Thực thể:** Mini-boss (168, 12) – truck 45 HP; Checkpoint (182, 12)

### R5 – Toa Ride Armor · đi ngang · độ khó 5
*x 184–239, y 2–14 (55×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · khoang hàng và đầu tàu

Khoang hàng: băng chuyền đẩy ngược −80 px/s. Ride Armor Pod ở đầu toa; cưỡi nó đấm vỡ vách thép nứt ở toa 6 → khoang kín có capsule Falcon Foot. Sub-Tank trên kệ hàng cao.
- **Thông số:** băng chuyền −80 px/s; vách nứt 16 HP (chỉ Ride Armor phá được)
- **Địa hình:** băng chuyền x 192–206 (-80 px/s); tường phá được x 206, y 8–12; băng chuyền x 210–220 (-80 px/s); khối x 220–222, y 10–12; bệ / kệ x 226–229, y 9.5; khối x 219–225, y 12–14
- **Thực thể:** Ride Armor / Chaser (193, 12) – Ride Armor Pod; Brute (199, 12); Sniper (215, 12); Sub-Tank (227, 9.5); Drone (231, 9); Capsule giáp (221, 13.5) – Falcon Foot (khoang kín dưới sàn)
- **Đường chính dùng:** băng chuyền, nhảy, rơi xuống
- **Lối bí mật:** (206, 12) → (206, 13.5) → (212, 13.5)

### R6 – Nóc toa đầu và hầm · đi ngang · độ khó 7
*x 239–294, y 2–14 (55×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · khoang hàng và đầu tàu

Cao trào. Gió mạnh −90 px/s; hai hầm đá quét qua nóc: trần hạ còn 1.6 ô, phải lướt sát nóc trước khi hầm tới (đèn đỏ + tiếng còi 1.5 s). Khe khớp nối 4 ô giữa hai hầm. Heart Tank trên nóc ống khói thấp giữa hai hầm.
- **Thông số:** gió −90 px/s; hầm tới mỗi 8 s, cảnh báo 1.5 s; khe 4 ô
- **Địa hình:** vùng gió x 239–249, y 3–12 (← gió −90 px/s); hố vực (rơi = mất mạng) x 261–265 (rộng 4 ô); khối x 269–271, y 9.5–12; vùng gió x 280–290, y 3–12
- **Thực thể:** Sniper (244, 12); Checkpoint (245, 12); Drone (269, 9); Heart Tank (270, 9.5) – trên ống khói; Brute (285, 12)
- **Đường chính dùng:** lướt dưới khe thấp, nhảy
- **Lối bí mật:** (269, 12) → (269, 9.5) → (271, 9.5)

### R7 – Toa chỉ huy · đi ngang · độ khó 2
*x 294–314, y 2–14 (20×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · khoang hàng và đầu tàu

Phòng nghỉ trong toa chỉ huy: năng lượng nhỏ, Reploid cuối, cửa boss.
- **Thực thể:** Reploid cứu (297, 12); Reploid cứu (306, 12)

### BOSS – Crescent Grizzly · đấu trường · độ khó 6
*x 314–344, y 2–14 (30×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Boss

Đấu trên nóc toa chỉ huy dài 30 ô, có gió ngang đổi chiều mỗi 6 s.
- **Thông số:** gió ngang ±60 px/s, đổi chiều mỗi 6 s
- **Thực thể:** Boss (328, 12)

## Bảng kẻ địch và vật phẩm

| Loại | Phòng | x | y | Ghi chú |
|---|---|---|---|---|
| Sniper | R1 | 11 | 32 |  |
| Drone | R1 | 36 | 27 |  |
| Sniper | R2 | 45 | 30 |  |
| Drone | R2 | 63 | 27 |  |
| Sniper | R2 | 82 | 30 |  |
| Reploid cứu | R2 | 86 | 30 |  |
| Sniper | R3 | 103 | 30 |  |
| Drone | R3 | 118 | 27 |  |
| Reploid cứu | R4 | 149.5 | 20 |  |
| Drone | R4 | 145.5 | 9.5 |  |
| Mini-boss | MID | 168 | 12 | truck 45 HP |
| Checkpoint | MID | 182 | 12 |  |
| Ride Armor / Chaser | R5 | 193 | 12 | Ride Armor Pod |
| Brute | R5 | 199 | 12 |  |
| Sniper | R5 | 215 | 12 |  |
| Sub-Tank | R5 | 227 | 9.5 |  |
| Drone | R5 | 231 | 9 |  |
| Capsule giáp | R5 | 221 | 13.5 | Falcon Foot (khoang kín dưới sàn) |
| Sniper | R6 | 244 | 12 |  |
| Checkpoint | R6 | 245 | 12 |  |
| Drone | R6 | 269 | 9 |  |
| Heart Tank | R6 | 270 | 9.5 | trên ống khói |
| Brute | R6 | 285 | 12 |  |
| Reploid cứu | R7 | 297 | 12 |  |
| Reploid cứu | R7 | 306 | 12 |  |
| Boss | BOSS | 328 | 12 |  |

Tổng: 14 kẻ địch thường (Sniper 6, Drone 6, Brute 2), 4 Reploid, 2 checkpoint, Heart Tank 1, Sub-Tank 1, capsule 1.

## Capsule theo dữ liệu game
🛡️ Capsule Falcon Armor — Foot Part (X=5160, Y=560 — Toa tàu số 6 Area 2): Hạ Sub-Boss đầu máy tại Mid-Gate, lấy Ride Armor Pod (X=3720), đi qua khoang băng chuyền và dùng cú đấm Mech phá vách toa thép nứt (X=4980). 8 Toa tàu tách rời + Gió ngược + Sub-Boss Đầu máy + Ride Armor lấy Falcon Foot Area 1: Nhảy qua 4 toa tàu bọc thép đầu tiên trong cơn gió ngược cực mạnh. Mid-Gate: Đánh Sub-Boss Đầu máy. Area 2: Chui vào khoang tàu chở hàng có băng chuyền đẩy ngược, dùng Ride Armor đục vách toa số 6 lấy Falcon Foot Part.

## Bí mật
| Vật phẩm | Phòng | Cách lấy |
|---|---|---|
| Capsule Falcon Foot | R5 | Cưỡi Ride Armor đấm vỡ vách nứt toa 6, rơi vào khoang kín dưới sàn. |
| Heart Tank | R6 | Đá tường lên nóc ống khói giữa hai hầm. |
| Sub-Tank | R5 | Kệ hàng cao sau đoạn băng chuyền thứ hai. |

## Boss
**Crescent Grizzly** · điểm yếu: Spike Ball / Twin Dream
- **Bộ chiêu (dữ liệu game):** Crescent Shot: Phóng lưỡi liềm năng lượng xanh bay vòng cung về phía người chơi. Burrow & Ambush: Đào sâu xuống sàn toa tàu, di chuyển ngầm rồi trồi lên cào mạnh. Claw Slash: Lao tới vung vuốt cận chiến tầm gần. Overdrive (Phase 2): Bắn liên hoàn loạt lưỡi liềm lớn và giậm đất tạo sóng chấn động.
- **Đấu trường:** nóc toa 30×11 ô, không trần (bầu trời), hai đầu là mép toa (rơi = mất máu, không chết).
- **Pha 2 (dưới 50% HP):** gió ngang mạnh gấp đôi và tàu chui hầm: trần hạ còn 4 ô trong 3 s mỗi 12 s, Grizzly đào xuống sàn tránh.

## Engine cần bổ sung
- Nền parallax trôi liên tục để tạo cảm giác tàu chạy
- Vùng gió đẩy ngang có tốc độ chỉnh được
- Khớp nối tách theo thời gian (khe rộng dần, có cảnh báo)
- Hầm quét: khối trần hạ theo lịch + cảnh báo
- Ride Armor phá vách nứt (breakable_blocks)
- Băng chuyền đẩy ngược

## Hình cần vẽ
- Nóc toa và khớp nối (tileset metal, 2 biến thể)
- Thùng hàng che đạn
- Cần cẩu và bệ hàng treo
- Miệng hầm đá + đèn cảnh báo
- Ống khói đầu tàu
- Xe tải bọc thép (mini-boss, có sẵn: truck)
- Nền sa mạc parallax 3 lớp

## Kiểm tra tự động
Đường chính đã được kiểm tra theo khả năng nhảy (gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô, lướt-nhảy ≤ 7 ô, đi bộ phải có nền) và theo quy ước số lượng.

**Kết quả: đạt.**
