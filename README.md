# bmp2c
This is a pretty simple python script that will take a 24 bit color bitmap and convert it to a 565 format byte array that can be used for the ILI9341 and most other similar 16 bit color displays. I've written it to use PIL, but it may work with the standard python library. 


	$ python bmp2c.py infile.bmp
