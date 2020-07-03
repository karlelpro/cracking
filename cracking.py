import hashlib
import base64
print("1) Hash")
print("2) Base64")
options = int(input("What do you want to decode? "))



if options == 1:
    hashtext = input("Type the MD5 hash: ")
    get_file = input("Wordlist file: ")
    try:
        wordlist_file = open("./wordlists/"+get_file, "r")
    except:
        print("File '"+get_file+"' not found!")
        quit()
    for force in wordlist_file:
        encode = force.encode('utf-8')
        digest = hashlib.md5(encode.strip()).hexdigest()

        if digest == hashtext:
            print("Password found! =>",force)
            break
        if digest != hashtext:
            print("Incorrect password, I try with a new one...")

if options == 2:
    basetext = input("Type the Base64 code: ")
    decoded = base64.b64decode(basetext)
    decoded = decoded.decode('utf8')
    print("Base64 decoded =>",decoded)
    
