while True:
    
    print('Code\tGame \n\n 1:\tHangman \n 2:\t7 up 7 down \n 3:\tRock Paper Scissors \n 4: \tXO')
    print()
    n=int(input("Enter the code of the Game to play: "))



###############Hangman###############    

    if n==1:
        file1=open("movies.txt","r")
        lines=file1.readlines()
        size=len(lines)
        
        import random

        tries=7
        ran=random.randint(0,size-1)

        letters=["a","e","i","o","u"]

        count = 0
        L=lines[ran].strip().lower()

        for i in range(0,len(L)):
            if L[i]==" " or L[i]=="\n":
                print(" ",end="")
            elif L[i] in letters:
                print(L[i],end="")
        else:
            print( "_", end="")
        print("\n")

        while True:
            if tries==0:
                print("All your tries are over you lost LOSER")
                break
            if count==len(L):
                print("You won CHAMP")
                break
            count=0
            print("tries=",tries)
            letter=str(input("Please Enter a Letter:"))
            if letter not in L:
                tries-=1
                continue
            letters.append(letter)
            for i in range (0,len(L)):
                if L[i]==' ' or L[i]=='\n':
                    print(' ',end=' ')
                    count=count+1
                elif L[i] in letters:
                    print(L[i],end=" ")
                    count=count+1
                else:
                    print("_",end=" ")

            print('\n')
        

######################### 7 up 7 down game #########################
    
    elif n==2:
        import random

        print("\nEnter 1 for 7 up \nEnter 2 for 7 down \nEnter 3 for 7")
        userchoice=int(input("Enter your choice : "))
        
        while userchoice>3 or userchoice<1 :
            userchoice=int(input("\nEnter a valid number"))

        if userchoice==1:
            userchoice_assumption="7 up"

        elif userchoice==2:
            userchoice_assumption="7 down"

        else:
            userchoice_assumption="7"

        print("\nUser's assumption is ",userchoice_assumption)

        dicenumber=random.randint(1,13)

        print("\nThe dice number is ",dicenumber)

        if dicenumber<7:
            print("\nThe number is less than 7")

        elif dicenumber>7:
            print("\nThe number is more than 7")

        else:
            print("\nThe number is 7")

        if dicenumber>7:
            dicenumber_value="7 up"

        elif dicenumber<7:
            dicenumber_value="7 down"

        else:
            dicenumber_value="7"

        if userchoice_assumption==dicenumber_value:
            print("\nYou won")

        else:
            print("\nYou lost")



######################### Rock Paper Scissors#########################

    elif n==3:
        import random

        ####### Rules of the game ########

        print('''Winning rules of rock paper scissors are as follows\n
              Rock vs paper -> paper wins \n
              Rock vs scissors -> rock wins \n
              paper vs scissors -> scissors wins\n''')

        print("\nEnter Your choice\n\t1. Rock\n\t2. Paper\n\t3. Scissors\n")

        ####### Take input from the user ########

        choice = int(input("User turn:   "))

        while choice > 3 or choice < 1:
            choice = int(input("Enter Valid Input :   "))
        
        if choice==1:
            choice_name = "Rock"

        elif choice==2:
            choice_name = "Paper"

        else :
            choice_name="Scissors"

        ##### Display user's choice #####                 
                 
        print( "User choice is : " + choice_name)
        print(" \nNow its computer turn")

        ###### Randomised computer choice #####

        comp_choice = random.randint(1,3)

        while comp_choice==choice:
            comp_choice=random.randint(1,3)

        if comp_choice==1:
            comp_choice_name="Rock"

        elif comp_choice==2:
            comp_choice_name="Paper"

        else:
            comp_choice_name="Scissors"

        ##### Display computer's Choice ######   

        print("Computer Choice is : "+comp_choice_name+'\n')
        print(choice_name + " vs "+ comp_choice_name+"\n")

        ##### Result computation ######

        ######  comparing  the choices ###### 

        if(choice==1 and comp_choice==2) or (comp_choice==2 and choice==3):
            print("Paper WINS\n",end="")
            result="Paper"

        elif (choice==2 and comp_choice==3) or (choice==3 and comp_choice==2):
            print(" Scissors WINS\n",end="")
            result="Scissors"
    
        else:
            print("Rock WINS\n",end="")
            result="Rock"

        if choice==result:
            print("User WINS")

        else:
            print("Computer WINS\n")

      
    elif n==4:
            board = ["-", "-", "-",
                     "-", "-", "-",
                     "-", "-", "-"]

            # Lets us know if the game is over yet
            game_still_going = True

            # Tells us who the winner is
            winner = None

            # Tells us who the current player is (X goes first)
            current_player = "X"


            # ------------- Functions ---------------

            # Play a game of tic tac toe
            def play_game():

              # Show the initial game board
              display_board()

              # Loop until the game stops (winner or tie)
              while game_still_going:

                # Handle a turn
                handle_turn(current_player)

                # Check if the game is over
                check_if_game_over()

                # Flip to the other player
                flip_player()
              
              # Since the game is over, print the winner or tie
              if winner == "X" or winner == "O":
                print(winner + " won.")
              elif winner == None:
                print("Tie.")


            # Display the game board to the screen
            def display_board():
              print("\n")
              print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
              print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
              print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
              print("\n")


            # Handle a turn for an arbitrary player
            def handle_turn(player):

              # Get position from player
              print(player + "'s turn.")
              position = input("Choose a position from 1-9: ")

              # Whatever the user inputs, make sure it is a valid input, and the spot is open
              valid = False
              while not valid:

                # Make sure the input is valid
                while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                  position = input("Choose a position from 1-9: ")
             
                # Get correct index in our board list
                position = int(position) - 1

                # Then also make sure the spot is available on the board
                if board[position] == "-":
                  valid = True
                else:
                  print("You can't go there. Go again.")

              # Put the game piece on the board
              board[position] = player

              # Show the game board
              display_board()


            # Check if the game is over
            def check_if_game_over():
              check_for_winner()
              check_for_tie()


            # Check to see if somebody has won
            def check_for_winner():
              # Set global variables
              global winner
              # Check if there was a winner anywhere
              row_winner = check_rows()
              column_winner = check_columns()
              diagonal_winner = check_diagonals()
              # Get the winner
              if row_winner:
                winner = row_winner
              elif column_winner:
                winner = column_winner
              elif diagonal_winner:
                winner = diagonal_winner
              else:
                winner = None


            # Check the rows for a win
            def check_rows():
              # Set global variables
              global game_still_going
              # Check if any of the rows have all the same value (and is not empty)
              row_1 = board[0] == board[1] == board[2] != "-"
              row_2 = board[3] == board[4] == board[5] != "-"
              row_3 = board[6] == board[7] == board[8] != "-"
              # If any row does have a match, flag that there is a win
              if row_1 or row_2 or row_3:
                game_still_going = False
              # Return the winner
              if row_1:
                return board[0] 
              elif row_2:
                return board[3] 
              elif row_3:
                return board[6] 
              # Or return None if there was no winner
              else:
                return None


            # Check the columns for a win
            def check_columns():
              # Set global variables
              global game_still_going
              # Check if any of the columns have all the same value (and is not empty)
              column_1 = board[0] == board[3] == board[6] != "-"
              column_2 = board[1] == board[4] == board[7] != "-"
              column_3 = board[2] == board[5] == board[8] != "-"
              # If any row does have a match, flag that there is a win
              if column_1 or column_2 or column_3:
                game_still_going = False
              # Return the winner
              if column_1:
                return board[0] 
              elif column_2:
                return board[1] 
              elif column_3:
                return board[2] 
              # Or return None if there was no winner
              else:
                return None


            # Check the diagonals for a win
            def check_diagonals():
              # Set global variables
              global game_still_going
              # Check if any of the columns have all the same value (and is not empty)
              diagonal_1 = board[0] == board[4] == board[8] != "-"
              diagonal_2 = board[2] == board[4] == board[6] != "-"
              # If any row does have a match, flag that there is a win
              if diagonal_1 or diagonal_2:
                game_still_going = False
              # Return the winner
              if diagonal_1:
                return board[0] 
              elif diagonal_2:
                return board[2]
              # Or return None if there was no winner
              else:
                return None


            # Check if there is a tie
            def check_for_tie():
              # Set global variables
              global game_still_going
              # If board is full
              if "-" not in board:
                game_still_going = False
                return True
              # Else there is no tie
              else:
                return False


            # Flip the current player from X to O, or O to X
            def flip_player():
              # Global variables we need
              global current_player
              # If the current player was X, make it O
              if current_player == "X":
                current_player = "O"
              # Or if the current player was O, make it X
              elif current_player == "O":
                current_player = "X"


            # ------------ Start Execution -------------
            # Play a game of tic tac toe
            play_game()

        ##### Re-play prompt ########  
    print('\nDo you want to play another game?')
    
    ch=input('Y/N : ')
    
    if ch == 'Y' or ch=='y':
        print('\n\n=======================================')
        continue
    elif ch== 'N' or ch== 'n':
        print('Thank You for playing')
        break
    else:
        print('Invalid input\n ***** QUITING THE PROGRAM ******')
        print('Program Ended\n Thank you for Playing')
        break
