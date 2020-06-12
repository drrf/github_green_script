import os
from datetime import date
from github import Github
from random import randrange

'''
	module:
		https://github.com/PyGithub/PyGithub

	todo:
		0. add services in OS Cron or TS
		1. run automatically random(1-10) times in each 24H
		2. connect to git
'''

# setting for github
g = Github("user", "password")
repo = g.get_repo('user/repo')

# setting for script
num = 5
rand = randrange(num) + 1
today = date.today()
folder = 'files'
f_format = '.txt'

def remove_file_from_github():
	for i in range(num):
		try:
			file = folder + '/' + str(i+1) + f_format
			contents = repo.get_contents(file)
			repo.delete_file(contents.path, "remove test", contents.sha)
			print('remove from GitHub: ' + file)
		except:
			pass
	
		
def create_new_file_github():
	for i in range(rand):
		file_data = create_data_in_file(i)
		file = folder + '/' + str(i+1) + f_format
		
		try:
			repo.create_file(file, "upload test", file_data)
			print('create file: ' + file)
		except:
			pass
			
def create_data_in_file(i):
	file_data = ''
	file_data += str(today)
	file_data += ("\nrand = %d\r\n" % (rand))
	file_data += ("This is automation github script %d\r\n" % (i+1))
	file_data += "goodbye :)"
	
	return file_data

# for testing only	
def github_get_repo_list():
	for repo in g.get_user().get_repos():
		print(repo.name)


# program start from here
remove_file_from_github()
create_new_file_github()
print("\nfinish with {} new files!".format(rand))