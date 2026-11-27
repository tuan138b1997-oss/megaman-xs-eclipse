# Zero Space Final — Boss Final Sigma W

`x5_f4_sigma` · chủ đề `core` · Pháo đài X5 · tổng ~178×64 ô (5696×2048 px)

![Sơ đồ](maps/x5_f4_sigma.png)

## Ý tưởng
Màn cuối Act I gom các đối tượng đã gặp: bệ di động trên vực + laser, giếng trọng lực, virus Sigma đuổi theo, rồi trục lõi virus với bệ chạy vòng quanh tâm. Kết thúc ở phòng quyết chiến Sigma.

## Tham khảo
X5 Zero Space 4 (tổng hợp), X1 Sigma (đấu cuối), X8 Jakob elevator.

## Chuẩn kích thước
Khung hình 640×360 px = 20×11.25 ô. Hành lang: trần 1 ô, trong lòng 9 ô, khối trần luôn nằm trong khung; phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô; đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô. X nhảy cao ~2.6 ô, xa ~5 ô: trên đường chính gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô (lướt-nhảy ≤ 7 ô); cao/xa hơn chỉ bằng đá tường, giáp hoặc cơ chế của màn, và dùng cho bí mật.

## Cấu trúc

- **Area 1** (R1 → R2): tổng hợp các đối tượng Act I
- **Mid** (MID): cổng virus
- **Area 2** (R3 → R5 → R7): hành lang Sigma, trục lõi virus
- **Boss** (BOSS): phòng quyết chiến

## Nhịp màn (độ khó)
R1 (5) → R2 (6) → MID (5) → R3 (6) → R5 (8) → R7 (2) → BOSS (8)

## Kịch bản từng phòng

### R1 – Tổng hợp 1 · đi ngang · độ khó 5
*x 0–40, y 48–62 (40×14 ô) · vào ở sàn y 58, ra ở sàn y 58* · Area 1 · tổng hợp

Bệ di động trên vực + laser quét (nhắc Zero Space 1–2).
- **Thông số:** laser 160 px/s; bệ ±3 ô
- **Địa hình:** hố vực (rơi = mất mạng) x 4–26 (rộng 22 ô); bệ di động x 7–11, y 57; bệ di động x 15–19, y 57; bệ di động x 22–25, y 58; tia laser x 30–40, y 49–58 (laser quét)
- **Thực thể:** Sniper (2, 58); Drone (35, 55); Reploid cứu (39, 58)
- **Đường chính dùng:** bệ di động, nhảy

### R2 – Tổng hợp 2 · leo dọc · độ khó 6
*x 40–54, y 30–60 (14×30 ô) · vào ở sàn y 58, ra ở sàn y 40* · Area 1 · tổng hợp

Giếng trọng lực biến thiên + gai (nhắc Zero Space 3).
- **Thông số:** trọng lực ×0.6 ↔ ×1.4 mỗi 3 s
- **Địa hình:** khối x 49–52, y 40–41; đảo trọng lực x 42–52, y 32–58 (trọng lực biến thiên); gai sàn x 42–42.6; bệ / kệ x 44–47, y 55.5; bệ / kệ x 48–51, y 53; bệ / kệ x 44–47, y 50.5; bệ / kệ x 48–51, y 48; bệ / kệ x 44–47, y 45.5; bệ / kệ x 48–51, y 43; bệ / kệ x 44–47, y 40.5
- **Thực thể:** Drone (49.5, 45); Reploid cứu (45.5, 40.5)
- **Đường chính dùng:** nhảy

### MID – Cổng quyết chiến · đấu trường · độ khó 5
*x 54–78, y 30–42 (24×12 ô) · vào ở sàn y 40, ra ở sàn y 40* · Mid

Mini-boss: cổng virus 45 HP sinh virus Sigma. Checkpoint 1.
- **Thông số:** sinh virus mỗi 3 s
- **Thực thể:** Mini-boss (65, 40) – cổng virus 45 HP; Checkpoint (76, 40)

### R3 – Hành lang Sigma · đi ngang · độ khó 6
*x 78–110, y 30–42 (32×12 ô) · vào ở sàn y 40, ra ở sàn y 40* · Area 2 · trục lõi virus

Virus Sigma bay theo người chơi (chậm 120 px/s, bắn tan được), vùng làm chậm ở giữa.
- **Thông số:** virus bám 120 px/s
- **Địa hình:** vùng chậm x 86–98, y 31–40 (vùng chậm)
- **Thực thể:** Drone (82, 37); Sniper (92, 40); Brute (100.667, 40); Reploid cứu (103.333, 40)

### R5 – Trục lõi virus · leo dọc · độ khó 8
*x 110–130, y 2–42 (20×40 ô) · vào ở sàn y 40, ra ở sàn y 12* · Area 2 · trục lõi virus

Cao trào: trục dọc rộng 20 ô, bệ chạy vòng quanh lõi ở tâm (bán kính 6 ô, 1 vòng / 8 s); virus bay ra từ lõi. Checkpoint 2 ở đáy trục.
- **Thông số:** bệ quay 1 vòng / 8 s; virus mỗi 2.5 s
- **Địa hình:** khối x 125–128, y 12–13; sàn điện x 118–122, y 16–20 (lõi virus); bệ xoay x 114–117, y 37.5; bệ xoay x 119–122, y 35; bệ xoay x 124–127, y 32.5; bệ xoay x 119–122, y 30; bệ xoay x 114–117, y 27.5; bệ xoay x 119–122, y 25; bệ xoay x 124–127, y 22.5; bệ xoay x 119–122, y 20; bệ xoay x 114–117, y 17.5; bệ xoay x 119–122, y 15; bệ xoay x 121–124, y 12.5
- **Thực thể:** Checkpoint (116, 40); Drone (120.5, 27); Reploid cứu (115.5, 17.5)
- **Đường chính dùng:** nhảy

### R7 – Trạm năng lượng · đi ngang · độ khó 2
*x 130–146, y 2–14 (16×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · trục lõi virus

Trạm năng lượng lớn trước phòng quyết chiến.
- **Thực thể:** Năng lượng lớn (136, 12) – trạm năng lượng lớn

### BOSS – Final Sigma W · đấu trường · độ khó 8
*x 146–176, y 2–14 (30×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Boss

Hai pha: thân Sigma rồi đầu Sigma khổng lồ.
- **Thực thể:** Boss (160, 12)

## Bảng kẻ địch và vật phẩm

| Loại | Phòng | x | y | Ghi chú |
|---|---|---|---|---|
| Sniper | R1 | 2 | 58 |  |
| Drone | R1 | 35 | 55 |  |
| Reploid cứu | R1 | 39 | 58 |  |
| Drone | R2 | 49.5 | 45 |  |
| Reploid cứu | R2 | 45.5 | 40.5 |  |
| Mini-boss | MID | 65 | 40 | cổng virus 45 HP |
| Checkpoint | MID | 76 | 40 |  |
| Drone | R3 | 82 | 37 |  |
| Sniper | R3 | 92 | 40 |  |
| Brute | R3 | 100.667 | 40 |  |
| Reploid cứu | R3 | 103.333 | 40 |  |
| Checkpoint | R5 | 116 | 40 |  |
| Drone | R5 | 120.5 | 27 |  |
| Reploid cứu | R5 | 115.5 | 17.5 |  |
| Năng lượng lớn | R7 | 136 | 12 | trạm năng lượng lớn |
| Boss | BOSS | 160 | 12 |  |

Tổng: 7 kẻ địch thường (Sniper 2, Drone 4, Brute 1), 4 Reploid, 2 checkpoint, Heart Tank 0, Sub-Tank 0, capsule 0.

## Boss
**Final Sigma W**
- **Bộ chiêu (dữ liệu game):** Virus Swarm, Cube Drop, Sigma Beam (đầu khổng lồ), Ground Slam.
- **Đấu trường:** 30×11 ô; pha 2 đầu Sigma chiếm nửa phải.
- **Pha 2 (dưới 50% HP):** sàn sụp từng mảng 3 ô theo thứ tự trái→phải, báo trước bằng vết nứt.

## Engine cần bổ sung
- Bệ chạy vòng quanh tâm
- Trọng lực biến thiên theo nhịp
- Virus bám đuổi
- Sàn sụp theo mảng trong trận boss

## Hình cần vẽ
- Lõi virus Sigma
- Bệ quay quanh lõi
- Mảng sàn sụp

## Kiểm tra tự động
Đường chính đã được kiểm tra theo khả năng nhảy (gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô, lướt-nhảy ≤ 7 ô, đi bộ phải có nền) và theo quy ước số lượng.

**Kết quả: đạt.**
