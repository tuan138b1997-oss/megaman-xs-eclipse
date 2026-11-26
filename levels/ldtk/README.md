# Project LDtk (LDtk 1.5.3)

Mỗi màn có một file `<id>.ldtk`, mở bằng [LDtk](https://ldtk.io) (miễn phí). Bố cục thế giới **Free**: mỗi phòng của kịch bản là một Level đặt đúng tọa độ (1 ô = 32px).
Hiện có 17 màn: Lò Nham Thạch (`x5_dinorex`), Intro, 7 màn boss X5 và 8 màn boss X6. 9 màn pháo đài được thêm ở đợt 3.

## Quy trình

1. Mở `levels/ldtk/<id>.ldtk` trong LDtk, chỉnh, lưu.
2. Trong `docs/level-design/campaign` chạy `python3 tools/import_ldtk.py <id>` → cập nhật `levels/data/<id>.json` và `levels/data/all.js`.
3. Bản web (`levels/runtime.js`) và Unity đọc dữ liệu đó. Lò Nham Thạch vẫn dùng builder riêng nên chưa nhập ngược.

Sinh lại toàn bộ file LDtk từ thiết kế gốc: `python3 tools/export_ldtk.py` (**ghi đè** chỉnh sửa trong LDtk — nhập ngược trước nếu cần giữ).
Mọi file sinh ra đều được kiểm tra bằng JSON schema chính thức LDtk 1.5.3.

## Lớp Collision (IntGrid, dùng chung mọi màn)

| Giá trị | Ý nghĩa |
|---|---|
| 1 | Đất đặc |
| 2 | Dốc 45° |
| 3 | Dốc 22.5° |
| 4 | Kệ một chiều |
| 5 | Sàn vỡ |
| 6 | Băng chuyền |
| 7 | Tường nứt |
| 8 | Trần bám được (trên vùng đảo trọng lực) |
| 9 | Dung nham / gai |

Auto-rule phủ tile `terrain-<chủ đề>` (assets/environments) lên ô 1, 2, 3, 7, 8 theo vị trí, nên mặt đất trong LDtk giống trong game.
Dốc (2, 3) cần thêm entity `Slope` để giữ đúng điểm đầu/cuối; ô 9 nên kèm `Hazard_Area` để chọn loại (lava/spike/thorn/acid), không có thì lấy theo chủ đề.

## Entity dùng chung

`PlayerSpawn, Checkpoint, Enemy_Sniper, Enemy_Drone, Enemy_Brute, NPC_Reploid, Item_Capsule (armor, part), Item_HeartTank, Item_SubTank, Item_Orb,
Hazard_Flame, Hazard_Press, Hazard_RollingRock, Hazard_Laser, Hazard_Elec, Hazard_LavaColumn, Hazard_Steam, Hazard_Mine, Hazard_Void, Hazard_Area,
Moving_Minecart, Platform_Moving, Platform_Lift, Platform_Phase (A/B), Platform_Bounce, Conveyor (speed), Slope,
Hazard_ChaseWall, Zone_RisingMagma, Zone_GravityFlip, Zone_Updraft, Zone_Water, Zone_Wind, Zone_Current, Zone_LowGravity, Zone_BlackHole, Zone_Slow, Zone_Dark,
Zone_AcidRain, Zone_Alarm, Zone_Mud, Zone_Ice, Zone_Electric, Switch (targets), Gate (kind, id), Wall_Breakable (breakBy), Portal (id, to, rush),
Turret, Vehicle (rideArmor/rideChaser), SubBoss (id, hp), BossGate`

Thuộc tính (nhịp `on/off/phase`, `speed`, `dir`, `armor/part`...) nằm trong Custom Fields. Ảnh đại diện entity lấy từ `assets/levels/ldtk/entity-icons.png` (khung đầu của sprite gốc X5/X6).
Level có field `code` (R1, MID, BOSS...), `difficulty`, `area` (1/2).
