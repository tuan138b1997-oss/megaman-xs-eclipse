# Căn cứ đáy biển — Boss Tidal Makkoeen

`x5_makkoeen` · chủ đề `water` · Act I · X5 · tổng chiều ngang khoảng 340 ô (10880px)

![Sơ đồ](maps/x5_makkoeen.png)

## Ý tưởng
Căn cứ chìm dưới biển: phần lớn màn ngập nước (trọng lực nhẹ, nhảy cao). Có đoạn mực nước rút/dâng theo công tắc, và tàu ngầm U-555 truy đuổi ở giữa màn.

## Tham khảo
X5 Tidal Makkoeen, X Launch Octopus/X3 Toxic Seahorse (nước + nhảy cao), X8 Bamboo Pandamonium (lối phụ cần thiết bị).

## Chuẩn kích thước
Theo màn mẫu Lò Nham Thạch: khung hình 640×360 px = 20×11.25 ô; hành lang trần→sàn 9 ô, khối trần luôn nằm trong khung; phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô (hai hành lang chồng nhau); đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô, leo bằng đá tường và kệ nghỉ. X nhảy cao ~2.6 ô (vy 520), xa ~5 ô: gờ trên đường chính ≤ 2.5 ô, hố ≤ 4 ô; cao/xa hơn phải dùng đá tường, lướt-nhảy hoặc giáp, và chỉ dùng cho bí mật.

## Nhịp màn
R1 (2) → R2 (3) → R3 (3) → MID (5) → R4 (4) → R5 (4) → R6 (2) → BOSS (6)

## Kịch bản từng phòng

### R1 – Bến tàu (50×11 ô, đi ngang, nhảy bệ) · độ khó 2
Trên mặt nước, sóng đẩy nhẹ. Nhảy xuống nước để thấy trọng lực nhẹ.
- **Đặt trong phòng:** Sniper, Drone

### R2 – Hành lang ngập (70×11 ô, đi ngang, nhảy bệ) · độ khó 3
Dưới nước: nhảy siêu cao lên kệ trần, cá máy (Drone nước) bơi zigzag.
- **Bẫy:** dòng chảy
- **Đặt trong phòng:** Drone, Drone, Reploid

### R3 – Trụ tường cao (20×40 ô, leo dọc) · độ khó 3
Giếng nước dọc; trọng lực nhẹ giúp đá tường lên trụ X=2350 → hốc trần chứa Falcon Head.
- **Đặt trong phòng:** Capsule giáp

### MID – Hầm tàu ngầm (30×11 ô, đấu trường) · độ khó 5
Sub-boss U-555 bắn ngư lôi; mực nước hạ dần để lộ điểm yếu.
- **Đặt trong phòng:** Mini-boss, Checkpoint

### R4 – Phòng bơm (50×11 ô, đi ngang, nhảy bệ) · độ khó 4
Bắn 2 công tắc bơm để rút nước → lối đi dưới đáy lộ ra (Sub-Tank). Rút nước thì mất nhảy cao.
- **Bẫy:** mực nước
- **Đặt trong phòng:** Công tắc, Công tắc, Sub-Tank

### R5 – Đường ống áp lực (60×11 ô, đi ngang, nhảy bệ) · độ khó 4
Ống xả bọt nước đẩy ngang; gai trên trần (nhảy cao quá là trúng).
- **Bẫy:** gai trần
- **Đặt trong phòng:** Drone, Sniper, Heart Tank

### R6 – Cửa cống (30×9 ô, đi ngang) · độ khó 2
Phòng nghỉ, Reploid, cửa boss.
- **Đặt trong phòng:** Reploid, Reploid

### BOSS – Tidal Makkoeen (30×11 ô, đấu trường) · độ khó 6
Đấu trường nửa ngập: Makkoeen trượt trên mặt nước, pha 2 nước dâng ngập toàn sân.
- **Bẫy:** nước
- **Đặt trong phòng:** Boss

## Bí mật và vật phẩm
| Vật phẩm | Phòng | Cách lấy |
|---|---|---|
| Capsule Falcon Head | R3 | Đá tường trong nước lên hốc trần. |
| Sub-Tank | R4 | Đáy lộ ra sau khi rút nước. |
| Heart Tank | R5 | Khe giữa hai dải gai trần — nhảy thấp. |

## Cơ chế mới cần engine
- Công tắc rút/dâng mực nước
- Dòng chảy ngang dưới nước

## Hình ảnh / element
terrain-water/cap-water, native-ice cho kệ kính, bg-water; bọt nước dùng lại fx-water.
