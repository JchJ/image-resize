#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image


def imageresize():
	img = Image.open("")
	img.size
	img = img.resize(("x","y"),Image.ANTIALIAS)
	img.save("",optimize=True,quality=85)

imageresize()
