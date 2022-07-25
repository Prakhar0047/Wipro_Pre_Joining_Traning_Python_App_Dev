import re
email = "from abc.xyz@pqr.com Mon Dec 29 01:12:15 2016"

result = re.search('(\d{2}:\d{2}:\d{2})', email).group(0)
print(result)

domain = re.findall('\S+@\S+', email)
print(domain)

# e = re.findall('^@\s{}', email)
# print(e)
