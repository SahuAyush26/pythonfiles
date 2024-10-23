questions = ["what is the capital of france ?", "how many faces are present in a cube ?", "how many colours present in a rainbow ?", "what does 1+1 equal to ?", "what is the capital of Japan?"]

answers = ["B", "C" , "B" , "A" , "D"]

instructions = ''' 1. Answer the questions correctly earn money, one correct answers earns you rupees 1000
2. One wrong answer automatically looses you the game
3. At the end total amount of money you earned will be displayed
4. To answer the questions correctly choose the correct options
5. If the correct option is, for example B, then type 'B' and not 'b'
6. Hope youenjoy the game '''

print(instructions)

options1 = '''
A - Berlin
B - Paris
C - New Delhi
D - Washington DC'''

options2 = '''
A - 4
B - 5
C - 6
D - 8'''

options3 = '''
A - 23
B - 7
C - 24
D - 25'''

options4 = '''
A - 2
B - 3
C - 4
D - 5'''

options5 = '''
A - Berlin
B - Paris
C - New Dehli
D - Tokyo'''




money = 0

print(questions[0])
print(options1)
a1 = input('Your Answer : ')
if a1 == answers[0]:
  money = money + 1000
  print("correct answer")
  print(questions[1])
  print(options2)
  a2 = input("your answer : ")
  if a2 == answers[1]:
    money = money + 1000
    print("correct answer")
    print(questions[2])
    print(options3)
    a3 = input("your answer :")
    if a3 == answers[2]:
      money = money + 1000
      print("correct answer")
      print(questions[3])
      print(options4)
      a4 = input("your answer :")
      if a4 == answers[3]:
        money = money + 1000
        print("correct answer")
        print(questions[4])
        print(options5)
        a5 = input("your answer :")
        if a5 == answers[4]:
          money = money + 1000
          print("correct answer, congratulations for getting all the answers correct")
        else:
                  print("wrong answer")
      else:
        print("wrong answer")
    else:
      print("wrong answer")
  else:
    print("wrong answer")
else:
  print("wrong answer")

print("you have earned rupees", money)

hs = f"Your latest high score is {money}"

string = ""

with open("high_score.txt", "r+") as f:
   data = f.read()
   if(data != ""):
    for i in data:
        if(i.isnumeric() == True):
          string = string + i
    previous_hs = int(string)
    if(previous_hs < money):
        f.write(hs)
   else:
      f.write(hs)
   
   
   