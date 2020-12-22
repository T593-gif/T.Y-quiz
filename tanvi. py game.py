print('Hello, Welcome to T.Yquiz!!')
ans=input('Are you ready to give this quiz (YES/NO):')
score = 0
totalQ = 5

if ans == 'YES':
    ans=input("1, Who appoints the Attorney General of India?"
              'A)The President'
               'B)The Prime Minister')
    if ans == 'A':
        score+=1
        print('Right')
    else:
        print('Wrong')


    ans=input("2, Who was the first indian in space?"
              'A)Vikram Ambalal'
               'B)Rakesh Sharma')
    if ans == 'B':
        score+=1
        print('Right')
    else:
        print('Wrong')

    
    ans=input("3, Who was the first indian scientist to win a Nobel Prize?"
              'A)CV Raman'
               'B)Amartya Sen')
    if ans == 'A':
        score+=1
        print('Right')
    else:
        print('Wrong')


    ans=input("4, Who was the first indian woman to win the Miss World Title?"
              'A)Aishwarya Rai'
               'B)Reia Faria')
    if ans == 'B':
        score+=1
        print('Right')
    else:
        print('Wrong')
    

    ans=input("5, Who was the first indian scientist to win the Booker Prize?"
              'A)Arundhati Roy'
               'B)Aravind Adiga')
    if ans == 'A':
        score+=1
        print('Right')
    else:
        print('Wrong')

print('Thans for playing you got',score,"Q correct")
mark= (score/totalQ)*10

print("Mark: ", mark)
print("Goodbye")
    

