---
title: '"ssl" --- TLS/SSL wrapper for socket objects'
source_url: https://docs.python.org/es/3
source_path: library/ssl.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3880
---

# "ssl" --- TLS/SSL wrapper for socket objects

**Código fuente:**Lib/ssl.py

======================================================================

This module provides access to Transport Layer Security (often known
as "Secure Sockets Layer") encryption and peer authentication
facilities for network sockets, both client-side and server-side.
This module uses the OpenSSL library.

This is an *optional module*. If it is missing from your copy of
CPython, look for documentation from your distributor (that is,
whoever provided Python to you). If you are the distributor, see
Requirements for optional modules.

Nota:

  Some behavior may be platform dependent, since calls are made to the
  operating system socket APIs.  The installed version of OpenSSL may
  also cause variations in behavior. For example, TLSv1.3 comes with
  OpenSSL version 1.1.1.

Advertencia:

  No use este módulo sin leer Consideraciones de seguridad. Hacerlo
  puede generar una falsa sensación de seguridad, ya que la
  configuración predeterminada del módulo ssl no es necesariamente la
  adecuada para su aplicación.

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

Esta sección documenta los objetos y funciones en el módulo "ssl";
para más información general sobre TLS,SSL, y certificados, se
recomienda que el lector acuda a la sección "Ver también" al final de
la página.

This module provides a class, "ssl.SSLSocket", which is derived from
the "socket.socket" type, and provides a socket-like wrapper that also
encrypts and decrypts the data going over the socket with SSL.  It
supports additional methods such as "getpeercert()", which retrieves
the certificate of the other side of the connection, "cipher()", which
retrieves the cipher being used for the secure connection or
"get_verified_chain()", "get_unverified_chain()" which retrieves
certificate chain.

Para aplicaciones más sofisticadas, la clase "ssl.SSLContext" ayuda a
administrar la configuración y los certificados, que luego pueden ser
heredados por sockets SSL creados a través del método
"SSLContext.wrap_socket()".

Distinto en la versión 3.5.3: Actualizado para admitir la vinculación
con OpenSSL 1.1.0

Distinto en la versión 3.6: OpenSSL 0.9.8, 1.0.0 y 1.0.1 son obsoletos
y no son compatibles. En el futuro, el módulo ssl requerirá al menos
OpenSSL 1.0.2 o 1.1.0.

Distinto en la versión 3.10: Se ha implementado **PEP 644**. El módulo
ssl requiere OpenSSL 1.1.1 o versiones más recientes.El uso de
constantes y funciones obsoletas genera advertencias de obsolescencia.

## Functions, constants, and exceptions

### Creación de sockets

Instances of "SSLSocket" must be created using the
"SSLContext.wrap_socket()" method. The helper function
"create_default_context()" returns a new context with secure default
settings.

Ejemplo de socket cliente con contexto por defecto y doble pila
IPv4/IPv6:

   import socket
   import ssl

   hostname = 'www.python.org'
   context = ssl.create_default_context()

   with socket.create_connection((hostname, 443)) as sock:
       with context.wrap_socket(sock, server_hostname=hostname) as ssock:
           print(ssock.version())

Ejemplo de socket cliente con contexto personalizado y IPv4:

   hostname = 'www.python.org'
   # PROTOCOL_TLS_CLIENT requires valid cert chain and hostname
   context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
   context.load_verify_locations('path/to/cabundle.pem')

   with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
       with context.wrap_socket(sock, server_hostname=hostname) as ssock:
           print(ssock.version())

Ejemplo de socket servidor escuchando en localhost IPv4:

   context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
   context.load_cert_chain('/path/to/certchain.pem', '/path/to/private.key')

   with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
       sock.bind(('127.0.0.1', 8443))
       sock.listen(5)
       with context.wrap_socket(sock, server_side=True) as ssock:
           conn, addr = ssock.accept()
           ...

### Creación de contexto

Una función conveniente ayuda a crear objetos "SSLContext" para
propósitos comunes.

ssl.create_default_context(purpose=Purpose.SERVER_AUTH, *, cafile=None, capath=None, cadata=None)

   Return a new "SSLContext" object with default settings for the
   given *purpose*.  The settings are chosen by the "ssl" module, and
   usually represent a higher security level than when calling the
   "SSLContext" constructor directly.

   *cafile*, *capath*, *cadata* representan certificados CA opcionales
   para confiar en la verificación de certificados, como en
   "SSLContext.load_verify_locations()". Si los tres son "None" al
   mismo tiempo, esta función puede optar por confiar en su lugar en
   los certificados CA por defecto del sistema.

   The settings are: "PROTOCOL_TLS_CLIENT" or "PROTOCOL_TLS_SERVER",
   "OP_NO_SSLv2", and "OP_NO_SSLv3" with high encryption cipher suites
   without RC4 and without unauthenticated cipher suites. Passing
   "SERVER_AUTH" as *purpose* sets "verify_mode" to "CERT_REQUIRED"
   and either loads CA certificates (when at least one of *cafile*,
   *capath* or *cadata* is given) or uses
   "SSLContext.load_default_certs()" to load default CA certificates.

   Cuando "keylog_filename" es soportado y la variable de entorno
   "SSLKEYLOGFILE" está establecida, "create_default_context()" activa
   el registro de claves.

   The default settings for this context include
   "VERIFY_X509_PARTIAL_CHAIN" and "VERIFY_X509_STRICT". These make
   the underlying OpenSSL implementation behave more like a conforming
   implementation of **RFC 5280**, in exchange for a small amount of
   incompatibility with older X.509 certificates.

   Nota:

     El protocolo, las opciones, el cifrado y otros ajustes pueden
     cambiar a valores mas restrictivos en cualquier momento sin
     previa obsolescencia. Los valores representan un equilibrio justo
     entre compatibilidad y seguridad.Si su aplicación necesita
     ajustes específicos, debe crear un "SSLContext" y aplicar los
     ajustes usted mismo.

   Nota:

     Si encuentra que cuando ciertos clientes o servidores antiguos
     intentan conectarse con un "SSLContext" creado con esta función
     obtienen un error indicando *Protocol or cipher suite mismatch*,
     puede ser que estos sólo soportan SSL3.0 el cual esta función
     excluye utilizando "OP_NO_SSLv3". SSL3.0 está ampliamente
     considerado como completamente roto. Si todavía desea seguir
     utilizando esta función pero permitir conexiones SSL 3.0, puede
     volver a activarlas mediante:

        ctx = ssl.create_default_context(Purpose.CLIENT_AUTH)
        ctx.options &= ~ssl.OP_NO_SSLv3

   Nota:

     This context enables "VERIFY_X509_STRICT" by default, which may
     reject pre-**RFC 5280** or malformed certificates that the
     underlying OpenSSL implementation otherwise would accept. While
     disabling this is not recommended, you can do so using:

        ctx = ssl.create_default_context()
        ctx.verify_flags &= ~ssl.VERIFY_X509_STRICT

   Added in version 3.4.

   Distinto en la versión 3.4.4: RC4 ha sido abandonado de la cadena
   de cifrado por defecto.

   Distinto en la versión 3.6: ChaCha20/Poly1305 ha sido agregado a la
   cadena de caracteres de cifrado por defecto.3DES ha sido abandonado
   de la cadena de caracteres de cifrado por defecto.

   Distinto en la versión 3.8: Soporte del registro de claves en
   "SSLKEYLOGFILE" ha sido agregado.

   Distinto en la versión 3.10: El contexto ahora usa el protocolo
   "PROTOCOL_TLS_CLIENT" o "PROTOCOL_TLS_SERVER" en lugar del
   "PROTOCOL_TLS" genérico.

   Distinto en la versión 3.13: The context now uses
   "VERIFY_X509_PARTIAL_CHAIN" and "VERIFY_X509_STRICT" in its default
   verify flags.

### Excepciones

exception ssl.SSLError

   Se lanza para señalar un error de la implementación de SSL
   subyacente (actualmente proporcionada por la biblioteca OpenSSL).
   Esto indica algún problema en la capa de cifrado y autenticación de
   alto nivel que se superpone a la conexión de red subyacente. Este
   error es un subtipo de "OSError". El código de error y el mensaje
   de las instancias de "SSLError" son proporcionados por la
   biblioteca OpenSSL.

   Distinto en la versión 3.3: "SSLError" era un subtipo de
   "socket.error".

   library

      Una cadena de caracteres mnemotécnica que designa el submódulo
      de OpenSSL en el que se ha producido el error, como "SSL", "PEM"
      o "X509". El rango de valores posibles depende de la versión de
      OpenSSL.

      Added in version 3.3.

   reason

      Una cadena de caracteres mnemotécnica que designa la razón por
      la que se produjo el error, por ejemplo
      "CERTIFICATE_VERIFY_FAILED". El rango de valores posibles
      depende de la versión de OpenSSL.

      Added in version 3.3.

exception ssl.SSLZeroReturnError

   Una subclase de "SSLError" lanzada cuando se intenta leer o
   escribir y la conexión SSL ha sido cerrada limpiamente. Tenga en
   cuenta que esto no significa que el transporte subyacente (lectura
   TCP) haya sido cerrado.

   Added in version 3.3.

exception ssl.SSLWantReadError

   Una subclase de "SSLError" lanzada por un socket SSL no bloqueante
   cuando se intenta leer o escribir datos, pero mas datos necesitan
   ser recibidos en el transporte TCP subyacente antes de que la
   solicitud pueda ser completada.

   Added in version 3.3.

exception ssl.SSLWantWriteError

   Una subclase de "SSLError" lanzada por un socket SSL no bloqueante
   cuando se intenta leer o escribir datos, pero mas datos necesitan
   ser enviados en el transporte TCP subyacente antes de que la
   solicitud pueda ser completada.

   Added in version 3.3.

exception ssl.SSLSyscallError

   Una subclase de "SSLError" lanzada cuando se encuentra un error del
   sistema mientras se intenta completar una operación en un socket
   SSL. Por desgracia, no hay una manera fácil de inspeccionar el
   número errno original.

   Added in version 3.3.

exception ssl.SSLEOFError

   Una subclase de "SSLError" lanzada cuando la conexión SSL ha sido
   cancelada abruptamente. Generalmente, no debería intentar
   reutilizar el transporte subyacente cuando este error se produce.

   Added in version 3.3.

exception ssl.SSLCertVerificationError

   Una subclase de "SSLError" lanzada cuando la validación del
   certificado ha fallado.

   Added in version 3.7.

   verify_code

      Un número de error numérico que indica el error de verificación.

   verify_message

      Una cadena de caracteres legible del error de verificación.

exception ssl.CertificateError

   Un alias para "SSLCertVerificationError".

   Distinto en la versión 3.7: La excepción es ahora un alias para
   "SSLCertVerificationError".

### Generación aleatoria

ssl.RAND_bytes(num, /)

   Retorna *num* bytes pseudoaleatorios criptográficamente fuertes.
   Lanza un "SSLError" si el PRNG no a sido sembrado con suficiente
   datos o si la operación no es soportada por el método RAND actual.
   "RAND_status()" puede ser usada para verificar el estado de PRNG y
   "RAND_add()" puede ser usada para sembrar el PRNG.

   Para casi todas las aplicaciones "os.urandom()" es preferible.

   Léase el artículo Wikipedia, Generador de números pseudoaleatorios
   criptográficamente seguro (CSPRNG), para obtener los requisitos
   para un generador criptográficamente seguro.

   Added in version 3.3.

ssl.RAND_status()

   Retorna "True" si el generador de números pseudoaleatorios SSL a
   sido sembrado con 'suficiente' aleatoriedad, y "False" de lo
   contrario. Puede utilizarse "ssl.RAND_egd()" y "ssl.RAND_add()"
   para aumentar la aleatoriedad del generador de números
   pseudoaleatorios.

ssl.RAND_add(bytes, entropy, /)

   Mix the given *bytes* into the SSL pseudo-random number generator.
   The parameter *entropy* (a float) is a lower bound on the entropy
   contained in string (so you can always use "0.0").  See **RFC
   1750** for more information on sources of entropy.

   Distinto en la versión 3.5: Ahora se acepta *bytes-like object*
   modificable.

### Gestión de certificados

ssl.cert_time_to_seconds(cert_time)

   Return the time in seconds since the epoch, given the "cert_time"
   string representing the "notBefore" or "notAfter" date from a
   certificate in ""%b %d %H:%M:%S %Y %Z"" strptime format (C locale).

   He aquí un ejemplo:

      >>> import ssl
      >>> import datetime as dt
      >>> timestamp = ssl.cert_time_to_seconds("Jan  5 09:34:43 2018 GMT")
      >>> timestamp
      1515144883
      >>> print(dt.datetime.fromtimestamp(timestamp, dt.UTC))
      2018-01-05 09:34:43+00:00

   Las fechas *notBefore* o *notAfter* deben utilizar GMT (**RFC
   5280**).

   Distinto en la versión 3.5: Interpreta la hora de entrada como una
   hora en UTC según lo especificado por la zona horaria 'GMT' en la
   cadena de caracteres de entrada. Anteriormente se utilizaba la zona
   horaria local. Retorna un número entero (sin fracciones de segundo
   en el formato de entrada)

ssl.get_server_certificate(addr, ssl_version=PROTOCOL_TLS_CLIENT, ca_certs=None[, timeout])

   Given the address "addr" of an SSL-protected server, as a
   (*hostname*, *port-number*) pair, fetches the server's certificate,
   and returns it as a PEM-encoded string.  If "ssl_version" is
   specified, uses that version of the SSL protocol to attempt to
   connect to the server.  If *ca_certs* is specified, it should be a
   file containing a list of root certificates, the same format as
   used for the *cafile* parameter in
   "SSLContext.load_verify_locations()".  The call will attempt to
   validate the server certificate against that set of root
   certificates, and will fail if the validation attempt fails.  A
   timeout can be specified with the "timeout" parameter.

   Distinto en la versión 3.3: Esta función es ahora compatible IPv6.

   Distinto en la versión 3.5: La *ssl_version* por defecto se cambia
   de "PROTOCOL_SSLv3" a "PROTOCOL_TLS" para una máxima compatibilidad
   con los servidores modernos.

   Distinto en la versión 3.10: Se agregó el argumento *session*.

ssl.DER_cert_to_PEM_cert(der_cert_bytes)

   Dado un certificado como blob de bytes codificado en DER, retorna
   una versión de cadena de caracteres codificada en PEM del mismo
   certificado.

ssl.PEM_cert_to_DER_cert(pem_cert_string)

   Dado un certificado como cadena de caracteres ASCII PEM, retorna
   una secuencia de bytes codificada con DER para ese mismo
   certificado.

ssl.get_default_verify_paths()

   Retorna una tupla con nombre con las rutas por defecto de cafile y
   capath de OpenSSL. Las rutas son las mismas que las usadas por
   "SSLContext.set_default_verify_paths()". El valor de retorno es una
   *named tuple* "DefaultVerifyPaths":

   * "cafile" - ruta resuelta a cafile o "None" si el archivo no
     existe,

   * "capath" - ruta resuelta a capath o "None" si el directorio no
     existe,

   * "openssl_cafile_env" - clave de entorno de OpenSSL que apunta a
     un cafile,

   * "openssl_cafile" - camino codificado de forma rígida a un cafile,

   * "openssl_capath_env" - clave de entorno de OpenSSL que apunta a
     un capath,

   * "openssl_capath" - camino codificado de forma rígida a un
     directorio capath

   Added in version 3.4.

ssl.enum_certificates(store_name)

   Recupera los certificados del almacén de certificados del sistema
   de Windows. *store_name* puede ser uno de los siguientes: "CA",
   "ROOT" o "MY". Windows también puede proporcionar almacenes de
   certificados adicionales.

   La función retorna una lista de tuplas (cert_bytes, encoding_type,
   trust). El encoding_type especifica la codificación de cert_bytes.
   Es "x509_asn" para datos X.509 ASN.1 o "pkcs_7_asn" para datos
   PKCS#7 ASN.1. Trust especifica el propósito del certificado como un
   conjunto de OIDS o exactamente "True" si el certificado es de
   confianza para todos los propósitos.

   Ejemplo:

      >>> ssl.enum_certificates("CA")
      [(b'data...', 'x509_asn', {'1.3.6.1.5.5.7.3.1', '1.3.6.1.5.5.7.3.2'}),
       (b'data...', 'x509_asn', True)]

   Availability: Windows.

   Added in version 3.4.

ssl.enum_crls(store_name)

   Obtiene CRLs del almacén de certificados del sistema de Windows.
   *store_name* puede ser uno de los siguientes: "CA", "ROOT" o "MY".
   Windows también puede proporcionar almacenes de certificados
   adicionales.

   La función retorna una lista de tuplas (cert_bytes, encoding_type,
   trust). El encoding_type especifica la codificación de cert_bytes.
   Es "x509_asn" para datos X.509 ASN.1 o "pkcs_7_asn" para datos
   PKCS#7 ASN.1.

   Availability: Windows.

   Added in version 3.4.

### Constantes

   Todas las constantes son ahora colecciones "enum.IntEnum" o
   "enum.IntFlag".

   Added in version 3.6.

ssl.CERT_NONE

   Possible value for "SSLContext.verify_mode". Except for
   "PROTOCOL_TLS_CLIENT", it is the default mode.  With client-side
   sockets, just about any cert is accepted.  Validation errors, such
   as untrusted or expired cert, are ignored and do not abort the
   TLS/SSL handshake.

   En modo servidor, no se solicita ningún certificado al cliente, por
   lo que el cliente no envía ninguno para la autenticación del
   certificado del cliente.

   Vea la discusión sobre Consideraciones de seguridad más abajo.

ssl.CERT_OPTIONAL

   Possible value for "SSLContext.verify_mode". In client mode,
   "CERT_OPTIONAL" has the same meaning as "CERT_REQUIRED". It is
   recommended to use "CERT_REQUIRED" for client-side sockets instead.

   En el modo servidor, se envía una solicitud de certificado de
   cliente al cliente. El cliente puede ignorar la solicitud o enviar
   un certificado para realizar la autenticación de certificado de
   cliente TLS. Si el cliente opta por enviar un certificado, éste se
   verifica. Cualquier error de verificación aborta inmediatamente el
   handshake TLS.

   Use of this setting requires a valid set of CA certificates to be
   passed to "SSLContext.load_verify_locations()".

ssl.CERT_REQUIRED

   Possible value for "SSLContext.verify_mode". In this mode,
   certificates are required from the other side of the socket
   connection; an "SSLError" will be raised if no certificate is
   provided, or if its validation fails. This mode is **not**
   sufficient to verify a certificate in client mode as it does not
   match hostnames.  "check_hostname" must be enabled as well to
   verify the authenticity of a cert. "PROTOCOL_TLS_CLIENT" uses
   "CERT_REQUIRED" and enables "check_hostname" by default.

   Con socket servidor, este modo proporciona una autenticación
   obligatoria de certificado de cliente TLS. Se envía una solicitud
   de certificado de cliente al cliente y el cliente debe proporcionar
   un certificado válido y de confianza.

   Use of this setting requires a valid set of CA certificates to be
   passed to "SSLContext.load_verify_locations()".

class ssl.VerifyMode

   Colección "enum.IntEnum" de constantes CERT_*.

   Added in version 3.6.

ssl.VERIFY_DEFAULT

   Valor posible para "SSLContext.verify_flags". En este modo, las
   listas de revocación de certificado (CRLs) no son verificadas. Por
   defecto OpenSSL no requiere ni verifica CRLs.

   Added in version 3.4.

ssl.VERIFY_CRL_CHECK_LEAF

   Valor posible para "SSLContext.verify_flags". En este modo, sólo el
   certificado de pares es verificado pero ninguno de los certificados
   CA intermedios. El modo requiere una CRL válida que esté firmada
   por el emisor del certificado de pares (su CA antecesora directa).
   Si no se ha cargado una CRL adecuada con
   "SSLContext.load_verify_locations", la validación fallará.

   Added in version 3.4.

ssl.VERIFY_CRL_CHECK_CHAIN

   Valor posible para "SSLContext.verify_flags". En este modo, las
   CRLs de todos los certificados en la cadena de certificado de pares
   son verificadas.

   Added in version 3.4.

ssl.VERIFY_X509_STRICT

   Valor posible para "SSLContext.verify_flags" para desactivar
   soluciones alternativas para certificados X.509 rotos.

   Added in version 3.4.

ssl.VERIFY_ALLOW_PROXY_CERTS

   Valor posible para "SSLContext.verify_flags" para desactivar
   soluciones alternativas para certificados X.509 rotos.

   Added in version 3.10.

ssl.VERIFY_X509_TRUSTED_FIRST

   Valor posible para "SSLContext.verify_flags". Indica a OpenSSL de
   preferir certificados de confianza al construir la cadena de
   confianza para validar un certificado. Esta opción está activada
   por defecto.

   Added in version 3.4.4.

ssl.VERIFY_X509_PARTIAL_CHAIN

   Valor posible para "SSLContext.verify_flags". Indica a OpenSSL que
   acepte CA intermedias en el almacén de confianza para que se traten
   como anclajes de confianza, de la misma manera que los certificados
   de CA raíz autofirmados. Esto hace posible confiar en los
   certificados emitidos por una CA intermedia sin tener que confiar
   en su CA raíz antecesora.

   Added in version 3.10.

class ssl.VerifyFlags

   Colección "enum.IntFlag" de constantes VERIFY_*.

   Added in version 3.6.

ssl.PROTOCOL_TLS

   Selecciona la versión mas alta del protocolo soportada tanto por el
   cliente como por el servidor. A pesar de su nombre, esta opción
   puede seleccionar ambos protocolos "SSL" y "TLS".

   Added in version 3.6.

   Obsoleto desde la versión 3.10: Los clientes y servidores TLS
   requieren diferentes configuraciones predeterminadas para una
   comunicación segura. La constante del protocolo TLS genérico está
   en desuso en favor de "PROTOCOL_TLS_CLIENT" y
   "PROTOCOL_TLS_SERVER".

ssl.PROTOCOL_TLS_CLIENT

   Negocie automáticamente la versión de protocolo más alta que
   admiten tanto el cliente como el servidor, y configure las
   conexiones del lado del cliente de contexto. El protocolo habilita
   "CERT_REQUIRED" y "check_hostname" de forma predeterminada.

   Added in version 3.6.

ssl.PROTOCOL_TLS_SERVER

   Selecciona la versión mas alta del protocolo soportada tanto por el
   cliente como por el servidor. A pesar de su nombre, esta opción
   puede seleccionar ambos protocolos "SSL" y "TLS".

   Added in version 3.6.

ssl.PROTOCOL_SSLv23

   Alias para "PROTOCOL_TLS".

   Obsoleto desde la versión 3.6: Utilice en su lugar "PROTOCOL_TLS".

ssl.PROTOCOL_SSLv3

   Selecciona la versión 3 de SSL como protocolo de cifrado del canal.

   Este protocolo no está disponible si se compila OpenSSL con la
   opción "no-ssl3".

   Advertencia:

     La versión 3 de SSL es insegura. Su uso es muy desaconsejado.

   Obsoleto desde la versión 3.6: OpenSSL ha descontinuado todos los
   protocolos específicos de la versión. Utilice el protocolo
   predeterminado "PROTOCOL_TLS_SERVER" o "PROTOCOL_TLS_CLIENT" con
   "SSLContext.minimum_version" y "SSLContext.maximum_version" en su
   lugar.

ssl.PROTOCOL_TLSv1

   Selecciona la versión 1.0 de TLS como protocolo de cifrado del
   canal.

   Obsoleto desde la versión 3.6: OpenSSL ha descontinuado todos los
   protocolos específicos de la versión.

ssl.PROTOCOL_TLSv1_1

   Selecciona la versión 1.1 de TLS como protocolo de cifrado del
   canal. Disponible sólo con openssl en versión 1.0.1+.

   Added in version 3.4.

   Obsoleto desde la versión 3.6: OpenSSL ha descontinuado todos los
   protocolos específicos de la versión.

ssl.PROTOCOL_TLSv1_2

   Selecciona la versión 1.1 de TLS como protocolo de cifrado del
   canal. Disponible sólo con openssl en versión 1.0.1+.

   Added in version 3.4.

   Obsoleto desde la versión 3.6: OpenSSL ha descontinuado todos los
   protocolos específicos de la versión.

ssl.OP_ALL

   Activa soluciones alternativas para varios errores presentes en
   otras implementaciones SSL. Esta opción esta activada por defecto.
   No necesariamente activa las mismas opciones como la constante
   "SSL_OP_ALL" de OpenSSL.

   Added in version 3.2.

ssl.OP_NO_SSLv2

   Evita una conexión SSLv2. Esta opción sólo es aplicable junto con
   "PROTOCOL_TLS". Evita que los pares elijan SSLv2 como versión del
   protocolo.

   Added in version 3.2.

   Obsoleto desde la versión 3.6: SSLv2 es obsoleto

ssl.OP_NO_SSLv3

   Evita una conexión SSLv3. Esta opción sólo es aplicable junto con
   "PROTOCOL_TLS". Evita que los pares elijan SSLv3 como versión del
   protocolo.

   Added in version 3.2.

   Obsoleto desde la versión 3.6: SSLv3 es obsoleto

ssl.OP_NO_TLSv1

   Evita una conexión TLSv1. Esta opción sólo es aplicable junto con
   "PROTOCOL_TLS". Evita que los pares elijan TLSv1 como versión del
   protocolo.

   Added in version 3.2.

   Obsoleto desde la versión 3.7: Esta opción es obsoleta desde
   OpenSSL 1.1.0, utilice en su lugar los nuevos
   "SSLContext.minimum_version" y "SSLContext.maximum_version".

ssl.OP_NO_TLSv1_1

   Evita una conexión TLSv1.1. Esta opción sólo es aplicable junto con
   "PROTOCOL_TLS". Evita que los pares elijan TLSv1.1 como versión del
   protocolo. Disponible sólo con openssl en versión 1.0.1+.

   Added in version 3.4.

   Obsoleto desde la versión 3.7: Esta opción es obsoleta desde
   OpenSSL 1.1.0.

ssl.OP_NO_TLSv1_2

   Evita una conexión TLSv1.2. Esta opción sólo es aplicable junto con
   "PROTOCOL_TLS". Evita que los pares elijan TLSv1.2 como versión del
   protocolo. Disponible sólo con openssl en versión 1.0.1+.

   Added in version 3.4.

   Obsoleto desde la versión 3.7: Esta opción es obsoleta desde
   OpenSSL 1.1.0.

ssl.OP_NO_TLSv1_3

   Evita una conexión TLSv1.3. Esta opción sólo es aplicable junto con
   "PROTOCOL_TLS". Evita que los pares elijan TLSv1.3 como versión del
   protocolo. TLS 1.3 está disponible con OpenSSL 1.1.1 o superior.
   Cuando Python es compilado contra una versión mas antigua de
   OpenSSL, la opción vale *0* por defecto.

   Added in version 3.6.3.

   Obsoleto desde la versión 3.7: The option is deprecated since
   OpenSSL 1.1.0. It was added to 2.7.15 and 3.6.3 for backwards
   compatibility with OpenSSL 1.0.2.

ssl.OP_NO_RENEGOTIATION

   Desactiva toda re-negociación en TLSv1.2 y anteriores. No envía
   mensajes HelloRequest e ignora solicitudes de re-negociación vía
   ClientHello.

   Esta opción sólo está disponible con OpenSSL 1.1.0h y posteriores.

   Added in version 3.7.

ssl.OP_CIPHER_SERVER_PREFERENCE

   Utiliza la preferencia de ordenación de cifrado del servidor, en
   lugar de la del cliente. Esta opción no tiene efecto en los sockets
   del cliente ni en los sockets del servidor SSLv2.

   Added in version 3.3.

ssl.OP_SINGLE_DH_USE

   Prevents reuse of the same DH key for distinct SSL sessions.  This
   improves forward secrecy but requires more computational resources.
   This option only applies to server sockets.

   Added in version 3.3.

ssl.OP_SINGLE_ECDH_USE

   Prevents reuse of the same ECDH key for distinct SSL sessions.
   This improves forward secrecy but requires more computational
   resources. This option only applies to server sockets.

   Added in version 3.3.

ssl.OP_ENABLE_MIDDLEBOX_COMPAT

   Enviar mensajes Change Cipher Spec (CCS) ficticios en el handshake
   de TLS 1.3 para que una conexión TLS 1.3 se parezca más a una
   conexión TLS 1.2.

   Esta opción sólo está disponible con OpenSSL 1.1.1 y posteriores.

   Added in version 3.8.

ssl.OP_NO_COMPRESSION

   Desactivar la compresión en el canal SSL. Esto es útil si el
   protocolo de la aplicación soporta su propio esquema de compresión.

   Added in version 3.3.

class ssl.Options

   Colección "enum.IntFlag" de constantes OP_*.

ssl.OP_NO_TICKET

   Evita que el lado del cliente solicite un ticket de sesión.

   Added in version 3.6.

ssl.OP_IGNORE_UNEXPECTED_EOF

   Ignore el cierre inesperado de las conexiones TLS.

   Esta opción sólo está disponible con OpenSSL 1.0.0 y posteriores.

   Added in version 3.10.

ssl.OP_ENABLE_KTLS

   Enable the use of the kernel TLS. To benefit from the feature,
   OpenSSL must have been compiled with support for it, and the
   negotiated cipher suites and extensions must be supported by it (a
   list of supported ones may vary by platform and kernel version).

   Note that with enabled kernel TLS some cryptographic operations are
   performed by the kernel directly and not via any available OpenSSL
   Providers. This might be undesirable if, for example, the
   application requires all cryptographic operations to be performed
   by the FIPS provider.

   Esta opción sólo está disponible con OpenSSL 1.0.0 y posteriores.

   Added in version 3.12.

ssl.OP_LEGACY_SERVER_CONNECT

   Allow legacy insecure renegotiation between OpenSSL and unpatched
   servers only.

   Added in version 3.12.

ssl.HAS_ALPN

   Si la biblioteca OpenSSL tiene soporte incorporado para la
   extensión TLS *Application-Layer Protocol Negotiation* como se
   describe en **RFC 7301**.

   Added in version 3.5.

ssl.HAS_NEVER_CHECK_COMMON_NAME

   Si la biblioteca OpenSSL tiene soporte incorporado para no
   comprobar el nombre común del sujeto y
   "SSLContext.hostname_checks_common_name" es modificable.

   Added in version 3.7.

ssl.HAS_ECDH

   Si la biblioteca OpenSSL tiene soporte incorporado para el
   intercambio de claves Diffie-Hellman basado en Elliptic Curve. Esto
   debería ser cierto a menos que la función haya sido desactivada
   explícitamente por el distribuidor.

   Added in version 3.3.

ssl.HAS_SNI

   Si la biblioteca OpenSSL tiene soporte incorporado para la
   extensión *Server Name Indication* (como se define en **RFC
   6066**).

   Added in version 3.2.

ssl.HAS_NPN

   Si la biblioteca OpenSSL tiene soporte incorporado para *Next
   Protocol Negotiation* como se describe en Application Layer
   Protocol Negotiation. Cuando es verdadero, puede utilizar el método
   "SSLContext.set_npn_protocols()" para anunciar los protocolos que
   desea soportar.

   Added in version 3.3.

ssl.HAS_SSLv2

   Si la biblioteca OpenSSL tiene soporte incorporado para el
   protocolo SSL 2.0.

   Added in version 3.7.

ssl.HAS_SSLv3

   Si la biblioteca OpenSSL tiene soporte incorporado para el
   protocolo SSL 3.0.

   Added in version 3.7.

ssl.HAS_TLSv1

   Si la biblioteca OpenSSL tiene soporte incorporado para el
   protocolo TLS 1.0.

   Added in version 3.7.

ssl.HAS_TLSv1_1

   Si la biblioteca OpenSSL tiene soporte incorporado para el
   protocolo TLS 1.1.

   Added in version 3.7.

ssl.HAS_TLSv1_2

   Si la biblioteca OpenSSL tiene soporte incorporado para el
   protocolo TLS 1.2.

   Added in version 3.7.

ssl.HAS_TLSv1_3

   Si la biblioteca OpenSSL tiene soporte incorporado para el
   protocolo TLS 1.3.

   Added in version 3.7.

ssl.HAS_PSK

   Whether the OpenSSL library has built-in support for TLS-PSK.

   Added in version 3.13.

ssl.HAS_PHA

   Whether the OpenSSL library has built-in support for TLS-PHA.

   Added in version 3.14.

ssl.CHANNEL_BINDING_TYPES

   Lista de tipos de enlace de canales TLS admitidos. Las cadenas de
   caracteres en esta lista pueden ser usadas como argumentos para
   "SSLSocket.get_channel_binding()".

   Added in version 3.3.

ssl.OPENSSL_VERSION

   La cadena de versión de la biblioteca OpenSSL cargada por el
   intérprete:

      >>> ssl.OPENSSL_VERSION
      'OpenSSL 1.0.2k  26 Jan 2017'

   Added in version 3.2.

ssl.OPENSSL_VERSION_INFO

   Una tupla de cinco números enteros representando la información de
   versión de la biblioteca OpenSSL:

      >>> ssl.OPENSSL_VERSION_INFO
      (1, 0, 2, 11, 15)

   Added in version 3.2.

ssl.OPENSSL_VERSION_NUMBER

   El número de versión en bruto de la biblioteca OpenSSL, como un
   único número entero:

      >>> ssl.OPENSSL_VERSION_NUMBER
      268443839
      >>> hex(ssl.OPENSSL_VERSION_NUMBER)
      '0x100020bf'

   Added in version 3.2.

ssl.ALERT_DESCRIPTION_HANDSHAKE_FAILURE
ssl.ALERT_DESCRIPTION_INTERNAL_ERROR
ALERT_DESCRIPTION_*

   Descripciones de alertas de **RFC 5246** y otras. El IANA TLS Alert
   Registry contiene esta lista y las referencias a las RFC donde se
   define su significado.

   Se utiliza como valor de retorno de la función callback en
   "SSLContext.set_servername_callback()".

   Added in version 3.4.

class ssl.AlertDescription

   Colección "enum.IntEnum" de constantes ALERT_DESCRIPTION_*.

   Added in version 3.6.

Purpose.SERVER_AUTH

   Opción para "create_default_context()" y
   "SSLContext.load_default_certs()". Este valor indica que el
   contexto puede utilizarse para autenticar servidores web (por lo
   tanto, se utilizará para crear sockets del lado del cliente).

   Added in version 3.4.

Purpose.CLIENT_AUTH

   Opción para "create_default_context()" y
   "SSLContext.load_default_certs()". Este valor indica que el
   contexto puede utilizarse para autenticar clientes web (por lo
   tanto, se utilizará para crear sockets del lado del servidor).

   Added in version 3.4.

class ssl.SSLErrorNumber

   Colección "enum.IntEnum" de constantes SSL_ERROR_*.

   Added in version 3.6.

class ssl.TLSVersion

   Colección "enum.IntEnum" de versiones SSL y TLS para
   "SSLContext.maximum_version" y "SSLContext.minimum_version".

   Added in version 3.7.

TLSVersion.MINIMUM_SUPPORTED

TLSVersion.MAXIMUM_SUPPORTED

   La mínima o máxima versión soportada de SSL o TLS. Estas son
   constantes mágicas. Sus valores no reflejan la mas baja o mas alta
   versión TLS/SSL disponible.

TLSVersion.SSLv3

TLSVersion.TLSv1

TLSVersion.TLSv1_1

TLSVersion.TLSv1_2

TLSVersion.TLSv1_3

   SSL 3.0 a TLS 1.3.

   Obsoleto desde la versión 3.10: Todos los miembros de "TLSVersion",
   excepto "TLSVersion.TLSv1_2" y "TLSVersion.TLSv1_3", están en
   desuso.

## SSL sockets

class ssl.SSLSocket(socket.socket)

   Los sockets SSL proporcionan los siguientes métodos de Objetos
   Socket:

   * "accept()"

   * "bind()"

   * "close()"

   * "connect()"

   * "detach()"

   * "fileno()"

   * "getpeername()", "getsockname()"

   * "getsockopt()", "setsockopt()"

   * "gettimeout()", "settimeout()", "setblocking()"

   * "listen()"

   * "makefile()"

   * "recv()", "recv_into()" (but passing a non-zero "flags" argument
     is not allowed)

   * "send()", "sendall()" (with the same limitation)

   * "sendfile()" (but "os.sendfile" will be used for plain-text
     sockets only, else "send()" will be used)

   * "shutdown()"

   Sin embargo, dado que el protocolo SSL (y TLS) tiene su propia
   estructura encima de TCP, la abstracción de los sockets SSL puede,
   en ciertos aspectos, divergir de la especificación de los sockets
   normales a nivel de SO. Ver especialmente las notas sobre sockets
   no bloqueantes.

   Instancias de "SSLSocket" deben ser creadas usando el método
   "SSLContext.wrap_socket()".

   Distinto en la versión 3.5: El método "sendfile()" ha sido
   agregado.

   Distinto en la versión 3.5: The "shutdown()" does not reset the
   socket timeout each time bytes are received or sent. The socket
   timeout is now the maximum total duration of the shutdown.

   Obsoleto desde la versión 3.6: Crear una instancia de "SSLSocket"
   directamente es obsoleto, utilice "SSLContext.wrap_socket()" para
   envolver un socket.

   Distinto en la versión 3.7: "SSLSocket" instances must be created
   with "wrap_socket()". In earlier versions, it was possible to
   create instances directly. This was never documented or officially
   supported.

   Distinto en la versión 3.10: Python ahora usa "SSL_read_ex" y
   "SSL_write_ex" internamente. Las funciones admiten la lectura y
   escritura de datos de más de 2 GB. La escritura de datos de
   longitud cero ya no falla con un error de violación de protocolo.

Los sockets SSL tienen también los siguientes métodos y atributos
adicionales:

SSLSocket.read(len=1024, buffer=None)

   Lee hasta *len* bytes de datos del socket SSL y retorna el
   resultado como una instancia "bytes". Si *buffer* es especificado,
   entonces se lee hacia el búfer en su lugar, y retorna el número de
   bytes leídos.

   Lanza "SSLWantReadError" o "SSLWantWriteError" si el socket es no-
   bloqueante y la lectura se bloquearía.

   Como en cualquier momento es posible una re-negociación, una
   llamada a "read()" también puede provocar operaciones de escritura.

   Distinto en la versión 3.5: The socket timeout is no longer reset
   each time bytes are received or sent. The socket timeout is now the
   maximum total duration to read up to *len* bytes.

   Obsoleto desde la versión 3.6: Utilice "recv()" en lugar de
   "read()".

SSLSocket.write(data)

   Write *data* to the SSL socket and return the number of bytes
   written. The *data* argument must be an object supporting the
   buffer interface.

   Lanza "SSLWantReadError" o "SSLWantWriteError" si el socket es no-
   bloqueante y la escritura se bloquearía.

   Como en cualquier momento es posible una re-negociación, una
   llamada a "write()" también puede provocar operaciones de lectura.

   Distinto en la versión 3.5: The socket timeout is no longer reset
   each time bytes are received or sent. The socket timeout is now the
   maximum total duration to write *data*.

   Obsoleto desde la versión 3.6: Utilice "send()" en lugar de
   "write()".

Nota:

  Los métodos "read()" y "write()" son los métodos de bajo nivel que
  leen y escriben datos no cifrados a nivel de aplicación y los
  descifran/cifran a datos cifrados a nivel de cable. Estos métodos
  requieren una conexión SSL activa, es decir, que se haya completado
  el handshake y no se haya llamado a "SSLSocket.unwrap()".Normalmente
  se deberían utilizar los métodos de la API de sockets como "recv()"
  y "send()" en lugar de estos métodos.

SSLSocket.do_handshake(block=False)

   Realiza el handshake de configuración SSL.

   If *block* is true and the timeout obtained by "gettimeout()" is
   zero, the socket is set in blocking mode until the handshake is
   performed.

   Distinto en la versión 3.4: The handshake method also performs
   "match_hostname()" when the "check_hostname" attribute of the
   socket's "context" is true.

   Distinto en la versión 3.5: The socket timeout is no longer reset
   each time bytes are received or sent. The socket timeout is now the
   maximum total duration of the handshake.

   Distinto en la versión 3.7: Hostname or IP address is matched by
   OpenSSL during handshake. The function "match_hostname()" is no
   longer used. In case OpenSSL refuses a hostname or IP address, the
   handshake is aborted early and a TLS alert message is sent to the
   peer.

SSLSocket.getpeercert(binary_form=False)

   Si no hay un certificado para el peer en el otro extremo de la
   conexión, retorna "None". Si el handshake SSL no se ha realizado
   todavía, lanza "ValueError".

   Si el parámetro "binary_form" es "False", y se ha recibido un
   certificado del peer, este método retorna una instancia "dict". Si
   el certificado no fue validado, el dict está vacío. Si el
   certificado fue validado, retorna un dict con varias claves, entre
   ellas "subject" (la entidad para la que se emitió el certificado) y
   "issuer" (la entidad que emite el certificado). Si un certificado
   contiene una instancia de la extensión *Subject Alternative Name*
   (véase **RFC 3280**), también habrá una clave "subjectAltName" en
   el diccionario.

   Los campos "subject" y "issuer" son tuplas que contienen la
   secuencia de nombres distinguidos relativos (RDNs) indicados en la
   estructura de datos del certificado para los campos respectivos, y
   cada RDN es una secuencia de pares nombre-valor. Este es un ejemplo
   del mundo real:

      {'issuer': ((('countryName', 'IL'),),
                  (('organizationName', 'StartCom Ltd.'),),
                  (('organizationalUnitName',
                    'Secure Digital Certificate Signing'),),
                  (('commonName',
                    'StartCom Class 2 Primary Intermediate Server CA'),)),
       'notAfter': 'Nov 22 08:15:19 2013 GMT',
       'notBefore': 'Nov 21 03:09:52 2011 GMT',
       'serialNumber': '95F0',
       'subject': ((('description', '571208-SLe257oHY9fVQ07Z'),),
                   (('countryName', 'US'),),
                   (('stateOrProvinceName', 'California'),),
                   (('localityName', 'San Francisco'),),
                   (('organizationName', 'Electronic Frontier Foundation, Inc.'),),
                   (('commonName', '*.eff.org'),),
                   (('emailAddress', 'hostmaster@eff.org'),)),
       'subjectAltName': (('DNS', '*.eff.org'), ('DNS', 'eff.org')),
       'version': 3}

   Si el parámetro "binary_form" es "True", y se proporcionó un
   certificado, este método retorna la forma codificada en DER del
   certificado completo como una secuencia de bytes, o "None" si el
   par no proporcionó un certificado. El hecho de que el par
   proporcione un certificado depende del rol del socket SSL:

   * para un socket SSL cliente, el servidor siempre proporcionará un
     certificado, independientemente de si se requirió la validación;

   * para un socket SSL servidor, el cliente sólo proporcionará un
     certificado cuando lo solicite el servidor; por lo tanto
     "getpeercert()" devolverá "None" si ha utilizado "CERT_NONE" (en
     lugar de "CERT_OPTIONAL" o "CERT REQUIRED").

   See also "SSLContext.check_hostname".

   Distinto en la versión 3.2: El diccionario retornado incluye
   elementos adicionales tales como "issuer" y "notBefore".

   Distinto en la versión 3.4: "ValueError" se lanza cuando no se
   realiza el handshake. El diccionario retornado incluye elementos de
   extensión X509v3 adicionales como "crlDistributionPoints",
   "caIssuers" y "OCSP" URIs.

   Distinto en la versión 3.9: Las cadenas de direcciones IPv6 ya no
   tienen una nueva línea al final.

SSLSocket.get_verified_chain()

   Returns verified certificate chain provided by the other end of the
   SSL channel as a list of DER-encoded bytes. If certificate
   verification was disabled method acts the same as
   "get_unverified_chain()".

   Added in version 3.13.

SSLSocket.get_unverified_chain()

   Returns raw certificate chain provided by the other end of the SSL
   channel as a list of DER-encoded bytes.

   Added in version 3.13.

SSLSocket.cipher()

   Retorna una tupla de tres valores que contiene el nombre del
   cifrado que se está utilizando, la versión del protocolo SSL que
   define su uso y el número de bits secretos que se están utilizando.
   Si no se ha establecido ninguna conexión, retorna "None".

SSLSocket.shared_ciphers()

   Return the list of ciphers available in both the client and server.
   Each entry of the returned list is a three-value tuple containing
   the name of the cipher, the version of the SSL protocol that
   defines its use, and the number of secret bits the cipher uses.
   "shared_ciphers()" returns "None" if no connection has been
   established or the socket is a client socket.

   Added in version 3.5.

SSLSocket.compression()

   Retorna el algoritmo de compresión utilizado como una cadena de
   caracteres, o "None" si la conexión no está comprimida.

   Si el protocolo de nivel superior soporta su propio mecanismo de
   compresión, puede utilizar "OP_NO_COMPRESSION" para desactivar la
   compresión a nivel de SSL.

   Added in version 3.3.

SSLSocket.get_channel_binding(cb_type='tls-unique')

   Obtiene los datos de enlace del canal para la conexión actual, como
   un objeto bytes. Retorna "None" si no está conectado o no se ha
   completado el handshake.

   El parámetro *cb_type* permite seleccionar el tipo de enlace de
   canal deseado. Los tipos de enlace de canal válidos se enumeran en
   la lista "CHANNEL_BINDING_TYPES". Actualmente, sólo se admite la
   vinculación de canal 'tls-unique', definida por **RFC 5929**.
   "ValueError" se lanzará si se solicita un tipo de vinculación de
   canal no admitido.

   Added in version 3.3.

SSLSocket.selected_alpn_protocol()

   Retorna el protocolo que fue seleccionado durante el handshake TLS.
   Si no se ha llamado a "SSLContext.set_alpn_protocols()", si la otra
   parte no soporta ALPN, si este socket no soporta ninguno de los
   protocolos propuestos por el cliente, o si el handshake no ha
   ocurrido todavía, se retorna "None".

   Added in version 3.5.

SSLSocket.selected_npn_protocol()

   Retorna el protocolo de nivel superior que se seleccionó durante el
   handshake TLS/SSL. Si no se llamó a
   "SSLContext.set_npn_protocols()", o si la otra parte no soporta
   NPN, o si el handshake aún no ha ocurrido, esto devolverá "None".

   Added in version 3.3.

   Obsoleto desde la versión 3.10: NPN ha sido reemplazada por ALPN

SSLSocket.unwrap()

   Realiza el handshake de cierre de SSL, que elimina la capa TLS del
   socket subyacente, y retorna el objeto socket subyacente. Esto
   puede utilizarse para pasar de una operación encriptada sobre una
   conexión a una sin encriptar. El socket retornado debe utilizarse
   siempre para la comunicación posterior con el otro lado de la
   conexión, en lugar del socket original.

SSLSocket.verify_client_post_handshake()

   Solicita la autenticación post-handshake (PHA) de un cliente TLS
   1.3. PHA sólo puede iniciarse para una conexión TLS 1.3 desde un
   socket del lado del servidor, después del handshake TLS inicial y
   con PHA habilitado en ambos lados, ver
   "SSLContext.post_handshake_auth".

   El método no realiza un intercambio de certificados inmediatamente.
   El lado del servidor envía una CertificateRequest durante el
   siguiente evento de escritura y espera que el cliente responda con
   un certificado en el siguiente evento de lectura.

   Si alguna precondición no se cumple (por ejemplo, no es TLS 1.3,
   PHA no está habilitado), se genera un "SSLError".

   Nota:

     Sólo está disponible con OpenSSL 1.1.1 y TLS 1.3 habilitados. Sin
     el soporte de TLS 1.3, el método lanza "NotImplementedError".

   Added in version 3.8.

SSLSocket.version()

   Retorna la versión real del protocolo SSL negociada por la conexión
   como una cadena, o "None" si no se establece una conexión segura.
   Al momento de escribir, los posibles valores de retorno incluyen
   ""SSLv2"", ""SSLv3"", ""TLSv1"", ""TLSv1.1"" y ""TLSv1.2"". Las
   versiones recientes de OpenSSL pueden definir más valores de
   retorno.

   Added in version 3.5.

SSLSocket.pending()

   Retorna el número de bytes ya descifrados disponibles para leer,
   pendientes de la conexión.

SSLSocket.context

   The "SSLContext" object this SSL socket is tied to.

   Added in version 3.2.

SSLSocket.server_side

   Un booleano que es "True" para los sockets del lado del servidor y
   "False" para los sockets del lado del cliente.

   Added in version 3.2.

SSLSocket.server_hostname

   Hostname del servidor: tipo "str", o "None" para el socket del lado
   del servidor o si el hostname no fue especificado en el
   constructor.

   Added in version 3.2.

   Distinto en la versión 3.7: El atributo es ahora siempre texto
   ASCII. Cuando "server_hostname" es un nombre de dominio
   internacionalizado (IDN), este atributo almacena ahora la forma de
   etiqueta A (""xn--pythn-mua.org""), en lugar de la forma de
   etiqueta U (""pythön.org"").

SSLSocket.session

   La "SSLSession" para esta conexión SSL. La sesión está disponible
   para los sockets del lado del cliente y del servidor después de que
   se haya realizado el handshake TLS. Para los sockets del cliente la
   sesión puede ser establecida antes de que "do_handshake()" haya
   sido llamado para reutilizar una sesión.

   Added in version 3.6.

SSLSocket.session_reused

   Added in version 3.6.

## SSL contexts

Added in version 3.2.

Un contexto SSL contiene varios datos más duraderos que las conexiones
SSL individuales, como opciones de configuración SSL, certificado(s) y
clave(s) privada(s). También gestiona un cache de sesiones SSL para
sockets del lado del servidor, para acelerar conexiones repetidas de
los mismos clientes.

class ssl.SSLContext(protocol=None)

   Crea un nuevo contexto SSL. Puede pasar *protocolo* que debe ser
   una de las constantes "PROTOCOL_*" definidas en este módulo. El
   parámetro especifica la versión del protocolo SSL a utilizar.
   Típicamente, el servidor elige una versión particular del
   protocolo, y el cliente debe adaptarse a la elección del servidor.
   La mayoría de las versiones no son interoperables con las demás. Si
   no se especifica, el valor por defecto es "PROTOCOL_TLS";
   proporciona la mayor compatibilidad con otras versiones.

   Esta es una tabla que muestra qué versiones de un cliente (en la
   parte inferior) pueden conectarse a qué versiones de un servidor
   (en la parte superior):

   +--------------------------+--------------+--------------+---------------+-----------+-------------+-------------+
   | *cliente* / **servidor** | **SSLv2**    | **SSLv3**    | **TLS** [3]   | **TLSv1** | **TLSv1.1** | **TLSv1.2** |
   +--------------------------+--------------+--------------+---------------+-----------+-------------+-------------+
   | *SSLv2*                  | si           | no           | no [1]        | no        | no          | no          |
   +--------------------------+--------------+--------------+---------------+-----------+-------------+-------------+
   | *SSLv3*                  | no           | si           | no [2]        | no        | no          | no          |
   +--------------------------+--------------+--------------+---------------+-----------+-------------+-------------+
   | *TLS* (*SSLv23*) [3]     | no [1]       | no [2]       | si            | si        | si          | si          |
   +--------------------------+--------------+--------------+---------------+-----------+-------------+-------------+
   | *TLSv1*                  | no           | no           | si            | si        | no          | no          |
   +--------------------------+--------------+--------------+---------------+-----------+-------------+-------------+
   | *TLSv1.1*                | no           | no           | si            | no        | si          | no          |
   +--------------------------+--------------+--------------+---------------+-----------+-------------+-------------+
   | *TLSv1.2*                | no           | no           | si            | no        | no          | si          |
   +--------------------------+--------------+--------------+---------------+-----------+-------------+-------------+

   -[ Notas a pie de página ]-

   [1] "SSLContext" desactiva SSLv2 con "OP_NO_SSLv2" por defecto.

   [2] "SSLContext" desactiva SSLv3 con "OP_NO_SSLv3" por defecto.

   [3] El protocolo TLS 1.3 estará disponible con "PROTOCOL_TLS" en
       OpenSSL >= 1.1.1. No existe una constante PROTOCOL dedicada
       sólo a TLS 1.3.

   Ver también:

     "create_default_context()" lets the "ssl" module choose security
     settings for a given purpose.

   Distinto en la versión 3.6: The context is created with secure
   default values. The options "OP_NO_COMPRESSION",
   "OP_CIPHER_SERVER_PREFERENCE", "OP_SINGLE_DH_USE",
   "OP_SINGLE_ECDH_USE", "OP_NO_SSLv2", and "OP_NO_SSLv3" (except for
   "PROTOCOL_SSLv3") are set by default. The initial cipher suite list
   contains only "HIGH" ciphers, no "NULL" ciphers and no "MD5"
   ciphers.

   Obsoleto desde la versión 3.10: "SSLContext" sin argumento de
   protocolo está en desuso. La clase de contexto requerirá el
   protocolo "PROTOCOL_TLS_CLIENT" o "PROTOCOL_TLS_SERVER" en el
   futuro.

   Distinto en la versión 3.10: Los conjuntos de cifrado
   predeterminados ahora incluyen solo cifrados AES y ChaCha20 seguros
   con secreto directo y nivel de seguridad 2. Están prohibidas las
   claves RSA y DH con menos de 2048 bits y las claves ECC con menos
   de 224 bits. "PROTOCOL_TLS", "PROTOCOL_TLS_CLIENT" y
   "PROTOCOL_TLS_SERVER" usan TLS 1.2 como versión mínima de TLS.

   Nota:

     "SSLContext" only supports limited mutation once it has been used
     by a connection. Adding new certificates to the internal trust
     store is allowed, but changing ciphers, verification settings, or
     mTLS certificates may result in surprising behavior.

   Nota:

     "SSLContext" is designed to be shared and used by multiple
     connections. Thus, it is thread-safe as long as it is not
     reconfigured after being used by a connection.

Los objetos "SSLContext" tienen los siguientes métodos y atributos:

SSLContext.cert_store_stats()

   Obtiene estadísticas sobre las cantidades de certificados X.509
   cargados, la cantidad de certificados X.509 marcados como
   certificados CA y las listas de revocación de certificados como
   diccionario.

   Ejemplo para un contexto con un certificado CA y otro certificado:

      >>> context.cert_store_stats()
      {'crl': 0, 'x509_ca': 1, 'x509': 2}

   Added in version 3.4.

SSLContext.load_cert_chain(certfile, keyfile=None, password=None)

   Carga una clave privada y el certificado correspondiente. La cadena
   *certfile* debe ser la ruta a un solo archivo en formato PEM que
   contenga el certificado, así como cualquier número de certificados
   de CA necesarios para establecer la autenticidad del certificado.
   La cadena *keyfile*, si está presente, debe apuntar a un archivo
   que contenga la clave privada. De lo contrario, la clave privada
   también se tomará de *certfile*. Consulte la discusión de
   Certificados para obtener más información sobre cómo se almacena el
   certificado en *certfile*.

   El argumento *password* puede ser una función a la que llamar para
   obtener la contraseña para descifrar la clave privada. Sólo se
   llamará si la clave privada está encriptada y se necesita una
   contraseña. Se llamará sin argumentos, y deberá devolver una cadena
   de caracteres, bytes o bytearray. Si el valor retornado es una
   cadena de caracteres, se codificará como UTF-8 antes de utilizarlo
   para descifrar la clave. Alternativamente, se puede suministrar un
   valor de cadena de caracteres, bytes o bytearray directamente como
   argumento *password*. Se ignorará si la clave privada no está
   cifrada y no se necesita una contraseña.

   Si el argumento *password* no es especificado y una contraseña es
   requerida, el mecanismo de solicitud de contraseña incorporado de
   OpenSSL se usará para solicitarle una contraseña al usuario de
   forma interactiva.

   Un "SSLError" es lanzado si la clave privada no coincide con el
   certificado.

   Distinto en la versión 3.3: Nuevo argumento opcional *password*.

SSLContext.load_default_certs(purpose=Purpose.SERVER_AUTH)

   Carga un conjunto de certificados predeterminados de "autoridad de
   certificación" (CA) desde ubicaciones predeterminadas. En Windows,
   carga certificados de CA de los almacenes del sistema "CA" y
   "ROOT". En todos los sistemas llama a
   "SSLContext.set_default_verify_paths()". En el futuro, el método
   también puede cargar certificados de CA desde otras ubicaciones.

   The *purpose* flag specifies what kind of CA certificates are
   loaded. The default settings "Purpose.SERVER_AUTH" loads
   certificates, that are flagged and trusted for TLS web server
   authentication (client side sockets). "Purpose.CLIENT_AUTH" loads
   CA certificates for client certificate verification on the server
   side.

   Added in version 3.4.

SSLContext.load_verify_locations(cafile=None, capath=None, cadata=None)

   Carga un conjunto de certificados de "autoridad de certificación"
   (CA) usados para validar certificados de otros pares cuando
   "verify_mode" es distinto de "CERT_NONE". Debe especificarse al
   menos uno de *cafile* o *capath*.

   Este método puede cargar también listas de revocación de
   certificados (CRLs) en formato PEM o DER. Para poder usar CRLs,
   "SSLContext.verify_flags" debe ser configurado correctamente.

   La cadena de caracteres *cafile*, si está presente, es la ruta a un
   archivo de certificados CA concatenados en formato PEM. Vea la
   discusión de Certificados para más información acerca de como
   organizar los certificados en este archivo.

   The *capath* string, if present, is the path to a directory
   containing several CA certificates in PEM format, following an
   OpenSSL specific layout.

   El objeto *cadata*, si está presente, es una cadena de caracteres
   ASCII de uno o más certificados codificados en PEM o un *bytes-like
   object* de certificados codificados en DER. Al igual que con
   *capath*, las líneas adicionales alrededor de los certificados
   codificados en PEM se ignoran, pero debe haber al menos un
   certificado.

   Distinto en la versión 3.4: Nuevo argumento opcional *cadata*

SSLContext.get_ca_certs(binary_form=False)

   Obtiene una lista de certificados de "autoridad de certificación"
   (CA) cargados. Si el parámetro "binary_form" es "False" cada
   entrada de la lista es un diccionario como la salida de
   "SSLSocket.getpeercert()". En caso contrario, el método retorna una
   lista de certificados codificados con DER. La lista retornada no
   contiene certificados de *capath* a menos que un certificado haya
   sido solicitado y cargado por una conexión SSL.

   Nota:

     Los certificados de un directorio capath no se cargan a menos que
     se hayan utilizado al menos una vez.

   Added in version 3.4.

SSLContext.get_ciphers()

   Obtiene una lista de cifrados habilitados. La lista está en orden
   de prioridad de cifrado. Véase "SSLContext.set_ciphers()".

   Ejemplo:

      >>> ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
      >>> ctx.set_ciphers('ECDHE+AESGCM:!ECDSA')
      >>> ctx.get_ciphers()
      [{'aead': True,
        'alg_bits': 256,
        'auth': 'auth-rsa',
        'description': 'ECDHE-RSA-AES256-GCM-SHA384 TLSv1.2 Kx=ECDH     Au=RSA  '
                       'Enc=AESGCM(256) Mac=AEAD',
        'digest': None,
        'id': 50380848,
        'kea': 'kx-ecdhe',
        'name': 'ECDHE-RSA-AES256-GCM-SHA384',
        'protocol': 'TLSv1.2',
        'strength_bits': 256,
        'symmetric': 'aes-256-gcm'},
       {'aead': True,
        'alg_bits': 128,
        'auth': 'auth-rsa',
        'description': 'ECDHE-RSA-AES128-GCM-SHA256 TLSv1.2 Kx=ECDH     Au=RSA  '
                       'Enc=AESGCM(128) Mac=AEAD',
        'digest': None,
        'id': 50380847,
        'kea': 'kx-ecdhe',
        'name': 'ECDHE-RSA-AES128-GCM-SHA256',
        'protocol': 'TLSv1.2',
        'strength_bits': 128,
        'symmetric': 'aes-128-gcm'}]

   Added in version 3.6.

SSLContext.set_default_verify_paths()

   Carga un conjunto de certificados de "autoridad de certificación"
   (CA) por defecto desde una ruta del sistema de archivos definida al
   construir la biblioteca OpenSSL. Desafortunadamente, no hay una
   manera fácil de saber si este método tiene éxito: no se retorna
   ningún error si no se encuentran certificados. Sin embargo, cuando
   la biblioteca OpenSSL se proporciona como parte del sistema
   operativo, es probable que esté configurada correctamente.

SSLContext.set_ciphers(ciphers, /)

   Set the available ciphers for sockets created with this context. It
   should be a string in the OpenSSL cipher list format. If no cipher
   can be selected (because compile-time options or other
   configuration forbids use of all the specified ciphers), an
   "SSLError" will be raised.

   Nota:

     cuando se conecta, el método "SSLSocket.cipher()" de los sockets
     SSL dará el cifrado actualmente seleccionado.OpenSSL 1.1.1 tiene
     suites de cifrado TLS 1.3 habilitadas por defecto. Las suites no
     se pueden desactivar con "set_ciphers()".

SSLContext.set_alpn_protocols(alpn_protocols)

   Especifica qué protocolos debe anunciar el socket durante el
   handshake SSL/TLS. Debe ser una lista de cadenas de caracteres
   ASCII, como "['http/1.1', 'spdy/2']", ordenadas por preferencia. La
   selección de un protocolo ocurrirá durante el handshake, y se
   desarrollará de acuerdo con **RFC 7301**. Después de un handshake
   exitoso, el método "SSLSocket.selected_alpn_protocol()" devolverá
   el protocolo acordado.

   Este método lanzará "NotImplementedError" si "HAS_ALPN" es "False".

   Added in version 3.5.

SSLContext.set_npn_protocols(npn_protocols)

   Especifica qué protocolos debe anunciar el socket durante el
   handshake SSL/TLS. Debe ser una lista de cadenas, como
   "['http/1.1', 'spdy/2']", ordenadas por preferencia. La selección
   de un protocolo ocurrirá durante el handshake, y se desarrollará de
   acuerdo a la Negociación del Protocolo de la Capa de Aplicación.
   Después de un handshake exitoso, el método
   "SSLSocket.selected_npn_protocol()" devolverá el protocolo
   acordado.

   Este método lanzará "NotImplementedError" si "HAS_NPN" es "False".

   Added in version 3.3.

   Obsoleto desde la versión 3.10: NPN ha sido reemplazada por ALPN

SSLContext.sni_callback

   Registra una función callback que se llamará después de que el
   servidor SSL/TLS haya recibido el mensaje de diálogo TLS Client
   Hello cuando el cliente TLS especifique una indicación de nombre de
   servidor. El mecanismo de indicación de nombre de servidor se
   especifica en **RFC 6066** sección 3 - Server Name Indication.

   Sólo se puede establecer una función callback por "SSLContext". Si
   *sni_callback* se establece como "None", la función callback se
   desactiva. Si se llama a esta función una vez más, se desactivará
   la función callback registrada anteriormente.

   La función callback será llamada con tres argumentos; el primero es
   el "ssl.SSLSocket", el segundo es una cadena que representa el
   nombre del servidor con el que el cliente pretende comunicarse (o
   "None" si el TLS Client Hello no contiene un nombre de servidor) y
   el tercer argumento es el "SSLContext" original. El argumento del
   nombre del servidor es un texto. En el caso de los nombres de
   dominio internacionalizados, el nombre del servidor es un IDN
   etiqueta A (""xn--pythn-mua.org"").

   Un uso típico de esta función callback es cambiar el atributo
   "SSLSocket.context" de "ssl.SSLSocket" por un nuevo objeto de tipo
   "SSLContext" que representa una cadena de certificados que coincide
   con el nombre del servidor.

   Due to the early negotiation phase of the TLS connection, only
   limited methods and attributes are usable like
   "SSLSocket.selected_alpn_protocol()" and "SSLSocket.context". The
   "SSLSocket.getpeercert()", "SSLSocket.get_verified_chain()",
   "SSLSocket.get_unverified_chain()" "SSLSocket.cipher()" and
   "SSLSocket.compression()" methods require that the TLS connection
   has progressed beyond the TLS Client Hello and therefore will not
   return meaningful values nor can they be called safely.

   La función *sni_callback* debe devolver "None" para permitir que la
   negociación TLS continúe. Si se requiere un fallo TLS, se puede
   devolver una constante "ALERT_DESCRIPTION_*". Otros valores de
   retorno resultarán en un error fatal TLS con
   "ALERT_DESCRIPTION_INTERNAL_ERROR".

   Si se lanza una excepción desde la función *sni_callback* la
   conexión TLS terminará con un mensaje de alerta TLS fatal
   "ALERT_DESCRIPTION_HANDSHAKE_FAILURE".

   Este método lanzará "NotImplementedError" si la biblioteca OpenSSL
   tenía definido OPENSSL_NO_TLSEXT cuando se construyó.

   Added in version 3.7.

SSLContext.set_servername_callback(server_name_callback)

   Se trata de una API heredada que se mantiene por compatibilidad con
   versiones anteriores. Cuando sea posible, debería utilizar
   "sni_callback" en su lugar. El *server_name_callback* dado es
   similar a *sni_callback*, excepto que cuando el nombre del servidor
   es un nombre de dominio internacionalizado codificado con IDN, el
   *server_name_callback* recibe una etiqueta U decodificada
   (""pythön.org"").

   If there is a decoding error on the server name, the TLS connection
   will terminate with an "ALERT_DESCRIPTION_INTERNAL_ERROR" fatal TLS
   alert message to the client.

   Added in version 3.4.

SSLContext.load_dh_params(dhfile, /)

   Carga los parámetros de generación de claves para el intercambio de
   claves Diffie-Hellman (DH). El uso del intercambio de claves DH
   mejora el secreto hacia adelante a expensas de recursos
   computacionales (tanto en el servidor como en el cliente). El
   parámetro *dhfile* debe ser la ruta de un archivo que contenga los
   parámetros DH en formato PEM.

   Esta configuración no se aplica a los sockets de los clientes.
   También puede utilizar la opción "OP_SINGLE_DH_USE" para mejorar
   aún más la seguridad.

   Added in version 3.3.

SSLContext.set_ecdh_curve(curve_name, /)

   Establece el nombre de la curva para el intercambio de claves
   Diffie-Hellman basado en la curva elíptica (ECDH). ECDH es
   significativamente más rápido que el DH normal, aunque podría
   decirse que es igual de seguro. El parámetro *curve_name* debe ser
   una cadena que describa una curva elíptica conocida, por ejemplo
   "prime256v1" para una curva ampliamente soportada.

   Esta configuración no se aplica a los sockets de los clientes.
   También puede utilizar la opción "OP_SINGLE_ECDH_USE" para mejorar
   aún más la seguridad.

   Este método no está disponible si "HAS_ECDH" es "False".

   Added in version 3.3.

   Ver también:

     SSL/TLS & Perfect Forward Secrecy
        Vincent Bernat.

SSLContext.wrap_socket(sock, server_side=False, do_handshake_on_connect=True, suppress_ragged_eofs=True, server_hostname=None, session=None)

   Wrap an existing Python socket *sock* and return an instance of
   "SSLContext.sslsocket_class" (default "SSLSocket"). The returned
   SSL socket is tied to the context, its settings and certificates.
   *sock* must be a "SOCK_STREAM" socket; other socket types are
   unsupported.

   El parámetro "server_side" es un booleano que identifica si se
   desea un comportamiento del lado del servidor o del lado del
   cliente en este socket.

   Para los sockets del lado del cliente, la construcción del contexto
   es perezosa; si el socket subyacente no está conectado todavía, la
   construcción del contexto se realizará después de llamar a
   "connect()" en el socket. Para los sockets del lado del servidor,
   si el socket no tiene un par remoto, se asume que es un socket a la
   escucha, y la envoltura SSL del lado del servidor se realiza
   automáticamente en las conexiones del cliente aceptadas a través
   del método "accept()". El método puede lanzar "SSLError".

   En las conexiones de cliente, el parámetro opcional
   *server_hostname* especifica el nombre del servicio al que nos
   estamos conectando. Esto permite que un único servidor aloje varios
   servicios basados en SSL con certificados distintos, de forma
   similar a los hosts virtuales HTTP. Al especificar
   *server_hostname* se producirá un "ValueError" si *server_side* es
   verdadero.

   El parámetro "do_handshake_on_connect" especifica si se hace el
   handshake SSL automáticamente después de hacer un
   "socket.connect()", o si el programa de aplicación lo llamará
   explícitamente, invocando el método "SSLSocket.do_handshake()".
   Llamar explícitamente a "SSLSocket.do_handshake()" da al programa
   el control sobre el comportamiento de bloqueo de la E/S del socket
   involucrada en el handshake.

   El parámetro "suppress_ragged_eofs" especifica cómo el método
   "SSLSocket.recv()" debe señalar los EOF inesperados desde el otro
   extremo de la conexión. Si se especifica como "True" (el valor por
   defecto), retorna un EOF normal (un objeto bytes vacío) en
   respuesta a los errores EOF inesperados que se produzcan desde el
   socket subyacente; si "False", lanzará las excepciones al llamador.

   *session*, véase "session".

   To wrap an "SSLSocket" in another "SSLSocket", use
   "SSLContext.wrap_bio()".

   Distinto en la versión 3.5: Siempre permite pasar un
   server_hostname, incluso si OpenSSL no tiene SNI.

   Distinto en la versión 3.6: Se agregó el argumento *session*.

   Distinto en la versión 3.7: El método retorna una instancia de
   "SSLContext.sslsocket_class" en lugar de "SSLSocket" codificado de
   forma rígida.

SSLContext.sslsocket_class

   The return type of "SSLContext.wrap_socket()", defaults to
   "SSLSocket". The attribute can be assigned to on instances of
   "SSLContext" in order to return a custom subclass of "SSLSocket".

   Added in version 3.7.

SSLContext.wrap_bio(incoming, outgoing, server_side=False, server_hostname=None, session=None)

   Envuelve los objetos BIO *incoming* y *outgoing* y retorna una
   instancia de "SSLContext.sslobject_class" (por defecto
   "SSLObject"). Las rutinas SSL leerán los datos de entrada de la BIO
   entrante y escribirán los datos en la BIO saliente.

   Los parámetros *server_side*, *server_hostname* y *session* tienen
   el mismo significado que en "SSLContext.wrap_socket()".

   Distinto en la versión 3.6: Se agregó el argumento *session*.

   Distinto en la versión 3.7: El método retorna una instancia de
   "SSLContext.sslobject_class" en lugar de "SSLObject" codificado de
   forma rígida.

SSLContext.sslobject_class

   El tipo de retorno de "SSLContext.wrap_bio()", por defecto es
   "SSLObject". El atributo puede anularse en la instancia de la clase
   para devolver una subclase personalizada de "SSLObject".

   Added in version 3.7.

SSLContext.session_stats()

   Get statistics about the SSL sessions created or managed by this
   context. A dictionary is returned which maps the names of each
   piece of information to their numeric values.  For example, here is
   the total number of hits and misses in the session cache since the
   context was created:

      >>> stats = context.session_stats()
      >>> stats['hits'], stats['misses']
      (0, 0)

SSLContext.check_hostname

   Si debe coincidir con el nombre de host del certificado de pares en
   "SSLSocket.do_handshake()". El "verify_mode" del contexto debe
   establecerse en "CERT_OPTIONAL" o "CERT_REQUIRED", y debe pasar
   *server_hostname* a "wrap_socket()" para que coincida con el nombre
   de host. La activación de la comprobación del nombre de host
   configura automáticamente "verify_mode" de "CERT_NONE" a
   "CERT_REQUIRED". No se puede volver a establecer en "CERT_NONE"
   siempre que la comprobación del nombre de host esté habilitada. El
   protocolo "PROTOCOL_TLS_CLIENT" habilita la verificación del nombre
   de host de forma predeterminada. Con otros protocolos, la
   verificación del nombre de host debe habilitarse explícitamente.

   Ejemplo:

      import socket, ssl

      context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
      context.verify_mode = ssl.CERT_REQUIRED
      context.check_hostname = True
      context.load_default_certs()

      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      ssl_sock = context.wrap_socket(s, server_hostname='www.verisign.com')
      ssl_sock.connect(('www.verisign.com', 443))

   Added in version 3.4.

   Distinto en la versión 3.7: "verify_mode" ahora se cambia
   automáticamente a "CERT_REQUIRED" cuando la comprobación del
   hostname está activada y "verify_mode" es "CERT_NONE".
   Anteriormente la misma operación habría fallado con un
   "ValueError".

SSLContext.keylog_filename

   Escribe las claves TLS en un archivo keylog, siempre que se genere
   o reciba material de claves. El archivo keylog está diseñado
   únicamente para fines de depuración. El formato del archivo está
   especificado por NSS y es utilizado por muchos analizadores de
   tráfico como Wireshark. El archivo de registro se abre en modo sólo
   añadir. Las escrituras se sincronizan entre hilos, pero no entre
   procesos.

   Added in version 3.8.

SSLContext.maximum_version

   A "TLSVersion" enum member representing the highest supported TLS
   version. The value defaults to "TLSVersion.MAXIMUM_SUPPORTED". The
   attribute is read-only for protocols other than "PROTOCOL_TLS",
   "PROTOCOL_TLS_CLIENT", and "PROTOCOL_TLS_SERVER".

   The attributes "maximum_version", "minimum_version" and
   "SSLContext.options" all affect the supported SSL and TLS versions
   of the context. The implementation does not prevent invalid
   combinations. For example a context with "OP_NO_TLSv1_2" in
   "options" and "maximum_version" set to "TLSVersion.TLSv1_2" will
   not be able to establish a TLS 1.2 connection.

   Added in version 3.7.

SSLContext.minimum_version

   Igual que "SSLContext.maximum_version" excepto que es la versión
   más baja soportada o "TLSVersion.MINIMUM_SUPPORTED".

   Added in version 3.7.

SSLContext.num_tickets

   Control the number of TLS 1.3 session tickets of a
   "PROTOCOL_TLS_SERVER" context. The setting has no impact on TLS 1.0
   to 1.2 connections.

   Added in version 3.8.

SSLContext.options

   Un número entero que representa el conjunto de opciones SSL
   habilitadas en este contexto. El valor por defecto es "OP_ALL",
   pero se pueden especificar otras opciones como "OP_NO_SSLv2"
   mediante la combinación OR.

   Distinto en la versión 3.6: "SSLContext.options" retorna opciones
   "Options":

   >>> ssl.create_default_context().options
   <Options.OP_ALL|OP_NO_SSLv3|OP_NO_SSLv2|OP_NO_COMPRESSION: 2197947391>

   Obsoleto desde la versión 3.7: Esta opción es obsoleta desde
   OpenSSL 1.1.0, utilice en su lugar los nuevos
   "SSLContext.minimum_version" y "SSLContext.maximum_version".

SSLContext.post_handshake_auth

   Habilita la autenticación del cliente TLS 1.3 post-handshake. La
   autenticación post-handshake está deshabilitada por defecto y un
   servidor sólo puede solicitar un certificado de cliente TLS durante
   el handshake inicial. Cuando se habilita, un servidor puede
   solicitar un certificado de cliente TLS en cualquier momento
   después del handshake.

   Cuando se activa en los sockets del lado del cliente, el cliente
   indica al servidor que soporta la autenticación post-handshake.

   Cuando se activa en los sockets del lado del servidor,
   "SSLContext.verify_mode" debe establecerse también como
   "CERT_OPTIONAL" o "CERT_REQUIRED". El intercambio real de
   certificados del cliente se retrasa hasta que se llama a
   "SSLSocket.verify_client_post_handshake()" y se realiza alguna E/S.

   Added in version 3.8.

SSLContext.protocol

   La versión del protocolo elegida cuando se construyó el contexto.
   Este atributo es de sólo lectura.

SSLContext.hostname_checks_common_name

   Si "check_hostname" vuelve a verificar el nombre común del sujeto
   del certificado en ausencia de una extensión de nombre alternativo
   del sujeto (por defecto: true).

   Added in version 3.7.

   Distinto en la versión 3.10: The flag had no effect with OpenSSL
   before version 1.1.1l. Python 3.8.9, 3.9.3, and 3.10 include
   workarounds for previous versions.

SSLContext.security_level

   An integer representing the security level for the context. This
   attribute is read-only.

   Added in version 3.10.

SSLContext.verify_flags

   Los indicadores para las operaciones de verificación de
   certificados. Se pueden establecer indicadores como
   "VERIFY_CRL_CHECK_LEAF" mediante la combinación OR. Por defecto,
   OpenSSL no requiere ni verifica las listas de revocación de
   certificados (CRL). Disponible sólo con la versión 0.9.8+ de
   openssl.

   Added in version 3.4.

   Distinto en la versión 3.6: "SSLContext.verify_flags" retorna
   opciones "VerifyFlags":

   >>> ssl.create_default_context().verify_flags
   <VerifyFlags.VERIFY_X509_TRUSTED_FIRST: 32768>

SSLContext.verify_mode

   Si se intenta verificar los certificados de otros pares y cómo
   comportarse si la verificación falla. Este atributo debe ser uno de
   los siguientes: "CERT_NONE", "CERT_OPTIONAL" o "CERT_REQUIRED".

   Distinto en la versión 3.6: "SSLContext.verify_mode" retorna
   "VerifyMode" enum:

   >>> ssl.create_default_context().verify_mode
   <VerifyMode.CERT_REQUIRED: 2>

SSLContext.set_psk_client_callback(callback)

   Enables TLS-PSK (pre-shared key) authentication on a client-side
   connection.

   In general, certificate based authentication should be preferred
   over this method.

   The parameter "callback" is a callable object with the signature:
   "def callback(hint: str | None) -> tuple[str | None, bytes]". The
   "hint" parameter is an optional identity hint sent by the server.
   The return value is a tuple in the form (client-identity, psk).
   Client-identity is an optional string which may be used by the
   server to select a corresponding PSK for the client. The string
   must be less than or equal to "256" octets when UTF-8 encoded. PSK
   is a *bytes-like object* representing the pre-shared key. Return a
   zero length PSK to reject the connection.

   Setting "callback" to "None" removes any existing callback.

   Nota:

     When using TLS 1.3:

     * the "hint" parameter is always "None".

     * client-identity must be a non-empty string.

   Example usage:

      context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
      context.check_hostname = False
      context.verify_mode = ssl.CERT_NONE
      context.maximum_version = ssl.TLSVersion.TLSv1_2
      context.set_ciphers('PSK')

      # A simple lambda:
      psk = bytes.fromhex('c0ffee')
      context.set_psk_client_callback(lambda hint: (None, psk))

      # A table using the hint from the server:
      psk_table = { 'ServerId_1': bytes.fromhex('c0ffee'),
                    'ServerId_2': bytes.fromhex('facade')
      }
      def callback(hint):
          return 'ClientId_1', psk_table.get(hint, b'')
      context.set_psk_client_callback(callback)

   This method will raise "NotImplementedError" if "HAS_PSK" is
   "False".

   Added in version 3.13.

SSLContext.set_psk_server_callback(callback, identity_hint=None)

   Enables TLS-PSK (pre-shared key) authentication on a server-side
   connection.

   In general, certificate based authentication should be preferred
   over this method.

   The parameter "callback" is a callable object with the signature:
   "def callback(identity: str | None) -> bytes". The "identity"
   parameter is an optional identity sent by the client which can be
   used to select a corresponding PSK. The return value is a *bytes-
   like object* representing the pre-shared key. Return a zero length
   PSK to reject the connection.

   Setting "callback" to "None" removes any existing callback.

   The parameter "identity_hint" is an optional identity hint string
   sent to the client. The string must be less than or equal to "256"
   octets when UTF-8 encoded.

   Nota:

     When using TLS 1.3 the "identity_hint" parameter is not sent to
     the client.

   Example usage:

      context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
      context.maximum_version = ssl.TLSVersion.TLSv1_2
      context.set_ciphers('PSK')

      # A simple lambda:
      psk = bytes.fromhex('c0ffee')
      context.set_psk_server_callback(lambda identity: psk)

      # A table using the identity of the client:
      psk_table = { 'ClientId_1': bytes.fromhex('c0ffee'),
                    'ClientId_2': bytes.fromhex('facade')
      }
      def callback(identity):
          return psk_table.get(identity, b'')
      context.set_psk_server_callback(callback, 'ServerId_1')

   This method will raise "NotImplementedError" if "HAS_PSK" is
   "False".

   Added in version 3.13.

## Certificados

En general, los certificados forman parte de un sistema de clave
pública/clave privada. En este sistema, a cada *principal* (que puede
ser una máquina, una persona o una organización) se le asigna una
clave de cifrado única de dos partes. Una parte de la clave es pública
y se llama *clave pública*; la otra parte se mantiene en secreto y se
llama *clave privada*. Las dos partes están relacionadas, en el
sentido de que si se cifra un mensaje con una de las partes, se puede
descifrar con la otra parte, y **sólo** con la otra parte.

Un certificado contiene información sobre dos sujetos. Contiene el
nombre de un *sujeto*, y la clave pública del sujeto. También contiene
una declaración de un segundo titular, el *emisor*, de que el sujeto
es quien dice ser, y de que ésta es efectivamente la clave pública del
sujeto. La declaración del emisor está firmada con su clave privada,
que sólo el emisor conoce. Sin embargo, cualquiera puede verificar la
declaración del emisor encontrando la clave pública del emisor,
descifrando la declaración con ella y comparándola con el resto de la
información del certificado. El certificado también contiene
información sobre el periodo de tiempo en el que es válido. Esto se
expresa en dos campos, llamados *notBefore* y *notAfter*.

En el uso de certificados en Python, un cliente o servidor puede
utilizar un certificado para demostrar quién es. El otro lado de una
conexión de red también puede ser requerido para producir un
certificado, y ese certificado puede ser validado a la satisfacción
del cliente o servidor que requiere dicha validación. El intento de
conexión puede configurarse para que lance una excepción si la
validación falla. La validación se realiza automáticamente, por el
subyacente framework OpenSSL; la aplicación no necesita preocuparse de
su mecánica. Sin embargo, la aplicación normalmente necesita
proporcionar conjuntos de certificados para permitir que este proceso
tenga lugar.

Python utiliza archivos para contener certificados. Deben ser
formateados como "PEM" (ver **RFC 1422**), que es una forma codificada
en base-64 envuelta con una línea de cabecera y una línea de pie de
página:

   -----BEGIN CERTIFICATE-----
   ... (certificate in base64 PEM encoding) ...
   -----END CERTIFICATE-----

### Cadenas de certificados

Los archivos de Python que contienen certificados pueden contener una
secuencia de certificados, a veces llamada *cadena de certificados*.
Esta cadena debería empezar con el certificado específico para el
principal que "es" el cliente o servidor, y luego el certificado para
el emisor de ese certificado, y luego el certificado para el emisor de
*ese* certificado, y así sucesivamente hasta llegar a un certificado
que es *auto-firmado*, es decir, un certificado que tiene el mismo
sujeto y emisor, a veces llamado *certificado raíz*. Los certificados
sólo deben concatenarse en el archivo de certificados. Por ejemplo,
supongamos que tenemos una cadena de tres certificados, desde el
certificado de nuestro servidor al certificado de la autoridad de
certificación que firmó nuestro certificado del servidor, hasta el
certificado raíz de la agencia que emitió el certificado de la
autoridad de certificación:

   -----BEGIN CERTIFICATE-----
   ... (certificate for your server)...
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   ... (the certificate for the CA)...
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   ... (the root certificate for the CA's issuer)...
   -----END CERTIFICATE-----

### Certificados CA

Si se requiere la validación del certificado del otro lado de la
conexión, se necesita proporcionar un archivo "CA certs", con las
cadenas de certificados para cada emisor en el que se está dispuesto a
confiar. De nuevo, este archivo sólo contiene estas cadenas
concatenadas. Para la validación, Python utilizará la primera cadena
que encuentre en el archivo que coincida. El archivo de certificados
de la plataforma se puede utilizar llamando a
"SSLContext.load_default_certs()", esto se hace automáticamente con
"create_default_context()".

### Clave y certificado combinados

Often the private key is stored in the same file as the certificate;
in this case, only the "certfile" parameter to
"SSLContext.load_cert_chain()" needs to be passed.  If the private key
is stored with the certificate, it should come before the first
certificate in the certificate chain:

   -----BEGIN RSA PRIVATE KEY-----
   ... (private key in base64 encoding) ...
   -----END RSA PRIVATE KEY-----
   -----BEGIN CERTIFICATE-----
   ... (certificate in base64 PEM encoding) ...
   -----END CERTIFICATE-----

### Certificados auto-firmados

Si va a crear un servidor que proporcione servicios de conexión
encriptada SSL, necesitará adquirir un certificado para ese servicio.
Hay muchas formas de adquirir los certificados adecuados, como comprar
uno a una autoridad de certificación. Otra práctica común es generar
un certificado auto-firmado. La forma más sencilla de hacerlo es con
el paquete OpenSSL, utilizando algo como lo siguiente:

   % openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout cert.pem
   Generating a 1024 bit RSA private key
   .......++++++
   .............................++++++
   writing new private key to 'cert.pem'
   -----
   You are about to be asked to enter information that will be incorporated
   into your certificate request.
   What you are about to enter is what is called a Distinguished Name or a DN.
   There are quite a few fields but you can leave some blank
   For some fields there will be a default value,
   If you enter '.', the field will be left blank.
   -----
   Country Name (2 letter code) [AU]:US
   State or Province Name (full name) [Some-State]:MyState
   Locality Name (eg, city) []:Some City
   Organization Name (eg, company) [Internet Widgits Pty Ltd]:My Organization, Inc.
   Organizational Unit Name (eg, section) []:My Group
   Common Name (eg, YOUR name) []:myserver.mygroup.myorganization.com
   Email Address []:ops@myserver.mygroup.myorganization.com
   %

La desventaja de un certificado auto-firmado es que es su propio
certificado raíz, y nadie más lo tendrá en su caché de certificados
raíz conocidos (y de confianza).

## Ejemplos

### Pruebas de compatibilidad con SSL

Para comprobar la presencia de soporte SSL en una instalación de
Python, el código del usuario debe utilizar el siguiente modismo:

   try:
       import ssl
   except ImportError:
       pass
   else:
       ...  # do something that requires SSL support

### Operación del lado del cliente

Este ejemplo crea un contexto SSL con la configuración de seguridad
recomendada para los sockets del cliente, incluyendo la verificación
automática de certificados:

   >>> context = ssl.create_default_context()

Si prefieres ajustar la configuración de seguridad tú mismo, puedes
crear un contexto desde cero (pero ten en cuenta que podrías no
acertar con la configuración):

   >>> context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
   >>> context.load_verify_locations("/etc/ssl/certs/ca-bundle.crt")

(este fragmento asume que tu sistema operativo coloca un paquete de
todos los certificados CA en "/etc/ssl/certs/ca-bundle.crt"; si no es
así, obtendrá un error y tendrá que ajustar la ubicación)

El protocolo "PROTOCOL_TLS_CLIENT" configura el contexto para la
validación de certificados y la verificación del hostname.
"verify_mode" se establece en "CERT_REQUIRED" y "check_hostname" se
establece en "True". Todos los demás protocolos crean contextos SSL
con valores predeterminados inseguros.

Cuando se utiliza el contexto para conectarse a un servidor,
"CERT_REQUIRED" y "check_hostname" validan el certificado del
servidor: se asegura de que el certificado del servidor se ha firmado
con uno de los certificados de la CA, se comprueba que la firma es
correcta y se verifican otras propiedades como la validez y la
identidad del hostname:

   >>> conn = context.wrap_socket(socket.socket(socket.AF_INET),
   ...                            server_hostname="www.python.org")
   >>> conn.connect(("www.python.org", 443))

A continuación, puede obtener el certificado:

   >>> cert = conn.getpeercert()

La inspección visual muestra que el certificado sí identifica el
servicio deseado (es decir, el host HTTPS "www.python.org"):

   >>> pprint.pprint(cert)
   {'OCSP': ('http://ocsp.digicert.com',),
    'caIssuers': ('http://cacerts.digicert.com/DigiCertSHA2ExtendedValidationServerCA.crt',),
    'crlDistributionPoints': ('http://crl3.digicert.com/sha2-ev-server-g1.crl',
                              'http://crl4.digicert.com/sha2-ev-server-g1.crl'),
    'issuer': ((('countryName', 'US'),),
               (('organizationName', 'DigiCert Inc'),),
               (('organizationalUnitName', 'www.digicert.com'),),
               (('commonName', 'DigiCert SHA2 Extended Validation Server CA'),)),
    'notAfter': 'Sep  9 12:00:00 2016 GMT',
    'notBefore': 'Sep  5 00:00:00 2014 GMT',
    'serialNumber': '01BB6F00122B177F36CAB49CEA8B6B26',
    'subject': ((('businessCategory', 'Private Organization'),),
                (('1.3.6.1.4.1.311.60.2.1.3', 'US'),),
                (('1.3.6.1.4.1.311.60.2.1.2', 'Delaware'),),
                (('serialNumber', '3359300'),),
                (('streetAddress', '16 Allen Rd'),),
                (('postalCode', '03894-4801'),),
                (('countryName', 'US'),),
                (('stateOrProvinceName', 'NH'),),
                (('localityName', 'Wolfeboro'),),
                (('organizationName', 'Python Software Foundation'),),
                (('commonName', 'www.python.org'),)),
    'subjectAltName': (('DNS', 'www.python.org'),
                       ('DNS', 'python.org'),
                       ('DNS', 'pypi.org'),
                       ('DNS', 'docs.python.org'),
                       ('DNS', 'testpypi.org'),
                       ('DNS', 'bugs.python.org'),
                       ('DNS', 'wiki.python.org'),
                       ('DNS', 'hg.python.org'),
                       ('DNS', 'mail.python.org'),
                       ('DNS', 'packaging.python.org'),
                       ('DNS', 'pythonhosted.org'),
                       ('DNS', 'www.pythonhosted.org'),
                       ('DNS', 'test.pythonhosted.org'),
                       ('DNS', 'us.pycon.org'),
                       ('DNS', 'id.python.org')),
    'version': 3}

Ahora que se ha establecido el canal SSL y se ha verificado el
certificado, se puede proceder a hablar con el servidor:

   >>> conn.sendall(b"HEAD / HTTP/1.0\r\nHost: linuxfr.org\r\n\r\n")
   >>> pprint.pprint(conn.recv(1024).split(b"\r\n"))
   [b'HTTP/1.1 200 OK',
    b'Date: Sat, 18 Oct 2014 18:27:20 GMT',
    b'Server: nginx',
    b'Content-Type: text/html; charset=utf-8',
    b'X-Frame-Options: SAMEORIGIN',
    b'Content-Length: 45679',
    b'Accept-Ranges: bytes',
    b'Via: 1.1 varnish',
    b'Age: 2188',
    b'X-Served-By: cache-lcy1134-LCY',
    b'X-Cache: HIT',
    b'X-Cache-Hits: 11',
    b'Vary: Cookie',
    b'Strict-Transport-Security: max-age=63072000; includeSubDomains',
    b'Connection: close',
    b'',
    b'']

Vea la discusión sobre Consideraciones de seguridad más abajo.

### Operación del lado del servidor

Para el funcionamiento del servidor, normalmente necesitarás tener un
certificado de servidor y una clave privada, cada uno en un archivo.
Primero crearás un contexto que contenga la clave y el certificado,
para que los clientes puedan comprobar tu autenticidad. Entonces
abrirás un socket, lo enlazarás a un puerto, llamarás a "listen()" en
él, y empezarás a esperar a que los clientes se conecten:

   import socket, ssl

   context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
   context.load_cert_chain(certfile="mycertfile", keyfile="mykeyfile")

   bindsocket = socket.socket()
   bindsocket.bind(('myaddr.example.com', 10023))
   bindsocket.listen(5)

Cuando un cliente se conecta, llamarás a "accept()" en el socket para
obtener el nuevo socket del otro extremo, y utilizarás el método
"SSLContext.wrap_socket()" del contexto para crear un socket SSL del
lado del servidor para la conexión:

   while True:
       newsocket, fromaddr = bindsocket.accept()
       connstream = context.wrap_socket(newsocket, server_side=True)
       try:
           deal_with_client(connstream)
       finally:
           connstream.shutdown(socket.SHUT_RDWR)
           connstream.close()

Entonces leerás los datos del "connstream" y harás algo con ellos
hasta que hayas terminado con el cliente (o el cliente haya terminado
contigo):

   def deal_with_client(connstream):
       data = connstream.recv(1024)
       # empty data means the client is finished with us
       while data:
           if not do_something(connstream, data):
               # we'll assume do_something returns False
               # when we're finished with client
               break
           data = connstream.recv(1024)
       # finished with client

Y volver a escuchar nuevas conexiones de clientes (por supuesto, un
servidor real probablemente manejaría cada conexión de cliente en un
hilo separado, o pondría los sockets en modo no-bloqueo y usaría un
bucle de eventos).

## Notas sobre los sockets no bloqueantes

Los sockets SSL se comportan de forma ligeramente diferente a los
sockets normales en modo no bloqueante. Cuando se trabaja con sockets
no bloqueantes, hay varias cosas que hay que tener en cuenta:

* La mayoría de los métodos de "SSLSocket" lanzarán
  "SSLWantWriteError" o "SSLWantReadError" en lugar de
  "BlockingIOError" si una operación de E/S se bloquea.
  "SSLWantReadError" se lanzará si es necesaria una operación de
  lectura en el socket subyacente, y "SSLWantWriteError" para una
  operación de escritura en el socket subyacente. Tenga en cuenta que
  los intentos de *escribir* en un socket SSL pueden requerir *leer*
  del socket subyacente primero, y los intentos de *leer* del socket
  SSL pueden requerir una *escritura* previa en el socket subyacente.

  Distinto en la versión 3.5: En versiones anteriores de Python, el
  método "SSLSocket.send()" devolvía cero en lugar de lanzar
  "SSLWantWriteError" o "SSLWantReadError".

* Llamar a "select()" le indica que se puede leer (o escribir) en el
  socket a nivel del SO, pero no implica que haya suficientes datos en
  la capa superior SSL. Por ejemplo, puede que sólo haya llegado una
  parte de una trama SSL. Por lo tanto, debe estar preparado para
  manejar los fallos de "SSLSocket.recv()" y "SSLSocket.send()", y re-
  intentar después de otra llamada a "select()".

* Por el contrario, dado que la capa SSL tiene su propia estructura,
  un socket SSL puede tener datos disponibles para leer sin que
  "select()" lo sepa. Por lo tanto, debería llamar primero a
  "SSLSocket.recv()" para drenar cualquier dato potencialmente
  disponible, y luego sólo bloquear en una llamada a "select()" si
  todavía es necesario.

  (por supuesto, se aplican disposiciones similares cuando se utilizan
  otras primitivas como "poll()", o las del módulo "selectors")

* El handshake SSL en sí mismo será no bloqueante: el método
  "SSLSocket.do_handshake()" tiene que ser re-intentado hasta que
  regrese con éxito. Aquí hay una sinopsis usando "select()" para
  esperar la disponibilidad del socket:

     while True:
         try:
             sock.do_handshake()
             break
         except ssl.SSLWantReadError:
             select.select([sock], [], [])
         except ssl.SSLWantWriteError:
             select.select([], [sock], [])

Ver también:

  The "asyncio" module supports non-blocking SSL sockets and provides
  a higher level Streams API. It polls for events using the
  "selectors" module and handles "SSLWantWriteError",
  "SSLWantReadError" and "BlockingIOError" exceptions. It runs the SSL
  handshake asynchronously as well.

## Memory BIO support

Added in version 3.5.

Desde que se introdujo el módulo SSL en Python 2.6, la clase
"SSLSocket" ha proporcionado dos áreas de funcionalidad relacionadas
pero distintas:

* Manejo del protocolo SSL

* E/S de red

La API de E/S de red es idéntica a la proporcionada por
"socket.socket", de la que también hereda "SSLSocket". Esto permite
que un socket SSL sea utilizado como un reemplazo de un socket normal,
haciendo que sea muy fácil añadir soporte SSL a una aplicación
existente.

La combinación del manejo del protocolo SSL y la E/S de red suele
funcionar bien, pero hay algunos casos en los que no es así. Un
ejemplo son los frameworks de E/S asíncronos que quieren utilizar un
modelo de multiplexación de E/S diferente al modelo
"selección/consulta de un descriptor de archivo" (basado en la
preparación) que es asumido por "socket.socket" y por las rutinas
internas de E/S de socket de OpenSSL. Esto es principalmente relevante
para plataformas como Windows donde este modelo no es eficiente. Para
este propósito, se proporciona una variante de ámbito reducido de
"SSLSocket" llamada "SSLObject".

class ssl.SSLObject

   Una variante de alcance reducido de "SSLSocket" que representa una
   instancia del protocolo SSL que no contiene ningún método de E/S de
   red. Esta clase suele ser utilizada por los autores de frameworks
   que quieren implementar E/S asíncrona para SSL a través de búfers
   de memoria.

   Esta clase implementa una interfaz sobre un objeto SSL de bajo
   nivel como el implementado por OpenSSL. Este objeto captura el
   estado de una conexión SSL pero no proporciona ninguna E/S de red
   en sí misma. La E/S debe realizarse a través de objetos "BIO"
   separados que son la capa de abstracción de E/S de OpenSSL.

   Esta clase no tiene un constructor público. Se debe crear una
   instancia "SSLObject" utilizando el método "wrap_bio()". Este
   método creará la instancia "SSLObject" y la vinculará a un par de
   BIOs. El BIO *de entrada* se utiliza para pasar los datos de Python
   a la instancia del protocolo SSL, mientras que el BIO *de salida*
   se utiliza para pasar los datos a la inversa.

   Los siguientes métodos son disponibles:

   * "context"

   * "server_side"

   * "server_hostname"

   * "session"

   * "session_reused"

   * "read()"

   * "write()"

   * "getpeercert()"

   * "get_verified_chain()"

   * "get_unverified_chain()"

   * "selected_alpn_protocol()"

   * "selected_npn_protocol()"

   * "cipher()"

   * "shared_ciphers()"

   * "compression()"

   * "pending()"

   * "do_handshake()"

   * "verify_client_post_handshake()"

   * "unwrap()"

   * "get_channel_binding()"

   * "version()"

   En comparación con "SSLSocket", este objeto carece de las
   siguientes características:

   * Cualquier forma de E/S de red; "recv()" y "send()" leen y
     escriben sólo en los búfers subyacentes de "MemoryBIO".

   * No existe la maquinaria *do_handshake_on_connect*. Siempre hay
     que llamar manualmente a "do_handshake()" para iniciar el
     handshake.

   * No hay manejo de *suppress_ragged_eofs*. Todas las condiciones de
     fin de archivo que violan el protocolo se reportan a través de la
     excepción "SSLEOFError".

   * La llamada al método "unwrap()" no retorna nada, a diferencia de
     lo que ocurre con un socket SSL, que retorna el socket
     subyacente.

   * La función callback *server_name_callback* pasada a
     "SSLContext.set_servername_callback()" obtendrá una instancia de
     "SSLObject" en lugar de una instancia de "SSLSocket" como primer
     parámetro.

   Algunas notas relacionadas con el uso de "SSLObject":

   * Toda la E/S en un "SSLObject" es non-blocking. Esto significa
     que, por ejemplo, "read()" lanzará un "SSLWantReadError" si
     necesita más datos de los que la BIO entrante tiene disponibles.

   Distinto en la versión 3.7: "SSLObject" instances must be created
   with "wrap_bio()". In earlier versions, it was possible to create
   instances directly. This was never documented or officially
   supported.

Un SSLObject se comunica con el mundo exterior utilizando búfers de
memoria. La clase "MemoryBIO" proporciona un búfer de memoria que
puede ser utilizado para este propósito. Envuelve un objeto BIO (Basic
IO) de memoria de OpenSSL:

class ssl.MemoryBIO

   Un búfer de memoria que se puede utilizar para pasar datos entre
   Python y una instancia del protocolo SSL.

   pending

      Retorna el número de bytes que se encuentran actualmente en la
      memoria búfer.

   eof

      Un booleano que indica si la memoria BIO es actual en la
      posición de fin de archivo.

   read(n=-1, /)

      Lee hasta *n* bytes del búfer de memoria. Si *n* no se
      especifica o es negativo, se retornan todos los bytes.

   write(buf, /)

      Escribe los bytes de *buf* en la memoria BIO. El argumento *buf*
      debe ser un objeto que soporte el protocolo de búfer.

      El valor de retorno es el número de bytes escritos, que siempre
      es igual a la longitud de *buf*.

   write_eof()

      Escribe un marcador EOF en la memoria BIO. Después de llamar a
      este método, es ilegal llamar a "write()". El atributo "eof" se
      convertirá en verdadero después de que se hayan leído todos los
      datos que hay actualmente en el búfer.

## Sesión SSL

Added in version 3.6.

class ssl.SSLSession

   Objeto sesión usado por "session".

   id

   time

   timeout

   ticket_lifetime_hint

   has_ticket

## Consideraciones de seguridad

### Los mejores valores por defecto

Para el **uso en el cliente**, si no tiene ningún requisito especial
para su política de seguridad, es muy recomendable que utilice la
función "create_default_context()" para crear su contexto SSL. Cargará
los certificados CA de confianza del sistema, habilitará la validación
de certificados y la comprobación del hostname, e intentará elegir una
configuración de protocolo y cifrado razonablemente segura.

Por ejemplo, así es como se utiliza la clase "smtplib.SMTP" para crear
una conexión segura y de confianza con un servidor SMTP:

   >>> import ssl, smtplib
   >>> smtp = smtplib.SMTP("mail.python.org", port=587)
   >>> context = ssl.create_default_context()
   >>> smtp.starttls(context=context)
   (220, b'2.0.0 Ready to start TLS')

Si se necesita un certificado de cliente para la conexión, se puede
añadir con "SSLContext.load_cert_chain()".

Por el contrario, si crea el contexto SSL llamando usted mismo al
constructor "SSLContext", no tendrá activada por defecto la validación
de certificados ni la comprobación de hostname. Si lo hace, lea los
párrafos siguientes para conseguir un buen nivel de seguridad.

### Ajustes manuales

#### Verificación de certificados

When calling the "SSLContext" constructor directly, "CERT_NONE" is the
default.  Since it does not authenticate the other peer, it can be
insecure, especially in client mode where most of the time you would
like to ensure the authenticity of the server you're talking to.
Therefore, when in client mode, it is highly recommended to use
"CERT_REQUIRED".  However, it is in itself not sufficient; you also
have to check that the server certificate, which can be obtained by
calling "SSLSocket.getpeercert()", matches the desired service.  For
many protocols and applications, the service can be identified by the
hostname. This common check is automatically performed when
"SSLContext.check_hostname" is enabled.

Distinto en la versión 3.7: Hostname matchings is now performed by
OpenSSL. Python no longer uses "match_hostname()".

En el modo servidor, si quiere autenticar a sus clientes utilizando la
capa SSL (en lugar de utilizar un mecanismo de autenticación de nivel
superior), también tendrá que especificar "CERT_REQUIRED" y comprobar
de forma similar el certificado del cliente.

#### Versiones del protocolo

Las versiones 2 y 3 de SSL se consideran inseguras y, por lo tanto, su
uso es peligroso. Si desea la máxima compatibilidad entre clientes y
servidores, se recomienda utilizar "PROTOCOL_TLS_CLIENT" o
"PROTOCOL_TLS_SERVER" como versión del protocolo. SSLv2 y SSLv3 están
desactivados por defecto.

   >>> client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
   >>> client_context.minimum_version = ssl.TLSVersion.TLSv1_2
   >>> client_context.maximum_version = ssl.TLSVersion.TLSv1_3

The SSL client context created above will only allow TLSv1.2 and
TLSv1.3 (if supported by your system) connections to a server.
"PROTOCOL_TLS_CLIENT" implies certificate validation and hostname
checks by default. You have to load certificates into the context.

#### Selección de cifrado

If you have advanced security requirements, fine-tuning of the ciphers
enabled when negotiating a SSL session is possible through the
"SSLContext.set_ciphers()" method.  Starting from Python 3.2.3, the
ssl module disables certain weak ciphers by default, but you may want
to further restrict the cipher choice. Be sure to read OpenSSL's
documentation about the cipher list format. If you want to check which
ciphers are enabled by a given cipher list, use
"SSLContext.get_ciphers()" or the "openssl ciphers" command on your
system.

### Multiprocesamiento

If using this module as part of a multi-processed application (using,
for example the "multiprocessing" or "concurrent.futures" modules), be
aware that OpenSSL's internal random number generator does not
properly handle forked processes.  Applications must change the PRNG
state of the parent process if they use any SSL feature with
"os.fork()".  Any successful call of "RAND_add()" or "RAND_bytes()" is
sufficient.

## TLS 1.3

Added in version 3.7.

Python tiene soporte provisional y experimental para TLS 1.3 con
OpenSSL 1.1.1. El nuevo protocolo se comporta de forma ligeramente
diferente a la versión anterior de TLS/SSL. Algunas de las nuevas
características de TLS 1.3 aún no están disponibles.

* TLS 1.3 utiliza un conjunto disjunto de suites de cifrado. Todas las
  suites de cifrado AES-GCM y ChaCha20 están habilitadas por defecto.
  El método "SSLContext.set_ciphers()" aún no puede habilitar o
  deshabilitar ningún cifrado de TLS 1.3, pero
  "SSLContext.get_ciphers()" los retorna.

* Los tickets de sesión ya no se envían como parte del handshake
  inicial y se manejan de forma diferente. "SSLSocket.session" y
  "SSLSession" no son compatibles con TLS 1.3.

* Los certificados del lado del cliente ya no se verifican durante el
  handshake inicial. Un servidor puede solicitar un certificado en
  cualquier momento. Los clientes procesan las solicitudes de
  certificados mientras envían o reciben datos de la aplicación desde
  el servidor.

* Las funciones de TLS 1.3, como los datos anticipados, la solicitud
  de certificado de cliente TLS diferida, la configuración del
  algoritmo de firma y la repetición de claves, aún no son
  compatibles.

Ver también:

  Clase "socket.socket"
     Documentación de la clase "socket" subyacente

  SSL/TLS Strong Encryption: An Introduction
     Introducción de la documentación del servidor HTTP Apache

  **RFC 1422: Privacy Enhancement for Internet Electronic Mail: Part
  II: Certificate-Based Key Management**
     Steve Kent

  **RFC 4086: Randomness Requirements for Security**
     Donald E. Eastlake, Jeffrey I. Schiller, Steve Crocker

  **RFC 5280: Internet X.509 Public Key Infrastructure Certificate and
  Certificate Revocation List (CRL) Profile**
     David Cooper et al.

  **RFC 5246: The Transport Layer Security (TLS) Protocol Version
  1.2**
     Tim Dierks and Eric Rescorla.

  **RFC 6066: Transport Layer Security (TLS) Extensions**
     Donald E. Eastlake

  IANA TLS: Transport Layer Security (TLS) Parameters
     IANA

  **RFC 7525: Recommendations for Secure Use of Transport Layer
  Security (TLS) and Datagram Transport Layer Security (DTLS)**
     IETF

  Mozilla's Server Side TLS recommendations
     Mozilla
