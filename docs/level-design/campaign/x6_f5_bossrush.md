# Màn: PHÒNG THÍ NGHIỆM CUỐI (Final Lab — Boss 8 boss → Hell Sigma)

Bản thiết kế để duyệt trước khi dựng. Sơ đồ: `maps/x6_f5_bossrush.png`.
Màn này thay cho `x6_f5_bossrush` hiện tại. Boss Hell Sigma, hành lang bẫy gai và băng chuyền, trục rơi, bệ di chuyển, Trung tâm 8 cổng dịch chuyển boss rush và hồi máu giữa trận vẫn giữ. Không có capsule/Heart Tank/Sub-Tank (theo dữ liệu game); thêm 4 Reploid, 1 mini-boss.

![Sơ đồ](maps/x6_f5_bossrush.png)

---

## 0. Công cụ và quy ước

Dùng chung với màn mẫu (`../lo-nham-thach-kich-ban.md`, mục 0): LDtk dựng bản đồ, Pixelorama vẽ tile, Krita vẽ nền parallax. 1 ô = 32px, khung hình 30×17 ô, các lớp `Collision` / `Tiles` / `Decor` / `Foreground` / `Entities`.

---

## 1. Ý tưởng tổng

Màn cuối cùng của chiến dịch. Đoạn đầu là bẫy gai kiểu pháo đài cổ điển, giữa là **boss rush 8 cổng**, cuối là **cầu thang sụp** dẫn lên Hell Sigma.

- **Area 1 – Hầm bẫy:** đỏ đen, gai khắp nơi. Băng chuyền gai, trục rơi gai thò, bệ dưới trần gai.
- **Area 2 – Đỉnh tháp:** sảnh 8 cổng, trạm hồi máu, cầu thang sụp, đấu trường trên đỉnh.
- **Điểm nhấn trải nghiệm:** băng chuyền đẩy vào gai → rơi qua trục gai thò → bệ dưới trần gai → cảnh vệ ghép 8 boss → boss rush 8 cổng → hồi máu → chạy lên cầu thang sụp → Hell Sigma
- **Đường cong độ khó:** 5 → 6 → 6 → (mini-boss) → 7 → 2 → 8 → boss (thang 10).
- **Thời lượng mục tiêu:** khoảng 12–15 phút lần đầu (gồm boss rush), khoảng 7 phút khi đã quen.

Các mẫu thiết kế tham khảo (không chép bản đồ gốc):

- **X6, Final Lab:** hành lang bẫy gai, băng chuyền, trung tâm 8 cổng boss rush, hồi máu, Hell Sigma.
- **X (SNES) / X2, pháo đài Sigma:** sảnh dịch chuyển boss rush.
- **X8, màn Jakob Elevator:** đoạn đi lên trước trận cuối.
- **X Corrupted:** boss rush dùng lại cơ chế môi trường của từng màn.

---

## 2. Kịch bản từng phòng

Tọa độ tính theo ô, gốc (0,0) ở góc trên trái thế giới, y tăng xuống dưới.

### R1 – Hành lang bẫy gai (x 0–64, y 40–54) · độ khó 5
- **Mục đích:** màn cuối cùng. Mở đầu bằng **băng chuyền đẩy vào gai**, có trần gai thấp ở chỗ phải nhảy.
- **Địa hình:** hành lang 64 ô, 2 băng chuyền xuôi chiều (110px/giây), mỗi băng chuyền kết thúc bằng một hố gai.
- **Cơ chế:** băng chuyền làm cú nhảy dài hơn. Ở hố gai đầu có trần gai ngay trên: nhảy hết lực là trúng.
- **Địch:** 1 Drone, 1 Sniper.
- **Vật phẩm:** Reploid #1 ở đầu hành lang.
- **Ghi chú:** dữ liệu game khuyên dùng Ultimate Armor hoặc Black Zero. Không có capsule/Heart Tank/Sub-Tank.

### R2 – Trục rơi bẫy gai (x 64–88, y 40–86) · độ khó 6
- **Mục đích:** đi xuống trục có **gai thò ra từ vách** theo nhịp.
- **Địa hình:** trục rộng 20 ô, sâu 36 ô (từ y 50 xuống y 84). 4 kệ zigzag.
- **Cơ chế:** 3 mảng gai trên vách thò ra 3 ô trong 1 giây, thụt 2 giây. Rơi ngang qua lúc gai thò là mất mạng.
- **Địch:** 1 Drone.

### R3 – Bệ di chuyển (x 88–148, y 70–88) · độ khó 6
- **Mục đích:** bệ di động trên gai, dưới trần gai.
- **Địa hình:** hố gai 48 ô, trần gai. 4 bệ chạy ngang và chéo.
- **Địch:** 1 Brute đứng chặn ngay mép đầu, 1 Drone.
- **Vật phẩm:** Reploid #2 ở mép bên kia.

### Mini-boss – Cảnh vệ cuối (x 148–178, y 70–86) · độ khó 6
- **Đấu trường 26 ô**, kín, hai vách đá tường được.
- **Cảnh vệ cuối** là cỗ máy ghép từ mảnh của 8 boss, đổi đòn theo từng 1/4 máu:
  - 100–75%: mưa giọt (Turtloid). 75–50%: khiên phản đạn (Sheldon).
  - 50–25%: lăn cầu đất (Scaravich). 25–0%: lao lửa (Heatnix).
- **Điểm yếu:** vũ khí khắc chế đúng đòn đang dùng gây sát thương gấp đôi.
- **Phần thưởng:** mở Trung tâm 8 cổng. Hạ không mất máu thì được thưởng Souls.

### R4 – Trung tâm 8 cổng (x 178–242, y 64–86) · độ khó 7
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** **boss rush**: đấu lại 8 boss Act II (theo dữ liệu game).
- **Địa hình:** sảnh 2 tầng. 4 cổng ở tầng dưới, 4 cổng trên ban công tầng trên.
- **Cơ chế:**
  - Mỗi cổng dẫn tới đấu trường của một boss: Rainy Turtloid, Shield Sheldon, Infinity Mijinion, Commander Yammark, Metal Shark Player, Blaze Heatnix, Blizzard Wolfang, Ground Scaravich.
  - Đánh xong thì trở về sảnh, cổng đó tắt sáng. Chọn thứ tự tùy ý.
  - Đấu trường trong boss rush là **bản pha 2** của mỗi boss (cơ chế môi trường đã thiết kế ở từng màn), nhưng máu boss chỉ còn 60%.
  - Đủ 8 trận thì cửa cuối sảnh mở.
- **Vật phẩm:** Reploid #3 giữa sảnh.

### R5 – Trạm hồi máu (x 242–272, y 74–88) · độ khó 2
- **Checkpoint 2** ở đầu phòng.
- **Hồi máu giữa trận** (theo dữ liệu game): Reploid #4, hồi đầy máu và năng lượng vũ khí.

### R6 – Cầu thang Sigma (x 272–328, y 52–84) · độ khó 8
- **Mục đích:** cao trào cuối cùng. **Cầu thang dẫn lên cửa Hell Sigma sụp dần** phía sau người chơi.
- **Địa hình:** 5 bậc thang lơ lửng đi lên, rộng 6 ô, mỗi bậc cao hơn 4 ô.
- **Cơ chế:**
  - Đứng lên bậc nào thì bậc đó sụp sau 0.6 giây.
  - Ngoài ra, các bậc **sụp lần lượt từ dưới lên** mỗi 1.5 giây kể từ khi bước vào phòng, dù có đứng hay không.
  - Vực không đáy bên dưới.
- **Địch:** 2 Drone chắn ngang đường nhảy, 1 Sniper trên chiếu nghỉ cuối.

### BOSS – Hell Sigma (x 328–362, y 54–72)
- **Đấu trường 34 ô** trên đỉnh tháp, không vách.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (Hell Sigma khổng lồ, tay kiếm, tia).
- **Pha 2** (dưới 50% HP):
  - **Sàn vỡ dần từ hai mép vào**, mỗi 12 giây mất 2 ô mỗi bên, tối đa còn 18 ô.
  - Tay của Sigma bám vào mép sàn còn lại và đập.
- Điểm yếu giữ nguyên theo dữ liệu game.

---

## 3. Bảng vật phẩm và kẻ địch

| Loại | Số lượng | Vị trí |
|---|---|---|
| Sniper | 2 | R1, R6 |
| Drone | 5 | R1, R2, R3, R6 ×2 |
| Brute | 1 | R3 |
| Mini-boss | 1 | MID |
| Reploid cứu | 4 | R1, R3, R4, R5 |
| Cổng dịch chuyển | 8 | R4 ×8 |
| Checkpoint | 2 | R4, R5 |

Tổng 8 kẻ địch thường (bản cũ: 20 con xếp đều), đặt có chủ đích theo mục đích từng phòng.

---

## 4. Những gì engine cần bổ sung

1. Băng chuyền và trần gai; gai thò từ vách theo nhịp.
2. Sảnh 8 cổng: theo dõi boss đã hạ, mở cửa khi đủ 8; đấu trường boss rush dùng lại cơ chế pha 2 của từng màn.
3. Bậc thang sụp khi đứng và sụp theo lịch từ dưới lên.
4. Mini-boss Cảnh vệ cuối đổi đòn theo máu.
5. Sàn boss vỡ dần từ hai mép.

## 5. Danh sách hình cần vẽ

- **Tileset "Pháo đài cuối":** 47 ô viền đỏ đen, gai, băng chuyền, bậc thang lơ lửng (3 khung sụp).
- **Vật thể:** 8 cổng dịch chuyển có biểu tượng từng boss (sáng/tắt), gai thò (3 khung).
- **Nền:** đỉnh tháp giữa trời đỏ và hình bóng Sigma (2 lớp parallax).

**Hướng phối hợp:** như màn mẫu — dựng bằng khối màu tạm theo sơ đồ để chơi thử, chốt cảm giác rồi mới thay tile thật.
