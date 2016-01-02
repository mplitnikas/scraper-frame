import bs4
import requests
import copy
import time
import os

offset_dist = 24	# number of pics that fit into one 'screenful'
offsets_travel = 1	# go thru this many screens
search_url_base = 'http://www.deviantart.com/browse/all/customization/wallpaper/scenery/?order=9&offset='
oembed_base = 'http://backend.deviantart.com/oembed?url='

pic_objects = []

# where do we set up the local storage path??

class Deviation(object):
	def __init__(self, json_info):
		self.json_info = json_info		# the base lump
		# carve up lump into attributes:
		# title, author, url, favorites
		# (who faved, using auth token)(later)
		# determine & store local path

def get_links():
	offset = 0
	for current_offset_batch in range(offsets_travel):

		res = requests.get(search_url_base + str(offset))
		res.raise_for_status()
		soup = bs4.BeautifulSoup(res.text, 'lxml')

		link_objects = soup.select('span.shadow a')

		# Add title and link to a dict for later
		for elem in link_objects:
			elem_url = elem.get('href')
			oembed_url = oembed_base + elem_url
			oembed_result = requests.get(oembed_url)

			print oembed_url
			# do request for json info page
			# create object using json info (what name)
			

		# move to next screenful down
		offset += offset_dist

get_links()

# for each link_url get JSON info and parse(for what)
	# for img url, title, author
	# can we use classes for the deviation item? (has title, author, link, faves, etc)
# go thru link urls and download to disk???

# generate a scrambled list

# ----should this be a diff module?----

# open image in a fullscreen browser??
# OR
# display it fullscreen for x seconds w other lib

# either way, add title, author, page url to a log

# move to the next image (fade effect)

# consider a pandora/netflix like recommendation system based on other faves
# https://www.deviantart.com/developers/http/v1/20151202/deviation_whofaved/5ce9c928e5ffa60a7b9790165855aa90