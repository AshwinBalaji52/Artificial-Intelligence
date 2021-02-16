# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 16:39:01 2021
@author: Ashwin Balaji
"""

import numpy as np
import random
import sys
from itertools import combinations
magic_square = np.array([[8,1,6],
                         [3,5,7],
                         [4,9,2]])
magic_square1 = np.array([[8,1,6],
                         [3,5,7],
                         [4,9,2]])
numberlist = [1,2,3,4,5,6,7,8,9]
computer_list = []
human_list = []
gameplay = [['_','_','_'],
            ['_','_','_'],
            ['_','_','_']]
key = None
human_sumlist = []
computer_sumlist = []
computer_turn = None
human_turn = None
step_human = 1
step_computer = 1
human_sum=0
computer_sum=0
result = [['_','_','_'],
          ['_','_','-'],
          ['_','_','_']]

principal_diagonal = []
secondary_diagonal=[]
diagonal = []
'''
Function to ask whether the human want to start the game, If he/she wants to start, they can do easily
making it more interactive
'''
def game_choice(key):
    key = input("Do you want to start the game ? Type Y/N: ")
    if (key == 'Y'or key == 'y'):
         print("Human starting the game with",human,"and Computer with",computer,"\n")
         print("MAGIC SQUARE")
         DisplayBoard()
         player_human()
    elif (key == 'N' or key == 'n'):
         print("Computer starting the game with",computer,"and Human with",human,"\n")
         player_computer()
    else:
        print("Invalid Input !!!")
        DisplayBoard()
        game_choice(key)
    return
'''
1. Checking the index corresponding the input chosen by AI this is because READ:2)
2. list contents gets deleted one by one, once the numbers from [1..9] i.e., moves starts consuming to keep a track of numbers 
    that have been used, so that human can easily judge which number to choose next
'''
def checklist_computer():
    global computer_turn
    global numberlist
    for x in range(len(numberlist)):
        if(computer_turn == x):
            return
        else:
            break
'''
1. Checking the index corresponding the input provided by human this is because READ:2)
2. I'm deleting the list contents once the numbers from [1..9] i.e., moves starts consuming to keep a track of numbers 
    that have been used, so that computer can easily judge which number to choose next
'''
def checklist_human():
    global human_turn
    global numberlist
    for x in range(len(numberlist)):
        if(human_turn==x):
            return 
        else:
            break
'''
Deleting the move option from the number list one-by-one once the moves
starts consuming by human/computer
'''
def compute_computer(computer_list):
    global step_computer
    global computer_turn
    global numberlist
    global gameplay
    check_win()#before starting the move we need to check whether computer is winning
    if computer_turn in numberlist:
        numberlist.remove(computer_turn)
        computer_list.append(computer_turn)
        step_computer+=1
        return
    else:
        player_computer()
        print("Wrong selection")
        return
'''
Deleting the move option from the number list one-by-one once the moves
starts consuming by human/computer
'''   
def compute_human(human_list):
    global step_human
    global human_turn
    global numberlist
    check_win()#before starting the move we need to check whether human is winning
    if human_turn in numberlist:
        numberlist.remove(human_turn)
        human_list.append(human_turn)
        step_human+=1
        return
    else:
        player_human()
        print("Wrong input")
'''
Accepting input from human and calling functions to w.r.t the input chosen
and reflect the same in the TIC-TAC-TOE Matrix
'''
def player_human():
    global magic_square
    global gameplay
    global human_turn
    global step_human
    check_win()
    if(len(numberlist)!=0):
        print("-------------------------------------------------------|")
        print("Human Turn Counter:",step_human)
        human_turn = int(input("Human Turn: "))
        checklist_human()
        print(magicsquare())
        #To fill tictactoe matrix with the human symbol
        for i in range(len(magic_square)):
            for j in range(len(magic_square[i])):
                if((human_turn == magic_square[i][j]) and (gameplay[i][j]=='_')):
                    gameplay[i][j] = human
                print('|', gameplay[i][j], '|', end='')
            print() 
        compute_human(human_list)
        sum_human(computer_list, human_list)
        check_win()
        player_computer()
    else:
        check_win()
        print("\nOh Oh .... A Draw Game !!!")
        sys.exit()
'''
This is an important and tricky part !!!
Accepting input from human and calling functions to w.r.t the input chosen
and reflect the same in the TIC-TAC-TOE Matrix
'''
def player_computer():
    global magic_square
    global gameplay
    global computer_turn
    global computer_sumlist
    global human_sumlist
    global step_computer
    check_win()
    print("-------------------------------------------------------|")
    if((len(computer_sumlist) or len(human_sumlist)) and len(numberlist)!=0):
        a = []
        b = []
        '''
        Since numberlist gets updated after every input chosen by the human/AI
        We can conclude some pattern.
        "A" list contains all such valid 15-sum(val) moves
        "B" list contains all such valid 15-sum(val) moves     
        We need to check whether 15-sum(val) is consumed or not if not consumed, those positions can be used to block oppenent
        that's why numberlist(intersection)sumlist
        '''
        a = list(set(numberlist).intersection(computer_sumlist))
        b = list(set(numberlist).intersection(human_sumlist))  
        if(len(a)!=0):
            #computer tries to win as this is the priority task
            #"A" contains permittable next moves of AI
            computer_turn = random.choice(a)#if "A" set contains value, than that value is high priority for the next move 
            check_win()
        elif(len(b)!=0):
            #if computer couldn't win it tries to block the opponents win
            #"B" contains permittable next moves of human
            computer_turn = random.choice(b)
            check_win()
        else:
            #No such case then random value chosen from numberlist
            computer_turn = random.choice(numberlist)
            check_win()
    elif(len(numberlist)==0):
        check_win()
        print("\nOh Oh .... A Draw Game !!!")
        sys.exit()
    else:
        computer_turn = random.choice(numberlist)
        check_win()
    checklist_computer()
    print("Computer Turn Counter:",step_computer)
    print("Computer Turn:",computer_turn)
    print(magicsquare())
    '''
    Updating gameplay matrix with the input chosen by AI
    '''
    for i in range(len(magic_square)):
        for j in range(len(magic_square[i])):
            if((computer_turn == magic_square[i][j]) and (gameplay[i][j]=='_')):
                gameplay[i][j] = computer
            print('|', gameplay[i][j], '|', end='')
        print()
    compute_computer(computer_list)
    sum_computer(computer_list, human_list)
    player_human()
'''
Main logic to predcit the next moves
'''
def sum_human(computer_list, human_list):
    global human_sum
    human_sumlist1 = []
    global human_sumlist
    check_win()
    # to make list of possible moves of size 2 i.e., checking possible moves 
    # two pairs selected must follow rules of magic sqaure given below
    list1 = list(combinations(human_list,2))
    for j,val in enumerate(list1):
        human_sum = 15-sum(val)
        '''
        15-sum(pair) will give the next predictable move of the opponent
        For Ex: human played at the pos (5,4) sum gives 9, now 15-9 gives 6
        this implies that computer should put at the pos 6 to stop human from winning
        is such sums are in the range of 0 to 9 that is permittable positions the such moves are updated
        otherwise pass
        '''
        if(human_sum<=9 and human_sum>=0):
            human_sumlist1.append(human_sum)
            human_sumlist = list(set(human_sumlist1))#set is to avoid repeated number sums
        else:
            break
    return
'''
Main logic to predcit the next moves
'''
def sum_computer(computer_list, human_list):
    global computer_sum
    global computer_sumlist
    computer_sumlist1 = []
    check_win()
    # to make list of possible moves of size 2 i.e., checking possible moves 
    # two pairs selected must follow rules of magic sqaure given below
    list2 = list(combinations(computer_list,2))
    for j,val in enumerate(list2):
        computer_sum = 15-sum(val)
        '''
        15-sum(pair) will give the next predictable move of the opponent
        For Ex: computer played at the pos (7,6) sum gives 13, now 15-13 gives 2
        this implies that human should put at the pos 2 to stop computer from winning
        is such sums are in the range of 0 to 9 that is permittable positions the such moves are updated
        otherwise pass
        '''
        if(computer_sum<=9 and computer_sum>=0):
            computer_sumlist1.append(computer_sum)
            computer_sumlist = list(set(computer_sumlist1))#set is to avoid repeated number sums
        else:
            continue
        
def Diagonals():
    global gameplay
    for i in range(len(gameplay)):
        for j in range(len(gameplay[i])):
            if (i == j):
                principal_diagonal.append(gameplay[i][j])
    for i in range(len(gameplay)):
        for j in range(len(gameplay[i])):
            if ((i + j) == (len(gameplay) - 1)):
                secondary_diagonal.append(gameplay[i][j])
    diagonal.append(principal_diagonal)
    diagonal.append(secondary_diagonal)
    for i in range(len(diagonal)):
        for j in range(len(diagonal)):
            if((diagonal[i][j]==diagonal[i][j+1]==diagonal[i][j+2]) and (diagonal[i][j]!='_' or diagonal[i][j+1]!='_' or diagonal[i][j+2]!='_')):
                print("\nWohooo .... ",gameplay[i][j],"Wins !!!")
                sys.exit()
            else:
                Rows()
                break
            break
        break
            
def Rows():
    global gameplay
    for i in range(len(gameplay)):
        for j in range(len(gameplay[i])):
            if((gameplay[i][j]==gameplay[i][j+1]==gameplay[i][j+2]) and (gameplay[i][j]!='_' or gameplay[i][j+1]!='_' or gameplay[i][j+2]!='_')):
                print("\nWohooo .... ",gameplay[i][j],"Wins !!!")
                sys.exit()
            else:
                Columns()
                break
            break
        
def Columns():
    global gameplay
    result = [[gameplay[j][i] for j in range(len(gameplay))] for i in range(len(gameplay[0]))]
    for i in range(len(result)):
        for j in range(len(result[i])):
             if((result[i][j]==result[i][j+1]==result[i][j+2]) and (result[i][j]!='_' or result[i][j+1]!='_' or result[i][j+2]!='_')):
                print("\nWohooo .... ",result[i][j],"Wins !!!")
                sys.exit()
             else:
                break  
             break

def check_win():
    Diagonals()
    Rows()
    Columns()
    return
    
def DisplayBoard():
    for i in range(len(magic_square)):
        for j in range(len(magic_square[i])):
            print('|', magic_square[i][j], '|', end='')
        print()
    return

def magicsquare():
    for i in range(len(magic_square1)):
        for j in range(len(magic_square1[i])):
            print('|', magic_square1[i][j], '|', end='')
        print()
    return ("")

print("\nWelcome to TIC TAC TOE: AI v/s Human\n")
symbol = input("Choose 'X' OR 'O': ")
if (symbol == 'X' or symbol == 'x'):
     human = 'X'
     computer = 'O'
     game_choice(key)
elif (symbol == 'O' or symbol == 'o'):
    human = 'O'
    computer = 'X'
    game_choice(key)
else:
    print("Invalid Input")




  
