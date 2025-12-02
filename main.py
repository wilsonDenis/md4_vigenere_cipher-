#a=ord("c")
#chr(a)
message = "lapin"
key=3

def cesar_cipher(messag,key):
    crypted_message=""
    for char in message:
        crypted_message=chr((ord(char)+key)%1_114_112)
        crypted_message+=crypted_message
    return crypted_message

def cesar_uncipher(crypted_message,key):
   
    return cesar_cipher(crypted_message, -key)