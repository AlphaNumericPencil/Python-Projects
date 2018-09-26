# pyex9.py
# use python2

import re
import urllib2


url = urllib.urlopen("http://www.monmouth.edu/news")

content = url.read() #content string

munews_soup = bs4.BeautifulSoup(content)

#Article titles after the h2 tag
titles = munews_soup.eslect('h2')

print titles


#print only the text of titles from titles list
for title in titles:
	print(title.getNext())

# Article links are under the section class="listing-results cf"
listing_results = munews_soup.find('section', attrs={'class': 'listing-results cf'})
