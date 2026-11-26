# Màn: KHU DUNG NHAM (Magma Area — Boss Blaze Heatnix)

Bản thiết kế để duyệt trước khi dựng. Sơ đồ: `maps/x6_heatnix.png`.
Màn này thay cho `x6_heatnix` hiện tại. Boss, capsule Shadow Arm, 3 cỗ máy vòng lửa Nightmare Donut, bệ phản lực, trục leo có dung nham dâng và khối sắt nứt vẫn giữ; thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.

![Sơ đồ](maps/x6_heatnix.png)

---

## 0. Công cụ và quy ước

Dùng chung với màn mẫu (`../lo-nham-thach-kich-ban.md`, mục 0): LDtk dựng bản đồ, Pixelorama vẽ tile, Krita vẽ nền parallax. 1 ô = 32px, khung hình 30×17 ô, các lớp `Collision` / `Tiles` / `Decor` / `Foreground` / `Entities`.

---

## 1. Ý tưởng tổng

Núi lửa tự nhiên bị virus Nightmare chiếm, khác hẳn nhà máy của màn mẫu Lò Nham Thạch. Màn này xoay quanh **những thứ trôi trên dung nham** (bệ phản lực, bè đá) và **vòng lửa Donut** chặn đường.

- **Area 1 – Sườn núi và hồ (ngoài trời):** đá bazan đen, trời đỏ. Dạy cột phun, bệ phản lực bay ngang, Donut, hang nhỏ giọt.
- **Area 2 – Lòng núi:** đỏ rực, khói. Bè đá trôi theo dòng, trục leo có dung nham dâng từng bậc, vành miệng phun.
- **Điểm nhấn trải nghiệm:** né cột phun → bay qua hồ trên bệ phản lực → hang nhỏ giọt → mini-boss vòng lửa co giãn → nhảy bè đá → leo trục khi nham dâng theo bậc → phá Donut chặn cửa → boss nửa sân ngập nham
- **Đường cong độ khó:** 2 → 3 → 4 → (mini-boss) → 5 → 7 → 6 → 2 → boss (thang 10).
- **Thời lượng mục tiêu:** khoảng 6–7 phút lần đầu, khoảng 3 phút khi đã quen.

Các mẫu thiết kế tham khảo (không chép bản đồ gốc):

- **X6, màn Blaze Heatnix:** Nightmare Donut, bệ phản lực Thruster, trục leo dung nham, khối sắt phá bằng Charge Saber giấu capsule Shadow Arm.
- **X4, màn Magma Dragoon:** dung nham dâng buộc leo nhanh (ở đây đổi thành dâng theo bậc để khác màn mẫu).
- **X2, màn Flame Stag:** trục dọc lòng núi lửa.
- **X Corrupted:** chướng ngại vừa là bẫy vừa là mục tiêu (Donut chặn cửa phải phá).

---

## 2. Kịch bản từng phòng

Tọa độ tính theo ô, gốc (0,0) ở góc trên trái thế giới, y tăng xuống dưới.

### R1 – Miệng núi (x 0–44, y 56–72) · độ khó 2
- **Mục đích:** giới thiệu **cột dung nham phun** từ hố: bật 1.5 giây, tắt 3 giây.
- **Địa hình:** sườn núi 44 ô, mặt đất ở y 68. 2 hố dung nham rộng 4 ô. Hố đầu có cột phun cao 8 ô.
- **Địch:** 1 Drone, 1 Sniper.
- **Trang trí:** đá bazan đen, khói, tro bay, trời đỏ.
- **Khác màn mẫu Lò Nham Thạch:** màn này là núi lửa tự nhiên, không phải nhà máy; cơ chế chính là bệ phản lực và vòng lửa Donut.

### R2 – Hồ dung nham (x 44–114, y 56–74) · độ khó 3
- **Mục đích:** vượt hồ dung nham bằng **bệ phản lực**.
- **Địa hình:** hồ rộng 58 ô, chạm dung nham là mất mạng. Một trụ đá giữa hồ.
- **Cơ chế – bệ phản lực:**
  - Đứng lên thì bệ bay ngang sang phải 110px/giây trong 4 giây, rồi hết nhiên liệu và chìm dần.
  - Phải nhảy sang trụ đá rồi bệ thứ hai trước khi bệ dưới chân chìm.
- **Bẫy – Donut #1:** cỗ máy vòng lửa gắn trên trụ đá. 3 quả cầu lửa quay quanh trụ (bán kính 3 ô, 1 vòng mỗi 2 giây). Bắn hạ được bằng 8 phát hoặc 2 phát nạp đầy; hạ được thì trụ an toàn.
- **Địch:** 2 Drone.
- **Vật phẩm:** Reploid #1 ở bờ bên kia.

### R3 – Hang đá nóng (x 114–174, y 56–72) · độ khó 4
- **Mục đích:** đoạn trong hang, đổi nhịp. Nguy hiểm từ trên đầu.
- **Địa hình:** hang 60 ô, trần ở y 58, sàn ở y 68.
- **Bẫy:** 3 điểm nhỏ giọt dung nham từ trần, mỗi 2 giây một giọt. Chỗ giọt rơi xuống cháy 1 giây.
- **Địch:** 1 Brute giữa hang, 1 Sniper cuối hang.
- **Lối phụ (Sub-Tank):** gờ đá cao cuối hang (x ≈ 162, y ≈ 62). Đá tường vách hang lên, nhưng một điểm nhỏ giọt nằm ngay trên chỗ đá tường: canh nhịp.

### Mini-boss – Donut Nightmare lớn (x 174–204, y 54–72) · độ khó 5
- **Đấu trường 26 ô**, hai vách đá tường được.
- **Donut Nightmare lớn** lơ lửng giữa phòng, 6 quả cầu lửa quay quanh.
- **Đòn đánh:**
  - Vòng lửa **co lại và giãn ra** (bán kính 3 ↔ 9 ô). Lúc giãn hết cỡ thì chạm vách: phải lọt vào giữa hai quả cầu.
  - Bắn từng quả cầu lửa ra 4 hướng.
  - Lao sang một vách, kéo vòng lửa theo.
- **Điểm yếu:** lõi ở tâm. Bắn trúng được lúc vòng lửa giãn ra.
- **Phần thưởng:** mở đường xuống dòng dung nham. Hạ không mất máu thì được thưởng Souls.

### R4 – Dòng bè đá (x 204–260, y 56–74) · độ khó 5
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** đi trên **bè đá bazan** trôi theo dòng dung nham.
- **Địa hình:** dòng dung nham rộng 44 ô.
- **Cơ chế:** 3 bè đá trôi sang phải 60px/giây. Một cột phun ở giữa dòng (bật 1.5 giây, tắt 3 giây) chắn đường trôi: phải nhảy sang bè khác trước khi bè trôi vào cột.
- **Địch:** 1 Drone, 1 Sniper ở bờ bên kia.
- **Vật phẩm:** Reploid #2 trên bè thứ hai.

### R5 – Trục núi lửa (x 260–286, y 12–70) · độ khó 7
- **Mục đích:** cao trào của màn. Leo trục dọc lòng núi lửa trong khi dung nham **dâng từng bậc**.
- **Địa hình:**
  - Trục rộng 22 ô, cao 54 ô (từ y 68 lên y 13).
  - 5 bệ phản lực xếp zigzag. Đứng lên thì bệ bốc lên 4 ô rồi dừng; hai vách đá tường được.
- **Cơ chế – dung nham dâng theo bậc:**
  - Dung nham dâng **4 ô trong 1 giây, rồi đứng yên 5 giây**, lặp lại. Mặt đất rung trước mỗi lần dâng.
  - Khác giếng nham của màn mẫu (dâng liên tục): ở đây người chơi có nhịp nghỉ, nhưng bậc dâng nhanh nên đứng sai chỗ là chết ngay.
- **Bẫy – Donut #3:** cỗ máy vòng lửa chắn ngay lối ra trên đỉnh. Phải hạ nó (8 phát) trong lúc dung nham vẫn dâng.
- **Địch:** 1 Drone giữa trục.
- **Lối phụ (Heart Tank):** hốc ở vách phải giữa trục (x ≈ 282, y ≈ 38). Chỉ vào được lúc dung nham đang nghỉ.
- **Lối phụ (Capsule Shadow Arm):**
  - Góc trên trái có **khối sắt nứt** (x ≈ 264, y ≈ 19). Chỉ phá được bằng **Charge Saber** của Zero/Blade hoặc **đạn nạp đầy**.
  - Sau khối sắt là capsule Shadow Arm.
  - Dung nham dừng hẳn khi đã hạ Donut #3, nên quay lại phá khối sắt sau đó là an toàn.

### R6 – Đỉnh miệng phun (x 286–338, y 9–23) · độ khó 6
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** kết hợp: cột phun và luồng khí nóng.
- **Địa hình:** vành miệng núi lửa 52 ô, ngoài trời.
- **Cơ chế:**
  - 2 cột phun lệch pha (bật 1.5 giây, tắt 3 giây).
  - Luồng khí nóng bốc lên làm mỗi cú nhảy cao hơn 2 ô: dễ nhảy qua cột phun, nhưng cũng dễ bay vào tầm bắn của Drone.
- **Địch:** 1 Drone, 1 Sniper.
- **Vật phẩm:** Reploid #3 trước cửa phòng tạm.

### R7 – Hang nghỉ (x 338–368, y 9–23) · độ khó 2
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss.

### BOSS – Blaze Heatnix (x 368–400, y 5–23)
- **Đấu trường 28 ô**, hai vách đá tường được, hai góc có rãnh dung nham nhỏ.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (Magma Blade, lao lửa, chim lửa).
- **Pha 2** (dưới 50% HP):
  - **Dung nham dâng ngập một nửa sân** (trái hoặc phải), đổi bên mỗi 10 giây.
  - Người chơi bị dồn vào nửa còn lại; Heatnix bay qua phần dung nham để tấn công.
- Điểm yếu giữ nguyên theo dữ liệu game.

---

## 3. Bảng vật phẩm và kẻ địch

| Loại | Số lượng | Vị trí |
|---|---|---|
| Sniper | 4 | R1, R3, R4, R6 |
| Drone | 6 | R1, R2 ×2, R4, R5, R6 |
| Brute | 1 | R3 |
| Ống phun / tháp pháo | 2 | R2, R5 |
| Mini-boss | 1 | MID |
| Reploid cứu | 4 | R2, R4, R6, R7 |
| Heart Tank | 1 | R5 |
| Sub-Tank | 1 | R3 |
| Capsule Shadow Arm | 1 | R5 |
| Checkpoint | 2 | R4, R6 |

Tổng 11 kẻ địch thường (bản cũ: 20 con xếp đều), đặt có chủ đích theo mục đích từng phòng.

---

## 4. Những gì engine cần bổ sung

1. Cột dung nham phun theo nhịp.
2. Bệ phản lực bay ngang có hết nhiên liệu; bệ phản lực bốc lên từng nấc.
3. Bè đá trôi theo dòng.
4. Dung nham dâng theo bậc (dâng nhanh, nghỉ, lặp lại), dừng khi hạ mục tiêu.
5. Vòng lửa Donut: cầu lửa quay quanh tâm, phá được.
6. Khối sắt nứt chỉ phá được bằng Charge Saber hoặc đạn nạp đầy.
7. Luồng khí nóng tăng độ cao nhảy.
8. Mini-boss Donut lớn có vòng lửa co giãn.

## 5. Danh sách hình cần vẽ

- **Tileset "Sườn núi" (Area 1):** 47 ô viền bazan, hố dung nham, mạch nham trong đá.
- **Tileset "Lòng núi" (Area 2):** 47 ô viền đá đỏ, bè bazan, khối sắt nứt (2 trạng thái).
- **Vật thể:** cột phun (4 khung), bệ phản lực (lửa 3 khung), Donut (cầu lửa 4 khung), giọt nham, mặt dung nham động (4 khung).
- **Nền:** Area 1: núi lửa xa và trời đỏ (2 lớp parallax). Area 2: lòng núi và dòng nham xa (2 lớp).

**Hướng phối hợp:** như màn mẫu — dựng bằng khối màu tạm theo sơ đồ để chơi thử, chốt cảm giác rồi mới thay tile thật.
