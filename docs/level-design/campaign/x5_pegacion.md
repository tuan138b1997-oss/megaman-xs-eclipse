# Không quân — Boss Spiral Pegacion

`x5_pegacion` · chủ đề `wind` · Act I · X5 · tổng chiều ngang khoảng 370 ô (11840px)

![Sơ đồ](maps/x5_pegacion.png)

## Ý tưởng
Chiến dịch trên không: nhảy giữa 4 chiến hạm đang bay, quạt khí nâng giữa các hạm, pháo đài bay hộ tống làm sub-boss.

## Tham khảo
X5 Spiral Pegacion, X2 Wire Sponge/X3 Blast Hornet (trên cao), X8 Optic Sunflower (bệ di động).

## Nhịp màn
R1 (2) → R2 (3) → R3 (4) → MID (5) → R4 (5) → R5 (5) → R6 (2) → BOSS (6)

## Kịch bản từng phòng

### R1 – Đường băng cất cánh (50×16 ô, đi ngang) · độ khó 2
Gió ngang nhẹ, máy bay địch cất cánh lao thấp.
- **Đặt trong phòng:** Sniper, Drone

### R2 – Chiến hạm 1 (60×18 ô, đi ngang) · độ khó 3
Boong có tháp pháo; cuối hạm là quạt nâng (updraft) đưa sang hạm 2.
- **Bẫy:** updraft
- **Đặt trong phòng:** Drone, Sniper, Reploid

### R3 – Giữa trời (50×30 ô, đi ngang) · độ khó 4
Khối mây cứng trôi + updraft; rơi = mất một mạng nên có lưới an toàn ở đoạn đầu.
- **Bẫy:** vực
- **Đặt trong phòng:** Drone, Drone

### MID – Pháo đài hộ tống (30×17 ô, đấu trường) · độ khó 5
Sub-boss pháo đài bay; Heart Tank X=3950 ở boong sau khi hạ. Checkpoint.
- **Đặt trong phòng:** Mini-boss, Checkpoint, Heart Tank

### R4 – Chiến hạm 3 (60×18 ô, đi ngang) · độ khó 5
Boong nghiêng theo nhịp (nhân vật trượt nhẹ); khối blocks rơi.
- **Bẫy:** boong nghiêng
- **Đặt trong phòng:** Sniper, Brute, Reploid

### R5 – Chiến hạm 4 (60×18 ô, đi ngang) · độ khó 5
Cưỡi quạt nâng lên boong trên cùng: capsule Gaea Body cuối hạm.
- **Bẫy:** updraft
- **Đặt trong phòng:** Drone, Capsule giáp, Sub-Tank

### R6 – Cầu chỉ huy (30×16 ô, đi ngang) · độ khó 2
Phòng nghỉ, Reploid, cửa boss.
- **Đặt trong phòng:** Reploid, Reploid

### BOSS – Spiral Pegacion (30×17 ô, đấu trường) · độ khó 6
Đấu trên boong mở, gió xoáy đẩy người chơi về mép.
- **Bẫy:** gió
- **Đặt trong phòng:** Boss

## Bí mật và vật phẩm
| Vật phẩm | Phòng | Cách lấy |
|---|---|---|
| Capsule Gaea Body | R5 | Boong trên cùng chiến hạm 4. |
| Heart Tank | MID | Boong pháo đài sau khi hạ sub-boss. |
| Sub-Tank | R5 | Dưới cánh hạm, cần lướt trên không. |

## Cơ chế mới cần engine
- Boong nghiêng theo nhịp
- Khối mây cứng trôi

## Hình ảnh / element
terrain-wind/cap-wind, mmx5_spiralpegacionplane cho chiến hạm nền, mmx6-platform cho bệ trôi.
