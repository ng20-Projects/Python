import csv
from termcolor import colored, cprint

def create_csv_file(CSV_file_name):
    with open(CSV_file_name,"w") as csvfile:
        writer=csv.writer(csvfile)
        Heading_List=input("Enter the Headings(Use ',' to seperate headings) :  ").split(',')
        writer.writerow(Heading_List)
        csvfile.close()
        print(f"\nEnter the value according to this -> {Heading_List}\n")
        entry_of_values(CSV_file_name)

def entry_of_values(CSV_file_name):
    with open(CSV_file_name,"a") as csvfile:
        writer=csv.writer(csvfile)
        Input_List=[]
        Input_List=input("Enter the values(Use ',' to seperate the Data): ").split(',')
        writer.writerow(Input_List)
        csvfile.close()
        if(input()):
            return
        else:
            entry_of_values(CSV_file_name)

def use_csv_file(CSV_file_name):
    try:
        get_value2=int(input("\n[+]Enter: "))

    except(ValueError):
        print(colored("\nEnter only Integer Value.\n",'red'))
        use_csv_file(CSV_file_name)

    if(get_value2==1):
        entry_of_values(CSV_file_name)
    else:
        create_csv_file(CSV_file_name)

def Start():
    try:
        get_value1=int(input("\n[+]Enter: "))

    except(ValueError):
        print(colored("\nEnter only Integer Value.\n",'red'))
        Start()

    if get_value1==1:
        CSV_file_name=input("Enter the name of the CSV File: ")
        if(not CSV_file_name[:-4:-1]=='csv'):
            CSV_file_name=f"{CSV_file_name}.csv"
        create_csv_file(CSV_file_name)

    elif get_value1==2:
        CSV_file_name=input("Enter the CSV File's name: ")
        if(not CSV_file_name[:-4:-1]=='csv'):
            CSV_file_name=f"{CSV_file_name}.csv"
        print("[*] Insert Data into the Old File (1)")
        print("[*] Overwrite Data into the Old File (2)")
        use_csv_file(CSV_file_name)

print("[*] Create a New CSV File (1)")
print("[*] Use an Old CSV File (2)")
Start()