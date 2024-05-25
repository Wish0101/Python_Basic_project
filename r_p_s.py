import random
print("\n\nWelcome to 'Rock' , 'Paper' ,'Scissor' game")
print("user use \n\t-- 0 - for Rock\n\t-- 1 - for Paper\n\t-- 2 - for Scissor")
print("\t\t\t\t\t--RULES--\n\t--Rock win Against Scissor\n\t--Scissor win Against Paper\n\t--Paper win Against Rock")


Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

R_P_S = [Rock,Paper,Scissors]#0,1,2
length = len(R_P_S)-1
Computer = random.randint(0,2)
user = int(input("What do you choose ??\n\t-- "))
if user == 0 and Computer == 2:
    print(R_P_S[user])
    print(R_P_S[Computer])
    print("Player wins")
elif user == 1 and Computer == 0:
    print(R_P_S[user])
    print(R_P_S[Computer])
    print("Player wins")
elif user == 2 and Computer == 1:
    print(R_P_S[user])
    print(R_P_S[Computer])
    print("Player wins")
elif user == Computer:
    print(R_P_S[user])
    print(R_P_S[Computer])
    print("DRAW")
else:
    print(R_P_S[user])
    print(R_P_S[Computer])
    print("Computer wins")
