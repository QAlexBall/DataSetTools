from PIL import Image
import os

img_path = './ImageSet/'
txt_path = './TextFile/'
new_txt_path = './NewText/'
imgs = os.listdir(img_path)
imgs.sort()
for i in range(0, len(imgs)):
	img = os.path.join(img_path + imgs[i])
	txt_name = imgs[i].split('.')
	txt = os.path.join(txt_path + txt_name[0] + '.txt')
	new_txt = os.path.join(new_txt_path + txt_name[0] + '.txt')
	print(img, txt)
	im = Image.open(img)
	x = im.size[0]
	y = im.size[1]
	print(x, y)
	with open(txt) as t:
		num = t.readline()
		f = open(new_txt, "w")
		for j in range(0, int(num)):
			s = t.readline().split(' ')
			print(s)
			x1 = float(s[0]) * x
			y1 = float(s[1]) * y
			x2 = float(s[2]) * x
			y2 = float(s[3]) * y
			f.write((str(int(x1)) + ' ' + 
					 str(int(y1)) + ' ' + 
					 str(int(x2)) + ' ' + 
					 str(int(y2)) + ' ' + s[4]))
	f.close()
