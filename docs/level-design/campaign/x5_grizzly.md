# Màn: TÀU BỌC THÉP (Armored Train — Boss Crescent Grizzly)

Bản thiết kế để duyệt trước khi dựng. Sơ đồ: `maps/x5_grizzly.png`.
Màn này thay cho `x5_grizzly` hiện tại. Boss, capsule Falcon Foot, Ride Armor Pod và sub-boss xe bọc thép vẫn giữ; thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.

![Sơ đồ](maps/x5_grizzly.png)

---

## 0. Công cụ và quy ước

Dùng chung với màn mẫu (`../lo-nham-thach-kich-ban.md`, mục 0): LDtk dựng bản đồ, Pixelorama vẽ tile, Krita vẽ nền parallax. 1 ô = 32px, khung hình 30×17 ô, các lớp `Collision` / `Tiles` / `Decor` / `Foreground` / `Entities`.

---

## 1. Ý tưởng tổng

Một đoàn tàu bọc thép 8 toa lao qua sa mạc. Màn chơi có **hai tầng song song**: nóc toa (nhanh, có gió ngược) và trong toa (chật, có địch). Người chơi phải chuyển tầng liên tục, nhất là khi tàu chui hầm.

- **Area 1 – Nóc tàu giữa sa mạc:** thép nóng, cát bay, nền trôi nhanh. Dạy gió ngược, khe giữa toa, khớp nối tách và leo cột cẩu.
- **Area 2 – Khoang hàng và đầu tàu:** trong nhà, ánh đèn vàng. Cưỡi Ride Armor phá vật cản, rồi cao trào là chạy trên nóc khi tàu chui hầm.
- **Điểm nhấn trải nghiệm:** chạy trên nóc ngược gió → chui vào toa → đua với khớp nối tách → leo cần cẩu → đấu xe bọc thép → cưỡi Ride Armor → né hầm quét → boss giữa gió
- **Đường cong độ khó:** 2 → 3 → 4 → 4 → (mini-boss) → 5 → 7 → 2 → boss (thang 10).
- **Thời lượng mục tiêu:** khoảng 6–7 phút lần đầu, khoảng 3 phút khi đã quen.

Các mẫu thiết kế tham khảo (không chép bản đồ gốc):

- **X5, màn Crescent Grizzly:** truy đuổi xe bọc thép, có Ride Armor phá vật cản, capsule giáp nằm sau vách cần sức mạnh.
- **X2, màn Overdrive Ostrich:** màn tốc độ trên sa mạc, nền trôi tạo cảm giác di chuyển.
- **X8, màn Earthrock Trilobite / Gigabolt Man-O-War:** đoàn tàu và vật thể lớn đuổi theo; bản 16-bit demake làm lại các đoạn tự cuộn thành màn chơi thường.
- **X Corrupted:** hai tầng đường đi song song, lối phụ cần đổi tầng đúng lúc.

---

## 2. Kịch bản từng phòng

Tọa độ tính theo ô, gốc (0,0) ở góc trên trái thế giới, y tăng xuống dưới.

### R1 – Sân ga (x 0–40, y 30–46) · độ khó 2
- **Mục đích:** cho người chơi nhận ra "mình đang ở trên một đoàn tàu chạy".
- **Địa hình:**
  - Sân ga phẳng 27 ô, mặt sàn ở y 42.
  - Toa cuối đoàn đậu sát sân ga. Sau 3 giây kể từ khi vào phòng, còi hú và đoàn tàu chạy. Nền parallax bắt đầu trôi.
  - Nhảy lên nóc toa (cao 8 ô so với sân ga, đứng trên thùng hàng để với tới).
- **Địch:**
  - 1 Sniper trên sân ga.
  - 1 Drone bay ngang nóc toa.
- **Trang trí:** biển ga, đèn tín hiệu, cát bay.

### R2 – Nóc toa 1–3 (x 40–124, y 30–46) · độ khó 3
- **Mục đích:** dạy **hai tầng đường đi** của màn: nóc toa (nhanh nhưng có gió) và trong toa (không gió nhưng chật, có địch).
- **Địa hình:**
  - 3 toa dài 24–26 ô, giữa các toa là **khe 4 ô**. Rơi xuống đường ray là mất mạng.
  - Nóc toa ở y 34, sàn trong toa ở y 42, trần trong toa thấp (cao 7 ô).
  - Mỗi đầu toa có cửa để chui vào/ra.
- **Bẫy – gió ngược:** trên nóc toa, gió đẩy lùi 55px/giây. Lướt hoặc nhảy dài ngược gió ngắn đi rõ rệt, nên nhảy qua khe phải lấy đà.
- **Địch:**
  - 1 Sniper trong toa 1 và 1 trong toa 3, đứng ở cuối toa, bắn dọc hành lang.
  - 1 Drone trên nóc toa 2.
- **Vật phẩm:** Reploid #1 trong toa 2.

### R3 – Khớp nối tách (x 124–158, y 30–46) · độ khó 4
- **Mục đích:** áp lực thời gian lần đầu.
- **Cơ chế – khớp nối tách:**
  - Khi người chơi bước lên toa trước khớp, khớp nối nổ chốt (có tiếng "cạch" và tia lửa).
  - Khe giữa hai toa **rộng dần từ 0 lên 6 ô trong 6 giây** (1 ô mỗi giây), toa phía sau tụt lại.
  - Qua sớm thì bước qua được; chậm hơn 4 giây thì phải lướt-nhảy; quá 6 giây thì không với tới, toa trôi về checkpoint (mất mạng).
- **Địch:**
  - 1 Drone lượn đúng trên khe: bắn ngay hoặc bỏ qua, không nên đứng đánh.
  - 1 Sniper trong toa sau.
- **Ghi chú:** trên nóc vẫn có gió ngược, nên cách an toàn là chui vào trong toa rồi chạy.

### R4 – Toa cần cẩu (x 158–176, y 4–46) · độ khó 4
- **Mục đích:** đoạn **leo dọc** duy nhất, cũng là đường vượt chỗ đoàn tàu bị đứt.
- **Địa hình:**
  - Toa chở cần cẩu có cột tháp cao 34 ô (từ y 42 lên y 8). Hai vách là khung giàn, đá tường được.
  - 4 kệ nghỉ zigzag cách nhau 7 ô.
  - Trên đỉnh có **móc cẩu chạy trên cáp**: đứng lên móc thì nó trượt sang phải với tốc độ 90px/giây, chở người chơi vượt khoảng trống giữa hai đoạn tàu rồi thả xuống toa sau.
- **Bẫy – đối trọng lắc:** khối đối trọng 5 ô lắc ngang giữa giếng, chu kỳ 3 giây. Ở giữa đường leo, phải chờ nó lắc qua.
- **Địch:** 1 Drone gần đỉnh.
- **Vật phẩm:** Reploid #2 trên kệ thứ hai, bị kẹt sau đối trọng.
- **Giáp hỗ trợ:** Gaea bám tường không trượt, dễ chờ nhịp đối trọng.

### Mini-boss – Xe tải bọc thép (x 176–208, y 30–46) · độ khó 5
- **Đấu trường là một toa sàn phẳng 30 ô**, hai đầu có thành chắn thấp (6 ô) để đá tường.
- **Xe tải bọc thép** chạy trên đường song song phía sau toa, nhảy lên toa để húc.
- **Đòn đánh:**
  - Bắn 2 quả đạn pháo theo đường vòng cung: đứng dưới điểm rơi thì bị trúng (có bóng báo trước).
  - Tăng tốc húc ngang từ đầu này sang đầu kia toa: đá tường lên thành chắn để né.
  - Thả 3 mìn lăn trên sàn.
- **Điểm yếu:** buồng lái lộ ra 2 giây sau mỗi cú húc.
- **Phần thưởng:** mở đường sang toa Ride Armor. Hạ không mất máu thì được thưởng Souls.

### R5 – Toa Ride Armor (x 208–262, y 30–50) · độ khó 5
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** cưỡi **Ride Armor** trong khoang hàng, phá vật cản để tìm lối phụ.
- **Địa hình:**
  - Khoang hàng dài 54 ô, trần ở y 34, sàn ở y 42.
  - **Băng chuyền chạy ngược** (đẩy sang trái 80px/giây) dài 28 ô.
  - 2 **thùng thép** chắn đường. Chỉ Ride Armor đấm vỡ được; X đi bộ phải nhảy qua (sát trần, khó).
- **Địch:**
  - 1 Brute giữa băng chuyền.
  - 1 Sniper cuối khoang.
- **Vật phẩm:** Reploid #3 sau thùng thép thứ hai.
- **Lối phụ (Capsule Falcon Foot):**
  - Cuối khoang có đoạn **sàn thép nứt** 10 ô (x 248–258). Ride Armor nhảy rồi dậm xuống thì sàn vỡ.
  - Bên dưới là **khoang két** chứa capsule Falcon Foot.
  - Ride Armor không leo ra được: bỏ xe, đá tường vách khoang lên lại.
- **Lối phụ (Sub-Tank):** trèo lên thùng thép thứ nhất, đứng trên nóc thùng rồi nhảy lên **cửa sập nóc toa**. Sub-Tank nằm trên nóc, giữa gió.

### R6 – Nóc toa đầu và hầm (x 262–338, y 30–46) · độ khó 7
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** cao trào của màn. Phải đọc cảnh báo và đổi tầng liên tục trong gió mạnh.
- **Cơ chế – hầm quét:**
  - Đoàn tàu chui qua **2 đường hầm** (dài 14 và 20 ô). Trong hầm, trần chỉ cách nóc toa 1 ô.
  - Đứng trên nóc khi tàu vào hầm là bị quét (mất 1/3 máu và rơi xuống khe).
  - Trước mỗi hầm 1.5 giây: đèn đỏ chớp, còi hú, chữ "TUNNEL".
  - Cách tránh: chui qua cửa đầu toa vào trong, hoặc nằm sát nóc toa và lướt liên tục (giáp Shadow có thể bò).
- **Gió:** mạnh nhất màn, −80px/giây trên nóc.
- **Địch:**
  - 1 Drone bay trong khe giữa hai toa đầu: buộc phải ra khỏi toa đúng lúc.
  - 1 Drone ở cuối phòng.
- **Vật phẩm:** Reploid #4 trong toa cuối.
- **Lối phụ (Heart Tank):**
  - Giữa hai hầm có **cột tín hiệu** ngang tầm nóc toa (x ≈ 292, y ≈ 31).
  - Phải nhảy lên nóc ngay khi tàu ra khỏi hầm 1 rồi nhảy với lên cột trước khi tàu chạy qua (cửa sổ khoảng 2 giây).
  - Giáp Falcon bay lên được bất kỳ lúc nào giữa hai hầm.

### R7 – Toa chỉ huy (x 338–368, y 30–46) · độ khó 2
- Phòng nghỉ trước boss: một viên năng lượng nhỏ, cửa boss.
- Công tắc **thả toa** (tùy chọn): bắn vào thì toa phía sau tách ra, mở ngắn đường quay lại nếu chết ở boss.

### BOSS – Crescent Grizzly (x 368–400, y 28–46)
- **Đấu trường là nóc toa chỉ huy dài 32 ô**, không có vách. Rơi khỏi mép là mất mạng.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (lao vuốt, ném bánh xe, đào lên).
- **Pha 2** (dưới 50% HP):
  - **Gió ngang đổi chiều mỗi 6 giây** (mũi tên trên HUD báo trước 1 giây), đẩy 70px/giây về phía mép.
  - Grizzly lợi dụng gió để lao xa hơn.
  - Một đường hầm ngắn quét qua mỗi 20 giây: cả X và Grizzly phải nằm xuống. Grizzly cứng đờ 1 giây sau mỗi lần nằm, đó là lúc bắn.
- Điểm yếu giữ nguyên theo dữ liệu game.

---

## 3. Bảng vật phẩm và kẻ địch

| Loại | Số lượng | Vị trí |
|---|---|---|
| Sniper | 5 | R1, R2 ×2, R3, R5 |
| Drone | 6 | R1, R2, R3, R4, R6 ×2 |
| Brute | 1 | R5 |
| Mini-boss | 1 | MID |
| Reploid cứu | 4 | R2, R4, R5, R6 |
| Heart Tank | 1 | R6 |
| Sub-Tank | 1 | R5 |
| Capsule Falcon Foot | 1 | R5 |
| Ride Armor / Chaser | 1 | R5 |
| Công tắc | 1 | R7 |
| Checkpoint | 2 | R5, R6 |

Tổng 12 kẻ địch thường (bản cũ: 20 con xếp đều), đặt có chủ đích theo mục đích từng phòng.

---

## 4. Những gì engine cần bổ sung

1. Nền parallax trôi liên tục để tạo cảm giác tàu chạy (thế giới đứng yên, chỉ nền và đường ray trôi).
2. Vùng gió đẩy ngang có tốc độ chỉnh được, đổi chiều theo nhịp.
3. Khớp nối tách: một đoạn toa trượt lùi theo thời gian sau khi người chơi kích hoạt.
4. Hầm quét: khối trần chạy ngang qua nóc tàu theo lịch, có cảnh báo trước.
5. Móc cẩu chạy trên cáp (bệ di động theo đường ray trên cao).
6. Sàn nứt chỉ vỡ khi Ride Armor dậm; thùng thép chỉ Ride Armor đấm vỡ.
7. Mini-boss Xe tải bọc thép chạy song song và nhảy lên toa.

## 5. Danh sách hình cần vẽ

- **Tileset "Toa thép" (Area 1):** 47 ô viền thép tán đinh, nóc toa, đầu toa có cửa, khớp nối.
- **Tileset "Khoang hàng" (Area 2):** 47 ô viền, băng chuyền, thùng thép (2 trạng thái), sàn nứt (2 trạng thái).
- **Vật thể:** móc cẩu, đối trọng lắc, cột tín hiệu, khung hầm đi qua (khối trần lớn), cửa sập nóc toa.
- **Nền:** Area 1: sa mạc và núi đá trôi nhanh (2 lớp parallax). Area 2: vách khoang và đèn chớp qua cửa sổ (2 lớp).

**Hướng phối hợp:** như màn mẫu — dựng bằng khối màu tạm theo sơ đồ để chơi thử, chốt cảm giác rồi mới thay tile thật.
