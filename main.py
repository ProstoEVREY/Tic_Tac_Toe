
list1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
BOARD = '_{}_|_{}_|_{}_\n_{}_|_{}_|_{}_\n_{}_|_{}_|_{}_'
PLAYER = ('X','O')
def game_start():
    choice = ''
    while choice.lower() not in ['Yes'.lower(),'No'.lower()]:
        choice = input("Do you want to start playing? Yes or No ")
    return True
def win(list1):
    if(list1[0]==list1[1]==list1[2]=='X' or list1[3]==list1[4]==list1[5]=='X' or list1[6]==list1[7]==list1[8]=='X' or list1[0]==list1[3]==list1[6]=='X' or list1[1]==list1[4]==list1[7]=='X' or list1[2]==list1[5]==list1[8]=='X' or list1[0]==list1[4]==list1[8]=='X' or list1[2]==list1[4]==list1[6]=='X'):
        print("PLAYER 1 WINS!")
        return True
    elif (list1[0] == list1[1] == list1[2] == 'O' or list1[3] == list1[4] == list1[5] == 'O' or list1[6] == list1[7] ==
            list1[8] == 'O' or list1[0] == list1[3] == list1[6] == 'O' or list1[1] == list1[4] == list1[7] == 'O' or
            list1[2] == list1[5] == list1[8] == 'O' or list1[0] == list1[4] == list1[8] == 'O' or list1[2] == list1[
                4] == list1[6] == 'O'):
        print("PLAYER 2 WINS!")
        return True
def game(BOARD):
    while (game_start()):
        print("The game starts!\nPlayer 1 will go first! (X)")
        print(BOARD.format(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6],list1[7],list1[8]))
        playernow = False
        choice = '0'
        counter = 0
        while int(choice) in range(0,10):
            if(win(list1)):
                break
            if(counter>8):
                print("Looks like this is a draw!")
                break
            choice = input("Choose the spot for your next move: ")
            if(choice.isdigit() and int(choice)<10 and int(choice)>0):
                choice = int(choice)
                if(not playernow):
                    if(list1[choice-1]==' '):
                        list1[choice-1]=PLAYER[playernow]
                        playernow = not playernow
                        counter+=1
                    else:
                        print('This place already taken!')
                        continue
                else:
                    if(list1[choice-1]==' '):
                        list1[choice-1]=PLAYER[playernow]
                        playernow = not playernow
                        counter+=1
                    else:
                        print('This place already taken!')
                        continue
                print(BOARD.format(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6],list1[7],list1[8]))
            else:
                choice='0'
                continue
        break
game(BOARD)








