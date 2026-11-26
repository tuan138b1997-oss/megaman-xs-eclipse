# Màn: NHÀ MÁY ĐIỆN (Energy Plant — Boss Volt Kraken)

Bản thiết kế để duyệt trước khi dựng. Sơ đồ: `maps/x5_kraken.png`.
Màn này thay cho `x5_kraken` hiện tại. Boss, capsule Falcon Arm, đoạn Ride Chaser và trạm ngắt điện (mid-gate) vẫn giữ; thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.

![Sơ đồ](maps/x5_kraken.png)

---

## 0. Công cụ và quy ước

Dùng chung với màn mẫu (`../lo-nham-thach-kich-ban.md`, mục 0): LDtk dựng bản đồ, Pixelorama vẽ tile, Krita vẽ nền parallax. 1 ô = 32px, khung hình 30×17 ô, các lớp `Collision` / `Tiles` / `Decor` / `Foreground` / `Entities`.

---

## 1. Ý tưởng tổng

Nhà máy điện cao thế giữa đồng hoang. Nửa đầu là **đua Ride Chaser** qua dốc nhảy và cầu sập, nửa sau là **leo tháp tụ điện** bằng bệ phản lực. Cả màn chung một nhịp: điện bật/tắt theo chu kỳ.

- **Area 1 – Đường đua cao thế (ngoài trời):** cột điện, trời giông, chớp xa. Tốc độ, dốc nhảy, nhặt quả năng lượng.
- **Area 2 – Nhà máy (trong nhà):** thép xám, đèn vàng, tia lửa. Sàn điện theo nhịp, tháp leo dọc, tường điện có công tắc.
- **Điểm nhấn trải nghiệm:** lên xe → đua qua dốc và cột điện → cầu sập phía sau bánh xe → mini-boss biến áp → né sàn điện → leo tháp bằng bệ phản lực → bắn công tắc tường điện → boss nước nhiễm điện
- **Đường cong độ khó:** 2 → 3 → 4 → (mini-boss) → 5 → 7 → 6 → 2 → boss (thang 10).
- **Thời lượng mục tiêu:** khoảng 6–7 phút lần đầu, khoảng 3 phút khi đã quen.

Các mẫu thiết kế tham khảo (không chép bản đồ gốc):

- **X5, màn Volt Kraken:** mở đầu bằng đoạn Ride Chaser có 8 quả năng lượng mở cửa ở cuối.
- **X8 16-bit demake:** làm lại các đoạn tự cuộn thành màn chơi thường; ở đây Ride Chaser chạy tự do, lùi lại được.
- **X4, màn Jet Stingray / X2, màn Overdrive Ostrich:** đường đua có dốc nhảy và vực.
- **X6, màn Commander Yammark / X8, màn Gigabolt Man-O-War:** bệ và sàn bật/tắt theo nhịp, đọc nhịp từ xa.
- **X Corrupted:** lối phụ đặt trên đường bay của cơ chế chính (Heart Tank chỉ với tới từ bệ phản lực).

---

## 2. Kịch bản từng phòng

Tọa độ tính theo ô, gốc (0,0) ở góc trên trái thế giới, y tăng xuống dưới.

### R1 – Ga Ride Chaser (x 0–30, y 40–54) · độ khó 2
- **Mục đích:** lên **Ride Chaser** (mô-tô bay). Ở phòng này xe đứng yên cho người chơi làm quen nút.
- **Địa hình:** sàn phẳng 30 ô, mặt đất ở y 50. Xe đậu ở x ≈ 20.
- **Địch:** 1 Sniper đứng chắn trước xe (hạ bằng chân trước khi lên xe).
- **Ghi chú điều khiển:**
  - Ride Chaser **không tự chạy**: người chơi tự tăng tốc, phanh và lùi.
  - Đây là khác biệt chính so với X5 gốc, học theo cách bản X8 16-bit demake làm lại các đoạn tự cuộn.
  - Tốc độ tối đa 320px/giây, nhảy dốc thì bay xa theo tốc độ.

### R2 – Đường đua cao thế (x 30–130, y 38–54) · độ khó 3
- **Mục đích:** cảm giác tốc độ. Dạy **dốc nhảy**, **tấm boost** và **cột điện theo nhịp**.
- **Địa hình:**
  - Đường đua 100 ô, mặt đường ở y 50.
  - 2 dốc nhảy dẫn tới 2 vực (rộng 8 và 10 ô). Phải đủ tốc độ mới bay qua.
  - Tấm **boost** trước mỗi dốc: chạy qua thì tốc độ vọt lên tối đa trong 1.5 giây.
- **Bẫy – cột điện:** 2 cột phóng điện chắn ngang đường, bật 1 giây, tắt 2 giây. Canh tốc độ để qua lúc tắt, hoặc phanh chờ.
- **Quả năng lượng:** 4 trong tổng số 8 quả nằm ở phòng này. 2 quả ở đỉnh quỹ đạo bay của dốc: chỉ lấy được khi bay qua đúng tốc độ tối đa.
- **Địch:**
  - 1 Drone bay thấp sau tấm boost thứ hai: xe húc vỡ được.
  - 1 Sniper cuối đường.

### R3 – Cầu sập (x 130–210, y 38–56) · độ khó 4
- **Mục đích:** đoạn tốc độ thử thách. Không được dừng.
- **Địa hình:**
  - 2 **cầu sập**: mỗi mảnh cầu rơi 0.6 giây sau khi xe chạy qua. Dừng giữa cầu là rơi theo.
  - 1 dốc nhảy giữa hai cầu, vực rộng 10 ô.
- **Địch:** 2 Drone bay ngang tầm nhảy. Bắn trước khi lên dốc hoặc lượn qua dưới.
- **Vật phẩm:** Reploid #1 trên bệ cuối, ngay trước cửa.
- **Lối phụ (Sub-Tank):**
  - **Cửa năng lượng** cuối phòng chỉ mở khi đã nhặt đủ **8 quả năng lượng** ở R2 và R3. Sau cửa là Sub-Tank.
  - Lỡ quả nào thì phải quay xe chạy lại (xe lùi được). Đó là lý do đường đua không tự cuộn.

### Mini-boss – Trạm ngắt điện (x 210–240, y 36–54) · độ khó 5
- **Đấu trường 26 ô**, kín. Ride Chaser dừng ở cửa: người chơi đánh bằng chân.
- **Lõi biến áp** treo giữa phòng, có 4 cánh tay phóng điện quay chậm quanh lõi (90° mỗi 2 giây).
- **Đòn đánh:**
  - Cánh tay quét theo vòng tròn: luồn qua khe giữa hai cánh.
  - Sàn nhiễm điện 1.5 giây sau mỗi vòng quay (có tia lửa báo trước): đá tường lên vách mà chờ.
- **Điểm yếu:** lõi mở nắp 2 giây sau khi sàn hết điện.
- **Phần thưởng:** ngắt điện khu sau để mở Area 2. Hạ không mất máu thì được thưởng Souls.

### R4 – Sàn điện (x 240–300, y 40–54) · độ khó 5
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** né theo nhịp trên sàn. Đây cũng là lần đổi không gian: từ đường đua ngoài trời vào trong nhà máy.
- **Địa hình:**
  - Hành lang 60 ô, trần thấp (cao 8 ô).
  - **4 tấm sàn điện** dài 6 ô, bật 1.5 giây, tắt 1.5 giây, lệch pha nhau thành một làn sóng.
  - Giữa các tấm có ô sàn an toàn rộng 6 ô.
- **Địch:**
  - 1 Brute đứng trên ô an toàn giữa phòng: phải hạ nó mà không bước lên tấm điện.
  - 1 Sniper cuối phòng, 1 Drone bay trên tấm điện thứ tư.
- **Vật phẩm:** Reploid #2 giữa hai tấm điện đầu.

### R5 – Tháp tụ điện (x 300–330, y 4–54) · độ khó 7
- **Mục đích:** cao trào của màn. Leo dọc bằng **bệ phản lực** và đá tường giữa các tia hồ quang.
- **Địa hình:**
  - Tháp rộng 20 ô, cao 46 ô (từ y 50 lên y 5).
  - Vách trái leo được suốt chiều cao. Vách phải có một hốc ở giữa.
- **Cơ chế – bệ phản lực:**
  - 4 bệ, đứng lên thì bệ bốc lên với tốc độ 80px/giây trong 3 giây, rồi tắt máy và rơi về chỗ cũ.
  - Phải nhảy sang bệ tiếp theo trước khi bệ dưới chân tắt máy.
- **Bẫy – hồ quang:** 2 tia điện nối hai vách, bật 1 giây, tắt 2 giây. Bệ phản lực bay xuyên qua tia, nên phải canh lúc đứng lên bệ.
- **Địch:** 2 Drone, chỉ để gây áp lực.
- **Lối phụ (Heart Tank):** **hốc ở vách phải** (x ≈ 324–330, y ≈ 28–32). Nhảy từ bệ phản lực thứ ba khi nó lên ngang hốc, lướt trên không vào.
- **Lối phụ (Capsule Falcon Arm):**
  - Kệ nhỏ sát trần bên trái (x ≈ 302, y ≈ 9), cao hơn lối ra.
  - Nhảy từ bệ phản lực thứ tư ở điểm cao nhất, đá vách trái 2 lần mới tới.
  - Giáp Gaea bám tường nên dễ; giáp thường phải canh rất chuẩn.

### R6 – Hành lang cáp (x 330–390, y 4–18) · độ khó 6
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** kết hợp: bắn công tắc trên cao, né địch, đi qua tường điện.
- **Địa hình:**
  - Hành lang 60 ô, trần ở y 6, sàn ở y 14.
  - **2 tường điện** chắn ngang hết chiều cao. Mỗi tường có một **công tắc** trên kệ cao phía trước nó.
- **Cơ chế:** bắn công tắc thì tường điện tắt trong **4 giây** rồi bật lại. Phải lên kệ, bắn, nhảy xuống và chạy qua kịp.
- **Địch:**
  - 1 Sniper sau tường thứ hai, bắn xuyên qua tường điện.
  - 1 Drone giữa hai tường.
- **Vật phẩm:** Reploid #3 giữa hai tường điện.

### R7 – Cổng (x 390–420, y 4–18) · độ khó 2
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss.

### BOSS – Volt Kraken (x 420–452, y 0–18)
- **Đấu trường 28 ô**, sàn ngập nước nông 3 ô. Hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (đạn điện, lao xúc tu, thả mực).
- **Pha 2** (dưới 50% HP):
  - Kraken phóng điện xuống nước mỗi 6 giây: **toàn bộ mặt nước nhiễm điện 1.5 giây** (nước chớp vàng 1 giây trước).
  - Lúc đó phải ở trên không: nhảy, đá tường, hoặc đứng trên vách.
- Điểm yếu giữ nguyên theo dữ liệu game.

---

## 3. Bảng vật phẩm và kẻ địch

| Loại | Số lượng | Vị trí |
|---|---|---|
| Sniper | 4 | R1, R2, R4, R6 |
| Drone | 7 | R2, R3 ×2, R4, R5 ×2, R6 |
| Brute | 1 | R4 |
| Mini-boss | 1 | MID |
| Reploid cứu | 4 | R3, R4, R6, R7 |
| Heart Tank | 1 | R5 |
| Sub-Tank | 1 | R3 |
| Capsule Falcon Arm | 1 | R5 |
| Ride Armor / Chaser | 1 | R1 |
| Công tắc | 2 | R6 ×2 |
| Checkpoint | 2 | R4, R6 |

Tổng 12 kẻ địch thường (bản cũ: 20 con xếp đều), đặt có chủ đích theo mục đích từng phòng.

---

## 4. Những gì engine cần bổ sung

1. Ride Chaser chạy tự do: tăng tốc, phanh, lùi, nhảy theo dốc. Không tự cuộn.
2. Tấm boost, dốc nhảy, cầu sập sau khi xe qua.
3. Cửa đếm vật phẩm (mở khi nhặt đủ 8 quả năng lượng).
4. Sàn điện và cột điện theo nhịp, lệch pha.
5. Bệ phản lực: bốc lên khi đứng, tắt sau 3 giây, rơi về chỗ cũ.
6. Tường điện bật/tắt bằng công tắc có hẹn giờ.
7. Mini-boss Lõi biến áp có cánh tay quay.

## 5. Danh sách hình cần vẽ

- **Tileset "Đường đua" (Area 1):** 47 ô viền đất đá, mặt đường nhựa, dốc nhảy, mảnh cầu sập (3 khung).
- **Tileset "Nhà máy" (Area 2):** 47 ô viền thép, tấm sàn điện (2 trạng thái), vách tháp tụ điện.
- **Vật thể:** quả năng lượng (4 khung), cột điện, tia hồ quang (4 khung), bệ phản lực (lửa 3 khung), tường điện, công tắc.
- **Nền:** Area 1: đồng hoang và cột cao thế dưới trời giông (2 lớp parallax). Area 2: tua-bin và cuộn dây khổng lồ (2 lớp).

**Hướng phối hợp:** như màn mẫu — dựng bằng khối màu tạm theo sơ đồ để chơi thử, chốt cảm giác rồi mới thay tile thật.
