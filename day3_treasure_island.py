print('''
*******************************************************************************
            ___________
           / |       | |
        ,' ,'         \/',_    __
     ,'__/             |    ',|  "'-,,,,,,,
   ,/  _|',            |                |   \
   |  |   |',           \               |    \
   |__|   |  ',          ',             |     \
  /       |     ',        ,_"""""---'-_,'______\
 /        |        ',,_-'"    |        |        ',
|_________|         |         /        |        / ',,'""""|
|__  |        ,____/         |        _|       /    |___  /
'\___|      ,'_,'|_,-,_______|         |       /      , '/
  \,' _', _/  ,, ,',|        |          \       |   '" ,'
   \ / |_ ,  |  \||||       ,' |      ,'|    _""    |,'
    ' ,'  ', |  ||||| __ ,'   _|_ ,'    |    |""---/
       ' ,"""','"""""" |     /           \"""|    /
                      |_____|_      __''"    \   |
                     |  |  /  """"""   |      \ /
                      \ / |            |       /
                       \--'            |      /
                       |   \__        _|__    |
                       |      |__     |   ',,,|
                       |         |____|   /   |
                       /         _|    ,,'_   |
                      |__________|___,'  ,,' /
                       \      ---'    \,/  ,'
                        \     |    ,,,' \_/
                         |    |_,''      |/
                         |    |       []_|
                          \___'        /
                           \       __,'
                            \_____/        FoulWing

*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

first_step = input("Left of right?\n").lower()
if first_step != "left":
    print("Fall into a hole. Game Over.")
else:
    step_two = input("Swim or wait\n").lower()
    if step_two != "wait":
        print("Attacked by trout. Game Over.\n")
    else:
        step_three = input("Which door? (Red, Blue or Yellow)\n").lower()
        if step_three == "red":
            print("Burned by fire. Game Over.\n")
        elif step_three == "blue":
            print("Eaten by beasts. Game Over.\n")
        elif step_three == "yellow":
            print("You Win!\n")
        else:
            print("Game Over\n")
