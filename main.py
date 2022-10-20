import random

players = []
savedRolls = []
finalScores = []
dice = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

allPlayersRolled = False
smallestNum = 6
biggestNum = 0

def playerNames():
    print("How many players? (2+)")
    numPlayers = int(input())
    x = 1
    if numPlayers < 2:
        print("must have two or more players!\n")
        playerNames()
    else:
        while x < numPlayers + 1:
            print("what is the name of player", x, "?")
            playerName = input()
            players.append(playerName)
            finalScores.append(0)
            x += 1

    playerTurn = 0
    return playerTurn

def numberOfRounds():
    print("How many rounds do you want to play?")
    numRounds = int(input())
    return numRounds

def rollDice(player):
    global allPlayersRolled
    while allPlayersRolled == False:
        y = 0
        print("\n", players[player], "'s turn!")
        while y < 3:
            print(dice)
            largestNum = dice[0]
            for i in range(0, len(dice) - 1):
                if dice[i + 1] > largestNum:
                    largestNum = dice[i + 1]
            savedRolls.append(largestNum)
            if y < 2:
                print("your largest number was a ", largestNum, ", so this value will be saved.")
                print("ready to roll your remaining", 2 - y, "dice? (y or n)")
            elif y == 2:
                print("your last roll was a ", largestNum, ", so this value will be saved.")
                if len(savedRolls) is not 3 * len(players):
                    print("\nIs the next player ready to roll? (y or n)")
                else:
                    print("\nEveryone has rolled! ready to move on? (y or n)")
                    allPlayersRolled = True
            rollAgain = input()
            if rollAgain == "y":
                for i in range(0, len(dice)):
                    dice.insert(i, random.randint(1, 6))
                    dice.pop(i + 1)
                dice.pop(0)
                y += 1
            else:
                print("game ended")
                exit()
        if player < len(players) - 1:
            player += 1
        else:
            player = 0
        dice.clear()
        for i in range(0, 3):
            dice.insert(i, random.randint(1, 6))

def rollRiskDice():
    print("But before we calculate scores, let's throw in a twist!")
    print("On the Risk Die, if you roll a: \n1- Lowest roll gets taken out of score"
          "\n2- Highest roll gets taken out of score"
          "\n3- Rolls get multiplied together"
          "\n4- Nothing happens to your score"
          "\n5- 5 points added to your score"
          "\n6- Automatically gets a score of 10")
    for i in range(0, len(players)):
        print("\n",players[i], "'s turn to roll the Risk Die! type 'roll' to roll!")
        rollDie = input()
        if rollDie == "roll":
            riskDieValue = random.randint(1, 6)
            print("You rolled a", riskDieValue, "!")
            riskDieScore(riskDieValue, i)

def riskDieScore(die, i):
    if die == 1:
        smallestNum = 6
        for j in range(3, 0, -1):
            if savedRolls[(3 * (i + 1)) - j] < smallestNum:
                smallestNum = savedRolls[(3 * (i + 1)) - j]
        finalScores[i] = finalScores[i] + (savedRolls[(3 * (i + 1)) - 3] + savedRolls[(3 * (i + 1)) - 2] + savedRolls[(3 * (i + 1)) - 1] - smallestNum)

    if die == 2:
        biggestNum = 0
        for j in range(3, 0, -1):
            if savedRolls[(3 * (i + 1)) - j] < biggestNum:
                biggestNum = savedRolls[(3 * (i + 1)) - j]
        finalScores[i] = finalScores[i] + (savedRolls[(3 * (i + 1)) - 3] + savedRolls[(3 * (i + 1)) - 2] + savedRolls[(3 * (i + 1)) - 1] - biggestNum)

    if die == 3:
        finalScores[i] = finalScores[i] + (savedRolls[(3 * (i + 1)) - 3] * savedRolls[(3 * (i + 1)) - 2] * savedRolls[(3 * (i + 1)) - 1])

    if die == 4:
        finalScores[i] = finalScores[i] + (savedRolls[(3 * (i + 1)) - 3] + savedRolls[(3 * (i + 1)) - 2] + savedRolls[(3 * (i + 1)) - 1])

    if die == 5:
        finalScores[i] = finalScores[i] + (savedRolls[(3 * (i + 1)) - 3] + savedRolls[(3 * (i + 1)) - 2] + savedRolls[(3 * (i + 1)) - 1] + 5)

    if die == 6:
        finalScores[i] = finalScores[i] + 10

def displayFinalScores():
    global allPlayersRolled
    for i in range(0, len(players)):
        print("\n", players[i], ":", finalScores[i])
    winningPlayer = max(finalScores)
    for i in range(0, len(finalScores)):
        if winningPlayer == finalScores[i]:
            print(players[i], "is in the lead!")
    allPlayersRolled = False
    savedRolls.clear()

def finalWinner():
    winnerPlayer = max(finalScores)
    for i in range(0, len(finalScores)):
        if winnerPlayer == finalScores[i]:
            print("\n",players[i], "is the ultimate winner! Congrats :)")

def playAgain():
    global allPlayersRolled
    print("play again? y or n?")
    userPlayAgain = input()
    if userPlayAgain == "n":
        print("thanks for playing :) have a good day!")
    elif userPlayAgain == "y":
        players.clear()
        savedRolls.clear()
        finalScores.clear()
        allPlayersRolled = False
        Main()

def Main():
    rounds = numberOfRounds()
    names = playerNames()
    x = 0
    while x < rounds:
        rollDice(names)
        rollRiskDice()
        displayFinalScores()
        x += 1
    finalWinner()
    playAgain()

Main()