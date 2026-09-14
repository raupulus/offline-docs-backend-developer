---
title: '"smtplib" --- SMTP protocol client'
source_url: https://docs.python.org/es/3
source_path: library/smtplib.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3820
---

# "smtplib" --- SMTP protocol client

**Código fuente:** Lib/smtplib.py

======================================================================

The "smtplib" module defines an SMTP client session object that can be
used to send mail to any internet machine with an SMTP or ESMTP
listener daemon.  For details of SMTP and ESMTP operation, consult
**RFC 821** (Simple Mail Transfer Protocol) and **RFC 1869** (SMTP
Service Extensions).

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

class smtplib.SMTP(host='', port=0, local_hostname=None, [timeout, ]source_address=None)

   Una instancia "SMTP" encapsula una conexión SMTP. Tiene métodos que
   admiten un repertorio completo de operaciones SMTP y ESMTP. Si se
   proporcionan los parámetros de *port* y *host* opcionales, se llama
   al método SMTP "connect()" con esos parámetros durante la
   inicialización. Si se especifica, *local_hostname* se utiliza como
   FQDN del host local en el comando HELO /EHLO. De lo contrario, el
   nombre de host local se encuentra mediante "socket.getfqdn()". Si
   la llamada "connect()" retorna algo que no sea un código de éxito,
   se lanza un "SMTPConnectError". El parámetro opcional *timeout*
   especifica un tiempo de espera en segundos para bloquear
   operaciones como el intento de conexión (si no se especifica, se
   utilizará la configuración de tiempo de espera global
   predeterminada). Si expira el tiempo de espera, se lanza
   "TimeoutError". El parámetro opcional *source_address* permite la
   vinculación a alguna dirección de origen específica en una máquina
   con múltiples interfaces de red y/o algún puerto TCP de origen
   específico. Se necesita una tupla de 2 (host, port), para que el
   socket se vincule como su dirección de origen antes de conectarse.
   Si se omite (o si el *host* o el *port* son "''" y/o 0
   respectivamente), se utilizará el comportamiento predeterminado del
   sistema operativo.

   Para un uso normal, solo debe requerir los métodos
   initialization/connect, "sendmail()" y "SMTP.quit()". A
   continuación se incluye un ejemplo.

   La clase "SMTP" admite la instrucción "with". Cuando se usa así, el
   comando SMTP "QUIT" se emite automáticamente cuando la "with" sale
   de la instrucción. por ejemplo:

      >>> from smtplib import SMTP
      >>> with SMTP("domain.org") as smtp:
      ...     smtp.noop()
      ...
      (250, b'Ok')
      >>>

   Todos los comandos lanzarán un evento de auditoría
   "smtplib.SMTP.send" con argumentos "self" y "data", donde "data"
   son los bytes que están a punto de ser enviado al host remoto.

   Distinto en la versión 3.3: Se agregó soporte para la sentencia
   "with".

   Distinto en la versión 3.3: Se agregó el argumento
   *source_address*.

   Added in version 3.5: La extensión SMTPUTF8 (**RFC 6531**) ahora es
   compatible.

   Distinto en la versión 3.9: Si el parámetro *timeout* se define a
   cero, lanzará un "ValueError" para evitar la creación de un socket
   no bloqueado.

class smtplib.SMTP_SSL(host='', port=0, local_hostname=None, *, [timeout, ]context=None, source_address=None)

   An "SMTP_SSL" instance behaves exactly the same as instances of
   "SMTP". "SMTP_SSL" should be used for situations where SSL is
   required from the beginning of the connection and using
   "starttls()" is not appropriate. If *host* is not specified, the
   local host is used. If *port* is zero, the standard SMTP-over-SSL
   port (465) is used.  The optional arguments *local_hostname*,
   *timeout* and *source_address* have the same meaning as they do in
   the "SMTP" class.  *context*, also optional, can contain a
   "SSLContext" and allows configuring various aspects of the secure
   connection.  Please read Consideraciones de seguridad for best
   practices.

   Distinto en la versión 3.3: se agregó *contexto*.

   Distinto en la versión 3.3: Se agregó el argumento
   *source_address*.

   Distinto en la versión 3.4: La clase ahora admite la verificación
   del nombre de host con "ssl.SSLContext.check_hostname" y *Server
   Name Indication* (ver "ssl.HAS_SNI").

   Distinto en la versión 3.9: Si el parámetro *timeout* se define a
   cero, lanzará un "ValueError" para evitar la creación de un socket
   no bloqueado

   Distinto en la versión 3.12: Los parámetros obsoletos *keyfile y
   *certifile* se han eliminado.

class smtplib.LMTP(host='', port=LMTP_PORT, local_hostname=None, source_address=None[, timeout])

   The LMTP protocol, which is very similar to ESMTP, is heavily based
   on the standard SMTP client. It's common to use Unix sockets for
   LMTP, so our "connect()" method must support that as well as a
   regular host:port server. The optional arguments *local_hostname*
   and *source_address* have the same meaning as they do in the "SMTP"
   class. To specify a Unix socket, you must use an absolute path for
   *host*, starting with a '/'.

   Se admite la autenticación mediante el mecanismo SMTP habitual.
   Cuando se usa un socket Unix, LMTP generalmente no admite ni
   requiere autenticación, pero su millaje puede variar.

   Distinto en la versión 3.9: Se ha añadido el parámetro opcional
   *timeout*.

También se define una buena selección de excepciones:

exception smtplib.SMTPException

   Subclase de "OSError" que es la clase de excepción base para todas
   las demás excepciones proporcionadas por este módulo.

   Distinto en la versión 3.4: SMTPException se convirtió en subclase
   de "OSError"

exception smtplib.SMTPServerDisconnected

   Esta excepción se genera cuando el servidor se desconecta
   inesperadamente o cuando se intenta usar la instancia "SMTP" antes
   de conectarlo a un servidor.

exception smtplib.SMTPResponseException

   Base class for all exceptions that include an SMTP error code.
   These exceptions are generated in some instances when the SMTP
   server returns an error code.

   smtp_code

      The error code.

   smtp_error

      The error message.

exception smtplib.SMTPSenderRefused

   Dirección del remitente rechazada.  Además de los atributos
   establecidos por todas las excepciones "SMTPResponseException",
   éste establece 'remitente' para la cadena de caracteres que el
   servidor SMTP rechazó.

exception smtplib.SMTPRecipientsRefused

   All recipient addresses refused.

   recipients

      A dictionary of exactly the same sort as returned by
      "SMTP.sendmail()" containing the errors for each recipient.

exception smtplib.SMTPDataError

   El servidor SMTP se negó a aceptar los datos del mensaje.

exception smtplib.SMTPConnectError

   Se produjo un error durante el establecimiento de conexión  con el
   servidor.

exception smtplib.SMTPHeloError

   El servidor rechazó nuestro mensaje "HELO".

exception smtplib.SMTPNotSupportedError

   El servidor no admite el comando o la opción que se intentó.

   Added in version 3.5.

exception smtplib.SMTPAuthenticationError

   La autenticación SMTP salió mal.  Lo más probable es que el
   servidor no aceptó la combinación proporcionada de
   username/password.

Ver también:

  **RFC 821** -  Protocolo Simple de Transferencia
     Definición de protocolo para SMTP. Este documento cubre el
     modelo, el procedimiento operativo y los detalles del protocolo
     para SMTP.

  **RFC 1869** - Extensiones de Servicio SMTP
     Definición de las extensiones ESMTP para SMTP. Esto describe un
     marco para extender SMTP con nuevos comandos, que admite el
     descubrimiento dinámico de los comandos proporcionados por el
     servidor y define algunos comandos adicionales.

## Objetos SMTP

Una instancia "SMTP" tiene los siguientes métodos:

SMTP.set_debuglevel(level)

   Establezca el nivel de salida de depuración. Un valor de 1 o "True"
   para *level* da como resultado mensajes de depuración para la
   conexión y para todos los mensajes enviados y recibidos desde el
   servidor. Un valor de 2 para *level* da como resultado que estos
   mensajes tengan una marca de tiempo.

   Distinto en la versión 3.5: Se agregó el nivel de depuración 2.

SMTP.docmd(cmd, args='')

   Envía un comando *cmd* al servidor.  El argumento opcional *args*
   simplemente se concatena con el comando, separado por un espacio.

   Esto devuelve una tupla de 2 compuestos por un código de respuesta
   numérico y la línea de respuesta real (las respuestas de varias
   líneas se unen en una línea larga).

   En funcionamiento normal, no debería ser necesario llamar a este
   método explícitamente. Se utiliza para implementar otros métodos y
   puede resultar útil para probar extensiones privadas.

   Si se pierde la conexión con el servidor mientras se espera la
   respuesta, se activará "SMTPServerDisconnected".

SMTP.connect(host='localhost', port=0)

   Conéctese a un host en un puerto determinado. Los valores
   predeterminados son para conectarse al host local en el puerto SMTP
   estándar (25). Si el nombre de host termina con dos puntos ("':'")
   seguido de un número, ese sufijo se eliminará y el número se
   interpretará como el número de puerto a utilizar. El constructor
   invoca automáticamente este método si se especifica un host durante
   la instanciación. Devuelve una tupla de 2 del código de respuesta y
   el mensaje enviado por el servidor en su respuesta de conexión.

   Genera un evento de auditoría "smtplib.connect" con argumentos
   "self", "host", "port".

SMTP.helo(name='')

   Identifíquese en el servidor SMTP usando "HELO". El argumento del
   nombre de host tiene como valor predeterminado el nombre de dominio
   completo del host local. El mensaje devuelto por el servidor se
   almacena como el atributo "helo_resp" del objeto.

   En funcionamiento normal, no debería ser necesario llamar a este
   método explícitamente. Será llamado implícitamente por "sendmail()"
   cuando sea necesario.

SMTP.ehlo(name='')

   Identifíquese en un servidor ESMTP mediante "EHLO". El argumento
   del nombre de host tiene como valor predeterminado el nombre de
   dominio completo del host local. Examine la respuesta para la
   opción ESMTP y guárdelos para que los utilice "has_extn()". También
   establece varios atributos informativos: el mensaje retornado por
   el servidor se almacena como el atributo "ehlo_resp", "does_esmtp"
   se establece en "True" o "False" dependiendo de si el servidor
   admite ESMTP, y "esmtp_features" será un diccionario que contiene
   los nombres de las extensiones de servicio SMTP de este servidor
   soportes, y sus parámetros (si los hay).

   A menos que desee utilizar "has_extn()" antes de enviar correo, no
   debería ser necesario llamar a este método explícitamente. Se
   llamará implícitamente por "sendmail()" cuando sea necesario.

SMTP.ehlo_or_helo_if_needed()

   Este método llama a "ehlo()" o "helo()" si no ha habido ningún
   comando "EHLO" o "HELO" anterior en esta sesión. Primero prueba
   ESMTP "EHLO".

   "SMTPHeloError"
      El servidor no respondió correctamente al saludo "HELO".

SMTP.has_extn(name)

   Retorna "True" si *name* está en el conjunto de extensiones de
   servicio SMTP devueltas por el servidor, "False" en caso contrario.
   El método es insensible a la presencia de mayúsculas en *name*.

SMTP.verify(address)

   Verifique la validez de una dirección en este servidor usando SMTP
   "VRFY". Retorna una tupla que consta del código 250 y una dirección
   completa **RFC 822** (incluido el nombre humano) si la dirección
   del usuario es válida. De lo contrario, devuelve un código de error
   SMTP de 400 o más y una cadena de error.

   Nota:

     Muchos sitios desactivan SMTP "VRFY" para frustrar a los
     spammers.

SMTP.login(user, password, *, initial_response_ok=True)

   Inicie sesión en un servidor SMTP que requiera autenticación. Los
   argumentos son el nombre de usuario y la contraseña para
   autenticarse. Si no ha habido ningún comando "EHLO" o "HELO"
   anterior en esta sesión, este método prueba primero ESMTP "EHLO".
   Este método regresará normalmente si la autenticación fue exitosa o
   puede generar las siguientes excepciones:

   "SMTPHeloError"
      El servidor no respondió correctamente al saludo "HELO".

   "SMTPAuthenticationError"
      El servidor no aceptó la combinación de nombre de
      username/password.

   "SMTPNotSupportedError"
      El servidor no admite el comando "AUTH".

   "SMTPException"
      No se encontró ningún método de autenticación adecuado.

   Each of the authentication methods supported by "smtplib" are tried
   in turn if they are advertised as supported by the server.  See
   "auth()" for a list of supported authentication methods.
   *initial_response_ok* is passed through to "auth()".

   El argumento de palabra clave opcional *initial_response_ok*
   especifica si, para los métodos de autenticación que lo admiten, se
   puede enviar una "respuesta inicial" como se especifica en **RFC
   4954** junto con el comando "AUTH", en lugar de requerir un
   desafío/respuesta .

   Distinto en la versión 3.5: "SMTPNotSupportedError" se puede
   generar y se agregó el parámetro *initial_response_ok*.

SMTP.auth(mechanism, authobject, *, initial_response_ok=True)

   Emita un comando "SMTP" "AUTH" para el *mechanism* de autenticación
   especificado y maneje la respuesta de desafío a través de
   *authobject*.

   *mechanism* especifica qué mecanismo de autenticación se utilizará
   como argumento para el comando "AUTH"; los valores válidos son los
   enumerados en el elemento "auth" de "esmtp_features".

   *authobject* debe ser un objeto que se pueda invocar y  que tome un
   único argumento opcional:

      data = authobject(challenge=None)

   Si la verificación de respuesta inicial devuelve "None", o si
   *initial_response_ok* es falso, se llamará a "authobject()" para
   procesar la respuesta de desafío del servidor; el argumento
   *challenge* que se pasa será un "bytes". Debería devolver *data*
   ASCII "str" que serán codificados en base64 y enviados al servidor.

   Si la verificación de respuesta inicial devuelve "None", o si
   *initial_response_ok* es falso, se llamará a "authobject()" para
   procesar la respuesta de desafío del servidor; el argumento
   *challenge* que se pasa será un "bytes". Debería devolver *data*
   ASCII "str" que serán codificados en base64 y enviados al servidor.

   La clase "SMTP" proporciona "authobjects" para los mecanismos
   "CRAM-MD5", "PLAIN" y "LOGIN"; se denominan "SMTP.auth_cram_md5",
   "SMTP.auth_plain" y "SMTP.auth_login" respectivamente. Todos
   requieren que las propiedades de "user" y "password" de la
   instancia "SMTP" se establezcan en los valores adecuados.

   User code does not normally need to call "auth" directly, but can
   instead call the "login()" method, which will try each of the above
   mechanisms in turn, in the order listed.  "auth" is exposed to
   facilitate the implementation of authentication methods not (or not
   yet) supported directly by "smtplib".

   Added in version 3.5.

SMTP.starttls(*, context=None)

   Ponga la conexión SMTP en modo TLS (Seguridad de la capa de
   transporte). Todos los comandos SMTP que siguen se cifrarán.
   Entonces deberías llamar a "ehlo()" de nuevo.

   Si se proporcionan *keyfile* y *certfile*, se utilizan para crear
   una "ssl.SSLContext".

   El parámetro *context* opcional es un objeto "ssl.SSLContext"; Esta
   es una alternativa al uso de un archivo de claves y un archivo de
   certificado y, si se especifica, tanto *keyfile* como *certfile*
   deben ser "None".

   Si no ha habido ningún comando "EHLO" o "HELO" anterior en esta
   sesión, este método intenta ESMTP "EHLO" primero.

   Distinto en la versión 3.12: Los parámetros obsoletos *keyfile y
   *certifile* se han eliminado.

   "SMTPHeloError"
      El servidor no respondió correctamente al saludo "HELO".

   "SMTPNotSupportedError"
      El servidor no admite la extensión STARTTLS.

   "RuntimeError"
      La compatibilidad con SSL/TLS no está disponible para su
      intérprete de Python.

   Distinto en la versión 3.3: se agregó *contexto*.

   Distinto en la versión 3.4: The method now supports hostname check
   with "ssl.SSLContext.check_hostname" and *Server Name Indicator*
   (see "HAS_SNI").

   Distinto en la versión 3.5: El error generado por falta de
   compatibilidad con STARTTLS ahora es la subclase
   "SMTPNotSupportedError" en lugar de la base "SMTPException".

SMTP.sendmail(from_addr, to_addrs, msg, mail_options=(), rcpt_options=())

   Send mail.  The required arguments are an **RFC 822** from-address
   string, a list of **RFC 822** to-address strings (a bare string
   will be treated as a list with 1 address), and a message string.
   The caller may pass a list of ESMTP options (such as ""8bitmime"")
   to be used in "MAIL FROM" commands as *mail_options*. ESMTP options
   (such as "DSN" commands) that should be used with all "RCPT"
   commands can be passed as *rcpt_options*. Each option should be
   passed as a string containing the full text of the option,
   including any potential key (for instance,
   ""NOTIFY=SUCCESS,FAILURE""). (If you need to use different ESMTP
   options to different recipients you have to use the low-level
   methods such as "mail()", "rcpt()" and "data()" to send the
   message.)

   Nota:

     Los parámetros *from_addr* y *to_addrs* se utilizan para
     construir el sobre del mensaje utilizado por los agentes de
     transporte. "sendmail" no modifica los encabezados de los
     mensajes de ninguna manera.

   *msg* puede ser una cadena que contenga caracteres en el rango
   ASCII o una cadena de bytes. Una cadena se codifica en bytes
   utilizando el códec ascii, y los caracteres "\r" y "\n" solitarios
   se convierten en caracteres "\ r\n". Una cadena de bytes no se
   modifica.

   Si no ha habido ningún comando "EHLO" o "HELO" anterior en esta
   sesión, este método prueba primero ESMTP "EHLO". Si el servidor
   utiliza ESMTP, se le pasará el tamaño del mensaje y cada una de las
   opciones especificadas (si la opción está en el conjunto de
   funciones que anuncia el servidor). Si "EHLO" falla, se probará
   "HELO" y se eliminarán las opciones de ESMTP.

   Este método volverá normalmente si se acepta el correo para al
   menos un destinatario. De lo contrario, lanzará una excepción. Es
   decir, si este método no genera una excepción, alguien debería
   recibir su correo. Si este método no genera una excepción, devuelve
   un diccionario, con una entrada para cada destinatario rechazado.
   Cada entrada contiene una tupla del código de error SMTP y el
   mensaje de error adjunto enviado por el servidor.

   Si se incluye "SMTPUTF8"' en *mail_options * y el servidor lo
   admite, *from_addr* y *to_addrs* pueden contener caracteres no
   ASCII.

   Este método puede lanzar las siguientes excepciones:

   "SMTPRecipientsRefused"
      All recipients were refused.  Nobody got the mail.

   "SMTPHeloError"
      El servidor no respondió correctamente al saludo "HELO".

   "SMTPSenderRefused"
      El servidor no aceptó el *from_addr*.

   "SMTPDataError"
      El servidor respondió con un código de error inesperado (que no
      sea el rechazo de un destinatario).

   "SMTPNotSupportedError"
      Se proporcionó "SMTPUTF8" en *mail_options* pero el servidor no
      lo admite.

   A menos que se indique lo contrario, la conexión estará abierta
   incluso después de que se lance una excepción.

   Distinto en la versión 3.2: *msg* puede ser una cadena de bytes.

   Distinto en la versión 3.5: Se agregó compatibilidad con
   "SMTPUTF8", así que la "SMTPNotSupportedError" puede ser lanzada si
   se especifica "SMTPUTF8" ya que el servidor no lo admite.

SMTP.send_message(msg, from_addr=None, to_addrs=None, mail_options=(), rcpt_options=())

   Este es un método conveniente para llamar a "sendmail()" con el
   mensaje representado por un objeto "email.message.Message". Los
   argumentos tienen el mismo significado que para "sendmail()",
   excepto que *msg* es un objeto "Mensaje".

   Si *from_addr* es "None" o *to_addrs* es "None", "send_message"
   llena esos argumentos con direcciones extraídas de los encabezados
   de *msg* como se especifica en **RFC 5322**: *from_addr* se
   establece en el campo *Sender* si está presente, y de lo contrario,
   en el campo *From*. *to_addrs* combina los valores (si los hay) de
   los campos *To*, *Cc* y *Bcc* de *msg*. Si aparece exactamente un
   conjunto de encabezados *Resent-** en el mensaje, los encabezados
   normales se ignoran y en su lugar se utilizan los encabezados
   *Resent- **. Si el mensaje contiene más de un conjunto de
   encabezados *Resent-**, se lanza un "ValueError", ya que no hay
   forma de detectar sin ambigüedades el conjunto más reciente de
   encabezados *Resent-*.

   "send_message" serializes *msg* using "BytesGenerator" with "\r\n"
   as the *linesep*, and calls "sendmail()" to transmit the resulting
   message.  Regardless of the values of *from_addr* and *to_addrs*,
   "send_message" does not transmit any *Bcc* or *Resent-Bcc* headers
   that may appear in *msg*.  If any of the addresses in *from_addr*
   and *to_addrs* contain non-ASCII characters and the server does not
   advertise "SMTPUTF8" support, an "SMTPNotSupportedError" is raised.
   Otherwise the "Message" is serialized with a clone of its "policy"
   with the "utf8" attribute set to "True", and "SMTPUTF8" and
   "BODY=8BITMIME" are added to *mail_options*.

   Added in version 3.2.

   Added in version 3.5: Soporte para direcciones internacionalizadas
   ("SMTPUTF8").

SMTP.quit()

   Termine la sesión SMTP y cierre la conexión.  Retorna el resultado
   del comando SMTP "QUIT".

Los métodos de bajo nivel correspondientes a los comandos estándar
SMTP/ESMTP "`HELP", "RSET", "NOOP", "MAIL", "RCPT", y "DATA" también
están soportados. Normalmente, no es necesario llamarlos directamente,
por lo que no se documentan aquí. Para más detalles, consulte el
código del módulo.

Additionally, an SMTP instance has the following attributes:

SMTP.helo_resp

   The response to the "HELO" command, see "helo()".

SMTP.ehlo_resp

   The response to the "EHLO" command, see "ehlo()".

SMTP.does_esmtp

   A boolean value indicating whether the server supports ESMTP, see
   "ehlo()".

SMTP.esmtp_features

   A dictionary of the names of SMTP service extensions supported by
   the server, see "ehlo()".

## Ejemplo SMTP

This example prompts the user for addresses needed in the message
envelope ('To' and 'From' addresses), and the message to be delivered.
Note that the headers to be included with the message must be included
in the message as entered; this example doesn't do any processing of
the **RFC 822** headers.  In particular, the 'To' and 'From' addresses
must be included in the message headers explicitly:

   import smtplib

   def prompt(title):
       return input(title).strip()

   from_addr = prompt("From: ")
   to_addrs  = prompt("To: ").split()
   print("Enter message, end with ^D (Unix) or ^Z (Windows):")

   # Add the From: and To: headers at the start!
   lines = [f"From: {from_addr}", f"To: {', '.join(to_addrs)}", ""]
   while True:
       try:
           line = input()
       except EOFError:
           break
       else:
           lines.append(line)

   msg = "\r\n".join(lines)
   print("Message length is", len(msg))

   server = smtplib.SMTP("localhost")
   server.set_debuglevel(1)
   server.sendmail(from_addr, to_addrs, msg)
   server.quit()

Nota:

  En general, querrá usar las características del paquete "email" para
  construir un mensaje de correo electrónico, que luego puede enviar a
  través de "send_message()"; ver email: Ejemplos.
