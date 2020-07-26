def base64decode():
    import base64
    while True:
        try:
            base64_message = input("[?]Enter A Base64: ")
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('ascii')
        except:
            print("[!!]Your Entered Code Is Not Base64")
            print("[!!]Please Try Again")
            continue
        else:
            break
    print("[!]Password Found!")
    print(message)