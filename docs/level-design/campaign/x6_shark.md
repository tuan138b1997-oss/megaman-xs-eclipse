# Màn: PHÒNG THÍ NGHIỆM TÁI CHẾ (Recycle Lab — Boss Metal Shark Player)

Bản thiết kế để duyệt trước khi dựng. Sơ đồ: `maps/x6_shark.png`.
Màn này thay cho `x6_shark` hiện tại. Boss, capsule Shadow Foot, trần máy ép thủy lực có hốc trú, Ride Armor Pod và tường rác vẫn giữ; đoạn tự cuộn được làm lại thành tường ép đuổi (người chơi tự điều khiển); thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.

![Sơ đồ](maps/x6_shark.png)

---

## 0. Công cụ và quy ước

Dùng chung với màn mẫu (`../lo-nham-thach-kich-ban.md`, mục 0): LDtk dựng bản đồ, Pixelorama vẽ tile, Krita vẽ nền parallax. 1 ô = 32px, khung hình 30×17 ô, các lớp `Collision` / `Tiles` / `Decor` / `Foreground` / `Entities`.

---

## 1. Ý tưởng tổng

Nhà máy tái chế nghiền mọi thứ thành khối kim loại. Cả màn là **cảm giác bị nghiền**: trần hạ xuống, rác rơi, tường ép đuổi theo. Người chơi phải tìm hốc trú và chạy theo nhịp máy.

- **Area 1 – Dây chuyền ép:** vàng-đen cảnh báo, đèn quay đỏ. Dạy trần ép toàn phòng, hốc trú, rác rơi, hai trần lệch nhịp.
- **Area 2 – Bãi rác và hầm:** núi rác, ánh lửa lò đốt. Ride Armor phá tường rác, rồi bị tường ép đuổi dọc đường hầm.
- **Điểm nhấn trải nghiệm:** trốn trần ép trong hốc → xuống hố rác → đọc hai trần lệch nhịp → mini-boss máy ép → cưỡi Ride Armor phá tường rác → chạy trước tường ép → lò đốt → boss có rác rơi
- **Đường cong độ khó:** 2 → 3 → 4 → 5 → (mini-boss) → 5 → 7 → 6 → 2 → boss (thang 10).
- **Thời lượng mục tiêu:** khoảng 6–7 phút lần đầu, khoảng 3 phút khi đã quen.

Các mẫu thiết kế tham khảo (không chép bản đồ gốc):

- **X6, màn Metal Shark Player:** trần máy ép thủy lực với hốc trú, Ride Armor phá tường rác giấu capsule Shadow Foot.
- **X5, màn Burn Dinorex / màn mẫu Lò Nham Thạch:** máy ép theo nhịp (ở đây mở rộng thành cả trần).
- **X8 16-bit demake:** đoạn tự cuộn làm lại thành đoạn người chơi tự điều khiển; ở đây là tường đuổi.
- **X Corrupted:** dùng bẫy môi trường để hạ địch (trần ép nghiền Brute).

---

## 2. Kịch bản từng phòng

Tọa độ tính theo ô, gốc (0,0) ở góc trên trái thế giới, y tăng xuống dưới.

### R1 – Cổng nhà máy (x 0–44, y 50–64) · độ khó 2
- **Mục đích:** mở đầu trong nhà máy tái chế. Giới thiệu băng chuyền rác và không khí ngột ngạt.
- **Địa hình:** cổng 44 ô, trần ở y 52, sàn ở y 60. Băng chuyền đẩy sang phải 80px/giây.
- **Địch:** 1 Drone dạng ruồi máy, 1 Sniper cuối phòng.
- **Trang trí:** núi rác ở nền, khối kim loại nén, đèn cảnh báo vàng-đen.

### R2 – Trần ép 1 (x 44–108, y 50–64) · độ khó 3
- **Mục đích:** giới thiệu **trần ép toàn phòng**, khác với máy ép đơn lẻ.
- **Địa hình:**
  - Phòng 64 ô, sàn ở y 60. Có **4 hốc trú** sâu 2.5 ô, rộng 4 ô, cách nhau 12–16 ô.
- **Cơ chế – trần ép:**
  - Cả trần (sọc vàng-đen) hạ xuống chỉ còn cách sàn 1.5 ô, rồi nâng lên. Chu kỳ 5 giây: đứng yên 3.2 giây, hạ 0.8 giây, giữ 0.5 giây, nâng 0.5 giây.
  - Đứng trên sàn lúc trần hạ là mất mạng. Nằm trong hốc thì an toàn.
  - Đèn đỏ quay và còi hú 1 giây trước khi hạ.
- **Địch:**
  - 1 Brute giữa phòng: trần ép hạ cũng nghiền chết nó, nên có thể dụ nó.
  - 1 Sniper nằm sẵn trong hốc thứ ba: phải hạ nó mới vào hốc đó được.
- **Vật phẩm:** Reploid #1 trong hốc thứ hai.

### R3 – Hố phế liệu (x 108–132, y 50–90) · độ khó 4
- **Mục đích:** đoạn dọc đi xuống, đổi nhịp sau phòng ép.
- **Địa hình:** hố rộng 20 ô, sâu 34 ô (từ y 60 xuống y 88). 4 kệ thép xếp zigzag.
- **Bẫy:**
  - **Khối rác nén** rơi từ miệng hố mỗi 2.5 giây, theo một trong 2 làn cố định. Bóng đổ trên kệ báo trước.
  - **Nam châm cẩu** chạy ngang giữa hố. Đứng lên được, nhưng nó hút giáp kim loại: đứng quá 2 giây thì bị kéo lên trên.
- **Địch:** 1 Drone ruồi.

### R4 – Trần ép 2 (x 132–196, y 78–92) · độ khó 5
- **Mục đích:** hai trần ép **lệch nhịp**, nên phải đọc hai đồng hồ cùng lúc.
- **Địa hình:**
  - Phòng 64 ô, sàn ở y 88. Một cột thép giữa phòng chia làm hai trần.
  - Mỗi nửa có 2 hốc trú.
- **Cơ chế:**
  - Trần A (nửa trái) chu kỳ 5 giây, trần B (nửa phải) chu kỳ 3.5 giây.
  - Dưới trần B có băng chuyền chạy ngược (đẩy sang trái 90px/giây), làm chậm đường chạy giữa hai hốc.
- **Địch:**
  - 1 Drone ruồi (không bị trần ép).
  - 1 Sniper cuối phòng, đứng trên đoạn an toàn.
- **Vật phẩm:** Reploid #2 trong hốc đầu tiên.

### Mini-boss – Máy ép chủ (x 196–226, y 74–90) · độ khó 5
- **Đấu trường 26 ô**, hai vách đá tường được.
- **Máy ép chủ** là khối ép khổng lồ gắn trên trần, có hai tay kẹp.
- **Đòn đánh:**
  - Đập xuống một nửa sân (trái hoặc phải), báo trước bằng bóng đổ 0.8 giây.
  - Hai tay kẹp quét ngang sát sàn: nhảy qua.
  - Mỗi lần mất 1/3 máu, **cả trần hạ xuống 2 ô**: đấu trường thấp dần, khó đá tường.
- **Điểm yếu:** lõi thủy lực lộ ra ở mặt dưới sau mỗi cú đập.
- **Phần thưởng:** mở bãi Ride Armor. Hạ không mất máu thì được thưởng Souls.

### R5 – Bãi rác Ride Armor (x 226–290, y 72–90) · độ khó 5
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** cưỡi Ride Armor đục xuyên **tường rác**.
- **Địa hình:**
  - Bãi rác 64 ô, sàn ở y 88. 2 bức tường rác nén cao 8 ô chắn hết đường.
  - X đi bộ không phá được tường rác: phải dùng Ride Armor (4 cú đấm mỗi tường).
  - Giữa hai tường có 2 máy ép nhỏ dập theo nhịp (chờ 1.5 giây, dập 0.3 giây), Ride Armor chịu được 2 cú.
- **Địch:** 1 Brute giữa bãi.
- **Vật phẩm:** Reploid #3 đầu bãi.
- **Lối phụ (Capsule Shadow Foot):**
  - Đấm vỡ **tường rác thứ hai** từ phía dưới thì lộ ra một khoang nhỏ phía trên, kẹp giữa 2 máy ép (x ≈ 268–280, y ≈ 74–76).
  - Nhảy Ride Armor lên đúng lúc hai máy ép cùng nâng lên. Capsule ở trong khoang.
- **Lối phụ (Sub-Tank):** kệ thép cuối bãi (x ≈ 282, y ≈ 78). Đứng trên Ride Armor nhảy lên rồi bật ra khỏi xe để với tới.

### R6 – Hầm tường ép đuổi (x 290–370, y 76–90) · độ khó 7
- **Mục đích:** cao trào của màn. Bị **tường ép đuổi** dọc một đường hầm dài 80 ô.
- **Cơ chế – tường ép đuổi:**
  - Khi người chơi bước vào, bức tường ép phía trái bắt đầu tiến sang phải 90px/giây, tăng lên 120px/giây ở nửa sau.
  - Bị kẹp giữa tường ép và vật cản là mất mạng.
  - Khác đoạn tự cuộn của X6 gốc: camera vẫn bám người chơi, người chơi được chạy nhanh hơn tường để tạo khoảng cách.
- **Vật cản:**
  - Trần thấp (khe 4 ô): phải lướt.
  - Khối thép thấp: nhảy qua.
  - Đoạn băng chuyền chạy ngược có gai ở giữa.
  - Khối rác cuối hầm, phải bắn 3 phát mới vỡ.
- **Địch:** 2 Drone ruồi, chỉ gây vướng: bắn hạ thì mất thời gian, lướt qua thì mất máu.
- **Lối phụ (Heart Tank):**
  - Một gờ cao trên trần ở x ≈ 316 (y ≈ 79), ngay sau khe trần thấp đầu tiên.
  - Lên lấy mất khoảng 1.5 giây: chỉ kịp nếu đã chạy nhanh từ đầu hầm. Giáp Blade lướt trên không giúp tiết kiệm thời gian.

### R7 – Lò đốt (x 370–420, y 78–92) · độ khó 6
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** kết hợp: lửa theo nhịp sau đoạn bị đuổi, cho người chơi thở chậm lại.
- **Địa hình:** hành lang lò đốt 50 ô, sàn ở y 88.
- **Bẫy:** 3 lưới sàn phụt lửa cao 3 ô, phụt 1 giây mỗi 2.5 giây, lệch pha nhau.
- **Địch:** 1 Drone ruồi, 1 Sniper cuối hành lang.

### R8 – Phòng điều khiển (x 420–450, y 78–92) · độ khó 2
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss.

### BOSS – Metal Shark Player (x 450–482, y 74–90)
- **Đấu trường 28 ô**, hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (bơi trong rác, Metal Anchor, cắn).
- **Pha 2** (dưới 50% HP):
  - **Khối rác nén rơi từ trần** mỗi 4 giây (bóng đổ báo trước). Khối rơi xong nằm lại 6 giây làm vật cản, có thể đứng lên.
  - Metal Shark bơi dưới sàn và trồi lên dưới chân người chơi.
- Điểm yếu giữ nguyên theo dữ liệu game.

---

## 3. Bảng vật phẩm và kẻ địch

| Loại | Số lượng | Vị trí |
|---|---|---|
| Sniper | 4 | R1, R2, R4, R7 |
| Drone | 6 | R1, R3, R4, R6 ×2, R7 |
| Brute | 2 | R2, R5 |
| Mini-boss | 1 | MID |
| Reploid cứu | 4 | R2, R4, R5, R8 |
| Heart Tank | 1 | R6 |
| Sub-Tank | 1 | R5 |
| Capsule Shadow Foot | 1 | R5 |
| Ride Armor / Chaser | 1 | R5 |
| Checkpoint | 2 | R5, R7 |

Tổng 12 kẻ địch thường (bản cũ: 20 con xếp đều), đặt có chủ đích theo mục đích từng phòng.

---

## 4. Những gì engine cần bổ sung

1. Trần ép toàn phòng: hạ/nâng theo lịch, giết mọi thứ không nằm trong hốc.
2. Khối rác rơi theo làn và lịch; nam châm cẩu kéo người chơi lên.
3. Tường rác chỉ Ride Armor phá được.
4. Tường ép đuổi: chạy theo người chơi với tốc độ tăng dần, kẹp là chết.
5. Lưới sàn phụt lửa theo nhịp.
6. Mini-boss Máy ép chủ: trần đấu trường hạ dần theo máu.

## 5. Danh sách hình cần vẽ

- **Tileset "Dây chuyền" (Area 1):** 47 ô viền thép sọc vàng-đen, trần ép, hốc trú, băng chuyền.
- **Tileset "Bãi rác" (Area 2):** 47 ô viền rác nén, tường rác (3 trạng thái vỡ), lưới lò đốt.
- **Vật thể:** khối rác nén, nam châm cẩu, tường ép đuổi (4 khung), lửa lò (4 khung), đèn quay.
- **Nền:** Area 1: dây chuyền và băng tải xa (2 lớp parallax). Area 2: núi rác và lò đốt (2 lớp).

**Hướng phối hợp:** như màn mẫu — dựng bằng khối màu tạm theo sơ đồ để chơi thử, chốt cảm giác rồi mới thay tile thật.
