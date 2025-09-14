list = {}

def create_list(new_item):
    number = len(list) + 1
    temp = ""
    counter = 0
    if(number > 0):
        
        for i in list:
            counter += 1
            if counter == len(list):
                temp = i
        list[f"{new_item}"] = temp
    else:
          list[new_item] = "foot"
    

while True:
    question = input("what do you want me to do? ")

    if(question == "add"):
        new_question = input("what should i add: ")
        create_list(new_question)
        for item in list:
            print(f"'{item}':'{list[item]}'")
        print(list)
    elif(question == "leave"):
        break    