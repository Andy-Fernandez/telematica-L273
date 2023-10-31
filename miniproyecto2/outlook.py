import imaplib
import email
from email.header import decode_header
import os
from getpass import getpass

# Datos del usuario
username = input("Correo: ")
password = getpass("Password: ")

def autenticar():
    # Crear conexión IMAP
    global imap
    imap = imaplib.IMAP4_SSL("outlook.office365.com")
    # Iniciar sesión
    imap.login(username, password)
    print("Sesión IMAP autenticada con éxito.")

def leer_correo():
    status, mensajes = imap.select("INBOX")
    print(mensajes)
    # Mensajes a recibir
    N = 3
    # Cantidad total de correos
    mensajes = int(mensajes[0])

    for i in range(mensajes, mensajes - N, -1):
        try:
            res, mensaje = imap.fetch(str(i), "(RFC822)")
        except:
            break
        for respuesta in mensaje:
            if isinstance(respuesta, tuple):
                mensaje = email.message_from_bytes(respuesta[1])
                subject = decode_header(mensaje["Subject"])[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode()
                from_ = mensaje.get("From")
                print("Subject:", subject)
                print("From:", from_)
                print("Mensaje obtenido con éxito")
                if mensaje.is_multipart():
                    for part in mensaje.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            print(body)
                        elif "attachment" in content_disposition:
                            nombre_archivo = part.get_filename()
                            if nombre_archivo:
                                if not os.path.isdir(subject):
                                    os.mkdir(subject)
                                ruta_archivo = os.path.join(subject, nombre_archivo)
                                open(ruta_archivo, "wb").write(part.get_payload(decode=True))
                else:
                    content_type = mensaje.get_content_type()
                    body = mensaje.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        print(body)

def crear_buzon():
    nuevo_buzon = input("Nombre del nuevo buzón: ")
    # Utiliza el comando IMAP CREATE para crear el buzón.
    imap.create(nuevo_buzon)
    print(f"Buzón '{nuevo_buzon}' creado con éxito.")

def borrar_buzon():
    buzon_a_borrar = input("Nombre del buzón a borrar: ")
    # Utiliza el comando IMAP DELETE para eliminar el buzón.
    imap.delete(buzon_a_borrar)
    print(f"Buzón '{buzon_a_borrar}' eliminado con éxito.")

def renombrar_buzon():
    buzon_anterior = input("Nombre del buzón a renombrar: ")
    nuevo_nombre = input("Nuevo nombre del buzón: ")
    # Crea un nuevo buzón con el nuevo nombre.
    imap.create(nuevo_nombre)
    # Copia los correos del buzón anterior al nuevo buzón.
    imap.rename(buzon_anterior, nuevo_nombre)
    # Opcional: Elimina el buzón anterior si es necesario.
    imap.delete(buzon_anterior)
    print(f"Buzón '{buzon_anterior}' renombrado a '{nuevo_nombre}' con éxito.")

def salir_del_servicio():
    imap.logout()
    print("Sesión IMAP cerrada. Adiós.")
    exit()

# Menú
while True:
    print("Opciones:")
    print("1. Autenticación")
    print("2. Leer Correo")
    print("3. Crear Buzón")
    print("4. Borrar Buzón")
    print("5. Renombrar Buzón")
    print("6. Salir del Servicio")

    opcion = input("Elige una opción (1/2/3/4/5/6): ")

    if opcion == "1":
        autenticar()
    elif opcion == "2":
        leer_correo()
    elif opcion == "3":
        crear_buzon()
    elif opcion == "4":
        borrar_buzon()
    elif opcion == "5":
        renombrar_buzon()
    elif opcion == "6":
        salir_del_servicio()
    else:
        print("Opción no válida. Inténtalo de nuevo.")

# Cierre de la conexión IMAP
imap.logout()
