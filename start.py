import os
from datetime import date
from random import randrange

rand = randrange(10+1)
today = date.today()

# create folder to the files
if not os.path.exists('files'):
	os.makedirs('files')

for i in range(rand):
	f = open("./files/" + str(i+1) + ".txt","w+")
	f.write(str(today))
	f.write("\nrand = %d\r\n" % (rand))
	f.write("This is automation github script %d\r\n" % (i+1))
	f.write("goodbye :)")
	f.close
	
print("finish with {} new files!".format(rand))