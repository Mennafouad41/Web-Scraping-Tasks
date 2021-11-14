

'''
This program to use requests function in python for doing these tasks:
    1- Send request to the website with a given url then recive the respons value of the wepsite and print this response
    2- Send request to the website with a given url then recive the respons text (html code) of the wepsite and print this code
    3- Send request to the website with a given url then recive the respons text (html code) of the wepsite and save this code in the file   
'''

import requests

url = "http://testphp.vulnweb.com/listproducts.php?cat=1%27"


#Function to print the response value for a website 

def response_value(link):
        
   req = requests.get(link)
   return req


Response=response_value(url)
print("The response value is:")
print(Response)

print("-------------------------------------------------------------------------")
#-------------------------------------------------------------------------------

#Function to print the HTML for a website 

def response_html(link):
        
   req = requests.get(link).text
   return req

print("The response text is:")
print(response_html(url))

#-------------------------------------------------------------------------------

#Function to save the HTML for a website in a file

def response_html_file(link):
    
    req = requests.get(link).text
    f = open("page.html","w")
    f.write(req)
    f.close()
    
response_html_file(url)
    
