import functions
app_on = True
logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""
print(logo)
while app_on:
    order_type = input("Type 'encode' to encrypt, or 'decode' to decrypt: \n")
    order_message = input("Type your message: \n")
    order_shift = int(input("Type the shift number: \n"))
    print(f"Here is your {order_type}d message: \n{functions.cipher(order_type, order_message, order_shift)}")
    order_continue = input("type 'y' if you want to continue, else type 'n'. \n")
    if not order_continue == "y":
        app_on = False
print(functions.cipher("encode", "Hello World!", 5))
