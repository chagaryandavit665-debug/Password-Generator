import random

letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
           'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
symnum = ['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','?']
password = ''

def lenpask1():
    lenp = int(input("------------------------------------\nHello bro!!!\nThis simple generator can make for you a specific secure password\nJust enter a number that must be the length of the password\n------------------------------------\n"))
    genpass(lenp)
def lenpask2():
    lenp = int(input(''))
    genpass(lenp)
def lenpask3():
    lenp = int(input('Please enter a number again\n'))
    genpass(lenp)

def genpass(lenp):

    def askyn():
        ans = input('The number you entered is very short and not recomended(LOW SECURITY!!!)\nDo you want to continiue?(y/n))')
        genpass1(ans)

    def genpass1(ans):
        
        if ans == "yes" or ans == "y":
            if lenp == 4:            
                randlist = random.sample(letters,k=2) + random.sample(symnum,k = 2)
                random.shuffle(randlist)
                password = ''.join(randlist)
                print(f"Your password generated successfully - \n---------------------\n{password}\n---------------------")
        
            if lenp == 5:            
                randlist = random.sample(letters,k=3) + random.sample(symnum,k = 2)
                random.shuffle(randlist)
                password = ''.join(randlist)
                print(f"Your password generated successfully - \n---------------------\n{password}\n---------------------")

            if lenp == 6:            
                randlist = random.sample(letters,k=3) + random.sample(symnum,k = 3)
                random.shuffle(randlist)
                password = ''.join(randlist)
                print(f"Your password generated successfully - \n---------------------\n{password}\n---------------------")

            if lenp == 7:            
                randlist = random.sample(letters,k=4) + random.sample(symnum,k = 3)
                random.shuffle(randlist)
                password = ''.join(randlist)
                print(f"Your password generated successfully - \n---------------------\n{password}\n---------------------")
        elif ans == 'no' or ans == 'n':
            lenpask3()

    if lenp > 3 and lenp < 8:
        askyn()

    elif lenp < 4:
        print("Number you entered is very short for password!!!\nTry a number bigger than 3\n")
        lenpask2()

    else:
        if lenp %2 == 0:            
            randlist = random.sample(letters,k=int(lenp/2)) + random.sample(symnum,k = int(lenp/2))
            random.shuffle(randlist)
            password = ''.join(randlist)
            print(f"Your password generated successfully - \n---------------------\n{password}\n---------------------")

        if lenp %2 != 0:            
            randlist = random.sample(letters,k=int((lenp/2)+(1/2))) + random.sample(symnum,k = int((lenp/2) + (1/2)))
            random.shuffle(randlist)
            password = ''.join(randlist)
            print(f"Your password generated successfully - \n---------------------\n{password}\n---------------------")
    

try:
    lenpask1()
except ValueError:
    print('Please enter a number!!\n..........................\n')
    lenpask()
