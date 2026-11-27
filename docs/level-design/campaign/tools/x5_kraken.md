# Nhà máy điện — Boss Volt Kraken

`x5_kraken` · chủ đề `volt` · Act I · X5 · tổng ~357×48 ô (11424×1536 px)

![Sơ đồ](maps/x5_kraken.png)

## Ý tưởng
Nhà máy điện ven biển. Area 1 là chặng Ride Chaser người chơi tự điều khiển tốc độ (không tự cuộn) xuyên đường băng điện và cầu sập; Area 2 xuống xe, leo tháp tụ điện bằng bệ phản lực và đá tường, qua phòng cuộn dây có sàn điện theo nhịp.

## Tham khảo
X5 Volt Kraken (nhà máy điện, Ride Chaser), X4 Jet Stingray (chặng xe), X2 Wheel Gator (tháp).

## Chuẩn kích thước
Khung hình 640×360 px = 20×11.25 ô. Hành lang: trần 1 ô, trong lòng 9 ô, khối trần luôn nằm trong khung; phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô; đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô. X nhảy cao ~2.6 ô, xa ~5 ô: trên đường chính gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô (lướt-nhảy ≤ 7 ô); cao/xa hơn chỉ bằng đá tường, giáp hoặc cơ chế của màn, và dùng cho bí mật.

## Cấu trúc

- **Area 1** (R1 → R2 → R3): chặng Ride Chaser tự điều khiển
- **Mid** (R3b): trạm biến áp (checkpoint)
- **Area 2** (R4 → R5 → R6): tháp tụ điện, phòng cuộn dây
- **Boss** (BOSS): sân cột thu sét

## Nhịp màn (độ khó)
R1 (1) → R2 (4) → R3 (5) → R3b (2) → R4 (7) → R5 (5) → R6 (2) → BOSS (6)

## Kịch bản từng phòng

### R1 – Bãi xuất phát · đi ngang · độ khó 1
*x 0–26, y 34–46 (26×12 ô) · vào ở sàn y 44, ra ở sàn y 44* · Area 1 · chặng Ride Chaser

Lên Ride Chaser (↑). Bảng hướng dẫn: giữ → tăng tốc, Space nhảy xe, Z bắn. Xe có thể dừng và lùi.
- **Thực thể:** Ride Armor / Chaser (8, 44) – Ride Chaser; Sniper (13, 44)

### R2 – Đường băng điện · đi ngang · độ khó 4
*x 26–152, y 34–46 (126×12 ô) · vào ở sàn y 44, ra ở sàn y 44* · Area 1 · chặng Ride Chaser

Ride Chaser: hai dốc nhảy, cột điện phóng hồ quang ngang (bật 1 s / tắt 2 s, có tia lửa báo trước), Drone lao từ phía sau. Tấm boost trên mặt đường tăng tốc lên 820 px/s để nhảy khe rộng.
- **Thông số:** hồ quang: bật 1 s / tắt 2 s, báo trước 0.5 s; boost 820 px/s trong 1.5 s
- **Địa hình:** sàn điện x 46–52, y 40–44 (hồ quang); dốc x 52–62 (y 44→41); hố vực (rơi = mất mạng) x 62–72 (rộng 10 ô); sàn điện x 92–98, y 40–44 (hồ quang); hố vực (rơi = mất mạng) x 108–120 (rộng 12 ô)
- **Thực thể:** Drone (36, 41); Sniper (82.6667, 44); Drone (87.3333, 41); Reploid cứu (103, 44); Drone (136, 41)
- **Đường chính dùng:** cưỡi xe

### R3 – Cầu sập · đi ngang · độ khó 5
*x 152–216, y 34–46 (64×12 ô) · vào ở sàn y 44, ra ở sàn y 44* · Area 1 · chặng Ride Chaser

Ride Chaser trên cầu treo: mặt cầu sập dần sau lưng khi xe đã đi qua (sập 1.5 s sau khi bánh xe rời khỏi). Không tự cuộn: đứng yên quá lâu trên một nhịp cầu thì nhịp đó sập. Cuối cầu nhảy vào cổng nhà máy.
- **Thông số:** nhịp cầu sập 1.5 s sau khi rời; đứng yên 3 s trên một nhịp thì sập
- **Địa hình:** hố vực (rơi = mất mạng) x 162–202 (rộng 40 ô); bệ sập x 162–170, y 44; bệ sập x 172–180, y 44; bệ sập x 182–190, y 43; bệ sập x 192–200, y 44
- **Thực thể:** Drone (204, 41)
- **Đường chính dùng:** cưỡi xe

### R3b – Trạm biến áp · đi ngang · độ khó 2
*x 216–239, y 34–46 (23×12 ô) · vào ở sàn y 44, ra ở sàn y 44* · Area 2 · tháp và lõi nhà máy

Xuống xe. Checkpoint 1. Heart Tank trên nóc trạm biến áp: đá tường lên vách trạm.
- **Địa hình:** khối x 228–231, y 42–44; khối x 231–233, y 38–42
- **Thực thể:** Checkpoint (224, 44); Heart Tank (232, 38) – nóc trạm
- **Đường chính dùng:** nhảy, rơi xuống
- **Lối bí mật:** (232, 42) → (232, 38) → (234, 38)

### R4 – Tháp tụ điện · leo dọc · độ khó 7
*x 239–259, y 2–46 (20×44 ô) · vào ở sàn y 44, ra ở sàn y 12* · Area 2 · tháp và lõi nhà máy

Cao trào. Tháp 20 ô rộng: bệ phản lực bật/tắt theo nhịp (đứng trên bệ đang tắt sẽ rơi), tia điện quét ngang mỗi 10 ô (báo trước bằng tia lửa ở hai đầu). Falcon Arm ở đỉnh tháp bên trái (dữ liệu game).
- **Thông số:** bệ phản lực: bật 2 s / tắt 1 s; tia điện quét ngang 2 s một lần, báo trước 0.6 s
- **Địa hình:** khối x 254–257, y 12–13; sàn điện x 241–257, y 32–33 (tia quét); sàn điện x 241–257, y 20–21 (tia quét); bệ phản lực x 243–246, y 41.5; bệ phản lực x 247.5–250.5, y 39; bệ phản lực x 253–256, y 36.5; bệ phản lực x 247.5–250.5, y 34; bệ phản lực x 243–246, y 31.5; bệ phản lực x 247.5–250.5, y 29; bệ phản lực x 253–256, y 26.5; bệ phản lực x 247.5–250.5, y 24; bệ phản lực x 243–246, y 21.5; bệ phản lực x 247.5–250.5, y 19; bệ phản lực x 253–256, y 16.5; bệ phản lực x 247.5–250.5, y 14; bệ phản lực x 252.5–255.5, y 14; bệ / kệ x 242–246, y 8
- **Thực thể:** Sniper (249, 34); Drone (249, 21); Drone (254, 11); Capsule giáp (244, 8) – Falcon Arm (đỉnh tháp)
- **Đường chính dùng:** nhảy
- **Lối bí mật:** (249, 12) → (244, 8)

### R5 – Phòng cuộn dây · đi ngang · độ khó 5
*x 259–305, y 2–14 (46×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · tháp và lõi nhà máy

Sàn nhiễm điện bật/tắt theo nhịp 1.2 s (vạch vàng sáng báo trước). Đứng trên cuộn dây (khối cách điện) để chờ. Reploid kẹt giữa hai cuộn dây. Checkpoint 2 ở đầu phòng.
- **Thông số:** sàn điện: bật 1.2 s / tắt 1.2 s; sát thương 4
- **Địa hình:** sàn điện x 263–271, y 10–12 (sàn điện 1.2 s); khối x 271–274, y 10–12; sàn điện x 276–286, y 10–12; khối x 286–289, y 10–12; sàn điện x 291–299, y 10–12
- **Thực thể:** Checkpoint (261, 12); Sniper (267, 12); Brute (279.333, 12); Reploid cứu (282.667, 12); Drone (295, 9)
- **Đường chính dùng:** nhảy, rơi xuống

### R6 – Hành lang lõi · đi ngang · độ khó 2
*x 305–325, y 2–14 (20×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · tháp và lõi nhà máy

Phòng nghỉ: Sub-Tank trong hốc tường (bắn vỡ nắp), Reploid, cửa boss.
- **Địa hình:** bệ / kệ x 314–317, y 9
- **Thực thể:** Reploid cứu (308, 12); Sub-Tank (315, 9) – hốc tường

### BOSS – Volt Kraken · đấu trường · độ khó 6
*x 325–355, y 2–14 (30×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Boss

Đấu trường có 4 cột thu sét ở hai bên.
- **Thực thể:** Boss (339, 12)

## Bảng kẻ địch và vật phẩm

| Loại | Phòng | x | y | Ghi chú |
|---|---|---|---|---|
| Ride Armor / Chaser | R1 | 8 | 44 | Ride Chaser |
| Sniper | R1 | 13 | 44 |  |
| Drone | R2 | 36 | 41 |  |
| Sniper | R2 | 82.6667 | 44 |  |
| Drone | R2 | 87.3333 | 41 |  |
| Reploid cứu | R2 | 103 | 44 |  |
| Drone | R2 | 136 | 41 |  |
| Drone | R3 | 204 | 41 |  |
| Checkpoint | R3b | 224 | 44 |  |
| Heart Tank | R3b | 232 | 38 | nóc trạm |
| Sniper | R4 | 249 | 34 |  |
| Drone | R4 | 249 | 21 |  |
| Drone | R4 | 254 | 11 |  |
| Capsule giáp | R4 | 244 | 8 | Falcon Arm (đỉnh tháp) |
| Checkpoint | R5 | 261 | 12 |  |
| Sniper | R5 | 267 | 12 |  |
| Brute | R5 | 279.333 | 12 |  |
| Reploid cứu | R5 | 282.667 | 12 |  |
| Drone | R5 | 295 | 9 |  |
| Reploid cứu | R6 | 308 | 12 |  |
| Sub-Tank | R6 | 315 | 9 | hốc tường |
| Boss | BOSS | 339 | 12 |  |

Tổng: 12 kẻ địch thường (Sniper 4, Drone 7, Brute 1), 3 Reploid, 2 checkpoint, Heart Tank 1, Sub-Tank 1, capsule 1.

## Capsule theo dữ liệu game
🛡️ Capsule Falcon Armor — Arm Part (X=5620, Y=350 — Đỉnh tháp Area 2): Sau khi hoàn thành chặng Ride Chaser ở Area 1, dùng chuỗi bệ đẩy Thruster và Wall-Jump leo lên đỉnh trụ tường X=5450 để mở Capsule mảnh tay Falcon. Area 1: Ride Chaser (Hoverbike) tốc độ cao -> Area 2: Trục leo tháp tụ điện lấy Falcon Arm Area 1 (0–3200px): Chế độ Ride Chaser (mô-tô bay) phóng tốc độ cao qua dốc nhảy và tấm tăng tốc Boost. Mid-Gate: Trạm ngắt điện. Area 2: Leo tháp tụ điện thẳng đứng bằng bệ đẩy Thruster và Wall-Jump để lấy Falcon Arm Part & mở cổng điện.

## Bí mật
| Vật phẩm | Phòng | Cách lấy |
|---|---|---|
| Capsule Falcon Arm | R4 | Kệ đỉnh tháp bên trái. |
| Heart Tank | R3b | Đá tường lên nóc trạm biến áp. |
| Sub-Tank | R6 | Bắn vỡ nắp hốc tường. |

## Boss
**Volt Kraken** · điểm yếu: Gel Shaver / F-Splasher
- **Bộ chiêu (dữ liệu game):** Tri-Thunder: Bắn 3 luồng sét chạy dọc theo tường và sàn. Electric Tentacle: Vươn xúc tu điện quất tầm trung. Spark Mine: Thả cầu điện lơ lửng phát nổ thành tia sét. Overdrive (Phase 2): Triệu hồi cột sét đánh liên tiếp từ trần xuống đấu trường.
- **Đấu trường:** sân 30×11 ô, 4 cột thu sét (2 mỗi bên) cao 3 ô làm vật che.
- **Pha 2 (dưới 50% HP):** Kraken nạp điện cho các cột: cột phóng hồ quang nối nhau theo nhịp 2 s, chia sân thành ô an toàn.

## Engine cần bổ sung
- Ride Chaser chạy tự do (người chơi chỉnh tốc độ, có lùi)
- Tấm boost
- Hồ quang theo nhịp
- Nhịp cầu sập sau khi rời
- Bệ phản lực bật/tắt
- Sàn điện theo nhịp

## Hình cần vẽ
- Đường băng nhà máy, cột điện
- Cầu treo + nhịp cầu sập
- Tháp tụ điện, bệ phản lực
- Cuộn dây cách điện
- Ride Chaser (có sẵn: bike)

## Kiểm tra tự động
Đường chính đã được kiểm tra theo khả năng nhảy (gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô, lướt-nhảy ≤ 7 ô, đi bộ phải có nền) và theo quy ước số lượng.

**Còn lỗi:**
- R4: nhảy xa 5.5 ô (> 5) tại x=10.0
- R4: nhảy xa 5.5 ô (> 5) tại x=15.5
- R4: nhảy xa 5.5 ô (> 5) tại x=10.0
- R4: nhảy xa 5.5 ô (> 5) tại x=15.5
- R4: nhảy xa 5.5 ô (> 5) tại x=10.0
- R4: nhảy xa 5.5 ô (> 5) tại x=15.5
- Mini-boss: 0 (chuẩn 1)
- Reploid cứu: 3 (chuẩn 4)
