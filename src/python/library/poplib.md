---
title: '"poplib" --- POP3 protocol client'
source_url: https://docs.python.org/es/3
source_path: library/poplib.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3500
---

# "poplib" --- POP3 protocol client

**Código fuente:** Lib/poplib.py

======================================================================

Este módulo define una clase, "POP3", que encapsula una conexión a un
servidor POP3 e implementa el protocolo como está definido en **RFC
1939**. La clase "POP3" soporta los mínimos y opcionales conjuntos de
comandos de **RFC 1939**. La clase "POP3" también soporta el comando
"STLS" introducido en **RFC 2595** para habilitar comunicación
encriptada en una conexión ya establecida.

Adicionalmente, este módulo provee una clase "POP3_SSL", que provee
soporte para conectar servidores POP3 que usan SSL como una capa de
protocolo subyacente.

Note que POP3, aunque ampliamente soportado, es obsoleto. La calidad
de implementación de servidores POP3 varía ampliamente, y muchos son
bastante pobres. Si su servidor de correo soporta IMAP, sería mejor
utilizar la clase "imaplib.IMAP4", ya que los servidores IMAP tienden
a estar mejor implementados.

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

The "poplib" module provides two classes:

class poplib.POP3(host, port=POP3_PORT[, timeout])

   Esta clase implementa el protocolo POP3 actual. La conexión es
   creada cuando la instancia es inicializada. Si *port* se omite, el
   puerto POP3 estándar (110) es utilizado. El parámetro opcional
   *timeout* especifica un tiempo de espera en segundos para el
   intento de conexión (si no se especifica, la configuración global
   de tiempo de espera será utilizada).

   Genera un evento de auditoría "poplib.connect" con argumentos
   "self", "host", "port".

   Todos los comandos lanzarán un evento de auditoría "poplib.putline"
   con argumentos "self" y "line", donde "line" son los bytes a ser
   enviados al host remoto.

   Distinto en la versión 3.9: Si el parámetro *timeout* se establece
   en cero, lanzará un "ValueError" para evitar la creación de un
   socket sin bloqueo.

class poplib.POP3_SSL(host, port=POP3_SSL_PORT, *, timeout=None, context=None)

   Esta es una subclase de "POP3" que conecta al servidor sobre un
   socket SSL encriptado. Si *port* no es especificado, 995, el puerto
   POP3-over-SSL es utilizado. *timeout* funciona como en el
   constructor  de la clase "POP3". *context* es un objeto
   "ssl.SSLContext" opcional que permite empaquetar opciones de
   configuración SSL, certificados y llaves privadas en una única
   (potencialmente longeva) estructura. Por favor lea Consideraciones
   de seguridad para buenas prácticas.

   Genera un evento de auditoría "poplib.connect" con argumentos
   "self", "host", "port".

   Todos los comandos lanzarán un evento de auditoría "poplib.putline"
   con argumentos "self" y "line", donde "line" son los bytes a ser
   enviados al host remoto.

   Distinto en la versión 3.2: Parámetro *context* agregado.

   Distinto en la versión 3.4: The class now supports hostname check
   with "ssl.SSLContext.check_hostname" and *Server Name Indication*
   (see "ssl.HAS_SNI").

   Distinto en la versión 3.9: Si el parámetro *timeout* se establece
   en cero, lanzará un "ValueError" para evitar la creación de un
   socket sin bloqueo.

   Distinto en la versión 3.12: The deprecated *keyfile* and
   *certfile* parameters have been removed.

One exception is defined as an attribute of the "poplib" module:

exception poplib.error_proto

   Excepción generada en cualquier error de este módulo (errores del
   módulo "socket" no son capturadas). La razón para la excepción es
   pasada al constructor como una cadena.

Ver también:

  Módulo "imaplib"
     El módulo IMAP de Python.

  Preguntas Frecuentes Sobre Fetchmail
     Las preguntas frecuentes para el cliente POP/IMAP **fetchmail**
     colecciona información en las variaciones del servidor POP3 e
     incumplimiento de RFC que puede ser útil si usted necesita
     escribir una aplicación basada en el protocolo POP.

## Objetos POP3

Todos los comandos POP3 están representados por métodos del mismo
nombre, en minúsculas; la mayoría retorna el texto de respuesta
enviado por el servidor.

Una instancia "POP3" tiene los siguientes métodos:

POP3.set_debuglevel(level)

   Establece el nivel de depuración de la instancia. Esto controla la
   cantidad de salida de depuración impresa. Por defecto, "0", no
   produce salida de depuración. Un valor de "1" produce una moderada
   cantidad de salida de depuración, generalmente una única línea por
   solicitud. Un valor de "2" o mayor produce la máxima cantidad de
   salida de depuración, registrando cada línea enviada y recibida en
   la conexión de control.

POP3.getwelcome()

   Retorna la cadena de saludo enviada por el servidor POP3.

POP3.capa()

   Consulta las capacidades del servidor como está especificado en
   **RFC 2449**. Retorna un diccionario en la forma "{'nombre':
   ['param'...]}".

   Added in version 3.4.

POP3.user(username)

   Envía el comando del usuario, la respuesta debería indicar que una
   contraseña es requerida.

POP3.pass_(password)

   Send password, response includes message count and mailbox size.
   Note: the mailbox on the server is locked until "quit()" is called.

POP3.apop(user, secret)

   Utiliza la autenticación APOP (más segura) para registrar en el
   servidor POP3.

POP3.rpop(user)

   Utiliza autenticación RPOP (similar a los comandos r de UNIX) para
   registrar en el servidor POP3.

POP3.stat()

   Obtiene el estado del buzón de correo. El resultado es una tupla de
   2 enteros: "(conteo de mensaje, tamaño del buzón de correo)".

POP3.list([which])

   Solicita lista de mensajes, el resultado es en la forma
   "(respuesta, ['mesg_num octets', ...], octets)". Si *which* está
   establecido, es el mensaje a listar.

POP3.retr(which)

   Recupera el número de mensaje completo *which*, y establece marca
   de visto. El resultado es en la forma "(respuesta, ['line', ...],
   octets)".

POP3.dele(which)

   Marca el número de mensaje *which* para eliminación. En la mayoría
   de los servidores las eliminaciones no están actualmente
   presentadas hasta QUIT (la mayor excepción es Eudora QPOP, que
   deliberadamente viola las RFC haciendo eliminaciones pendientes en
   cada desconexión).

POP3.rset()

   Remueve las marcas de eliminación para el buzón de correo.

POP3.noop()

   No hace nada. Puede ser utilizado como keep-alive.

POP3.quit()

   Cierra sesión: envía los cambios, desbloquea el buzón de correo,
   desconecta.

POP3.top(which, howmuch)

   Recupera la cabecera del mensaje mas *howmuch* las líneas del
   mensaje después del cabecera del número de mensajes *which*. El
   resultado es en la forma "(respuesta, ['línea', ...]. octets)".

   El comando TOP POP3 que este método utiliza, a diferencia del
   comando RETR, no establece la marca de visto del mensaje;
   desafortunadamente, TOP está pobremente especificado en las RFC y
   se rompe con frecuencia en servidores off-brand. Pruebe este método
   a mano contra los servidores POP3 que usted utilizará antes de
   confiar en él.

POP3.uidl(which=None)

   Retorna la lista del resumen de mensajes (id único). Si *which* es
   especificado, el resultado contiene el id único para ese mensaje en
   la forma "'response mesgnum uid", de otra forma el resultado es una
   lista "(respuesta, ['mengnum uid', ...], octets)".

POP3.utf8()

   Trata de cambiar al modo UTF-8. Retorna la respuesta del servidor
   si es exitosa, genera "error_proto" si no. Especificado en **RFC
   6856**.

   Added in version 3.5.

POP3.stls(context=None)

   Comienza una sesión TLS en la conexión activa como está
   especificado en **RFC 2595**. Esto es únicamente permitido antes de
   la autenticación de usuario

   El parámetro *context* es un objeto "ssl.SSLContext" que permite
   empaquetar opciones de configuración SSL, certificados y llaves
   privadas en una única (potencialmente longeva) estructura. Por
   favor lea Consideraciones de seguridad para buenas prácticas.

   This method supports hostname checking via
   "ssl.SSLContext.check_hostname" and *Server Name Indication* (see
   "ssl.HAS_SNI").

   Added in version 3.4.

Instancias de "POP3_SSL" no tienen métodos adicionales. La interfaz de
esta subclase es idéntica a su padre.

## Ejemplo POP3

Este es un ejemplo mínimo (sin chequeo de errores) que abre un buzón
de correo y retorna e imprime todos los mensajes:

   import getpass, poplib

   M = poplib.POP3('localhost')
   M.user(getpass.getuser())
   M.pass_(getpass.getpass())
   numMessages = len(M.list()[1])
   for i in range(numMessages):
       for j in M.retr(i+1)[1]:
           print(j)

Al final del módulo, hay una sección de test que contiene un ejemplo
más extensivo de uso.
