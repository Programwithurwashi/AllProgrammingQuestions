from os import path
def createfile(dest):
    if not(path.isfile(dest)):
        open(dest,'w')
        f.write('welcome to python scripting')
        f.close()

dest='E:\All codes\\sample.txt'
createfile(dest)
print("file created")()