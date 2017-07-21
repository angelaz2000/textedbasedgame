from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
# setup(500,500)
# x_pos = 0
# y_pos = 0
# t.setposition(x_pos, y_pos)

### Write your code below:
for game in range(5):
    person = input('Enter your name: ')
    print('Hello', person, '!')
    print('This is the world where everybody can become an idol(aka celebrity) as long as  they meet the requirements for it.')

    idol = input('Do you want to be an idol? ')
    if (idol == "yes"):
        print('You can be an idol through going into this school called "Celebrity Academy".')

    if (idol == "no"):
        print('Too bad. This game is meant for players that want to learn the experience of being an idol.')

    if (idol != "yes") and (idol != "no"):
        print('Please answer with a yes or no.')
    else:
        print('In the Celebrity School you will learn to sing, dance, and sell your visuals.')
    points = 0
    print('In your stay at Celebrity Academy, you will have 5 points.')

    print('The points represent how popular you will be if you became an idol')

    print('Each time you have a charateristic that does not fit the personnel of an idol,  you will lose a point.')

    print('When you have no more points, that means you will most likely not be fit to be  an idol.')

    print('Lets get started.')

    voice = input('Do you consider yourself to have a good voice?')
    if (voice == "yes"):
        print('The basics of being an idol is to be good at singing.')
        points += 1
        print("Score:", points)
    if (voice == "no"):
        print('Too bad.')
        points += -1
        print("Score:", points)
    if (voice != "yes") and (voice != "no"):
        print('Please answer with a yes or no.')

    dance = input('Do you consider yourself to be good in dance?')
    if (dance == "yes"):
        print('Another part of being an idol is to be good at dancing.')
        points += 1
        print("Score:", points)
    if (dance == "no"):
        print('Too bad.')
        points += -1
        print("Score:", points)
    if (dance != "yes") and (dance != "no"):
        print('Please answer with a yes or no.')

    visualFace = input('Does your face have blemishes?')
    if (visualFace == "yes"):
        print('Too bad.')
        points += -1
        print("Score:", points)
    if (visualFace == "no"):
        print('Having a clear face is a good trait when you are an idol.')
        points += 1
        print("Score:", points)
    if (visualFace != "yes") and (visualFace != "no"):
        print('Please answer with a yes or no.')

    visualEyes = input('Are your eyes big?')
    if (visualEyes == "yes"):
        print('Big eyes have been a quality that many wish for.')
        points += 1
        print("Score:", points)
    if (visualEyes == "no"):
        print('Too bad')
        points += -1
        print("Score:", points)
    if (visualEyes != "yes") and (visualEyes != "no"):
        print('Please answer with a yes or no.')

    visualStructure = input('Do you have high cheek bones?')
    if (visualStructure == "yes"):
        print('Many people have done surgery to obtain high cheek bones.')
        points += 1
        print("Score:", points)
    if (visualStructure == "no"):
        print('Too bad')
        points += -1
        print("Score:", points)
    if (visualStructure != "yes") and (visualStructure != "no"):
        print('Please answer with a yes or no.')

    print('Your final score is', points, 'out of five criterias of being an idol.')

    print("Your are", points / 5 * 100, "%", "fit to be an idol.")

# # Close window on click.
# exitonclick()
exit()
