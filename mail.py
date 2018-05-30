#!/usr/bin/python3
import smtplib
# importing smtp module for python3 
s = smtplib.SMTP("smtp.gmail.com",587)  # port 587 some times 487 or so 
s.starttls()
s.login("subham.k.rai@gmail.com",<password>)  # in place of password write you password
msg= "hello"  # type your message

s.sendmail("sender@mail.com","reciver@mail.com",msg)    # write sender or reciver mail id 
s.quit()
