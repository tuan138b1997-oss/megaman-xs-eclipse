# Khu Amazon — Boss Commander Yammark

`x6_yammark` · chủ đề `nature` · Act II · X6 · tổng chiều ngang khoảng 280 ô (8960px)

![Sơ đồ](maps/x6_yammark.png)

## Ý tưởng
Rừng mưa 2 tầng tách nhánh ở checkpoint giữa: nhánh trên (tán cây) có Blade Foot, nhánh dưới (hang) có Heart Tank.

## Tham khảo
X6 Amazon Area, X4 Web Spider, X8 Bamboo Pandamonium (rẽ nhánh).

## Chuẩn kích thước
Theo màn mẫu Lò Nham Thạch: khung hình 640×360 px = 20×11.25 ô; hành lang trần→sàn 9 ô, khối trần luôn nằm trong khung; phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô (hai hành lang chồng nhau); đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô, leo bằng đá tường và kệ nghỉ. X nhảy cao ~2.6 ô (vy 520), xa ~5 ô: gờ trên đường chính ≤ 2.5 ô, hố ≤ 4 ô; cao/xa hơn phải dùng đá tường, lướt-nhảy hoặc giáp, và chỉ dùng cho bí mật.

## Nhịp màn
R1 (2) → R2 (3) → MID (2) → R3a (5) → R3b (4) → R4 (2) → BOSS (6)

## Kịch bản từng phòng

### R1 – Bìa rừng mưa (60×9 ô, đi ngang) · độ khó 2
Côn trùng máy bay theo đàn, cây gãy làm cầu.
- **Đặt trong phòng:** Drone, Drone, Sniper

### R2 – Bờ sông (60×11 ô, đi ngang, nhảy bệ) · độ khó 3
Khúc gỗ trôi trên sông làm bệ di động.
- **Bẫy:** sông
- **Đặt trong phòng:** Drone, Reploid

### MID – Ngã ba (30×9 ô, đi ngang) · độ khó 2
Checkpoint. Lối lên (tán cây) và lối xuống (hang).
- **Đặt trong phòng:** Checkpoint

### R3a – Nhánh trên: tán cây (70×11 ô, đi ngang, nhảy bệ) · độ khó 5
Lá lớn làm bệ nảy, gió lay cành; capsule Blade Foot X=4550.
- **Bẫy:** vực
- **Đặt trong phòng:** Drone, Capsule giáp

### R3b – Nhánh dưới: hang (70×9 ô, đi ngang) · độ khó 4
Hang tối, côn trùng phát sáng; Heart Tank cuối hang.
- **Bẫy:** tối
- **Đặt trong phòng:** Sniper, Brute, Heart Tank

### R4 – Đền lá (30×9 ô, đi ngang) · độ khó 2
Hai nhánh nhập lại; Sub-Tank, Reploid, cửa boss.
- **Đặt trong phòng:** Sub-Tank, Reploid, Reploid

### BOSS – Commander Yammark (30×11 ô, đấu trường) · độ khó 6
Boss gọi 3 chuồn chuồn vệ tinh xoay quanh.
- **Đặt trong phòng:** Boss

## Bí mật và vật phẩm
| Vật phẩm | Phòng | Cách lấy |
|---|---|---|
| Capsule Blade Foot | R3a | Nhánh trên. |
| Heart Tank | R3b | Nhánh dưới. |
| Sub-Tank | R4 | Đền lá. |

## Cơ chế mới cần engine
- Nhánh đường đi tách đôi
- Khúc gỗ trôi

## Hình ảnh / element
terrain-nature, prop-nature, bg-nature; lá nảy dùng bounce zone có sẵn.
