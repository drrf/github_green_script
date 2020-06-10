import os
from datetime import date
from random import randrange

# setting
num = 10
rand = randrange(num) + 1
today = date.today()
folder = 'files'
f_format = '.txt'

# create folder to the files, and delete old files
def folder_and_files():
	try:
		if not os.path.exists(folder):
			os.makedirs(folder)
		for i in range(num):
			file = './' + folder + '/' + str(i+1) + f_format
			if os.path.exists(file):
				os.remove(file)
				print('remove: ' + file)
	except:
		print("except: folder_and_files()")
		exit()

def create_new_files():
	for i in range(rand):
		f = open("./files/" + str(i+1) + f_format,"w+")
		f.write(str(today))
		f.write("\nrand = %d\r\n" % (rand))
		f.write("This is automation github script %d\r\n" % (i+1))
		f.write("goodbye :)")
		f.close

# program start from here
folder_and_files()
create_new_files()
print("\nfinish with {} new files!".format(rand))


