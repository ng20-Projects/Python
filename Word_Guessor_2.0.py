import random
#import emoji
print("Welcome to Number Guessor !!!@@__||")
print("          ")
print("Life only gives you some chances and I give you only 20 chances to predict the right number :)")

#extra values
n=0
count=0
f=0
k=0
o=0
#end

b=[2,20,91,89,66,19,314,47,287,23]
#x=['(>'-')>','◕_◕','( ಥـْـِـِـِـْಥ)','']
c = random.randint(0,9)
for i in range(0,20):
    try:
        a=int(input("Enter the number-> "))
        count=count+1
        if(a<b[c]):
            print(" ◕_◕ Entered number is lesser than the correct answer.    Chances Used:",count)
        elif(a>b[c]):
            print(" ◕_◕ Entered number is greater than the correct answer.   Chances Used:",count)
        else:
            k=0
            print("Entered number is Correct.")    
            print("(ツ) Congratulations!!! You got the right answer |:D")
            #print(emoji.emojize(":grinning_face_with_big_eyes:"))
            break
    except ValueError:
        print(" ಠ_ಠ You have entered an invalid input. Please enter only INTERGER")
        i=i-1
        count=count-1
        if(f==0):
            print("   Don't Worry your number of chances will not reduce :)")
            f=1
    if(i==9):
            print("Can't able to predict ¯\_('_')_/¯")
            while(k==0):    
                g=input("DO you want to know the answer: y/n-> ")
                if(g=='y'):
                    print("The correct answer is",b[c])
                    o=1
                    k=1
                elif(g=='n'):
                    k=1
                else:
                    print("Enter y/n only....")    
            if(o==1):
                break

if(count==20):
    print("     ")
    print("   (-_(-_(-_(-_-)_-)_-)_-)")
    print("   X_X Sorry but you LOSE X_X") 
    print("(>'-')> sBetter luck next time :) :) :)")