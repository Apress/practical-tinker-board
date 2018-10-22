#!/usr/bin/env python

import epd2in13
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pyowm
import math

epd = epd2in13.EPD()

owm = pyowm.OWM('insert_API_key_here')

def main():
    
    epd.init(epd.lut_full_update)

    while (True):

        observation = owm.weather_at_place('New York,US') #  define location 

        w = observation.get_weather() #  pull data

        print w.get_status() #  print forecast status
        
        w.get_temperature('fahrenheit')['temp'] #  get temperature
        temp = str(math.trunc(w.get_temperature('fahrenheit')['temp'])) #  get temperature minus decimal as a string
        print w.get_temperature('fahrenheit') #  print full temperature data, can also just print temp
           
        image = Image.new('1', (250, 128), 255)  # set resolution for horizontal orientation
        draw = ImageDraw.Draw(image) #  setup 
        font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 24)
        font2 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 24)
        font3 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansBoldOblique.ttf', 18)
        
        draw.rectangle((0, 0, 250, 128), fill = 255) #  border rectangle
        draw.text((7, 5), time.strftime('%a. %b. %d, %Y'), font = font3, fill = 0) #  date (ex: Mon. Jan. 1, 2018)
        draw.text((170, 5), time.strftime('%l:%M%p'), font = font3, fill = 0) #  time (ex: 12:00AM)
        
        draw.line((250, 25, 0, 25), fill = 0) # top horizontal line
        draw.line((170, 0, 164, 25), fill = 0) #  vertical line that divides date/time
        
        draw.text((30, 35), 'Weather:', font= font2, fill = 0) #  "Weather:"
        draw.text((170, 35), w.get_status(), font = font, fill = 0) #  forecast data

        draw.text((5, 85), 'Temperature:', font = font2, fill = 0) #  "Temperature:"
        draw.text((182, 85), temp + chr(176) + 'F', font = font, fill = 0) #  temp minus decimal with the degree and F
        
        draw.line((164, 25, 164, 128), fill = 0) # vertical dividing line
        draw.line((250, 70, 0, 70), fill = 0) #  horizontal dividing line
        
        epd.clear_frame_memory(0xFF)
        epd.set_frame_memory(image.transpose(Image.ROTATE_270), 0, 0) # rotate image to view horizontallyc
        epd.display_frame()

        epd.delay_ms(2000)

        # for partial update
        epd.init(epd.lut_partial_update)
    
        epd.set_frame_memory(image.transpose(Image.ROTATE_270), 0, 0) #  send new data to both memory 
        epd.display_frame()
        epd.set_frame_memory(image.transpose(Image.ROTATE_270), 0, 0)
        epd.display_frame()

if __name__ == '__main__':
    main()
