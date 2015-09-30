

#   nw2s::bmptoc - an open source rocket launch control and telemetry system
#   Copyright (C) 2015 Scott Wilson (thomas.scott.wilson@gmail.com)
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Note that the image should be 240x320 (portrait)

from PIL import Image
from string import Template
import sys

ROWSIZE = 20

# Convert 24 bit RGB to 16 bit 565 format
def to565(pixel) :
    
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    
    return ((r & 0x00F8) << 8) | ((g & 0x00FC) << 3) | ((b & 0x00F8) >> 3)


# MAIN
# MAIN
# MAIN

# Load image from command line
if len(sys.argv) < 2: 

    print 'No input file provided'
    exit()

# Open the source image
img = Image.open(sys.argv[1])
imgdata = list(img.getdata())

# Get the name of the file
imgname = sys.argv[1].split('.')[0].split('/')[1]

# Print out a bit of info
print 'Image name:   {0}'.format(imgname)
print 'Image size:   {0}'.format(img.size)
print 'Image format: {0}'.format(img.format)

# Open the template
templatefile = open("template.txt", "r")
template = Template(templatefile.read())

# Build the template parameter list
data = {}
data['imgname'] = imgname
data['imgnamecaps'] = imgname.upper()
data['imglen'] = img.size[0] * img.size[1]
data['imgdata'] = ',\n\t'.join([', '.join(['0x{:04X}'.format(to565(x)) for x in imgdata[y : y + ROWSIZE]]) for y in xrange(0, len(imgdata), ROWSIZE)])

# Open the the text file
outputfile = open(imgname + ".cpp", "w")

outputfile.write(template.substitute(data))
outputfile.close()



