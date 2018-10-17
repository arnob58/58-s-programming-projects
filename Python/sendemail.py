'''
Hello this is a small little python script which takes a gmail and password and send mail to the receptor via gmail smtp server.
Please note that this module DOES NOT have any masking on password, so the password you input will be VISIBLE. So, if use this software, use it with your own responsibility.
You are welcome to make any adjustments or improvements to the script, just please notify me when you make changes.
To contact, you can mail me at dcosta.arnob@gmail.com
Thank you
'''
import smtplib
import sys
## This function will take the gmail and password and send a mail via gmail smtp server
def send_mail(gmail,password):
    print('Connecting to the google smtp server')
    smtpObj = smtplib.SMTP('smtp.gmail.com',587)
    hello=smtpObj.ehlo()
    if hello[0]==250:
        print('Successfully connected to the smtp server via 587 port....')
    ttls_response=smtpObj.starttls()
    if ttls_response[0] == 220:
        print('Successfully setup tls connection....')
    print('trying to login gmail account.....')
    try:
        try:
            smtpObj.login(gmail,password)
            print('Login successful!')
        except:
            print('You put wrong email or password. Try to put the correct one: ')
            print('Enter Your Gmail: ')
            gmail = input()
            print('Enter your password(WARNING! PASSWORD IS NOT MASKED. USE WITH CAUTIOUS):')
            password = input()
            send_mail(gmail,password)
        recep = input('Enter the receptors email address: ')
        print('Enter your message')
        message = input()
        print('Sending mail to '+ recep+'/nPlease Wait')
        smtpObj.sendmail(gmail,recep,message)
        print('message sent!')
        print('Closing session')
        smtpObj.quit()
        sys.exit()
    except:
        print('An error has occured. System will be terminated')
        sys.exit()

## This function will take input and processes to the send_mail function
def start():
    print('Welcome to the simple smtp based mail system. This program can send mails only. Note that the password is NOT MASKED when inputting. So, be cautious when inputing the password. Note the smtp server this project is using google smtp server. So, to send a mail,you only can use an gmail account.')
    print('\nEnter Your Gmail: ')
    Gmail = input()
    print('Enter your password(WARNING! PASSWORD IS NOT MASKED. USE WITH CAUTIOUS):')
    Password = input()
    send_mail(Gmail,Password)
    
if __name__ == '__main__':
    start()
    

