import PIL
from PIL import Image
import os
import sys

mdpi = 48
hdpi = 72
xhdpi = 96
xxhdpi = 144
xxxhdpi = 192

if len(sys.argv) > 1:
	image_name = sys.argv[1]
	if not os.path.exists(image_name):
		print("[Error]: give Image does not exits")
		print("Failure")
		exit(0)
else:
	print("[Error]: Image name is missing")
	print("Failure")
	exit(0)
	
file_extension = os.path.splitext(image_name)[1]
folders = ('mipmap-mdpi', 'mipmap-hdpi', 'mipmap-xhdpi', 'mipmap-xxhdpi', 'mipmap-xxxhdpi')

''' For better result give square(M x M) Image and size greater or
	equal to 192px X 192'''

def resize_pic(size, folder_name):
	
	d = os.path.dirname('res/'+folder_name+'/ic_launcher' + file_extension)
	if not os.path.exists(d):
		os.makedirs(d)
	img = Image.open(image_name)
	if img.size[0] != img.size[1]:
		print("[Error]: Image hight & width are not equal. \nNote: Image hight and width should be equal")
		print("Failure")
		exit(0)
	wpercent = (size / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((size, hsize), PIL.Image.ANTIALIAS)
	img.save(d+'/ic_launcher'+ file_extension)


for fldr_name in folders :
	resize_pic(mdpi, fldr_name)
print("Success")