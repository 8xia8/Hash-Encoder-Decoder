def sha512decode():
    import hashlib
    import time

    counter = 1

    sha512_pass = input("Enter A SHA-512 Hash : ")
    sha512_file = input("Enter A Wordlist Location : ")

    try:
        sha512_file = open(sha512_file, "r")
    except:
        print("\n File Not Found")
        quit()

    for password in sha512_file:
        hash_obj = hashlib.sha512(password.strip().encode('utf-8')).hexdigest()
        start = time.time()
        print("[?]Trying Password %d : %s " % (counter, password.strip()))
        counter += 1
        end = time.time()
        t_time = end - start

        if hash_obj == sha512_pass:
            print("\n[!]Password Found & Password Is : %s " % password)
            print("[!]Total Running Time is :  ", t_time, "seconds")
            break

    else:
        print("\n[!]Password Not Found")
        print("[!]Try Another Wordlist Or Hash")