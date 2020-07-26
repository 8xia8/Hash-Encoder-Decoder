def user_input():
    from md5decode import md5decode
    from md5encode import md5encode
    from sha1encode import sha1encode
    from sha1decode import sha1decode
    from sha256encode import sha256encode
    from sha256decode import sha256decode
    from sha512encode import sha512encode
    from sha512decode import sha512decode
    from base64encode import base64encode
    from base64decode import base64decode
    import subprocess
    user_input_1_list = ["ENCODE","DECODE"]
    user_input_2_list = ["MD5", "SHA1", "SHA256", "SHA512", "BASE64"]
    print("[?] Specify As (Encode) Or (Decode) You Want To Do")
    while True:
        a = input("[?] You want to Encode Or Decode?: ")
        b = a.upper()
        if b in user_input_1_list:
            break
        else:
            print("[?] You Entered Wrong")
            continue
    if b == "ENCODE":
        print("[!] Available Encodes (""sha1", "sha256", "sha512", "base64", "md5"")")
        while True:
            c = input("[?] Specify the Type of Hash You Want to Encode: ")
            d = str(c.upper())
            if d in user_input_2_list:
                break
            else:
                print("[!!] You Entered Wrong")
                continue
        if d == "SHA1":
            sha1encode()
            print("ENCODE COMPLETED")
        if d == "SHA256":
            sha256encode()
            print("ENCODE COMPLETED")
        if d == "SHA512":
            sha512encode()
            print("ENCODE COMPLETED")
        if d == "BASE64":
            base64encode()
            print("ENCODE COMPLETED")
        if d == "MD5":
            md5encode()
            print("ENCODE COMPLETED")
    if b == "DECODE":
        print("[!] Available Decodes (""sha1", "sha256", "sha512", "base64", "md5"")")
        while True:
            ab = input("[?] Specify the Type of Hash You Want to Decode: ")
            ba = str(ab.upper())
            if ba in user_input_2_list:
                break
            else:
                print("[!!] You Entered Wrong")
                continue
        if ba == "SHA1":
            sha1decode()
            print("DECODE COMPLETED")
        if ba == "SHA256":
            sha256decode()
            print("DECODE COMPLETED")
        if ba == "SHA512":
            sha512decode()
            print("DECODE COMPLETED")
        if ba == "BASE64":
            base64decode()
            print("DECODE COMPLETED")
        if ba == "MD5":
            md5decode()
            print("DECODE COMPLETED")

