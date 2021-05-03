n=18
i=0
while (i<10):
    x = int(input("Guess the no"))
    if x>n:
        print("ur no is greater")
        print("this is ur",i,"left out of 9")
    elif x<n:
        print("ur no is smaller")
        print("this is ur",i,"left out of 9")
    elif x==n:
        print("YOU GUESSED RIGHT")
        break
    else:
        continue
    i=i+1
