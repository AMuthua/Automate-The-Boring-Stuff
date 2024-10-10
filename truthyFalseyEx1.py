name = ''
while not name:
    print('Enter your name:')
    name = input()
print('How many users are you planning to have?' + " " + name)
numOfUsers = int(input())
if numOfUsers:
    print('Be sure to make enough space for all users.')
print('Successfully Done!')