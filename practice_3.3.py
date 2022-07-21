# Task-1
username=input("Please enter a username:")
pas=input("Please enter a password:")

lines = [username, pas]
with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
#Example -2
more_lines = ['', 'Append text files', 'The End']
with open('readme.txt', 'a') as f:
    f.writelines('\n'.join(more_lines))
  
