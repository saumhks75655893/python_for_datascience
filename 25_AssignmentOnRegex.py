import re

# phone number varification 

phn = "222-333-444-2345"

if re.search("\d{3}-\d{3}-\d{3}-\d{4}",phn):
    print("It's a valid number")
else:
    print("It's not a valid phone number.")


# # email varification 

email = "john@gmail.com   john@.com   david.988@yahoo.com"

print(re.findall(r"[\w._%]{0,20}@[\w-].[A-Za-z]{2,3}",email))

# web scrapping 

import urllib.request
from re import findall

url = "https://www.summet.com/dmsi/html/codesamples/addresses.html"

a = urllib.request.urlopen(url)
html = a.read()
htmlstr = html.decode()

phn = findall(r"\(\d{3}\) \d{3}-\d{4}", htmlstr)

for phone in phn: 
    print(phone)