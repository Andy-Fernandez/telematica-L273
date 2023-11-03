#Correo: miniproy3PC@outlook.com
#Contraseña: MiniProyecto3
# Importar bibliotecas necesarias
import imaplib  # Para acceder a buzones de correo IMAP
import email    # Para trabajar con mensajes de correo electrónico
from email.header import decode_header  # Para decodificar encabezados de correo
import os      # Para operaciones con el sistema de archivos
from getpass import getpass  # Para obtener la contraseña del usuario sin mostrarla en pantalla


# Definir función para autenticación en el servidor IMAP
#def autenticar():
    # Iniciar sesión en el servidor IMAP con el nombre de usuario y contraseña proporcionados
 #   imap.login(username, password)
 #   print("Sesión IMAP autenticada con éxito.")


# Definir función para leer correos en la bandeja de entrada
def leer_correo():
    # Seleccionar la bandeja de entrada
    status, mensajes = imap.select("INBOX")
    print(mensajes)
    # Definir cuántos correos deseamos recibir
    N = 3
    # Obtener la cantidad total de correos en la bandeja de entrada
    mensajes = int(mensajes[0])
    # Recorrer los últimos N correos
    for i in range(mensajes, mensajes - N, -1):
        try:
            # Obtener el mensaje
            res, mensaje = imap.fetch(str(i), "(RFC822)")
        except:
            break
        for respuesta in mensaje:
            if isinstance(respuesta, tuple):
                # Obtener el contenido del mensaje
                mensaje = email.message_from_bytes(respuesta[1])
                # Decodificar el asunto del correo
                subject = decode_header(mensaje["Subject"])[0][0]
                if isinstance(subject, bytes):
                    # Convertir el asunto a cadena de texto si es necesario
                    subject = subject.decode()
                # Obtener el remitente del correo
                from_ = mensaje.get("From")
                print("Subject:", subject)
                print("From:", from_)
                print("Mensaje obtenido con éxito")
                # Si el correo es multipart (tiene partes múltiples, como texto y archivos adjuntos)
                if mensaje.is_multipart():
                    # Recorrer las partes del correo
                    for part in mensaje.walk():
                        # Obtener información sobre la parte
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            # Obtener el cuerpo del correo
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            # Mostrar el cuerpo del correo si es texto plano
                            print(body)
                        elif "attachment" in content_disposition:
                            # Descargar archivos adjuntos
                            nombre_archivo = part.get_filename()
                            if nombre_archivo:
                                if not os.path.isdir(subject):
                                    # Crear una carpeta para el mensaje si no existe
                                    os.mkdir(subject)
                                ruta_archivo = os.path.join(subject, nombre_archivo)
                                # Guardar el archivo adjunto
                                open(ruta_archivo, "wb").write(part.get_payload(decode=True))
                else:
                    # Si el correo no es multipart, simplemente obtener y mostrar el cuerpo del mensaje
                    content_type = mensaje.get_content_type()
                    body = mensaje.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        print(body)
# Definir función para crear un nuevo buzón
def crear_buzon():
    # Solicitar al usuario el nombre del nuevo buzón
    nuevo_buzon = input("Nombre del nuevo buzón: ")
    # Utilizar el comando IMAP CREATE para crear el buzón
    imap.create(nuevo_buzon)
    print(f"Buzón '{nuevo_buzon}' creado con éxito.")

# Definir función para borrar un buzón
def borrar_buzon():
    # Solicitar al usuario el nombre del buzón a borrar
    buzon_a_borrar = input("Nombre del buzón a borrar: ")
    # Utilizar el comando IMAP DELETE para eliminar el buzón
    imap.delete(buzon_a_borrar)
    print(f"Buzón '{buzon_a_borrar}' eliminado con éxito.")

# Definir función para renombrar un buzón
def renombrar_buzon():
    # Solicitar al usuario el nombre del buzón anterior y el nuevo nombre
    buzon_anterior = input("Nombre del buzón a renombrar: ")
    nuevo_nombre = input("Nuevo nombre del buzón: ")
    # Crear un nuevo buzón con el nuevo nombre
    imap.create(nuevo_nombre)
    # Copiar los correos del buzón anterior al nuevo buzón
    imap.rename(buzon_anterior, nuevo_nombre)
    # Opcionalmente, eliminar el buzón anterior si es necesario
    imap.delete(buzon_anterior)
    print(f"Buzón '{buzon_anterior}' renombrado a '{nuevo_nombre}' con éxito.")

# Definir función para salir del servicio
def salir_del_servicio():
    # Cerrar la sesión IMAP
    imap.logout()
    print("Sesión IMAP cerrada. Adiós.")
    exit()

# Solicitar al usuario su nombre de usuario y contraseña
username = input("Correo: ")
password = getpass("Password: ")

# Crear una conexión IMAP con el servidor de Outlook Office 365
imap = imaplib.IMAP4_SSL("outlook.office365.com")
# Iniciar sesión con el nombre de usuario y contraseña
imap.login(username, password)

# Menú de opciones para el usuario
while True:
    print("Opciones:")
   # print("1. Autenticación")
    print("1. Leer Correo")
    print("2. Crear Buzón")
    print("3. Borrar Buzón")
    print("4. Renombrar Buzón")
    print("5. Salir del Servicio")

    opcion = input("Elige una opción (1/2/3/4/5): ")

    if opcion == "0":
        #autenticar()
        pass
    elif opcion == "1":
        leer_correo()
    elif opcion == "2":
        crear_buzon()
    elif opcion == "3":
        borrar_buzon()
    elif opcion == "4":
        renombrar_buzon()
    elif opcion == "5":
        salir_del_servicio()
    else:
        print("Opción no válida. Inténtalo de nuevo.")

# Cerrar la conexión IMAP al final del programa
imap.close()
imap.logout()