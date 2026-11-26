# Màn: TRUNG TÂM VŨ KHÍ (Weapons Center — Boss Infinity Mijinion)

Bản thiết kế để duyệt trước khi dựng. Sơ đồ: `maps/x6_mijinion.png`.
Màn này thay cho `x6_mijinion` hiện tại. Boss, capsule Blade Head, phi thuyền Illumina khóa mục tiêu, bệ dây cáp và lõi cáp ở mid-gate vẫn giữ; thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.

![Sơ đồ](maps/x6_mijinion.png)

---

## 0. Công cụ và quy ước

Dùng chung với màn mẫu (`../lo-nham-thach-kich-ban.md`, mục 0): LDtk dựng bản đồ, Pixelorama vẽ tile, Krita vẽ nền parallax. 1 ô = 32px, khung hình 30×17 ô, các lớp `Collision` / `Tiles` / `Decor` / `Foreground` / `Entities`.

---

## 1. Ý tưởng tổng

Căn cứ vũ khí nằm dưới bóng phi thuyền khổng lồ Illumina. Khi ở ngoài trời, người chơi **luôn bị ngắm bắn**. Cả màn xoay quanh việc di chuyển liên tục, dùng chỗ nấp và vượt vực trên bệ treo cáp.

- **Area 1 – Bến và kho (ngoài trời):** thép xám, bầu trời có phi thuyền chiếm nửa nền. Dạy tâm ngắm, chỗ nấp bị phá, bệ treo cáp.
- **Area 2 – Xưởng và vực lớn:** trong xưởng có băng chuyền và tay ép, rồi ra vực cáp lớn với tâm ngắm bắn 2 phát.
- **Điểm nhấn trải nghiệm:** né tâm ngắm → nấp sau thùng → đi cáp qua vực → leo tháp nạp đạn → phá lõi cáp → băng chuyền và tay ép → vực cáp lớn dưới hỏa lực → boss phân thân
- **Đường cong độ khó:** 2 → 3 → 4 → 4 → (mini-boss) → 5 → 7 → 6 → 2 → boss (thang 10).
- **Thời lượng mục tiêu:** khoảng 6–8 phút lần đầu, khoảng 3 phút khi đã quen.

Các mẫu thiết kế tham khảo (không chép bản đồ gốc):

- **X6, màn Infinity Mijinion:** phi thuyền Illumina ở nền khóa mục tiêu, bệ dây cáp trên vực, lõi cáp ở mid-gate.
- **X8, màn Gigabolt Man-O-War:** hỏa lực từ vật thể khổng lồ ở nền.
- **X5, màn Spiral Pegacion:** vượt vực trên bệ chạy theo đường cố định.
- **X Corrupted:** cơ chế gây nguy hiểm cũng dùng được để tấn công (dụ pháo bắn địch).

---

## 2. Kịch bản từng phòng

Tọa độ tính theo ô, gốc (0,0) ở góc trên trái thế giới, y tăng xuống dưới.

### R1 – Bến vũ khí (x 0–50, y 50–66) · độ khó 2
- **Mục đích:** giới thiệu **tâm ngắm Illumina**. Phi thuyền khổng lồ ở nền xa khóa mục tiêu vào người chơi.
- **Cơ chế – tâm ngắm:**
  - Một vòng ngắm đỏ bám theo X, mất 2 giây để khóa (vòng thu nhỏ dần, tiếng bíp nhanh dần).
  - Khóa xong thì 0.5 giây sau một tia pháo bắn xuống đúng chỗ đó, rộng 3 ô.
  - Chạy đổi hướng hoặc lướt ra khỏi vòng là né được. Nấp sau thùng thép thì tâm ngắm mất dấu.
  - Chu kỳ 6 giây một lần.
- **Địa hình:** bến cảng 50 ô, mặt sàn ở y 62. 2 thùng thép làm chỗ nấp.
- **Địch:** 1 Drone đầu bến, 1 Sniper cuối bến.

### R2 – Kho tên lửa (x 50–120, y 50–66) · độ khó 3
- **Mục đích:** nấp và tiến lên trong khi tâm ngắm phá dần chỗ nấp.
- **Địa hình:** kho 70 ô, 4 chồng thùng làm vật che.
- **Cơ chế:** tia pháo của Illumina **phá được thùng**. Nấp quá lâu ở một chỗ thì mất chỗ nấp đó.
- **Địch:**
  - 1 Brute giữa kho.
  - 1 Sniper cuối kho.
- **Vật phẩm:** Reploid #1 sau chồng thùng thứ nhất.
- **Mẹo:** dụ tia pháo bắn trúng Brute: pháo gây sát thương cho cả địch.

### R3 – Vực cáp 1 (x 120–180, y 48–70) · độ khó 4
- **Mục đích:** lần đầu đi trên **bệ treo cáp** qua vực.
- **Địa hình:** vực rộng 48 ô, rơi là mất mạng. Một sợi cáp chạy ngang trên cao.
- **Cơ chế – bệ treo cáp:**
  - 4 bệ treo dưới cáp, trượt qua lại 6 ô và đung đưa nhẹ (lệch 1 ô).
  - Tâm ngắm vẫn hoạt động. Đứng yên trên bệ để chờ là bị khóa.
- **Địch:** 2 Drone.
- **Lối phụ (Heart Tank):**
  - Một gờ thép nhỏ dưới tầm bệ thứ hai, gần đáy vực (x ≈ 146, y ≈ 64).
  - Thả người từ bệ thứ hai xuống gờ và lấy Heart Tank.
  - Gờ không có vách để đá tường: phải chờ bệ thứ ba trượt tới gần rồi nhảy lên.

### R4 – Tháp nạp đạn (x 180–202, y 12–62) · độ khó 4
- **Mục đích:** đoạn dọc trong nhà, thoát khỏi tâm ngắm (không có tầm nhìn ra trời).
- **Địa hình:** tháp rộng 18 ô, cao 46 ô (từ y 60 lên y 14). 4 kệ zigzag.
- **Bẫy:** một băng tải đạn chạy ngang giữa tháp có dòng điện chạy dọc, bật 1 giây, tắt 2 giây.
- **Địch:** 1 Drone.
- **Vật phẩm:** Reploid #2 trên kệ cao nhất.

### Mini-boss – Lõi cáp Illumina (x 202–232, y 6–22) · độ khó 5
- **Đấu trường 26 ô**, kín, hai vách đá tường được.
- **Lõi cáp Illumina** treo giữa trần, nối với 4 sợi cáp năng lượng chạy xuống sàn.
- **Đòn đánh:**
  - Mỗi sợi cáp phóng điện theo thứ tự, cột điện rộng 2 ô.
  - Lõi bắn tia xuống theo tâm ngắm (như R1, nhưng khóa trong 1.5 giây).
- **Điểm yếu:** phá 4 sợi cáp (mỗi sợi 3 phát) thì lõi rơi xuống sàn 4 giây, lúc đó mới đánh lõi được.
- **Phần thưởng:** tắt tâm ngắm trong khu xưởng tiếp theo. Hạ không mất máu thì được thưởng Souls.

### R5 – Xưởng lắp ráp (x 232–296, y 8–22) · độ khó 5
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** băng chuyền xuôi chiều kết hợp tay ép, trong nhà (không còn tâm ngắm).
- **Địa hình:** xưởng 64 ô, 2 đoạn băng chuyền đẩy sang phải 100px/giây.
- **Bẫy – tay ép:** 2 tay ép thủy lực trên băng chuyền: chờ 1.2 giây, đập 0.3 giây. Băng chuyền đẩy người chơi vào tay ép nên phải canh nhịp.
- **Địch:** 1 Brute giữa hai băng chuyền, 1 Sniper cuối xưởng.
- **Vật phẩm:** Reploid #3 cuối băng chuyền thứ nhất.
- **Lối phụ (Sub-Tank):** một cánh tay robot nâng hàng (bệ di động lên xuống) ở giữa xưởng. Đứng lên tay robot lúc nó lên cao nhất rồi nhảy sang kệ hàng phía trên (x ≈ 285, y ≈ 12).

### R6 – Vực cáp lớn (x 296–366, y 4–28) · độ khó 7
- **Mục đích:** cao trào của màn. Vực cáp dài 58 ô (khoảng 1.850px) với 7 bệ cáp, tâm ngắm trở lại mạnh hơn.
- **Cơ chế:**
  - 7 bệ treo cáp trượt lệch pha nhau, tốc độ tăng dần từ bệ đầu tới bệ cuối.
  - **Tâm ngắm khóa nhanh hơn (1.5 giây) và bắn 2 phát liền.** Phải nhảy sang bệ khác ngay khi vòng ngắm bắt đầu thu nhỏ.
- **Địch:**
  - 1 Drone bay ngang tầm bệ thứ hai.
  - 1 Drone bay lên từ đáy vực.
- **Lối phụ (Capsule Blade Head):**
  - Một bệ thép cao gần cuối vực (x ≈ 348, y ≈ 7), cao hơn mọi bệ cáp.
  - Nhảy từ bệ cáp thứ sáu lúc nó trượt sang phải hết cỡ, rồi lướt trên không mới tới.
  - Giáp Blade lướt trên không 2 lần nên dễ hơn.

### R7 – Phòng điều khiển pháo (x 366–418, y 8–22) · độ khó 6
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** kết hợp: tâm ngắm đôi, chỗ nấp ít dần.
- **Địa hình:** sân thượng 52 ô, ngoài trời, 3 bệ thép thấp làm chỗ nấp.
- **Cơ chế:** **2 tâm ngắm** cùng lúc, khóa lệch nhau 1 giây. Phải di chuyển liên tục giữa các chỗ nấp.
- **Địch:** 1 Sniper cuối sân thượng, đứng trên bệ cao.

### R8 – Hầm chỉ huy (x 418–448, y 8–22) · độ khó 2
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss.

### BOSS – Infinity Mijinion (x 448–480, y 4–20)
- **Đấu trường 28 ô**, mở trời, hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (phân thân, Ground Dash, nhảy bật).
- **Pha 2** (dưới 50% HP):
  - **Tâm ngắm Illumina** trở lại, khóa vào người chơi mỗi 8 giây.
  - Tia pháo cũng xóa phân thân của Mijinion: dụ tâm ngắm vào đám phân thân là cách dọn sân nhanh.
- Điểm yếu giữ nguyên theo dữ liệu game.

---

## 3. Bảng vật phẩm và kẻ địch

| Loại | Số lượng | Vị trí |
|---|---|---|
| Sniper | 4 | R1, R2, R5, R7 |
| Drone | 6 | R1, R3 ×2, R4, R6 ×2 |
| Brute | 2 | R2, R5 |
| Mini-boss | 1 | MID |
| Reploid cứu | 4 | R2, R4, R5, R8 |
| Heart Tank | 1 | R3 |
| Sub-Tank | 1 | R5 |
| Capsule Blade Head | 1 | R6 |
| Checkpoint | 2 | R5, R7 |

Tổng 12 kẻ địch thường (bản cũ: 20 con xếp đều), đặt có chủ đích theo mục đích từng phòng.

---

## 4. Những gì engine cần bổ sung

1. Tâm ngắm bám người chơi, khóa theo thời gian, mất dấu khi nấp sau vật che; tia pháo phá vật che và gây sát thương cả địch.
2. Bệ treo cáp: trượt dọc cáp và đung đưa.
3. Tay ép thủy lực theo nhịp trên băng chuyền.
4. Cánh tay robot nâng hàng (bệ lên xuống).
5. Mini-boss Lõi cáp: phá 4 cáp thì lõi rơi.

## 5. Danh sách hình cần vẽ

- **Tileset "Bến vũ khí" (Area 1):** 47 ô viền thép, thùng thép (3 trạng thái hư hại), cáp và bệ treo.
- **Tileset "Xưởng" (Area 2):** 47 ô viền, băng chuyền, tay ép (3 khung), kệ hàng.
- **Vật thể:** vòng tâm ngắm (4 khung thu nhỏ), tia pháo (3 khung), lõi cáp.
- **Nền:** Area 1: phi thuyền Illumina chiếm nửa trời (2 lớp parallax). Area 2: dây chuyền lắp ráp (2 lớp).

**Hướng phối hợp:** như màn mẫu — dựng bằng khối màu tạm theo sơ đồ để chơi thử, chốt cảm giác rồi mới thay tile thật.
