from PIL import Image, ImageDraw, ImageFont
import csv

def createNameTag(title, colour, first_name, last_name, institution,occupation):
  img = Image.open(title + '.jpg')
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 28, encoding="unic")
  draw.text((100, 60),first_name + " " + last_name,(0,0,0),font = font)
  draw.text((40,90), institution, colour, font = font)
  font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 25, encoding ="unic")
  draw.text((40,125), occupation, colour, font = font)
  img.save('Test/{}.jpg'.format(first_name + "_" + last_name + "_" + institution + "_" + occupation))
  return

title = 'Organizer'

colour = (0,0,0)
if((title != 'Organizer') and (title != 'Attendee') and (title != 'Volunteer')):
  colour = (255,255,255)

with open(title + ".csv") as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  for row in csv_reader:
    first_name = row[0]
    last_name = row[1]
    institution = row[2]
    occupation = row[3]
    createNameTag(title, colour, first_name, last_name, institution, occupation)