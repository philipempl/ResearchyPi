#!/usr/bin/python
# -*- coding:utf-8 -*-
from scholarly import scholarly
import sys
import os
import argparse
#picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'module')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("ResearchyPi 2022")

    epd = epd2in13_V2.EPD()
    epd.init(epd.FULL_UPDATE)

    logging.info("Loading Google Scholar stats...")

    parser = argparse.ArgumentParser(description='ResearchyPi.')
    parser.add_argument("id", help="Google Scholar identifier")
    args = parser.parse_args()

    author = scholarly.search_author_id(args.id)
    author = scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])

    author_name = author['name']
    author_hindex = "H-Index: "+ str(author['hindex'])
    author_cites = "Cites: "+ str(author['citedby'])
    author_pubs = "Paper: " + str(len(author['publications']))

    # Drawing on the image
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

    # read bmp file on window
    logging.info("Display stats")
    # epd.Clear(0xFF)
    image1 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    bmp = Image.open(os.path.join(picdir, 'scholar-icon.bmp'))
    image1.paste(bmp, (0,25))
    draw = ImageDraw.Draw(image1)
    draw.text((80, 2), author_name, font = font24, fill = 0)
    draw.line([(80,30),(240,30)], fill = 0,width = 4)
    draw.text((80, 40), author_pubs, font = font24, fill = 0)
    draw.text((80, 65), author_cites, font = font24, fill = 0)
    draw.text((80, 90), author_hindex, font = font24, fill = 0)
    epd.display(epd.getbuffer(image1))

    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in13_V2.epdconfig.module_exit()
    exit()
