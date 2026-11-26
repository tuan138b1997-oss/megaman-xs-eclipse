# Màn mẫu: LÒ NHAM THẠCH (Volcano Base — Boss Burn Dinorex)

Bản thiết kế để duyệt trước khi dựng. Sơ đồ: `lo-nham-thach-map.png`.
Màn này thay cho `x5_dinorex` hiện tại. Boss, capsule Gaea Arm, 4 Reploid, Heart Tank và Sub-Tank vẫn giữ nguyên, chỉ thay địa hình và nhịp chơi.

---

## 0. Công cụ và quy ước

| Hạng mục | Lựa chọn | Lý do |
|---|---|---|
| Vẽ bản đồ | **LDtk** (miễn phí) | Tự ghép viền theo luật, tách phòng (Level) rõ ràng, có lớp Entity để đặt địch/bẫy/vật phẩm, xuất JSON gọn để game JS đọc trực tiếp. |
| Vẽ tile và trang trí | **Pixelorama** (miễn phí); nâng cấp lên **Aseprite** nếu muốn | Có chế độ vẽ tilemap, xuất sprite sheet PNG. |
| Nền parallax | **Krita** (miễn phí) | Vẽ nền xa và nền giữa khổ lớn. |
| Bảng màu | Lospec, 24–32 màu cho chủ đề lửa | Đồng bộ tông với sprite PS. |

- **Kích thước:** 1 ô = 32px trong game (vẽ ở 16px rồi phóng ×2). Khung hình = 30×17 ô. Nhân vật cao khoảng 1.6 ô.
- **Lớp LDtk:**
  - `Collision`: IntGrid. Giá trị: 1 = đặc, 2 = dốc 45°, 3 = dốc 22.5°, 4 = kệ một chiều, 5 = sàn vỡ, 6 = băng chuyền, 9 = dung nham.
  - `Tiles`: tự ghép từ Collision.
  - `Decor`, `Foreground`: trang trí.
  - `Entities`: địch, bẫy, vật phẩm, checkpoint, vùng.
- **Màn gồm 10 phòng** nối liền theo tọa độ thế giới (LDtk "free layout"). Camera bám cả ngang lẫn dọc, khóa trong khung từng phòng.

---

## 1. Ý tưởng tổng

Một nhà máy luyện quặng xây trên miệng núi lửa đang hoạt động.

- **Area 1 – Miệng núi (ngoài trời):** đá bazan, trời đỏ, tro bay. Dạy chạy, lướt, đá tường, rồi thử bằng xe quặng trên ray.
- **Area 2 – Lò luyện (trong nhà):** thép xám, ánh lửa cam. Dạy né theo nhịp (máy ép, thác nham), cao trào là **giếng nham dâng** phải leo thật nhanh.
- **Điểm nhấn trải nghiệm:** chạy ngang → leo dọc → nhảy trên vật thể di động → né theo nhịp → bị đuổi theo chiều dọc → boss.
- **Đường cong độ khó:** 2 → 3 → 4 → 4 → (mini-boss) → 5 → 7 → 6 → 6 → boss (thang 10).
- **Thời lượng mục tiêu:** khoảng 6–8 phút lần đầu, khoảng 3 phút khi đã quen.

Các mẫu thiết kế tham khảo từ dòng X (không chép bản đồ gốc):

- **X4, màn núi lửa:** dung nham dâng buộc người chơi leo nhanh.
- **X5, màn Dinorex:** bẫy phun lửa đặt cố định trên nền.
- **X6, màn Heatnix:** dung nham lấp nửa đấu trường boss.
- **X8 (bản gốc và bản 16-bit demake):** giếng dọc dài đầy máy móc. Bản demake làm lại các đoạn tự cuộn thành màn chơi thường.
- **X Corrupted:** tile mới hoàn toàn nhưng kết hợp cơ chế của nhiều phần X, lối phụ cần kỹ năng.

---

## 2. Kịch bản từng phòng

Tọa độ tính theo ô, gốc (0,0) ở góc trên trái thế giới, y tăng xuống dưới.

### R1 – Bãi đáp (x 0–60, mặt đất y ≈ 52) · độ khó 2
- **Mục đích:** làm quen điều khiển, an toàn. Đoạn này cho người chơi thấy "màn này có dốc và dung nham".
- **Địa hình:**
  - Nền phẳng 18 ô, rồi **dốc 22.5° đi lên**, rồi một bệ cao.
  - **Hố nham rộng 4 ô** phải nhảy qua (rơi xuống là mất máu và bị đẩy về mép, không chết ngay).
  - Hạ xuống một bậc, cửa sang R2.
- **Địch:**
  - 2 Sniper, một trên đỉnh dốc, một sau hố.
  - 1 Drone bay trên hố để dạy bắn chéo khi nhảy.
- **Vật phẩm:** Reploid #1 ở cuối phòng.
- **Trang trí:** cọc tiêu, khung giàn khoan sập, mạch nham phát sáng trong vách đá.

### R2 – Sườn đá lăn (x 60–140, dốc đi xuống từ y 52 đến 58) · độ khó 3
- **Mục đích:** đoạn tốc độ đầu tiên. Đá lăn từ phía sau đuổi theo người chơi.
- **Địa hình:**
  - Dốc dài 50 ô đi xuống.
  - **2 hốc né** (sâu 2 ô) để nằm tránh đá. Lướt qua đá được nếu canh khung bất tử.
  - Cuối dốc là bãi phẳng.
- **Bẫy:** đá lăn sinh ra mỗi 2.2 giây ở đầu dốc, lăn nhanh dần, vỡ khi chạm tường cuối.
- **Địch:** 1 Brute ở chân dốc, chặn đường để buộc người chơi chọn dừng lại bắn hoặc nhảy qua.
- **Lối phụ (Heart Tank):** chuỗi 4 kệ đi lên phía trên dốc. Phải đá tường lên kệ đầu rồi nhảy liên tiếp trong lúc né đá. Heart Tank nằm ở kệ cuối (x ≈ 111, y ≈ 32).
  - Giáp Falcon / Fourth: bay hoặc lơ lửng lên dễ hơn.

### R3 – Giếng thông hơi (x 140–160, leo từ y 58 lên y 12) · độ khó 4
- **Mục đích:** đoạn dọc đầu tiên, luyện **đá tường liên tiếp**.
- **Địa hình:** giếng rộng 16 ô, hai vách leo được, 3 kệ nhỏ để nghỉ.
- **Bẫy:**
  - **6 ống phun hơi nóng** trên vách, xen kẽ trái/phải.
  - Phun 1.2 giây, tắt 1.6 giây, các ống lệch pha nhau.
  - Leo đúng nhịp thì không phải dừng.
- **Giáp hỗ trợ:**
  - Gaea: bám tường không trượt, dễ canh nhịp hơn.
  - Shadow: miễn sát thương gai nhưng **không** miễn hơi nóng.
- **Lối ra:** mép phải phía trên, dẫn sang R4.

### R4 – Đường ray quặng (x 160–230, ray ở y 12, dung nham ở y 20) · độ khó 4
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** nhảy trên vật thể di động phía trên dung nham.
- **Địa hình:**
  - Một đường ray chạy ngang. **4 xe quặng** (rộng 4 ô) chạy liên tục từ trái sang phải, tốc độ 110px/giây.
  - 2 cột đá giữa dòng nham để dừng chân.
- **Địch:** 3 Drone bay ngang tầm ray, thả bom xuống.
- **Lối phụ (Sub-Tank):** một gờ hẹp sát mặt dung nham (x ≈ 195, y ≈ 18), dưới gầm ray.
  - Thả người từ xe xuống: giáp thường phải canh rất chuẩn.
  - Fourth lơ lửng, Falcon bay: lấy an toàn.
- **Cửa ra:** một bệ đá dẫn vào phòng mini-boss.

### Mini-boss – Máy khoan nham (x 230–260) · độ khó 5
- **Đấu trường phẳng 30 ô**, hai vách để đá tường.
- **Máy khoan** chui ra từ trần hoặc sàn theo thứ tự ngẫu nhiên. Khi trồi lên để lộ lõi 2 giây, đó là lúc bắn.
- **Đòn đánh:**
  - Mảnh đá văng chéo lên.
  - Lao ngang sát sàn: nhảy hoặc đá tường để né.
- **Phần thưởng:** mở cửa vào Area 2. Hạ không mất máu thì được thưởng Souls.

### R5 – Lò ép (x 260–312, nội thất, sàn y 18) · độ khó 5
- **Mục đích:** né theo nhịp trong không gian chật. Đây cũng là lần đổi không gian: từ ngoài trời vào trong lò.
- **Địa hình:**
  - Trần thấp.
  - **Băng chuyền chạy ngược** (đẩy sang trái 120px/giây).
  - **5 máy ép** đập xuống theo nhịp: chờ 1.4 giây, đập 0.25 giây, nâng lên 0.6 giây. Các máy lệch pha thành một làn sóng.
  - Giữa các máy có hốc an toàn.
- **Địch:**
  - 1 Sniper đứng trên nóc một máy ép.
  - Reploid #2 kẹt giữa hai máy ép (phải canh nhịp để cứu).
- **Chuyển cảnh:** 8 ô cuối là **sàn sập**. Đứng lên thì sau 0.5 giây sàn rơi, người chơi rơi xuống đáy R6 (có cảnh rung và chữ "WARNING").

### R6 – Giếng nham dâng (x 312–344, từ đáy y 72 leo lên y 12) · độ khó 7 (cao trào)
- **Mục đích:** bị đuổi theo chiều dọc. Đây là đoạn đáng nhớ nhất của màn.
- **Cơ chế:**
  - **Dung nham dâng từ đáy**, tốc độ 70px/giây, tăng lên 95px/giây ở nửa trên.
  - Chạm dung nham là chết.
  - Dung nham tạm dừng 2 giây mỗi khi người chơi đặt chân lên một kệ "an toàn" có đèn xanh (2 kệ).
- **Địa hình:**
  - Giếng rộng 28 ô, 9 kệ xếp zigzag.
  - 4 trong số đó là **sàn vỡ**: rung 0.4 giây rồi rơi.
  - Hai vách đá tường được, nên người chơi giỏi có thể bỏ kệ và leo thẳng.
- **Địch:** 2 Drone, chỉ để gây áp lực. Bắn hạ hay né đều được.
- **Lối ra:** kệ rộng ở đỉnh, đi thẳng sang R7. Dung nham dừng lại ngay dưới mép cửa.

### R7 – Kênh xỉ (x 344–404, nội thất, sàn y 16) · độ khó 6
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** kết hợp mọi thứ đã học: nhịp, nhảy, bắn.
- **Bẫy:**
  - **3 thác nham** đổ từ trần xuống thành cột lửa. Bật 1.5 giây, tắt 1.5 giây, lệch pha nhau.
  - **2 ống phun lửa**: một trên sàn (bắn lên), một trên trần (bắn xuống). Bắn hạ được bằng 3 viên đạn thường.
  - Một hố nham 4 ô gần cuối phòng.
- **Vật phẩm:**
  - Reploid #3 giữa hai thác nham.
  - Reploid #4 ở R8 (phòng tạm trước boss).
- **Lối phụ (Capsule Gaea Arm):**
  - **Tường nứt** ở cuối phòng, chỉ phá được bằng **đạn nạp đầy** (Gaea Shot phá bằng 1 phát).
  - Sau tường là hầm nhỏ chứa capsule Gaea – Arm Part.

### R8 – Cổng (x 404–434) · độ khó 2
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss.

### BOSS – Burn Dinorex (x 434–464)
- **Đấu trường 30 ô**, sàn đá. Hai mép là **dung nham rộng 3 ô**.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (flame, stomp, breath).
- **Pha 2** (dưới 50% HP):
  - Dung nham hai mép **dâng lên 1 ô**, thu hẹp sàn còn 22 ô.
  - Hai vách thành dung nham, không đá tường được. Muốn né phải lướt và nhảy chính xác.
- Điểm yếu giữ nguyên theo dữ liệu game.

---

## 3. Bảng vật phẩm và kẻ địch

| Loại | Số lượng | Vị trí |
|---|---|---|
| Sniper | 4 | R1 ×2, R5 ×1, R2 (đầu dốc) ×1 |
| Drone | 7 | R1 ×1, R4 ×3, R6 ×2, R7 ×1 |
| Brute | 1 | R2 chân dốc |
| Ống phun lửa (bắn hạ được) | 2 | R7 |
| Mini-boss | 1 | Máy khoan nham |
| Reploid | 4 | R1, R5, R7, R8 |
| Heart Tank | 1 | R2 lối trên |
| Sub-Tank | 1 | R4 dưới ray |
| Capsule Gaea Arm | 1 | R7 sau tường nứt |
| Checkpoint | 2 | Đầu R4, đầu R7 |

Tổng 12 kẻ địch thường. Hiện tại mỗi màn có 20 con xếp đều nhau, nên bản mới ít hơn nhưng đặt có chủ đích.

---

## 4. Những gì engine cần bổ sung

1. Đọc file `.ldtk` (JSON): Collision IntGrid, các lớp tile, Entities.
2. Camera bám cả ngang và dọc, khóa trong khung từng phòng. Thế giới có kích thước tùy màn.
3. Dốc 45° và 22.5° (va chạm theo độ cao của ô).
4. Vật thể mới: đá lăn, xe quặng trên ray, máy ép, ống hơi theo nhịp, thác nham, sàn vỡ, dung nham dâng có điểm dừng, tường nứt (cần đạn nạp), sàn sập chuyển cảnh.
5. Mini-boss Máy khoan nham (dùng sprite có sẵn trong kho X5/X6 hoặc vẽ mới).
6. Giữ nguyên định dạng cũ cho 25 màn còn lại. Chỉ màn có file `.ldtk` mới dùng engine mới.

## 5. Danh sách hình cần vẽ

- **Tileset "Đá bazan" (Area 1):** 47 ô viền tự ghép, 4 ô dốc, 6 ô trang trí (mạch nham, đá vụn, cọc tiêu).
- **Tileset "Lò luyện" (Area 2):** 47 ô viền, ô lưới thép, ô ống dẫn, ô tường nứt (2 trạng thái).
- **Vật thể:** đá lăn (4 khung), xe quặng, máy ép (3 khung), ống hơi (3 khung), thác nham (4 khung), sàn vỡ (3 khung), bề mặt dung nham động (4 khung).
- **Nền:**
  - Area 1: trời đỏ và núi xa (2 lớp parallax).
  - Area 2: dàn ống và lò cao (2 lớp).

**Hướng phối hợp:** mình dựng toàn bộ bằng tile tạm (khối màu như sơ đồ) để bạn chơi thử trước. Sau khi bạn chốt cảm giác, bạn hoặc mình vẽ tile thật trong Pixelorama và thay vào. Không cần sửa bản đồ, vì LDtk tự ghép lại theo luật.
