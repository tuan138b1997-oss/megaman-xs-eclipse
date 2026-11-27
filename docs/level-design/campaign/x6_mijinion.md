# Trung tâm vũ khí — Boss Infinity Mijinion

`x6_mijinion` · chủ đề `metal` · Act II · X6 · tổng ~238×18 ô (7616×576 px)

![Sơ đồ](maps/x6_mijinion.png)

## Ý tưởng
Trung tâm thử vũ khí ở Tây Úc. Siêu phi thuyền Illumina lượn trên trời, vòng ngắm bám người chơi rồi bắn xuống (vòng chuyển đỏ đậm 1 s trước). Giữa màn là mini-boss lõi cáp Illumina; Area 2 là vực lớn với bệ treo cáp đung đưa.

## Tham khảo
X6 Infinity Mijinion / Weapon Center (vòng ngắm Illumina), X4 Split Mushroom (bệ treo), X8 Avalanche Yeti (vực lớn).

## Chuẩn kích thước
Khung hình 640×360 px = 20×11.25 ô. Hành lang: trần 1 ô, trong lòng 9 ô, khối trần luôn nằm trong khung; phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô; đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô. X nhảy cao ~2.6 ô, xa ~5 ô: trên đường chính gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô (lướt-nhảy ≤ 7 ô); cao/xa hơn chỉ bằng đá tường, giáp hoặc cơ chế của màn, và dùng cho bí mật.

## Cấu trúc

- **Area 1** (R1 → R2): bãi thử, khu chứa
- **Mid** (MID): lõi cáp Illumina
- **Area 2** (R3 → R4 → R5): vực cáp, bệ cáp cuối
- **Boss** (BOSS): hầm thử

## Nhịp màn (độ khó)
R1 (3) → R2 (4) → MID (5) → R3 (7) → R4 (5) → R5 (3) → BOSS (6)

## Kịch bản từng phòng

### R1 – Bãi thử · đi ngang · độ khó 3
*x 0–36, y 2–14 (36×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 1 · bãi thử

Illumina lượn trên trời; vòng ngắm đỏ bám theo, đỏ đậm 1 s rồi bắn. Đứng dưới mái che khi vòng đỏ đậm.
- **Thông số:** vòng ngắm bám 180 px/s; bắn sau 1 s đỏ đậm
- **Địa hình:** khối x 6–10, y 7.5–8.5; khối x 20–24, y 7.5–8.5
- **Thực thể:** Sniper (3, 12); Drone (15, 9); Sniper (28, 12)

### R2 – Khu chứa · đi ngang · độ khó 4
*x 36–66, y 2–14 (30×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 1 · bãi thử

Thùng vũ khí phát nổ khi bị bắn (bán kính 3 ô) – dùng để diệt Brute. Reploid sau dãy thùng.
- **Thông số:** thùng nổ bán kính 3 ô, 8 sát thương
- **Địa hình:** khối x 42–44, y 10–12; khối x 52–54, y 10–12
- **Thực thể:** Drone (39, 9); Brute (49, 12); Sniper (58, 12); Reploid cứu (60, 12)
- **Đường chính dùng:** nhảy, rơi xuống

### MID – Lõi cáp Illumina · đấu trường · độ khó 5
*x 66–96, y 2–14 (30×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Mid

Mini-boss: phá 3 lõi cáp neo Illumina (mỗi lõi 15 HP) trong khi vòng ngắm vẫn bám. Checkpoint 1.
- **Thông số:** vòng ngắm bắn mỗi 3 s
- **Thực thể:** Mini-boss (80, 12) – 3 lõi cáp × 15 HP; Checkpoint (94, 12)

### R3 – Vực cáp lớn · đi ngang · độ khó 7
*x 96–154, y 2–16 (58×14 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · vực cáp

Cao trào: 7 bệ treo cáp đung đưa trên vực; bắn đứt cáp thì bệ rơi (đừng bắn nhầm). Drone bay giữa vực. Checkpoint 2 trên bệ cứng giữa.
- **Thông số:** bệ cáp đung đưa ±2 ô, chu kỳ 3 s
- **Địa hình:** hố vực (rơi = mất mạng) x 100–122 (rộng 22 ô); bệ treo cáp x 103–106, y 11; bệ treo cáp x 109–112, y 10; bệ treo cáp x 115–118, y 11; bệ treo cáp x 119–121, y 12; hố vực (rơi = mất mạng) x 126–146 (rộng 20 ô); bệ treo cáp x 129–132, y 11; bệ treo cáp x 135–138, y 10; bệ treo cáp x 141–144, y 11
- **Thực thể:** Drone (98, 9); Checkpoint (124, 12); Drone (148, 9); Sniper (151.333, 12); Reploid cứu (152.667, 12)
- **Đường chính dùng:** bệ di động, nhảy

### R4 – Bệ cáp cuối · đi ngang · độ khó 5
*x 154–188, y 2–16 (34×14 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · vực cáp

Capsule Blade Head trên bệ cáp cuối (X=5020 dữ liệu game); Heart Tank trên giàn treo phía trên. Sniper trên giàn.
- **Địa hình:** hố vực (rơi = mất mạng) x 160–174 (rộng 14 ô); bệ treo cáp x 163–166, y 11; bệ treo cáp x 169–172, y 11; bệ / kệ x 179–183, y 7.5
- **Thực thể:** Sniper (157, 12); Capsule giáp (176, 12) – Blade Head; Heart Tank (181, 7.5) – giàn treo; Brute (181, 12)
- **Đường chính dùng:** bệ di động, nhảy
- **Lối bí mật:** (178, 12) → (180, 7.5)

### R5 – Hầm thử nghiệm · đi ngang · độ khó 3
*x 188–206, y 2–14 (18×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · vực cáp

Phòng nghỉ: Sub-Tank trong tủ vũ khí, Reploid, cửa boss.
- **Thực thể:** Reploid cứu (191, 12); Sub-Tank (196, 12) – tủ vũ khí; Reploid cứu (197, 12)

### BOSS – Infinity Mijinion · đấu trường · độ khó 6
*x 206–236, y 2–14 (30×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Boss

Boss nhân bản khi trúng đạn thường; diệt bản gốc bằng đạn nạp.
- **Thực thể:** Boss (220, 12)

## Bảng kẻ địch và vật phẩm

| Loại | Phòng | x | y | Ghi chú |
|---|---|---|---|---|
| Sniper | R1 | 3 | 12 |  |
| Drone | R1 | 15 | 9 |  |
| Sniper | R1 | 28 | 12 |  |
| Drone | R2 | 39 | 9 |  |
| Brute | R2 | 49 | 12 |  |
| Sniper | R2 | 58 | 12 |  |
| Reploid cứu | R2 | 60 | 12 |  |
| Mini-boss | MID | 80 | 12 | 3 lõi cáp × 15 HP |
| Checkpoint | MID | 94 | 12 |  |
| Drone | R3 | 98 | 9 |  |
| Checkpoint | R3 | 124 | 12 |  |
| Drone | R3 | 148 | 9 |  |
| Sniper | R3 | 151.333 | 12 |  |
| Reploid cứu | R3 | 152.667 | 12 |  |
| Sniper | R4 | 157 | 12 |  |
| Capsule giáp | R4 | 176 | 12 | Blade Head |
| Heart Tank | R4 | 181 | 7.5 | giàn treo |
| Brute | R4 | 181 | 12 |  |
| Reploid cứu | R5 | 191 | 12 |  |
| Sub-Tank | R5 | 196 | 12 | tủ vũ khí |
| Reploid cứu | R5 | 197 | 12 |  |
| Boss | BOSS | 220 | 12 |  |

Tổng: 11 kẻ địch thường (Sniper 5, Drone 4, Brute 2), 4 Reploid, 2 checkpoint, Heart Tank 1, Sub-Tank 1, capsule 1.

## Capsule theo dữ liệu game
🛡️ Capsule Blade Armor — Head Part (X=5020, Y=440 — Bệ cáp cuối Area 2 [YT 01:12:15]): Phá lõi cáp Illumina ở Mid-Gate, vượt qua chuỗi bệ dây cáp trên vực lớn Area 2 và nhảy vọt lên bệ cao X=4920. Siêu phi thuyền Illumina khóa tâm ngắm + Vực 7 Bệ dây cáp + Capsule Blade Head Area 1: Phóng qua bến cảng vũ khí dưới hỏa lực khóa mục tiêu của siêu phi thuyền Illumina và vượt chuỗi 4 bệ dây cáp trên vực lớn. Mid-Gate: Bắn lõi cáp Illumina. Area 2: Vượt vực cáp tầng cao lấy Blade Head Part.

## Bí mật
| Vật phẩm | Phòng | Cách lấy |
|---|---|---|
| Capsule Blade Head | R4 | Bệ cáp cuối. |
| Heart Tank | R4 | Giàn treo phía trên. |
| Sub-Tank | R5 | Tủ vũ khí. |

## Boss
**Infinity Mijinion** · điểm yếu: Guard Shell
- **Bộ chiêu (dữ liệu game):** Ray Arrow: Bắn loạt tia năng lượng từ trên xuống theo hàng. Infinite Clone: Mỗi khi bị đánh thường sẽ tạo thêm bản sao bọ nước. Bubble Trap: Thả bong bóng điện bay lơ lửng khắp phòng. Overdrive (Phase 2): Phóng chùm tia Ray Arrow dày đặc kèm 3 bản sao cùng lúc.
- **Đấu trường:** hầm 30×11 ô.
- **Pha 2 (dưới 50% HP):** bản sao không biến mất sau 5 s mà tồn tại tới khi trúng; vòng ngắm Illumina bật lại trong đấu trường.

## Engine cần bổ sung
- Vòng ngắm bám người chơi + bắn trễ
- Mái che chặn đạn trên cao
- Thùng nổ
- Bệ treo cáp đung đưa, bắn đứt cáp

## Hình cần vẽ
- Bãi thử vũ khí sa mạc
- Vòng ngắm Illumina
- Thùng vũ khí
- Bệ treo cáp + cáp

## Kiểm tra tự động
Đường chính đã được kiểm tra theo khả năng nhảy (gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô, lướt-nhảy ≤ 7 ô, đi bộ phải có nền) và theo quy ước số lượng.

**Kết quả: đạt.**
