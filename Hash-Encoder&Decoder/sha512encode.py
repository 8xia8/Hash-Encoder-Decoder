def sha512encode():
    import hashlib
    word = input("[?]Enter A Word: ").encode('utf-8')
    crypt = hashlib.sha512()
    crypt.update(word)
    crypt = crypt.hexdigest()
    print("[!]Word Changed To")
    print(crypt)
    print("SHA-512 Hash")