import urllib.request
from urllib.parse import quote
import json

subcategory_dict = {
    "blush": [
        "Vegan", "Gluten free", "Canadian", "Natural", "Non-gmo", "Purpicks",
        "Usda organic", "Organic", "Certclean", "Ewg verified",
        "Hypoallergenic", "No talc"
    ],
    "bronzer": [
        "Gluten free", "Canadian", "Natural", "Organic", "Vegan", "Purpicks",
        "Ewg verified"
    ],
    "eyebrow": ["Ewg verified", "Purpicks"],
    "eyeliner": [
        "Vegan", "Natural", "Canadian", "Gluten free", "Organic", "Purpicks",
        "Certclean", "Ewg verified", "Hypoallergenic", "No talc", "Ecocert"
    ],
    "eyeshadow": [
        "Vegan", "Canadian", "Natural", "Gluten free", "Non-gmo", "Purpicks",
        "Certclean", "Ewg verified", "Organic", "Usda organic",
        "Hypoallergenic", "No talc", "Ecocert"
    ],
    "foundation": [
        "Vegan", "Canadian", "Natural", "Gluten free", "Purpicks", "Certclean",
        "Ewg verified", "Hypoallergenic", "No talc", "Water free",
        "Cruelty free", "Alcohol free", "Oil free"
    ],
    "lip%20liner": [
        "Natural", "Vegan", "Gluten free", "Canadian", "Purpicks",
        "Ewg verified", "Hypoallergenic", "No talc", "Cruelty free"
    ],
    "lipstick": [
        "Canadian", "Natural", "Gluten free", "Non-gmo", "Peanut free product",
        "Vegan", "Cruelty free", "Organic", "Purpicks", "Certclean",
        "Chemical free", "Ewg verified", "Hypoallergenic", "No talc"
    ],
    "mascara": [
        "Natural", "Gluten free", "Vegan", "Canadian", "Organic", "Purpicks",
        "Ewg verified", "Hypoallergenic", "No talc", "Ecocert", "Usda organic",
        "Certclean"
    ],
    "nail%20polish": [
        "Vegan", "Canadian", "Natural", "Gluten free", "Fair trade",
        "Sugar free", "Non-gmo", "Dairy free"
    ]
}

product = input(
    "Welcome to the Perfect Makeup Finder!\nWhat makeup product would yo ulike to search for?\nYour options are: Blush, Bronzer, Eyebrows,\nEyeliner, Eyeshadow, Foundation, Lip Liner, Lipstick,\nMascara, and Nail Polish!\n"
)
product = quote(product.strip())
product = product.lower()

subcategory = input(f"Alright, to narrow down results further, what subcategory of your product would you like to look at? Here are your options: {subcategory_dict[product]} \nIf you don't wish to answer this question, just hit enter. \n ")
subcategory = quote(subcategory.strip())
subcategory = subcategory.lower()

while True:
  brand = input("Final question. What brand would you like this product to be?\n If you don't want to answer this question, just hit enter. \n")
  brand = quote(brand.strip())
  brand = brand.lower()
  url = f'https://makeup-api.herokuapp.com/api/v1/products.json?product_type={product}&brand={brand}&product_tags={subcategory}'
  
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
  if len(result) > 0:
    break
  else:
    print("Looks like your brand doesn't have this product available! Please enter another brand.")

result_dict = result[0]
final_result = result_dict["name"]
final_result = quote(final_result.strip())
final_result = final_result.lower()

amazon_link = f"https://www.amazon.com/s?k={final_result}%20{brand}&ref=nb_sb_noss"

print(amazon_link)


