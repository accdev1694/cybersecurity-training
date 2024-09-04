import base64
# the encode function takes in a password and returns an ecrypted object

def encoded_password(password):
    return base64.b64encode(password.encode())

print(encoded_password(input("What is your password? ")))