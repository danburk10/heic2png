# batch convert HEIC to png
# from cli: ls -name *.HEIC | python .\io.py

# requires pillow, pillow_heif

import sys
from PIL import Image
import pillow_heif

pillow_heif.register_heif_opener()

for line in sys.stdin:
    filename = line.strip()
    img = Image.open(filename)
    img.save(filename+'.png', format('png'))
    img.close()
    
