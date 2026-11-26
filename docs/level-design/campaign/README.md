# Kịch bản & sơ đồ toàn chiến dịch

Màn mẫu đã duyệt: **Lò Nham Thạch** (`x5_dinorex`) — xem `lo-nham-thach-kich-ban.md`. 25 màn còn lại dùng cùng khung: phòng có mục đích rõ, mỗi màn 1 cơ chế chính + 1 phụ, đoạn dọc, checkpoint giữa, bí mật cần giáp/kỹ năng.

## Tiến độ làm lại theo chuẩn màn mẫu

Các màn dưới đây đã được **viết lại đầy đủ** như màn mẫu Lò Nham Thạch: sơ đồ có địa hình theo ô (nền, dốc, hố, giếng dọc, kệ, bẫy, đường đi chính và lối bí mật), kịch bản từng phòng có tọa độ và thông số nhịp, bảng vật phẩm/kẻ địch, phần engine cần bổ sung và danh sách hình cần vẽ.

| Đợt | Màn | Trạng thái |
|---|---|---|
| 1 | [Cao tốc Neo Arcadia](intro.md), [Tàu bọc thép](x5_grizzly.md), [Căn cứ đáy biển](x5_makkoeen.md), [Nhà máy điện](x5_kraken.md), [Phòng thí nghiệm Laser](x5_hotarunicus.md), [Rừng đột biến](x5_rosered.md), [Đài thiên văn](x5_necrobat.md), [Không quân](x5_pegacion.md) | Đã làm lại |
| 2 | 8 màn boss X6 | Chờ |
| 3 | 4 màn Zero Space (X5) + 5 màn Gate Lab (X6) | Chờ |

Công cụ: `tools/gen2.py` (dữ liệu từng màn ở `tools/stages/<id>.py`, bộ vẽ ở `tools/lib.py`). Các màn chưa làm lại vẫn dùng `tools/gen.py` cũ; `gen.py` tự bỏ qua màn đã có trong `tools/stages/`.

**Nguồn tham khảo:** không xem được video YouTube; các trang wiki và FAQ chi tiết bị chặn mạng trong môi trường này. Thiết kế dựa trên thông tin tóm tắt (tên màn, vật phẩm, cơ chế chính của X4/X5/X6/X8, bản X8 16-bit demake, X Corrupted) và dữ liệu `campaign-data.js`; bố cục là tự thiết kế, không chép bản đồ gốc.

## Danh sách màn

| Màn | Boss | Chủ đề | Cơ chế chính | Độ khó cao nhất | Bí mật |
|---|---|---|---|---|---|
| [Cao tốc Neo Arcadia](intro.md) | 1D-1000 → High Max | intro | Bảng chỉ dẫn nút, Tường bê tông phá bằng Ride Armor | 3 | 2 |
| [Tàu bọc thép](x5_grizzly.md) | Crescent Grizzly | metal | Khớp nối toa tách theo thời gian, Hầm thấp quét qua nóc tàu (phải cúi/lướt) | 5 | 3 |
| [Căn cứ đáy biển](x5_makkoeen.md) | Tidal Makkoeen | water | Công tắc rút/dâng mực nước, Dòng chảy ngang dưới nước | 5 | 3 |
| [Nhà máy điện](x5_kraken.md) | Volt Kraken | volt | Ride Chaser chạy tự do (không tự cuộn), Sàn điện theo nhịp | 5 | 3 |
| [Phòng thí nghiệm Laser](x5_hotarunicus.md) | Shining Hotarunicus | volt | Công tắc quang học, Gương xoay đổi hướng tia | 5 | 3 |
| [Rừng đột biến](x5_rosered.md) | Spike Rosered | nature | Dây leo đu, Bùn làm chậm | 5 | 3 |
| [Đài thiên văn](x5_necrobat.md) | Dark Necrobat | shadow | Khối nổi trôi chậm, Thấu kính đẩy lùi | 5 | 3 |
| [Không quân](x5_pegacion.md) | Spiral Pegacion | wind | Boong nghiêng theo nhịp, Khối mây cứng trôi | 5 | 3 |
| [Zero Space 1](x5_f1_dynamo.md) | Dynamo | shadow | Laser quét toàn màn hình + hốc trú ẩn | 6 | 0 |
| [Zero Space 2](x5_f2_shadow.md) | Shadow Devil | shadow | Chuỗi bệ đổi pha dài | 6 | 0 |
| [Zero Space 3](x5_f3_rangda.md) | Rangda Bangda W | shadow | Trọng lực đổi chiều theo nhịp trong giếng | 6 | 1 |
| [Zero Space Final](x5_f4_sigma.md) | Final Sigma W | core | Sàn sụp từng mảng trong trận boss | 6 | 0 |
| [Đền Inami](x6_turtloid.md) | Rainy Turtloid | nature | Mưa axit gây sát thương theo thời gian, Mái che an toàn | 5 | 4 |
| [Viện Laser](x6_sheldon.md) | Shield Sheldon | shadow | Tường giả đi xuyên được, Gương xoay bằng đạn | 5 | 3 |
| [Trung tâm vũ khí](x6_mijinion.md) | Infinity Mijinion | metal | Vòng ngắm Illumina, Bệ treo cáp đung đưa | 6 | 3 |
| [Khu Amazon](x6_yammark.md) | Commander Yammark | nature | Nhánh đường đi tách đôi, Khúc gỗ trôi | 5 | 3 |
| [Phòng thí nghiệm tái chế](x6_shark.md) | Metal Shark Player | metal | Tường ép đuổi tự cuộn, Tường rác phá bằng Ride Armor | 6 | 3 |
| [Khu dung nham](x6_heatnix.md) | Blaze Heatnix | fire | Bệ phản lực Thruster, Vòng lửa Donut | 6 | 3 |
| [Bắc Cực](x6_wolfang.md) | Blizzard Wolfang | ice | Tường băng trượt nhanh, Tuyết lở đuổi khi đang cưỡi Ride Chaser | 5 | 3 |
| [Bảo tàng Trung tâm](x6_scaravich.md) | Ground Scaravich | metal | Báo động khi bị đèn pha phát hiện, Cột Totem chặn đường | 5 | 3 |
| [Không gian ác mộng](x6_f1_nzero.md) | Nightmare Zero | shadow | Tầm nhìn hạn chế, Bệ ảo ảnh | 6 | 0 |
| [Phòng thí nghiệm Gate 1](x6_f2_nmother.md) | Nightmare Mother | fire | Bệ xoay quanh trục | 7 | 0 |
| [Phòng thí nghiệm Gate 2](x6_f3_highmax.md) | High Max | core | Totem chặn bệ | 7 | 0 |
| [Phòng thí nghiệm Gate 3](x6_f4_gate.md) | Gate | core | Tinh thể Nightmare nổ | 6 | 1 |
| [Phòng thí nghiệm cuối](x6_f5_bossrush.md) | 8 boss → Hell Sigma | core | Gai nhô theo nhịp trong trục rơi | 7 | 0 |

## Giáp / kỹ năng mở bí mật
| Màn | Bí mật | Cách lấy |
|---|---|---|
| Cao tốc Neo Arcadia | Capsule Fourth Armor (R5) | Dùng Ride Armor đấm vỡ tường tầng 2. |
| Tàu bọc thép | Capsule Falcon Foot (R5) | Cần Ride Armor từ R4. |
| Căn cứ đáy biển | Capsule Falcon Head (R3) | Đá tường trong nước lên hốc trần. |
| Nhà máy điện | Capsule Falcon Arm (R4) | Đỉnh tháp tụ điện. |
| Phòng thí nghiệm Laser | Capsule Falcon Body (R3) | Sau công tắc quang học #2. |
| Rừng đột biến | Capsule Gaea Foot (R6) | Tán cây cổ thụ (Falcon bay hoặc nấm + lướt trên không). |
| Đài thiên văn | Capsule Gaea Head (R4) | Đỉnh đài thiên văn cuối Area 1. |
| Không quân | Capsule Gaea Body (R5) | Boong trên cùng chiến hạm 4. |
| Zero Space 3 | Secret Capsule Ultimate X5 / Black Zero (R3) | Hốc trần trong vùng đảo trọng lực. |
| Đền Inami | Capsule Shadow Body (R4) | Mái đền tầng cao. |
| Viện Laser | Capsule Shadow Head (R4) | Xuyên tường giả ở tầng trên. |
| Trung tâm vũ khí | Capsule Blade Head (R4) | Bệ cáp cuối Area 2. |
| Khu Amazon | Capsule Blade Foot (R3a) | Nhánh trên. |
| Phòng thí nghiệm tái chế | Capsule Shadow Foot (R3) | Sau tường rác thứ 2. |
| Khu dung nham | Capsule Shadow Arm (R5) | Đỉnh trục leo dung nham. |
| Bắc Cực | Capsule Blade Body (R3) | Vách băng cao. |
| Bảo tàng Trung tâm | Capsule Blade Arm (R4) | Hốc cao Cell 2. |
| Phòng thí nghiệm Gate 3 | Secret Ultimate Armor (R1) | Trần biển gai trong vùng đảo trọng lực. |

## Nguồn tham khảo
Nguồn chính là mô tả cơ chế và vị trí capsule sẵn có trong dữ liệu dự án (`campaign-data.js`). Bổ sung thêm các mẫu thiết kế từ dòng X:
- [Mega Man X5 – Mega Man Wiki](https://megamanwiki.com/wiki/Mega_Man_X5), [X5 – MobyGames](https://www.mobygames.com/game/3790), [X5 walkthrough (video-games-museum)](https://video-games-museum.com/en/faqs/Playstation/28537-Mega-Man-X5.pdf)
- [Mega Man X6 – Mega Man Wiki](https://megamanwiki.com/wiki/Mega_Man_X6), [Inami Temple](https://mugen.fandom.com/wiki/Inami_Temple), [Weapon Center](https://megaman.fandom.com/wiki/Weapon_Center), [X6 hints (SuperCheats)](https://www.supercheats.com/playstation/mega-man-x6/14966/randomness/)
- [Mega Man X4 – MobyGames](https://www.mobygames.com/game/3136), [X4 hints (mmhp)](https://mmhp.net/GameHints/MMX4.html)
- [Mega Man X8 – TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/MegaManX8), [X8 review – GameSpot](https://www.gamespot.com/reviews/mega-man-x8-review/1900-6114749/), [X8 16-bit demake – Time Extension](https://www.timeextension.com/news/2024/09/mega-man-x8-has-just-got-a-free-16-bit-fan-demake)
- [Mega Man X Corrupted – TV Tropes](https://www.tvtropes.org/pmwiki/pmwiki.php/VideoGame/MegaManXCorrupted)

Bài học rút ra: X8 bị chê vì gimmick tự cuộn, gai và vực dày đặc, phải thử-sai nhiều. Màn được khen là màn có gimmick thật sự vui (Gravity Antonion) và có lối phụ cần thiết bị (Bamboo Pandamonium). Vì vậy bộ kịch bản này: không dùng màn tự cuộn bắt buộc (trừ đường hầm ép ở Recycle Lab), mọi bẫy chết ngay đều có báo trước, bí mật luôn gắn với giáp hoặc kỹ năng.
