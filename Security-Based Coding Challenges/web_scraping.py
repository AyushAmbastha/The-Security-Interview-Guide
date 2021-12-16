import requests
from bs4 import BeautifulSoup

# Make a request to https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Extract title of page
page_title = soup.title

# print the result
print(page_title)

# Extract first <h1>(...)</h1> text
first_h1 = soup.select('div.thumbnail') # Find div with classname = thumbnail -> CSS Selector


# element = soup.find(id='target') 
# elements = soup.find_all(class_='class_c')
# elements = soup.find_all(lambda tag: tag.name == 'p' and tag.parent.attrs.get('id', None) == 'main_content')

#python_jobs = results.find_all(
#     "h2", string=lambda text: "python" in text.lower()
# )

print(first_h1)

# Create top_items as empty list -> Get Links
image_data = []

# Extract and store in top_items according to instructions on the left
images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    image_data.append({"src": src, "alt": alt})

#print(image_data)

#CSV File-

# all_products = []

# products = soup.select('div.thumbnail')
# for product in products:
#     # TODO: Work
#     print("Work on product here")


# keys = all_products[0].keys()

# with open('products.csv', 'w', newline='') as output_file:
#     dict_writer = csv.DictWriter(output_file, keys) -> Create a header so take keys from any element
#     dict_writer.writeheader()
#     dict_writer.writerows(all_products)