import sys


def encryption(key: int, message: str) -> str:
    array = [[] for _ in range(key)]

    encrypted_message = ""
    height = 0
    direction = True

    for letter in message:
        array[height].append(letter)

        if direction:
            height += 1
            if height == key:
                direction = False
                height -= 2
        else:
            height -= 1
            if height < 0:
                direction = True
                height += 2

    for sub_array in array:
        for letter in sub_array:
            encrypted_message += letter

    return encrypted_message


def decryption(key: int, message: str) -> str:
    decrypted_message = ""
    direction = True
    height = 0
    length = len(message)
    array = [[""] * length for i in range(key)]

    for i in range(length):
        array[height][i] = "*"

        if direction:
            height += 1
            if height == key:
                direction = False
                height -= 2
        else:
            height -= 1
            if height < 0:
                direction = True
                height += 2

    k = 0
    for y in range(key):
        for x in range(length):
            if array[y][x] == "*":
                array[y][x] = message[k]
                k += 1

    direction = True
    height = 0

    for i in range(length):
        if array[height][i] != "":
            decrypted_message += array[height][i]

        if direction:
            height += 1
            if height == key:
                direction = False
                height -= 2
        else:
            height -= 1
            if height < 0:
                direction = True
                height += 2
    
    return decrypted_message


def check_key(key) -> bool:
    try:
        key = int(key)        
    except:
        return False

    if key < 1:
        return False
    else:
        return True


def main():
    if len(sys.argv) == 4:
        operation = sys.argv[1]
        key = sys.argv[2]
        message = sys.argv[3]
    else:
        print("Bad arguments")
        sys.exit()


    if check_key(key):
        key = int(key)
    else:
        print("Bad arguments")
        sys.exit()


    if operation == 'e':
        print(encryption(key, message))
    elif operation == 'd':
        print(decryption(key, message))
    else:
        print("Bad arguments")
        sys.exit()


if __name__ == "__main__":
    main()
