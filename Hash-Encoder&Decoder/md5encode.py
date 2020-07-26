def md5encode():
    import hashlib
    word = input("[?]Enter A Word: ").encode('utf-8')
    crypt = hashlib.md5()
    crypt.update(word)
    crypt = crypt.hexdigest()
    print("[!]Word Changed To")
    print(crypt)
    print("MD5 Hash")