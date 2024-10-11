def printLetterGrade():
    num= int(input())
    if num >=90 and num <= 100:
        print("A")
    if num >=80 and num<=90:
        print("B")

    if num >=70 and num<=80:
        print("C")

    if num >=55 and num<=70:
        print("D")

    if num >=50 and num<=55:
        print("E")

def rps():
    choice1 = input()
    choice2 = input()

    if  choice1== "scissors" and choice2 =="paper":
        print ("player1 wins")


if __name__ =="__main__":
    printLetterGrade()
    rps()


