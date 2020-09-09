from datetime import datetime
import os

# os.path will tell you the current path you are currently in!
print(os.path)

# To actually see what kind of functions we have
print(dir(os))

# getcwd means current working directory
print(os.getcwd())
# /Users/kaushiktummalapalli/Desktop/ALGOEXPERT

# chdir means change Directory
os.chdir('/Users/kaushiktummalapalli/Desktop/')
print(os.getcwd())
# /Users/kaushiktummalapalli/Desktop
# Its desktop bcz we changed the path

print(os.listdir())
# It will list all the files from the desktop:
"""
['untitled folder', 'CDGS2020 (1).dmg', 'Python-ML-WD Projects', 'PYTHON TINKER', 'Marvin_Source Code', 'vscode1', 'JOBS-RELATED', 'Screenshot 2020-07-28 at 10.47.34 PM.png', 'JOB AGENCY', 'Machine Learning A-Z Template Folder', 'jdk-13.0.1_osx-x64_bin.dmg','.DS_Store', 'python_automation', 'Ex_Files_Python_Object_Programming', '5d347118-e71e-4fe9-af99-7d9c73dc2dac.pdf', 'python', '.localized', 'HazeOver.app','python_google', 'Sublime Text (3176).app', 'Full stack-B', 'GRE', 'Screenshot 2020-08-30 at 11.01.53 PM.png', 'DATA SETS',
 'UDACITY PROJECTS', 'vscode.py', 'college pics', 'PENDRIVE_FILES', '1.The Hundred Page ML Book" by Andriy Burkov', 'GitHub Desktop.app', 'OMDENA ML', 'sqlite-tools-osx-x86-3310100', 'income tax', 'Composite Form.pdf', 'my_project', 'versatileproductionsystem', 'APTITUDE', 'object_detection', '.izip.dmg.icloud', 'Data_Preprocessing', 'Resume-3.pdf', 'TODO LIST', 'course.txt', '.git', 'Events', 'TALENTIO', 'college', 'machine learning innomatics.ipynb', 'JPMC TECH ', 'Linkedin Learning courses Folders']
"""

# To create a new folder on the current directory(desktop):
os.mkdir('os-demo/sub-dir-1')
# If we do this,this will lead us to an error that os-demo is not yet created

"""
Traceback(most recent call last):
    File "os_module.py", line 26, in < module >
    os.mkdir('os-demo/sub-dir-1')
FileNotFoundError: [Errno 2] No such file or directory: 'os-demo/sub-dir-1'
"""

os.mkdir('os-demo')
# This will create os-demo in the desktop as that is our current directory

# Difference Between mkdir and makedirs:
# mkdir cannot create a sub folder for the main directory if it doesn't exist!
# But this is not the case for makedirs!

# But to improve os.mkdir('os-demo/sub-dir-1') without getting an error is:
os.makedirs('os-demo/sub-dir-1')
# If os-demo is not present it will make an os-demo and then it will create a sub folder( child node)


os.rmdir('os-demo/sub-dir-1')
# When we execute this command it will only remove the
# sub folder i.e 'sub-dir-1' in os-demo

# But when we use removedirs() it will delete whole folders
# and also the main directory! So we have to be cautious while using this!
os.removedirs('os-demo/sub-dir-1')


# To rename the file names:
os.rename('original.txt', 'renamed.txt')
print(os.listdir())
# When you print this we can see a change that original.txt
# is actually changed to the renamed.txt

# To actually know the stats of a folder:
print(os.stat('renamed.txt'))
# In this we have some imp details like mtime(modified time stamp),
# size(number of bits) and many other details!
# st_mtime stand for modifies time:
mod_time = os.stat('renamed.txt').st_mtime
print(mod_time)
# But we get the time in non human readible format:
# O/P: 1459819315.0
# we can convert this into human readible by using datetime library
mod_time = os.stat('renamed.txt').st_mtime
print(datetime.fromtimestamp(mod_time))
# O/P: 2016-04-04 19:21:55

# To get the Tree like Structure of all the directories
# I mean to get the dirpath, dirnames and filenames:
for dirpath, dirnames, filenames in os.walk('/Users/kaushiktummalapalli/Desktop/JPMC TECH '):
    print("Current Path:", dirpath)
    print("dir names:", dirnames)
    print("Files:", filenames)
    print()
"""
EX:
Current Path: /Users/kaushiktummalapalli/Desktop/JPMC TECH
dir names: ['node_modules']
Files: ['constants.js', 'websocket-server.js', 'event-target.js', 'permessage-deflate.js', 'receiver.js', 'sender.js', 'websocket.js', 'validation.js', 'buffer-util.js', 'extension.js']

Current Path: /Users/kaushiktummalapalli/Desktop/JPMC TECH /node_modules
dir names: ['__mocks__', '__tests__']
Files: ['index.js']
"""
# So os.walk menthod helps us to search through the files nd directories very easily!

print(os.environ.get('HOME'))
# This prints out the HOME directory path
# and if we want to create a file text.txt and add to the HOME Dir:
# We can use concantination like:
file_path = os.environ.get('HOME')+'/text.txt'
# This will work but sometimes if we miss out the '/' it might cause some problems
#  like:# Then we get kaushik/HOMEtext.txt
# So to resolve this issue we have the os.join()[For combining HOME Dir to file name]
file_path = os.path.join(os.environ.get('HOME'), 'text.txt')
# Then we get kaushik/HOME/text.txt

# To get the basename of a path(it may not exist to check that out):
print(os.path.basename('tmp/test.txt'))
# O/P: test.txt

# To get the Dirname of a path(it may not exist to check that out):
print(os.path.dirname('tmp/test.txt'))
# O/P: /tmp

# If you to print both dirname and basename:
print(os.path.split('tmp/test.txt'))
# O/P: ['/tmp','test.txt']

# To check whether a file exists or not:
print(os.path.exists('tmp/test.txt'))
# O/P: False(coz we do not have the path on the file system!)

# To check whether it is a dir or not:
print(os.path.isdir('tmp/test.txt'))


# To check if it has a file:
print(os.path.isfile('tmp/test.txt'))
# O/P: False(coz we do not have the path on the file system!)

# If you get the file name without extension and not wasting time on string parsing:
print(os.path.splitext('tmp/test.txt'))
# O/P: ('/tmp/test','.txt')
