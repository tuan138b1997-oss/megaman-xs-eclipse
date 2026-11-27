# Rừng đột biến — Boss Spike Rosered

`x5_rosered` · chủ đề `nature` · Act I · X5 · tổng chiều ngang khoảng 350 ô (11200px)

![Sơ đồ](maps/x5_rosered.png)

## Ý tưởng
Rừng nấm khổng lồ 2 tầng. Nấm đàn hồi bật người chơi lên tầng tán cây. Sub-boss dây leo chặn giữa màn, cuối màn leo thân cây cổ thụ.

## Tham khảo
X4 Web Spider (rừng, dây leo đu), X5 Spike Rosered, X6 Commander Yammark (2 tầng tách nhánh).

## Chuẩn kích thước
Theo màn mẫu Lò Nham Thạch: khung hình 640×360 px = 20×11.25 ô; hành lang trần→sàn 9 ô, khối trần luôn nằm trong khung; phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô (hai hành lang chồng nhau); đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô, leo bằng đá tường và kệ nghỉ. X nhảy cao ~2.6 ô (vy 520), xa ~5 ô: gờ trên đường chính ≤ 2.5 ô, hố ≤ 4 ô; cao/xa hơn phải dùng đá tường, lướt-nhảy hoặc giáp, và chỉ dùng cho bí mật.

## Nhịp màn
R1 (2) → R2 (3) → R3 (4) → MID (5) → R5 (4) → R6 (5) → R7 (2) → BOSS (6)

## Kịch bản từng phòng

### R1 – Bìa rừng (60×9 ô, đi ngang) · độ khó 2
Nấm đàn hồi đầu tiên (bật cao 900px/s), dạy nảy lên tầng trên.
- **Bẫy:** nấm bật
- **Đặt trong phòng:** Sniper, Drone

### R2 – Tầng nấm (70×17 ô, đi ngang, 2 tầng) · độ khó 3
Hai tầng song song: dưới nhiều địch, trên ít địch nhưng nhiều khe. Gai dây leo dưới đáy.
- **Bẫy:** gai
- **Đặt trong phòng:** Drone, Drone, Reploid

### R3 – Dây leo đu (50×11 ô, đi ngang, nhảy bệ) · độ khó 4
Dây leo đu qua vực (giữ nút nhảy để bám, thả để bay).
- **Bẫy:** vực
- **Đặt trong phòng:** Drone

### MID – Lõi dây leo (30×11 ô, đấu trường) · độ khó 5
Sub-boss Dây leo: 3 bông hoa phun gai, phải bắn theo thứ tự. Checkpoint sau trận.
- **Đặt trong phòng:** Mini-boss, Checkpoint

### R5 – Đầm lầy (60×11 ô, đi ngang, nhảy bệ) · độ khó 4
Bùn làm chậm 40%; bệ gỗ nổi chìm dần khi đứng lâu.
- **Bẫy:** bùn
- **Đặt trong phòng:** Sniper, Brute, Heart Tank

### R6 – Thân cây cổ thụ (20×44 ô, leo dọc) · độ khó 5
Leo thân cây X=4850 bằng đá tường + nấm; tán cây có capsule Gaea Foot.
- **Bẫy:** gai
- **Đặt trong phòng:** Drone, Capsule giáp, Sub-Tank

### R7 – Vườn hoa (30×9 ô, đi ngang) · độ khó 2
Phòng nghỉ, 2 Reploid, cửa boss.
- **Đặt trong phòng:** Reploid, Reploid

### BOSS – Spike Rosered (30×11 ô, đấu trường) · độ khó 6
Sàn có bụi gai mọc lại sau 4 giây; boss treo trên dây leo trần.
- **Bẫy:** gai
- **Đặt trong phòng:** Boss

## Bí mật và vật phẩm
| Vật phẩm | Phòng | Cách lấy |
|---|---|---|
| Capsule Gaea Foot | R6 | Tán cây cổ thụ (Falcon bay hoặc nấm + lướt trên không). |
| Heart Tank | R5 | Trên bệ gỗ cao nhất trước khi chìm. |
| Sub-Tank | R6 | Hốc thân cây giữa giếng. |

## Cơ chế mới cần engine
- Dây leo đu
- Bùn làm chậm
- Bệ gỗ chìm dần

## Hình ảnh / element
terrain-nature/cap-nature, prop-nature, nấm và dây leo vẽ mới; bụi gai dùng hazard spikes.
