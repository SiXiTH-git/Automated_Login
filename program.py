# Imported Python Libraries
# Temporary and Permanent
from tkinter import *
from selenium import webdriver
from csv import DictReader
import os
import csv
import itertools
import urllib
import urllib2
import cookielib
import webbrowser
import subprocess
import re
from tkinter import *
import Tkinter, Tkconstants, tkFileDialog
from tkinter.messagebox import showerror
import mechanize
from urllib2 import HTTPError
from mechanize import Browser
from tkinter import ttk
import tkinter as tk 





# File converting Function
def fileConvertion(event):
	fileCW = Tk()

	# Opens a file dialog window for searching for list text file
	fileCW.fileName = tkFileDialog.askopenfilename( filetypes = [ ( "Text Files", "*.txt") ] )

	# Sets the files path equal to fname
	fname = fileCW.fileName

	# Opens a file dialog window for searching for csv file
	fileCW.folderName = tkFileDialog.askopenfilename( filetypes = [ ( "CSV Files", "*.csv") ] )

	# Sets the files path equal to folname
	folname = fileCW.folderName

	# Opens fname and it read it as the in_file
	with open(fname, 'r') as in_file:
		stripped = (line.strip() for line in in_file)
		lines = (line.split(":") for line in stripped if line)
		grouped = itertools.izip(* [lines] * 3)
		with open(folname, 'w') as out_file: # Outputs the contents of fname to folname 
			writer = csv.writer(out_file)
			writer.writerow( ('Email', 'Password') )
			writer.writerows(lines)

	# Closes convert window
	fileCW.destroy()

	fileCW.mainloop()




# Amazon Login Function
def amazonLog(event):
	
	# File Dialog for opening a file to be read
	listin = tkFileDialog.askopenfilename( filetypes = [ ("CSV Files", "*.csv") ] )

	#Reads csv file into two seperate lists for email and password
	email_in, password_in=[],[]
	with open(listin) as f:
		for row in DictReader(f):
			email_in.append(row["Email"])
			password_in.append(row["Password"])

	# Sets varible "url" to browser url to be opened
	url = 'https://www.amazon.com/ap/signin?clientContext=165-7575283-6209430&openid.return_to=https%3A%2F%2Fauth.comixology.com%3A443%2Fap-post-redirect&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_comixology&openid.mode=checkid_setup&marketPlaceId=A3K7XZP00M3RXO&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=cmx_us&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.pape.max_auth_age=3600&siteState=clientContext%3D165-7575283-6209430%2CsourceUrl%3Dhttps%253A%252F%252Fwww.comixology.com%252Fap%252Freturn%2Csignature%3DpInNLu9rBzLj2F3rmA1bohFio7qgYj3D'

	# Opens url with default web browser
	webbrowser.open(url)
	
	# File to list Function
	def File_IN(event):
		formsub = Tk()

		email_f = open(email_in, 'r')
		stringE = ""
		while 1:
			line = f.readline(entryNE)
			if not line:break
			stringE += line

		email_f.close()

		pass_f = open(password_in, 'r')
		stringP = ""
		while 1:
			line = f.readline(entryNE)
			if not line:break
			stringP += line

		pass_f.close()

		


		
		

		# List info to HTML form Function

		# Form location (Supposed)	
		webpage = r"https://www.amazon.com/ap/signin?ie=UTF8&amp"

		# Username and Password variables
		amazon_username = stringE
		amazon_password = stringP

		driver = webdriver.Firefox()
		driver.get(webpage)

		emailF = driver.find_element_by_class_name("email")
		emailF.send_keys(amazon_username)

		passF = driver.find_element_by_class_name("password")
		passF.send_keys(amazon_password)

		File_IN.destroy()
		File_OUT.destroy()

		File_IN.mainloop()


		
	amazonLogW = Tk()

	# About label
	about = Label(amazonLogW, text='Program made by: MALCOLM_X')
	
	# Row Number Input
	entryNL = Label(amazonLogW, text='Entry Number: ')
	entryNE = Entry(amazonLogW)

	# File to list Button
	Lnext = Button(amazonLogW, text='Load Entry')
	Lnext.bind("<Button-1>", File_IN)

	# Button and Label Display
	about.grid(row=0, columnspan=2)
	entryNE.grid(row=1, column=1)
	entryNL.grid(row=1)
	Lnext.grid(row=2)

	amazonLogW.mainloop()


# Login Setup
loginW = Tk()




# Password Authentication Function
def Authentication(event):
	
	valid = 'python' # Correct Password

	if pwordE.get() == valid: # Checks to see if password give equals the correct password
		
		# Main Program
		mp = Tk()
		loginW.destroy() # Closes Login window

		# About label
		about = Label(mp, text='Program made by: MALCOLM_X')

		# Buttons for other parts of program
		fileC = Button(mp, text='Text to CSV')
		amLog = Button(mp, text='Amazon Login')

		# Binds a function to buttons
		fileC.bind("<Button-1>", fileConvertion)
		amLog.bind("<Button-1>", amazonLog)

		# Displays buttons and label
		about.grid(row=0, columnspan=2)
		fileC.grid(row=1)
		amLog.grid(row=1, column=1)

		mp.mainloop()
	
	else: # Displayed if password was incorrect
		errorW = Tk()

		# Error message
		errorL = Label(errorW, text='Invalid Password!', bg='black', fg='red')

		# Displays error message
		errorL.pack()
		errorW.mainloop()

# About label
about = Label(loginW, text='Program made by: MALCOLM_X')
# Login Window
pwordL = Label(loginW, text='Password: ')
pwordE = Entry(loginW, show='*')

# Login button with binded function
logBtn = Button(loginW, text='Login')
logBtn.bind("<Button-1>", Authentication)

# Displays password and about label, entry box, and login button
about.grid(row=0, columnspan=2)
pwordL.grid(row=1)
pwordE.grid(row=1, column=1)
logBtn.grid(row=2, columnspan=2)

loginW.mainloop()
