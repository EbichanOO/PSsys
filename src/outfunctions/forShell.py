# run unix command function
import subprocess, sys
def OutForShell(command=""):
    if command == "":
        # if out command isn't exist, doesn't operate this function
        return "", ""
    output = ""
    err = ""
    tmp = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if tmp.returncode != 0:
        tmp = subprocess.run(command, shell=True, stderr=subprocess.PIPE, universal_newlines=True)
        err = tmp.stderr
    else:
        output = tmp.stdout
    return output, err

if __name__=='__main__':
    ou= OutForShell("ls-la")
    print(ou)