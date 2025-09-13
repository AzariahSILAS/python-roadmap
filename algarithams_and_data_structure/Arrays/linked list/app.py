list = {}

def create_list(new_item):
    number = len(list) + 1
    list[f"{new_item}{number}"] = new_item
    print(list)
    

while True:
    question = input("what do you want me to do? ")

    if(question == "add this to list"):
        new_question = input("what should i add: ")
        create_list(new_question)
        print(list)
    elif(question == "leave"):
        break    
