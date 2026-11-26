# Màn: CĂN CỨ ĐÁY BIỂN (Ocean Base — Boss Tidal Makkoeen)

Bản thiết kế để duyệt trước khi dựng. Sơ đồ: `maps/x5_makkoeen.png`.
Màn này thay cho `x5_makkoeen` hiện tại. Boss, capsule Falcon Head và sub-boss tàu ngầm U-555 vẫn giữ; thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.

![Sơ đồ](maps/x5_makkoeen.png)

---

## 0. Công cụ và quy ước

Dùng chung với màn mẫu (`../lo-nham-thach-kich-ban.md`, mục 0): LDtk dựng bản đồ, Pixelorama vẽ tile, Krita vẽ nền parallax. 1 ô = 32px, khung hình 30×17 ô, các lớp `Collision` / `Tiles` / `Decor` / `Foreground` / `Entities`.

---

## 1. Ý tưởng tổng

Một căn cứ hải quân chìm dần dưới biển. Toàn màn xoay quanh **nước**: dưới nước thì nhảy cao, rơi chậm, nhưng dòng chảy và thủy lôi khó lường. Người chơi học cách tận dụng nước, rồi học cách điều khiển mực nước.

- **Area 1 – Cảng và hành lang ngập:** bê tông, đèn xanh, bọt khí. Dạy trọng lực nước, thủy lôi, leo giếng nửa ngập.
- **Area 2 – Đáy biển:** ống thép, san hô gai, bóng tối xanh thẫm. Câu đố mực nước, ống hút ngược dòng, rãnh đi xuống.
- **Điểm nhấn trải nghiệm:** lặn xuống → nhảy siêu cao dưới nước → leo giếng nửa ngập → đấu tàu ngầm → rút/bơm nước → bơi ngược dòng hút → luồn xuống rãnh gai → boss nước dâng
- **Đường cong độ khó:** 2 → 3 → 4 → (mini-boss) → 5 → 7 → 6 → 2 → boss (thang 10).
- **Thời lượng mục tiêu:** khoảng 6–8 phút lần đầu, khoảng 3 phút khi đã quen.

Các mẫu thiết kế tham khảo (không chép bản đồ gốc):

- **X5, màn Tidal Makkoeen:** căn cứ đáy biển, tàu ngầm làm sub-boss, capsule giáp trên hốc trần cần nhảy cao.
- **X (SNES) Launch Octopus / X3 Toxic Seahorse:** nhảy cao dưới nước làm cơ chế chính.
- **X4, màn Jet Stingray / X6 Metal Shark Player:** đoạn bị cuốn hoặc bị ép, phải di chuyển liên tục.
- **X8 16-bit demake / X Corrupted:** câu đố công tắc thay đổi địa hình; lối phụ đòi hiểu cơ chế thay vì chỉ kỹ năng.

---

## 2. Kịch bản từng phòng

Tọa độ tính theo ô, gốc (0,0) ở góc trên trái thế giới, y tăng xuống dưới.

### R1 – Bến cảng (x 0–50, y 40–60) · độ khó 2
- **Mục đích:** giới thiệu **nước**: vào nước thì trọng lực nhẹ (×0.32), nhảy cao gấp khoảng 2.5 lần nhưng rơi chậm.
- **Địa hình:**
  - Cầu tàu bê tông dài 30 ô, mặt sàn ở y 48.
  - Cuối cầu tàu là mặt biển. Đáy biển ở y 58, nước sâu 8 ô.
  - Trên mặt nước có sóng nhấp nhô 1 ô (chỉ để nhìn, không đẩy).
- **Địch:**
  - 1 Sniper trên cầu tàu.
  - 1 Drone bay sát mặt nước, lao xuống khi người chơi nhảy xuống nước.
- **Trang trí:** cần cẩu bến, container, đèn hải đăng ở nền xa.

### R2 – Hành lang ngập (x 50–120, y 40–60) · độ khó 3
- **Mục đích:** luyện di chuyển dưới nước và né **thủy lôi**.
- **Địa hình:**
  - Hành lang căn cứ ngập hoàn toàn, dài 70 ô, trần ở y 42, đáy ở y 58.
  - 2 kệ cao sát trần (y 47 và y 46). Chỉ với tới được nhờ trọng lực nước.
- **Bẫy:**
  - **3 thủy lôi** trôi lơ lửng, nhấp nháy. Chạm hoặc bắn trúng thì nổ sau 1 giây, bán kính 2 ô. Bắn từ xa là an toàn.
  - **Dòng chảy ngang** đẩy sang phải 60px/giây ở nửa sau hành lang (có bọt khí chỉ hướng). Đi xuôi dòng nhanh hơn, nhưng dễ trôi vào thủy lôi.
- **Địch:** 2 Drone dạng cá máy, bơi zigzag.
- **Vật phẩm:** Reploid #1 trên kệ cao thứ hai.

### R3 – Trụ thông khí (x 120–140, y 10–60) · độ khó 4
- **Mục đích:** đoạn dọc đầu tiên, nửa dưới ngập nước, nửa trên là không khí.
- **Địa hình:**
  - Giếng rộng 16 ô, cao 48 ô (từ y 58 lên y 11).
  - Mặt nước ở y 30. Dưới mặt nước leo rất dễ (nhảy cao), lên khỏi mặt nước thì trọng lực trở lại bình thường: phải đá tường.
  - 4 kệ zigzag. Lối ra ở khe vách phải phía trên (y 15–24).
- **Địch:**
  - 1 Drone cá dưới nước.
  - 1 Sniper trên kệ cao nhất, bắn xuống khi người chơi vừa ra khỏi mặt nước.
- **Bẫy:** 1 thủy lôi ngay dưới mặt nước.
- **Lối phụ (Capsule Falcon Head):**
  - Kệ capsule nằm sát trần bên trái (x ≈ 124, y ≈ 14), cao hơn mọi kệ khác.
  - Mẹo: **nhảy từ dưới nước lên**. Nhảy ở mặt nước giữ được độ cao của nhảy dưới nước, vừa đủ với tới kệ.
  - Đá tường từ kệ cao nhất cũng không tới, nên người chơi phải hiểu cơ chế nước.

### Mini-boss – Tàu ngầm U-555 (x 140–180, y 14–34) · độ khó 5
- **Đấu trường 38 ô**, nước ngập đến y 22 (sâu 10 ô).
- **Tàu ngầm U-555** bơi qua lại trong nước, chỉ nhô tháp chỉ huy lên mặt nước.
- **Đòn đánh:**
  - Bắn 2 ngư lôi đuổi theo chậm: bắn hạ được.
  - Thả 4 thủy lôi nổi lên từ từ.
  - Nhô lên húc theo đường cong khi người chơi đứng trên mặt nước.
- **Mực nước:** mỗi khi mất 1/3 máu, tàu xả van và nước hạ 2 ô. Nước càng thấp thì tàu càng lộ thân, nhưng người chơi mất khả năng nhảy cao.
- **Điểm yếu:** tháp chỉ huy (nhảy từ nước lên mà bắn).
- **Phần thưởng:** mở cửa phòng bơm. Hạ không mất máu thì được thưởng Souls.

### R4 – Phòng bơm (x 180–230, y 14–38) · độ khó 5
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** câu đố **mực nước**: lúc thì cần nước để nhảy cao, lúc thì cần rút nước để xuống sâu.
- **Địa hình:**
  - Phòng 48 ô, giữa có một **bồn trũng** sâu 4 ô (x 194–216).
  - Cửa ra nằm cao ở vách phải (y 18–23). Chỉ với tới khi phòng còn ngập.
- **Cơ chế:**
  - **Công tắc 1** trên kệ cao bên trái: bắn vào thì bơm rút nước trong 3 giây, chỉ còn đọng trong bồn trũng.
  - **Công tắc 2** dưới đáy bồn: bắn vào thì nước dâng lại trong 3 giây.
- **Địch:**
  - 1 Brute dưới đáy bồn (chỉ lộ ra khi rút nước).
  - 1 Sniper ở kệ cửa ra.
- **Vật phẩm:** Reploid #2 ở đầu phòng.
- **Lối phụ (Sub-Tank):**
  - Đường chính không cần rút nước: cứ nhảy cao dưới nước rồi lên kệ cửa ra.
  - Muốn lấy **Sub-Tank** ở đáy bồn: bắn công tắc 1, xuống bồn, hạ Brute, lấy Sub-Tank, rồi bắn công tắc 2 để nước dâng lại mới ra được.

### R5 – Ống hải lưu (x 230–294, y 10–28) · độ khó 7
- **Mục đích:** cao trào của màn. Bơi ngược dòng hút mạnh dần trong một ống có san hô gai.
- **Cơ chế:**
  - **Tua-bin** ở đầu trái ống hút nước về phía nó: 60px/giây, tăng lên 90px/giây ở nửa sau ống.
  - Chạm tua-bin là mất mạng.
  - Đi sang phải nghĩa là đi ngược dòng: phải lướt liên tục, mỗi lần dừng là bị kéo lùi.
- **Địa hình:**
  - Ống dài 64 ô, cao 8 ô (y 18–26).
  - **San hô gai** mọc xen kẽ trên trần và dưới sàn. Nhảy quá cao (trọng lực nước) là chạm gai trần, nên phải nhảy thấp.
- **Bẫy:** 2 thủy lôi trôi theo dòng về phía người chơi.
- **Địch:** 2 Drone cá. Cá đầu tiên chặn giữa hai bụi gai.
- **Lối phụ (Heart Tank):**
  - Giữa ống có một **giếng đứng** đi lên (x 260–264). Trong giếng không có dòng hút.
  - Heart Tank ở đỉnh giếng. Giếng cũng là chỗ nghỉ duy nhất trong ống.
- **Giáp hỗ trợ:** Falcon lướt trên không xa hơn, vượt dòng dễ hơn.

### R6 – Rãnh san hô (x 294–320, y 16–62) · độ khó 6
- **Checkpoint 2** ở đầu phòng (gờ đá ngay cửa ống).
- **Mục đích:** đi xuống có kiểm soát: rơi chậm trong nước nhưng bị dòng kéo xuống.
- **Địa hình:**
  - Rãnh đứng rộng 22 ô, sâu 34 ô (từ y 26 xuống y 60).
  - **4 mỏm san hô gai** chìa ra xen kẽ trái/phải.
- **Cơ chế:** dòng nước **kéo xuống 40px/giây**. Người chơi phải lái sang trái/phải để luồn giữa các mỏm gai. Thả tay là trôi thẳng vào gai.
- **Địch:**
  - 1 Drone cá giữa rãnh.
  - 1 Sniper đứng trên mỏm san hô cuối, bắn lên.
- **Vật phẩm:** Reploid #3 trên mặt phẳng của mỏm san hô thứ hai (mặt trên không có gai).
- **Lối ra:** khe vách phải ở đáy rãnh.

### R7 – Cửa cống (x 320–350, y 48–62) · độ khó 2
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss. Nước nông 3 ô.

### BOSS – Tidal Makkoeen (x 350–382, y 44–62)
- **Đấu trường 28 ô**, nửa dưới ngập nước (sâu 6 ô). Hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (sóng thần, bắn băng, lướt trên mặt nước).
- **Pha 2** (dưới 50% HP):
  - **Nước dâng ngập toàn sân** trong 4 giây.
  - Người chơi nhảy cao hơn nhưng di chuyển chậm hơn. Makkoeen bơi nhanh gấp đôi.
  - Các khối băng Makkoeen bắn ra trôi lên trần, thành bệ tạm 5 giây.
- Điểm yếu giữ nguyên theo dữ liệu game.

---

## 3. Bảng vật phẩm và kẻ địch

| Loại | Số lượng | Vị trí |
|---|---|---|
| Sniper | 4 | R1, R3, R4, R6 |
| Drone | 7 | R1, R2 ×2, R3, R5 ×2, R6 |
| Brute | 1 | R4 |
| Mini-boss | 1 | MID |
| Reploid cứu | 4 | R2, R4, R6, R7 |
| Heart Tank | 1 | R5 |
| Sub-Tank | 1 | R4 |
| Capsule Falcon Head | 1 | R3 |
| Công tắc | 2 | R4 ×2 |
| Checkpoint | 2 | R4, R6 |

Tổng 12 kẻ địch thường (bản cũ: 20 con xếp đều), đặt có chủ đích theo mục đích từng phòng.

---

## 4. Những gì engine cần bổ sung

1. Vùng nước: trọng lực ×0.32, tốc độ rơi tối đa giảm, nhảy ở mặt nước giữ độ cao nhảy dưới nước.
2. Mực nước thay đổi được theo công tắc (vùng nước có độ cao động).
3. Dòng chảy: vùng đẩy theo hướng, tốc độ tăng dần theo vị trí.
4. Thủy lôi: nổ chậm 1 giây khi chạm hoặc bị bắn, bán kính 2 ô.
5. Tua-bin hút (vùng chết ở đầu ống).
6. Mini-boss Tàu ngầm U-555 bơi trong nước, mực nước hạ theo máu.

## 5. Danh sách hình cần vẽ

- **Tileset "Cảng" (Area 1):** 47 ô viền bê tông ướt, cầu tàu, hành lang căn cứ có cửa sổ tròn.
- **Tileset "Đáy biển" (Area 2):** 47 ô viền, ống thép, san hô gai (trần và sàn), đá rong.
- **Vật thể:** thủy lôi (3 khung nhấp nháy), tua-bin (4 khung), công tắc bơm (2 trạng thái), mặt nước động (4 khung), bọt khí.
- **Nền:** Area 1: biển đêm và hải đăng (2 lớp parallax). Area 2: tia sáng xuyên nước và đàn cá xa (2 lớp).

**Hướng phối hợp:** như màn mẫu — dựng bằng khối màu tạm theo sơ đồ để chơi thử, chốt cảm giác rồi mới thay tile thật.
