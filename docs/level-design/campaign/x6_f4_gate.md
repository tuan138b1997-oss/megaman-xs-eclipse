# Màn: PHÒNG THÍ NGHIỆM GATE 3 (Gate's Secret Lab 3 — Boss Gate)

Bản thiết kế để duyệt trước khi dựng. Sơ đồ: `maps/x6_f4_gate.png`.
Màn này thay cho `x6_f4_gate` hiện tại. Boss Gate, vùng đảo trọng lực giấu capsule bí mật Ultimate Armor, tinh thể Nightmare nổ, trạm hồi máu đầy và đấu trường có vực giữa sàn + 3 bệ nổi vẫn giữ. Không có Heart Tank/Sub-Tank (theo dữ liệu game); thêm 4 Reploid, 1 mini-boss.

![Sơ đồ](maps/x6_f4_gate.png)

---

## 0. Công cụ và quy ước

Dùng chung với màn mẫu (`../lo-nham-thach-kich-ban.md`, mục 0): LDtk dựng bản đồ, Pixelorama vẽ tile, Krita vẽ nền parallax. 1 ô = 32px, khung hình 30×17 ô, các lớp `Collision` / `Tiles` / `Decor` / `Foreground` / `Entities`.

---

## 1. Ý tưởng tổng

Tầng 3, phòng riêng của Gate. Màn xoay quanh **tinh thể Nightmare nổ dây chuyền**: vừa là bẫy vừa là công cụ phá đường. Lối trần bí mật ở đầu màn giữ capsule Ultimate Armor.

- **Area 1 – Phòng thí nghiệm:** hồng tím, tinh thể phát sáng. Biển gai có lối trần bí mật, phòng tinh thể phá khối chắn.
- **Area 2 – Lõi phòng Gate:** hành lang tinh thể mọc lại, giếng nổ dây chuyền, trạm hồi máu.
- **Điểm nhấn trải nghiệm:** kích nổ tinh thể → chọn bệ di động hoặc đảo trọng lực lên trần lấy capsule → nổ tinh thể phá khối chắn → mini-boss tinh thể mẹ → hành lang tinh thể mọc lại → leo giếng nổ dây chuyền → Gate
- **Đường cong độ khó:** 4 → 6 → 6 → (mini-boss) → 6 → 8 → 2 → boss (thang 10).
- **Thời lượng mục tiêu:** khoảng 5–6 phút lần đầu, khoảng 2.5 phút khi đã quen.

Các mẫu thiết kế tham khảo (không chép bản đồ gốc):

- **X6, Gate Lab 3:** vùng đảo trọng lực trên biển gai giấu capsule Ultimate Armor, trạm hồi máu, đấu trường có vực + 3 bệ.
- **X5, Zero Space 3:** đi lộn ngược trên trần lấy capsule bí mật (ở đây là lối phụ, còn đường chính dùng bệ di động).
- **X3, màn Doppler:** vật nổ phá vật cản.
- **X Corrupted:** công tắc bí mật ngụy trang thành đồ trang trí.

---

## 2. Kịch bản từng phòng

Tọa độ tính theo ô, gốc (0,0) ở góc trên trái thế giới, y tăng xuống dưới.

### R1 – Sảnh Gate (x 0–36, y 44–58) · độ khó 4
- **Mục đích:** tầng 3 phòng thí nghiệm Gate. Giới thiệu **tinh thể Nightmare**: bắn hoặc chạm thì nổ sau 0.5 giây, bán kính 2 ô.
- **Địa hình:** sảnh 36 ô, trần ở y 42, sàn ở y 50.
- **Địch:** 1 Sniper. Dụ nó tới gần tinh thể rồi bắn tinh thể.
- **Vật phẩm:** Reploid #1 ở đầu sảnh.
- **Ghi chú:** màn này giữ **capsule bí mật Ultimate Armor** (theo dữ liệu game). Không có Heart Tank/Sub-Tank.

### R2 – Biển gai trần (x 36–96, y 38–62) · độ khó 6
- **Mục đích:** đường chính đi trên **bệ di động** qua biển gai. **Lối bí mật** là đi lộn ngược trên trần.
- **Địa hình:** biển gai 44 ô. 3 bệ di động ở giữa chiều cao. Trần liền, có một mảng gai 6 ô.
- **Đường chính:** nhảy qua 3 bệ di động (chạy ngang 6 ô, chu kỳ 3 giây).
- **Lối phụ (Capsule bí mật Ultimate Armor):**
  - Ở mép vực có một **công tắc trọng lực** gắn trên vách, trông giống đèn trang trí. Bắn vào thì trọng lực trong vùng đảo ngược.
  - Đi lộn ngược trên trần, nhảy (xuống dưới) qua mảng gai trần, tới capsule ở giữa trần (x ≈ 70, y ≈ 41).
  - Bắn công tắc lần nữa (bắn được từ trên trần) để trở lại bình thường, rơi xuống bệ di động.
  - Điều kiện mở capsule giữ nguyên theo dữ liệu game.
- **Địch:** 2 Drone, miễn đảo trọng lực.

### R3 – Phòng tinh thể (x 96–152, y 44–58) · độ khó 6
- **Mục đích:** dùng tinh thể nổ để **phá khối chắn**.
- **Địa hình:** phòng 56 ô, 2 khối chắn đường. Cạnh mỗi khối có tinh thể.
- **Cơ chế:** bắn tinh thể rồi lùi ra 2 ô. Vụ nổ phá khối chắn. Nổ lan: một tinh thể nổ làm tinh thể gần đó (trong 3 ô) nổ theo sau 0.3 giây.
- **Địch:** 1 Drone, 1 Brute giữa hai khối chắn.
- **Vật phẩm:** Reploid #2 cuối phòng.

### Mini-boss – Tinh thể mẹ (x 152–182, y 40–56) · độ khó 6
- **Đấu trường 26 ô**, kín, hai vách đá tường được.
- **Tinh thể mẹ** treo giữa trần, mọc tinh thể con trên sàn và vách.
- **Đòn đánh:**
  - Mọc 3 tinh thể con ở chỗ người chơi vừa đứng (1 giây sau).
  - Phát sóng làm mọi tinh thể con nổ cùng lúc.
- **Điểm yếu:** chỉ bị thương bởi vụ nổ của tinh thể con ngay dưới nó. Dụ nó mọc tinh thể giữa sân rồi bắn.
- **Phần thưởng:** mở hành lang tinh thể. Hạ không mất máu thì được thưởng Souls.

### R4 – Hành lang tinh thể (x 182–242, y 44–58) · độ khó 6
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** di chuyển giữa các cụm tinh thể **mọc lại**.
- **Cơ chế:** cụm tinh thể nổ xong thì mọc lại sau 4 giây. Phải kích nổ từ xa rồi chạy qua trước khi nó mọc lại. Cụm trên trần rơi xuống khi nổ.
- **Địch:** 1 Drone, 1 Sniper.
- **Vật phẩm:** Reploid #3 giữa hành lang.

### R5 – Giếng tinh thể (x 242–266, y 8–56) · độ khó 8
- **Mục đích:** cao trào của màn. Leo giếng trong khi **chuỗi tinh thể nổ dây chuyền** từ đáy lên.
- **Địa hình:** giếng rộng 20 ô, cao 44 ô (từ y 50 lên y 7). 5 kệ, tinh thể bám trên vách và giữa giếng.
- **Cơ chế:**
  - Mỗi 8 giây một vụ nổ ở đáy giếng, lan lên theo các tinh thể (mỗi bước 0.3 giây).
  - Đứng cạnh tinh thể khi sóng nổ tới là mất 1/3 máu và bị đẩy văng.
  - Người chơi có thể chủ động bắn nổ tinh thể phía trên để "cắt" chuỗi, tạo vùng an toàn.
- **Địch:** 2 Drone.

### R6 – Trạm hồi máu (x 266–296, y 5–19) · độ khó 2
- **Checkpoint 2** ở đầu phòng.
- **Trạm hồi máu đầy** trước phòng Gate (theo dữ liệu game): Reploid #4, hồi đầy máu và năng lượng vũ khí.

### BOSS – Gate (x 296–330, y 1–19)
- **Đấu trường 30 ô có vực thẳm giữa sàn** (rộng 14 ô) và **3 bệ lơ lửng** phía trên vực (theo dữ liệu game). Hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (tinh thể Nightmare, bắn chùm, dịch chuyển).
- **Pha 2** (dưới 50% HP):
  - Gate bắn tinh thể lên 3 bệ: bệ có tinh thể nổ thì tắt 3 giây.
  - Người chơi phải nhảy qua vực bằng các bệ còn lại để đuổi theo Gate.
- Điểm yếu giữ nguyên theo dữ liệu game.

---

## 3. Bảng vật phẩm và kẻ địch

| Loại | Số lượng | Vị trí |
|---|---|---|
| Sniper | 2 | R1, R4 |
| Drone | 6 | R2 ×2, R3, R4, R5 ×2 |
| Brute | 1 | R3 |
| Mini-boss | 1 | MID |
| Reploid cứu | 4 | R1, R3, R4, R6 |
| Capsule bí mật Ultimate Armor | 1 | R2 |
| Công tắc | 1 | R2 |
| Checkpoint | 2 | R4, R6 |

Tổng 9 kẻ địch thường (bản cũ: 20 con xếp đều), đặt có chủ đích theo mục đích từng phòng.

---

## 4. Những gì engine cần bổ sung

1. Tinh thể Nightmare: nổ khi bị bắn/chạm, nổ lan trong bán kính, mọc lại theo thời gian; phá được khối chắn.
2. Vùng đảo trọng lực bật bằng công tắc ngụy trang.
3. Bệ di động trên biển gai.
4. Trạm hồi máu đầy.
5. Mini-boss Tinh thể mẹ (chỉ bị thương bởi vụ nổ).
6. Đấu trường có vực giữa và 3 bệ có thể tắt.

## 5. Danh sách hình cần vẽ

- **Tileset "Phòng Gate":** 47 ô viền hồng tím, khối chắn phá được (2 trạng thái).
- **Vật thể:** tinh thể Nightmare (3 khung + nổ 4 khung), công tắc ngụy trang, bệ nổi đấu trường.
- **Nền:** ống nuôi Nightmare và màn hình nghiên cứu của Gate (2 lớp parallax).

**Hướng phối hợp:** như màn mẫu — dựng bằng khối màu tạm theo sơ đồ để chơi thử, chốt cảm giác rồi mới thay tile thật.
