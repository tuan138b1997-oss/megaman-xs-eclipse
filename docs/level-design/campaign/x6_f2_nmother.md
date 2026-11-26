# Màn: PHÒNG THÍ NGHIỆM GATE 1 (Gate's Secret Lab 1 — Boss Nightmare Mother)

Bản thiết kế để duyệt trước khi dựng. Sơ đồ: `maps/x6_f2_nmother.png`.
Màn này thay cho `x6_f2_nmother` hiện tại. Boss Nightmare Mother, sàn gai dày đặc, bệ di động dọc/ngang, trục leo dọc có dung nham dâng vẫn giữ. Không có capsule/Heart Tank/Sub-Tank (theo dữ liệu game); thêm 4 Reploid, 1 mini-boss và trạm nạp lớn.

![Sơ đồ](maps/x6_f2_nmother.png)

---

## 0. Công cụ và quy ước

Dùng chung với màn mẫu (`../lo-nham-thach-kich-ban.md`, mục 0): LDtk dựng bản đồ, Pixelorama vẽ tile, Krita vẽ nền parallax. 1 ô = 32px, khung hình 30×17 ô, các lớp `Collision` / `Tiles` / `Decor` / `Foreground` / `Entities`.

---

## 1. Ý tưởng tổng

Tầng 1 phòng thí nghiệm bí mật của Gate. Đây là **màn của các bệ di động trên gai**: ngang, dọc, chéo, rồi thang máy chạy đua với dung nham.

- **Area 1 – Phòng thí nghiệm đỏ:** gai khắp nơi, đèn đỏ. Gai sàn, bệ ngang/dọc, băng chuyền đẩy vào gai.
- **Area 2 – Lò dưới phòng thí nghiệm:** bệ chéo, rồi trục thang máy với dung nham dâng.
- **Điểm nhấn trải nghiệm:** nhảy qua bãi gai → bệ ngang/dọc → băng chuyền đẩy vào vách gai → mini-boss khối gai bay → bệ chéo → đua với dung nham trên thang máy → boss
- **Đường cong độ khó:** 4 → 5 → 5 → (mini-boss) → 6 → 8 → 2 → boss (thang 10).
- **Thời lượng mục tiêu:** khoảng 5–6 phút lần đầu, khoảng 2.5 phút khi đã quen.

Các mẫu thiết kế tham khảo (không chép bản đồ gốc):

- **X6, Gate Lab 1:** gai sàn dày đặc, bệ di động dọc/ngang, trục leo 600px với dung nham dâng.
- **X4, màn Magma Dragoon:** dung nham dâng.
- **X2, màn X-Hunter / X3, màn Doppler 1:** bệ di động trên gai trong pháo đài.
- **X Corrupted:** dùng lại cơ chế cũ (dung nham dâng) với điểm đứng di động để thành thử thách mới.

---

## 2. Kịch bản từng phòng

Tọa độ tính theo ô, gốc (0,0) ở góc trên trái thế giới, y tăng xuống dưới.

### R1 – Phòng gai (x 0–50, y 56–70) · độ khó 4
- **Mục đích:** tầng 1 phòng thí nghiệm Gate: **gai sàn dày**, chỉ chừa ô an toàn 2–4 ô.
- **Địa hình:** phòng 50 ô, trần ở y 42, sàn ở y 50. 3 bãi gai dài 8–10 ô.
- **Địch:** 1 Drone, 1 Sniper.
- **Vật phẩm:** Reploid #1 ở đầu phòng.
- **Ghi chú:** dữ liệu game khuyên mặc trọn bộ Blade hoặc Shadow (Shadow miễn gai). Không có capsule/Heart Tank/Sub-Tank.

### R2 – Bệ di động trên gai (x 50–114, y 52–70) · độ khó 5
- **Mục đích:** **bệ di động** cả ngang lẫn dọc trên một hố gai dài 52 ô.
- **Cơ chế:** bệ 1 và 3 chạy ngang 6 ô; bệ 2 và 4 chạy lên xuống 6 ô. Nhảy từ bệ ngang sang bệ dọc phải canh cả hai chuyển động.
- **Địch:** 2 Drone: một bay cao, một bay sát gai.

### R3 – Băng chuyền gai (x 114–170, y 56–70) · độ khó 5
- **Mục đích:** băng chuyền **đẩy người chơi vào vách gai** ở giữa phòng.
- **Địa hình:** phòng 56 ô. Giữa phòng có một vách gai thấp (cao 4 ô) mà hai băng chuyền đều đẩy về phía nó.
- **Cơ chế:** băng chuyền 120px/giây. Phải nhảy lên kệ trên cao ngay trước vách gai, rồi nhảy qua.
- **Địch:** 1 Brute trên băng chuyền thứ hai (bị đẩy về phía vách gai theo người chơi).
- **Vật phẩm:** Reploid #2 cuối phòng.

### Mini-boss – Lõi cảnh vệ (x 170–200, y 52–68) · độ khó 6
- **Đấu trường 26 ô**, kín, trần phủ gai.
- **Lõi cảnh vệ** lơ lửng giữa phòng, điều khiển 4 khối gai bay.
- **Đòn đánh:**
  - Khối gai bay theo hình vuông quanh sân.
  - Khối gai lao thẳng về phía người chơi, cắm vào vách 2 giây (đứng lên được, làm bệ).
- **Điểm yếu:** lõi, chỉ hở khi ít nhất 2 khối gai đang cắm vào vách.
- **Phần thưởng:** mở cầu bệ chéo. Hạ không mất máu thì được thưởng Souls.

### R4 – Cầu bệ chéo (x 200–260, y 52–70) · độ khó 6
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** bệ chạy **chéo 45°** trên hố gai.
- **Cơ chế:** mỗi bệ chạy chéo lên-xuống 5 ô. Đáp lên bệ đang đi xuống thì có cảm giác "hụt chân".
- **Địch:** 1 Drone, 1 Sniper ở mép bên kia.
- **Vật phẩm:** Reploid #3 trên bệ thứ ba.

### R5 – Trục thang máy dung nham (x 260–286, y 10–68) · độ khó 8
- **Mục đích:** cao trào của màn. Trục dọc 600px: **thang máy** chạy lên chậm hơn **dung nham dâng**.
- **Địa hình:** trục rộng 22 ô, cao 54 ô (từ y 66 lên y 13). 5 thang máy nhỏ.
- **Cơ chế:**
  - Dung nham dâng 60px/giây, tăng lên 80px/giây ở nửa trên.
  - Thang máy tự chạy lên 70px/giây rồi dừng ở đỉnh hành trình (6 ô) và quay xuống.
  - Đứng yên trên thang máy thì sớm muộn bị dung nham đuổi kịp. Phải nhảy sang thang máy kế tiếp, cao hơn, đúng lúc nó đang ở đáy hành trình.
  - Khác Lò Nham Thạch (kệ cố định) và Khu dung nham (dâng theo bậc): ở đây mọi điểm đứng đều di chuyển.
- **Địch:** 2 Drone.

### R6 – Trạm nghỉ (x 286–316, y 7–21) · độ khó 2
- **Checkpoint 2** ở đầu phòng.
- Phòng nghỉ trước boss: Reploid #4, **nạp năng lượng lớn**, cửa boss.

### BOSS – Nightmare Mother (x 316–348, y 3–19)
- **Đấu trường 28 ô**, kín, hai góc sàn có gai.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (lõi trung tâm, 2 khối phụ, bắn Nightmare).
- **Pha 2** (dưới 50% HP):
  - **Gai sàn lan dần vào giữa** mỗi 10 giây (mỗi lần thêm 2 ô mỗi bên), tối đa còn 12 ô sàn an toàn.
- Điểm yếu giữ nguyên theo dữ liệu game.

---

## 3. Bảng vật phẩm và kẻ địch

| Loại | Số lượng | Vị trí |
|---|---|---|
| Sniper | 2 | R1, R4 |
| Drone | 6 | R1, R2 ×2, R4, R5 ×2 |
| Brute | 1 | R3 |
| Mini-boss | 1 | MID |
| Reploid cứu | 4 | R1, R3, R4, R6 |
| Checkpoint | 2 | R4, R6 |

Tổng 9 kẻ địch thường (bản cũ: 20 con xếp đều), đặt có chủ đích theo mục đích từng phòng.

---

## 4. Những gì engine cần bổ sung

1. Bệ di động ngang, dọc và chéo; thang máy tự chạy lên rồi quay xuống.
2. Dung nham dâng liên tục có tăng tốc.
3. Băng chuyền và vách gai.
4. Mini-boss Lõi cảnh vệ: khối gai bay cắm vào vách làm bệ tạm.
5. Gai sàn lan dần trong trận boss.

## 5. Danh sách hình cần vẽ

- **Tileset "Gate Lab":** 47 ô viền kim loại đỏ có đèn, gai, băng chuyền.
- **Vật thể:** bệ di động (3 loại), thang máy, khối gai bay, mặt dung nham (4 khung).
- **Nền:** ống nghiệm Nightmare và máy móc của Gate (2 lớp parallax).

**Hướng phối hợp:** như màn mẫu — dựng bằng khối màu tạm theo sơ đồ để chơi thử, chốt cảm giác rồi mới thay tile thật.
