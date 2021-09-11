from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageFont

from statistics import mean

import os
import csv
import re

files_path = "static/source_images"
header = ['week','height','image']
data = []
counter = 0

def process(file_name):
    print("Filter image to find edges")
    #read from existing image
    image = Image.open(files_path + "/" + file_name)
    final = image.filter(ImageFilter.FIND_EDGES)
    final.save("static/processed_images/" + file_name)

def analyse(file_name):
    print("Analyse pixels of the image")
    #open the outlined version of the image
    image2 = Image.open('static/processed_images/' + file_name)
    pixels = list(image2.getdata())
    width, height = image2.size

    list_of_y = []

    for y in range(height):
        for x in range(width):
            pixel_to_scan = image2.getpixel((x,y))
            if pixel_to_scan != (0,0,0) and pixel_to_scan != (255,255,255):
            
                if mean(pixel_to_scan)>30 and mean(pixel_to_scan)<200: #within the range of desired intensity
                    print("(" + str(x) + "," +  str(y) + ")=" + str(image2.getpixel((x,y))))
                    list_of_y.append(y)

    line_y = list(set(list_of_y))[0]

    print("Show the processed image")
    draw = ImageDraw.Draw(image2)
    draw.line((0,line_y, width, line_y), fill=128)
    image2.show()

    image = Image.open(files_path + "/" + file_name)
    draw = ImageDraw.Draw(image)
    draw.line((0,line_y, width, line_y), fill=128)
    pixel_height = height-line_y
    pixel_cm = round(pixel_height / 13)
    text_to_display = "Current height = " + str(pixel_height) + " pixels "
    draw.text((5, line_y),text_to_display,fill=(255,0,0))
    image.show()

    print("Workout the height of the object")
    image.save("static/result_images/" + file_name)

    print("Saved and show the new image")
    week_no = re.findall(r'\d+', file_name)
    row = [int(week_no[0]),pixel_cm, file_name]
    data.append(row)
    
for filename in os.listdir(files_path):
    process(filename)
    analyse(filename)

data.sort()
print("Sorted the heights data")

with open('static/heights.csv','w',encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
print("Saved height data into CSV")

