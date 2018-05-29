import os
import random

list1=[]

for i in range(65, 65+26):
      list1.append(chr(i)) # List to generate Capital Alphabets

list2=[]
for j in range(48,48+10):
		list2.append(chr(j))   # List to generate Integers between 0-9

list3=list1+list2         # List of alpha-numeric characters
#listd = random.choice(listd)
#listdig = ['1','2','3','4','5','6','7',8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

blur_list =['0x1','0x1','0x4','0x3','0x2']  #  List amount of blurr

blur_e = random.choice(blur_list) #Randomly choose Amount of blurr

GN = random.randint(0,1)    # Generate randomly Noise parameter for Gaussian Noise
rot = random.randint(0,45)  #Generate randomly rotation for test between (0-45 degrees)


#List of 25 Fonts available in ImageMagick 

listFont = ['AvantGarde-Book','AvantGarde-BookOblique','AvantGarde-Demi'
   'AvantGarde-DemiOblique',
  'Bookman-Demi',
   'Bookman-DemiItalic',
   'Bookman-Light',
   'Bookman-LightItalic',
   'Courier',
   'Courier-Bold',
   'Courier-BoldOblique',
  'Courier-Oblique',
   'fixed',
  'Helvetica',
   'Helvetica-Bold',
   'Helvetica-BoldOblique',
'Helvetica-Narrow',
   'Helvetica-Narrow-Bold',
  'Helvetica-Narrow-BoldOblique',
   'Helvetica-Narrow-Oblique',
  'Helvetica-Oblique',
   'NewCenturySchlbk-Bold',
  'NewCenturySchlbk-BoldItalic',
  'NewCenturySchlbk-Italic',
   'NewCenturySchlbk-Roman',]

listf =random.choice(listFont) # Randomly choose Font
gravity =['south','north','east'] # randomly place the Text in Image


list_files=(os.listdir('/home/krutika/Downloads/background_images/check'))
list_files = ['/home/krutika/Downloads/background_images/check/' + x for x in list_files]




# Resize Background Images tp 32 cross 32 pixels as required
# Command Required [convert image.jpg -resize 600x400\> image.jpg] where the image is resized and overriden


for i in range(0,len(list_files)):
		command ="magick convert "+ str(list_files[i])+ " -resize 32x32\! "+ str(list_files[i])
		print(command)ssss
		os.system(str(command))

# To generate images with a random font and a random Background
## sample code [magick convert image.jpg -fill Black -font Courier-Oblique -weight 50 -pointsize 12 -gravity center -blur 0x8 -evaluate Gaussian-noise 1.2  -annotate 0+0 "Some text" output_image
# show me how the above finla command works
#convert koala.gif  -rotate   0  rotate_0.gif]


## Add noise between 1-1.5(Gaussian Noise)
## Keep all colors of font as white ******


for i in range(0,len(list3)):
	for j in range(0,1000):
		list_filernd = random.choice(list_files)
		command =  "magick convert " + str(list_filernd) + " -fill White -font "+ \
            str(listf) + " -weight 200 -pointsize 12 -gravity south " + "-blur " + str(blur_e) \
+ " -evaluate Gaussian-noise " + str(GN) +  " " + " -annotate +0+0 "+  str(list3[i]) + " " + "output_file"+str(i)+".jpg"
		os.system(str(command))
		

# Weight = 200
# gravity = To place text randomly at any location in Image
#GN = Amount of Random Gaussian Noise
# Magick convert = command line convert() command










