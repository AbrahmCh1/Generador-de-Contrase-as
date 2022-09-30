import random
import os
import hashlib
from termcolor import colored as cdd


def generar_contrasena():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[',
             '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    c = str.upper(input(
        "Quieres que la contraseña se genere con caracteres especiales? \n \t\t[Y][N]"))
    if c == "Y":
        caracteres = MAYUS + MINUS + CHARS + NUMS
        f = "s"
        while f != "n":
            cps = str.lower(
                input("¿Quieres excluir algún caractér especial ? \n \t\t [Y][N]"))
            if cps == "y":
                print(CHARS)
                cpop = input(
                    "Escribe que caractér quieres excluir (UNO A LA VEZ SEGUIDO DE <ENTER>) ")
                CHARS.remove(cpop)
            else:
                break

    else:
        caracteres = MAYUS + MINUS + NUMS

    contrasena = []

    n = int(
        input("De cuantos caracteres de largo quieres que se genere tu contraseña? "))

    for i in range(n):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena
    return appl


def application():
    appl = input(
        "Ingresa el nombre del servicio en el que utilizarás esta contraseña: ")
    return appl


def uusuario():
    uss = input("Ingresa tu nombre de usuario:")
    return uss


def main():
    appl = application()
    uss = uusuario()
    contrasena = generar_contrasena()
    print(f"Tu nueva contraseña es: {contrasena}")
    file = open("passcodes.txt", "a")
    file.write(f"{appl}:\t")
    file.write(f"{uss} - ")
    file.write(f"{contrasena}\n")
    file.close()


def generar_contrasena1():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[',
             '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    c = str.upper(input(
        "Quieres que la contraseña se genere con caracteres especiales? \n \t\t[Y][N]"))
    if c == "Y":
        caracteres = MAYUS + MINUS + CHARS + NUMS
        f = "s"
        while f != "n":
            cps = str.lower(
                input("¿Quieres excluir algún caractér especial ? \n \t\t [Y][N]"))
            if cps == "y":
                print(CHARS)
                cpop = input(
                    "Escribe que caractér quieres excluir (UNO A LA VEZ SEGUIDO DE <ENTER>) ")
                CHARS.remove(cpop)
            else:
                break

    else:
        caracteres = MAYUS + MINUS + NUMS

    contrasena = []

    n = int(
        input("De cuantos caracteres de largo quieres que se genere tu contraseña? "))

    for i in range(n):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena
    return appl


def application1():
    appl = input(
        "Ingresa el nombre del servicio en el que utilizarás esta contraseña: ")

    return appl


def uusuario1():
    uss = input("Ingresa tu nombre de usuario:")
    return uss


def main1():
    appl = application1()
    uss = uusuario1()
    contrasena = generar_contrasena1()
    print(f"Tu nueva contraseña es: {contrasena}")
    file = open("passcodesUser2.txt", "a")
    file.write(f"{appl}:\t")
    file.write(f"{uss} - ")
    file.write(f"{contrasena}\n")
    file.close()


def signup():
    email = input("Crea tu usuario: ")
    pwd = input("Crea tu contraseña: ")
    conf_pwd = input("Confirma tu contraseña: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt", "a") as f:
            f.write("\n" + email + "\n")
            f.write(hash1)
            f.close()
            print("Te has registrado exitosamente!")
    else:
        print("Tus contraseñas no coinciden! \n")


def login():
    email = input("Ingresa tu usuario: ")
    pwd = input("Ingresa tu contraseña: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        clearss, stored_email, stored_pwd, stored_email2, stored_pwd2 = f.read().split("\n")
        f.close()
        if email == stored_email and auth_hash == stored_pwd:
            print("Inicio de sesión exitoso!\n")
            main()
        elif email == stored_email2 and auth_hash == stored_pwd2:
            print("Inicio de sesión exitoso!\n")
            main1()

        else:
            print("Datos erróneos! \n")


while 1:
    print("********** Inicio de Sesión **********")
    print("")
    print("1.Inicia sesión")
    print("2.Salir")
    ch = int(input("Elige tu opción: "))
    if ch == 1:
        login()
    elif ch == 2:
        break
    else:
        print("Has ingresado una opción invalida!")


print("DONE")
