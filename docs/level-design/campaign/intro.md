# Màn: CAO TỐC NEO ARCADIA (Neo Arcadia Highway — Intro — Boss 1D-1000 → High Max)

Bản thiết kế để duyệt trước khi dựng. Sơ đồ: `maps/intro.png`.
Màn này thay cho `intro` hiện tại. Boss 1D-1000 → High Max, capsule Fourth Armor và Ride Armor Pod giữ nguyên; thêm 4 Reploid, 1 Heart Tank, 1 Sub-Tank và thay toàn bộ địa hình.

![Sơ đồ](maps/intro.png)

---

## 0. Công cụ và quy ước

Dùng chung với màn mẫu (`../lo-nham-thach-kich-ban.md`, mục 0): LDtk dựng bản đồ, Pixelorama vẽ tile, Krita vẽ nền parallax. 1 ô = 32px, khung hình 30×17 ô, các lớp `Collision` / `Tiles` / `Decor` / `Foreground` / `Entities`.

---

## 1. Ý tưởng tổng

Cao tốc trên cao của Neo Arcadia bị đánh sập lúc hoàng hôn. Đây là màn dạy chơi: **mỗi phòng dạy đúng một kỹ năng** và cho thử ngay trong vùng an toàn trước khi dùng thật.

- **Area 1 – Cao tốc (ngoài trời):** bê tông, cột đèn đổ, trời cam. Dạy chạy, bắn, nhảy hố, đá tường, lướt, rồi cưỡi Ride Armor.
- **Area 2 – Hầm (trong nhà):** hầm tối đèn vàng. Ôn lại mọi thứ trong không gian chật, có bí mật trên trần.
- **Điểm nhấn trải nghiệm:** chạy ngang → nhảy hố → leo dọc lần đầu → lướt qua khe → cưỡi Ride Armor phá tường → hầm tối → boss nhện bám trần
- **Đường cong độ khó:** 1 → 2 → 2 → 3 → 3 → (mini-boss) → 3 → 2 → boss (thang 10).
- **Thời lượng mục tiêu:** khoảng 4–5 phút lần đầu, khoảng 2 phút khi đã quen.

Các mẫu thiết kế tham khảo (không chép bản đồ gốc):

- **X4 / X5, màn mở đầu:** mỗi đoạn dạy một kỹ năng, boss kích thước lớn, kết thúc bằng trận không thể thắng để dẫn truyện.
- **X8, màn mở đầu (Noah's Park):** màn "thẳng", không có cơ chế nặng; vật thể lớn cháy nổ làm vật cản.
- **X8 16-bit demake:** cùng bố cục mở đầu nhưng làm lại dạng 2D thuần, có bí mật dưới gầm cầu.
- **Mega Man X (SNES), màn cao tốc:** cầu sập, mặt đường làm sàn chính. Chỉ lấy nhịp dạy kỹ năng, không chép bố cục.

---

## 2. Kịch bản từng phòng

Tọa độ tính theo ô, gốc (0,0) ở góc trên trái thế giới, y tăng xuống dưới.

### R1 – Làn đường sập (x 0–52, y 40–54) · độ khó 1
- **Mục đích:** dạy chạy, nhảy, bắn. Không có chỗ nào chết được.
- **Địa hình:**
  - Mặt đường phẳng 52 ô, mặt đất ở y 50.
  - 2 khối bê tông thấp (cao 2 và 3 ô) để dạy nhảy lên vật cản.
  - Bảng chỉ dẫn nút hiện ngay trên đầu nhân vật khi đi ngang (NHẢY, rồi BẮN).
- **Địch:**
  - 1 Sniper đứng trên khối bê tông thứ hai, bắn thẳng, chậm: dạy bắn đáp trả.
  - 1 Sniper cuối phòng, đứng ngang tầm.
- **Trang trí:** xe bỏ hoang, cột đèn đổ, khói xa ở nền, trời hoàng hôn.

### R2 – Cầu vượt gãy (x 52–116, y 40–58) · độ khó 2
- **Mục đích:** dạy nhảy qua hố và bắn chéo khi đang nhảy.
- **Địa hình:**
  - Mặt cầu gãy làm 3 đoạn, giữa là **2 hố rộng 4 ô**.
  - Rơi vào hố gãy thì mất 2 máu và được đặt lại ở mép, không mất mạng (màn dạy chơi).
  - Ba trụ cầu đỡ bên dưới. Đáy phòng là vực thật (y 57), chỉ rơi được nếu cố ý đi xuống gầm cầu.
- **Địch:**
  - 1 Drone bay lượn đúng trên hố thứ hai: buộc phải bắn trước khi nhảy hoặc bắn chéo khi đang trên không.
  - 1 Sniper cuối cầu.
- **Vật phẩm:** Reploid #1 ở cuối cầu.
- **Lối phụ (Sub-Tank):**
  - Ở hố thứ hai, thả người bám vách trái của hố rồi trượt xuống gờ hẹp dưới gầm cầu (x ≈ 82, y ≈ 55).
  - Sub-Tank nằm trên gờ. Đá tường vào trụ cầu để leo lại lên mặt cầu.
  - Đây là bài học đầu tiên về "lối phụ nằm ngoài tầm nhìn".

### R3 – Trụ cầu (x 116–134, y 16–58) · độ khó 2
- **Mục đích:** đoạn dọc ngắn đầu tiên, dạy **đá tường**.
- **Địa hình:**
  - Giếng rộng 14 ô kẹp giữa hai trụ bê tông, cao 36 ô (từ y 52 lên y 20).
  - 4 kệ nghỉ xếp zigzag cách nhau 7 ô. Người mới cứ nhảy kệ, người quen đá tường thẳng lên.
  - Bảng chỉ dẫn "giữ hướng vào vách + NHẢY" hiện khi chạm vách lần đầu.
- **Địch:** 1 Drone giữa giếng, bay chậm qua lại.
- **Lối ra:** khe phía trên vách phải (y 17–24), dẫn ra tầng trên cao tốc.

### R4 – Tầng trên cao tốc (x 134–204, y 10–24) · độ khó 3
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** dạy **lướt** (dash), cả lướt để vượt nhanh lẫn lướt để chui qua khe thấp.
- **Địa hình:**
  - Mặt đường thẳng 70 ô ở y 22.
  - 2 xe cháy làm vật cản. Lửa trên nóc xe bùng 1.0 giây rồi tắt 2.0 giây: nhảy qua lúc lửa tắt, hoặc lướt nhảy cho xa.
  - **Biển báo sập** treo thấp ở x ≈ 180, chỉ chừa khe cao 2 ô. Đứng thẳng không qua được, phải lướt.
- **Địch:**
  - 1 Brute đứng giữa hai xe cháy: chắn đường, phải bắn 4 phát hoặc nạp đạn.
  - 1 Sniper sau biển báo.
  - 1 Drone bay cao cuối phòng.
- **Vật phẩm:** Reploid #2 sau xe cháy thứ hai.

### R5 – Bãi Ride Armor (x 204–248, y 2–24) · độ khó 3
- **Mục đích:** lần đầu cưỡi **Ride Armor** và mở lối phụ bằng sức mạnh của nó.
- **Địa hình:**
  - Bãi đậu xe 2 tầng. Tầng dưới (y 22) là đường chính, tầng trên (y 13) là sàn bê tông vỡ.
  - Bậc thang khối bê tông cao 3 và 6 ô dẫn lên tầng 2. Ride Armor nhảy được bậc này, X đi bộ cũng lên được.
  - Ride Armor Pod đậu sẵn đầu phòng (x ≈ 208).
- **Địch:** 1 Brute ở tầng dưới. Ride Armor đấm 1 phát là hạ: cho người chơi cảm giác mạnh.
- **Lối phụ (Capsule Fourth Armor):**
  - **Tường bê tông nứt** ở tầng 2 (x ≈ 234). Chỉ Ride Armor đấm vỡ được (3 cú).
  - Sau tường là buồng nhỏ chứa capsule Fourth Armor (bộ đầy đủ).
  - Ride Armor không qua được cửa sang phòng sau: phải xuống xe ở cuối phòng.

### Mini-boss – Trực thăng tuần tra (x 248–278, y 8–24) · độ khó 4
- **Đấu trường phẳng 26 ô**, hai vách để đá tường lên tầm bắn.
- **Trực thăng tuần tra** bay ngang phía trên, đổi hướng ở hai vách.
- **Đòn đánh:**
  - Thả 3 quả bom thành hàng: chạy qua khe giữa các quả.
  - Hạ thấp càng quét ngang sàn (báo trước bằng đèn đỏ 1 giây): nhảy hoặc đá tường để né.
- **Điểm yếu:** cánh quạt chỉ trúng khi đá tường lên ngang tầm. Dạy rằng đá tường cũng là cách tấn công.
- **Phần thưởng:** mở cửa vào hầm. Hạ không mất máu thì được thưởng Souls.

### R6 – Đường hầm đèn vàng (x 278–340, y 12–24) · độ khó 3
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** áp lực nhẹ trong không gian kín, chuẩn bị tinh thần cho boss.
- **Địa hình:**
  - Hầm thẳng 62 ô, trần thấp (cao 7 ô).
  - Đoạn giữa có đèn trần chớp: sáng 2 giây, tối 1 giây. Lúc tối chỉ thấy đèn mắt địch.
- **Địch:** 2 Drone lao vào từ hai đầu hầm theo đường chéo.
- **Vật phẩm:** Reploid #3 giữa hầm.
- **Lối phụ (Heart Tank):**
  - **Khe thông gió** trên trần ở x ≈ 318. Đứng dưới khe, lướt rồi nhảy (lướt-nhảy cao hơn nhảy thường) để bám vào miệng khe.
  - Trong ống thông gió phải bò ngang 10 ô, Heart Tank ở cuối ống.
  - Giáp Fourth (lơ lửng) vào khe dễ hơn.

### R7 – Lối ra cao tốc (x 340–370, y 12–24) · độ khó 2
- Phòng nghỉ trước boss: Reploid #4, một viên năng lượng nhỏ, cửa boss.

### BOSS – 1D-1000 / High Max (x 370–402, y 4–24)
- **Đấu trường 26 ô**, kín bốn phía. Trần và hai vách là nơi nhện 1D-1000 bò.
- **Pha 1** (100–50% HP):
  - Nhện bò dọc trần, thả bom nhện rơi thẳng.
  - Bò xuống một vách rồi lao ngang sàn: nhảy qua hoặc đá tường vách đối diện.
- **Pha 2** (dưới 50% HP):
  - Nhện giật đứt dây cáp trần, 3 đoạn cáp điện rơi xuống sàn thành vùng điện 2 giây.
  - Tốc độ bò tăng 30%.
- **Kết thúc:** hạ 1D-1000 thì High Max đáp xuống giữa sân. Trận này **không thể thắng**: sau 20 giây hoặc khi X còn 1/4 máu thì chuyển cảnh.
- Điểm yếu giữ nguyên theo dữ liệu game.

---

## 3. Bảng vật phẩm và kẻ địch

| Loại | Số lượng | Vị trí |
|---|---|---|
| Sniper | 4 | R1 ×2, R2, R4 |
| Drone | 5 | R2, R3, R4, R6 ×2 |
| Brute | 2 | R4, R5 |
| Mini-boss | 1 | MID |
| Reploid cứu | 4 | R2, R4, R6, R7 |
| Heart Tank | 1 | R6 |
| Sub-Tank | 1 | R2 |
| Capsule Fourth Armor (bộ đầy đủ) | 1 | R5 |
| Ride Armor / Chaser | 1 | R5 |
| Checkpoint | 2 | R4, R6 |

Tổng 11 kẻ địch thường (bản cũ: 20 con xếp đều), đặt có chủ đích theo mục đích từng phòng.

---

## 4. Những gì engine cần bổ sung

1. Bảng chỉ dẫn nút hiện theo vùng (Entity `Tutorial` có chữ và nút).
2. Hố "dạy chơi": rơi thì mất 2 máu và đặt lại ở mép thay vì mất mạng (cờ `softPit` trên vùng).
3. Ride Armor Pod: lên/xuống xe, đấm, nhảy thấp. Xe không qua được cửa phòng.
4. Tường nứt chỉ Ride Armor phá được (thuộc tính `breakBy: rideArmor`).
5. Đèn trần chớp theo nhịp làm tối khung hình.
6. Mini-boss Trực thăng tuần tra; boss nhện bò trên trần và vách (di chuyển theo viền đấu trường).

## 5. Danh sách hình cần vẽ

- **Tileset "Cao tốc" (Area 1):** 47 ô viền bê tông, mặt đường kẻ vạch, mép gãy có cốt thép, trụ cầu.
- **Tileset "Hầm" (Area 2):** 47 ô viền, ô đèn vàng, ô ống thông gió.
- **Vật thể:** xe cháy (lửa 4 khung), biển báo sập, khối bê tông, tường nứt (2 trạng thái), cửa boss.
- **Nền:** Area 1: thành phố hoàng hôn và khói (2 lớp parallax). Area 2: vách hầm và quạt thông gió (2 lớp).

**Hướng phối hợp:** như màn mẫu — dựng bằng khối màu tạm theo sơ đồ để chơi thử, chốt cảm giác rồi mới thay tile thật.
