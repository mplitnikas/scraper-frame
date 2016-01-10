import bs4
import requests
import json
import os

base_folder = 'pictures'

# settings to DL from Deviantart search pages
offset_dist = 24							# number of pics that fit into one 'screenful'
offsets_travel = 1							# go thru this many screens
search_url_base = 'http://www.deviantart.com/browse/all/customization/wallpaper/scenery/?order=9&offset='
oembed_base = 'http://backend.deviantart.com/oembed?url='
selector = 'span.shadow a'


try:
	os.makedirs(base_folder)
except OSError:
	pass


def get_link_urls(search_term):
	
	# this doesn't actually make use of the search term yet
	link_urls = []

	for current_offset in range(0, (offsets_travel * offset_dist), offset_dist):

		res = requests.get(search_url_base + str(current_offset))
		res.raise_for_status()
		soup = bs4.BeautifulSoup(res.text, 'lxml') # change to 'html5lib' on the pi

		link_objects = soup.select(selector)

		# Add title and link to a list for later
		for elem in link_objects:
			elem_url = elem.get('href')
			link_urls.append(elem_url)

	return link_urls
			

def get_json(link):
	oembed_url = oembed_base + link
	oembed_result = requests.get(oembed_url)
	return oembed_result.text

def get_image_url(link):
	json_text = json.loads(get_json(link))

	if 'fullsize_url' in json_text.keys():
		return json_text['fullsize_url']
	elif 'url' in json_text.keys():
		return json_text['url']
	else:
		return "\nURL NOT FOUND!!\n"

print "Getting search results..."
hrefs = get_link_urls('dummy search term')
print "done!"

image_urls = []
# turn search result urls into direct image urls
for search_result in hrefs:
	print "Finding image url for: %s" % search_result
	image_urls.append(get_image_url(search_result))

# download each image url into created folder
for image_url in image_urls:
	print "Downloading image %s..." % image_url
	image_path = os.path.join(base_folder, os.path.basename(image_url))
	
	if os.path.exists(image_path):
		print "already exists!"
		continue

	res = requests.get(image_url)
	res.raise_for_status()

	imageFile = open(image_path, 'wb')

	for chunk in res.iter_content(100000):
		imageFile.write(chunk)

	imageFile.close()
	print "done!"
