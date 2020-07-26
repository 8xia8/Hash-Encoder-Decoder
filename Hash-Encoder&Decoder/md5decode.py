def md5decode():
    import hashlib
    import time

    counter = 1

    md5_pass = input("Enter A MD5 Hash : ")
    md5_file = input("Enter A Wordlist Location : ")

    try:
        md5_file = open(md5_file, "r")
    except:
        print("\n File Not Found")
        quit()

    for password in md5_file:
        hash_obj = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
        start = time.time()
        print("[?]Trying Password %d : %s " % (counter, password.strip()))
        counter += 1
        end = time.time()
        t_time = end - start

        if hash_obj == md5_pass:
            print("\n[!]Password Found & Password Is : %s " % password)
            print("[!]Total Running Time is :  ", t_time, "seconds")
            break

    else:
        print("\n[!]Password Not Found")
        print("[!]Try Another Wordlist Or Hash")