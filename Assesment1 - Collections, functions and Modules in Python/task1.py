import datetime

while True:
    s="""
    Welcome to Python E-Note
    
    Press 1 for generate Note
    Press 2 for view note
    Press 3 for exit
    """
    print(s)
    choice=int(input("Enter your choice="))
    if choice==1:
        try:
            a=(input("Enter Python E-note generate Name="))
        except:
            print("Invalid output")
            a=(input("Enter Python E-note generate Name="))
        

        b=input("Enter Python E-note Title=")
        c=input("Enter E-note Content=")
        file=open("task.txt","w")
        for i in a,b,c:
            file.write('%s\n'%i)
    
            
    elif choice==2:
        print("----------------------------")
        print(datetime.datetime.now())
        print("Enter Python E-note generate Name=",a) 
        print("Enter Python E-note Title=",b)
        print("Enter E-note Content=",c)   

    else:
        break

    