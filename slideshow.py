import os
import random
#import pygame
import webbrowser
import time

webbrowser._tryorder = ['firefox'] # debug - change this on the pi??

continue_loop = True

def is_valid_file(f, path_base):
	img_types = ['jpg', 'jpeg', 'png', 'bmp', 'gif', 'tif', 'tiff']
	filetype = f.split('.')[-1]
	img_path = os.path.join(path_base, f)
	return (os.path.isfile(img_path) and filetype in img_types)

# get pointed to a folder
def slideshow(folder, delay_time):
	path_base = os.path.join('.', folder)
	folder_contents = [f for f in os.listdir(path_base) if is_valid_file(f, path_base)]
	random.shuffle(folder_contents)

	for img_file in folder_contents:
		img_path = os.path.join(path_base, img_file)
		webbrowser.open(img_path)
		time.sleep(delay_time)


def loop(function):
	global continue_loop
	while continue_loop == True:
		function()

slideshow('deviantart', 5)

# open that folder (try/except)

# list all (image) files in that folder

# shuffle list

# display shuffled list one-by-one in pygame

# loop back to 7 until stopped/changed