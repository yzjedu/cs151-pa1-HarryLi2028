# Programmers: Harry Li
# Course:  CS151 sec 06
# Due Date: 10/10/2024
# Lab Assignment: School Adventure
# Problem Statement: Creating an advanture game about school and output different results based on the user input
# Data In: Answers to the questions, exam choice, and name 
# Data Out: The grade you get from the results you have entered

# Output the introduction of the program 
print ('Welcome to My Adventure of School')

# Prompt user to input their name 
user_name = str(input('Please enter your Username: '))

# When user does not enter name, ask them to enter their name until they put something in
while user_name == '':
    user_name = str(input('Please enter a valid Username: '))

# Output a statement based on the length of their name
if len(user_name) <= 4:
    print('Wow that is a short name!')
elif len(user_name) <= 7:
    print('That is a cool name!')
else:
    print('It must be a struggle writing your name everytime!')

# Output the rules and introduction
print('Hello', user_name, 'your task is to survive throughout the school with a passing grade. You will get 100 points to start the day, and based on your decisions it would determine your final grade.')
final_grade = 100
# Prompt user to enter which test they want to take
test_one = str(input('Please enter the test choice A or B:'))
test_one = test_one.lower
# Based on the input in test one provide a question of the dedicated test, otherwise deduct 50 points from their total grade
if test_one == 'a':
    question_a = float(input('What is the deciaml form of 16/32:'))
    if question_a == 0.5:
        print('Great job, you are one smart cookie!')
    else:
        print('Oh no, you got it wrong! That is going to be a 25 point deduction on your final grade! Try harder next time.')
        final_grade -= 25
elif test_one == 'b':
    question_b = float(input('What is the decimal of 15/12:'))
    if question_b == 1.25:
        print('Your answer is correct! Congratulations!')
    else:
        print('That is the wrong answer! Your grade has dropped by 25 points! Please study harder!')
        final_grade -= 25 
else:
    print(user_name,' has failed to take the test. 50 points would be deducted from the final grade.')
    final_grade -= 50

# Output the introduction the the final quiz 
print('Here is the final quiz of the day. There is 3 quizes and you will choose one out of the 3 to answer')

# Prompt user to input the quiz they want to take
final_quiz = input('Please choose the quiz between 1-3:')


if final_quiz == '1':
    quiz_1 = int(input('what is the answer to 6(7-5)^3:'))
    if quiz_1 == 48:
        print('Your Correct!')
        if total_grade < 100:
            final_grade += 20
    else:
        print('The answer is WRONG!')
        final_grade -= 20
elif final_quiz == '2':
    quiz_2 = int(input('what is the answer to 0(9+10)^5:'))
    if quiz_2 == 0:
        print('Wow, you got that right!')
        if total_grade < 100:
            final_grade += 30
    else:
        print('The answer is WRONG!')
        final_grade -= 40
elif final_quiz == '3':
    quiz_3 = int(input('what is the answer to 11(2+1)^2:'))
    if quiz_3 == 99:
        print('Your Correct!')
        if total_grade < 100:
            final_grade += 15
    else:
        print('The answer is WRONG!')
        final_grade -= 10
else:
    final_grade -= 50

if final_grade < 60:
    print('your final grade is: ' ,final_grade, ' you have failed to pass the school day! >:(')
elif final_grade < 70:
    print('your final grade is: ' ,final_grade, ' you barely pass the school day! :(')
elif final_grade < 80:
    print('your final grade is: ' ,final_grade, ' you have gotten an average grade for the school day! :|')
elif final_grade < 90:
    print('your final grade is: ' ,final_grade, ' your grade is almost an A! keep up the good work! :)')
elif final_grade < 100:
    print('your final grade is: ' ,final_grade, ' your grade is an A! Great performance! : )')
else:
    print('your final grade is: ' ,final_grade, ' your grade is 100%! Outstanding performance! : )')
    
