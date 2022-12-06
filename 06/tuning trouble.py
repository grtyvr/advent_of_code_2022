data = open("input.txt")

def getMessage(data):
#read 4 characters
    fPointer =0
    while True:
        message = data.read(4)
        if message == "":
            break
        else:
            if len(set(message)) == 4:
                return fPointer + 4
            else:
                fPointer+=1
                data.seek(fPointer)

if __name__ == "__main__":
    print(getMessage(data))