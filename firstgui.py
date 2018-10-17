

from easygui import *
import sys
while 1:
    msgbox("E.Y.Bazar")

    msg ="Select your online shopping site"
    title = "Online shopping"
    choices = ["Amazon", "Flipcart", "Snapdeal"]
    choice = choicebox(msg, title, choices)
    if  choices=="Flipcart":
        choices1 = ["Shirts","Jeans","T-shirts"]
        choice = choicebox(msg,choices1)
        msgbox("You choose:"+ str(choices1))
    elif  choices=="Amazon":
          choices1 = ["Shirts","Jeans","T-shirts"] 
          choice = choicebox(msg,choices1)
    elif  choices=="Snapdeal":
          choices1 = ["Shirts","Jeans","T-shirts"] 
          choice = choicebox(msg,choices1)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("You chose: " + str(choice), "Online box")
    

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)


