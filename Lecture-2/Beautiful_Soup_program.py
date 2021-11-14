'''
This program to use BeautifulSoup function with requests function in python for doing these tasks:
    1- Find the specific section in the html code using find() function
    2- Function to find the specific section in the html code using find() function (Only the text in the section)
    3- Find the multiple specific sections in the html code using find_all() function
    4- Using prettify() function to print the output of find() function in a beautiy form
'''


from bs4 import BeautifulSoup
import requests


url = "http://testphp.vulnweb.com/listproducts.php?cat=1%27"

req = requests.get(url).text

soup = BeautifulSoup(req,'html.parser')


#Function to find the specific section in the html code using find() function

def specific_section(Soup , target):
    find_soup = Soup.find(target)
    return find_soup

#Function to find the specific section in the html code using find() function (Only the text in the section)

def specific_section_text(Soup , target):
    find_soup = Soup.find(target)
    New_find_soup = find_soup.text
    return New_find_soup
    
    
#Function to find the multiple specific sections in the html code using find_all() function

def multiple_specific_sections(Soup , target):
    find_soup = Soup.find_all(target)
    for link in find_soup:
     print(link)


#Function to Using prettify() function to print the output of find() function in a peautiy form

def beautiy_form(Soup , target):
    find_soup = Soup.find(target)
    New_find_soup = find_soup.prettify()
    return New_find_soup


print("specific_section:")
print(specific_section(soup , "h3"))
print("----------------------------------------------------------")
print("specific_section (text):")
print(specific_section_text(soup , "h3"))
print("----------------------------------------------------------")
print("peautiy_form:")
print(beautiy_form(soup , "h3"))
print("----------------------------------------------------------")
print(" multiple_specific_sections:")
multiple_specific_sections(soup , "a")





