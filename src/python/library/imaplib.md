---
title: '"imaplib" --- IMAP4 protocol client'
source_url: https://docs.python.org/es/3
source_path: library/imaplib.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2920
---

# "imaplib" --- IMAP4 protocol client

**Código fuente:** Lib/imaplib.py

======================================================================

This module defines three classes, "IMAP4", "IMAP4_SSL" and
"IMAP4_stream", which encapsulate a connection to an IMAP4 server and
implement a large subset of the IMAP4rev1 client protocol as defined
in **RFC 3501**. It is backward compatible with IMAP4 (**RFC 1730**)
servers, but note that the "STATUS" command is not supported in IMAP4.

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

Three classes are provided by the "imaplib" module, "IMAP4" is the
base class:

class imaplib.IMAP4(host='', port=IMAP4_PORT, timeout=None)

   This class implements the actual IMAP4 protocol.  The connection is
   created and protocol version (IMAP4 or IMAP4rev1) is determined
   when the instance is initialized. If *host* is not specified, "''"
   (the local host) is used. If *port* is omitted, the standard IMAP4
   port (143) is used. The optional *timeout* parameter specifies a
   timeout in seconds for the connection attempt. If timeout is not
   given or is "None", the global default socket timeout is used.

   La clase "IMAP4" soporta la sentencia "with". Cuando se usa de esta
   manera, el comando IMAP4 "LOGOUT" se emite automáticamente cuando
   se cierra la declaración "with". P.ej.:

      >>> from imaplib import IMAP4
      >>> with IMAP4("domain.org") as M:
      ...     M.noop()
      ...
      ('OK', [b'Nothing Accomplished. d25if65hy903weo.87'])

   Distinto en la versión 3.5: Se agregó soporte para la sentencia
   "with".

   Distinto en la versión 3.9: El parámetro opcional *timeout* fue
   agregado.

Se definen tres excepciones como atributos de la clase "IMAP4":

exception IMAP4.error

   Excepción lanzada por cualquier error. El motivo de la excepción se
   pasa al constructor como una cadena de caracteres.

exception IMAP4.abort

   Los errores del servidor IMAP4 causan que esta excepción sea
   lanzada. Esta es una subclase de "IMAP4.error". Tenga en cuenta que
   cerrar la instancia e instanciar una nueva generalmente permitirá
   la recuperación de esta excepción.

exception IMAP4.readonly

   Esta excepción es lanzada cuando el servidor cambia el estado de un
   buzón de correo de escritura. Esta es una subclase de
   "IMAP4.error". Algún otro cliente ahora tiene permiso de escritura
   y será necesario volver a abrir el buzón para volver a obtener el
   permiso de escritura.

También hay una subclase para conexiones seguras:

class imaplib.IMAP4_SSL(host='', port=IMAP4_SSL_PORT, *, ssl_context=None, timeout=None)

   Esta es una subclase derivada de "IMAP4" que se conecta a través de
   un socket cifrado SSL (para usar esta clase necesita un módulo de
   socket que se compiló con soporte SSL). Si no se especifica *host*,
   se usa "''" (el host local). Si se omite *port*, se usa el puerto
   IMAP4 estándar sobre SSL (993). *ssl_context* es un objeto
   "ssl.SSLContext" que permite agrupar opciones de configuración SSL,
   certificados y claves privadas en una estructura única
   (potencialmente de larga duración). Leer Consideraciones de
   seguridad para conocer las mejores prácticas.

   Nota:

     With the default *ssl_context*, the connection is encrypted but
     the server certificate and hostname are not verified. To verify
     them, pass a context created by "ssl.create_default_context()".

   The optional *timeout* parameter specifies a timeout in seconds for
   the connection attempt. If timeout is not given or is "None", the
   global default socket timeout is used.

   Distinto en la versión 3.3: El parámetro *ssl_context* fue
   agregado.

   Distinto en la versión 3.4: La clase ahora admite la verificación
   del nombre de host con "ssl.SSLContext.check_hostname" y *Server
   Name Indication* (ver "ssl.HAS_SNI").

   Distinto en la versión 3.9: El parámetro opcional *timeout* fue
   agregado.

   Distinto en la versión 3.12: Se han eliminado los parámetros
   obsoletos *keyfile* y *certfile*.

La segunda subclase permite conexiones creadas por un proceso hijo:

class imaplib.IMAP4_stream(command)

   Esta es una subclase derivada de "IMAP4" que se conecta a los
   descriptores de archivo "stdin/stdout" creados al pasar *command* a
   "subprocess.Popen ()".

Se definen las siguientes funciones de utilidad:

imaplib.Internaldate2tuple(resp)

   Parse a *bytes-like object* containing an IMAP4 "INTERNALDATE"
   response and return the corresponding local time.  The return value
   is a "time.struct_time" tuple or "None" if the input has wrong
   format.

imaplib.Int2AP(num)

   Convierte un número entero en una representación de bytes
   utilizando caracteres del conjunto ["A" .. "P"].

imaplib.ParseFlags(resp)

   Converts a *bytes-like object* containing an IMAP4 "FLAGS" response
   to a tuple of individual flags as "bytes".  The return value is an
   empty tuple if the input has wrong format.

imaplib.Time2Internaldate(date_time)

   Convierte *date_time* en una representación IMAP4 "INTERNALDATE".
   El valor de retorno es una cadena de caracteres en la forma: ""DD-
   Mmm-YYYY HH:MM:SS +HHMM"" (incluyendo comillas dobles). El
   argumento *date_time* puede ser un número (int o float) que
   representa segundos en un espacio de tiempo (como lo retorna
   "time.time()"), una tupla de 9 que representa la hora local como
   una instancia de "time.struct_time" (según lo retornado por
   "time.localtime()"), una instancia actualizada de
   "datetime.datetime", o una cadena de caracteres entre comillas
   dobles. En el último caso, se supone que ya está en el formato
   correcto.

Tenga en cuenta que los números de mensaje IMAP4 cambian a medida que
cambia el buzón de correo; en particular, después de que un comando
"EXPUNGE" realiza eliminaciones, los mensajes restantes se vuelven a
numerar. Por lo tanto, es muy recomendable usar UIDs en su lugar, con
el comando UID.

Al final del módulo, hay una sección de prueba que contiene un ejemplo
más extenso de uso.

Ver también:

  Documentos describiendo el protocolo, y fuentes de servidores que lo
  implementan, del Centro de Información IMAP de la Universidad de
  Washington, pueden ser encontrados en (**Código Fuente**)
  https://github.com/uw-imap/imap (**Fuera de mantención**).

## Objetos de IMAP4

Todos los comandos IMAP4rev1 están representados por métodos del mismo
nombre, ya sea en mayúsculas o minúsculas.

All arguments to commands are converted to strings, except for
"AUTHENTICATE", and the last argument to "APPEND" which is passed as
an IMAP4 literal.  If necessary (the string contains IMAP4 protocol-
sensitive characters and isn't enclosed with either parentheses or
double quotes) each string is quoted. However, the *password* argument
to the "LOGIN" command is always quoted. If you want to avoid having
an argument string quoted (eg: the *flags* argument to "STORE") then
enclose the string in parentheses (eg: "r'(\Deleted)'"). In general,
pass arguments unquoted and let the module quote them as needed. An
argument that is already enclosed in double quotes is left unchanged,
so that code which quotes arguments itself keeps working.

Most commands return a tuple: "(type, [data, ...])" where *type* is
usually "'OK'" or "'NO'", and *data* is either the text from the
command response, or mandated results from the command. Each *data* is
either a "bytes", or a tuple. If a tuple, then the first part is the
header of the response, and the second part contains the data (ie:
'literal' value).

Las opciones *message_set* de los siguientes comandos son una cadena
de caracteres que especifica uno o más mensajes sobre los que se debe
actuar. Puede ser un número de mensaje simple ("'1'"), un rango de
números de mensaje ("'2:4'") o un grupo de rangos no contiguos
separados por comas ("'1:3,6:9'"). Un rango puede contener un
asterisco para indicar un límite superior infinito ("'3:*'").

Una instancia de "IMAP4" tiene los siguientes métodos:

IMAP4.append(mailbox, flags, date_time, message)

   Agregar *mensaje* al buzón de correo con nombre.

   *flags* may be "None" or a string of IMAP flag tokens.  Multiple
   flags are separated by spaces, for example "r'\Seen \Answered'". If
   *flags* is not already enclosed in parentheses, parentheses are
   added automatically.

IMAP4.authenticate(mechanism, authobject)

   Autenticar comando --- requiere procesamiento de respuesta.

   *mechanism* especifica qué mecanismo de autenticación se utilizará;
   debe aparecer en la variable de instancia "capabilities" en la
   forma "AUTH=mechanism".

   *authobject* debe ser un objeto invocable:

      data = authobject(response)

   Se llamará para procesar las respuestas de continuación del
   servidor; el argumento *response* que se pasa será "bytes". Debería
   retornar "bytes" *data* que se codificarán en base64 y se enviarán
   al servidor. Debería retornar "None" si la respuesta de cancelación
   de cliente "*" se debe enviar en su lugar.

   Distinto en la versión 3.5: los nombres de usuario y las
   contraseñas de cadena de caracteres ahora están codificados para
   "utf-8" en lugar de limitarse a ASCII.

IMAP4.check()

   Control del buzón de correo en el servidor.

IMAP4.close()

   Cerrar el buzón de correo seleccionado actualmente. Los mensajes
   eliminados se eliminan del buzón de correo de escritura. Este es el
   comando recomendado antes de "LOGOUT".

IMAP4.copy(message_set, new_mailbox)

   Copia mensajes *message_set* al final de *new_mailbox*.

IMAP4.create(mailbox)

   Crea un nuevo buzón de correo llamado *mailbox*.

IMAP4.delete(mailbox)

   Elimina el buzón de correo antiguo llamado *mailbox*.

IMAP4.deleteacl(mailbox, who)

   Elimina las ACLs (elimina cualquier derecho) establecidas para
   quién en el buzón de correo.

IMAP4.enable(capability)

   Habilita *capability* (ver **RFC 5161**). La mayoría de las
   capacidades no necesitan estar habilitadas. Actualmente solo esta
   soportada la capacidad "UTF8=ACCEPT" (consulte **RFC 6855**).

   Added in version 3.5: El método "enable()" en sí, y soporte **RFC
   6855**.

IMAP4.expunge()

   Elimina permanentemente los elementos eliminados del buzón de
   correo seleccionado. Genera una respuesta "EXPUNGE" para cada
   mensaje eliminado. Los datos retornados contienen una lista de
   números de mensaje "EXPUNGE" en el orden recibido.

IMAP4.fetch(message_set, message_parts)

   Obtiene (partes de) mensajes. *message_parts* debe ser una cadena
   de nombres de partes de mensajes encerrados entre paréntesis, por
   ejemplo: ""(UID BODY[TEXT])"". Los datos retornados son una tupla
   de mensaje parte sobre y datos.

IMAP4.getacl(mailbox)

   Obtiene la "ACL"s para *mailbox*. El método no es estándar, pero es
   compatible con el servidor "Cyrus".

IMAP4.getannotation(mailbox, entry, attribute)

   Recupera la "ANNOTATION"s especificada para *mailbox*. El método no
   es estándar, pero es compatible con el servidor "Cyrus".

IMAP4.getquota(root)

   Obtiene el uso y los límites de los recursos de la "quota" de
   *root*. Este método es parte de la extensión IMAP4 QUOTA definida
   en rfc2087.

IMAP4.getquotaroot(mailbox)

   Obtiene la lista de "quota" "roots" para el nombrado *mailbox*.
   Este método es parte de la extensión IMAP4 QUOTA definida en
   rfc2087.

IMAP4.idle(duration=None)

   Return an "Idler": an iterable context manager implementing the
   IMAP4 "IDLE" command as defined in **RFC 2177**.

   The returned object sends the "IDLE" command when activated by the
   "with" statement, produces IMAP untagged responses via the
   *iterator* protocol, and sends "DONE" upon context exit.

   All untagged responses that arrive after sending the "IDLE" command
   (including any that arrive before the server acknowledges the
   command) will be available via iteration. Any leftover responses
   (those not iterated in the "with" context) can be retrieved in the
   usual way after "IDLE" ends, using "IMAP4.response()".

   Responses are represented as "(type, [data, ...])" tuples, as
   described in IMAP4 Objects.

   The *duration* argument sets a maximum duration (in seconds) to
   keep idling, after which any ongoing iteration will stop. It can be
   an "int" or "float", or "None" for no time limit. Callers wishing
   to avoid inactivity timeouts on servers that impose them should
   keep this at most 29 minutes (1740 seconds). Requires a socket
   connection; *duration* must be "None" on "IMAP4_stream"
   connections.

      >>> with M.idle(duration=29 * 60) as idler:
      ...     for typ, data in idler:
      ...         print(typ, data)
      ...
      EXISTS [b'1']
      RECENT [b'1']

   Idler.burst(interval=0.1)

      Yield a burst of responses no more than *interval* seconds apart
      (expressed as an "int" or "float").

      This *generator* is an alternative to iterating one response at
      a time, intended to aid in efficient batch processing. It
      retrieves the next response along with any immediately available
      subsequent responses. (For example, a rapid series of "EXPUNGE"
      responses after a bulk delete.)

      Requires a socket connection; does not work on "IMAP4_stream"
      connections.

         >>> with M.idle() as idler:
         ...     # get a response and any others following by < 0.1 seconds
         ...     batch = list(idler.burst())
         ...     print(f'processing {len(batch)} responses...')
         ...     print(batch)
         ...
         processing 3 responses...
         [('EXPUNGE', [b'2']), ('EXPUNGE', [b'1']), ('RECENT', [b'0'])]

      Truco:

        The "IDLE" context's maximum duration, as passed to
        "IMAP4.idle()", is respected when waiting for the first
        response in a burst. Therefore, an expired "Idler" will cause
        this generator to return immediately without producing
        anything. Callers should consider this if using it in a loop.

   Nota:

     The iterator returned by "IMAP4.idle()" is usable only within a
     "with" statement. Before or after that context, unsolicited
     responses are collected internally whenever a command finishes,
     and can be retrieved with "IMAP4.response()".

   Nota:

     The "Idler" class name and structure are internal interfaces,
     subject to change. Calling code can rely on its context
     management, iteration, and public method to remain stable, but
     should not subclass, instantiate, compare, or otherwise directly
     reference the class.

   Added in version 3.14.

IMAP4.list(directory='', pattern='*')

   Lista los nombres de buzones de correo en *directory* coincidiendo
   *pattern*. *directory* por defecto es la carpeta de correo de nivel
   superior, y *pattern* por defecto coincide con cualquier cosa. Los
   datos retornados contienen una lista de respuestas "LIST".

IMAP4.login(user, password)

   Identifica al cliente con una contraseña de texto sin formato. El
   *password* será citado.

IMAP4.login_cram_md5(user, password)

   Fuerza el uso de la autenticación "CRAM-MD5" al identificar al
   cliente para proteger la contraseña. Solo funcionará si la
   respuesta "CAPABILITY" del servidor incluye la frase "AUTH=CRAM-
   MD5".

   Distinto en la versión 3.14: An "IMAP4.error" is raised if MD5
   support is not available.

IMAP4.logout()

   Cierra la conexión al servidor. Retorna la respuesta "BYE" desde el
   servidor .

   Distinto en la versión 3.8: El método ya no ignora las excepciones
   silenciosamente arbitrarias.

IMAP4.lsub(directory='', pattern='*')

   Lista los nombres de buzones de correos suscritos en el patrón de
   coincidencia del directorio *directory* por defecto para el
   directorio de nivel superior y *pattern* por defecto para que
   coincida con cualquier buzón de correo. Los datos retornados son
   una tupla de mensaje parte sobre y datos.

IMAP4.myrights(mailbox)

   Muestra mis ACLs para un buzón de correo (es decir, los derechos
   que tengo sobre el buzón de correo).

IMAP4.namespace()

   Retorna espacios de nombres IMAP como se define en **RFC 2342**.

IMAP4.noop()

   Envía "NOOP" al servidor.

IMAP4.open(host, port, timeout=None)

   Opens socket to *port* at *host*. The optional *timeout* parameter
   specifies a timeout in seconds for the connection attempt. If
   timeout is not given or is "None", the global default socket
   timeout is used. Also note that if the *timeout* parameter is set
   to be zero, it will raise a "ValueError" to reject creating a non-
   blocking socket. This method is implicitly called by the "IMAP4"
   constructor. The connection objects established by this method will
   be used in the "IMAP4.read()", "IMAP4.readline()", "IMAP4.send()",
   and "IMAP4.shutdown()" methods. You may override this method.

   Genera un evento de auditoría "imaplib.open" con argumentos "self",
   "host", "port".

   Distinto en la versión 3.9: El parámetro *timeout* fue agregado.

IMAP4.partial(message_num, message_part, start, length)

   Obtiene partes truncadas de un mensaje. Los datos retornados son
   una tupla de mensaje parte sobre y datos.

IMAP4.proxyauth(user)

   Asume la autenticación como *user*. Permite a un administrador
   autorizado hacer un proxy en el buzón de correo de cualquier
   usuario.

IMAP4.read(size)

   Lee *size* bytes del servidor remoto. Podemos sobrescribir este
   método.

IMAP4.readline()

   Lee una línea del servidor remoto. Podemos sobrescribir este
   método.

IMAP4.recent()

   Solicita al servidor una actualización. Los datos retornados son
   "None" si no hay mensajes nuevos, de lo contrario el valor de
   respuesta es "RECENT".

IMAP4.rename(oldmailbox, newmailbox)

   Cambia el nombre del buzón de correo llamado *oldmailbox* a
   *newmailbox*.

IMAP4.response(code)

   Retorna los datos para la respuesta *code* si se recibió, o "None".
   Retorna el código dado, en lugar del tipo habitual.

IMAP4.search(charset, criterion[, ...])

   Busca en el buzón de correo mensajes coincidentes. El *charset*
   puede ser "None", en cuyo caso no se especificará "CHARSET" en la
   solicitud al servidor. El protocolo IMAP requiere que se
   especifique al menos un criterio; se lanzará una excepción cuando
   el servidor retorne un error. *charset* debe ser "None" si la
   capacidad "UTF8=ACCEPT" se habilitó utilizando el comando
   "enable()".

   Ejemplo:

      # M is a connected IMAP4 instance...
      typ, msgnums = M.search(None, 'FROM', '"LDJ"')

      # or:
      typ, msgnums = M.search(None, '(FROM "LDJ")')

IMAP4.select(mailbox='INBOX', readonly=False)

   Seleccione un buzón de correo. Los datos retornados son el recuento
   de mensajes en *mailbox* (respuesta "EXISTS"). El *mailbox*
   predeterminado es "'INBOX'". Si se establece el indicador
   *readonly*, no se permiten modificaciones en el buzón de correo.

IMAP4.send(data)

   Envía "data" al servidor remoto. Podemos sobrescribir este método.

   Lanza un evento de auditoría "imaplib.send" con argumentos "self",
   "data".

IMAP4.setacl(mailbox, who, what)

   Establece una "ACL" para *mailbox*. El método no es estándar, pero
   es compatible con el servidor "Cyrus".

IMAP4.setannotation(mailbox, entry, attribute[, ...])

   Establece "ANNOTATION"s para *mailbox*. El método no es estándar,
   pero es compatible con el servidor "Cyrus".

IMAP4.setquota(root, limits)

   Establece los recursos *limits* de la "quota" de los *root*. Este
   método es parte de la extensión IMAP4 QUOTA definida en rfc2087.

IMAP4.shutdown()

   Cierra la conexión establecida en "open". Este método es llamado
   implícitamente por "IMAP4.logout()". Podemos sobrescribir este
   método.

IMAP4.socket()

   Retorna la instancia de socket utilizada para conectarse al
   servidor.

IMAP4.sort(sort_criteria, charset, search_criterion[, ...])

   El comando "sort" es una variante de "search" con semántica de
   clasificación para los resultados. Los datos retornados contienen
   una lista separada por espacios de números de mensajes
   coincidentes.

   *Sort* tiene dos argumentos antes del argumento (s)
   *search_criterion*; una lista entre paréntesis de *sort_criteria*,
   y la búsqueda del *charset*. Tenga en cuenta que, a diferencia de
   "search", el argumento de búsqueda *charset* es obligatorio.
   También hay un comando "uid sort" que corresponde a "sort" de la
   misma manera que "uid search" corresponde a "search". El comando
   "sort" primero busca en el buzón de correo mensajes que coincidan
   con los criterios de búsqueda dados utilizando el argumento
   *charset* para la interpretación de cadenas de caracteres en los
   criterios de búsqueda. Luego retorna los números de mensajes
   coincidentes.

   Este es un comando de extensión "IMAP4rev1".

IMAP4.starttls(ssl_context=None)

   Envía un comando "STARTTLS". El argumento *ssl_context* es opcional
   y debe ser un objeto "ssl.SSLContext". Esto habilitará el cifrado
   en la conexión IMAP. Leer Consideraciones de seguridad para conocer
   las mejores prácticas.

   Nota:

     With the default *ssl_context*, the connection is encrypted but
     the server certificate and hostname are not verified. To verify
     them, pass a context created by "ssl.create_default_context()".

   Added in version 3.2.

   Distinto en la versión 3.4: El método ahora admite la verificación
   del nombre de host con "ssl.SSLContext.check_hostname" y *Server
   Name Indication* (ver "ssl.HAS_SNI").

IMAP4.status(mailbox, names)

   Solicita condiciones de estado con nombre para *mailbox*.

IMAP4.store(message_set, command, flag_list)

   Alters flag dispositions for messages in mailbox.  *command* is
   specified by section 6.4.6 of **RFC 3501** as being one of "FLAGS",
   "+FLAGS", or "-FLAGS", optionally with a suffix of ".SILENT".

   Por ejemplo, para establecer el indicador de eliminación en todos
   los mensajes:

      typ, data = M.search(None, 'ALL')
      for num in data[0].split():
         M.store(num, '+FLAGS', '\\Deleted')
      M.expunge()

   Nota:

     Creating flags containing ']' (for example: "[test]") violates
     **RFC 3501** (the IMAP protocol).  However, imaplib has
     historically allowed creation of such flags, and popular IMAP
     servers, such as Gmail, accept and produce such flags.  There are
     non-Python programs which also create such flags.  Although it is
     an RFC violation and IMAP clients and servers are supposed to be
     strict, imaplib still continues to allow such flags to be created
     for backward compatibility reasons, and as of Python 3.6, handles
     them if they are sent from the server, since this improves real-
     world compatibility.

IMAP4.subscribe(mailbox)

   Suscribe al nuevo buzón de correo.

IMAP4.thread(threading_algorithm, charset, search_criterion[, ...])

   El comando "thread" es una variante de "search" con semántica de
   hilos para los resultados. Los datos retornados contienen una lista
   de miembros de hilos separados por espacios.

   Los miembros de del hilo (*thread*) consisten en cero o más números
   de mensajes, delimitados por espacios, que indican sucesivos padres
   e hijos.

   *Thread* tiene dos argumentos antes del argumento(s)
   *search_criterion*; un *threading_algorithm*, y la búsqueda del
   *charset*. Tenga en cuenta que, a diferencia de "search", el
   argumento de búsqueda *charset* es obligatorio. También hay un
   comando "uid thread" que corresponde a "thread" de la misma manera
   que "uid search" corresponde a "search". El comando "thread"
   primero busca en el buzón de correo mensajes que coincidan con los
   criterios de búsqueda dados utilizando el argumento *charset* para
   la interpretación de cadenas de caracteres en los criterios de
   búsqueda. Luego retorna los mensajes coincidentes enfilados según
   el algoritmo de subproceso especificado.

   Este es un comando de extensión "IMAP4rev1".

IMAP4.uid(command, arg[, ...])

   Ejecuta argumentos de comando con mensajes identificados por UID,
   en lugar de número de mensaje. Retorna la respuesta apropiada al
   comando. Se debe proporcionar al menos un argumento; Si no se
   proporciona ninguno, el servidor retornará un error y se lanzará
   una excepción.

IMAP4.unsubscribe(mailbox)

   Darse de baja del antiguo buzón de correo.

IMAP4.unselect()

   "imaplib.IMAP4.unselect()" libera recursos del servidor asociados
   al buzón de correo seleccionado y devuelve el servidor al estado
   autenticado. Este comando realiza las mismas acciones que
   "imaplib.IMAP4.close()", con la excepción de que ningún mensaje es
   permanentemente borrado del buzón de correo actualmente
   seleccionado.

   Added in version 3.9.

IMAP4.xatom(name[, ...])

   Permite comandos de extensión simples notificados por el servidor
   en la respuesta "CAPABILITY".

Los siguientes atributos se definen en instancias de "IMAP4":

IMAP4.PROTOCOL_VERSION

   El protocolo mas recientemente admitido en la respuesta
   "CAPABILITY" desde el servidor.

IMAP4.debug

   Valor entero para controlar la salida de depuración. El valor de
   inicialización se toma de la variable del módulo "Debug". Valores
   mayores de tres rastrean cada comando.

IMAP4.utf8_enabled

   Valor booleano que normalmente es "False", pero se establece en
   "True" si un comando "enable()" es exitosamente emitido para la
   capacidad "UTF8=ACCEPT".

   Added in version 3.5.

## Ejemplo IMAP4

Aquí hay un ejemplo mínimo (sin verificación de errores) que abre un
buzón de correo y recupera e imprime todos los mensajes:

   import getpass, imaplib

   M = imaplib.IMAP4(host='example.org')
   M.login(getpass.getuser(), getpass.getpass())
   M.select()
   typ, data = M.search(None, 'ALL')
   for num in data[0].split():
       typ, data = M.fetch(num, '(RFC822)')
       print('Message %s\n%s\n' % (num, data[0][1]))
   M.close()
   M.logout()

Nota:

  A "FETCH" response may contain additional or unsolicited data (see
  **RFC 3501**, section 7.4.2), so production code should inspect the
  whole response rather than rely on "data[0][1]".
