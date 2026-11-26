# Màn: KHÔNG GIAN ÁC MỘNG (Nightmare Space — Boss Nightmare Zero)

Bản thiết kế để duyệt trước khi dựng. Sơ đồ: `maps/x6_f1_nzero.png`.
Màn này thay cho `x6_f1_nzero` hiện tại. Boss Nightmare Zero, màn tối nhiễu, đèn quét ảo ảnh, bệ Cyber nhấp nháy và vùng đảo trọng lực vẫn giữ. Không có capsule/Heart Tank/Sub-Tank (theo dữ liệu game); thêm 4 Reploid, 1 mini-boss và trạm nạp lớn.

![Sơ đồ](maps/x6_f1_nzero.png)

---

## 0. Công cụ và quy ước

Dùng chung với màn mẫu (`../lo-nham-thach-kich-ban.md`, mục 0): LDtk dựng bản đồ, Pixelorama vẽ tile, Krita vẽ nền parallax. 1 ô = 32px, khung hình 30×17 ô, các lớp `Collision` / `Tiles` / `Decor` / `Foreground` / `Entities`.

---

## 1. Ý tưởng tổng

Không gian ác mộng tạo từ ký ức của Zero. Cả màn đánh vào **sự tin tưởng vào mắt nhìn**: tối nhiễu, bệ ảo ảnh, bản sao bắt chước, trọng lực lật ngược.

- **Area 1 – Hành lang ác mộng:** đen tím nhiễu, đèn quét trắng. Tầm nhìn hẹp, bệ thật/ảo, bệ nhấp nháy.
- **Area 2 – Không gian lộn ngược:** đỏ thẫm. Đệm đảo chiều trên sàn gai, giếng tự đảo trọng lực.
- **Điểm nhấn trải nghiệm:** đi trong nhiễu tối → theo vệt đèn tìm bệ thật → đếm nhịp bệ trong bóng tối → đánh bản sao chính mình → đi zigzag sàn-trần → leo giếng hai chiều → Nightmare Zero
- **Đường cong độ khó:** 3 → 5 → 5 → (mini-boss) → 6 → 8 → 2 → boss (thang 10).
- **Thời lượng mục tiêu:** khoảng 5–6 phút lần đầu, khoảng 2.5 phút khi đã quen.

Các mẫu thiết kế tham khảo (không chép bản đồ gốc):

- **X6, Nightmare Space / màn Nightmare Zero:** tối nhiễu, đèn quét ảo ảnh, bệ nhấp nháy, đảo trọng lực.
- **X6, màn Gate Lab:** đổi luật vật lý liên tục.
- **X8, màn Dark Mantis:** tầm nhìn bị giới hạn.
- **X Corrupted:** bệ thật/ảo chỉ phân biệt được bằng một cơ chế khác (đèn quét).

---

## 2. Kịch bản từng phòng

Tọa độ tính theo ô, gốc (0,0) ở góc trên trái thế giới, y tăng xuống dưới.

### R1 – Hành lang nhiễu (x 0–44, y 44–58) · độ khó 3
- **Mục đích:** vào không gian ác mộng nơi Nightmare Zero chờ. Màn hình nhiễu, **chỉ thấy rõ trong 8 ô quanh X**.
- **Địa hình:** hành lang 44 ô, trần ở y 42, sàn ở y 50.
- **Địch:** 1 Drone, 1 Sniper (chỉ thấy đèn mắt khi ở xa).
- **Vật phẩm:** Reploid #1 ở đầu hành lang.
- **Ghi chú:** đánh bại Nightmare Zero thì Zero thật được giải cứu và mở cho các tầng Gate Lab (theo dữ liệu game). Không có capsule/Heart Tank/Sub-Tank.

### R2 – Đèn quét ảo ảnh (x 44–108, y 44–62) · độ khó 5
- **Mục đích:** giới thiệu **đèn quét ảo ảnh**: thứ thấy được chưa chắc là thật.
- **Địa hình:** vực rộng 52 ô, hai mép đá ở hai đầu.
- **Cơ chế:**
  - Có 2 loại bệ. **Bệ ảo ảnh** hiện rõ trong bóng tối nhưng **biến mất khi đèn quét chiếu vào**. **Bệ thật** vô hình trong bóng tối và **chỉ hiện khi được đèn chiếu**.
  - Đèn quét qua lại trên vực, 70px/giây. Người chơi đi theo vệt đèn để thấy và đứng trên bệ thật.
  - Đứng trên bệ ảo ảnh lúc đèn quét tới là rơi.
- **Địch:** 1 Drone.

### R3 – Bệ nhấp nháy (x 108–164, y 44–62) · độ khó 5
- **Mục đích:** bệ 2 pha (như Zero Space 2) trong bóng tối nhiễu.
- **Địa hình:** vực 44 ô, 5 bệ xen kẽ pha A/B, nhịp 2 giây.
- **Cơ chế:** vì tầm nhìn chỉ 8 ô, người chơi không thấy hết chuỗi bệ. Âm thanh "tách" khi đổi pha giúp đếm nhịp.
- **Địch:** 1 Drone.
- **Vật phẩm:** Reploid #2 ở mép bên kia.

### Mini-boss – Bóng ma X (x 164–194, y 40–56) · độ khó 6
- **Đấu trường 26 ô**, kín, hai vách đá tường được.
- **Bóng ma X** là bản sao Nightmare của X, **lặp lại động tác của người chơi** sau 1 giây.
- **Đòn đánh:** bắn, lướt, nhảy, đá tường giống hệt những gì người chơi vừa làm 1 giây trước.
- **Điểm yếu:** đứng yên thì nó cũng đứng yên, bắn vào nó lúc đó. Nạp đạn đầy thì nó cũng nạp: phải bắn trước.
- **Phần thưởng:** mở vùng đảo trọng lực. Hạ không mất máu thì được thưởng Souls.

### R4 – Vùng đảo trọng lực (x 194–254, y 40–62) · độ khó 6
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** đảo trọng lực bằng **đệm đảo chiều** (khác công tắc ở Zero Space 3).
- **Địa hình:** khoảng trống 44 ô, sàn là gai, trần liền.
- **Cơ chế:** dẫm lên **đệm đảo chiều** thì trọng lực lật ngược ngay lập tức. 4 đệm xen kẽ trên sàn và trên trần, người chơi đi zigzag giữa sàn và trần.
- **Địch:** 1 Brute đứng lộn ngược trên trần, 1 Sniper cuối phòng.
- **Vật phẩm:** Reploid #3 trên sàn gần cuối (khúc không có gai).

### R5 – Giếng hai chiều (x 254–278, y 10–56) · độ khó 8
- **Mục đích:** cao trào của màn. Leo giếng trong khi **trọng lực tự đảo mỗi 4 giây** và nửa giữa giếng bị nhiễu tối.
- **Địa hình:** giếng rộng 20 ô, cao 42 ô (từ y 50 lên y 13). 5 kệ.
- **Cơ chế:**
  - Lúc trọng lực ngược, người chơi "rơi" lên. Đó là lúc leo nhanh nhất, nhưng phải dừng lại kịp trên mặt dưới của kệ.
  - Lúc trọng lực thường, bám vách hoặc đứng trên mặt trên của kệ để không rơi mất độ cao.
  - Nửa giữa giếng tối: chỉ thấy 8 ô quanh X.
- **Địch:** 2 Drone, miễn đảo trọng lực.

### R6 – Trạm cuối (x 278–308, y 7–21) · độ khó 2
- **Checkpoint 2** ở đầu phòng.
- Phòng nghỉ trước boss: Reploid #4, **nạp năng lượng lớn**, cửa boss.

### BOSS – Nightmare Zero (x 308–340, y 3–19)
- **Đấu trường 28 ô**, kín, hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (chém kiếm, Shippuuga, Genmu Zero).
- **Pha 2** (dưới 50% HP):
  - **Nhiễu tối toàn sân**, chỉ thấy 8 ô quanh X. Nightmare Zero lướt vào từ ngoài vùng sáng; đôi mắt đỏ của nó hiện trước 0.5 giây.
- Điểm yếu giữ nguyên theo dữ liệu game.

---

## 3. Bảng vật phẩm và kẻ địch

| Loại | Số lượng | Vị trí |
|---|---|---|
| Sniper | 2 | R1, R4 |
| Drone | 5 | R1, R2, R3, R5 ×2 |
| Brute | 1 | R4 |
| Mini-boss | 1 | MID |
| Reploid cứu | 4 | R1, R3, R4, R6 |
| Checkpoint | 2 | R4, R6 |

Tổng 8 kẻ địch thường (bản cũ: 20 con xếp đều), đặt có chủ đích theo mục đích từng phòng.

---

## 4. Những gì engine cần bổ sung

1. Vùng tối nhiễu (tầm nhìn bán kính 8 ô quanh X).
2. Bệ ảo ảnh và bệ thật phản ứng ngược nhau với vệt đèn quét.
3. Bệ 2 pha có âm báo đổi pha.
4. Đệm đảo chiều (dẫm lên thì lật trọng lực); vùng trọng lực tự đảo theo nhịp.
5. Mini-boss Bóng ma X lặp lại đầu vào của người chơi với độ trễ 1 giây.

## 5. Danh sách hình cần vẽ

- **Tileset "Ác mộng":** 47 ô viền đen tím nhiễu, bệ thật (viền sáng) và bệ ảo ảnh (đặc), đệm đảo chiều.
- **Vật thể:** đèn quét (vệt sáng 3 khung), bóng ma X (bảng màu tối của sprite X), hiệu ứng nhiễu (lớp phủ).
- **Nền:** mảnh ký ức trôi, hình bóng Zero mờ (2 lớp parallax).

**Hướng phối hợp:** như màn mẫu — dựng bằng khối màu tạm theo sơ đồ để chơi thử, chốt cảm giác rồi mới thay tile thật.
