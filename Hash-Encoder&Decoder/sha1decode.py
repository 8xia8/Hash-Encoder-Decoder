def sha1decode():
    import hashlib
    import time

    counter = 1

    sha1_pass = input("Enter A SHA-1 Hash : ")
    sha1_file = input("Enter A Wordlist Location : ")

    try:
        sha1_file = open(sha1_file, "r")
    except:
        print("\n File Not Found")
        quit()

    for password in sha1_file:
        hash_obj = hashlib.sha1(password.strip().encode('utf-8')).hexdigest()
        start = time.time()
        print("[?]Trying Password %d : %s " % (counter, password.strip()))
        counter += 1
        end = time.time()
        t_time = end - start

        if hash_obj == sha1_pass:
            print("\n[!]Password Found & Password Is : %s " % password)
            print("[!]Total Running Time is :  ", t_time, "seconds")
            break

    else:
        print("\n[!]Password Not Found")
        print("[!]Try Another Wordlist Or Hash")