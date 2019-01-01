from PIL import Image, ImageDraw, ImageFont
img = Image.open('School-Name-Tag.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 28, encoding="unic")
draw.text((100, 60),"Rafid Dewan",(0,0,0),font=font)
draw.text((40,90), "Carleton University", (0,0,0), font =font)
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 25, encoding="unic")
draw.text((40,125), "Software  Engineering", (0,0,0), font =font)
img.show();