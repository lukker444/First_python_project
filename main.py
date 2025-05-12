
def Manager():
    print("To create an exersise: 1")
    print("To see exersises:      2")
    print("To update an exersise: 3")
    print("To delete an exersise: 4")
    print("To quit the program:   0")

def Creating_Exersise():
    name_of_exersise = input("Write a name of exersise: ")
    description_of_exersise = input("Write an exersise: ")
    exersise_priority = input("Input a priority of exersise low/mid/high: ")
    exersise_status = input("Status of exersise new/processing/end: ")
starting_code = input("To start anything enter start: ")
if starting_code == "start":
    while True:
        Manager()
        choosing_number = input("What do you want to do: ")
        if choosing_number == "0":
            break
        elif choosing_number == "1":
            Creating_Exersise()

