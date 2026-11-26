# Màn: ZERO SPACE FINAL (Zero Space Final — Boss Final Sigma W)

Bản thiết kế để duyệt trước khi dựng. Sơ đồ: `maps/x5_f4_sigma.png`.
Màn này thay cho `x5_f4_sigma` hiện tại. Boss Final Sigma W, nền không gian vỡ vụn, bệ di chuyển lõi virus, vùng đảo trọng lực và cổng quyết chiến vẫn giữ. Không có capsule/Heart Tank/Sub-Tank (theo dữ liệu game); thêm 4 Reploid, 1 mini-boss và trạm nạp lớn.

![Sơ đồ](maps/x5_f4_sigma.png)

---

## 0. Công cụ và quy ước

Dùng chung với màn mẫu (`../lo-nham-thach-kich-ban.md`, mục 0): LDtk dựng bản đồ, Pixelorama vẽ tile, Krita vẽ nền parallax. 1 ô = 32px, khung hình 30×17 ô, các lớp `Collision` / `Tiles` / `Decor` / `Foreground` / `Entities`.

---

## 1. Ý tưởng tổng

Màn cuối Act I, **ôn tập mọi cơ chế** người chơi đã học: nền vỡ, bệ di động, gió, nước, laser, Time Zone, sàn điện, đảo trọng lực. Mỗi cơ chế xuất hiện ngắn, ghép nhau dày hơn.

- **Area 1 – Rìa lõi virus:** hồng tím, mảnh vỡ trôi. Nền vỡ, bệ lõi trong gió, hành lang ký ức.
- **Area 2 – Lõi Sigma:** đỏ đậm, tia sáng. Đảo trọng lực có Boost, trục leo quanh lõi bắn tia.
- **Điểm nhấn trải nghiệm:** chạy trên nền vỡ → bay bệ lõi trong gió → hành lang ký ức Act I → 3 bóng ma Sigma → đảo trọng lực qua vực → leo quanh lõi virus → boss sàn sụp
- **Đường cong độ khó:** 4 → 5 → 6 → (mini-boss) → 6 → 8 → 2 → boss (thang 10).
- **Thời lượng mục tiêu:** khoảng 6–7 phút lần đầu, khoảng 3 phút khi đã quen.

Các mẫu thiết kế tham khảo (không chép bản đồ gốc):

- **X5, Zero Space Final:** hợp nhất cơ chế Act I, trọng lực biến thiên, bệ di chuyển, cổng quyết chiến Sigma.
- **X6, màn Gate Lab cuối:** ôn lại các màn trước bằng đoạn ngắn.
- **X8, màn Jakob Elevator / Sigma Palace:** leo quanh trục trung tâm.
- **X Corrupted:** pháo đài cuối ghép cơ chế của nhiều màn.

---

## 2. Kịch bản từng phòng

Tọa độ tính theo ô, gốc (0,0) ở góc trên trái thế giới, y tăng xuống dưới.

### R1 – Nền vỡ vụn (x 0–50, y 44–60) · độ khó 4
- **Mục đích:** bước vào lõi virus Sigma: **nền không gian vỡ vụn** dưới chân.
- **Địa hình:** 50 ô, mặt nền ở y 52. 2 đoạn nền vỡ (10 và 12 ô) sụp 0.4 giây sau khi đứng, rơi xuống vực.
- **Địch:** 1 Drone, 1 Sniper.
- **Ghi chú:** màn cuối Act I, ôn lại mọi cơ chế của Act I. Không có capsule/Heart Tank/Sub-Tank (theo dữ liệu game); hoàn thành màn mở khóa Act II.

### R2 – Bệ lõi virus (x 50–114, y 40–62) · độ khó 5
- **Mục đích:** ôn **bệ di động** và **gió giật** của màn Không quân.
- **Địa hình:** vực 52 ô, 4 bệ lõi virus bay qua lại.
- **Cơ chế:** gió giật 2 giây mỗi 5 giây, đẩy ngược. Bệ bay theo đường chéo, không phải ngang.
- **Địch:** 2 Drone.
- **Vật phẩm:** Reploid #1 trên bệ thứ ba.

### R3 – Hành lang ký ức (x 114–184, y 44–58) · độ khó 6
- **Mục đích:** hành lang **ký ức** ghép các đoạn ngắn của Act I.
- **Địa hình và cơ chế (theo thứ tự):**
  - Vùng nước (trọng lực ×0.32, như Căn cứ đáy biển).
  - Hàng rào laser 2 giây bật / 1 giây tắt (như Phòng thí nghiệm Laser).
  - Vùng Time Zone có búa lắc (như Đài thiên văn).
  - Sàn điện 1.5 giây / 1.5 giây (như Nhà máy điện).
- **Địch:** 1 Brute, 1 Sniper.
- **Vật phẩm:** Reploid #2 sau vùng Time Zone.

### Mini-boss – Phân thân Sigma (x 184–214, y 40–56) · độ khó 6
- **Đấu trường 26 ô**, kín, hai vách đá tường được.
- **Phân thân Sigma** là 3 bóng ma của Sigma xuất hiện lần lượt, mỗi bóng dùng một đòn.
- **Đòn đánh:**
  - Bóng 1: chém kiếm ngang sân.
  - Bóng 2: bắn tia từ trán.
  - Bóng 3: nhảy dội sàn tạo sóng xung kích.
- **Điểm yếu:** mỗi bóng chỉ nhận đòn khi đang ra đòn. Hạ đủ 3 bóng thì xong.
- **Phần thưởng:** mở vùng đảo trọng lực. Hạ không mất máu thì được thưởng Souls.

### R4 – Vùng đảo trọng lực (x 214–278, y 40–62) · độ khó 6
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** ôn **đảo trọng lực** của Zero Space 3, kết hợp tấm Boost.
- **Địa hình:** vực 48 ô. Trần liền phía trên, một cầu nhỏ giữa vực.
- **Cơ chế:**
  - Hai vùng đảo trọng lực cố định (không cần công tắc): vào vùng là rơi lên trần.
  - Giữa hai vùng là cầu nhỏ có tấm Boost: phải ra khỏi vùng đúng chỗ để rơi xuống cầu, rồi lướt Boost vào vùng sau.
  - Trần có một mảng gai.
- **Địch:** 1 Drone, 1 Sniper.
- **Vật phẩm:** Reploid #3 trên cầu giữa.

### R5 – Trục lõi virus (x 278–304, y 14–60) · độ khó 8
- **Mục đích:** cao trào của màn. Leo trục dọc trên các bệ chạy vòng quanh **lõi virus** đang bắn.
- **Địa hình:** trục rộng 22 ô, cao 42 ô (từ y 54 lên y 13). 5 bệ di động.
- **Cơ chế:**
  - Các bệ chạy vòng tròn quanh lõi virus ở giữa trục (bán kính 7 ô, mỗi vòng 8 giây).
  - **Lõi bắn tia quay** 1 vòng mỗi 4 giây. Tia dài tới vách, chỉ né được bằng cách nhảy qua đúng lúc.
  - Hai vách đá tường được, nhưng vách có vệt dữ liệu nhiễu ở nửa trên (đẩy ra 1 ô).
- **Địch:** 2 Drone.
- **Giáp hỗ trợ:** Falcon bay; Ultimate lướt Nova Strike xuyên tia.

### R6 – Cổng quyết chiến (x 304–334, y 11–25) · độ khó 2
- **Checkpoint 2** ở đầu phòng.
- Phòng nghỉ trước trận cuối Act I: Reploid #4, **nạp năng lượng lớn**, cổng Sigma.

### BOSS – Final Sigma W (x 334–368, y 7–25)
- **Đấu trường 34 ô**, không vách.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (Final Sigma W khổng lồ, tay, mắt, tia).
- **Pha 2** (dưới 50% HP):
  - **Sàn sụp từng mảng**: 3 mảng (rộng 6 ô) lần lượt sụp 4 giây rồi dựng lại. Mảng sắp sụp nứt đỏ 1 giây trước.
  - Sigma nhắm đòn vào mảng sàn an toàn còn lại.
- Điểm yếu giữ nguyên theo dữ liệu game.

---

## 3. Bảng vật phẩm và kẻ địch

| Loại | Số lượng | Vị trí |
|---|---|---|
| Sniper | 3 | R1, R3, R4 |
| Drone | 6 | R1, R2 ×2, R4, R5 ×2 |
| Brute | 1 | R3 |
| Mini-boss | 1 | MID |
| Reploid cứu | 4 | R2, R3, R4, R6 |
| Checkpoint | 2 | R4, R6 |

Tổng 10 kẻ địch thường (bản cũ: 20 con xếp đều), đặt có chủ đích theo mục đích từng phòng.

---

## 4. Những gì engine cần bổ sung

1. Dùng lại toàn bộ đối tượng của Act I (nền vỡ, bệ di động, gió, nước, laser, Time Zone, sàn điện, đảo trọng lực).
2. Bệ chạy vòng quanh một tâm trong trục dọc; lõi bắn tia quay.
3. Mini-boss Phân thân Sigma (3 bóng lần lượt).
4. Sàn boss sụp từng mảng theo lịch.

## 5. Danh sách hình cần vẽ

- **Tileset "Lõi virus":** 47 ô viền hồng tím có mạch, nền vỡ (3 khung).
- **Vật thể:** bệ lõi virus, lõi bắn tia (4 khung), bóng ma Sigma, mảng sàn sụp.
- **Nền:** khối mảnh vỡ trôi và hình bóng Sigma mờ (2 lớp parallax).

**Hướng phối hợp:** như màn mẫu — dựng bằng khối màu tạm theo sơ đồ để chơi thử, chốt cảm giác rồi mới thay tile thật.
