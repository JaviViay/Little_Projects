print('\033[34m' + "   / / / /___ ______/ /_   " + '\033[0m' + "\033[91m" + " /  |/  / ____/" + "\033[0m")
print('\033[34m' + "  / /_/ / __ `/ ___/ __ \ " + '\033[0m' + "\033[91m" + " / /|_/ / __/   " + "\033[0m")
print('\033[34m' + " / __  / /_/ (__  ) / / / " + '\033[0m' + "\033[91m" + "/ /  / / /___   " + "\033[0m")
print('\033[34m' + "/_/ /_/\__,_/____/_/ /_/ " + '\033[0m' + "\033[91m" + "/_/  /_/_____/   " + "\033[0m")

import hashlib
message = input("Enter the text you want to hash: ")

print("\033[91m" + "    1. md5" + "\033[0m")
print("\033[91m" + "    2. sha1" + "\033[0m")
print("\033[91m" + "    3. sha224" + "\033[0m")
print("\033[91m" + "    4. sha256" + "\033[0m")
print("\033[91m" + "    5. sha384" + "\033[0m")
print("\033[91m" + "    6. sha512" + "\033[0m")
print("\033[91m" + "    7. blake2b" + "\033[0m")
print("\033[91m" + "    8. blake2s" + "\033[0m")
print("\033[91m" + "    9. sha3_224" + "\033[0m")
print("\033[91m" + "    10. sha3_256" + "\033[0m")
print("\033[91m" + "    11. sha3_384" + "\033[0m")
print("\033[91m" + "    12. sha3_512" + "\033[0m")
option = input("Select a hash algorithm: ")

if option == "1":
    hash = hashlib.md5()
    hash.update(message.encode('utf-16'))
    hashme = hash.hexdigest()
    print('\033[34m' + hashme + '\033[0m')

elif option == "2":
    hash = hashlib.sha1()
    hash.update(message.encode('utf-16'))
    hashme = hash.hexdigest()
    print('\033[34m' + hashme + '\033[0m')

elif option == "3":
    hash = hashlib.sha224()
    hash.update(message.encode('utf-16'))
    hashme = hash.hexdigest()
    print('\033[34m' + hashme + '\033[0m')

elif option == "4":
    hash = hashlib.sha256()
    hash.update(message.encode('utf-16'))
    hashme = hash.hexdigest()
    print('\033[34m' + hashme + '\033[0m')

elif option == "5":
    hash = hashlib.sha384()
    hash.update(message.encode('utf-16'))
    hashme = hash.hexdigest()
    print('\033[34m' + hashme + '\033[0m')

elif option == "6":
    hash = hashlib.sha512()
    hash.update(message.encode('utf-16'))
    hashme = hash.hexdigest()
    print('\033[34m' + hashme + '\033[0m')

elif option == "7":
    hash = hashlib.blake2b()
    hash.update(message.encode('utf-16'))
    hashme = hash.hexdigest()
    print('\033[34m' + hashme + '\033[0m')

elif option == "8":
    hash = hashlib.blake2s()
    hash.update(message.encode('utf-16'))
    hashme = hash.hexdigest()
    print('\033[34m' + hashme + '\033[0m')

elif option == "9":
    hash = hashlib.sha3_224()
    hash.update(message.encode('utf-16'))
    hashme = hash.hexdigest()
    print('\033[34m' + hashme + '\033[0m')

elif option == "10":
    hash = hashlib.sha3_256()
    hash.update(message.encode('utf-16'))
    hashme = hash.hexdigest()
    print('\033[34m' + hashme + '\033[0m')

elif option == "11":
    hash = hashlib.sha3_384()
    hash.update(message.encode('utf-16'))
    hashme = hash.hexdigest()
    print('\033[34m' + hashme + '\033[0m')

elif option == "12":
    hash = hashlib.sha3_512()
    hash.update(message.encode('utf-16'))
    hashme = hash.hexdigest()
    print('\033[34m' + hashme + '\033[0m')

else:
    print("Invalid option!")