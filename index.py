import pandas as pd
import os
import csv
from csv import writer
#append_list_as_row(strri,["Time","Max","Min","Avg","Delay","Fill Level","Received Frames","Idle Frames Sent","DateTime"])
def append_list_as_row(file_name, list_of_elem):
        # Open file in append mode
        with open(file_name, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(list_of_elem)
#to see what files are present in the folder
def login():
    print("Enter the Username")
    username=input()
    print("Enter the Password")
    password=input()
    if(username=="admin"):
        if(password=="admin"):
            print("Welcome")
            #write a function to display choices to 1. add new user 2. view new user entry 3. update a user entry
            userform()
        else:
            print("You have entered a wrong username or password")
            login()
    else:
        print("You have entered a wrong username or password")
        login()


#write a function to display choices to 1. add new user 2. view new user entry 3. update a user entry
def userform():
   
    checkstr=True
    while(checkstr):
        print("\n")
        print("Enter \n1. add new user \n2. view user info \n3. update a user entry \n4. Weekly info \n5. Monthly info \n6. Exit")
        switchint=input()
        #1. add new user
        if(switchint=="1"):
            print("Enter user name")
            name=input()
            print("Enter the Age of user")
            age=input()
            print("User is male or female")
            sex=input()
            print("Enter the height of the user in Meters")
            height=input()
            print("Enter the weight of the user in kg")
            weight=input()
            checkflag=1
            detailspathname="./details.csv"
            if not (os.path.isfile(detailspathname)):
                append_list_as_row(detailspathname,["Name","Age","Sex","Height","Weight"])
                
            else:
                #check if that name exists in the csv file
                df = pd.read_csv('./details.csv')
                namelist=df['Name']
                
                for i in namelist:
                    if(i==name):
                        print("User with same name has already been added\n")
                        checkflag=0
            if(checkflag==1):

                append_list_as_row(detailspathname,[name,age,sex,height,weight])
                append_list_as_row("./data/"+name+".csv",["Day No:","No: of steps","Time taken"])

        elif(switchint=="2"):
            print("Enter the name of the user you want info of\n")
            findinfoof=input()
            dfinfo = pd.read_csv('./details.csv')
            nameinfo=dfinfo['Name']
           
            infocheck=1
            count=0
            for k in nameinfo:
                if(k==findinfoof):
                    infocheck=0
                    print("Name :"+k+"\n")
                    print("Age :"+str(dfinfo['Age'][count])+"\n")
                    print("Sex :"+str(dfinfo['Sex'][count])+"\n")
                    print("Weight :"+str(dfinfo['Height'][count])+"\n")
                    print("Height :"+str(dfinfo['Weight'][count])+"\n")
                    BMI=dfinfo['Weight'][count]/(dfinfo['Height'][count]*dfinfo['Height'][count])
                    print("BMI : "+str(BMI)+"\n")
                    if( BMI<18.5):
                        print("BMI depicts that the user is Underweight\n")
                    elif(BMI>=18.5 | BMI<=24.9):
                        print("BMI depicts that the user is Normal weight")
                    elif(BMI>24.9 | BMI<=29.9):
                        print("BMI depicts that the user is Overweight\n")
                    else:
                        print("BMI depicts that the user is Obese\n")
                count=count+1
            if( infocheck==1):
                print("The entered user has not been registered please register the user before viewing his info\n")

        elif(switchint=="3"):
            print("enter the name of user for which workout update is to be inputed\n")
            nameworkout=input()
            dfinfo = pd.read_csv('./details.csv')
            nameinfo=dfinfo['Name']
           
            infocheck=1
             
            for k in nameinfo:
                if(k==findinfoof):
                    storename=k
                    infocheck=0

            if(infocheck==1):
                print("The entered user has not been registered please register the user before adding any inputs\n")
            else:
                print("Enter the Day number which represent the following 1:Mon 2:Tue 3:Wed 4:Thr 5:Fri 6:Sat 7:Sun\n")
                day=input()
                print("Enter the number of steps taken\n")
                steps=input()
                print("Enter the time taken in minutes\n")
                timetaken=input()
                append_list_as_row("./data/"+storename+".csv",[day,steps,timetaken])
        elif(switchint=="4"):
            print("enter the name of user for which one week avg is to be seen\n")
            nameworkout=input()
            dfinfo = pd.read_csv('./details.csv')
            nameinfo=dfinfo['Name']
           
            infocheck=1
             
            for k in nameinfo:
                if(k==nameworkout):
                    storename=k
                    infocheck=0
            if(infocheck==1):
                print("Please register the user\n")
            else:
                df=pd.read_csv("./data/"+storename+".csv")
                lengthofdb=len(df)
                stepstaken=df['No: of steps']
                
                if(lengthofdb<7):
                    print("week hasn't been completed yet enter full weeks data\n")
                else:
                    tdis=0
                    ttime=0
                    countholidays=0
                    for i in range(7):
                        if(df['Time taken'][lengthofdb-i-1]!=0):
                            print(df['Time taken'][lengthofdb-i-1])
                            tdis=tdis+(stepstaken[lengthofdb-i-1]*0.0007)
                            ttime=ttime+int(df['Time taken'][lengthofdb-i-1])
                            #print(ttime)
                        else:
                            countholidays=countholidays+1

                    Weeklyavg=tdis/(ttime/60)
                    print("Weekly Average: "+str(Weeklyavg)+" Km/hr\n")
                    print("The user had taken "+str(countholidays)+" days holiday\n")
                    maxsteps=max(df['No: of steps'])
                    maxtime=max(df['Time taken'])
                    print("The user had taken max steps of "+str(maxsteps)+" during this week\n")
                    print("The max time walked by the user is "+str(maxtime)+" min during this week\n")
                    if(countholidays==0):
                        print("The user has been awarded for the week\n")
                    else:
                        print("The user has not been awarded as he took holidays\n")

        elif(switchint=="5"):
            print("Enter the name of user for whome you want to find one months data\n")
            nameworkout=input()
            dfinfo = pd.read_csv('./details.csv')
            nameinfo=dfinfo['Name']
           
            infocheck=1
             
            for k in nameinfo:
                if(k==nameworkout):
                    storename=k
                    infocheck=0
            if(infocheck==1):
                print("Please register the user\n")
            else:
                df=pd.read_csv("./data/"+storename+".csv")
                lengthofdb=len(df)
                stepstaken=df['No: of steps']
                
                if(lengthofdb<28):
                    print("entire months data hasn't been completed yet enter full full months data\n")
                else:
                    tdis=0
                    ttime=0
                    countholidays=0
                    holi=[0,0,0,0]
                    v=0
                    for i in range(28):
                        if(df['Time taken'][lengthofdb-i-1]!=0):
                            print(df['Time taken'][lengthofdb-i-1])
                            tdis=tdis+(stepstaken[lengthofdb-i-1]*0.0007)
                            ttime=ttime+int(df['Time taken'][lengthofdb-i-1])
                            #print(ttime)
                            if((i+1)%7==0):

                                if(countholidays>0):
                                    holi[v]=1
                                    
                                countholidays=0
                                v=v+1
                        
                        else:
                            countholidays=countholidays+1
                            if((i+1)%7==0):

                                if(countholidays>0):
                                    holi[v]=1
                                   
                                countholidays
                                v=v+1

                    monthlyavg=tdis/(ttime/60)
                    print("Monthly Average: "+str(Weeklyavg)+" Km/hr\n")
                    maxsteps=max(df['No: of steps'])
                    maxtime=max(df['Time taken'])
                    print("The user had taken max steps of "+str(maxsteps)+" during this week\n")
                    print("The max time walked by the user is "+str(maxtime)+" min during this week\n")
                    for iter in range(4):
                        if(holi[iter]==0):
                            print("The user has been awarded for the "+iter+" week\n")
                        else:
                            print("The user has put leave in the "+iter+" week, hence not been awarded for that week\n")

                     



        else:
            checkstr=False


         

login()



