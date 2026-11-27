# Phòng thí nghiệm Gate 2 — Boss High Max

`x6_f3_highmax` · chủ đề `core` · Pháo đài X6 · tổng ~198×34 ô (6336×1088 px)

![Sơ đồ](maps/x6_f3_highmax.png)

## Ý tưởng
Vực gai toàn khu vực: chuỗi bệ nhỏ 2 ô có cột Totem chặn (phá mới đứng được), băng chuyền chạy dưới tia laser dọc chạy ngang. Cao trào ở chuỗi bệ nhỏ thứ hai.

## Tham khảo
X6 Gate Lab 2, X5 Zero Space 2 (bệ nhỏ), X1 Sigma stage.

## Chuẩn kích thước
Khung hình 640×360 px = 20×11.25 ô. Hành lang: trần 1 ô, trong lòng 9 ô, khối trần luôn nằm trong khung; phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô; đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô. X nhảy cao ~2.6 ô, xa ~5 ô: trên đường chính gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô (lướt-nhảy ≤ 7 ô); cao/xa hơn chỉ bằng đá tường, giáp hoặc cơ chế của màn, và dùng cho bí mật.

## Cấu trúc

- **Area 1** (R1 → R2): bệ nhỏ, băng chuyền laser
- **Mid** (MID): Totem chủ
- **Area 2** (R5 → R6 → R7): chuỗi bệ nhỏ 2, tháp totem
- **Boss** (BOSS): phòng High Max

## Nhịp màn (độ khó)
R1 (6) → R2 (6) → MID (5) → R5 (8) → R6 (7) → R7 (2) → BOSS (7)

## Kịch bản từng phòng

### R1 – Bệ nhỏ · đi ngang · độ khó 6
*x 0–36, y 18–32 (36×14 ô) · vào ở sàn y 28, ra ở sàn y 28* · Area 1 · chuỗi bệ nhỏ

Bệ 2×1 ô trên vực gai; cột Totem trên bệ (6 HP) phải phá mới đứng được.
- **Thông số:** Totem bắn 1 viên mỗi 2 s
- **Địa hình:** hố gai x 4–28 (rộng 24 ô); bệ / kệ x 7–9, y 27; bệ / kệ x 12–14, y 26; bệ / kệ x 17–19, y 27; bệ / kệ x 22–24, y 27
- **Thực thể:** Drone (2, 25); Reploid cứu (34, 28)
- **Đường chính dùng:** nhảy

### R2 – Băng chuyền laser · đi ngang · độ khó 6
*x 36–74, y 18–30 (38×12 ô) · vào ở sàn y 28, ra ở sàn y 28* · Area 1 · chuỗi bệ nhỏ

Băng chuyền chạy nhanh 180 px/s dưới tia laser dọc chạy ngang (vạch đỏ trên sàn báo vị trí).
- **Thông số:** laser dọc 200 px/s; băng 180 px/s
- **Địa hình:** tia laser x 40–70, y 19–28 (laser dọc chạy ngang); băng chuyền x 40–54 (+180 px/s); băng chuyền x 58–70 (-180 px/s)
- **Thực thể:** Sniper (38, 28); Drone (47, 28); Reploid cứu (72, 28)
- **Đường chính dùng:** băng chuyền

### MID – Điểm dừng · đấu trường · độ khó 5
*x 74–98, y 18–30 (24×12 ô) · vào ở sàn y 28, ra ở sàn y 28* · Mid

Mini-boss: Totem chủ 45 HP. Checkpoint 1.
- **Thông số:** 3 tầng bắn luân phiên
- **Thực thể:** Mini-boss (85, 28) – Totem chủ 45 HP; Checkpoint (96, 28)

### R5 – Chuỗi bệ nhỏ 2 · đi ngang · độ khó 8
*x 98–136, y 18–32 (38×14 ô) · vào ở sàn y 28, ra ở sàn y 28* · Area 2 · tháp totem

Cao trào: bệ nhỏ 2 ô + Totem + laser dọc chạy ngang qua chuỗi; Drone bay giữa. Checkpoint 2 ở bệ cứng đầu.
- **Thông số:** laser 220 px/s
- **Địa hình:** tia laser x 102–132, y 19–28 (laser dọc); hố gai x 102–128 (rộng 26 ô); bệ / kệ x 105–107, y 27; bệ / kệ x 110–112, y 26; bệ / kệ x 115–117, y 27; bệ / kệ x 120–122, y 26; bệ / kệ x 125–127, y 27
- **Thực thể:** Checkpoint (100, 28); Drone (130, 25); Sniper (133.333, 28); Reploid cứu (134.667, 28)
- **Đường chính dùng:** nhảy

### R6 – Tháp totem · leo dọc · độ khó 7
*x 136–150, y 2–30 (14×28 ô) · vào ở sàn y 28, ra ở sàn y 12* · Area 2 · tháp totem

Leo giữa các totem bắn đạn ngang.
- **Thông số:** totem bắn mỗi 1.8 s
- **Địa hình:** khối x 145–148, y 12–13; bệ / kệ x 140–143, y 25.5; bệ / kệ x 144–147, y 23; bệ / kệ x 140–143, y 20.5; bệ / kệ x 144–147, y 18; bệ / kệ x 140–143, y 15.5; bệ / kệ x 141–144, y 13
- **Thực thể:** Drone (141.5, 17.5); Reploid cứu (142.5, 13)
- **Đường chính dùng:** nhảy

### R7 – Trạm năng lượng · đi ngang · độ khó 2
*x 150–166, y 2–14 (16×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · tháp totem

Trạm năng lượng lớn trước boss.
- **Thực thể:** Năng lượng lớn (156, 12) – trạm năng lượng lớn; Brute (161, 12)

### BOSS – High Max · đấu trường · độ khó 7
*x 166–196, y 2–14 (30×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Boss

Khiên bất khả xâm phạm; dùng Charge Saber của Blade (giữ ↑ rồi thả) để làm choáng.
- **Thực thể:** Boss (180, 12)

## Bảng kẻ địch và vật phẩm

| Loại | Phòng | x | y | Ghi chú |
|---|---|---|---|---|
| Drone | R1 | 2 | 25 |  |
| Reploid cứu | R1 | 34 | 28 |  |
| Sniper | R2 | 38 | 28 |  |
| Drone | R2 | 47 | 28 |  |
| Reploid cứu | R2 | 72 | 28 |  |
| Mini-boss | MID | 85 | 28 | Totem chủ 45 HP |
| Checkpoint | MID | 96 | 28 |  |
| Checkpoint | R5 | 100 | 28 |  |
| Drone | R5 | 130 | 25 |  |
| Sniper | R5 | 133.333 | 28 |  |
| Reploid cứu | R5 | 134.667 | 28 |  |
| Drone | R6 | 141.5 | 17.5 |  |
| Reploid cứu | R6 | 142.5 | 13 |  |
| Năng lượng lớn | R7 | 156 | 12 | trạm năng lượng lớn |
| Brute | R7 | 161 | 12 |  |
| Boss | BOSS | 180 | 12 |  |

Tổng: 7 kẻ địch thường (Sniper 2, Drone 4, Brute 1), 4 Reploid, 2 checkpoint, Heart Tank 0, Sub-Tank 0, capsule 0.

## Boss
**High Max** · điểm yếu: Bắn vỡ Nightmare Orb để mảnh vỡ dội ngược vào Gate
- **Bộ chiêu (dữ liệu game):** Orb Barrage, Shield (bất khả xâm phạm trừ khi choáng), Teleport.
- **Đấu trường:** 30×11 ô.
- **Pha 2 (dưới 50% HP):** High Max tạo 2 khiên quỹ đạo; chỉ choáng được khi cả hai khiên ở phía sau.

## Engine cần bổ sung
- Bệ nhỏ có Totem chặn
- Laser dọc chạy ngang
- Băng chuyền nhanh
- Boss cần làm choáng bằng Charge Saber

## Hình cần vẽ
- Bệ nhỏ 2 ô
- Cột Totem
- Laser dọc

## Kiểm tra tự động
Đường chính đã được kiểm tra theo khả năng nhảy (gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô, lướt-nhảy ≤ 7 ô, đi bộ phải có nền) và theo quy ước số lượng.

**Kết quả: đạt.**
