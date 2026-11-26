# Zero Space 1 — Boss Dynamo

`x5_f1_dynamo` · chủ đề `shadow` · Pháo đài Act I · tổng chiều ngang khoảng 254 ô (8128px)

![Sơ đồ](maps/x5_f1_dynamo.png)

## Ý tưởng
Pháo đài Sigma: 6 cụm laser tử thần quét toàn màn hình, buộc người chơi chạy giữa các hốc trú ẩn. Băng chuyền tốc độ cao làm khó canh nhịp.

## Tham khảo
X5 Zero Space 1, X4 final stages (laser quét màn hình), X8 Jakob (trần ép).

## Nhịp màn
R1 (3) → R2 (5) → R3 (5) → MID (2) → R4 (6) → BOSS (7)

## Kịch bản từng phòng

### R1 – Cổng pháo đài (40×16 ô, đi ngang) · độ khó 3
Laser quét #1 chậm, có 3 hốc trú ẩn gần nhau để làm quen.
- **Bẫy:** laser màn
- **Đặt trong phòng:** Sniper

### R2 – Hành lang băng chuyền (70×16 ô, đi ngang) · độ khó 5
Băng chuyền nhanh (200px/s) và laser quét #2–#3; hốc trú ẩn xa nhau hơn.
- **Bẫy:** laser màn
- **Đặt trong phòng:** Drone, Brute

### R3 – Giếng tia (20×40 ô, leo dọc) · độ khó 5
Leo lên trong khi laser quét dọc theo chiều cao.
- **Bẫy:** laser dọc
- **Đặt trong phòng:** Drone

### MID – Điểm dừng (24×17 ô, đi ngang) · độ khó 2
Checkpoint, nạp năng lượng.
- **Đặt trong phòng:** Checkpoint

### R4 – Hành lang cuối (70×16 ô, đi ngang) · độ khó 6
Laser #5–#6 phối hợp nhịp khác nhau; khối blocks chặn hốc trú ẩn phải bắn vỡ.
- **Bẫy:** laser màn
- **Đặt trong phòng:** Drone, Sniper

### BOSS – Dynamo (30×17 ô, đấu trường) · độ khó 7
Đấu trường trống, Dynamo ném boomerang và gọi mạch nước nóng.
- **Đặt trong phòng:** Boss

## Cơ chế mới cần engine
- Laser quét toàn màn hình + hốc trú ẩn

## Hình ảnh / element
terrain-shadow, native-panel, fx-laser phóng to cho laser màn hình, mmx5_v-block cho khối chặn hốc.
