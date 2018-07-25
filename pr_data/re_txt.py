import os
# txt_path = 'NewText/'
# count = 0
# i = 0
# txts = os.listdir(txt_path)
# txts.sort()
# for txt in txts:
# 	with open(txt_path + txt) as t:
# 		t_txt = txt.split('.')
# 		# print(t_txt[0] + '.jpg')
# 		img_names = os.walk(t_txt[0] + '.jpg')
# 		for img_name in img_names:
# 			for i in range(len(img_name)):
# 				i = i + 1
# 				count = count + 1
# 				label = t.readline().split(' ')
# 				print(label[4])
# print(count)
img_folders = './'
img_floder = os.listdir(img_folders)
img_floder.sort()
for txt_im in img_floder:
	txt = txt_im.split('.')
	file_txt_img = os.listdir(txt_im)
	print(len(file_txt_img))
	# print('./NewText/' + txt[0] + '.txt')
	with open('./NewText/' + txt[0] + '.txt') as t:
		for i in range(len(file_txt_img)):
			line = t.readline()
			line = line.split(' ')
			img_txt_name = txt_im + '/' + txt[0] + '___' + str(i) + '.txt'
			print(img_txt_name)
			with open(img_txt_name, 'w') as f:
				f.write(img_txt_name + ' ' + line[4] + '\n')

			print(line[4])