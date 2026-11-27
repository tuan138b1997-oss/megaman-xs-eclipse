# Rừng đột biến — Boss Spike Rosered

`x5_rosered` · chủ đề `nature` · Act I · X5 · tổng ~280×56 ô (8960×1792 px)

![Sơ đồ](maps/x5_rosered.png)

## Ý tưởng
Rừng nấm khổng lồ bị virus Sigma làm đột biến. Nấm bật đưa người chơi lên tầng tán; bụi gai độc mọc lại sau khi bị bắn. Area 1 có tầng nấm hai lối và dây leo đu qua vực; Area 2 là đầm lầy làm chậm và thân cây cổ thụ cao trào.

## Tham khảo
X5 Spike Rosered (rừng), X3 Toxic Seahorse (đầm), X4 Web Spider (rừng hai tầng).

## Chuẩn kích thước
Khung hình 640×360 px = 20×11.25 ô. Hành lang: trần 1 ô, trong lòng 9 ô, khối trần luôn nằm trong khung; phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô; đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô. X nhảy cao ~2.6 ô, xa ~5 ô: trên đường chính gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô (lướt-nhảy ≤ 7 ô); cao/xa hơn chỉ bằng đá tường, giáp hoặc cơ chế của màn, và dùng cho bí mật.

## Cấu trúc

- **Area 1** (R1 → R2 → R3): bìa rừng, tầng nấm, dây leo
- **Mid** (MID): lõi dây leo
- **Area 2** (R5 → R6 → R7): đầm lầy, thân cây cổ thụ
- **Boss** (BOSS): vườn gai

## Nhịp màn (độ khó)
R1 (2) → R2 (3) → R3 (4) → MID (5) → R5 (5) → R6 (7) → R7 (2) → BOSS (6)

## Kịch bản từng phòng

### R1 – Bìa rừng · đi ngang · độ khó 2
*x 0–43, y 36–48 (43×12 ô) · vào ở sàn y 46, ra ở sàn y 44* · Area 1 · bìa rừng và tầng nấm

Nấm bật đầu tiên (bật lên 900 px/s ≈ 6 ô) dạy nảy lên kệ cao. Bụi gai độc 2 ô chặn đường, bắn tan nhưng mọc lại sau 4 s.
- **Thông số:** nấm bật 900 px/s; bụi gai mọc lại 4 s
- **Địa hình:** nấm bật x 8–10, y 46; gai sàn x 22–24; hố gai x 28–30 (rộng 2 ô)
- **Thực thể:** Sniper (4, 46); Drone (21, 39); Sniper (35, 44)
- **Đường chính dùng:** nhảy, nấm bật, rơi xuống

### R2 – Tầng nấm · đi ngang · độ khó 3
*x 43–88, y 35–54 (45×19 ô) · vào ở sàn y 44, ra ở sàn y 44* · Area 1 · bìa rừng và tầng nấm

Hai tầng song song: tầng dưới nhiều địch và gai dây leo, tầng trên ít địch nhưng nhiều khe 3–4 ô. Lối chính là tầng trên; nấm bật ở đầu phòng nối hai tầng.
- **Thông số:** khe tầng trên 3–4 ô
- **Địa hình:** khối x 54–55, y 44–45; khối x 55–61, y 44–45; khối x 65–66, y 44–45; khối x 77–78, y 44–45; gai sàn x 53–57
- **Thực thể:** Drone (47, 41); Reploid cứu (70, 44); Brute (48, 53); Drone (57, 50); Sniper (66, 53)
- **Đường chính dùng:** nhảy
- **Lối bí mật:** (43, 53) → (53, 53) → (61, 53) → (71, 53) → (81, 53) → (88, 53)

### R3 – Dây leo đu · đi ngang · độ khó 4
*x 88–138, y 34–48 (50×14 ô) · vào ở sàn y 44, ra ở sàn y 44* · Area 1 · bìa rừng và tầng nấm

Dây leo treo trên vực: giữ Space để bám, thả để bay theo đà. Ba dây cách nhau 6–7 ô. Drone tuần dưới dây.
- **Thông số:** dây đu biên độ ±60°, chu kỳ 2.4 s
- **Địa hình:** hố vực (rơi = mất mạng) x 94–120 (rộng 26 ô)
- **Thực thể:** Drone (106, 40); Sniper (127.333, 44); Reploid cứu (130.667, 44)
- **Đường chính dùng:** dây leo đu

### MID – Lõi dây leo · đấu trường · độ khó 5
*x 138–168, y 34–46 (30×12 ô) · vào ở sàn y 44, ra ở sàn y 44* · Mid

Mini-boss: lõi dây leo với 3 bông hoa phun gai; phải bắn hoa theo thứ tự đỏ → vàng → tím (sai thứ tự hoa mọc lại). Checkpoint 1 sau trận.
- **Thông số:** hoa phun gai mỗi 1.6 s
- **Thực thể:** Mini-boss (152, 44) – 3 hoa, mỗi hoa 15 HP; Checkpoint (166, 44)

### R5 – Đầm lấy · đi ngang · độ khó 5
*x 168–210, y 34–47 (42×13 ô) · vào ở sàn y 44, ra ở sàn y 44* · Area 2 · đầm lầy và cây cổ thụ

Bùn làm chậm 40% và không lướt được. Bệ gỗ nổi chìm dần sau 1.5 s đứng. Heart Tank trên gò đất cao giữa đầm (nhảy từ bệ gỗ).
- **Thông số:** bùn: tốc độ ×0.6; bệ gỗ chìm sau 1.5 s, nổi lại sau 3 s
- **Địa hình:** vùng chậm x 172–180, y 41–44 (bùn ×0.6); hố bùn (chậm) x 180–194 (rộng 14 ô); khúc gỗ trôi x 183–186, y 43; khúc gỗ trôi x 189–192, y 43; khối x 197–200, y 41.5–44; vùng chậm x 198–206, y 41–44
- **Thực thể:** Sniper (170, 44); Brute (176, 44); Heart Tank (198.5, 41.5) – gò đất; Sniper (202, 44); Checkpoint (208, 44)
- **Đường chính dùng:** bệ di động, nhảy
- **Lối bí mật:** (196, 44) → (198, 40)

### R6 – Thân cây cổ thụ · leo dọc · độ khó 7
*x 210–226, y 2–46 (16×44 ô) · vào ở sàn y 44, ra ở sàn y 12* · Area 2 · đầm lầy và cây cổ thụ

Cao trào. Leo trong lòng thân cây: kệ nấm so le, gai dây leo mọc trên vách (đá tường chỉ ở vùng vỏ trơn). Tán cây trên cùng bên trái có capsule Gaea Foot; Sub-Tank trong hốc giữa.
- **Thông số:** gai vách mọc lại 4 s sau khi bị bắn
- **Địa hình:** khối x 221–224, y 12–13; gai sàn x 212–213; gai sàn x 223–224; nấm bật x 214–217, y 41.5; nấm bật x 217–220, y 39; nấm bật x 220–223, y 36.5; nấm bật x 217–220, y 34; nấm bật x 214–217, y 31.5; nấm bật x 217–220, y 29; nấm bật x 220–223, y 26.5; nấm bật x 217–220, y 24; nấm bật x 214–217, y 21.5; nấm bật x 217–220, y 19; nấm bật x 220–223, y 16.5; nấm bật x 217–220, y 14; bệ / kệ x 213–217, y 8; bệ / kệ x 212–214, y 24
- **Thực thể:** Drone (221.5, 33.5); Sniper (221.5, 26.5); Capsule giáp (215, 8) – Gaea Foot (tán cây); Sub-Tank (213, 24) – hốc giữa
- **Đường chính dùng:** nhảy
- **Lối bí mật:** (220, 12) → (215, 8); (215.5, 26) → (213, 24)

### R7 – Vườn hoa · đi ngang · độ khó 2
*x 226–248, y 2–14 (22×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Area 2 · đầm lầy và cây cổ thụ

Phòng nghỉ: năng lượng nhỏ, hai Reploid, cửa boss.
- **Thực thể:** Reploid cứu (230, 12); Reploid cứu (237, 12)

### BOSS – Spike Rosered · đấu trường · độ khó 6
*x 248–278, y 2–14 (30×12 ô) · vào ở sàn y 12, ra ở sàn y 12* · Boss

Sàn có bụi gai mọc lại sau 4 s; boss treo trên dây leo trần.
- **Thực thể:** Boss (262, 12)

## Bảng kẻ địch và vật phẩm

| Loại | Phòng | x | y | Ghi chú |
|---|---|---|---|---|
| Sniper | R1 | 4 | 46 |  |
| Drone | R1 | 21 | 39 |  |
| Sniper | R1 | 35 | 44 |  |
| Drone | R2 | 47 | 41 |  |
| Reploid cứu | R2 | 70 | 44 |  |
| Brute | R2 | 48 | 53 |  |
| Drone | R2 | 57 | 50 |  |
| Sniper | R2 | 66 | 53 |  |
| Drone | R3 | 106 | 40 |  |
| Sniper | R3 | 127.333 | 44 |  |
| Reploid cứu | R3 | 130.667 | 44 |  |
| Mini-boss | MID | 152 | 44 | 3 hoa, mỗi hoa 15 HP |
| Checkpoint | MID | 166 | 44 |  |
| Sniper | R5 | 170 | 44 |  |
| Brute | R5 | 176 | 44 |  |
| Heart Tank | R5 | 198.5 | 41.5 | gò đất |
| Sniper | R5 | 202 | 44 |  |
| Checkpoint | R5 | 208 | 44 |  |
| Drone | R6 | 221.5 | 33.5 |  |
| Sniper | R6 | 221.5 | 26.5 |  |
| Capsule giáp | R6 | 215 | 8 | Gaea Foot (tán cây) |
| Sub-Tank | R6 | 213 | 24 | hốc giữa |
| Reploid cứu | R7 | 230 | 12 |  |
| Reploid cứu | R7 | 237 | 12 |  |
| Boss | BOSS | 262 | 12 |  |

Tổng: 14 kẻ địch thường (Sniper 7, Drone 5, Brute 2), 4 Reploid, 2 checkpoint, Heart Tank 1, Sub-Tank 1, capsule 1.

## Capsule theo dữ liệu game
🛡️ Capsule Gaea Armor — Foot Part (X=5040, Y=440 — Tán cây cổ thụ Area 2): Dùng Falcon Armor bay hoặc nấm đàn hồi + Air-Dash lên thân cây trụ X=4850, nhảy sang bệ lá di động. Rừng nấm đàn hồi 2 tầng -> Sub-Boss Dây leo -> Trục leo thân cây lấy Gaea Foot Area 1: Dùng nấm đàn hồi sinh học bật nhảy lên tầng tán cây cao để tránh bụi gai độc dưới đất. Mid-Gate: Hạ Sub-Boss Dây leo khổng lồ. Area 2: Leo dọc thân cây cổ thụ cao 600px lấy Gaea Foot Part và Heart Tank ẩn.

## Bí mật
| Vật phẩm | Phòng | Cách lấy |
|---|---|---|
| Capsule Gaea Foot | R6 | Tán cây trên cùng bên trái (Falcon bay hoặc nấm + lướt trên không). |
| Heart Tank | R5 | Gò đất giữa đầm, nhảy từ bệ gỗ. |
| Sub-Tank | R6 | Hốc giữa thân cây. |

## Boss
**Spike Rosered** · điểm yếu: Ground Fire / Quake Blazer
- **Bộ chiêu (dữ liệu game):** Spike Ball: Tung quả cầu gai nảy liên tục trên sàn và tường. Vine Whip: Quất roi gai tầm xa đánh chéo lên không. Clone Illusion: Phân thân thành 2 bản sao tấn công kẹp. Overdrive (Phase 2): Triệu hồi gai mọc từ mặt đất và mưa cầu gai.
- **Đấu trường:** vườn 30×11 ô, dây leo trên trần cho boss treo.
- **Pha 2 (dưới 50% HP):** bụi gai mọc kín 1/3 sân mỗi 8 s (luân phiên trái/giữa/phải), báo trước bằng nụ hoa.

## Engine cần bổ sung
- Bụi gai độc mọc lại
- Nấm bật
- Dây leo đu (bám/thả)
- Bùn làm chậm, cấm lướt
- Bệ gỗ chìm dần

## Hình cần vẽ
- Nấm khổng lồ (bệ + nấm bật)
- Bụi gai độc
- Dây leo đu
- Đầm bùn, bệ gỗ nổi
- Lòng thân cây cổ thụ

## Kiểm tra tự động
Đường chính đã được kiểm tra theo khả năng nhảy (gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô, lướt-nhảy ≤ 7 ô, đi bộ phải có nền) và theo quy ước số lượng.

**Kết quả: đạt.**
