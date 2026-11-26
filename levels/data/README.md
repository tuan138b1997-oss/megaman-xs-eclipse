# Dữ liệu màn chơi (định dạng trung lập)

Mỗi màn thiết kế lại có một file `<id>.json`, sinh tự động từ `docs/level-design/campaign/tools/stages/<id>.py` bằng
`python3 tools/export_levels.py [id ...]` (chạy trong `docs/level-design/campaign`). **Không sửa tay file JSON**: sửa file thiết kế rồi xuất lại.

- `all.js` gộp mọi màn vào `window.LEVEL_DATA` cho bản web; `levels/runtime.js` dựng màn từ dữ liệu này.
- Unity (và engine khác) đọc thẳng các file `.json`. Lò Nham Thạch (`x5_dinorex`) vẫn dùng `../lo-nham-thach.level.json`.

## Quy ước

- Đơn vị: **ô 32px**. Gốc (0,0) ở góc trên trái thế giới, y tăng xuống dưới. Hình chữ nhật dùng `x, y, w, h`.
- Đấu trường boss luôn là phòng cuối: `width` = mép phải đấu trường, `floorBoss` = mặt sàn boss, `bossGateX` = chỗ kích hoạt boss.
- `theme` là chủ đề hình ảnh của game (`intro, fire, ice, water, nature, wind, metal, volt, shadow, core`): dùng `terrain-<theme>`, `cap-<theme>`, `bg-<theme>`, `prop-<theme>` trong `assets/environments/`. Phòng `area: 2` (sau mini-boss) dùng nền kim loại `native-panel`.

## Các trường

| Trường | Nội dung |
|---|---|
| `rooms[]` | `code, name, x, y, w, h, area (1/2), kind (room/mini/boss), difficulty`. Camera khóa trong phòng chứa người chơi. |
| `checkpoints[]` | `x, y` (y = mặt sàn). Phần tử đầu là điểm xuất phát. |
| `solids[]` | Khối đặc: `x, y, w, h, area`. |
| `slopes[]` | Dốc: `x0, y0, x1, y1, bottom` (đi được, phần dưới đặc tới `bottom`). |
| `ledges[]` | Bệ một chiều cao 0.5 ô: `x, y, w, kind`. `kind`: `shelf` (thường), `safe`, `move` (qua lại ±3 ô), `thrust` (lên xuống ±3 ô), `break` (sập 0.5s, hồi 4s), `bounce` (nấm bật), `holo` / `holoB` (bệ 2 pha, đổi pha mỗi 2.2s, ngược nhau). |
| `conveyors[]` | `x, y, w, speed` (px/s, âm = đẩy sang trái). |
| `hazards[]` | `type, x, y, w, h, on, off, phase, column`. `type`: `lava, acid, void` (rơi = mất máu, về chỗ an toàn), `spike, thorn` (giáp Shadow miễn), `elec, laser, fire, steam` (bật `on` giây / tắt `off` giây), `trash` (khối nghiền), `mine` (nổ lan bán kính 2 ô, hồi 4s). |
| `zones[]` | `type, x, y, w, h, label` (+ `dx, dy, strength` cho gió/dòng chảy). `type`: `water` (trọng lực ×0.5, chậm), `ice` (trơn), `mud`, `slow`, `wind`, `current`, `updraft`, `flip` (đảo trọng lực), `flipcycle` (đảo mỗi 4s), `lowgrav` (×0.42), `well` (hút về tâm), `dark` (tầm nhìn 8 ô), `rain` (mưa axit theo nhịp trong `label`), `alarm` (đèn pha quét, phát hiện thì báo động), `elec`. |
| `walls[]` | `type, x, y, w, h`. `stone` (phá bằng đạn nạp đầy), `steel` (Ride Armor đấm), `laser` / `gate` (tắt/mở bằng công tắc), `orbgate` (mở khi nhặt đủ quả năng lượng). |
| `switches[]` | `x, y, targets[]` (chỉ số trong `walls`). Bắn trúng là bật vĩnh viễn. |
| `portals[]` | `x, y, room, to` (chỉ số cổng đích) hoặc `rush` (màn cuối: 8 cổng boss rush). Tương tác bằng E. |
| `enemies[]` | `type (sniper/drone/brute), x, y` (y = chân). |
| `items[]` | `type (rescue/relic/tank/capsule/orb), id, x, y` (+ `armor, part` cho capsule). |
| `turrets[]` | Tháp pháo/ống phun bắn được: `x, y, hp`. |
| `vehicles[]` | `type (mech = Ride Armor, chaser = Ride Chaser chạy tự do), x, y`. |
| `subBoss` | `id (donut/truck/submarine/illumina), x, y, hp, room, gate{x,y,w,h}` — cổng mở khi hạ mini-boss. |
| `palette` | Màu nền phòng theo Area (`bg1, bg2, rock1, rock2`). |

## Element mới

Hình element dùng chung ở `assets/levels/common/el-*.png` (vẽ bằng `docs/level-design/campaign/tools/draw_elements.py`, xem trước ở `docs/level-design/campaign/elements-preview.png`). Ảnh nhiều khung xếp ngang, 1 ô = 16px gốc, phóng ×2 khi vẽ.
