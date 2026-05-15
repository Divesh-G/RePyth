def check_for_word():
    with open("practice.txt", "r") as f:
        data = f.read()

    new_data = data.replace("Java", "Python")
    print(new_data)

    with open("practice.txt", "w") as f:
        f.write(new_data)

    with open("practice.txt", "r") as f:
        dataa = f.read()
        if(dataa.find("learning") != -1):
            print("found")
        else:
            print("not found")
# check_for_word()

def check_for_line():
    word = "want"
    data = True
    line_no  = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1
    return -1
print(check_for_line())