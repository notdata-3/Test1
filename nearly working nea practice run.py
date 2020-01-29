import time
import random
import sleep
i = 0
Player_1P = 0
Player_2P = 0
Player_1T = 0
Player_2T = 0
Winner_Points = 0


#player 1 login which probably works--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
user = False
user= str(input('What is your username?       '))
if user == 'haris':
    print ('Authorised username')
    user = True
else:
        print ('incorrect username')

password = False
password= str(input('what is your password?   '))
if password == 'ABC':
    print ('Authorised password')
    password = True
else:
        print ('Incorrect password, acess denied please try again')


#player 2 login which also probably works ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
user_1 = False
user_1= str(input('What is your username?       '))
if user_1 == 'bob':
    print ('Authorised username')
    user_1 = True
else:
        print ('incorrect username')
password_1 = False
password_1= str(input('what is your password?   '))
if password_1 == 'DEF':
    print ('Authorised password')
    password_1= True
else:
        print ('Incorrect password, acess denied please try again')


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#rules of game yes
if password== True and user == True and password_1 == True and user_1 == True:
    print ('Welcome to the game. Here are the rules & how to play the game')
    time.sleep(2)
    print ('Two players roll a 6-sided dice and get points depending on what they roll')
    time.sleep(2)
    print ('There are 5 rounds in a game. In each round, each player rolls the two dice')
    time.sleep(2)
    print ('Points rolled on each players dice are added to their score.')
    time.sleep(2)
    print ('If the total is an even number, an additional 10 points are added')
    time.sleep(2)
    print ('If the total is an odd number, 5 points are taken')
    time.sleep(2)
    print ('If a double is rolled an extra die is rolled and points added')
    time.sleep(2)
    print ('Score cannot go below 0 at any point. \n Highest score at the end of the 5 round wins. \n if both players have the same score at the end of 5 rounds, 1 die is rolled each and the highest score wins. (Repeats until someone wins).')
    time.sleep(4)
    print ('Only authorised players can play')
    time.sleep(2)

    #actual game time ok---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def roll():
     die1= random.randint(1, 6)
     die2= random.randint(1, 6)
     change = 10 if (die1+die2) % 2 == 0 else -5
     points = die1+die2+change
     if die1 == die2:
        points += random.randint(1, 6)
        return points

    
    #ok this works ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    for i in range (1, 5):
        Player_1P += roll()
        print ('After this round ', user, 'you now have gained ' ,Player_2P, ' Points')
        time.sleep(1)
        Player_2P += roll()
        print ('After this round ' ,user_1, 'You now have gained ',Player_2P, 'Points')
        time.sleep(1)

        #---ok i think this also works-----

        if Player_1P == Player_2P:
            while Player_1T == Player_2T:
                print ('x')
                Player_1T = random.randint(1, 6)
                Player_2T = random.randint(1, 6)

                if Player_1T > Player_2T:
                    Player_2P = 0
                else:
                        Player_2T > Player_1T
                        Player_1P = 0


                            #ok winner calculations now

                        if Player_1P > Player_2P:
                                Winner_Points = Player_1P
                                Winner_User = user
                                winner = (Winner_Points, user)
                        elif Player_2P > Player_1P:
                                    Winner_Points = Player_2P
                                    Winner = (Winner_Points, user_1)
                                    Winner_User = user_1

                                    print('Well done, ', Winner_User, 'you won with ',Winner_Points,' points.')

                                    #now 2 store the winners file

                                    Winner = (Winner_Points,',' ,Winner_User)
                                    f = open ('Winner.txt', 'a')
                                    f.write(''.join(winner))
                                    f.write('\n')
                                    f.close

                                    #ok now thats done time 2 move onto the leaderboard

                                    f=open('the_big_pro_leaderboard.txt', 'r')
                                    leaderboard = [line.replace('\n' , '') for line in f.readlines()]
                                    f.close

                                    for idx, item in enumerate(leaderboard):
                                        if item.split(', ') [1] == winner[1] and int(item(split(', ')[0] < int(winner[0])
                                                                                          [idx] = '{}, {}'.format(winner[0], winner[1]
                                                                                                                  
