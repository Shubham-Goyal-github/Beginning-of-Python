# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 08:03:59 2021

@author: hp
"""
try:
    
    import random
    print("WELCOME! To The Game of RPSLS(Rock-Paper-Scissor-Lizard-Spock")
    name=input("Enter your name")
    round_no=int(input("How many rounds of the game you want to play?"))

    player_points=0
    comp_points=0

    def number_to_name(no):
        if no==0:
            return "rock"
        elif no==1:
            return "spock"
        elif no==2:
            return "paper"
        elif no==3:
            return "lizard"
        elif no==4:
            return "scissors"
        else:
            return "none"

    def name_to_number(name):
        if name=="rock":
            return 0
        elif name=="spock":
            return 1
        elif name=="paper":
            return 2
        elif name=="lizard":
            return 3
        elif name=='scissor':
            return 4
        else:
            return "none"
        
        
    



    def rpsls(player_choice):
     
        
        global comp_points
        global player_points
        global difference
        player_cho_number=name_to_number(player_choice)
        computer_choice=random.randrange(0,4)
        comp_choice_name=number_to_name(computer_choice)
        
        if player_choice=='rock' and comp_choice_name=="scissor" or player_choice=="rock" and comp_choice_name=="lizard":
            player_points+=1
            print("You win the round",i)
            print("system choice:",comp_choice_name)
            print("your choice:",player_choice)
        elif player_choice=='rock' and comp_choice_name=="paper" or player_choice=="rock" and comp_choice_name=="spock":
            comp_points+=1
            print("the system wins the round",i)
            print("system choice:",comp_choice_name)
            print("your choice:",player_choice)
        elif player_choice=='paper' and comp_choice_name=="rock" :
            player_points+=1
            print("You win the round",i)
            print("system choice:",comp_choice_name)
            print("your choice:",player_choice)
        elif player_choice=='paper' and comp_choice_name=="scissor" or player_choice=="paper" and comp_choice_name=="spock"or player_choice=="paper" and comp_choice_name=="lizard":
            comp_points+=1
            print("the system wins the round",i)
            print("system choice:",comp_choice_name)
            print("your choice:",player_choice)
        elif player_choice=='scissor' and comp_choice_name=="paper" or player_choice=="scissor" and comp_choice_name=="lizard":
            player_points+=1
            print("You win the round",i)
            print("system choice:",comp_choice_name)
            print("your choice:",player_choice)
        elif player_choice=='scissor' and comp_choice_name=="rock" or player_choice=="scissor" and comp_choice_name=="spock":
            comp_points+=1
            print("the system wins the round",i)
            print("system choice:",comp_choice_name)
            print("your choice:",player_choice)
        elif player_choice=='spock' and comp_choice_name=="scissor" or player_choice=="spock" and comp_choice_name=="rock":
            player_points+=1
            print("You win the round",i)
            print("system choice:",comp_choice_name)
            print("your choice:",player_choice)
        elif player_choice=='spock' and comp_choice_name=="paper" or player_choice=="spock" and comp_choice_name=="lizard":
            comp_points+=1
            print("the system wins the round",i)
            print("system choice:",comp_choice_name)
            print("your choice:",player_choice)
        elif player_choice=='lizard' and comp_choice_name=="paper" or player_choice=="lizard" and comp_choice_name=="spock":
            player_points+=1
            print("You win the round",i)
            print("system choice:",comp_choice_name)
            print("your choice:",player_choice)
        elif player_choice=='lizard' and comp_choice_name=="rock" or player_choice=="lizard" and comp_choice_name=="scissor":
            comp_points+=1
            print("the system wins the round",i)
            print("system choice:",comp_choice_name)
            print("your choice:",player_choice)
        elif player_choice==comp_choice_name:
            comp_points+=0.5
            player_points+=0.5
            print("the round is tied between you and the system")
            print("system choice:",comp_choice_name)
            print("your choice:",player_choice)
     
        print("For round",i,"the difference between your and system's choice no. is ")
        print(abs(player_cho_number-computer_choice))
        print('------------------------------------------------------------')

    for i in range(1,round_no+1):
        print("Make your choice from the following available choices for the round",i)
        print("Enter the respective name while making the choice...")
        print("0:rock\n 1:spock\n 2:paper\n 3:lizard\n 4:scissor")
        player_input=input().lower()
        rpsls(player_input)

    if player_points > comp_points:
        print("CONGRATULATIONS!!",name," you wins the game")
        print("your score:",player_points)
        print("system score:",comp_points)
    elif player_points < comp_points:
        print("SORRY!!Better luck next time")
        print("your score:",player_points)
        print("system score:",comp_points)
    else:
        print("the game is tied ")
        print("your score:",player_points)
        print("system score:",comp_points)
   
    
except:
    print("Please try again later.")
    print("You are making a wrong input")
    