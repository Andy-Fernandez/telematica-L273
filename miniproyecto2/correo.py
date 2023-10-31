import imaplib 
import email 
from email.header import decode_header 
import os 
from getpass import getpass 
 
# Datos del usuario 
username = input("Correo: ") 
password = getpass("Password: ") 
 
# Crear conexión 
imap = imaplib.IMAP4_SSL("outlook.office365.com") 
# iniciar sesión 
imap.login(username, password) 
  
status, mensajes = imap.select("INBOX") 
print(mensajes) 


def autenticar():
    # Ya tienes esta parte en tu código para iniciar sesión.
    imap.login(username, password)
    print("Sesión IMAP autenticada con éxito.")

def leer_correo():
    # mensajes a recibir 
    N = 3 
    # cantidad total de correos 
    mensajes = int(mensajes[0]) 
    
    for i in range(mensajes, mensajes - N, -1): 
        # print(f"vamos por el mensaje: {i}") 
    #     # Obtener el mensaje 
        try: 
            res, mensaje = imap.fetch(str(i), "(RFC822)") 
        except: 
            break 
        for respuesta in mensaje: 
            if isinstance(respuesta, tuple): 
                # Obtener el contenido 
                mensaje = email.message_from_bytes(respuesta[1]) 
                # decodificar el contenido 
                subject = decode_header(mensaje["Subject"])[0][0] 
                if isinstance(subject, bytes): 
                    # convertir a string 
                    subject = subject.decode() 
                # de donde viene el correo 
                from_ = mensaje.get("From") 
                print("Subject:", subject) 
                print("From:", from_) 
                print("Mensaje obtenido con exito") 
                # si el correo es html 
                if mensaje.is_multipart(): 
                    # Recorrer las partes del correo 
                    for part in mensaje.walk(): 
                        # Extraer el contenido 
                        content_type = part.get_content_type() 
                        content_disposition = str(part.get("Content-Disposition")) 
                        try: 
                            # el cuerpo del correo 
                            body = part.get_payload(decode=True).decode() 
                        except: 
                            pass 
                        if content_type == "text/plain" and "attachment" not in content_disposition: 
                            # Mostrar el cuerpo del correo 
                            print(body) 
                        elif "attachment" in content_disposition: 
    #                         # download attachment 
                            nombre_archivo = part.get_filename() 
                            if nombre_archivo: 
                                if not os.path.isdir(subject): 
                                    # crear una carpeta para el mensaje 
                                    os.mkdir(subject) 
                                ruta_archivo = os.path.join(subject, nombre_archivo) 
                                # download attachment and save it 
                                open(ruta_archivo, "wb").write(part.get_payload(decode=True)) 
                else: 
                    # contenido del mensaje 
                    content_type = mensaje.get_content_type() 
                    # cuerpo del mensaje 
                    body = mensaje.get_payload(decode=True).decode() 
                    if content_type == "text/plain": 
    #                     # mostrar solo el texto 
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


imap.close() 
imap.logout()