import sys
import os
import argparse
import logging
from PIL import Image, ImageDraw, ImageFont

picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "resources")
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "module")

if os.path.exists(libdir):
    sys.path.append(libdir)

from scholarly import scholarly
from waveshare_epd import epd2in13_V2

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("ResearchyPi 2022")

    # initilaizing epaper display
    logging.info("Initializing...")
    epd = epd2in13_V2.EPD()
    epd.init(epd.FULL_UPDATE)

    # parsing scholar id argument
    parser = argparse.ArgumentParser(description="ResearchyPi")
    parser.add_argument("id", help="Google Scholar identifier")
    args = parser.parse_args()

    # loading scholar stats
    logging.info("Loading Google Schoalr stats...")
    result = scholarly.search_author_id(args.id)
    author = scholarly.fill(
        result, sections=["basics", "indices", "counts", "publications"]
    )
    author_name = author["name"]
    author_publications = "Articles: " + str(len(author["publications"]))
    author_citations = "Citations: " + str(author["citedby"])
    author_hindex = "H-Index: " + str(author["hindex"])

    # drawing on epaper display
    logging.info("Drawing stats on display...")
    font20 = ImageFont.truetype(os.path.join(picdir, "Font.ttc"), 20)
    font22 = ImageFont.truetype(os.path.join(picdir, "Font.ttc"), 22)
    image = Image.new("1", (epd.height, epd.width), 255)
    bmp = Image.open(os.path.join(picdir, "scholar-icon.bmp"))
    image.paste(bmp, (0, 0))
    draw = ImageDraw.Draw(image)
    draw.text((80, 2), author_name, font=font22, fill=0)
    draw.line([(80, 30), (240, 30)], fill=0, width=4)
    draw.text((80, 40), author_publications, font=font20, fill=0)
    draw.text((80, 65), author_citations, font=font20, fill=0)
    draw.text((80, 90), author_hindex, font=font20, fill=0)
    epd.display(epd.getbuffer(image))
    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in13_V2.epdconfig.module_exit()
    exit()
