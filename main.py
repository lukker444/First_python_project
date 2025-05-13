def manager():
    print("To create an exersise: 1")
    print("To see exersises:      2")
    print("To update an exersise: 3")
    print("To delete an exersise: 4")
    print("To quit the program:   0")

id = 1

def creating_list_from_file():
    try:
        second_append_list = []
        helper_list = []
        final_list = []
        with open("list.txt", "r") as file:
            first_append_list = file.read().split("|")
        for i in first_append_list:
            k = i.split("/")
            second_append_list.append(k)
        for i in second_append_list:
            for x in i:
                a = x.split("-")
                helper_list.append(tuple(a))
            w = dict(helper_list)  
            final_list.append(w)
        return  final_list
    except(ValueError):
        print("There aren't any exersises :(")

def id_counter():
    try:
        last_exersise = list1[-1:]
        for i in last_exersise:
            id = int(i["id"]) + 1
        return id
    except(TypeError):
        return 1
    
def saving_exersises_to_file():
    with open("list.txt", "r") as file:
        reading_file = file.read()
    with open("list.txt", "a") as file:
        if reading_file.startswith("i"):
            file.write(f"|id-{id}/name-{name}/description-{description}/priority-{priority}/status-{status}")
        else:
            file.write(f"id-{id}/name-{name}/description-{description}/priority-{priority}/status-{status}")
   
def create_exercise():  
    name = input("Name: ")
    description = input("Description: ")
    priority = input("Priority low/mid/high: ")
    status = input("Status new/processing/end: ")
    return name, description, priority, status
    
starting_code = input("To start anything enter start: ")
if starting_code == "start":
    while True:
        manager()
        choosing_number = input("What do you want to do: ")
        if choosing_number == "0":
            break
        elif choosing_number == "1":
            name, description, priority, status = create_exercise()
            list1 = creating_list_from_file()
            id = id_counter()
            saving_exersises_to_file()
            
        




