# Màn: PHÒNG THÍ NGHIỆM GATE 2 (Gate's Secret Lab 2 — Boss High Max)

Bản thiết kế để duyệt trước khi dựng. Sơ đồ: `maps/x6_f3_highmax.png`.
Màn này thay cho `x6_f3_highmax` hiện tại. Boss High Max, vực gai toàn khu, chuỗi bệ nhỏ lơ lửng, 2 cột totem chặn bệ và tia laser quét dọc vẫn giữ. Không có capsule/Heart Tank/Sub-Tank (theo dữ liệu game); thêm 4 Reploid, 1 mini-boss và trạm nạp lớn.

![Sơ đồ](maps/x6_f3_highmax.png)

---

## 0. Công cụ và quy ước

Dùng chung với màn mẫu (`../lo-nham-thach-kich-ban.md`, mục 0): LDtk dựng bản đồ, Pixelorama vẽ tile, Krita vẽ nền parallax. 1 ô = 32px, khung hình 30×17 ô, các lớp `Collision` / `Tiles` / `Decor` / `Foreground` / `Entities`.

---

## 1. Ý tưởng tổng

Tầng 2 phòng thí nghiệm Gate: **màn nhảy chính xác** khó nhất. Gần như toàn màn là vực gai với bệ chỉ rộng 2 ô.

- **Area 1 – Vực gai trên:** bệ nhỏ, laser dọc chạy ngang.
- **Area 2 – Vực gai dưới:** totem trồi chặn bệ, rồi đoạn tổng hợp mọi thứ.
- **Điểm nhấn trải nghiệm:** lướt-nhảy giữa bệ 2 ô → canh khe giữa 2 tia laser → làm choáng khối giáp → né totem trồi → đoạn tổng hợp → High Max
- **Đường cong độ khó:** 4 → 6 → 6 → (mini-boss) → 7 → 8 → 2 → boss (thang 10).
- **Thời lượng mục tiêu:** khoảng 5–7 phút lần đầu (nhiều lần chết), khoảng 2.5 phút khi đã quen.

Các mẫu thiết kế tham khảo (không chép bản đồ gốc):

- **X6, Gate Lab 2:** vực gai, 10 bệ nhỏ, 2 totem chặn bệ, laser quét dọc, High Max cần Charge Saber.
- **X (SNES), màn Sigma 2:** chuỗi bệ nhỏ trên gai.
- **X6, màn Ground Scaravich:** totem trồi/thụt.
- **X Corrupted:** mini-boss dạy trước cách hạ boss (làm choáng rồi mới đánh).

---

## 2. Kịch bản từng phòng

Tọa độ tính theo ô, gốc (0,0) ở góc trên trái thế giới, y tăng xuống dưới.

### R1 – Mép vực gai (x 0–40, y 40–58) · độ khó 4
- **Mục đích:** tầng 2 phòng thí nghiệm Gate: thử thách **nhảy chính xác** khó nhất game bắt đầu.
- **Địa hình:** mỏm sàn 30 ô, sau đó là **vực gai** kéo dài gần hết màn.
- **Địch:** 1 Sniper ở mép vực.
- **Vật phẩm:** Reploid #1 ở đầu mỏm.
- **Ghi chú:** dữ liệu game khuyên dùng Charge Saber của Blade Armor để làm choáng giáp High Max. Không có capsule/Heart Tank/Sub-Tank.

### R2 – Chuỗi bệ nhỏ 1 (x 40–104, y 36–58) · độ khó 6
- **Mục đích:** chuỗi **bệ nhỏ 2 ô** cách nhau 10 ô trên vực gai.
- **Cơ chế:** khoảng cách 10 ô vừa đủ cho một cú lướt-nhảy. Nhảy thường không tới.
- **Địch:** 2 Drone ở khoảng giữa các bệ: bị bắn trúng là rơi. Hạ chúng từ bệ trước rồi mới nhảy.

### R3 – Laser quét dọc (x 104–164, y 36–58) · độ khó 6
- **Mục đích:** bệ nhỏ cộng **tia laser dọc chạy ngang**.
- **Cơ chế:** 2 tia laser cao hết phòng chạy qua lại ngược chiều nhau, 80px/giây. Tia đi qua bệ nào thì bệ đó không đứng được lúc ấy. Phải nhảy theo khoảng trống giữa hai tia.
- **Địch:** 1 Drone.
- **Vật phẩm:** Reploid #2 trên bệ thứ ba.

### Mini-boss – Khối giáp Nightmare (x 164–196, y 36–56) · độ khó 6
- **Đấu trường là 3 bệ** trên vực gai.
- **Khối giáp Nightmare** là phiên bản nhỏ của High Max, giáp bất khả xâm phạm.
- **Đòn đánh:**
  - Bắn quả cầu năng lượng chậm, nảy giữa các bệ.
  - Dịch chuyển sang bệ khác và đập xuống bệ đó (bệ rung, người đứng trên bị nảy lên).
- **Điểm yếu:** chỉ nhận sát thương sau khi bị **làm choáng** bằng đạn nạp đầy hoặc Charge Saber. Đây là bài học trước trận High Max.
- **Phần thưởng:** mở khu totem. Hạ không mất máu thì được thưởng Souls.

### R4 – Bệ totem (x 196–256, y 36–58) · độ khó 7
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** **cột totem chặn bệ**: totem trồi lên ngay trên bệ nhảy.
- **Cơ chế:** 2 bệ có totem. Totem trồi chiếm hết bệ 2 giây, thụt 2 giây. Đáp lên bệ lúc totem sắp trồi là bị hất văng.
- **Địch:** 1 Sniper đứng trên bệ không có totem.
- **Vật phẩm:** Reploid #3 ở mỏm bên kia.

### R5 – Chuỗi bệ nhỏ 2 (x 256–326, y 36–58) · độ khó 8
- **Mục đích:** cao trào của màn. Ghép tất cả: bệ 2 ô, laser chạy ngang, totem chặn bệ, Drone.
- **Địa hình:** vực gai 70 ô, 6 bệ nhỏ.
- **Cơ chế:** 2 tia laser dọc, 1 totem trên bệ giữa. Nhịp của laser và totem không khớp nhau.
- **Địch:** 2 Drone.
- **Giáp hỗ trợ:** Shadow miễn gai nên rơi xuống vực không mất mạng (vẫn phải leo lên). Ultimate lướt Nova Strike xuyên totem.

### R6 – Trạm nghỉ (x 326–356, y 40–54) · độ khó 2
- **Checkpoint 2** ở đầu phòng.
- Phòng nghỉ trước boss: Reploid #4, **nạp năng lượng lớn**, cửa boss.

### BOSS – High Max (x 356–388, y 36–52)
- **Đấu trường 28 ô**, kín, hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (giáp bất khả xâm phạm, cầu năng lượng, dịch chuyển). Phải làm choáng bằng Charge Saber/đạn nạp đầy rồi mới gây sát thương (theo dữ liệu game).
- **Pha 2** (dưới 50% HP):
  - **4 khối giáp** bay quanh High Max, chặn đạn. Một khối bị phá thì 4 giây sau mọc lại.
- Điểm yếu giữ nguyên theo dữ liệu game.

---

## 3. Bảng vật phẩm và kẻ địch

| Loại | Số lượng | Vị trí |
|---|---|---|
| Sniper | 2 | R1, R4 |
| Drone | 5 | R2 ×2, R3, R5 ×2 |
| Mini-boss | 1 | MID |
| Reploid cứu | 4 | R1, R3, R4, R6 |
| Checkpoint | 2 | R4, R6 |

Tổng 7 kẻ địch thường (bản cũ: 20 con xếp đều), đặt có chủ đích theo mục đích từng phòng.

---

## 4. Những gì engine cần bổ sung

1. Bệ nhỏ 2 ô; vực gai toàn màn.
2. Tia laser dọc chạy ngang.
3. Totem trồi/thụt trên bệ, hất văng người chơi.
4. Trạng thái "giáp bất khả xâm phạm" chỉ hở khi bị làm choáng.
5. Mini-boss Khối giáp Nightmare.

## 5. Danh sách hình cần vẽ

- **Tileset "Gate Lab 2":** 47 ô viền tím, bệ nhỏ 2 ô, vực gai.
- **Vật thể:** tia laser dọc (3 khung), totem (3 khung trồi), khối giáp bay.
- **Nền:** hành lang phòng thí nghiệm tím và ống năng lượng (2 lớp parallax).

**Hướng phối hợp:** như màn mẫu — dựng bằng khối màu tạm theo sơ đồ để chơi thử, chốt cảm giác rồi mới thay tile thật.
