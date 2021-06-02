from src.outfunctions.forShell import OutForShell

# ------------- now communicate way -------------
def infromCmd(text=""):
    return input(text)

def outforCmd(text):
    return print(text)
# -----------------------------------------------

if __name__=='__main__':
    while True:
        getInput = infromCmd()
        if getInput == "exit()":
            break
        elif getInput == "shell":
            command = infromCmd("write shell: ")
            out, err = OutForShell(command)
            if err != "":
                outforCmd("error: " + err)
            else:
                outforCmd(out)