# Zero Space 1 — Boss Dynamo

`x5_f1_dynamo` · chủ đề `shadow` · Pháo đài X5 · tổng ~244×34 ô (7808×1088 px)

![Sơ đồ](maps/x5_f1_dynamo.png)

## Ý tưởng
Pháo đài Sigma tầng 1: các cụm laser quét toàn chiều cao hành lang, buộc người chơi chạy giữa các hốc trú trong sàn. Băng chuyền tốc độ cao làm khó canh nhịp. Area 1 làm quen, Area 2 phối hợp nhiều nhịp laser.

## Tham khảo
X5 Zero Space 1 (laser quét), X6 Gate Lab (tia dọc), X3 Doppler stage 1.

## Chuẩn kích thước
Khung hình 640×360 px = 20×11.25 ô. Hành lang: trần 1 ô, trong lòng 9 ô, khối trần luôn nằm trong khung; phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô; đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô. X nhảy cao ~2.6 ô, xa ~5 ô: trên đường chính gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô (lướt-nhảy ≤ 7 ô); cao/xa hơn chỉ bằng đá tường, giáp hoặc cơ chế của màn, và dùng cho bí mật.

## Cấu trúc

- **Area 1** (R1 → R2 → R3): làm quen laser + hốc trú
- **Mid** (MID): lõi laser
- **Area 2** (R4 → R6 → R7): phối hợp nhiều nhịp laser
- **Boss** (BOSS): đấu trường trống

## Nhịp màn (độ khó)
R1 (3) → R2 (5) → R3 (5) → MID (5) → R4 (6) → R6 (8) → R7 (2) → BOSS (7)

## Kịch bản từng phòng

### R1 – Cổng pháo đài · đi ngang · độ khó 3
*x 0–30, y 20–32 (30×12 ô) · vào ở sàn y 30, ra ở sàn y 30* · Area 1 · cổng pháo đài

Laser quét #1 chậm (từ trái sang, 140 px/s). Ba hốc trú trong sàn gần nhau (cách 6 ô): nằm vào hốc khi tia đi qua.
- **Thông số:** laser #1 140 px/s, còi báo 1 s trước khi quét
- **Địa hình:** tia laser x 0–30, y 21–30 (laser #1 quét →)
- **Thực thể:** Sniper (3, 30); Reploid cứu (21, 30)

### R2 – Hành lang băng chuyền · đi ngang · độ khó 5
*x 30–70, y 20–32 (40×12 ô) · vào ở sàn y 30, ra ở sàn y 30* · Area 1 · cổng pháo đài

Băng chuyền nhanh 200 px/s và laser #2–#3 quét ngược chiều nhau; hốc trú xa nhau 10 ô. Drone thả mìn lên băng chuyền.
- **Thông số:** băng chuyền 200 px/s; laser #2 160 px/s →, #3 160 px/s ←
- **Địa hình:** tia laser x 30–70, y 21–30 (laser #2 → / #3 ←); băng chuyền x 30–44 (+200 px/s); vùng tối x 44–47, y 29.8–30.8; băng chuyền x 48–62 (+200 px/s); vùng tối x 62–65, y 29.8–30.8
- **Thực thể:** Drone (37, 30); Brute (55, 30)
- **Đường chính dùng:** băng chuyền

### R3 – Giếng tia · leo dọc · độ khó 5
*x 70–84, y 2–32 (14×30 ô) · vào ở sàn y 30, ra ở sàn y 12* · Area 1 · cổng pháo đài

Leo giếng trong khi laser quét dọc theo chiều cao (từ dưới lên, 100 px/s). Kệ có hốc trú phía sau vách.
- **Thông số:** laser dọc quét lên 100 px/s mỗi 5 s
- **Địa hình:** khối x 79–82, y 12–13; tia laser x 72–82, y 22–23 (laser quét lên); bệ / kệ x 74–77, y 27.5; bệ / kệ x 78–81, y 25; bệ / kệ x 74–77, y 22.5; bệ / kệ x 78–81, y 20; bệ / kệ x 74–77, y 17.5; bệ / kệ x 78–81, y 15; bệ / kệ x 74–77, y 12.5
- **Thực thể:** Drone (75.5, 14.5); Reploid cứu (75.5, 12.5)
- **Đường chính dùng:** nhảy

### MID – Điểm dừng · đấu trường · độ khó 5
*x 84–108, y 2–14 (24×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Mid

Mini-boss: lõi laser 45 HP điều khiển 2 tia chéo. Checkpoint 1 sau trận.
- **Thông số:** 2 tia chéo xoay 30°/s
- **Thực thể:** Mini-boss (95, 12) – lõi laser 45 HP; Checkpoint (106, 12)

### R4 – Hành lang cuối · đi ngang · độ khó 6
*x 108–148, y 2–14 (40×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · hành lang tử thần

Laser #4–#5 nhịp khác nhau (3 s và 4.5 s). Khối chắn che hốc trú phải bắn vỡ trước (8 HP).
- **Thông số:** laser #4 mỗi 3 s, #5 mỗi 4.5 s; khối chắn 8 HP
- **Địa hình:** tia laser x 108–148, y 3–12 (laser #4 / #5); khối x 116–118, y 11–12; khối x 130–132, y 11–12
- **Thực thể:** Sniper (112, 12); Drone (125, 9); Reploid cứu (139, 12)
- **Đường chính dùng:** nhảy, rơi xuống

### R6 – Hành lang tử thần · đi ngang · độ khó 8
*x 148–196, y 2–14 (48×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · hành lang tử thần

Cao trào: ba laser phối hợp + băng chuyền ngược −160 px/s. Hốc trú chỉ đủ 1 lần tia qua, phải chạy liên tục. Checkpoint 2 ở đầu phòng.
- **Thông số:** laser #6 2.5 s, #7 3.5 s, #8 4 s; băng chuyền −160 px/s
- **Địa hình:** tia laser x 152–196, y 3–12 (laser #6/#7/#8); băng chuyền x 152–168 (-160 px/s); vùng tối x 168–171, y 11.8–12.8; băng chuyền x 172–188 (-160 px/s); vùng tối x 188–191, y 11.8–12.8
- **Thực thể:** Checkpoint (150, 12); Sniper (160, 12); Drone (180, 12); Reploid cứu (192, 12)
- **Đường chính dùng:** băng chuyền

### R7 – Trạm năng lượng · đi ngang · độ khó 2
*x 196–212, y 2–14 (16×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · hành lang tử thần

Trạm năng lượng lớn trước boss (hồi đầy HP + WEP).
- **Thực thể:** Năng lượng lớn (202, 12) – trạm năng lượng lớn

### BOSS – Dynamo · đấu trường · độ khó 7
*x 212–242, y 2–14 (30×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Boss

Đấu trường trống; Dynamo ném boomerang và gọi mạch nước nóng.
- **Thực thể:** Boss (226, 12)

## Bảng kẻ địch và vật phẩm

| Loại | Phòng | x | y | Ghi chú |
|---|---|---|---|---|
| Sniper | R1 | 3 | 30 |  |
| Reploid cứu | R1 | 21 | 30 |  |
| Drone | R2 | 37 | 30 |  |
| Brute | R2 | 55 | 30 |  |
| Drone | R3 | 75.5 | 14.5 |  |
| Reploid cứu | R3 | 75.5 | 12.5 |  |
| Mini-boss | MID | 95 | 12 | lõi laser 45 HP |
| Checkpoint | MID | 106 | 12 |  |
| Sniper | R4 | 112 | 12 |  |
| Drone | R4 | 125 | 9 |  |
| Reploid cứu | R4 | 139 | 12 |  |
| Checkpoint | R6 | 150 | 12 |  |
| Sniper | R6 | 160 | 12 |  |
| Drone | R6 | 180 | 12 |  |
| Reploid cứu | R6 | 192 | 12 |  |
| Năng lượng lớn | R7 | 202 | 12 | trạm năng lượng lớn |
| Boss | BOSS | 226 | 12 |  |

Tổng: 8 kẻ địch thường (Sniper 3, Drone 4, Brute 1), 4 Reploid, 2 checkpoint, Heart Tank 0, Sub-Tank 0, capsule 0.

## Boss
**Dynamo**
- **Bộ chiêu (dữ liệu game):** Boomerang Saber (ném vòng cung), Geyser (mạch nước nóng từ sàn), Leap Slash (nhảy chém).
- **Đấu trường:** đấu trường 30×11 ô trống.
- **Pha 2 (dưới 50% HP):** laser quét từ pháo đài bật lại theo nhịp 6 s trong lúc đấu.

## Engine cần bổ sung
- Laser quét toàn chiều cao + còi báo
- Hốc trú trong sàn
- Băng chuyền nhanh
- Khối chắn bắn vỡ

## Hình cần vẽ
- Hành lang pháo đài Sigma
- Đầu phát laser
- Hốc trú có nắp
- Băng chuyền tốc độ cao

## Kiểm tra tự động
Đường chính đã được kiểm tra theo khả năng nhảy (gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô, lướt-nhảy ≤ 7 ô, đi bộ phải có nền) và theo quy ước số lượng.

**Kết quả: đạt.**
