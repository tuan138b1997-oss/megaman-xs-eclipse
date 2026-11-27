# Khu dung nham — Boss Blaze Heatnix

`x6_heatnix` · chủ đề `fire` · Act II · X6 · tổng chiều ngang khoảng 294 ô (9408px)

![Sơ đồ](maps/x6_heatnix.png)

## Ý tưởng
Khu núi lửa hoạt động: 3 cỗ máy vòng lửa Nightmare Donut, bệ phản lực Thruster, cuối màn là trục leo dọc dung nham. Dùng lại bộ element màn Lò Nham Thạch nhưng nhịp khác.

## Tham khảo
X6 Magma Area, X4 Magma Dragoon (nham dâng), màn mẫu Lò Nham Thạch.

## Chuẩn kích thước
Theo màn mẫu Lò Nham Thạch: khung hình 640×360 px = 20×11.25 ô; hành lang trần→sàn 9 ô, khối trần luôn nằm trong khung; phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô (hai hành lang chồng nhau); đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô, leo bằng đá tường và kệ nghỉ. X nhảy cao ~2.6 ô (vy 520), xa ~5 ô: gờ trên đường chính ≤ 2.5 ô, hố ≤ 4 ô; cao/xa hơn phải dùng đá tường, lướt-nhảy hoặc giáp, và chỉ dùng cho bí mật.

## Nhịp màn
R1 (3) → R2 (4) → R3 (5) → MID (2) → R4 (5) → R5 (6) → R6 (2) → BOSS (6)

## Kịch bản từng phòng

### R1 – Miệng hố (60×11 ô, đi ngang, nhảy bệ) · độ khó 3
Mưa đá lửa nhỏ, hố nham. Dạy bệ Thruster đầu tiên.
- **Bẫy:** nham
- **Đặt trong phòng:** Sniper, Drone

### R2 – Donut #1 (30×11 ô, đấu trường) · độ khó 4
Nightmare Donut #1 bắn vòng lửa; bệ Thruster ở hai bên.
- **Đặt trong phòng:** Mini-boss, Reploid

### R3 – Sông nham (70×11 ô, đi ngang, nhảy bệ) · độ khó 5
Bệ đá trôi trên sông nham, cột lửa phun theo nhịp.
- **Bẫy:** nham
- **Đặt trong phòng:** Drone, Drone

### MID – Hang mát (24×9 ô, đi ngang) · độ khó 2
Checkpoint.
- **Đặt trong phòng:** Checkpoint

### R4 – Donut #2 (30×11 ô, đấu trường) · độ khó 5
Donut #2 + đá lăn.
- **Đặt trong phòng:** Mini-boss, Heart Tank

### R5 – Trục leo dung nham (20×50 ô, leo dọc) · độ khó 6
Leo trục X=5250, nham dâng chậm; Donut #3 ở giữa trục. Shadow Arm ở đỉnh.
- **Bẫy:** nham dâng
- **Đặt trong phòng:** Mini-boss, Capsule giáp

### R6 – Đỉnh núi (30×9 ô, đi ngang) · độ khó 2
Phòng nghỉ, Sub-Tank, cửa boss.
- **Đặt trong phòng:** Sub-Tank, Reploid

### BOSS – Blaze Heatnix (30×11 ô, đấu trường) · độ khó 6
Nham lấp nửa dưới đấu trường ở pha 2.
- **Bẫy:** nham
- **Đặt trong phòng:** Boss

## Bí mật và vật phẩm
| Vật phẩm | Phòng | Cách lấy |
|---|---|---|
| Capsule Shadow Arm | R5 | Đỉnh trục leo dung nham. |
| Heart Tank | R4 | Sau Donut #2. |
| Sub-Tank | R6 | Đỉnh núi. |

## Cơ chế mới cần engine
- Bệ phản lực Thruster
- Vòng lửa Donut

## Hình ảnh / element
Toàn bộ element màn Lò Nham Thạch (terrain-fire, lv-fireball, lv-crusher...), sub "donut" có sẵn.
