import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Reply hazy try again'
    elif answerNumber == 4:
        return 'Ask again later'
    elif answerNumber == 5:
        return 'Yes'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is NO'
    elif answerNumber == 8:
        return 'Outlook nicht zu gut'
    elif answerNumber == 9:
        return 'Very Doubtful'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)
