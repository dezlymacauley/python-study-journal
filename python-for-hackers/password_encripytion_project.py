# NOTE: This will create an encrypted password

import base64

def encrpyt_pass(_password):
    encoded_bytes = base64.b64encode(_password.encode())
    print(encoded_bytes)

user_pass = input("Enter your password: ") 
encrpyt_pass(user_pass)

# NOTE: How this works

# If you enter the word shortstack as your password,
# You will get back this output b'c2hvcnRzdGFjaw=='
#  c2hvcnRzdGFjaw== is the encrypted password

# For the next section if you type in c2hvcnRzdGFjaw==
# This will decript that password and give you shortstack


###############################################################################

# NOTE: This will decrypt the password

def decrypt_pass(_password):
    decoded_bytes = base64.b64decode(_password)
    decode_data = decoded_bytes.decode()
    print(f"decoded data {decode_data}")

encryted_pass = input("Enter the encrypted password: ")
decrypt_pass(encryted_pass) 
