print('colour identification quiz for nursery champs!')
answer=input('Are you ready to play the marolix Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: What color is the apple in?')
    if answer.lower()=='red':
        score =score+1
        print('correct')
    else:
        print('Wrong Answer :')
 
 
    answer=input('Question 2: What is the name of that fruit that will be the same as the color name of a fruit name ')
    if answer.lower()=='orange':
        score =score+1
        print('correct')
    else:
        print('Wrong Answer :')
 
    answer=input('Question 3: how many colours in our Bharath(indian) flag?')
    if answer.lower() =='three':
        score =score+1
        print('correct')
    else:
        print('Wrong Answer :')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
print('Thanks for participating in marolix quiz program ')


