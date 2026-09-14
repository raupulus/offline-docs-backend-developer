---
title: '"ftplib" --- FTP protocol client'
source_url: https://docs.python.org/es/3
source_path: library/ftplib.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2670
---

# "ftplib" --- FTP protocol client

**Código fuente** Lib/ftplib.py

======================================================================

Este módulo define la clase "FTP" y algunos elementos relacionados. La
clase "FTP" implementa el lado cliente del protocolo FTP. Puede usar
esto para escribir programas de Python que realicen una variedad de
trabajos FTP automatizados, como duplicar otros servidores FTP.
También es utilizado por el módulo "urllib.request" para manejar URL
que usan FTP. Para más información sobre FTP (File Transfer Protocol),
ver internet **RFC 959**.

La codificación predeterminada es UTF-8, siguiendo **RFC 2640**.

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

Here's a sample session using the "ftplib" module:

   >>> from ftplib import FTP
   >>> ftp = FTP('ftp.us.debian.org')  # connect to host, default port
   >>> ftp.login()                     # user anonymous, passwd anonymous@
   '230 Login successful.'
   >>> ftp.cwd('debian')               # change into "debian" directory
   '250 Directory successfully changed.'
   >>> ftp.retrlines('LIST')           # list directory contents
   -rw-rw-r--    1 1176     1176         1063 Jun 15 10:18 README
   ...
   drwxr-sr-x    5 1176     1176         4096 Dec 19  2000 pool
   drwxr-sr-x    4 1176     1176         4096 Nov 17  2008 project
   drwxr-xr-x    3 1176     1176         4096 Oct 10  2012 tools
   '226 Directory send OK.'
   >>> with open('README', 'wb') as fp:
   >>>     ftp.retrbinary('RETR README', fp.write)
   '226 Transfer complete.'
   >>> ftp.quit()
   '221 Goodbye.'

## Reference

### FTP objects

class ftplib.FTP(host='', user='', passwd='', acct='', timeout=None, source_address=None, *, encoding='utf-8')

   Return a new instance of the "FTP" class.

   Parámetros:
      * **host** (*str*) -- The hostname to connect to. If given,
        "connect(host)" is implicitly called by the constructor.

      * **user** (*str*) -- The username to log in with (default:
        "'anonymous'"). If given, "login(host, passwd, acct)" is
        implicitly called by the constructor.

      * **passwd** (*str*) -- The password to use when logging in. If
        not given, and if *passwd* is the empty string or ""-"", a
        password will be automatically generated.

      * **acct** (*str*) -- Account information to be used for the
        "ACCT" FTP command. Few systems implement this. See RFC-959
        for more details.

      * **timeout** (*float** | **None*) -- A timeout in seconds for
        blocking operations like "connect()" (default: the global
        default timeout setting).

      * **source_address** (*tuple** | **None*) -- A 2-tuple "(host,
        port)" for the socket to bind to as its source address before
        connecting.

      * **encoding** (*str*) -- The encoding for directories and
        filenames (default: "'utf-8'").

   La clase "FTP" admite la instrucción "with", por ejemplo:

   >>> from ftplib import FTP
   >>> with FTP("ftp1.at.proftpd.org") as ftp:
   ...     ftp.login()
   ...     ftp.dir()
   ...
   '230 Anonymous login ok, restrictions apply.'
   dr-xr-xr-x   9 ftp      ftp           154 May  6 10:43 .
   dr-xr-xr-x   9 ftp      ftp           154 May  6 10:43 ..
   dr-xr-xr-x   5 ftp      ftp          4096 May  6 10:43 CentOS
   dr-xr-xr-x   3 ftp      ftp            18 Jul 10  2008 Fedora
   >>>

   Distinto en la versión 3.2: Se agregó compatibilidad con la
   instrucción "with".

   Distinto en la versión 3.3: Se agregó el parámetro
   *source_address*.

   Distinto en la versión 3.9: Si el parámetro *timeout* se establece
   en cero, lanzará un "ValueError" para evitar la creación de un
   socket sin bloqueo. Se agregó el parámetro *encoding*, y el valor
   predeterminado se cambió de Latin-1 a UTF-8 para seguir **RFC
   2640**.

   Several "FTP" methods are available in two flavors: one for
   handling text files and another for binary files. The methods are
   named for the command which is used followed by "lines" for the
   text version or "binary" for the binary version.

   Las instancias de "FTP" tienen los siguientes métodos:

   set_debuglevel(level)

      Set the instance's debugging level as an "int". This controls
      the amount of debugging output printed. The debug levels are:

      * "0" (default): No debug output.

      * "1": Produce a moderate amount of debug output, generally a
        single line per request.

      * "2" or higher: Produce the maximum amount of debugging output,
        logging each line sent and received on the control connection.

   connect(host='', port=0, timeout=None, source_address=None)

      Connect to the given host and port. This function should be
      called only once for each instance; it should not be called if a
      *host* argument was given when the "FTP" instance was created.
      All other "FTP" methods can only be called after a connection
      has successfully been made.

      Parámetros:
         * **host** (*str*) -- The host to connect to.

         * **port** (*int*) -- The TCP port to connect to (default:
           "21", as specified by the FTP protocol specification). It
           is rarely needed to specify a different port number.

         * **timeout** (*float** | **None*) -- A timeout in seconds
           for the connection attempt (default: the global default
           timeout setting).

         * **source_address** (*tuple** | **None*) -- A 2-tuple
           "(host, port)" for the socket to bind to as its source
           address before connecting.

      Lanza un evento auditor "ftplib.connect" con los argumentos
      "self", "host", "port".

      Distinto en la versión 3.3: Se agregó el parámetro
      *source_address*.

   getwelcome()

      Retornar el mensaje de bienvenida enviado por el servidor como
      respuesta a la conexión inicial. (Este mensaje a veces contiene
      renuncias de responsabilidad o información de ayuda que puede
      ser relevante para el usuario.)

   login(user='anonymous', passwd='', acct='')

      Log on to the connected FTP server. This function should be
      called only once for each instance, after a connection has been
      established; it should not be called if the *host* and *user*
      arguments were given when the "FTP" instance was created. Most
      FTP commands are only allowed after the client has logged in.

      Parámetros:
         * **user** (*str*) -- The username to log in with (default:
           "'anonymous'").

         * **passwd** (*str*) -- The password to use when logging in.
           If not given, and if *passwd* is the empty string or ""-"",
           a password will be automatically generated.

         * **acct** (*str*) -- Account information to be used for the
           "ACCT" FTP command. Few systems implement this. See RFC-959
           for more details.

   abort()

      Anula una transferencia de archivo que está en progreso. Usarlo
      no siempre funciona, pero vale la pena intentarlo.

   sendcmd(cmd)

      Envía una cadena de comando simple al servidor y retorna la
      cadena de caracteres de respuesta.

      Genera un evento auditor "ftplib.sendcmd" con los argumentos
      "self", "cmd".

   voidcmd(cmd)

      Send a simple command string to the server and handle the
      response.  Return the response string if the response code
      corresponds to success (codes in the range 200--299).  Raise
      "error_reply" otherwise.

      Genera un evento auditor "ftplib.sendcmd" con los argumentos
      "self", "cmd".

   retrbinary(cmd, callback, blocksize=8192, rest=None)

      Retrieve a file in binary transfer mode.

      Parámetros:
         * **cmd** (*str*) -- An appropriate "RETR" command: ""RETR
           *filename*"".

         * **callback** (*callable*) -- A single parameter callable
           that is called for each block of data received, with its
           single argument being the data as "bytes".

         * **blocksize** (*int*) -- The maximum chunk size to read on
           the low-level "socket" object created to do the actual
           transfer. This also corresponds to the largest size of data
           that will be passed to *callback*. Defaults to "8192".

         * **rest** (*int*) -- A "REST" command to be sent to the
           server. See the documentation for the *rest* parameter of
           the "transfercmd()" method.

   retrlines(cmd, callback=None)

      Retrieve a file or directory listing in the encoding specified
      by the *encoding* parameter at initialization. *cmd* should be
      an appropriate "RETR" command (see "retrbinary()") or a command
      such as "LIST" or "NLST" (usually just the string "'LIST'").
      "LIST" retrieves a list of files and information about those
      files. "NLST" retrieves a list of file names. The *callback*
      function is called for each line with a string argument
      containing the line with the trailing CRLF stripped.  The
      default *callback* prints the line to "sys.stdout".

   set_pasv(val)

      Habilita el modo pasivo si *val* es verdadero, de lo contrario
      lo inhabilita. El modo pasivo es el valor predeterminado.

   storbinary(cmd, fp, blocksize=8192, callback=None, rest=None)

      Store a file in binary transfer mode.

      Parámetros:
         * **cmd** (*str*) -- An appropriate "STOR" command: ""STOR
           *filename*"".

         * **fp** (*file object*) -- A file object (opened in binary
           mode) which is read until EOF, using its "read()" method in
           blocks of size *blocksize* to provide the data to be
           stored.

         * **blocksize** (*int*) -- The read block size. Defaults to
           "8192".

         * **callback** (*callable*) -- A single parameter callable
           that is called for each block of data sent, with its single
           argument being the data as "bytes".

         * **rest** (*int*) -- A "REST" command to be sent to the
           server. See the documentation for the *rest* parameter of
           the "transfercmd()" method.

      Distinto en la versión 3.2: The *rest* parameter was added.

   storlines(cmd, fp, callback=None)

      Almacena un archivo en modo de línea. *cmd* debe ser un comando
      "STOR" apropiado (ver "storbinary()"). Las líneas se leen hasta
      EOF del *file object* *fp* (abierto en modo binario) usando su
      método "readline()" para proporcionar los datos que se
      almacenarán. *callback* es un parámetro único opcional que se
      puede llamar en cada línea después de su envío.

   transfercmd(cmd, rest=None)

      Inicia una transferencia sobre la conexión de datos.  Si la
      transferencia es activa, envía un comando "EPRT" o  "PORT" y el
      comando de transferencia especificado por *cmd*, y acepta la
      conexión. Si el servidor es pasivo, envía un comando "EPSV" o
      "PASV", lo conecta, e inicia el comando de transferencia. De
      cualquier manera, retorna el socket para la conexión.

      Si se proporciona *rest* opcional, se envía un comando "REST" al
      servidor, pasando *rest* como argumento. *rest* suele ser un
      desplazamiento de bytes en el archivo solicitado, que le indica
      al servidor que reinicie el envío de los bytes del archivo en el
      desplazamiento solicitado, omitiendo los bytes iniciales. Sin
      embargo, tenga en cuenta que el método "transfercmd()" convierte
      *rest* en una cadena de caracteres con el parámetro *encoding*
      especificado en la inicialización, pero no se realiza ninguna
      comprobación del contenido de la cadena de caracteres. Si el
      servidor no reconoce el comando "REST", se lanzará una excepción
      "error_reply". Si esto sucede, simplemente llame a
      "transfercmd()" sin un argumento *rest*.

   ntransfercmd(cmd, rest=None)

      Como "transfercmd()", pero retorna una tupla de conexión de
      datos y el tamaño esperado de los datos. Si el tamaño esperado
      no se pudo computar, retornará "None" como tal. *cmd* y *rest*
      significan lo mismo que en "transfercmd()".

   mlsd(path='', facts=[])

      Enumera un directorio en un formato estandarizado usando el
      comando "MLSD" (**RFC 3659**). Si se omite *path*, se asume el
      directorio actual. *facts* es una lista de cadenas de caracteres
      que representan el tipo de información deseada (por ejemplo,
      "["type", "size", "perm"]"). Retorna un objeto generador que
      produce una tupla de dos elementos por cada archivo encontrado
      en la ruta. El primer elemento es el nombre del archivo, el
      segundo es un diccionario que contiene datos sobre el nombre del
      archivo. El contenido de este diccionario puede estar limitado
      por el argumento *facts*, pero no se garantiza que el servidor
      retorne todos los datos solicitados.

      Added in version 3.3.

   nlst(argument[, ...])

      Retorna una lista de nombres de archivos tal como los retorna el
      comando "NLST". El *argument* opcional es un directorio para
      listar (el predeterminado es el directorio del servidor actual).
      Se pueden usar varios argumentos para pasar opciones no estándar
      al comando "NLST".

      Nota:

        Si tu servidor admite el comando, "mlsd()" ofrece una API
        mejor.

   dir(argument[, ...])

      Produce a directory listing as returned by the "LIST" command,
      printing it to standard output.  The optional *argument* is a
      directory to list (default is the current server directory).
      Multiple arguments can be used to pass non-standard options to
      the "LIST" command.  If the last argument is a function, it is
      used as a *callback* function as for "retrlines()"; the default
      prints to "sys.stdout".  This method returns "None".

      Nota:

        Si tu servidor admite el comando, "mlsd()" ofrece una API
        mejor.

   rename(fromname, toname)

      Asigna un nombre nuevo al archivo en el servidor desde
      *fromname* a *toname*.

   delete(filename)

      Remueve el archivo nombrado *filename* del servidor.  De ser
      exitoso, retorna el texto de la respuesta, de lo contrario,
      lanza "error_perm" sobre errores de permiso o "error_reply"
      sobre otros errores.

   cwd(pathname)

      Configura el directorio actual en el servidor.

   mkd(pathname)

      Crea un nuevo directorio en el servidor.

   pwd()

      Retorna el nombre de ruta del directorio actual en el servidor.

   rmd(dirname)

      Elimina el directorio en el servidor llamado *dirname*.

   size(filename)

      Solicita el tamaño del archivo llamado *filename* en el
      servidor.  De ser exitoso, se retorna el tamaño del archivo como
      un entero, de lo contrario retorna "None". Nótese que el comando
      "SIZE" no está estandarizado, pero es admitido por muchas
      implementaciones comunes de servidor.

   quit()

      Envía un comando "QUIT" al servidor y cierra la conexión. Esta
      es la forma "políticamente correcta" de cerrar una conexión,
      pero puede lanzar una excepción si el servidor responde con un
      error al comando "QUIT". Esto implica una llamada al método
      "close()" que hace inútil la instancia de "FTP" para llamadas
      posteriores (véase más adelante).

   close()

      Cierra la conexión de forma unilateral. Esto no debería
      aplicarse a una conexión ya cerrada, como luego de una llamada
      exitosa a "quit()". Después de esta llamada, la instancia "FTP"
      ya no debería utilizarse (luego de una llamada a "close()" o
      "quit()" no puedes abrir nuevamente la conexión emitiendo otro
      método "login()".

### FTP_TLS objects

class ftplib.FTP_TLS(host='', user='', passwd='', acct='', *, context=None, timeout=None, source_address=None, encoding='utf-8')

   An "FTP" subclass which adds TLS support to FTP as described in
   **RFC 4217**. Connect to port 21 implicitly securing the FTP
   control connection before authenticating.

   Nota:

     The user must explicitly secure the data connection by calling
     the "prot_p()" method.

   Parámetros:
      * **host** (*str*) -- The hostname to connect to. If given,
        "connect(host)" is implicitly called by the constructor.

      * **user** (*str*) -- The username to log in with (default:
        "'anonymous'"). If given, "login(host, passwd, acct)" is
        implicitly called by the constructor.

      * **passwd** (*str*) -- The password to use when logging in. If
        not given, and if *passwd* is the empty string or ""-"", a
        password will be automatically generated.

      * **acct** (*str*) -- Account information to be used for the
        "ACCT" FTP command. Few systems implement this. See RFC-959
        for more details.

      * **context** ("ssl.SSLContext") -- An SSL context object which
        allows bundling SSL configuration options, certificates and
        private keys into a single, potentially long-lived, structure.
        Please read Consideraciones de seguridad for best practices.

      * **timeout** (*float** | **None*) -- A timeout in seconds for
        blocking operations like "connect()" (default: the global
        default timeout setting).

      * **source_address** (*tuple** | **None*) -- A 2-tuple "(host,
        port)" for the socket to bind to as its source address before
        connecting.

      * **encoding** (*str*) -- The encoding for directories and
        filenames (default: "'utf-8'").

   Added in version 3.2.

   Distinto en la versión 3.3: Added the *source_address* parameter.

   Distinto en la versión 3.4: La clase ahora admite el chequeo del
   nombre con "ssl.SSLContext.check_hostname" y *Server Name
   Indication* (véase "ssl.HAS_SNI").

   Distinto en la versión 3.9: Si el parámetro *timeout* se establece
   en cero, lanzará un "ValueError" para evitar la creación de un
   socket sin bloqueo. Se agregó el parámetro *encoding*, y el valor
   predeterminado se cambió de Latin-1 a UTF-8 para seguir **RFC
   2640**.

   Distinto en la versión 3.12: Se han eliminado los parámetros
   obsoletos *keyfile* y *certfile*.

   Aquí hay una sesión de ejemplo que usa la clase "FTP_TLS":

      >>> ftps = FTP_TLS('ftp.pureftpd.org')
      >>> ftps.login()
      '230 Anonymous user logged in'
      >>> ftps.prot_p()
      '200 Data protection level set to "private"'
      >>> ftps.nlst()
      ['6jack', 'OpenBSD', 'antilink', 'blogbench', 'bsdcam', 'clockspeed', 'djbdns-jedi', 'docs', 'eaccelerator-jedi', 'favicon.ico', 'francotone', 'fugu', 'ignore', 'libpuzzle', 'metalog', 'minidentd', 'misc', 'mysql-udf-global-user-variables', 'php-jenkins-hash', 'php-skein-hash', 'php-webdav', 'phpaudit', 'phpbench', 'pincaster', 'ping', 'posto', 'pub', 'public', 'public_keys', 'pure-ftpd', 'qscan', 'qtc', 'sharedance', 'skycache', 'sound', 'tmp', 'ucarp']

   "FTP_TLS" class inherits from "FTP", defining these additional
   methods and attributes:

   ssl_version

      La versión SSL para usar (toma como predeterminado
      "ssl.PROTOCOL_SSLv23").

   auth()

      Establece una conexión de control segura usando TLS o SSL,
      dependiendo de qué esté especificado en el atributo
      "ssl_version".

      Distinto en la versión 3.4: El método ahora admite el chequeo
      del nombre con "ssl.SSLContext.check_hostname" y *Server Name
      Indication* (véase "ssl.HAS_SNI").

   ccc()

      Revierte el canal de control a texto plano. Esto puede ser útil
      para aprovechar cortafuegos que saben manejar NAT con FTP no-
      seguro sin abrir puertos fijos.

      Added in version 3.3.

   prot_p()

      Configura conexión de datos segura.

   prot_c()

      Configura la conexión de datos de tipo texto común.

### Module variables

exception ftplib.error_reply

   Se lanza una excepción cuando una respuesta inesperada se recibe
   del servidor.

exception ftplib.error_temp

   Se genera una excepción cuando  se recibe un código de error que
   refiere a un error temporal (códigos de respuesta en el rango
   400-499).

exception ftplib.error_perm

   Se lanza una excepción cuando se recibe un código de error que
   refiere a un error permanente (códigos de respuesta en el rango 500
   --599).

exception ftplib.error_proto

   Se lanza una excepción cuando se recibe una respuesta del servidor
   que no coincide con las especificaciones de respuesta del protocolo
   de transferencia de archivos (FTP), es decir, que comienza con un
   dígito en el rango 1--5.

ftplib.all_errors

   El conjunto de todas las excepciones (como una tupla) que los
   métodos de instancias "FTP" pueden lanzar como resultado de
   problemas con la conexión FTP (a diferencia de los errores de
   programación hechos por el autor de la llamada). Este conjunto
   incluye las cuatro excepciones enumeradas anteriormente, como
   también "OSError" y "EOFError".

Ver también:

  Módulo "netrc"
     Analizador para el formato de archivo ".netrc". El archivo
     ".netrc" suele ser utilizado por clientes FTP para cargar la
     información de autenticación de usuario antes de solicitarlo al
     usuario.
