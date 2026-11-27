# Phòng thí nghiệm Gate 1 — Boss Nightmare Mother

`x6_f2_nmother` · chủ đề `fire` · Pháo đài X6 · tổng ~160×46 ô (5120×1472 px)

![Sơ đồ](maps/x6_f2_nmother.png)

## Ý tưởng
Tầng 1 phòng thí nghiệm Gate: biển gai với bệ di động ngang, bệ xoay quanh trục, rồi trục thang máy có dung nham dâng liên tục tăng tốc (khó hơn giếng nham dâng của Lò Nham Thạch: không có kệ dừng).

## Tham khảo
X6 Gate Lab 1, Lò Nham Thạch R6 (nham dâng), X2 Magna Centipede (bệ).

## Chuẩn kích thước
Khung hình 640×360 px = 20×11.25 ô. Hành lang: trần 1 ô, trong lòng 9 ô, khối trần luôn nằm trong khung; phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô; đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô. X nhảy cao ~2.6 ô, xa ~5 ô: trên đường chính gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô (lướt-nhảy ≤ 7 ô); cao/xa hơn chỉ bằng đá tường, giáp hoặc cơ chế của màn, và dùng cho bí mật.

## Cấu trúc

- **Area 1** (R1 → R2): biển gai, bệ xoay
- **Mid** (MID): lõi Nightmare lửa
- **Area 2** (R3 → R7): trục thang máy dung nham
- **Boss** (BOSS): phòng lõi

## Nhịp màn (độ khó)
R1 (6) → R2 (6) → MID (5) → R3 (8) → R7 (2) → BOSS (7)

## Kịch bản từng phòng

### R1 – Biển gai · đi ngang · độ khó 6
*x 0–38, y 30–44 (38×14 ô) · vào ở sàn y 40, ra ở sàn y 40* · Area 1 · biển gai

Bệ di động ngang/dọc trên sàn gai. Drone đứng chặn trên đường bay của bệ.
- **Thông số:** bệ ±4 ô, chu kỳ 3 s
- **Địa hình:** hố gai x 4–30 (rộng 26 ô); bệ di động x 7–11, y 39; bệ di động x 15–19, y 38; bệ di động x 23–27, y 39
- **Thực thể:** Drone (2, 37); Drone (32, 37); Reploid cứu (36, 40)
- **Đường chính dùng:** bệ di động, nhảy

### R2 – Bệ xoay · đi ngang · độ khó 6
*x 38–74, y 30–44 (36×14 ô) · vào ở sàn y 40, ra ở sàn y 40* · Area 1 · biển gai

Bệ xoay quanh trục (1 vòng / 6 s), gai ở cả trên và dưới; đứng lâu ở đỉnh vòng là chạm gai trần.
- **Thông số:** bệ xoay 1 vòng / 6 s
- **Địa hình:** gai trần x 42–72; hố gai x 42–66 (rộng 24 ô); bệ xoay x 45–48, y 39; bệ xoay x 51–54, y 38; bệ xoay x 57–60, y 39; bệ xoay x 62–65, y 40
- **Thực thể:** Sniper (40, 40); Brute (71.3333, 40); Reploid cứu (72.6667, 40)
- **Đường chính dùng:** bệ di động, nhảy

### MID – Điểm dừng · đấu trường · độ khó 5
*x 74–98, y 30–42 (24×12 ô) · vào ở sàn y 40, ra ở sàn y 40* · Mid

Mini-boss: lõi Nightmare lửa 45 HP. Checkpoint 1.
- **Thông số:** cầu lửa 4 hướng mỗi 2 s
- **Thực thể:** Mini-boss (85, 40) – lõi lửa 45 HP; Checkpoint (96, 40)

### R3 – Trục thang máy dung nham · leo dọc · độ khó 8
*x 98–112, y 2–42 (14×40 ô) · vào ở sàn y 40, ra ở sàn y 12* · Area 2 · trục thang máy

Cao trào: dung nham dâng 70→90 px/s, không có kệ dừng; gai trên vách trái. Kệ so le 2.5 ô, Drone bay ngang. Checkpoint 2 ở đáy trục.
- **Thông số:** nham dâng 70→90 px/s, bắt đầu 1.5 s sau khi vào
- **Địa hình:** khối x 107–110, y 12–13; dung nham dâng x 100–110, y 34–40 (nham dâng 70→90); gai sàn x 100–100.6; bệ / kệ x 102–105, y 37.5; bệ / kệ x 106–109, y 35; bệ / kệ x 102–105, y 32.5; bệ / kệ x 106–109, y 30; bệ / kệ x 102–105, y 27.5; bệ / kệ x 106–109, y 25; bệ / kệ x 102–105, y 22.5; bệ / kệ x 106–109, y 20; bệ / kệ x 102–105, y 17.5; bệ / kệ x 106–109, y 15; bệ / kệ x 102–105, y 12.5
- **Thực thể:** Checkpoint (103, 40); Drone (107.5, 27); Sniper (107.5, 20); Reploid cứu (103.5, 12.5)
- **Đường chính dùng:** nhảy

### R7 – Trạm năng lượng · đi ngang · độ khó 2
*x 112–128, y 2–14 (16×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · trục thang máy

Trạm năng lượng lớn trước boss; Reploid cuối.
- **Thực thể:** Reploid cứu (115, 12); Năng lượng lớn (118, 12) – trạm năng lượng lớn; Drone (123, 9)

### BOSS – Nightmare Mother · đấu trường · độ khó 7
*x 128–158, y 2–14 (30×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Boss

Khối Nightmare lơ lửng, 4 lõi nguyên tố đổi màu.
- **Thực thể:** Boss (142, 12)

## Bảng kẻ địch và vật phẩm

| Loại | Phòng | x | y | Ghi chú |
|---|---|---|---|---|
| Drone | R1 | 2 | 37 |  |
| Drone | R1 | 32 | 37 |  |
| Reploid cứu | R1 | 36 | 40 |  |
| Sniper | R2 | 40 | 40 |  |
| Brute | R2 | 71.3333 | 40 |  |
| Reploid cứu | R2 | 72.6667 | 40 |  |
| Mini-boss | MID | 85 | 40 | lõi lửa 45 HP |
| Checkpoint | MID | 96 | 40 |  |
| Checkpoint | R3 | 103 | 40 |  |
| Drone | R3 | 107.5 | 27 |  |
| Sniper | R3 | 107.5 | 20 |  |
| Reploid cứu | R3 | 103.5 | 12.5 |  |
| Reploid cứu | R7 | 115 | 12 |  |
| Năng lượng lớn | R7 | 118 | 12 | trạm năng lượng lớn |
| Drone | R7 | 123 | 9 |  |
| Boss | BOSS | 142 | 12 |  |

Tổng: 7 kẻ địch thường (Sniper 2, Drone 4, Brute 1), 4 Reploid, 2 checkpoint, Heart Tank 0, Sub-Tank 0, capsule 0.

## Boss
**Nightmare Mother** · điểm yếu: Bắn vỡ Nightmare Orb để mảnh vỡ dội ngược vào Gate
- **Bộ chiêu (dữ liệu game):** Element Orbs (4 lõi nguyên tố), Cube Drop, Body Slam.
- **Đấu trường:** 30×11 ô.
- **Pha 2 (dưới 50% HP):** dung nham dâng 2 ô ở hai mép sân, lõi bắn đồng thời.

## Engine cần bổ sung
- Bệ di động ngang/dọc
- Bệ xoay quanh trục
- Dung nham dâng không dừng, tăng tốc

## Hình cần vẽ
- Biển gai phòng thí nghiệm
- Bệ xoay
- Trục thang máy + dung nham

## Kiểm tra tự động
Đường chính đã được kiểm tra theo khả năng nhảy (gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô, lướt-nhảy ≤ 7 ô, đi bộ phải có nền) và theo quy ước số lượng.

**Kết quả: đạt.**
