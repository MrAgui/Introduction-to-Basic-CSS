# import pyperclip
# Need to automate creating files 
def makeDash(stringD):
    for a in stringD:
        if (a.isspace()) == True:
            stringD = stringD.replace(" ", "-")
    # newVar = print(stringD+".html")             
    newVar= stringD+".html"
    
    print(newVar)

    


makeDash("Inherit Styles from the Body Element");