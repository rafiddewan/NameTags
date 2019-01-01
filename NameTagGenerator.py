from PIL import Image, ImageDraw, ImageFont
import csv
import random

def createNameTag(title, colour, first_name, last_name, institution,occupation, id):
  img = Image.open(title + '.jpg')
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 28, encoding="unic")
  draw.text((100, 60),first_name + " " + last_name,(0,0,0),font = font)
  draw.text((40,90), institution, colour, font = font)
  font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 25, encoding ="unic")
  draw.text((40,125), occupation, colour, font = font)
  filename = first_name + "_" + last_name + "_" + institution + "_" + str(id)
  img.save('Test/{}.jpg'.format(filename))
  return

def idMaker():
  id = random.randint(1,351)
  with open('id.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
      if(line_count == 0 and row == ''):
        break;
      elif row == str(id):   
        idMaker()
  with open('id.csv', mode='w') as id_file:
    id_writer = csv.writer(id_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    id_writer.writerow(str(id))
  return id


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
    id = idMaker();
    createNameTag(title, colour, first_name, last_name, institution, occupation, id)