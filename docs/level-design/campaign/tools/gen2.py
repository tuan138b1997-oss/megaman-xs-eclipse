# Sinh sơ đồ PNG + kịch bản .md cho các màn đã viết lại theo chuẩn màn mẫu.
# Chạy: python3 tools/gen2.py [id ...]   (từ thư mục docs/level-design/campaign)
import sys, os, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib import draw, write_md

ROOT = os.path.dirname(HERE)
ORDER = ['intro', 'x5_grizzly', 'x5_makkoeen', 'x5_kraken', 'x5_hotarunicus', 'x5_rosered', 'x5_necrobat', 'x5_pegacion']
ids = sys.argv[1:] or [s for s in ORDER if os.path.exists(os.path.join(HERE, 'stages', s + '.py'))]
os.makedirs(os.path.join(ROOT, 'maps'), exist_ok=True)
for sid in ids:
    st = importlib.import_module('stages.' + sid).STAGE
    size = draw(st, os.path.join(ROOT, 'maps', sid + '.png'))
    write_md(sid, st, os.path.join(ROOT, sid + '.md'), 'maps/' + sid + '.png')
    print(sid, size)
