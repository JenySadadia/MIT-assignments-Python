print("Think of a number between 1 and 100, but don't tell me what you choose.")
min_n = 1
max_n = 100
right_answer = False
while not right_answer:
    mid_n = (max_n + min_n + 1)/2
    answer = input('Is it ' + str(mid_n) + '? ')
    if answer[0] == 'y':
        right_answer = True
    elif answer.startswith('higher'):
        min_n = mid_n + 1
    elif answer.startswith('lower'):
        max_n = mid_n -1
    else:
        print("Sorry, I don't understand your answer.")
print('Woohoo! I got it!')
'''
ans1: 'while not right_answer:' specifies that the field right_ans is is not false so that While True will executes loop infinite times.
ans2: The statement 'Woohoo! I got it!' will print only once when execution of while loop will terminated.
ans3: Veriable answer is used for displaying middle number.
ans4: program will only understand the responses that 'y','higher' or 'lower'.
ans5: If the program gets the response ’higher’ it will again find middle number between mid_n and 100
ans5: min_n : for minimum number
      max_n : for maximum number
      mid_n : for middle number
'''