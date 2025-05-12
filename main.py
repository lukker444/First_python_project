def Manager():
    print("To create an exersise: 1")
    print("To see exersises:      2")
    print("To update an exersise: 3")
    print("To delete an exersise: 4")
    print("To quit the program:   0")


def Dict_Exersise(name, description, priority, status):
   dict_exersise = {}
   dict_exersise["id"] = id
   dict_exersise["name"] = name
   dict_exersise["description"] = description
   dict_exersise["priority"] = priority
   dict_exersise["status"] = status
   return dict_exersise



def Saving_Exersises_To_File():
    with open("list.txt", "a") as file:
        file.write(f"{str(dict_exersise)}\n")

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
            dict_exersise = Dict_Exersise(name, description, priority, status)
            Saving_Exersises_To_File()
            
        




