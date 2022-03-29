import mysql.connector as sqltor
mydb=sqltor.connect(host='localhost', user='root', passwd='iamks', database='khushaal')
mycur=mydb.cursor()
#quizsys (pname,sex,nationality,score)(It is the table used by the system under the database khushaal)
def adddata(n,s):
    str="INSERT INTO quizsys VALUES('{}','{}','{}',{})"

    pname=n
    sex=input('Enter your sex(M/O/F):')
    nation=input('Enter your nationality:')
    score=int(s)
    query=str.format(pname,sex,nation,score)

    mycur.execute(query)
    mydb.commit
def updatedata(n,s):
    str="UPDATE quizsys SET Score={} WHERE Pname='{}'"

    name=n
    score=int(s)
    query=str.format(score,name)

    mycur.execute(query)
    mydb.commit
def deletedata(n):
    name=n

    stm="DELETE FROM quizsys WHERE Pname='{}'"
    query=stm.format(name)
    mycur.execute(query)
    mydb.commit()
def fetchdata():
    query="SELECT* FROM quizsys ORDER BY Score DESC"
    mycur.execute(query)

    result=mycur.fetchall()
    print('>=<>=<>=<>=<>=<>=<>=<>=SCOREBOARD=<>=<>=<>=<>=<>=<>=<>=<>=<>=<')
    print('==============================================================')
    print('PLAYER\tSEX\tNATIONALITY\tSCORE')
    print('==============================================================')
    for x in result:
        str="{}\t{}\t{}\t\t{}"
        print(str.format(x[0],x[1],x[2],x[3]))
def maxdata():
    query="SELECT* FROM quizsys WHERE Score=(SELECT MAX(Score) FROM quizsys)"
    mycur.execute(query)
    result=mycur.fetchall()
    print('>=<>=<>=<>=<>=<>=<>=<>=WINNER=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<')
    print('=============================================================')
    print('PLAYER\tSEX\tNATIONALITY\tSCORE')
    print('=============================================================')
    for x in result:
        str="{}\t{}\t{}\t\t{}"
        print(str.format(x[0],x[1],x[2],x[3]))
def lifelineab(q):
    i=q.find('(C)')
    newq=q.replace(q[i:],'')
    print(newq)
def lifelinecd(q):
    k=q.find('(A)')
    i=q.find('(C)')
    newq=q.replace(q[k:i+1],'')
    print(newq)

   
ch=True
while ch==True:
    print("\t    ===     ==     ==  ===   ===============")
    print("\t  ==   ==   ==     ==  ===               ===")
    print("\t ==     ==  ==     ==  ===             ===  ")
    print("\t==       == ==     ==  ===          ===     ")
    print("\t ==  =  ==  ==     ==  ===       ===        ")
    print("\t  ==  ===   =========  ===   ===            ")
    print("\t    === ==  =========  ===   ===============")
    

    
    print('=========================================================')
    print('\t\tMENU')
    print('=========================================================')
    print('1.) Play Game')
    print('2.) Scoreboard')
    print('3.) About Us')
    print('4.) Exit')
    print()
    choice=int(input('Enter your choice from the above menu:'))
    
    if choice==1:
        ncon=str(input('Are you new to the game?(Y/N):'))
        if ncon=='Y' or 'y':
            newn=input('Enter your name:')
        elif ncon=='N' or 'n':
            oldn=input('Enter your name which you have used at your last game:')
        print()
        print()
        print('=====================================================================')
        print()
        print()
        print('\tINSTRUCTIONS TO PLAY THE GAME')
        print()
        print('1.) This quiz has G.K. questions related to computer science.')
        print('2.) You cannot leave any question empty.')
        print('3.) There are 12 questions in this quiz.')
        print('4.) There are four options against each question.')
        print('5.) You will be awarded 100 points for every correct answer and -10 for every wrong answer.')
        print('6.) You will be provided 3 50:50 lifelines(Two wrong options will be eliminated).')
        print('7.) You are requested to kindly keep your CAPS LOCK ON for all the entries (answers, options, entry, etc.).')
        print()
        print()
        print('\t\t\tTHE SHOW BEGINS!!!!')
        print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
        print()
        print()
        s=0;u=0# where s is count for score and u is count for lifeline.
        q1='Q1 Which day is celebrated as World Computer Literacy Day?\n(A)December 2\t(B)July 3\n(C)September 5\t(D)October 9'
        print(q1)
        life1=str(input('Do you want to use the 50:50 lifeline?(Y/N):'))
        if life1=='Y':
            lifelineab(q1)
            u+=1
        elif life1=='N':
            pass
            
        ans1=input('Enter your option:')
        if ans1=='A':
            print('CORRECT!!!! Keep Going')
            s=s+100
        else:
            print('SORRY!!! You are wrong')
            s=s-10
        print()
        print()
        print()
        print()
        print()
        q2='Q2 LongHorn was the code name of?\n(A)Windows 7\t(B)Windows xp\n(C)Windows Vista\t(D)Macintosh'
        print(q2)
        life2=input('Do you want to use the 50:50 lifeline?(Y/N):')
        print()
        print()
        if life2=='Y':
            lifelinecd(q2)
            u+=1
        elif life2=='N':
            pass
        ans2=input('Enter your option:')
        if ans2=='C':
            print('CORRECT!!!! Keep Going')
            s=s+100
        else:
            print('SORRY!!! You are wrong')
            s=s-10
        print()
        print()
        print()
        print()
        print()
        q3='Q3 Which term means people who work with the computer?\n(A)Hardware\t(B)Liveware\n(C)Software\t(D)Scareware'
        print(q3)
        life3=input('Do you want to use the 50:50 lifeline?(Y/N):')
        print()
        print()
        print()
        if life3=='Y':
            u+=1
            lifelineab(q3)
        elif life3=='N':
            pass
        ans3=input('Enter your option:')
        if ans3=='B':
            print('CORRECT!!!! Keep Going')
            s=s+100
        else:
            print('SORRY!!! You are wrong')
            s=s-10
        print()
        print()
        print()
        print()
        print()
        q4='Q4 Who invented Compact Disc?\n(A)Charles Babbage\t(B)Charles Bachman\n(C)James T Russel\t(D)John Backus'
        print(q4)
        life4=input('Do you want to use the 50:50 lifeline?(Y/N):')
        print()
        print()
        print()
        if life4=='Y':
            if u==3:
                print('Sorry you have used your all lifelines')
            elif u<3:
                lifelinecd(q4)
                u+=1
        elif life4=='N':
            pass
       
        ans4=input('Enter your option:')
        if ans4=='C':
            print('CORRECT!!!! Keep Going')
            s=s+100
        else:
            print('SORRY!!! You are wrong')
            s=s-10
        print()
        print()
        print()
        print()
        print()
        q5="Q5 'Do no evil' is the tagline of which tech company?\n(A)Microsoft\t(B)Sun Microsystems\n(C)Apple\t(D)Google"
        print(q5)
        life5=input('Do you want to use the 50:50 lifeline?(Y/N):')
        print()
        print()
        print()
        if life5=='Y':
            if u==3:
                print('Sorry you have used your all lifelines')
                pass
            elif u<3:
                lifelinecd(q5)
                u+=1
        elif life5=='N':
            pass
        ans5=input('Enter your option:')
        if ans5=='D':
            print('CORRECT!!!! Keep Going')
            s=s+100
        else:
            print('SORRY!!! You are wrong')
            s=s-10
        print()
        print()
        print()
        print()
        print()
        q6='Q6 First Indian cinema released through internet is?\n(A)DDLJ\t\t(B)Vivah\n(C)Maine Pyaar Kiya\t(D)Main Hoon Na'
        print(q6)
        life6=input('Do you want to use the 50:50 lifeline?(Y/N):')
        print()
        print()
        print()
        if life6=='Y':
            if u==3:
                print('Sorry you have used your all lifelines')
                pass
            elif u<3:
                lifelineab(q6)
                u+=1
        elif life6=='N':
            pass
        ans6=input('Enter your option:')
        if ans6=='B':
            print('CORRECT!!!! Keep Going')
            s=s+100
        else:
            print('SORRY!!! You are wrong')
            s=s-10
        print()
        print()
        print()
        print()
        print()
        q7="Q7 World's first microprocessor is?\n(A)Intel 8080\t(B)IBM zEC12\n(C)Intel 4004\t(D)None of these"
        print(q7)
        life7=input('Do you want to use the 50:50 lifeline?(Y/N):')
        print()
        print()
        print()
        if life7=='Y':
            if u==3:
                print('Sorry you have used your all lifelines')
                pass
            elif u<3:
                lifelinecd(q7)
                u+=1
        elif life7=='N':
            pass
        ans7=input('Enter your option:')
        if ans7=='C':
            print('CORRECT!!!! Keep Going')
            s=s+100
        else:
            print('SORRY!!! You are wrong')
            s=s-10
        print()
        print()
        print()
        print()
        print()
        q8="Q8 Which IT company has its nickname as 'THE BIG BLUE'?\n(A)IBM\t(B)Wipro\n(C)Facebook\t(D)None of these"
        print(q8)
        life8=input('Do you want to use the 50:50 lifeline?(Y/N):')
        print()
        print()
        print()
        if life8=='Y':
            if u==3:
                print('Sorry you have used your all lifelines')
                pass
            elif u<3:
                lifelineab(q8)
                u+=1
        elif life8=='N':
            pass
        ans8=input('Enter your option:')
        if ans8=='A':
            print('CORRECT!!!! Keep Going')
            s=s+100
        else:
            print('SORRY!!! You are wrong')
            s=s-10
        print()
        print()
        print()
        print()
        print()
        q9='Q9 Orkut.com is now owned by which IT company?\n(A)Microsoft\t(B)Apple\n(C)HP\t(D)Google'
        print(q9)
        life9=input('Do you want to use the 50:50 lifeline?(Y/N):')
        print()
        print()
        print()
        if life9=='Y':
            if u==3:
                print('Sorry you have used your all lifelines')
                pass
            elif u<3:
                lifelinecd(q9)
                u+=1
        elif life9=='N':
            pass
        ans9=input('Enter your option:')
        if ans9=='D':
            print('CORRECT!!!! Keep Going')
            s=s+100
        else:
            print('SORRY!!! You are wrong')
            s=s-10
        print()
        print()
        print()
        print()
        print()
        q10="Q10 'Weaving the web' was written by?\n(A)Tim Burners Lee\t(B)Larry Page\n(C)Bill Gates\t(D)Jeff Bezos"
        print(q10)
        life10=input('Do you want to use the 50:50 lifeline?(Y/N):')
        print()
        print()
        print()
        if life10=='Y':
            if u==3:
                print('Sorry you have used your all lifelines')
                pass
            elif u<3:
                lifelineab(q10)
                u+=1
        elif life10=='N':
            pass
        ans10=input('Enter your option:')
        if ans10=='A':
            print('CORRECT!!!! Keep Going')
            s=s+100
        else:
            print('SORRY!!! You are wrong')
            s=s-10
        print()
        print()
        print()
        print()
        print()
        q11="Q11 Who is known as the 'Human Computer of India'?\n(A)Azim Premji\t(B)Narayan Murthy\n(C)Vinod Khosla\t(D)Shakuntala Devi"
        print(q11)
        life11=input('Do you want to use the 50:50 lifeline?(Y/N):')
        print()
        print()
        print()
        if life11=='Y':
            if u==3:
                print('Sorry you have used your all lifelines')
                pass
            elif u<3:
                lifelinecd(q11)
                u+=1
        elif life11=='N':
            pass
        ans11=input('Enter your option:')
        if ans11=='D':
            print('CORRECT!!!! Keep Going')
            s=s+100
        else:
            print('SORRY!!! You are wrong')
            s=s-10
        print()
        print()
        print()
        print()
        print()
        q12='Q12 Who invented Java?\n(A)Dennis Ritchie\t(B)Guido van Rossum\n(C)James A Gosling\t(D)Tim Berners Lee'
        print(q12)
        life12=input('Do you want to use the 50:50 lifeline?(Y/N):')
        print()
        print()
        print()
        if life12=='Y':
            if u==3:
                print('Sorry you have used your all lifelines')
                pass
            elif u<3:
                lifelinecd(q12)
                u+=1
        elif life12=='N':
            pass
        ans12=input('Enter your option:')
        if ans12=='C':
            print('CORRECT!!!! Keep Going')
            s=s+100
        else:
            print('SORRY!!! You are wrong')
            s=s-10
        print()
        print()
        print()
        print()
        print('********************THANKYOU FOR PLAYING THIS GAME********************')
        print()
        print('NO. OF LIFELINES USED:',u)
        print("YOUR TOTAL SCORE:",s)
        acc=input("Have played this game before?(Y/N):")
        if acc=='N':
            adddata(newn,s)
            print("Your entry has been added to the scoreboard.")
        if acc=='Y':
            n=input("Enter the name with which you played the game last time:")
            updatedata(n,s)
            print("Your score has been updated.")
        print()
        print()
        print()
        print('\t...+...+...+...+...+...+...+...+...+...+...+...+...+...+...+...+...+...+...+...+...+...+...+...')
        print()
        print()
    if choice==2:

        print('\t2.1) Delete a record')
        print('\t2.2) Display Scoreboard')
        print('\t2.3) First Position')
        
        choice2=float(input('Enter your choice(2.1/2.2/2.3):'))
        if choice2==2.1:
            name=input('Enter the name which you want to delete from the scoreboard:')
            deletedata(name)
            print('The entry for',name,' is deleted... check scoreboard.')
        elif choice2==2.2:
            fetchdata()
        elif choice2==2.3:
            maxdata()
        print()
        print()
        print()
    if choice==3:
        print('*******************This quiz sysytem is created by a team of Khushaal and Krishna under the guidance of our teacher Yash Kant Sir.*******************')
        print()
        print()
        print()

    if choice==4:
        print("HOPE YOU LIKED OUR SYSTEM!!!")
        print("HAVE A NICE DAY....")
        print("EXITING FROM SYSTEM....")
        ch=False
    
        
        
        
