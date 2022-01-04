import time
import os
import threading

configlist = []
with open("config.txt", "r") as f:
    configs = f.read().split("\n")
    for config in configs:
        config = config.split("//")[0].split(": ")[1]
        configlist.append(config)
        
for i in range(5):
    def p():
        os.system(f'node /main/main.js {configlist[0]} {configlist[1]} {configlist[2]} {configlist[3]} {configlist[4]} {configlist[5]}{str(i+1)} {configlist[6]}')
    t = threading.Thread(target=p)
    t.start()
    time.sleep(6)
