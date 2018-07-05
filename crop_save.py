import os
from PIL import Image

image_path = 'demo/'
path = 'results/'
path_list = os.listdir(path)

for i in path_list:
	if os.path.splitext(i)[1] == '.jpg':
		with Image.open(image_path + i) as image:
			txt = i.split('.')
			os.mkdir('cropImage/' + i)
			with open(path + 'res_' + txt[0] + '.txt') as t:
				a = len(t.readlines())
			with open(path + 'res_' + txt[0] + '.txt') as t:
				for j in range(a):
					coordinate = t.readline()
					coordinate = coordinate.split(',')
					x0 = int(coordinate[0])
					y0 = int(coordinate[1])
					x1 = int(coordinate[2])
					y1 = int(coordinate[3])
					region = image.crop((x0, y0, x1, y1))
					region.save('./cropImage/' + i + '/' + txt[0] + '___' + str(j) + '.jpg')