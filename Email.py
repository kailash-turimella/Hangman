import smtplib

email = input('which email do you have??\n').lower()

while(email != 'gmail' and email != 'outlook' and email != 'yahoo'):
    email = input('Enter one of the following:\n1.Gmail\n2.Outlook\n3.Yahoo\n\n').lower()
   
if(email == 'gmail'):
    email = 'smtp.gmail.com'
    domain = '@gmail.com'
elif(email == 'outlook'):
    email = 'smtp-mail.outlook.com'
    domain = '@outlook.com'
elif(email == 'yahoo'):
    email = 'smtp.mail.yahoo.com'
    domain = '@yahoo.com'
    
conn = smtplib.SMTP(email, 587)            # smtp.gmail.com
                                           # smtp-mail.outlook.com
                                           # smtp.mail.yahoo.com
        
conn.ehlo()      # Starting the connection
conn.starttls()  # Encrypting the connection

emailid = input('Enter Email address'+'('+domain+')'+'...\n')
emailid+=domain
password = input('Enter your password...\n')
while(True):
    try:
        conn.login(emailid,password)
        print('\nLogged in:)')
        break
    except smtplib.SMTPAuthenticationError:
        print('\n\nIncorrect email or password\n')
    print('Is this your email address?\n',emailid,'\n')
    yn = input().lower()
    if(yn == 'no'):
        emailid = input('Re-enter your email address\n')
    password = input('Enter password\n')

to=input('Who do you want to send the email to?\n')

subject=input('Subject : ')
text=input('Enter the body of the email...\n')

message = 'Subject: '+subject+'\n\n'+text

print('\n\n\n'+message,'\n\nsend?')
send=input()
if send=='yes':
    conn.sendmail(emailid,to,message)
    print('\nsent!')
else:
    print('ok')
    
#conn.sendmail(from, to, message)
