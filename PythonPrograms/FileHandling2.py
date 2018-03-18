#reading from file
'''
file1=open('file1.txt','r')
print(file1.read())# this prints the file1.txt
#print(file1) # this prints the objects specifictions
print(file1.tell())# tells the current position of CURSOR
print(file1.seek(0,0))#sets the CURCOR to starting point
print(file1.read(10))'''

# writing in the file
''' 
file2=open('file2.txt','w') # 'w' deletes the old stuff an writes the new statements
print(file2.write('dude i am having morning shifts'))
file2.close()
file2=open('file2.txt','r')
print(file2.read()) '''

# Appending in to file
'''
file2=open('file2.txt','a')
print(file2.write(' ->this is an appended line'))
file2.close()
file2=open('file2.txt','r')
print(file2.read())
file2.close() '''

# copying 1 file data to another file
'''
userFile=input('enter the file name :')
userFile=userFile+'.txt'
file2=open(userFile,'r')
fileCopied=open('copiedFile.txt','w')
print(file2.read())
file2.write(fileCopied.read())
print(fileCopied.read())
'''












