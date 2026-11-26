# Màn: BẢO TÀNG TRUNG TÂM (Central Museum — Boss Ground Scaravich)

Bản thiết kế để duyệt trước khi dựng. Sơ đồ: `maps/x6_scaravich.png`.
Màn này thay cho `x6_scaravich` hiện tại. Boss, capsule Blade Arm, 5 đèn pha an ninh, 4 cổng dịch chuyển (Cell 1 và Cell 2), Đại cột Totem ở mid-gate, đá lăn và cổng Alt Path vẫn giữ; thêm 4 Reploid, Sub-Tank và thay địa hình. Heart Tank giữ ở Cell 1.

![Sơ đồ](maps/x6_scaravich.png)

---

## 0. Công cụ và quy ước

Dùng chung với màn mẫu (`../lo-nham-thach-kich-ban.md`, mục 0): LDtk dựng bản đồ, Pixelorama vẽ tile, Krita vẽ nền parallax. 1 ô = 32px, khung hình 30×17 ô, các lớp `Collision` / `Tiles` / `Decor` / `Foreground` / `Entities`.

---

## 1. Ý tưởng tổng

Bảo tàng lịch sử ban đêm, hệ thống an ninh vẫn chạy. Màn này là **lẻn và giải đố**: tránh đèn pha, dùng cổng dịch chuyển giữa các phòng triển lãm, né đá lăn và totem cổ.

- **Area 1 – Sảnh và Cell 1:** gỗ, đá cẩm thạch, ánh đèn vàng ấm. Dạy đèn pha, chỗ nấp, cổng dịch chuyển, leo giếng có đèn chùm.
- **Area 2 – Khu triển lãm cổ:** đá sa thạch, tượng Ai Cập và totem. Đá lăn, cụm cổng Cell 2, phòng totem trồi thụt.
- **Điểm nhấn trải nghiệm:** nấp tránh đèn pha → lẻn qua hành lang → dịch chuyển lên kho lấy Heart Tank → leo dưới đèn chùm → phá cột totem → leo dốc đá lăn → giải cụm Cell 2 → vượt totem trồi thụt → boss trong bóng tối
- **Đường cong độ khó:** 2 → 3 → 4 → 4 → (mini-boss) → 5 → 7 → 6 → 2 → boss (thang 10).
- **Thời lượng mục tiêu:** khoảng 6–8 phút lần đầu, khoảng 3 phút khi đã quen.

Các mẫu thiết kế tham khảo (không chép bản đồ gốc):

- **X6, màn Ground Scaravich:** đèn pha an ninh, cụm cổng dịch chuyển Cell 1/Cell 2, Đại cột Totem, đá lăn, capsule Blade Arm.
- **X8, màn Dark Mantis:** đèn quét, bị phát hiện thì sinh thêm địch.
- **X5, màn mẫu Lò Nham Thạch (R2):** vật lăn theo dốc đuổi người chơi.
- **X Corrupted:** bị phát hiện không phạt mất mạng mà phạt thời gian và khóa vật phẩm.

---

## 2. Kịch bản từng phòng

Tọa độ tính theo ô, gốc (0,0) ở góc trên trái thế giới, y tăng xuống dưới.

### R1 – Sảnh bảo tàng (x 0–44, y 50–64) · độ khó 2
- **Mục đích:** giới thiệu **đèn pha an ninh** trong lúc chưa có hậu quả nặng.
- **Địa hình:** sảnh 44 ô, trần ở y 52, sàn ở y 60. Một tủ trưng bày làm chỗ nấp.
- **Cơ chế – đèn pha:**
  - Đèn quét qua lại trên sàn (rộng 5 ô, 60px/giây).
  - Đứng trong vệt sáng 0.5 giây là **bị phát hiện**: còi báo động, cửa chớp hai đầu phòng sập xuống và 2 Drone an ninh bay ra. Hạ hết Drone thì cửa mở lại.
  - Nấp sau tủ trưng bày hoặc lướt qua nhanh thì không bị phát hiện.
- **Địch:** 1 Drone, 1 Sniper (không tính Drone an ninh sinh ra khi báo động).

### R2 – Hành lang đèn pha (x 44–114, y 50–64) · độ khó 3
- **Mục đích:** lẻn qua **3 đèn pha** quét lệch pha nhau.
- **Địa hình:** hành lang 70 ô, 4 tủ trưng bày làm chỗ nấp, cách nhau 18 ô.
- **Cơ chế:** đi từ tủ này sang tủ kia lúc vệt sáng vừa quét qua. Bị phát hiện thì cửa chớp sập, 2 Drone an ninh xuất hiện.
- **Địch:** 1 Sniper cuối hành lang.
- **Vật phẩm:** Reploid #1 sau tủ thứ ba.
- **Ghi chú:** bị phát hiện không mất mạng, chỉ tốn thời gian và máu. Người chơi giỏi đi qua không bị phát hiện lần nào.

### R3 – Cụm phòng Cell 1 (x 114–164, y 40–64) · độ khó 4
- **Mục đích:** giới thiệu **cổng dịch chuyển** của cụm phòng triển lãm.
- **Địa hình:**
  - Phòng 2 tầng. Tầng dưới (y 60) là đường chính, đi thẳng sang phải.
  - Tầng trên (y 48) là phòng kho bảo tàng, không có lối đi bộ vào.
- **Cơ chế:** **cổng P1** cuối tầng dưới đưa lên **cổng P2** ở đầu tầng trên. Tầng trên có một đèn pha quét.
- **Địch:** 1 Drone, 1 Sniper ở tầng dưới.
- **Lối phụ (Heart Tank):** cuối tầng trên (x ≈ 152, y ≈ 47). Phải đi qua vệt đèn pha mà không bị phát hiện; bị phát hiện thì Heart Tank bị khóa trong lồng kính cho tới khi hạ hết Drone an ninh.

### R4 – Giếng mái vòm (x 164–186, y 14–62) · độ khó 4
- **Mục đích:** đoạn dọc dưới mái vòm bảo tàng.
- **Địa hình:** giếng rộng 18 ô, cao 44 ô (từ y 60 lên y 21). 4 kệ zigzag.
- **Bẫy – đèn chùm:** một đèn chùm pha lê lắc qua lại giữa giếng (chu kỳ 3 giây). Đứng lên đèn chùm được, nhưng nó lắc mạnh dần.
- **Địch:** 1 Drone.

### Mini-boss – Đại cột Totem (x 186–216, y 7–23) · độ khó 5
- **Đấu trường 26 ô**, hai vách đá tường được. Giữa sân là một **cột totem khổng lồ** cao từ sàn tới trần, chắn đôi đấu trường.
- **Đòn đánh:**
  - Totem có 4 mặt xếp chồng, mỗi mặt quay về một phía và bắn theo nhịp.
  - Mặt dưới cùng phun lửa sát sàn.
  - Totem thụt xuống sàn 2 giây rồi trồi lên (đứng trên chỗ nó trồi là bị hất lên trần).
- **Điểm yếu:** phá từng mặt từ dưới lên. Mỗi mặt bị phá thì totem thấp đi một nấc, đến khi nhảy qua được.
- **Phần thưởng:** mở đường vào khu triển lãm cổ. Hạ không mất máu thì được thưởng Souls.

### R5 – Dốc đá lăn (x 216–276, y 9–23) · độ khó 5
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** leo dốc ngược chiều **đá lăn**.
- **Địa hình:** hành lang 60 ô, đoạn sau là dốc 22.5° đi lên dài 20 ô.
- **Bẫy:** tảng đá tròn (tượng cổ vỡ) lăn từ đỉnh dốc xuống mỗi 2.5 giây, nhanh dần. Nhảy qua, hoặc bắn 4 phát cho vỡ. Đá lăn hết dốc thì đập vào bệ tượng đầu phòng và vỡ.
- **Địch:** 1 Brute giữa phòng (đá lăn hạ được nó), 1 Sniper trên đỉnh dốc.
- **Vật phẩm:** Reploid #2 nấp trên bệ tượng đầu phòng.

### R6 – Cụm phòng Cell 2 (x 276–340, y 0–26) · độ khó 7
- **Mục đích:** cao trào của màn. Kết hợp **cổng dịch chuyển, đèn pha và đá lăn** trong một phòng.
- **Địa hình:**
  - Tầng dưới (y 24) bị cắt bởi **hố gai** dài 22 ô, không nhảy qua được.
  - Cổng **P3** ở đầu tầng dưới đưa lên cổng **P4** trên ban công giữa (y 12).
  - Ban công dài 32 ô, có 2 đèn pha quét.
  - Đá lăn từ đầu phải ban công lăn sang trái mỗi 2 giây, đúng vào đường đi.
  - Cuối ban công nhảy xuống tầng dưới phía sau hố gai để ra cửa.
- **Cơ chế:** bị đèn pha phát hiện thì đá lăn nhanh gấp đôi và cửa ra sập lại tới khi hạ Drone an ninh.
- **Địch:** 2 Drone.
- **Lối phụ (Capsule Blade Arm):**
  - Hốc cao sát vách phải (x ≈ 333, y ≈ 3).
  - Từ cuối ban công, đá tường vách phải 3 lần lên hốc. Phải làm trước khi đá lăn tiếp theo tới.
- **Ghi chú:** phòng này cũng giữ cổng sang lối thay thế (Alt Path) theo dữ liệu game, đặt cạnh cổng P3.

### R7 – Phòng Totem (x 340–396, y 12–26) · độ khó 6
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** kết hợp: **cột totem** trồi lên chặn đường rồi thụt xuống.
- **Địa hình:** phòng 56 ô, 3 cột totem.
- **Cơ chế:** mỗi cột trồi lên chặn kín 2 giây, thụt xuống 2 giây, lệch pha nhau. Đứng trên cột lúc nó trồi thì bị đẩy lên sát trần.
- **Địch:** 1 Drone, 1 Sniper cuối phòng.
- **Vật phẩm:** Reploid #3 giữa cột 1 và cột 2.
- **Lối phụ (Sub-Tank):** trên đỉnh cột totem thứ hai, lúc nó trồi lên cao nhất. Đứng lên cột lúc nó đang thụt rồi để nó đưa lên.

### R8 – Phòng trưng bày cuối (x 396–426, y 12–26) · độ khó 2
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss.

### BOSS – Ground Scaravich (x 426–458, y 8–24)
- **Đấu trường 28 ô**, hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (lăn quả cầu đất, đào, nhảy).
- **Pha 2** (dưới 50% HP):
  - **Tắt đèn**, chỉ còn một đèn pha quét qua lại. Quả cầu đất chỉ thấy khi lăn vào vệt sáng.
  - Bị đèn pha chiếu vào thì Scaravich nhắm theo chính xác hơn.
- Điểm yếu giữ nguyên theo dữ liệu game.

---

## 3. Bảng vật phẩm và kẻ địch

| Loại | Số lượng | Vị trí |
|---|---|---|
| Sniper | 5 | R1, R2, R3, R5, R7 |
| Drone | 6 | R1, R3, R4, R6 ×2, R7 |
| Brute | 1 | R5 |
| Mini-boss | 1 | MID |
| Reploid cứu | 4 | R2, R5, R7, R8 |
| Heart Tank | 1 | R3 |
| Sub-Tank | 1 | R7 |
| Capsule Blade Arm | 1 | R6 |
| Cổng dịch chuyển | 4 | R3 ×2, R6 ×2 |
| Checkpoint | 2 | R5, R7 |

Tổng 12 kẻ địch thường (bản cũ: 20 con xếp đều), đặt có chủ đích theo mục đích từng phòng.

---

## 4. Những gì engine cần bổ sung

1. Đèn pha quét theo đường cố định; đứng trong vệt sáng 0.5 giây thì kích hoạt báo động (cửa chớp sập, sinh Drone an ninh, khóa vật phẩm).
2. Cổng dịch chuyển theo cặp (P1–P2, P3–P4).
3. Đá lăn theo dốc, phá được, gây sát thương cả địch.
4. Đèn chùm lắc (bệ con lắc).
5. Cột totem trồi/thụt theo nhịp, đẩy người chơi lên.
6. Mini-boss Đại cột Totem: phá từng mặt từ dưới lên.

## 5. Danh sách hình cần vẽ

- **Tileset "Sảnh bảo tàng" (Area 1):** 47 ô viền đá cẩm thạch và gỗ, tủ trưng bày, cửa chớp (2 trạng thái).
- **Tileset "Triển lãm cổ" (Area 2):** 47 ô viền sa thạch, dốc, bệ tượng.
- **Vật thể:** đèn pha (vệt sáng 3 khung), đèn chùm, cổng dịch chuyển (4 khung), đá lăn (4 khung), cột totem (4 mặt), lồng kính.
- **Nền:** Area 1: phòng trưng bày tối (2 lớp parallax). Area 2: tượng và kim tự tháp mô hình (2 lớp).

**Hướng phối hợp:** như màn mẫu — dựng bằng khối màu tạm theo sơ đồ để chơi thử, chốt cảm giác rồi mới thay tile thật.
