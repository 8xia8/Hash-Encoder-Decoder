def base64encode():
    import base64
    word = input("[?]Enter A Word: ")
    word_byte = word.encode('ascii')
    base64_bytes = base64.b64encode(word_byte)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)