import re

#    415-555-0000
#    555-0000
#    (415) 555-0000
#    555-0000 ext 1234 / ext. 1234 / x1234

phoneNumberRegex = re.compile(r'''
(                              
((\d\d\d)|(\(\d\d\d\)))?             # area code(optional)
(\s|-)                               # separator
\d\d\d                               # first three digits
-                                    # separator
\d\d\d\d                             # last four digits
(((ext(\.)?\s)|x)   (\d{2,5}))?      # extension(optional)
)
''', re.VERBOSE) 


emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+             # name
@                           # @
[a-zA-Z0-9_.+]+             # domain name
''', re.VERBOSE)

 
text = '''
800-420-7240
415-863-9900
415-863-9950 ext 12345
info@nostarch.com
media@nostarch.com
academic@nostarch.com
info@nostarch.com
'''

extractedPhoneNumbers = phoneNumberRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhoneNumbers:
    allPhoneNumbers.append(phoneNumber[0])

result = '\n'.join(allPhoneNumbers)+'\n'+'\n'.join(extractedEmail)

print(result)