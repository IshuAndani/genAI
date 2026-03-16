import os

def run(cmd:str):
    return os.system(cmd)

cmd = input("enter command:")

while(cmd != "exit"):
    run(cmd)
    cmd = input("enter command:")
    
