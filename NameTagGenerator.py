from PIL import Image, ImageDraw, ImageFont
first_name = "Rafid"
last_name = "Dewan"
university = "Carleton Univeristy"
program = "Software Engineering"
imageName = 'School-Name-Tag'
img = Image.open(imageName + '.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 28, encoding="unic")
draw.text((100, 60),first_name + " " + last_name,(0,0,0),font = font)
draw.text((40,90), university, (0,0,0), font = font)
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 25, encoding ="unic")
draw.text((40,125), program, (0,0,0), font = font)
img.show()
img.save('Test/{}.jpg'.format(first_name + "_" + last_name + "_" + university + "_" + program))