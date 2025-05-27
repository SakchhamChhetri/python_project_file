import csv
def append_1():

    f=open("data_of_med.csv","a",newline="")
    fw=['id','name','age','disease','note']
    writer=csv.writer(f)
    writer.writerow(fw)
    rec=[]
    while True :
        ab=input("enter the id no:")
        a=input('''enter the name of the patient:''')
        b=input("enter the age of the patient:")
        c=input("enter the disease of the patient:")
        d=input("enter any note for the patient if any or type nil: ")
        my=[ab,a,b,c,d]
        rec.append(my)
       
        e=input(''' 1)Add data
                2)Exist
                :-''')
        if e=='2':
            break
        else :
            continue
    for i in rec:
            writer.writerow(i)
        
    f.close()

def search_1():
    f=open("data_of_med.csv","r")
    reader=csv.reader(f)
    
    while True :
        p=0
        a=input("Enter the last Id of the patient to search :")
        for i in reader:
            if i[0]==a:
                print(i)
                p=1
        if p!=1:
            print("record unavailable ")
        b=input(''' want to search more 
                1)yes
                2)no''')
        if b=='1' or b=='yes':
            continue
        else :
            break


while True:
    print(''' what operation do you want to perform???
          1)Add the patient info
          2)search the patient info
          3)exist''')
    a=input(":-")
    if a=='1':
        append_1()
    elif a=='2':
        search_1()
    else:
        break