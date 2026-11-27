# Đền Inami — Boss Rainy Turtloid

`x6_turtloid` · chủ đề `nature` · Act II · X6 · tổng chiều ngang khoảng 340 ô (10880px)

![Sơ đồ](maps/x6_turtloid.png)

## Ý tưởng
Ngôi đền cổ dưới cơn mưa axit xanh: đứng ngoài mưa mất máu từ từ, 8 mái che trụ đá là điểm an toàn. Có lối rẽ Nightmare Zero.

## Tham khảo
X6 Inami Temple (mưa axit), X4 Web Spider (rừng/đền), X8 Bamboo Pandamonium (lối phụ).

## Chuẩn kích thước
Theo màn mẫu Lò Nham Thạch: khung hình 640×360 px = 20×11.25 ô; hành lang trần→sàn 9 ô, khối trần luôn nằm trong khung; phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô (hai hành lang chồng nhau); đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô, leo bằng đá tường và kệ nghỉ. X nhảy cao ~2.6 ô (vy 520), xa ~5 ô: gờ trên đường chính ≤ 2.5 ô, hố ≤ 4 ô; cao/xa hơn phải dùng đá tường, lướt-nhảy hoặc giáp, và chỉ dùng cho bí mật.

## Nhịp màn
R1 (3) → R2 (4) → R3 (4) → MID (2) → R4 (5) → R5 (4) → R6 (2) → BOSS (6)

## Kịch bản từng phòng

### R1 – Cổng đền (50×9 ô, đi ngang) · độ khó 3
Mưa axit bắt đầu; mái che đầu tiên dạy cách trú.
- **Bẫy:** mưa axit
- **Đặt trong phòng:** Sniper, Drone

### R2 – Sân đá (70×9 ô, đi ngang) · độ khó 4
Chạy giữa các mái che trụ đá; Nightmare Virus bay chậm.
- **Bẫy:** mưa axit
- **Đặt trong phòng:** Drone, Drone, Reploid

### R3 – Bậc đền (20×30 ô, leo dọc) · độ khó 4
Leo bậc đá có mái hiên; bắn công tắc #1 mở cổng đền.
- **Bẫy:** mưa axit
- **Đặt trong phòng:** Công tắc, Sniper

### MID – Chính điện (30×9 ô, đi ngang) · độ khó 2
Trong nhà, hết mưa; checkpoint.
- **Đặt trong phòng:** Checkpoint

### R4 – Mái đền (60×9 ô, đi ngang) · độ khó 5
Đi trên mái tầng 2 X=3740: capsule Shadow Body phía trên Heart Tank.
- **Bẫy:** mưa axit
- **Đặt trong phòng:** Drone, Capsule giáp, Heart Tank

### R5 – Hành lang tượng (50×9 ô, đi ngang) · độ khó 4
Tượng đá phun axit theo nhịp; cổng Alt Path dẫn tới Nightmare Zero.
- **Bẫy:** axit phun
- **Đặt trong phòng:** Sniper, Brute, Reploid

### R6 – Hồ sen (30×9 ô, đi ngang) · độ khó 2
Phòng nghỉ, Sub-Tank dưới mặt hồ, cửa boss.
- **Đặt trong phòng:** Sub-Tank, Reploid

### BOSS – Rainy Turtloid (30×11 ô, đấu trường) · độ khó 6
Mưa axit trong đấu trường theo đợt; mai rùa phản đạn khi thu mình.
- **Bẫy:** mưa axit
- **Đặt trong phòng:** Boss

## Bí mật và vật phẩm
| Vật phẩm | Phòng | Cách lấy |
|---|---|---|
| Capsule Shadow Body | R4 | Mái đền tầng cao. |
| Heart Tank | R4 | Dưới mái, cạnh capsule. |
| Sub-Tank | R6 | Dưới mặt hồ sen. |
| Alt Path Nightmare Zero | R5 | Cổng tím cuối hành lang. |

## Cơ chế mới cần engine
- Mưa axit gây sát thương theo thời gian
- Mái che an toàn

## Hình ảnh / element
terrain-nature, prop-nature, mmx6_totem_gate cho cổng, mưa vẽ bằng hạt.
