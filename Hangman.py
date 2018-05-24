def hangman(word):
    stages = [
    "______",
    "|     |",
    "|     0",
    "|    /",
    "|     |",
    "|    /"]
    usedletters = []
    wrong = 0
    i = 0
    board = []
    while i < len(word):
        board.append("_")
        i = i + 1
    i = 0
    theword = list(word)
    while wrong < 7:
        letter = False
        if wrong < 2:
            if wrong == 0:
                print("\n".join(stages[0:2]))
            elif wrong == 1:
                print("\n".join(stages[0:3]))
        if wrong > 1 and wrong < 4:
            if wrong == 2:
                print("\n".join(stages[0:4]))
            elif wrong == 3:
                stages[3] = stages[3] + " \\"
                print("\n".join(stages[0:4]))
        if wrong == 4:
            print("\n".join(stages[0:5]))
        if wrong > 4:
            if wrong == 5:
                print("\n".join(stages))
            elif wrong == 6:
                stages[5] = stages[5] + " \\"
                print("\n".join(stages))
                print(char + " is not in the word or phrase. You lose")
                break
        print("")
        print(" ".join(board))
        if "_" not in board:
            print("You've won the game")
            break
        char = input("Guess a letter: ")
        print("")
        if char == "quit":
            break
        if char == "a" or char == "b" or char == "c" or char == "d" or char == "e" or char == "f":
            letter = True
        elif    char == "g" or char == "h" or char == "i" or char == "j" or char == "k" or char == "l":
            letter = True
        elif   char == "m" or char == "n" or char == "o" or char == "p" or char == "q" or char == "r":
            letter = True
        elif  char == "s" or char == "t" or char == "u" or char == "v" or char == "w" or char == "x":
            letter = True
        elif char == "y" or char == "z":
            letter = True
        if letter == False:
            print("You can only guess a single letter")
            continue
        if char in usedletters:
            print("You already guessed this letter")
            continue
        
        while i < len(theword):
            place = theword[i]
            if char == place:
                board[i] = place
                
            i = i + 1
        usedletters.append(char)
        i = 0
   
        if char not in theword:
            wrong = wrong + 1
            print(char + " is not in the word or phrase")

       
hangman("addition")
     
    

    
