# Bắc Cực — Boss Blizzard Wolfang

`x6_wolfang` · chủ đề `ice` · Act II · X6 · tổng ~314×38 ô (10048×1216 px)

![Sơ đồ](maps/x6_wolfang.png)

## Ý tưởng
Area 1 là chặng Ride Chaser đổ dốc tuyết bị tuyết lở đuổi (người chơi tự lái, tuyết lở chậm hơn tốc độ tối đa). Area 2: vách băng cao trơn, hồ băng có băng nhọn rơi, sông băng trôi cao trào.

## Tham khảo
X6 Blizzard Wolfang (Bắc Cực, Ride Chaser), X1 Chill Penguin (băng), X8 Avalanche Yeti (tuyết lở).

## Chuẩn kích thước
Khung hình 640×360 px = 20×11.25 ô. Hành lang: trần 1 ô, trong lòng 9 ô, khối trần luôn nằm trong khung; phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô; đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô. X nhảy cao ~2.6 ô, xa ~5 ô: trên đường chính gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô (lướt-nhảy ≤ 7 ô); cao/xa hơn chỉ bằng đá tường, giáp hoặc cơ chế của màn, và dùng cho bí mật.

## Cấu trúc

- **Area 1** (R1 → R2): trạm trượt, dốc tuyết lở
- **Mid** (MID): trạm khí tượng
- **Area 2** (R3 → R4 → R6 → R5): vách băng, hồ băng, sông băng
- **Boss** (BOSS): hang băng lớn

## Nhịp màn (độ khó)
R1 (1) → R2 (5) → MID (5) → R3 (5) → R4 (5) → R6 (7) → R5 (2) → BOSS (6)

## Kịch bản từng phòng

### R1 – Trạm trượt · đi ngang · độ khó 1
*x 0–22, y 12–24 (22×12 ô) · vào ở sàn y 22, ra ở sàn y 22* · Area 1 · dốc tuyết

Lên Ride Chaser (↑). Bảng: tuyết lở sẽ đuổi, giữ tốc độ.
- **Thực thể:** Ride Armor / Chaser (8, 22) – Ride Chaser; Sniper (11, 22)

### R2 – Dốc tuyết lở · đi ngang · độ khó 5
*x 22–132, y 12–36 (110×24 ô) · vào ở sàn y 22, ra ở sàn y 32* · Area 1 · dốc tuyết

Ride Chaser xuống dốc dài 130 ô; tuyết lở đuổi phía sau 300 px/s (xe tối đa 560 px/s). Nhảy qua khe băng, né cây thông đổ, tảng băng lăn ngược chiều. Reploid trên mỏm đá giữa dốc (dừng xe lấy).
- **Thông số:** tuyết lở 300 px/s; tảng băng lăn mỗi 3 s
- **Địa hình:** tuyết lở x 22–42, y 13–22 (← tuyết lở đuổi 300 px/s); dốc x 22–42 (y 22→25); hố hố tuyết x 42–50 (rộng 8 ô); dốc x 56–76 (y 25→28); hố hố tuyết x 82–92 (rộng 10 ô); dốc x 98–118 (y 29→32)
- **Thực thể:** Drone (42, 22); Reploid cứu (79, 28); Drone (118, 29); Sniper (123, 32)
- **Đường chính dùng:** cưỡi xe

### MID – Trạm khí tượng · đấu trường · độ khó 5
*x 132–156, y 22–34 (24×12 ô) · vào ở sàn y 32, ra ở sàn y 32* · Mid

Xuống xe. Mini-boss: radar khí tượng 45 HP bắn băng đá; checkpoint 1.
- **Thông số:** băng đá 3 viên mỗi 2 s
- **Thực thể:** Mini-boss (143, 32) – radar 45 HP; Checkpoint (154, 32)

### R3 – Vách băng cao · leo dọc · độ khó 5
*x 156–170, y 2–34 (14×32 ô) · vào ở sàn y 32, ra ở sàn y 12* · Area 2 · vách và hồ băng

Bám tường băng X=3850 (trơn: trượt xuống nhanh hơn, đá tường vẫn được). Blade Body ở hốc cao bên trái (dữ liệu game).
- **Thông số:** vách băng: trượt 180 px/s khi bám
- **Địa hình:** khối x 165–168, y 12–13; tảng băng trôi x 160–163, y 29.5; tảng băng trôi x 164–167, y 27; tảng băng trôi x 160–163, y 24.5; tảng băng trôi x 164–167, y 22; tảng băng trôi x 160–163, y 19.5; tảng băng trôi x 164–167, y 17; tảng băng trôi x 160–163, y 14.5; bệ / kệ x 159–163, y 8
- **Thực thể:** Drone (161.5, 21.5); Sniper (161.5, 14.5); Capsule giáp (161, 8) – Blade Body (hốc cao)
- **Đường chính dùng:** nhảy
- **Lối bí mật:** (165, 12) → (161, 8)

### R4 – Hồ băng · đi ngang · độ khó 5
*x 170–206, y 2–16 (36×14 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · vách và hồ băng

Sàn băng trơn, băng nhọn rơi từ trần theo nhịp (rung 0.6 s trước). Heart Tank trên tảng băng trôi giữa hồ.
- **Thông số:** băng nhọn mỗi 2 s; sàn trơn ×0.3
- **Địa hình:** hố nước sâu x 176–192 (rộng 16 ô); tảng băng trôi x 179–183, y 11; tảng băng trôi x 186–189, y 11
- **Thực thể:** Sniper (173, 12); Heart Tank (186, 11) – tảng băng trôi; Brute (199, 12)
- **Đường chính dùng:** bệ di động, nhảy

### R6 – Sông băng trôi · đi ngang · độ khó 7
*x 206–264, y 2–16 (58×14 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · vách và hồ băng

Cao trào: tảng băng trôi xuôi dòng (80 px/s) chìm dần khi đứng; tảng băng lăn từ thượng nguồn. Checkpoint 2 ở bờ đầu.
- **Thông số:** tảng băng chìm sau 2 s; băng lăn mỗi 2.5 s
- **Địa hình:** hố nước sâu x 210–236 (rộng 26 ô); tảng băng trôi x 213–217, y 11; tảng băng trôi x 220–224, y 11; tảng băng trôi x 227–230, y 10; tảng băng trôi x 232–235, y 11; hố nước sâu x 240–256 (rộng 16 ô); tảng băng trôi x 243–247, y 11; tảng băng trôi x 250–253, y 11
- **Thực thể:** Checkpoint (208, 12); Drone (208, 9); Reploid cứu (238, 12); Drone (262, 9)
- **Đường chính dùng:** bệ di động, nhảy

### R5 – Hang băng · đi ngang · độ khó 2
*x 264–282, y 2–14 (18×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · vách và hồ băng

Phòng nghỉ: Sub-Tank trong khối băng (bắn vỡ), hai Reploid, cửa boss.
- **Thực thể:** Reploid cứu (267, 12); Sub-Tank (272, 12) – khối băng; Reploid cứu (273, 12); Sniper (279, 12)

### BOSS – Blizzard Wolfang · đấu trường · độ khó 6
*x 282–312, y 2–14 (30×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Boss

Sàn đấu đóng băng dần (trơn); sói phóng băng.
- **Thực thể:** Boss (296, 12)

## Bảng kẻ địch và vật phẩm

| Loại | Phòng | x | y | Ghi chú |
|---|---|---|---|---|
| Ride Armor / Chaser | R1 | 8 | 22 | Ride Chaser |
| Sniper | R1 | 11 | 22 |  |
| Drone | R2 | 42 | 22 |  |
| Reploid cứu | R2 | 79 | 28 |  |
| Drone | R2 | 118 | 29 |  |
| Sniper | R2 | 123 | 32 |  |
| Mini-boss | MID | 143 | 32 | radar 45 HP |
| Checkpoint | MID | 154 | 32 |  |
| Drone | R3 | 161.5 | 21.5 |  |
| Sniper | R3 | 161.5 | 14.5 |  |
| Capsule giáp | R3 | 161 | 8 | Blade Body (hốc cao) |
| Sniper | R4 | 173 | 12 |  |
| Heart Tank | R4 | 186 | 11 | tảng băng trôi |
| Brute | R4 | 199 | 12 |  |
| Checkpoint | R6 | 208 | 12 |  |
| Drone | R6 | 208 | 9 |  |
| Reploid cứu | R6 | 238 | 12 |  |
| Drone | R6 | 262 | 9 |  |
| Reploid cứu | R5 | 267 | 12 |  |
| Sub-Tank | R5 | 272 | 12 | khối băng |
| Reploid cứu | R5 | 273 | 12 |  |
| Sniper | R5 | 279 | 12 |  |
| Boss | BOSS | 296 | 12 |  |

Tổng: 11 kẻ địch thường (Sniper 5, Drone 5, Brute 1), 4 Reploid, 2 checkpoint, Heart Tank 1, Sub-Tank 1, capsule 1.

## Capsule theo dữ liệu game
🛡️ Capsule Blade Armor — Body Part (X=4020, Y=350 — Vách băng cao đầu Area 2 [YT 35:01]): Sau chặng trượt Ride Chaser né tuyết lở, bám tường băng X=3850 nhảy lên bệ kính cao X=3920. Area 1: Ride Chaser trượt dốc tuyết lở Avalanche -> Area 2: Vách băng cao lấy Blade Body Area 1 (0–3200px): Ride Chaser trượt tốc độ cao trên dốc tuyết lở Avalanche né các tảng băng lăn khổng lồ. Area 2: Vách băng cao giấu Blade Body Part và đoạn hành lang khối băng trôi sát trần gai ở cuối màn.

## Bí mật
| Vật phẩm | Phòng | Cách lấy |
|---|---|---|
| Capsule Blade Body | R3 | Hốc cao bên trái vách băng. |
| Heart Tank | R4 | Tảng băng trôi giữa hồ. |
| Sub-Tank | R5 | Bắn vỡ khối băng. |

## Boss
**Blizzard Wolfang** · điểm yếu: Magma Blade / Shoenzan
- **Bộ chiêu (dữ liệu game):** Ice Burst: Tạo khối băng bay thẳng rồi vỡ thành mảnh băng sắc nhọn. Wall Cling Pounce: Bám lên tường/trần rồi phóng xuống vồ người chơi. Slide Tackle: Trượt băng tốc độ cao trên mặt sàn. Overdrive (Phase 2): Hú gọi mưa băng từ trần và lao vồ liên tục.
- **Đấu trường:** hang băng 30×11 ô.
- **Pha 2 (dưới 50% HP):** sàn đóng băng toàn phần (trơn ×0.2), băng nhọn rơi từ trần theo hàng.

## Engine cần bổ sung
- Ride Chaser đổ dốc (người chơi tự lái)
- Tuyết lở đuổi chậm hơn tốc độ tối đa
- Tảng băng lăn
- Vách băng trơn
- Tảng băng trôi chìm dần

## Hình cần vẽ
- Dốc tuyết + cây thông đổ
- Tuyết lở (mặt trước)
- Vách băng
- Tảng băng trôi
- Ride Chaser (có sẵn)

## Kiểm tra tự động
Đường chính đã được kiểm tra theo khả năng nhảy (gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô, lướt-nhảy ≤ 7 ô, đi bộ phải có nền) và theo quy ước số lượng.

**Kết quả: đạt.**
