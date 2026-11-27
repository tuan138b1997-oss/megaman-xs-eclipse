# Bắc Cực — Boss Blizzard Wolfang

`x6_wolfang` · chủ đề `ice` · Act II · X6 · tổng chiều ngang khoảng 324 ô (10368px)

![Sơ đồ](maps/x6_wolfang.png)

## Ý tưởng
Area 1 là chặng Ride Chaser trượt dốc tuyết bị tuyết lở đuổi; Area 2 là vách băng cao, sàn trơn và băng rơi.

## Tham khảo
X6 North Pole Area, X4 Frost Walrus, X8 Avalanche Yeti (bản demake làm lại thành màn chơi thường).

## Chuẩn kích thước
Theo màn mẫu Lò Nham Thạch: khung hình 640×360 px = 20×11.25 ô; hành lang trần→sàn 9 ô, khối trần luôn nằm trong khung; phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô (hai hành lang chồng nhau); đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô, leo bằng đá tường và kệ nghỉ. X nhảy cao ~2.6 ô (vy 520), xa ~5 ô: gờ trên đường chính ≤ 2.5 ô, hố ≤ 4 ô; cao/xa hơn phải dùng đá tường, lướt-nhảy hoặc giáp, và chỉ dùng cho bí mật.

## Nhịp màn
R1 (1) → R2 (5) → MID (2) → R3 (5) → R4 (4) → R5 (2) → BOSS (6)

## Kịch bản từng phòng

### R1 – Trạm trượt (30×9 ô, đi ngang) · độ khó 1
Lên Ride Chaser.
- **Đặt trong phòng:** Ride Armor / Chaser

### R2 – Dốc tuyết lở (130×22 ô, đi xuống) · độ khó 5
Ride Chaser xuống dốc dài; tuyết lở đuổi phía sau, nhảy qua khe băng, né cây thông đổ.
- **Bẫy:** tuyết lở
- **Đặt trong phòng:** Drone, Drone, Reploid

### MID – Trạm khí tượng (24×9 ô, đi ngang) · độ khó 2
Checkpoint, xuống xe.
- **Đặt trong phòng:** Checkpoint

### R3 – Vách băng cao (20×46 ô, leo dọc) · độ khó 5
Bám tường băng X=3850 (trơn, trượt nhanh hơn); Blade Body ở hốc cao.
- **Bẫy:** băng rơi
- **Đặt trong phòng:** Drone, Capsule giáp

### R4 – Hồ băng (60×9 ô, đi ngang) · độ khó 4
Sàn băng trơn, băng nhọn rơi từ trần theo nhịp; Heart Tank trên tảng băng trôi.
- **Bẫy:** sàn trơn
- **Đặt trong phòng:** Sniper, Brute, Heart Tank

### R5 – Hang băng (30×9 ô, đi ngang) · độ khó 2
Phòng nghỉ, Sub-Tank, cửa boss.
- **Đặt trong phòng:** Sub-Tank, Reploid

### BOSS – Blizzard Wolfang (30×11 ô, đấu trường) · độ khó 6
Sàn đấu đóng băng dần (trơn), sói phóng băng.
- **Bẫy:** sàn trơn
- **Đặt trong phòng:** Boss

## Bí mật và vật phẩm
| Vật phẩm | Phòng | Cách lấy |
|---|---|---|
| Capsule Blade Body | R3 | Vách băng cao. |
| Heart Tank | R4 | Tảng băng trôi. |
| Sub-Tank | R5 | Hang băng. |

## Cơ chế mới cần engine
- Tường băng trượt nhanh
- Tuyết lở đuổi khi đang cưỡi Ride Chaser

## Hình ảnh / element
terrain-ice/cap-ice, native-ice, mmx6-ice, mmx6_invertediceblocks.
