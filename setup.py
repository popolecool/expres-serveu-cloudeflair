import subprocess
    #pour python3
# We load the newline seperated commands from the commands file. 
    #with open("commands.txt", "r") as fh:
    # We use the readlines() method to get a list of all the lines in the file.
#    cmds = fh.readlines()
#    for item in cmds:
    # We run each command using the subprocess.run() function in Python.
#        subprocess.run(item.split(" "))

with open("commands.txt", "r") as fh:
    cmds = fh.readlines()
    for item in cmds:
        subprocess.call(item.split(" "))