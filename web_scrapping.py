# If you want to scrape a website:
# 1. Use the API
# 2. HTML web Scraping using some tool like bs4

# there are 4 steps to complete the web scrapping 
    # i.install all requirments
    # ii.Get the HTML
    # iii.Parse the HTML
    # iv. HTML Tree travers

# Step0: install all the Requirment Libraries:
# 1. pip install requests
# 2. pip install html5lib
# 3. pip install bs4

# importing the libraries
import requests
from  bs4 import BeautifulSoup
url = "https://codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)
# print(soup.prettify)

# Step 3: HTML Tree traversal
    # Commonly used types of objects:
    # print(type(title)) # 1. Tag
    # print(type(title.string)) # 2.NavigableString
    # print(type(soup))  # 3. BeautifulSoup
    # 4.Comment 

# Get the title of the HTML page
title = soup.title
# print(title)

# Get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)



# Get the first paragraph in the HTML page 
# print(soup.find('p'))
# print(soup.find('p')['class']) #and also get the class of the HTML

# find all the elements with class lead
# print(soup.find_all("p",class_="lead"))

# Get the text from the tags/soup
# print(soup.find('p').get_text())

# Get all the anchor tags from the page
anchors = soup.find_all('a')
# print(anchors) 
all_links = set() 

# Get all the links on the page
for link in anchors:
    if (link.get('href') !='#'):
        linkText = "https://codewithharry.com" +link.get('href')
        all_links.add(linkText)
        # print(linkText)


# ---Get the Comment of HTML
# markup = "<p><!-- this is a comment --></p>"
# soup = BeautifulSoup(markup)
# print(soup.p.string)
# print(type(soup.p.string))


# ----Geting content of spacefic id in the HTML

navbarSupportedContent = soup.find(id = 'navbarSupportedContent')
# print(navbarSupportedContent)
# print(navbarSupportedContent.contents)
# ---Itrating all the content using for loop
# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
# for elen in navbarSupportedContent.contents:
#     print(elen)

# -----Get content the ID in string form 
# for item in navbarSupportedContent.string:
# for item in navbarSupportedContent.stripped_string:
    # print(item)

# print(navbarSupportedContent.parent)
# print(navbarSupportedContent.parents)
# for item in navbarSupportedContent.parents:
#     print(item)
#     print(item.name)

# Geting next and previous sibling in the html content
# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

# Geting CSS in the html using CSS
# elem = soup.select('#.loginModel')
# elem = soup.select('#.model-footer')
# print(elem)

