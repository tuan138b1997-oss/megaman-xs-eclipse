# Phòng thí nghiệm Laser — Boss Shining Hotarunicus

`x5_hotarunicus` · chủ đề `volt` · Act I · X5 · tổng chiều ngang khoảng 324 ô (10368px)

![Sơ đồ](maps/x5_hotarunicus.png)

## Ý tưởng
Viện nghiên cứu quang học: tia laser đỏ chặn lối, phải bắn công tắc quang học để tắt. Nửa sau là bệ hologram nhấp nháy trên băng chuyền.

## Tham khảo
X5 Shining Firefly (laser + gương), X6 Shield Sheldon (laser phản xạ), X4 Cyber Peacock (bệ ảo).

## Chuẩn kích thước
Theo màn mẫu Lò Nham Thạch: khung hình 640×360 px = 20×11.25 ô; hành lang trần→sàn 9 ô, khối trần luôn nằm trong khung; phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô (hai hành lang chồng nhau); đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô, leo bằng đá tường và kệ nghỉ. X nhảy cao ~2.6 ô (vy 520), xa ~5 ô: gờ trên đường chính ≤ 2.5 ô, hố ≤ 4 ô; cao/xa hơn phải dùng đá tường, lướt-nhảy hoặc giáp, và chỉ dùng cho bí mật.

## Nhịp màn
R1 (2) → R2 (3) → R3 (4) → R4 (4) → MID (2) → R5 (5) → R6 (4) → BOSS (6)

## Kịch bản từng phòng

### R1 – Sảnh viện (50×9 ô, đi ngang) · độ khó 2
Laser đỏ quét chậm theo chiều dọc, dạy canh nhịp.
- **Bẫy:** laser quét
- **Đặt trong phòng:** Sniper, Drone

### R2 – Khoang quang học #1 (40×9 ô, đi ngang) · độ khó 3
Bắn công tắc #1 tắt cửa laser đầu tiên. Gương xoay đổi hướng tia.
- **Bẫy:** gương
- **Đặt trong phòng:** Công tắc, Sniper, Reploid

### R3 – Khoang quang học #2 (20×30 ô, leo dọc) · độ khó 4
Leo bệ cao X=2150 bắn công tắc #2 → tường laser tắt → buồng Falcon Body.
- **Bẫy:** laser
- **Đặt trong phòng:** Công tắc, Capsule giáp

### R4 – Khoang quang học #3 (40×9 ô, đi ngang) · độ khó 4
Công tắc #3 phải bắn khi đứng trong vùng an toàn giữa 2 tia quét.
- **Bẫy:** laser quét
- **Đặt trong phòng:** Công tắc, Drone, Heart Tank

### MID – Trạm làm mát (24×9 ô, đi ngang) · độ khó 2
Checkpoint.
- **Đặt trong phòng:** Checkpoint

### R5 – Bệ Hologram (70×11 ô, đi ngang, nhảy bệ) · độ khó 5
Bệ hologram hiện/tắt 2 pha (xanh/tím) trên vực; băng chuyền ở hai đầu.
- **Bẫy:** bệ nhấp nháy
- **Đặt trong phòng:** Drone, Drone, Reploid

### R6 – Dây chuyền thấu kính (50×9 ô, đi ngang) · độ khó 4
Băng chuyền đôi chạy ngược chiều nhau, thấu kính rơi từ trần.
- **Bẫy:** băng chuyền
- **Đặt trong phòng:** Sniper, Brute, Sub-Tank

### BOSS – Shining Hotarunicus (30×11 ô, đấu trường) · độ khó 6
Đấu trường tối; boss tạo phân thân ánh sáng, gương ở 2 góc phản xạ đạn của người chơi.
- **Đặt trong phòng:** Boss

## Bí mật và vật phẩm
| Vật phẩm | Phòng | Cách lấy |
|---|---|---|
| Capsule Falcon Body | R3 | Sau công tắc quang học #2. |
| Heart Tank | R4 | Trên cụm gương, bắn công tắc từ dưới. |
| Sub-Tank | R6 | Cuối băng chuyền đôi. |

## Cơ chế mới cần engine
- Công tắc quang học
- Gương xoay đổi hướng tia
- Bệ hologram 2 pha

## Hình ảnh / element
terrain-volt, native-cyberblock + mmx5_cyberblock cho bệ hologram, fx-laser cho tia, gương vẽ mới (2 khung).
