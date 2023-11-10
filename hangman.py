from random import *
import time
d=5
def main():
    with open('cars.csv','r+') as f:
        r=f.read()
        l=[]
        s=''
        w=''
        for i in range(136):
            if(r[i]!='\n'):
                s+=r[i]
            else:
                l.append(s)
                s=""
        print('\n','*'*29,"WELCOME TO HANGMAN",'*'*29,'\n')
        time.sleep(2)
        try:
            choose=int(input("""Difficulty: Beginner - Enter a letter freely without needing to specify the
position of the letter
Expert - Enter a letter in specific positions
Choose your difficulty
1 - Beginner
2 - Expert: """))
            if(choose==1):
                print("\n")
                print("*"*79)
                print("""You have chosen beginner mode
In case you don't know the rules,
. A word will be displayed partially on the screen and you have two options.
. 1st option - Guess the entire word
. 2nd option - Guess individual letters.
. You have 5 tries.
Good luck!!\n""")
            elif(choose==2):
                print("\n")
                print("*"*79)
                print("You have chosen expert mode")
                print(""". A word will be displayed partially on the screen and you have two options.
. 1st option - Guess the entire word.
. 2nd option - Guess individual letters specifying dash numbers.
. You have 5 tries
Good luck!!\n""")
            else:
                print("Enter a valid choice")
                time.sleep(1)
                main()
            print("Generating word...")
            time.sleep(2)
            print("The word is\n")
            t=randint(0,19)
            w=l[t].upper()
            g=''
            hints=[]
            go=0
            x=randint(len(w)//2,(len(w)//2)+1)
            for i in range(x):
                y=randint(1,len(w)-1)
                if(y not in hints):
                    hints.append(y)
            hints.sort()
            for i in range(len(w)):
                if(i not in hints):
                    g+='_'
                else:
                    g+=w[hints[go]].upper()
                    go+=1
            v=[g[i] for i in range(len(g))]
            for i in range(len(g)):
                print(g[i],end=" ")
            if(choose==1):
                beginner(w,d,v)
            elif(choose==2):
                expert(w,d,v)
        except:
            print("Invalid character entered")
            time.sleep(1)
            main()
def expert(w,d,v):
    try:
        while('_' in v):
            while(d>0):
                u=int(input("""\n\n1. Guess entire word
2. Guess character in specific dash number
Enter choice: """))
                if u==1:
                    s=input("Enter word: ")
                    if(w.upper()==s.upper()):
                        right(w,d)
                    for i in range(len(s)):
                        if(s[i] in '0123456789'):
                            print("\nOnly characters allowed\n")
                            time.sleep(1)
                            for i in range(len(v)):
                                    print(v[i],end=" ")
                            expert(w,d,v)
                    else:
                        d-=1
                        wrong(w,d)
                        print("You have",d,"attempts left")
                elif u==2:
                    try:
                        dash=int(input("Enter the position of the dash number: "))
                        if(dash>0 and dash<=len(v)):
                            b=dash-1
                            if(v[b]=='_'):
                                  c=input("Enter character: ")
                                  nm=c.upper()
                                  print("\n")
                                  if(nm==w[b]):
                                      v[b]=w[b].upper()
                                      for i in range(len(v)):
                                          print(v[i],end=" ")
                                      expert(w,d,v)
                                  elif(nm in '0123456789'):
                                      print("Only characters allowed\n")
                                      time.sleep(1)
                                      for i in range(len(v)):
                                          print(v[i],end=" ")
                                      expert(w,d,v)
                                  else:
                                      d-=1
                                      wrong(w,d)
                                      print("\nYou have",d,"attempts left\n")
                                      time.sleep(1)
                                      for i in range(len(v)):
                                          print(v[i],end=" ")
                            else:
                                print("\nYou have entered the index of a found element\n")
                                time.sleep(1)
                                for i in range(len(v)):
                                          print(v[i],end=" ")
                                continue
                        else:
                            print("\nDash position starts from 1 till",len(v)," \n")
                            time.sleep(1)
                            for i in range(len(v)):
                                    print(v[i],end=" ")
                            expert(w,d,v)
                    except:
                        print("\nEnter a valid character\n")
                        for i in range(len(v)):
                                print(v[i],end=" ")
                        expert(w,d,v)
                else:
                    print("\nEnter a valid choice\n")
                    time.sleep(1)
                    for i in range(len(v)):
                                print(v[i],end=" ")
                    expert(w,d,v)
        print('\n')
        right(w,d)
    except:
            print("You have entered an incorrect character")
            time.sleep(1)
            choice=input("Try again? (Y/N): ")
            if(choice in 'Yy'):
                print('\n')
                for i in range(len(v)):
                            print(v[i],end=" ")
                expert(w,d,v)
            elif(choice in 'Nn'):
                exit()
            else:
                print("Command not found... Going to main menu\n")
                main()
def beginner(w,d,v):
    while('_' in v):
        while(d>0):
            try:
                indexes=[]
                u=int(input("""\n\n1. Guess entire word
2. Guess character
Enter choice: """))
                if u==1:
                    s=input("Enter word: ")
                    if(w.upper()==s.upper()):
                        right(w,d)
                    for i in range(len(s)):
                        if(s[i] in '0123456789'):
                            print("\nOnly characters allowed\n")
                            time.sleep(1)
                            for i in range(len(v)):
                                    print(v[i],end=" ")
                            beginner(w,d,v)
                    else:
                        d-=1
                        wrong(w,d)
                        print("You have",d,"attempts left")
                        time.sleep(1)
                        for i in range(len(v)):
                                print(v[i],end=" ")
                elif u==2:
                    c=input("Enter character: ")
                    nm=c.upper()
                    if(nm in w):
                        for i in range(len(w)):
                            if(nm==w[i]):
                                indexes.append(i)
                                for i in indexes: 
                                    v[i]=w[i].upper()
                                if('_' not in v):
                                    right(w,d)
                    elif(nm in '0123456789'):
                        print("\nOnly characters allowed\n")
                        time.sleep(1)
                        for i in range(len(v)):
                                    print(v[i],end=" ")
                        beginner(w,d,v)
                    else:
                        d-=1
                        wrong(w,d)
                        print("You have",d,"attempts left\n")
                        time.sleep(1)
                    for i in range(len(v)):
                            print(v[i],end=" ")
                    beginner(w,d,v)
                else:
                    print("\nEnter a valid choice\n")
                    time.sleep(1)
                    for i in range(len(v)):
                                    print(v[i],end=" ")
                    beginner(w,d,v)
            except:
                    print("You have entered an incorrect character")
                    time.sleep(1)
                    choice=input("\nTry again? (Y/N): ")
                    if(choice in 'Yy'):
                        print('\n')
                        for i in range(len(v)):
                                    print(v[i],end=" ")
                        beginner(w,d,v)
                    elif(choice in 'Nn'):
                        main()
                    else:
                        print("Command not found... Going to main menu\n")
                        main()
        print('\n')
        right(w,d)   
def wrong(w,d):
    if(d==4):
        print("+----") 
        print("|   |")
        print("|   O")
        print("|   |")
        print("|")
        print("|")
        print("|")
        print("---")
    elif(d==3):
        print("+----") 
        print("|   |")
        print("|   O")
        print("|  /|")
        print("|")
        print("|")
        print("|")
        print("---")
    elif(d==2):
        print("+----") 
        print("|   |")
        print("|   O")
        print("|  /|\ ")
        print("|")
        print("|")
        print("|")
        print("---")
    elif(d==1):
        print("+----") 
        print("|   |")
        print("|   O")
        print("|  /|\ ")
        print('|    \ ')
        print("|")
        print("|")
        print("---")
    else:
        print("+----") 
        print("|   |")
        print("|   O")
        print("|  /|\ ")
        print("|  / \ ")
        print("|")
        print("|")
        print("---")
        print("You have no attempts left")
        print("\nThe answer was:",w)
        i=input("Try again? (Y/N): ")
        if(i in 'Yy'):
            main()
        elif(i in 'Nn'):
            exit()
        else:
            print("\nCommand not found...Going to main menu")
            main()
def right(w,d):
    print("\nYou have successfully guessed the word with",d,"attempts remaining")
    i=input("Try again? (Y/N): ")
    if(i in 'Yy'):
        main()
    elif(i in "Nn"):
        exit()
    else:
        print("\nCommand not found...Going to main menu")
        main()
main()   
    


