def Manager():
    print("To create an exersise: 1")
    print("To see exersises:      2")
    print("To update an exersise: 3")
    print("To delete an exersise: 4")
    print("To quit the program:   0")

def Dict_Exersise(name, description, priority, status):
   dict_exersise = {"name": name, "description": description, "priority": priority, "status": status}
   return dict_exersise

def Saving_Exersises_To_File(name, description, priority, status):
    with open("list.txt", "a") as file:
        #file.write(f"Id: {id_exersise}")
        file.write(f"\nName: {name}")
        file.write(f"\nDescription: {description}")
        file.write(f"\nPriority: {priority}")
        file.write(f"\nStatus: {status}\n")
        

def create_exercise():
    name = input("Name: ")
    description = input("Description ")
    priority = input("Priority low/mid/high: ")
    status = input("Status new/processing/end: ")
    return name, description, priority, status

starting_code = input("To start anything enter start: ")
if starting_code == "start":
    while True:
        Manager()
        choosing_number = input("What do you want to do: ")
        if choosing_number == "0":
            break
        elif choosing_number == "1":
            name, description, priority, status = create_exercise()
            Saving_Exersises_To_File(name, description, priority, status)
            Dict_Exersise(name, description, priority, status)
        




