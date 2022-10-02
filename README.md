# Generador-de-Contrase-as

credentials will be empty for default, you can set up in "keygen.py" 
to register (Two users) if you register only one, you have to remove "<<<<<<stored_email2, stored_pwd2>>>>>>" from the code or just replace def login() in the code with the code below:


    def login():
        email = input("Ingresa tu usuario: ")
        pwd = input("Ingresa tu contraseña: ")
        auth = pwd.encode()
        auth_hash = hashlib.md5(auth).hexdigest()
        with open("credentials.txt", "r") as f:
            clearss, stored_email, stored_pwd = f.read().split("\n")
            f.close()
            if email == stored_email and auth_hash == stored_pwd:
                print("Inicio de sesión exitoso!\n")
                main()
            elif email == stored_email2 and auth_hash == stored_pwd2:
                print("Inicio de sesión exitoso!\n")
                main1()
            else:
                print("Datos erróneos! \n")
