# Màn: BẮC CỰC (North Pole Area — Boss Blizzard Wolfang)

Bản thiết kế để duyệt trước khi dựng. Sơ đồ: `maps/x6_wolfang.png`.
Màn này thay cho `x6_wolfang` hiện tại. Boss, capsule Blade Body, Ride Chaser trên dốc tuyết lở, sàn băng quán tính, vách băng cao và đoạn khối băng sát trần gai vẫn giữ; thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.

![Sơ đồ](maps/x6_wolfang.png)

---

## 0. Công cụ và quy ước

Dùng chung với màn mẫu (`../lo-nham-thach-kich-ban.md`, mục 0): LDtk dựng bản đồ, Pixelorama vẽ tile, Krita vẽ nền parallax. 1 ô = 32px, khung hình 30×17 ô, các lớp `Collision` / `Tiles` / `Decor` / `Foreground` / `Entities`.

---

## 1. Ý tưởng tổng

Trạm nghiên cứu Bắc Cực giữa bão tuyết. Nửa đầu là **lao dốc bằng Ride Chaser** trước tuyết lở, nửa sau là **đi bộ trên băng trơn** với vách không bám được và trần gai thấp.

- **Area 1 – Dốc và hồ (ngoài trời):** trắng xanh, trời xám, tuyết bay. Ride Chaser đổ dốc, tuyết lở đuổi, hồ băng mỏng.
- **Area 2 – Hang và vách băng:** xanh băng, ánh lạnh. Sàn trơn, cột băng rơi, vách băng có bão, sông băng dưới trần gai.
- **Điểm nhấn trải nghiệm:** lên xe → lao dốc trước tuyết lở → giữ tốc độ trên băng mỏng → mini-boss gấu tuyết → trượt trong hang có cột băng rơi → leo vách băng trong bão → nhảy khối băng dưới trần gai → boss trong bão tuyết
- **Đường cong độ khó:** 2 → 3 → 4 → (mini-boss) → 5 → 6 → 7 → 6 → 2 → boss (thang 10).
- **Thời lượng mục tiêu:** khoảng 6–7 phút lần đầu, khoảng 3 phút khi đã quen.

Các mẫu thiết kế tham khảo (không chép bản đồ gốc):

- **X6, màn Blizzard Wolfang:** Ride Chaser trên dốc tuyết lở, vách băng cao giấu Blade Body, khối băng trôi sát trần gai.
- **X8 16-bit demake (màn Avalanche Yeti):** đoạn tự cuộn được làm lại thành đoạn chơi thường, lấy cảm hứng từ X2 Overdrive Ostrich.
- **X (SNES), màn Chill Penguin / X3, màn Blizzard Buffalo:** sàn băng quán tính, cột băng rơi.
- **X Corrupted:** giáp mở đường tắt rõ ràng (Shadow miễn trần gai).

---

## 2. Kịch bản từng phòng

Tọa độ tính theo ô, gốc (0,0) ở góc trên trái thế giới, y tăng xuống dưới.

### R1 – Trạm cực (x 0–40, y 30–46) · độ khó 2
- **Mục đích:** lên **Ride Chaser** ở trạm nghiên cứu Bắc Cực.
- **Địa hình:** sân trạm 40 ô, mặt tuyết ở y 42.
- **Địch:** 1 Sniper chắn trước xe.
- **Ghi chú:** khác đường đua Nhà máy điện (đi ngang, chạy tự do), ở đây là **đổ dốc xuống**, có tuyết lở đuổi phía sau nên không được dừng lâu.

### R2 – Dốc tuyết lở (x 40–140, y 30–60) · độ khó 3
- **Mục đích:** lao xuống dốc dài 100 ô trên Ride Chaser, **tuyết lở đuổi phía sau**.
- **Địa hình:**
  - Dốc đi xuống từ y 42 tới y 56, có 2 vực (rộng 8 ô) ở cuối hai đoạn dốc, nhảy qua bằng đà.
- **Cơ chế:**
  - **Tuyết lở** là một bức tường tuyết đuổi theo với tốc độ 240px/giây. Chậm hơn nó là bị vùi (mất mạng). Xe chạy tối đa 320px/giây, nên vẫn có khoảng dư để phanh một chút.
  - **Tảng băng lăn** từ trên dốc xuống chậm hơn xe: nhảy qua, hoặc bắn 2 phát cho vỡ.
- **Địch:** 2 Drone bay ngang tầm nhảy qua vực. Xe húc vỡ được.
- **Quả năng lượng:** 2 quả nằm trên đường bay qua vực, chỉ để thưởng (hồi năng lượng vũ khí).

### R3 – Hồ băng mỏng (x 140–200, y 44–60) · độ khó 4
- **Mục đích:** giữ tốc độ trên **mặt băng mỏng**.
- **Địa hình:** hồ băng rộng 44 ô, mặt băng ở y 56. Dưới là nước lạnh (rơi xuống là mất mạng).
- **Cơ chế:**
  - Đi nhanh (trên 200px/giây) thì băng chỉ nứt sau lưng xe.
  - Đi chậm thì băng vỡ 0.4 giây sau khi xe chạm.
  - Tuyết lở vẫn đuổi tới đầu hồ rồi dừng.
- **Địch:** 1 Drone giữa hồ, 1 Sniper ở bờ bên kia.
- **Vật phẩm:** Reploid #1 ở bờ bên kia, cạnh chỗ xuống xe (xe không qua được cửa phòng sau).

### Mini-boss – Gấu tuyết máy (x 200–230, y 42–58) · độ khó 5
- **Đấu trường 26 ô**, sàn băng trơn, hai vách đá tường được.
- **Gấu tuyết máy** to bằng 3 ô, chạy và trượt trên băng.
- **Đòn đánh:**
  - Lao trượt ngang sân rồi đâm vào vách, làm rơi 3 cột băng nhọn từ trần.
  - Ném tảng tuyết lăn trên sàn.
  - Thổi hơi lạnh: trúng thì đóng băng 1 giây (bấm liên tục để thoát).
- **Điểm yếu:** lưng, sau mỗi lần đâm vách nó choáng 1.5 giây.
- **Phần thưởng:** mở cửa hang băng. Hạ không mất máu thì được thưởng Souls.

### R4 – Hang băng trơn (x 230–290, y 44–58) · độ khó 5
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** đi bộ trên sàn băng có quán tính, trong hang có cột băng rơi.
- **Địa hình:** hang 60 ô, sàn băng ở y 56, trần ở y 46.
- **Bẫy – cột băng:** 3 cột băng treo trần, rung khi người chơi lại gần trong 3 ô rồi rơi sau 0.5 giây. Trên sàn trơn khó dừng đúng chỗ.
- **Địch:** 1 Brute trượt trên băng (không dừng kịp nên đâm cả vào cột băng rơi), 1 Sniper.
- **Vật phẩm:** Reploid #2 giữa hang.
- **Lối phụ (Sub-Tank):** kệ băng trên cao (x ≈ 277, y ≈ 48), ngay dưới cột băng thứ ba. Phải làm cột băng rơi trước rồi mới lên.

### R5 – Vách băng cao (x 290–314, y 6–58) · độ khó 6
- **Mục đích:** đoạn dọc. Vách băng một phần **không bám được**, bão tuyết thổi ngang từng đợt.
- **Địa hình:**
  - Khe vách băng rộng 20 ô, cao 48 ô (từ y 56 lên y 9). 5 kệ băng zigzag.
  - Mảng băng láng trên vách (trái ở đoạn giữa, phải ở đoạn dưới): không đá tường được ở đó.
- **Cơ chế – bão tuyết:** gió thổi sang phải 100px/giây, 2 giây mỗi 6 giây, ở nửa trên. Đang đá tường vách trái mà gặp gió thì bị thổi bật ra.
- **Địch:** 1 Drone dạng chim cánh cụt bay.
- **Lối phụ (Capsule Blade Body):**
  - Kệ băng sát trần bên trái (x ≈ 292, y ≈ 10), cao hơn lối ra.
  - Bám vách trái ngay phía trên mảng băng láng, đá tường 2 lần lên kệ. Phải lên lúc không có gió.
- **Lối phụ (Heart Tank):** một gờ nhỏ ở vách phải (x ≈ 310, y ≈ 39), ngay trên mảng băng láng: nhảy chéo từ kệ thứ hai sang, không đá tường được.

### R6 – Sông băng trôi (x 314–384, y 4–18) · độ khó 7
- **Mục đích:** cao trào của màn. Nhảy trên **khối băng trôi** dưới trần gai thấp.
- **Địa hình:**
  - Sông băng dài 58 ô dưới một hang có **trần phủ gai**, chỉ cách mặt khối băng 3.5 ô.
  - Rơi xuống nước là mất mạng.
- **Cơ chế:**
  - Khối băng trôi sang phải 50px/giây, mỗi khối rộng 6 ô.
  - Khối băng **trơn và nghiêng nhẹ** khi đứng ở mép, nên người chơi trượt ra mép.
  - Nhảy hết lực là chạm trần gai. Phải nhảy ngắn giữa các khối, nhất là khi khoảng cách giữa hai khối giãn ra.
- **Địch:** 2 Drone chim cánh cụt bay sát trần: bắn ngang, không cần nhảy.
- **Giáp hỗ trợ:** Shadow miễn gai (kể cả trần gai), nên đoạn này dễ hẳn.

### R7 – Cổng sông băng (x 384–434, y 4–18) · độ khó 6
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** kết hợp: sàn băng trơn và bậc khối băng.
- **Địa hình:** hành lang 50 ô, sàn băng, 2 khối băng cao 3 và 4 ô.
- **Địch:** 1 Drone, 1 Sniper đứng sau khối băng thứ hai.
- **Vật phẩm:** Reploid #3 giữa hai khối băng.

### R8 – Lều trạm (x 434–464, y 4–18) · độ khó 2
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss.

### BOSS – Blizzard Wolfang (x 464–496, y 0–16)
- **Đấu trường 28 ô**, sàn băng trơn, hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (Ice Burst, cào, nhảy vách).
- **Pha 2** (dưới 50% HP):
  - **Bão tuyết** thổi ngang, đổi chiều mỗi 6 giây.
  - Tầm nhìn giảm (tuyết bay), Wolfang lẩn vào bão rồi lao ra.
- Điểm yếu giữ nguyên theo dữ liệu game.

---

## 3. Bảng vật phẩm và kẻ địch

| Loại | Số lượng | Vị trí |
|---|---|---|
| Sniper | 4 | R1, R3, R4, R7 |
| Drone | 7 | R2 ×2, R3, R5, R6 ×2, R7 |
| Brute | 1 | R4 |
| Mini-boss | 1 | MID |
| Reploid cứu | 4 | R3, R4, R7, R8 |
| Heart Tank | 1 | R5 |
| Sub-Tank | 1 | R4 |
| Capsule Blade Body | 1 | R5 |
| Ride Armor / Chaser | 1 | R1 |
| Checkpoint | 2 | R4, R7 |

Tổng 12 kẻ địch thường (bản cũ: 20 con xếp đều), đặt có chủ đích theo mục đích từng phòng.

---

## 4. Những gì engine cần bổ sung

1. Ride Chaser đổ dốc; tường tuyết lở đuổi theo tốc độ cố định.
2. Tảng băng lăn (vật thể lăn theo dốc, phá được).
3. Mặt băng mỏng: vỡ theo tốc độ đi qua.
4. Sàn băng quán tính; vách băng láng không đá tường được.
5. Cột băng rơi khi người chơi lại gần.
6. Bão tuyết: vùng gió theo nhịp, giảm tầm nhìn.
7. Khối băng trôi trơn, nghiêng khi đứng ở mép.
8. Mini-boss Gấu tuyết máy.

## 5. Danh sách hình cần vẽ

- **Tileset "Dốc tuyết" (Area 1):** 47 ô viền tuyết, dốc tuyết, mặt băng mỏng (3 khung nứt).
- **Tileset "Hang băng" (Area 2):** 47 ô viền băng, mảng băng láng, trần gai băng.
- **Vật thể:** tuyết lở (4 khung), tảng băng lăn, cột băng (3 khung), khối băng trôi, bông tuyết bão (lớp phủ).
- **Nền:** Area 1: núi tuyết và cực quang (2 lớp parallax). Area 2: lòng sông băng xanh (2 lớp).

**Hướng phối hợp:** như màn mẫu — dựng bằng khối màu tạm theo sơ đồ để chơi thử, chốt cảm giác rồi mới thay tile thật.
