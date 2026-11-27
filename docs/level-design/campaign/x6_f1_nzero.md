# Không gian ác mộng — Boss Nightmare Zero

`x6_f1_nzero` · chủ đề `shadow` · Phòng thí nghiệm Gate · tổng chiều ngang khoảng 244 ô (7808px)

![Sơ đồ](maps/x6_f1_nzero.png)

## Ý tưởng
Không gian nhiễu tối: tầm nhìn bị thu hẹp quanh nhân vật, đèn quét tạo ảo ảnh (bệ giả), bệ nhấp nháy và đảo trọng lực.

## Tham khảo
X6 Nightmare stages, X8 Dark Mantis (tối), X5 Zero Space 3.

## Chuẩn kích thước
Theo màn mẫu Lò Nham Thạch: khung hình 640×360 px = 20×11.25 ô; hành lang trần→sàn 9 ô, khối trần luôn nằm trong khung; phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô (hai hành lang chồng nhau); đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô, leo bằng đá tường và kệ nghỉ. X nhảy cao ~2.6 ô (vy 520), xa ~5 ô: gờ trên đường chính ≤ 2.5 ô, hố ≤ 4 ô; cao/xa hơn phải dùng đá tường, lướt-nhảy hoặc giáp, và chỉ dùng cho bí mật.

## Nhịp màn
R1 (5) → R2 (6) → MID (2) → R3 (6) → BOSS (7)

## Kịch bản từng phòng

### R1 – Hành lang nhiễu (60×11 ô, đi ngang, nhảy bệ) · độ khó 5
Tầm nhìn bán kính 220px; bệ ảo ảnh (viền nhấp nháy) không đứng được.
- **Bẫy:** tối
- **Đặt trong phòng:** Drone

### R2 – Bệ nhấp nháy (70×11 ô, đi ngang, nhảy bệ) · độ khó 6
Bệ đổi pha trên vực, đèn quét làm lộ bệ thật.
- **Bẫy:** vực
- **Đặt trong phòng:** Drone, Sniper

### MID – Điểm dừng (24×9 ô, đi ngang) · độ khó 2
Checkpoint.
- **Đặt trong phòng:** Checkpoint

### R3 – Đảo trọng lực (60×11 ô, đi ngang, nhảy bệ) · độ khó 6
Đi trên trần qua gai.
- **Bẫy:** gai, đảo trọng lực
- **Đặt trong phòng:** Drone

### BOSS – Nightmare Zero (30×11 ô, đấu trường) · độ khó 7
Bản sao Zero dùng Genmu Zero; đánh bại để mở khóa Zero thật.
- **Đặt trong phòng:** Boss

## Cơ chế mới cần engine
- Tầm nhìn hạn chế
- Bệ ảo ảnh

## Hình ảnh / element
bg-shadow tối, mmx6_cyberblock, vòng tối vẽ bằng mặt nạ canvas.
