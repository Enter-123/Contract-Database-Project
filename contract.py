import database


def choice():
    while True:
        print()
        print("1 Add Contract")
        print("2 Remove Contract")
        print("3 View Contract")
        print("4 Exit Program")
        choic = int(input("Enter Your Choice :"))
        print()

        if choic == 1:
            count = int(input("Enter Number of contact to add : "))
            for i in range(count):
                name = input("Enter Your Name : ")
                num = int(input("Enter Your Number : "))
                database.add(name,num)
                print()
            print()
            print(i+1,"Contract Added Successfully\n")
            print()

        elif choic == 2:
            number = int(input("Enter the number to remove : "))
            database.remove(number)
            
        elif choic == 3:
            database.view()

        elif choic == 4:
            print("\n....   Exiting    ....")
            break

        else:
            print("-------Invalid Input")

choice()











