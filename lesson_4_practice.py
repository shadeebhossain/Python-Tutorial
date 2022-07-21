#Example-1 
username=input("Please enter your username:")
pas=input("Please enter a password:")
lines = ['Username of User 1 is:', username,'Password of User 1 is:',pas]
with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
username1=input("Please enter your username:")
pas1=input("Please enter a password:")
lines1 = ['Username of User 2 is:', username1,'Password of User 2 is:',pas1]
with open('readme1.txt', 'w') as f:
    for line1 in lines:
        f.write(line)
        f.write('\n')
if username==username1 and pas1==pas:
    print("The username and password are a complete match")
else:
    print("Please try again")
with open('readme.txt') as f:
    contents = f.read()
    print(contents)
   
