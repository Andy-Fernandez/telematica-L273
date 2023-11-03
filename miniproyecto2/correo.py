#Hola Carlos, te dejo los datos de la cuenta de correo para que puedas probar el programa.
#Correo: miniproy3PC@outlook.com
#Contraseña: MiniProyecto3
import imaplib
import email
from email.header import decode_header 
import os
from getpass import getpass 

def autenticar():
    imap.login(username, password)
    print("Sesión IMAP autenticada con éxito.")

def leer_correo():
    # Selecciona la bandeja de entrada "INBOX"
    status, mensajes = imap.select("INBOX") 
    print(mensajes)  # Muestra la cantidad total de mensajes en la bandeja de entrada
    
    # Número de mensajes a recibir
    N = 3 
    # Cantidad total de correos
    mensajes = int(mensajes[0])
    
    # Itera desde el último mensaje al tercer mensaje más reciente
    for i in range(mensajes, mensajes - N, -1): 
        try: 
            # Obtiene el mensaje utilizando el estándar RFC822
            res, mensaje = imap.fetch(str(i), "(RFC822)") 
        except: 
            break 
        
        for respuesta in mensaje: 
            if isinstance(respuesta, tuple): 
                # Obtiene el contenido del mensaje y lo convierte en un objeto email
                mensaje = email.message_from_bytes(respuesta[1]) 
                
                # Decodifica el asunto del mensaje
                subject = decode_header(mensaje["Subject"])[0][0] 
                if isinstance(subject, bytes): 
                    # Convierte el asunto a una cadena (string)
                    subject = subject.decode() 
                
                # Obtiene la dirección de correo del remitente
                from_ = mensaje.get("From") 
                print("Subject:", subject) 
                print("From:", from_) 
                print("Mensaje obtenido con éxito") 
                
                # Verifica si el correo es multipart (contiene múltiples partes)
                if mensaje.is_multipart(): 
                    # Recorre las partes del correo
                    for part in mensaje.walk(): 
                        # Extrae el tipo de contenido y disposición de la parte
                        content_type = part.get_content_type() 
                        content_disposition = str(part.get("Content-Disposition")) 
                        
                        try: 
                            # Obtiene el cuerpo del correo, decodifica y lo muestra
                            body = part.get_payload(decode=True).decode() 
                        except: 
                            pass 
                        
                        if content_type == "text/plain" and "attachment" not in content_disposition: 
                            # Muestra el cuerpo del correo si es de tipo "text/plain" sin archivo adjunto
                            print(body) 
                        elif "attachment" in content_disposition: 
                            # Si hay un archivo adjunto
                            nombre_archivo = part.get_filename() 
                            if nombre_archivo: 
                                if not os.path.isdir(subject): 
                                    # Crea una carpeta con el nombre del asunto para guardar el archivo adjunto
                                    os.mkdir(subject) 
                                ruta_archivo = os.path.join(subject, nombre_archivo) 
                                # Descarga y guarda el archivo adjunto
                                open(ruta_archivo, "wb").write(part.get_payload(decode=True)) 
                else: 
                    # Si el correo no es multipart, obtiene el contenido del cuerpo
                    content_type = mensaje.get_content_type() 
                    body = mensaje.get_payload(decode=True).decode() 
                    if content_type == "text/plain": 
                        # Muestra el cuerpo del correo si es de tipo "text/plain"
                        print(body) 
                # if content_type == "text/html": 
                #     # Abrir el html en el navegador 
                #     if not os.path.isdir(subject): 
                #         os.mkdir(subject) 
                #     nombre_archivo = f"{subject}.html" 
                #     ruta_archivo = os.path.join(subject, nombre_archivo) 
                #     open(ruta_archivo, "w").write(body) 
                #     # abrir el navegador 
                #     webbrowser.open(ruta_archivo) 
    #             print("********************************") 

def crear_buzon():
    # Para crear un buzón, debes proporcionar el nombre del buzón.
    nuevo_buzon = input("Nombre del nuevo buzón: ")
    # Utiliza el comando IMAP CREATE para crear el buzón.
    imap.create(nuevo_buzon)
    print(f"Buzón '{nuevo_buzon}' creado con éxito.")

def borrar_buzon():
    # Para borrar un buzón, debes proporcionar el nombre del buzón a eliminar.
    buzon_a_borrar = input("Nombre del buzón a borrar: ")
    # Utiliza el comando IMAP DELETE para eliminar el buzón.
    imap.delete(buzon_a_borrar)
    print(f"Buzón '{buzon_a_borrar}' eliminado con éxito.")

def renombrar_buzon():
    # Para renombrar un buzón, debes proporcionar el nombre del buzón anterior y el nuevo nombre.
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

# Datos del usuario
username = input("Correo: ") 
password = getpass("Password: ") 

# Crear conexión
imap = imaplib.IMAP4_SSL("outlook.office365.com")
# iniciar sesión
imap.login(username, password)

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

imap.close() 
imap.logout()