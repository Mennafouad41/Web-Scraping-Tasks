
'''
This program is to implement:
    1- Function to find a specific section in html code with a specific id
    2- Function to find a specific section in html code with a specific id and the tag name
    3- Function to find all sections in html code with a specific id
    4- Function to find all sections in html code with a specific id and the tag name
    5- Function to find a specific section in html code with a specific class
    6- Function to find a specific section in html code with a specific class and the tag name
    7- Function to find all sections in html code with a specific class
    8- Function to find all sections in html code with a specific class and the tag name
'''


import requests
from bs4 import BeautifulSoup


url = "http://testphp.vulnweb.com/listproducts.php?cat=1%27"

req = requests.get(url).text

soup = BeautifulSoup(req,'html.parser')

#Function to find a specific section in html code with a specific id

def specific_section_ID(Soup , ID):
    by_id = Soup.find(id = ID)
    return by_id


#Function to find a specific section in html code with a specific id and the tag name

def specific_section_ID_tagName(Soup ,tag_name, ID):
    by_id = Soup.find(tag_name , id = ID)
    return by_id


#Function to find all sections in html code with a specific id

def specific_section_all_ID(Soup , ID):
    by_id = Soup.find_all(id = ID)
    return by_id

#Function to find all sections in html code with a specific id and the tag name

def specific_section_all_ID_tagName(Soup ,tag_name, ID):
    by_id = Soup.find_all(tag_name , id = ID)
    return by_id

#Function to find a specific section in html code with a specific class

def specific_section_class(Soup , CLASS):
    by_class = Soup.find(class_ = CLASS)
    return by_class


#Function to find a specific section in html code with a specific class and the tag name

def specific_section_class_tagName(Soup ,tag_name, CLASS):
    by_class = Soup.find(tag_name , class_ = CLASS)
    return by_class



#Function to find all sections in html code with a specific class

def specific_section_all_class(Soup , CLASS):
    by_class = Soup.find_all(class_ = CLASS)
    return by_class

#Function to find all sections in html code with a specific class and the tag name

def specific_section_all_class_tagName(Soup ,tag_name, CLASS):
    by_class = Soup.find_all(tag_name , class_ = CLASS)
    return by_class



############################### MAIN ##########################################

print("Print section with specific id : ")
print(specific_section_ID(soup , 'content'))
print("---------------------------------------")

print("Print section with specific id and tag_name : ")
print(specific_section_ID_tagName(soup,"h6",'siteInfo'))
print("---------------------------------------")

print("Print all sections with specific id : ")
print(specific_section_all_ID(soup , 'siteInfo'))
print("---------------------------------------")

print("Print all sections with specific id and tag_name : ")
print(specific_section_all_ID_tagName(soup,"div",'siteInfo'))
print("---------------------------------------")