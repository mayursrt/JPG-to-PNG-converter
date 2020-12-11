import sys
import os
from PIL import Image

source=sys.argv[1]
destination=sys.argv[2]

if not os.path.exists(destination):
	 os.makedirs(destination)

for filename in os.listdir(source):
	img = Image.open(f'{source}{filename}')
	clean_name = os.path.splitext(filename)[0]
	img.save(f'{destination}{clean_name}.png')

print('all done')