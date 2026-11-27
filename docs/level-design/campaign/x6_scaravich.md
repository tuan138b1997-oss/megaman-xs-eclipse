# Bảo tàng Trung tâm — Boss Ground Scaravich

`x6_scaravich` · chủ đề `metal` · Act II · X6 · tổng ~233×24 ô (7456×768 px)

![Sơ đồ](maps/x6_scaravich.png)

## Ý tưởng
Bảo tàng ban đêm: đèn pha an ninh quét theo đường cố định; bị phát hiện thì cửa phòng sập khóa và gọi 2 lính. Giữa màn là Đại cột Totem chặn đường. Area 2 có hai cụm phòng nối bằng cổng dịch chuyển theo cặp.

## Tham khảo
X6 Ground Scaravich / Central Museum, X8 Dark Mantis (lén lút), X4 Split Mushroom.

## Chuẩn kích thước
Khung hình 640×360 px = 20×11.25 ô. Hành lang: trần 1 ô, trong lòng 9 ô, khối trần luôn nằm trong khung; phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô; đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô. X nhảy cao ~2.6 ô, xa ~5 ô: trên đường chính gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô (lướt-nhảy ≤ 7 ô); cao/xa hơn chỉ bằng đá tường, giáp hoặc cơ chế của màn, và dùng cho bí mật.

## Cấu trúc

- **Area 1** (R1 → R2): sảnh, phòng hóa thạch
- **Mid** (MID): Đại cột Totem
- **Area 2** (R3 → R6 → R7): cụm phòng Cell 1–2
- **Boss** (BOSS): kho tàng

## Nhịp màn (độ khó)
R1 (3) → R2 (4) → MID (5) → R3 (4) → R6 (7) → R7 (2) → BOSS (6)

## Kịch bản từng phòng

### R1 – Sảnh trưng bày · đi ngang · độ khó 3
*x 0–36, y 2–14 (36×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 1 · sảnh trưng bày

Đèn pha quét đầu tiên (vệt vàng qua lại 6 ô). Bị phát hiện → cửa sập 6 s + 2 Drone báo động (không tính vào đếm).
- **Thông số:** đèn quét 2.5 s một chiều; báo động khóa cửa 6 s
- **Địa hình:** đèn pha x 6–14, y 3–12 (đèn pha quét); khối x 14–16, y 10–12; đèn pha x 24–32, y 3–12 (đèn pha quét)
- **Thực thể:** Sniper (3, 12); Drone (21, 9)
- **Đường chính dùng:** nhảy, rơi xuống

### R2 – Phòng hóa thạch · đi ngang · độ khó 4
*x 36–68, y 3–22 (32×19 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 1 · sảnh trưng bày

Hai tầng: tầng trên đi trên khung xương khủng long (khe 3 ô), tầng dưới sàn bảo tàng có đèn pha chéo. Lối chính tầng trên.
- **Thông số:** đèn pha chéo 3 s
- **Địa hình:** khối x 36–42, y 12–13; khối x 45–46, y 12–13; khối x 57–58, y 12–13; đèn pha x 36–50, y 13–21 (đèn pha chéo)
- **Thực thể:** Drone (39, 9); Reploid cứu (50, 12); Sniper (58, 21)
- **Đường chính dùng:** nhảy
- **Lối bí mật:** (36, 21) → (50, 21) → (66, 21) → (68, 21)

### MID – Đại cột Totem · đấu trường · độ khó 5
*x 68–94, y 2–14 (26×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Mid

Mini-boss: Đại cột Totem 45 HP, mỗi tầng mặt bắn đạn khác nhau; phá từ dưới lên. Checkpoint 1.
- **Thông số:** mỗi tầng bắn 1.5 s
- **Thực thể:** Mini-boss (80, 12) – Totem 45 HP (3 tầng); Checkpoint (92, 12)

### R3 – Cụm phòng Cell 1 · đi ngang · độ khó 4
*x 94–134, y 2–14 (40×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · cụm phòng Cell

Bốn cổng dịch chuyển theo cặp nối hai cụm phòng; mỗi phòng một tủ trưng bày (Heart Tank ở một tủ). Đèn pha trong mỗi phòng.
- **Thông số:** cổng hồi 1 s
- **Địa hình:** đèn pha x 112–120, y 3–12 (đèn pha)
- **Thực thể:** Drone (97, 9); Heart Tank (114, 12) – tủ trưng bày; Sniper (116, 12); Sniper (131.333, 12); Reploid cứu (132.667, 12)
- **Đường chính dùng:** cổng dịch chuyển

### R6 – Cụm phòng Cell 2 · đi ngang · độ khó 7
*x 134–183, y 2–14 (49×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · cụm phòng Cell

Cao trào: đèn pha phối hợp ba vệt + cổng dịch chuyển; bị phát hiện là khóa phòng với Brute. Hốc cao có capsule Blade Arm (X=4840 dữ liệu game); Sub-Tank qua cổng phụ. Checkpoint 2.
- **Thông số:** 3 đèn quét lệch pha 1 s
- **Địa hình:** đèn pha x 138–148, y 3–12 (đèn ×3); khối x 148–151, y 10–12; bệ / kệ x 153–157, y 7.5; đèn pha x 153–163, y 3–12
- **Thực thể:** Checkpoint (136, 12); Brute (143, 12); Capsule giáp (155, 7.5) – Blade Arm (hốc cao); Drone (158, 9); Sub-Tank (171, 12) – phòng kín; Sniper (176, 12)
- **Đường chính dùng:** cổng dịch chuyển, nhảy, rơi xuống
- **Lối bí mật:** (152, 10) → (154, 7.5)

### R7 – Kho lưu trữ · đi ngang · độ khó 2
*x 183–201, y 2–14 (18×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · cụm phòng Cell

Phòng nghỉ: hai Reploid, cửa boss.
- **Thực thể:** Reploid cứu (186, 12); Reploid cứu (192, 12); Drone (198, 9)

### BOSS – Ground Scaravich · đấu trường · độ khó 6
*x 201–231, y 2–14 (30×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Boss

Bọ hung lăn tảng đá khổng lồ; cổng dịch chuyển trong đấu trường.
- **Thực thể:** Boss (215, 12)

## Bảng kẻ địch và vật phẩm

| Loại | Phòng | x | y | Ghi chú |
|---|---|---|---|---|
| Sniper | R1 | 3 | 12 |  |
| Drone | R1 | 21 | 9 |  |
| Drone | R2 | 39 | 9 |  |
| Reploid cứu | R2 | 50 | 12 |  |
| Sniper | R2 | 58 | 21 |  |
| Mini-boss | MID | 80 | 12 | Totem 45 HP (3 tầng) |
| Checkpoint | MID | 92 | 12 |  |
| Drone | R3 | 97 | 9 |  |
| Heart Tank | R3 | 114 | 12 | tủ trưng bày |
| Sniper | R3 | 116 | 12 |  |
| Sniper | R3 | 131.333 | 12 |  |
| Reploid cứu | R3 | 132.667 | 12 |  |
| Checkpoint | R6 | 136 | 12 |  |
| Brute | R6 | 143 | 12 |  |
| Capsule giáp | R6 | 155 | 7.5 | Blade Arm (hốc cao) |
| Drone | R6 | 158 | 9 |  |
| Sub-Tank | R6 | 171 | 12 | phòng kín |
| Sniper | R6 | 176 | 12 |  |
| Reploid cứu | R7 | 186 | 12 |  |
| Reploid cứu | R7 | 192 | 12 |  |
| Drone | R7 | 198 | 9 |  |
| Boss | BOSS | 215 | 12 |  |

Tổng: 11 kẻ địch thường (Sniper 5, Drone 5, Brute 1), 4 Reploid, 2 checkpoint, Heart Tank 1, Sub-Tank 1, capsule 1.

## Capsule theo dữ liệu game
🛡️ Capsule Blade Armor — Arm Part (X=4840, Y=420 — Hốc cao cụm phòng Cell 2 Area 2 [YT 45:41]): Vượt qua đèn pha quét an ninh và Đại Cột Totem ở Mid-Gate, đi vào cụm cổng Cell 2 (P3/P4) và leo lên vách X=4650. Đèn pha quét an ninh (Searchlights) + 4 Cổng Dịch Chuyển 2 Cụm Phòng + Blade Arm Part Area 1: Hành lang bảo tàng tối có Đèn pha quét an ninh và Cụm cổng Cell 1 (P1–P2) chứa Heart Tank. Mid-Gate: Phá Đại Cột Totem. Area 2: Cụm cổng Cell 2 (P3–P4) với bẫy đá lăn, Blade Arm Part và cổng Alt Path.

## Bí mật
| Vật phẩm | Phòng | Cách lấy |
|---|---|---|
| Capsule Blade Arm | R6 | Hốc cao Cell 2. |
| Heart Tank | R3 | Tủ trưng bày qua cổng A→B. |
| Sub-Tank | R6 | Phòng kín qua cổng E→F. |

## Boss
**Ground Scaravich** · điểm yếu: Yammar Option
- **Bộ chiêu (dữ liệu game):** Ground Dash (Rolling Rock): Đẩy tảng đá khổng lồ lăn ngang đấu trường, càng lăn càng to. Burrow Drop: Đào lên trần rồi thả đá vụn xuống đầu người chơi. Boulder Toss: Hất đá bay theo đường parabol. Overdrive (Phase 2): Tạo tảng đá năng lượng khổng lồ vỡ ra nhiều mảnh.
- **Đấu trường:** kho 30×11 ô, 2 cổng dịch chuyển hai góc.
- **Pha 2 (dưới 50% HP):** tảng đá to gấp đôi và đi qua cổng dịch chuyển ra phía sau người chơi.

## Engine cần bổ sung
- Đèn pha quét theo đường cố định, phát hiện → khóa phòng
- Cổng dịch chuyển theo cặp
- Đại cột Totem nhiều tầng

## Hình cần vẽ
- Bảo tàng ban đêm, tủ trưng bày
- Khung xương khủng long (bệ)
- Đèn pha an ninh
- Cổng dịch chuyển
- Cột Totem

## Kiểm tra tự động
Đường chính đã được kiểm tra theo khả năng nhảy (gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô, lướt-nhảy ≤ 7 ô, đi bộ phải có nền) và theo quy ước số lượng.

**Kết quả: đạt.**
