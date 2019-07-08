import os
import io
import json
import random

savefile = "save.txt"
maxpoolnum = 185
right_ans = ['y', 'Y', 'n', 'N']

def prYellow(skk): print("\033[93m{}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m{}\033[00m" .format(skk))

def main():
    # initial set
    prYellow("\n===== Welcome to use pickTopic =====")
    nonnewsave = False
    if os.path.exists(savefile):
        while True:
            ans = input("\nWould you like to begin a new savefile?\n(y/n): ")
            if ans in right_ans:
                break
        nonnewsave = True if ans == 'n' or ans == 'N' else False

    # open the topic & save files
    with open('pool.txt','r', encoding="utf-8") as f:
        lines = f.readlines()
    if nonnewsave:
        with open(savefile, 'r') as f1:
            num = json.load(f1)
    else:
        num = list(range(maxpoolnum))

    # pick a topic randomly
    pick = int(random.choice(num))
    print(f"\nWe choose the topic #{pick} for you! :)")
    print("And here comes your writing topic:\n")
    prPurple(lines[pick])
    num.remove(pick)
    with open(savefile, 'w') as f1:
        json.dump(num, f1)
    prYellow("Thanks for using pickTopic. Have a nice day!\n")

if __name__ == "__main__":
    main()
