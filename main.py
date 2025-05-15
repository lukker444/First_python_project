def manager():
# Функция которая просто предлагает то что юзер может сделать 
    while True:
        print("To create an exersise: 1")
        print("To see exersises:      2")
        print("To update an exersise: 3")
        print("To delete an exersise: 4")
        print("To quit the program:   0")
        try:
            return int(input("What do you want to do: "))
            break
        except(ValueError):
            print("Please try again")

def creating_list_from_file():
#Одна из важнейших функций, разделяет строку из файла на микро листики а потом переделывает ее в лист со словарями
    try:
        second_append_list = []
        helper_list = []
        final_list = []
        with open("list.txt", "r") as file:
            first_append_list = file.read().strip().split("|")
        for i in first_append_list:
            k = i.split("/")
            second_append_list.append(k)
        for i in second_append_list:
            for x in i:
                a = x.split("-")
                helper_list.append(tuple(a))
            w = dict(helper_list)  
            final_list.append(w)
        return final_list
    except(ValueError):
        return None


def watching_exersises(n):
#Функция по числе выписывает сортирированые задачи а также есть поиск по слову
    if n == 1:
        for i in main_list:
            print("----------------------------------------------")
            print(f"ID: {i["id"]},\n Name: {i["name"]},\n Priority: {i["priority"]},\n Status: {i["status"]}\nDescription: {i["description"]}")
            print("----------------------------------------------")

    elif n == 2:
        new = [ex for ex in main_list if ex["status"] == "new"]
        processing = [ex for ex in main_list if ex["status"] == "processing"]
        end = [ex for ex in main_list if ex["status"] == "end"]
        for i in new:
            print("----------------------------------------------")
            print(f"ID: {i["id"]}, Name: {i["name"]}, Priority: {i["priority"]}, Status: {i["status"]}\nDescription: {i["description"]}")
            print("----------------------------------------------")
        for i in processing:
            print("----------------------------------------------")
            print(f"ID: {i["id"]}, Name: {i["name"]}, Priority: {i["priority"]}, Status: {i["status"]}\nDescription: {i["description"]}")
            print("----------------------------------------------")
        for i in end:
            print("----------------------------------------------")
            print(f"ID: {i["id"]}, Name: {i["name"]}, Priority: {i["priority"]}, Status: {i["status"]}\nDescription: {i["description"]}")
            print("----------------------------------------------")
        
    elif n == 3:
        high = [ex for ex in main_list if ex["priority"] == "high"]
        mid = [ex for ex in main_list if ex["priority"] == "mid"]
        low = [ex for ex in main_list if ex["priority"] == "low"]
        for i in high:
            print("----------------------------------------------")
            print(f"ID: {i["id"]}, Name: {i["name"]}, Priority: {i["priority"]}, Status: {i["status"]}\nDescription: {i["description"]}")
            print("----------------------------------------------")
        for i in mid:
            print("----------------------------------------------")
            print(f"ID: {i["id"]}, Name: {i["name"]}, Priority: {i["priority"]}, Status: {i["status"]}\nDescription: {i["description"]}")
            print("----------------------------------------------")
        for i in low:
            print("----------------------------------------------")
            print(f"ID: {i["id"]}, Name: {i["name"]}, Priority: {i["priority"]}, Status: {i["status"]}\nDescription: {i["description"]}")
            print("----------------------------------------------")
        
    elif n == 4:
        word_for_finding = input("Please input the word you want to find: ")
        for i in main_list: 
            if word_for_finding.upper() in i["name"].upper() or word_for_finding.upper() in i["description"].upper():
                print("----------------------------------------------")
                print(f"ID: {i["id"]}, Name: {i["name"]}, Priority: {i["priority"]}, Status: {i["status"]}\nDescription: {i["description"]}")
                print("----------------------------------------------")
            else:
                print(f"You don't have this word in name or description in exersise {i["id"]}")
                input()
    else:
        print("Wrong input number")
        input()



def id_counter():
#Счетчик ID который не перезаписывается при закрытии консоли. Берет последний словарь и добавляет к нему 1. Если файл пустой вернет 1.
    if main_list != None:
        last_exersise = main_list[-1:]
        for i in last_exersise:
            id = int(i["id"]) + 1
        return id
    else:
        return 1
    
def saving_exersises_to_file(id, name, description, priority, status):
#В отличее од функции перезаписи она просто добавляет в файл задание которое мы записали
    f_string = f"id-{id}/name-{name}/description-{description}/priority-{priority}/status-{status}"
    with open("list.txt", "r") as file:
        reading_file = file.read()
    with open("list.txt", "a") as file:
        if not reading_file:
            file.write(f_string)    
        else:
            file.write("|" + f_string)
            
   
def create_exercise(): 
#Создание задачи с проверками
    while True:
        name = input("Name: ")
        if name == "" or name.startswith(" "):
            print("Name can't be empty")
        else:
            break
    while True:
        description = input("Description: ")
        if description == "" or description.startswith(" "):
            print("Description can't be empty")
        else:
            break
    while True:
        priority = input("Priority low/mid/high: ")
        if priority == "low" or priority == "mid" or priority == "high":
            break
        else:
            print("You can write low/mid/high")
    while True:
        status = input("Status new/processing/end: ")
        if status == "new" or status == "processing" or status == "end":
            break
        else:
            print("You can write new/processing/end")
    return name, description, priority, status

def deleating_exersise_by_id(n):
#Удаление задачи через айди
    for i in main_list:
        if int(i["id"]) == n:
            main_list.remove(i)
    return main_list



def rewriting_exersise(n):
#Очень важная функция которая перезаписывает файл через список из задач
    with open("list.txt", 'w'):
        pass
    with open("list.txt", "w") as file:
        for idx, i in enumerate(n):
            entry = f"id-{i['id']}/name-{i['name']}/description-{i['description']}/priority-{i['priority']}/status-{i['status']}"
            if idx != 0:
                file.write("|")  
            file.write(entry)


def print_write_exersises():
#Функция которая выписывает выбор задач
    print("Watch all exersises: 1")
    print("Sort by status:      2")
    print("Sort by priority:    3")
    print("Input the word:      4")
    while True:
        try:
            number_for_printing = int(input("Input the number: "))
            return number_for_printing
            break
        except(ValueError):
            print("Input must be integer")



def redacting_exercise(n):
#Функция которая редактирует задание, с проверками.
    try:
        for i in main_list:
            if int(i["id"]) == n:
                g = input("What do you want to redact name|description|priority|status: ")
                while True:
                    if g == "name" or g == "description" or g == "priority" or g == "status":
                        break
                    else:
                        g = input("You can only write name|description|priority|status: ")
        if g == "name":
            p = input("Please rename your exersise: ")
            while True:
                if p == "" or p.startswith(" "):
                    p = input("Name can't be empty: ")
                else:
                    break
            i["name"] = p
        elif g == "description": 
            p = input("Please redact your description: ")
            while True:
                if p == "" or p.startswith(" "):
                    p = input("Description can't be empty: ")
                else:
                    break
            i["description"] = p
        elif g == "priority":
            while True:
                p = input("Please redact your priority: ")
                if p == "low" or p == "mid" or p == "high":
                    i["priority"] = p
                    break     
                else:
                    print("You can write low/mid/high")
        elif g == "status":
            while True:
                p = input("Please redact your status: ")
                if p == "new" or p == "processing" or p == "end":
                    i["status"] = p
                    break
                else:
                    print("You can write new/processing/end")
        return main_list
    except(UnboundLocalError):
        print("This id doesn't exist")





starting_code = input("To start anything enter start: ")
if starting_code == "start":


    while True: 
        choosing_number = manager()
        main_list = creating_list_from_file()


        if choosing_number == 0:
            break


        elif choosing_number == 1:
            name, description, priority, status = create_exercise()
            id = id_counter()
            saving_exersises_to_file(id, name, description, priority, status)
            print("------------------------\nExersise was successfuly created\n------------------------")


        elif choosing_number == 2:
            if main_list != None:  
                number_for_printing = print_write_exersises()
                watching_exersises(number_for_printing)
            else:
                print("There isn't any exersises in file")
                input()


        elif choosing_number == 3:
            if main_list != None:
                while True:
                    try:
                        redact_exersise = int(input("Enter id of exersise you want to redact: "))
                        break
                    except(ValueError):
                        print("Input must be integer")
                redacted_list = redacting_exercise(redact_exersise)
                if redacted_list != None:
                    rewriting_exersise(redacted_list)
                else:
                    rewriting_exersise(main_list)
                
            else:
                print("There isn't any exersise in file")
                input()


        elif choosing_number == 4:
            if main_list != None:
                while True:
                    try:
                        del_exersise = int(input("Enter id of exersise you want to delete: "))
                        break
                    except(ValueError):
                        print("Input must be integer")
                deleted_list = deleating_exersise_by_id(del_exersise)
                rewriting_exersise(deleted_list)
            else:
                print("There isn't any exersise in file")
                input()

