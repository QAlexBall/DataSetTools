import os
from shutil import copyfile

def extract(imgpath, txtpath, new_image_path, new_txt_path):		# 将已经打上标签的txt复制到一个新的目录
	imgfile = os.listdir(imgpath)
	imgfile.sort()

	txtfile = os.listdir(txtpath)
	txtfile.sort()

	for i in range(0, len(txtfile)):
		with open(os.path.join(txtpath + txtfile[i]),  encoding='gb2312') as txt:
			filename = os.path.join(txtpath + txtfile[i])
			new_name = os.path.join(new_txt_path + str(i) + '?' + txtfile[i])
			first_char = txt.read(1)
			if first_char:
				if int(first_char) > 0:
					print(first_char)
					copyfile(filename, new_name)

					txt_find = txtfile[i].split('.')
					img_name = os.path.join(imgpath + txt_find[0] + '.jpg')
					new_img_name = os.path.join(new_image_path + str(i) + '?' + txt_find[0] + '.jpg')
					copyfile(img_name, new_img_name)
	
def new_name(new_image_path, new_txt_path):
	images = os.listdir(new_image_path)
	for i in range(0, len(images)):
		image_name = images[i].split('.')
		print(os.path.join(new_image_path + image_name[0]))
		print(os.path.join(new_image_path + str(i) + '.jpg'))

		os.rename(os.path.join(new_image_path + image_name[0] + '.jpg'), 
					os.path.join(new_image_path + str(i) + '.jpg'))
		os.rename(os.path.join(new_txt_path + image_name[0] + '.txt'),
					os.path.join(new_txt_path + str(i) + '.txt'))

def main():
	imgpath = 'all_images/'			# 图片路径
	txtpath = 'all_labels/'			# lables
	new_txt_path = '/home/alex/SummerWP2018/DataSets/pr_data/TextFile/' # 已经打上标签txt的路径
	new_image_path = '/home/alex/SummerWP2018/DataSets/pr_data/ImageSet/'


	# extract(imgpath, txtpath, new_image_path, new_txt_path)
	# new_name(new_image_path, new_txt_path)

if __name__ == '__main__':
	main()