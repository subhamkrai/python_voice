#!/usr/bimn/python3
import fbchat
#importing fbchat module for facebook chat
from getpass import getpass
#getpass is used for password 
username = input("Username: ")

client = fbchat.Client(username, getpass())
no_of_friends = int(input("Number of friends: "))

for i in range(no_of_friends):
	name = input("user:")
	friends = client.searchForUsers(name)
	friend = friends[0].uid
	msg = str(input("message:"))
	msg = client.sendMessage(msg,friend)
	if set:
		print("message sent ")


