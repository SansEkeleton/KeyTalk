import random
import Config.JsonFiles as JsonFiles

# Create a random 30 character password, encrypt it, and save it to a file
# [MODIFIED] to include the user's name in the password
def createPassword(name):
    random.seed(name)
    # create a list of all possible characters
    allCharacters = []
    for i in range(33, 127):
        allCharacters.append(chr(i))
    # create a list of 30 random characters
    passwordCharacters = []
    for i in range(30 - name.__len__()):
        passwordCharacters.append(random.choice(allCharacters))
    # add the user's name to the password
    passwordCharacters.append(name)
    # turn list of characters into a string
    password = ""
    for character in passwordCharacters:
        password += character
    return password
def WritePasswordToFile(name):
    password = createPassword(name)
    # encrypt password
    encryptedPassword = encryptPassword(password)
    # save encrypted password to file
    JsonFiles.writeEncryptedPasswordToFile(encryptedPassword)
    return password
# Encrypt a password
def encryptPassword(password):
    encryptedPassword = ""
    for character in password:
        encryptedPassword += chr(ord(character) + 3)
    return encryptedPassword
# Decrypt a password
def decryptPassword(encryptedPassword):
    password = ""
    for character in encryptedPassword:
        password += chr(ord(character) - 3)
    return password

# check if a nameFilename exist using nameFileExists() from JsonFiles.py, if not prompt the user to input a name and save it to a file using writeNameToFile() from JsonFiles.py
def createName():
    if JsonFiles.nameFileExists() == False:
        name = input("Please enter your name: ")
        JsonFiles.writeNameToFile(name)
        createdPassword = WritePasswordToFile(name)
        print("Your password is: " + createdPassword)
        print("Please remember this password, you will need it to use most of your account's functionality.")
        input("Press enter to continue...")
    #if a namefile exists, read the name from the file using readNameFromFile() from JsonFiles.py and check if it matches the password generated by the app
    # [MODIFIED] copilot repeated the same code twice, so I completed it correctly in accordance to the prompt
    else:
        name = JsonFiles.readNameFromFile()
        createdPassword = createPassword(name)
        # if the password matches, do nothing, if not, give an error message and exit the program
        if comparePassword(createdPassword):
            pass
        else:
            print("Error: Password does not match.")
            exit()

# compare an imputed password to the decrypted password
def comparePassword(password):
    encryptedPassword = JsonFiles.readEncryptedPasswordFromFile()
    if password == decryptPassword(encryptedPassword):
        return True
    else:
        return False