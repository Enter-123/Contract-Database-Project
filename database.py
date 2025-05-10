contract = []

def add(name,no):
    for entry in contract:
        if no in entry.values():
            print("Contract with this Number already Exits. ")
            return
    contract.append({name.lower():no})
            

def remove(number):
    found = False
    for i in contract:
        for name,num in i.items():
            if num == number:
                print("Contract Removed Successfully")
                contract.remove(i)
                found = True
                break
    if not found:
        print("No Such Number in Contracts.")


def view():
    if not contract:
        print("No contract Available\n")
        print()
    else:
        for entry in contract:
            for i,j in entry.items():
                print(f"Name : {i.title()} \t Number : {j}")








