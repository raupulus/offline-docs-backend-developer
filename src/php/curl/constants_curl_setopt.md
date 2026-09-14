---
title: curl_setopt
source_url: https://www.php.net/manual/es/constant.curlopt-abstract-unix-socket.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/constants_curl_setopt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: e7e81a179
order: 9660
---

`CURLOPT_ABSTRACT_UNIX_SOCKET` (`int`)  
Activa el uso de un socket Unix abstracto en lugar de establecer una conexión TCP a un host y define la ruta dada en `string`. Esta opción comparte las mismas semánticas que `CURLOPT_UNIX_SOCKET_PATH`. Ambas opciones comparten el mismo almacenamiento y por lo tanto solo una de ellas puede ser definida por un manejador. Disponible a partir de PHP 7.3.0 y cURL 7.53.0.

`CURLOPT_ACCEPT_ENCODING` (`int`)  
Define un `string` con el contenido del encabezado `Accept-Encoding:` enviado en una solicitud HTTP. Establecer en `null` para desactivar el envío del encabezado `Accept-Encoding:`. Por omisión a `null`. Disponible a partir de cURL 7.21.6.

`CURLOPT_ACCEPTTIMEOUT_MS` (`int`)  
El número máximo de milisegundos a esperar para que un servidor se reconecte a cURL cuando se usa una conexión FTP activa. Por omisión a `60000` milisegundos. Disponible a partir de cURL 7.24.0.

`CURLOPT_ADDRESS_SCOPE` (`int`)  
El identificador de ámbito a usar al conectarse a una dirección IPv6. Esta opción acepta cualquier valor que pueda ser convertido en un `int` válido. Por omisión a `0`. Disponible a partir de cURL 7.19.0.

`CURLOPT_ALTSVC` (`int`)  
Pasar un `string` con el nombre de archivo para que cURL lo use como caché Alt-Svc para leer el contenido de la caché existente y eventualmente reescribirlo después de un transferencia, a menos que `CURLALTSVC_READONLYFILE` esté definido a través de `CURLOPT_ALTSVC_CTRL`. Disponible a partir de PHP 8.2.0 y cURL 7.64.1.

`CURLOPT_ALTSVC_CTRL` (`int`)  
Rellena el bitmask con el conjunto correcto de funcionalidades para indicar a cURL cómo manejar Alt-Svc para los transferencias usando este manejador. cURL solo acepta los encabezados Alt-Svc en HTTPS. También completará una solicitud a un origen alternativo solo si este origen está correctamente alojado en HTTPS. Definir un bit activará el motor alt-svc. Definido en una de las constantes `CURLALTSVC_*`. Por omisión, la gestión Alt-Svc está desactivada. Disponible a partir de PHP 8.2.0 y cURL 7.64.1.

`CURLOPT_APPEND` (`int`)  
Establecer esta opción a `1` hará que las descargas FTP añadan al archivo remoto en lugar de sobrescribirlo. Por omisión a `0`. Disponible a partir de cURL 7.17.0.

`CURLOPT_AUTOREFERER` (`int`)  
`true` para definir automáticamente el campo `Referer:` en las solicitudes donde sigue una redirección `Location:`. Por omisión, el valor es `0`.

`CURLOPT_AWS_SIGV4` (`int`)  
Proporciona autenticación de firma AWS V4 en el encabezado HTTP(S) como `string`. Esta opción reemplaza cualquier otro tipo de autenticación que haya sido definido en `CURLOPT_HTTPAUTH`. Este método no puede combinarse con otros tipos de autenticación. Disponible a partir de PHP 8.2.0 y cURL 7.75.0.

`CURLOPT_BINARYTRANSFER` (`int`)  
Esta constante ya no se usa a partir de PHP 5.5.0. Deprecado a partir de PHP 8.4.0.

`CURLOPT_BUFFERSIZE` (`int`)  
Un tamaño de búfer a usar para cada lectura. No hay garantía de que esta solicitud será satisfecha, sin embargo. Esta opción acepta cualquier valor que pueda ser convertido en un `int` válido. Por omisión, el valor es `CURL_MAX_WRITE_SIZE` (actualmente, 16kB). Disponible a partir de cURL 7.10.

`CURLOPT_CAINFO` (`int`)  
Un `string` con el nombre de un archivo que contiene uno o varios certificados para verificar el par con. Esto solo tiene sentido cuando se usa en combinación con `CURLOPT_SSL_VERIFYPEER`. Puede requerir una ruta absoluta. Disponible a partir de cURL 7.4.2.

`CURLOPT_CAINFO_BLOB` (`int`)  
Un `string` binario con contenido codificado en PEM que contiene uno o varios certificados para verificar el par. Esta opción reemplaza `CURLOPT_CAINFO`. Disponible a partir de PHP 8.2.0 y cURL 7.77.0.

`CURLOPT_CAPATH` (`int`)  
Un `string` con un directorio que contiene varios certificados CA. Use esta opción en combinación con `CURLOPT_SSL_VERIFYPEER`. Disponible a partir de cURL 7.9.8.

`CURLOPT_CA_CACHE_TIMEOUT` (`int`)  
Define el tiempo máximo en segundos durante el cual un almacén de certificados CA almacenado en caché en memoria puede ser conservado y reutilizado para nuevas conexiones. Esta opción acepta cualquier valor que pueda ser convertido en un `int` válido. Por omisión, el valor es `86400` (24 horas). Disponible a partir de PHP 8.3.0 y cURL 7.87.0

`CURLOPT_CERTINFO` (`int`)  
`true` para salir con información sobre el certificado SSL en `STDERR` en transferencias seguras. Requiere `CURLOPT_VERBOSE` para tener efecto. Por omisión, el valor es `false`. Disponible a partir de cURL 7.19.1.

`CURLOPT_CONNECTTIMEOUT` (`int`)  
El número de segundos a esperar al intentar conectarse. Use `0` para esperar indefinidamente. Esta opción acepta cualquier valor que pueda ser convertido en un `int` válido. Por omisión, el valor es `300`. Disponible a partir de cURL 7.7.0.

`CURLOPT_CONNECTTIMEOUT_MS` (`int`)  
El número de milisegundos a esperar al intentar conectarse. Use `0` para esperar indefinidamente. Si cURL está compilado para usar el resolutor de nombres estándar del sistema, esta parte de la conexión siempre usará una resolución a segundo completo para los tiempos de espera con un tiempo de espera mínimo permitido de un segundo. Esta opción acepta cualquier valor que pueda ser convertido en un `int` válido. Por omisión, el valor es `300000`. Disponible a partir de cURL 7.16.2.

`CURLOPT_CONNECT_ONLY` (`int`)  
`true` para indicar a la biblioteca que no realice autenticación de proxy y configuración de conexión requerida, pero no transferencia de datos. Esta opción está implementada para HTTP, SMTP y POP3. Por omisión, el valor es `false`. Disponible a partir de cURL 7.15.2.

`CURLOPT_CONNECT_TO` (`int`)  
Conecta a un host y puerto específicos en lugar del host y puerto de la URL. Acepta un `array` de `string`s en el formato `HOST:PORT:CONNECT-TO-HOST:CONNECT-TO-PORT`. Disponible a partir de PHP 7.0.7 y cURL 7.49.0.

`CURLOPT_COOKIE` (`int`)  
Un `string` con el contenido del encabezado `"Cookie: "` a usar en la solicitud HTTP. Es de notar que múltiples cookies están separadas por un punto y coma seguido de un espacio (por ejemplo, `fruit=apple; colour=red`). Disponible a partir de cURL 7.1.0.

`CURLOPT_COOKIEFILE` (`int`)  
Un `string` con el nombre del archivo que contiene los datos de las cookies. El archivo de cookies puede estar en formato Netscape, o simplemente encabezados HTTP clásicos volcados en un archivo. Si el nombre es una cadena vacía, no se cargan cookies, pero la gestión de cookies sigue activada. Disponible a partir de cURL 7.1.0.

`CURLOPT_COOKIEJAR` (`int`)  
Un `string` con el nombre del archivo para guardar todas las cookies internas cuando el destructor del manejador es llamado. Disponible a partir de cURL 7.9.0.

> [!WARNING]
> A partir de PHP 8.0.0, `curl_close` es una operación nula y no destruye *ningún* manejador. Si las cookies deben ser escritas antes de que el manejador sea destruido automáticamente, ejecute `curl_setopt($ch, CURLOPT_COOKIELIST, "FLUSH");`.

`CURLOPT_COOKIELIST` (`int`)  
Un `string` de cookies (es decir, una sola línea en el formato Netscape/Mozilla, o un encabezado Set-Cookie HTTP regular) añade esta única cookie al almacenamiento interno de cookies. `ALL` borra todas las cookies almacenadas en memoria, `SESS` borra todas las cookies de sesión almacenadas en memoria, `FLUSH` escribe todas las cookies conocidas en el archivo especificado por `CURLOPT_COOKIEJAR`, `RELOAD` carga todas las cookies desde los archivos especificados por `CURLOPT_COOKIEFILE` . Disponible a partir de cURL 7.14.1.

`CURLOPT_COOKIESESSION` (`int`)  
`true` para marcar esto como una nueva "sesión" de cookies. Esto forzará a cURL a ignorar todas las cookies que está a punto de cargar que son "cookies de sesión" de la sesión anterior. Por omisión, cURL almacena y carga siempre todas las cookies, independientemente de si son cookies de sesión o no. Las cookies de sesión son cookies sin fecha de expiración y están destinadas a ser vivas y existentes solo para esta "sesión". Disponible a partir de cURL 7.9.7.

`CURLOPT_CRLF` (`int`)  
`true` para convertir los finales de línea Unix en finales de línea CRLF en las transferencias. Disponible a partir de cURL 7.1.0.

`CURLOPT_CRLFILE` (`int`)  
Pasar un `string` nombrando un archivo con la concatenación de la CRL (Certificate Revocation List) (en formato PEM) para usar en la validación del certificado que ocurre durante el intercambio SSL. Cuando cUrl está compilado para usar GnuTLS, no hay manera de influir en el uso de CRL pasado para ayudar en el proceso de verificación. Cuando cUrl está compilado para usar OpenSSL, `X509_V_FLAG_CRL_CHECK` y `X509_V_FLAG_CRL_CHECK_ALL` están ambos definidos, exigiendo la verificación de la CRL contra todos los elementos de la cadena de certificados si un archivo CRL es pasado. También es de notar que `CURLOPT_CRLFILE` implica `CURLSSLOPT_NO_PARTIALCHAIN` a partir de cURL 7.71.0 debido a un bug de OpenSSL. Disponible a partir de cURL 7.19.0.

`CURLOPT_CUSTOMREQUEST` (`int`)  
Un método de solicitud personalizado a usar en lugar de `GET` o `HEAD` al realizar una solicitud HTTP. Esto es útil para realizar solicitudes HTTP más oscuras como `DELETE` u otras. Los valores válidos son cosas como `GET`, `POST`, `CONNECT` y así sucesivamente; es decir, no ingresar una línea completa de solicitud HTTP aquí. Por ejemplo, ingresar `GET /index.html HTTP/1.0\r\n\r\n` sería incorrecto. Esta opción acepta un `string` o `null`. Disponible a partir de cURL 7.1.0.

> [!NOTE]
> No hacer esto sin asegurarse de que el servidor soporte el método de solicitud personalizado primero.

`CURLOPT_DEFAULT_PROTOCOL` (`int`)  
Un `string` con el protocolo por defecto a usar si la URL carece de un nombre de esquema. Disponible a partir de PHP 7.0.7 y cURL 7.45.0.

`CURLOPT_DIRLISTONLY` (`int`)  
Definir esta opción a `1` para tener efectos diferentes basados en el protocolo con el que se usa. Las URLs basadas en FTP y SFTP solo listarán los nombres de archivos en un directorio. POP3 listará el mensaje o mensajes de correo electrónico en el servidor POP3. Para FILE, esta opción no tiene efecto ya que los directorios siempre se listan en este modo. Usar esta opción con `CURLOPT_WILDCARDMATCH` evitará que este último tenga algún efecto. Por omisión a `0`. Disponible a partir de cURL 7.17.0.

`CURLOPT_DISALLOW_USERNAME_IN_URL` (`int`)  
`true` para no permitir URLs que incluyen un nombre de usuario. Los nombres de usuario están permitidos por omisión. Disponible a partir de PHP 7.3.0 y cURL 7.61.0.

`CURLOPT_DNS_CACHE_TIMEOUT` (`int`)  
El número de segundos para mantener las entradas DNS en memoria. Esta opción está definida por omisión a `120` (2 minutos). Esta opción acepta cualquier valor que pueda ser convertido en un `int` válido. Disponible a partir de cURL 7.9.3.

`CURLOPT_DNS_INTERFACE` (`int`)  
Define el nombre de la interfaz de red a la que el resolutor DNS debe enlazarse. Esto debe ser un nombre de interfaz (no una dirección). Esta opción acepta un `string` o `null`. Disponible a partir de PHP 7.0.7 y cURL 7.33.0

`CURLOPT_DNS_LOCAL_IP4` (`int`)  
Define la dirección IPv4 local a la que el resolutor debe enlazarse. El argumento debe contener una sola dirección IPv4 numérica. Esta opción acepta un `string` o `null`. Disponible a partir de PHP 7.0.7 y cURL 7.33.0.

`CURLOPT_DNS_LOCAL_IP6` (`int`)  
Define la dirección IPv6 local a la que el resolutor debe enlazarse. El argumento debe contener una sola dirección IPv6 numérica. Esta opción acepta un `string` o `null`. Disponible a partir de PHP 7.0.7 y cURL 7.33.0.

`CURLOPT_DNS_SERVERS` (`int`)  
Pasar un `string` con una lista separada por comas de servidores DNS a usar en lugar del sistema por defecto (por ejemplo: `192.168.1.100,192.168.1.101:8080`). Disponible a partir de cURL 7.24.0.

`CURLOPT_DNS_SHUFFLE_ADDRESSES` (`int`)  
`true` para mezclar el orden de todas las direcciones devueltas para que sean usadas en un orden aleatorio, cuando un nombre es resuelto y más de una dirección IP es devuelta. Esto puede resultar en el uso de IPv4 antes que IPv6 o viceversa. Disponible a partir de PHP 7.3.0 y cURL 7.60.0.

`CURLOPT_DNS_USE_GLOBAL_CACHE` (`int`)  
`true` para usar una caché DNS global. Esta opción no es thread-safe. Está activada por omisión si PHP está compilado para uso no threadado (CLI, FCGI, Apache2-Prefork, etc.). Disponible a partir de cURL 7.9.3 y obsoleta a partir de cURL 7.11.1. A partir de PHP 8.4, esta opción ya no tiene ningún efecto.

`CURLOPT_DOH_SSL_VERIFYHOST` (`int`)  
Establecer en `2` para verificar el campo de nombre del certificado SSL del servidor DNS-over-HTTPS en comparación con el nombre de host. Disponible a partir de PHP 8.2.0 y cURL 7.76.0.

`CURLOPT_DOH_SSL_VERIFYPEER` (`int`)  
Establecer en `1` para activar y `0` para desactivar la verificación de la autenticidad del certificado SSL del servidor DNS-over-HTTPS. Disponible a partir de PHP 8.2.0 y cURL 7.76.0.

`CURLOPT_DOH_SSL_VERIFYSTATUS` (`int`)  
Establecer en `1` para activar y `0` para desactivar la verificación del estado del certificado del servidor DNS-over-HTTPS usando la extensión TLS "Certificate Status Request" (OCSP stapling). Disponible a partir de PHP 8.2.0 y cURL 7.76.0.

`CURLOPT_DOH_URL` (`int`)  
Proporciona la URL DNS-over-HTTPS. Esta opción acepta un `string` o `null`. Disponible a partir de PHP 8.1.0 y cURL 7.62.0.

`CURLOPT_EGDSOCKET` (`int`)  
Como `CURLOPT_RANDOM_FILE` excepto que pasas una cadena que contiene un nombre de archivo al socket Entropy Gathering Daemon. Disponible a partir de cURL 7.7.0 y obsoleto a partir de cURL 7.84.0.

`CURLOPT_ENCODING` (`int`)  
El contenido de los encabezados `Accept-Encoding:` como `string`. Esto permite decodificar la respuesta. Los encodings soportados son `identity`, `deflate`, `gzip` . Si una cadena vacía, `string`, es definida, un encabezado que contiene todos los tipos de encoding soportados es enviado. Disponible a partir de cURL 7.10.

`CURLOPT_EXPECT_100_TIMEOUT_MS` (`int`)  
El tiempo de espera para las respuestas `Expect: 100-continue` en milisegundos. Por omisión, `1000` milisegundos. Esta opción acepta cualquier valor que pueda convertirse en un `int` válido. Disponible a partir de PHP 7.0.7 y cURL 7.36.0.

`CURLOPT_FAILONERROR` (`int`)  
`true` para fallar verbalmente si el código HTTP devuelto es superior o igual a `400`. El comportamiento por omisión es devolver la página normalmente, ignorando el código. Disponible a partir de cURL 7.1.0.

`CURLOPT_FILE` (`int`)  
Acepta un descriptor de fichero `resource` hacia el fichero en el que debe escribirse la transferencia. El valor por omisión es `STDOUT` (la ventana del navegador). Disponible a partir de cURL 7.1.0 y obsoleto a partir de cURL 7.9.7.

`CURLOPT_FILETIME` (`int`)  
Definir en `true` para intentar recuperar la fecha de modificación del documento remoto. Este valor puede ser recuperado utilizando la opción `CURLINFO_FILETIME` con `curl_getinfo`. Disponible a partir de cURL 7.5.0.

`CURLOPT_FNMATCH_FUNCTION` (`int`)  
Pasar un `callable` que será utilizado para la correspondencia de caracteres genéricos. La firma de la función de devolución de llamada debe ser:

```php
callback(resource $curlHandle, string $pattern, string $string): int
```php

`curlHandle`  
El manejador cURL.

`pattern`  
La cadena de caracteres genéricos.

`string`  
El `string` sobre el que ejecutar la correspondencia de caracteres genéricos.

La función de devolución de llamada debe devolver `CURL_FNMATCHFUNC_MATCH` si el patrón coincide con el `string`, `CURL_FNMATCHFUNC_NOMATCH` si no es así o `CURL_FNMATCHFUNC_FAIL` si ha ocurrido un error. Disponible a partir de cURL 7.21.0.

`CURLOPT_FOLLOWLOCATION` (`int`)  
Definir en `true` para seguir todos los encabezados `Location:` enviados por el servidor en la respuesta HTTP. Ver también `CURLOPT_MAXREDIRS`. Esta constante no está disponible cuando [open_basedir](#ini.open-basedir) está activado.

`CURLOPT_FORBID_REUSE` (`int`)  
Definir en `true` para forzar el cierre explícito de la conexión cuando el proceso finaliza, por lo que no se almacenará en caché para su reutilización. Disponible a partir de cURL 7.7.0.

`CURLOPT_FRESH_CONNECT` (`int`)  
Definir en `true` para forzar el uso de una nueva conexión en lugar de una conexión almacenada en caché. Disponible a partir de cURL 7.7.0.

`CURLOPT_FTPAPPEND` (`int`)  
Definir en `true` para añadir al fichero remoto en lugar de sobrescribirlo. Disponible a partir de cURL 7.1.0 y obsoleto a partir de cURL 7.16.4.

`CURLOPT_FTPASCII` (`int`)  
Un alias de `CURLOPT_TRANSFERTEXT`. Utilice esto en su lugar. Disponible a partir de cURL 7.1, obsoleto a partir de cURL 7.11.1 y disponible por última vez a partir de cURL 7.15.5. Eliminado a partir de PHP 7.3.0.

`CURLOPT_FTPLISTONLY` (`int`)  
Definir en `true` para solo listar los nombres de un directorio FTP. Disponible a partir de cURL 7.1.0 y obsoleto a partir de cURL 7.16.4.

`CURLOPT_FTPPORT` (`int`)  
Una `string` que se utilizará para obtener la dirección IP a usar para el comando FTP `PORT`. El comando `PORT` indica al servidor remoto que se conecte a nuestra dirección IP especificada. El `string` puede ser una dirección IP simple, un nombre de host, un nombre de interfaz de red (en Unix), o simplemente un `-` para usar la dirección IP por defecto del sistema. Esta opción acepta una `string` o `null`. Disponible a partir de cURL 7.1.0.

`CURLOPT_FTPSSLAUTH` (`int`)  
Definir el método de autenticación FTP sobre SSL (si está activado) en una de las constantes `CURLFTPAUTH_*`. El valor por omisión es `CURLFTPAUTH_DEFAULT`.

`CURLOPT_FTP_ACCOUNT` (`int`)  
Pasar un `string` que será enviado como información de cuenta en FTP (usando el comando `ACCT`) después de que el nombre de usuario y la contraseña hayan sido proporcionados al servidor. Definir en `null` para desactivar el envío de la información de cuenta. Por omisión en `null`. Disponible a partir de cURL 7.13.0.

`CURLOPT_FTP_ALTERNATIVE_TO_USER` (`int`)  
Pasar un `string` que será utilizado para intentar autenticarse en FTP si la negociación `USER/PASS` falla. Disponible a partir de cURL 7.15.5.

`CURLOPT_FTP_CREATE_MISSING_DIRS` (`int`)  
Definir en `true` para crear los directorios faltantes cuando una operación FTP encuentra un camino que actualmente no existe. Disponible a partir de cURL 7.10.7.

`CURLOPT_FTP_FILEMETHOD` (`int`)  
Indica a curl qué método usar para alcanzar un fichero en un servidor FTP(S). Los valores posibles son una de las constantes `CURLFTPMETHOD_*`. El valor por omisión es `CURLFTPMETHOD_MULTICWD`. Disponible a partir de cURL 7.15.1.

`CURLOPT_FTP_RESPONSE_TIMEOUT` (`int`)  
El tiempo de espera en segundos que cURL esperará para una respuesta de un servidor FTP Esta opción reemplaza `CURLOPT_TIMEOUT`. Esta opción acepta cualquier valor que pueda convertirse en un `int` válido. Este nombre de opción es reemplazado por `CURLOPT_SERVER_RESPONSE_TIMEOUT`, disponible a partir de PHP 8.4.0. Disponible a partir de cURL 7.10.8 y deprecado a partir de cURL 7.85.0.

`CURLOPT_FTP_SKIP_PASV_IP` (`int`)  
Si esta opción está definida en `1`, cURL no utilizará la dirección IP que el servidor sugiere en su respuesta 227 al comando `PASV` de cURL sino que utilizará la dirección IP que usó para la conexión. El número de puerto recibido de la respuesta 227 no será ignorado por cURL. Por omisión en `1` a partir de cURL 7.74.0 y `0` antes de eso. Disponible a partir de cURL 7.15.0.

`CURLOPT_FTP_SSL` (`int`)  
Disponible a partir de cURL 7.11.0 y obsoleto a partir de cURL 7.16.4.

`CURLOPT_FTP_SSL_CCC` (`int`)  
Esta opción hace que cURL use CCC (Clear Command Channel) que detiene la capa SSL/TLS después de la autenticación dejando el resto de la comunicación del canal de control sin cifrar. Usar una de las constantes `CURLFTPSSL_CCC_*`. Por omisión en `CURLFTPSSL_CCC_NONE`. Disponible a partir de cURL 7.16.1.

`CURLOPT_FTP_USE_EPRT` (`int`)  
Definir en `true` para usar `EPRT` (y `LPRT`) durante las descargas FTP activas. Definir en `false` para desactivar `EPRT` y `LPRT` y usar solo `PORT`. Disponible a partir de cURL 7.10.5.

`CURLOPT_FTP_USE_EPSV` (`int`)  
Definir en `true` para intentar primero un comando `EPSV` para las transferencias FTP antes de volver a `PASV`. Definir en `false` para desactivar `EPSV`. Disponible a partir de cURL 7.9.2.

`CURLOPT_FTP_USE_PRET` (`int`)  
Definir en `1` para enviar un comando `PRET` antes `PASV` (y `EPSV`). No tiene ningún efecto al usar el modo de transferencia FTP activo. Por omisión en `0`. Disponible a partir de cURL 7.20.0.

`CURLOPT_GSSAPI_DELEGATION` (`int`)  
Definir en `CURLGSSAPI_DELEGATION_FLAG` para permitir la delegación incondicional de las credenciales GSSAPI. Definir en `CURLGSSAPI_DELEGATION_POLICY_FLAG` para delegar solo si la bandera `OK-AS-DELEGATE` está definida en el ticket de servicio. Por omisión en `CURLGSSAPI_DELEGATION_NONE`. Disponible a partir de cURL 7.22.0.

`CURLOPT_HAPPY_EYEBALLS_TIMEOUT_MS` (`int`)  
Un avance para IPv6 para el algoritmo Happy Eyeballs. Happy Eyeballs intenta conectarse tanto a las direcciones IPv4 como IPv6 para los hosts de doble pila, prefiriendo IPv6 primero para los milisegundos de tiempo de espera. Por omisión en `CURL_HET_DEFAULT`, que actualmente es de 200 milisegundos. Esta opción acepta cualquier valor que pueda convertirse en un `int` válido. Disponible a partir de PHP 7.3.0 y cURL 7.59.0.

`CURLOPT_HAPROXYPROTOCOL` (`int`)  
`true` para enviar un encabezado de protocolo HAProxy `PROXY` v1 al inicio de la conexión. La acción por omisión es no enviar este encabezado. Disponible a partir de PHP 7.3.0 y cURL 7.60.0.

`CURLOPT_HEADER` (`int`)  
Definir en `true` para incluir los encabezados en la salida enviada al callback definido por `CURLOPT_WRITEFUNCTION`. Disponible a partir de cURL 7.1.0.

`CURLOPT_HEADERFUNCTION` (`int`)  
Un `callable` con la siguiente firma:

```php
callback(resource $curlHandle, string $headerData): int
```

`curlHandle`  
El manejador cURL.

`headerData`  
Los datos de encabezado que deben ser escritos por el callback.

El callback debe devolver el número de bytes escritos. Disponible a partir de cURL 7.7.2.

`CURLOPT_HEADEROPT` (`int`)  
Enviar los encabezados HTTP tanto al proxy como al host o por separado. Los valores posibles son cualquiera de las constantes `CURLHEADER_*`. Por omisión en `CURLHEADER_SEPARATE` a partir de cURL 7.42.1, y `CURLHEADER_UNIFIED` antes de eso. Disponible a partir de PHP 7.0.7 y cURL 7.37.0.

`CURLOPT_HSTS` (`int`)  
`string` con el nombre del archivo de caché HSTS (HTTP Strict Transport Security) o `null` para permitir HSTS sin leer ni escribir en un archivo y borrar la lista de archivos para leer los datos HSTS. Disponible a partir de PHP 8.2.0 y cURL 7.74.0.

`CURLOPT_HSTS_CTRL` (`int`)  
Acepta una máscara de bits de las características HSTS (HTTP Strict Transport Security) definidas por las constantes `CURLHSTS_*`. Disponible a partir de PHP 8.2.0 y cURL 7.74.0.

`CURLOPT_HTTP09_ALLOWED` (`int`)  
Si se permiten las respuestas HTTP/0.9. Por omisión en `false` a partir de cURL 7.66.0; antes, era `true`. Disponible a partir de PHP 7.3.15 y 7.4.3, respectivamente, y cURL 7.64.0

`CURLOPT_HTTP200ALIASES` (`int`)  
Un `array` de respuestas HTTP `200` que serán consideradas como respuestas válidas y no como errores. Disponible a partir de cURL 7.10.3.

`CURLOPT_HTTPAUTH` (`int`)  
Una máscara de bits de los métodos de autenticación HTTP a usar. Las opciones son: `CURLAUTH_BASIC`, `CURLAUTH_DIGEST`, `CURLAUTH_GSSNEGOTIATE`, `CURLAUTH_NTLM`, `CURLAUTH_AWS_SIGV4`, `CURLAUTH_ANY`, `CURLAUTH_ANYSAFE` . Si se usa más de un método, cURL interrogará al servidor para ver qué métodos soporta y elegirá el mejor. `CURLAUTH_ANY` define todos los bits. cURL seleccionará automáticamente la que encuentre más segura. Disponible a partir de cURL 7.10.6.

`CURLOPT_HTTPGET` (`int`)  
Definir en `true` para restablecer el método de solicitud HTTP a `GET`. Como `GET` es el valor por omisión, esto solo es necesario si la solicitud de solicitud ha sido cambiada. Disponible a partir de cURL 7.8.1.

`CURLOPT_HTTPHEADER` (`int`)  
Un `array` de campos de encabezado HTTP a definir. Este array debe estar en el formato `array('Content-type: text/plain', 'Content-length: 100')` Disponible a partir de cURL 7.1.0.

`CURLOPT_HTTPPROXYTUNNEL` (`int`)  
`true` para tunelizar a través de un proxy HTTP dado. Disponible a partir de cURL 7.3.0.

`CURLOPT_HTTP_CONTENT_DECODING` (`int`)  
`false` para desactivar el decodificado automático del contenido de respuesta. Disponible a partir de cURL 7.16.2.

`CURLOPT_HTTP_TRANSFER_DECODING` (`int`)  
Si se define en `0`, el decodificado de transferencia está desactivado. Si se define en `1`, el decodificado de transferencia está activado. cURL hace el decodificado de transferencia por partes por omisión a menos que esta opción se defina en `0`. Por omisión en `1`. Disponible a partir de cURL 7.16.2.

`CURLOPT_HTTP_VERSION` (`int`)  
Definir en una de las constantes `CURL_HTTP_VERSION_*` para que cURL use la versión HTTP especificada. Disponible a partir de cURL 7.9.1.

`CURLOPT_IGNORE_CONTENT_LENGTH` (`int`)  
Si se define en `1`, ignora el encabezado `Content-Length` en la respuesta HTTP e ignora la solicitud o dependencia de este para las transferencias FTP. Por omisión en `0`. Disponible a partir de cURL 7.14.1.

`CURLOPT_INFILE` (`int`)  
Acepta un manejador de fichero `resource` hacia el fichero desde el que debe leerse la transferencia durante la descarga. Disponible a partir de cURL 7.1.0 y deprecado a partir de cURL 7.9.7. Use `CURLOPT_READDATA` en su lugar.

`CURLOPT_INFILESIZE` (`int`)  
El tamaño esperado, en bytes, del fichero al enviar un fichero a un sitio remoto. Es de notar que el uso de esta opción no evitará que cURL envíe más datos, ya que lo que se envía depende exactamente de `CURLOPT_READFUNCTION`. Esta opción acepta cualquier valor que pueda convertirse en un `int` válido. Disponible a partir de cURL 7.1.0.

`CURLOPT_INFILESIZE_LARGE` (`int`)  
El tamaño esperado, en bytes, del fichero al enviar un fichero a un sitio remoto. Es la variante de 64 bits de `CURLOPT_INFILESIZE`, que permite especificar tamaños superiores a 2 GB. Disponible a partir de PHP 8.5.0.

`CURLOPT_INTERFACE` (`int`)  
Definir en una `string` que contiene el nombre de la interfaz de red saliente a usar. Esto puede ser un nombre de interfaz, una dirección IP o un nombre de host. Disponible a partir de cURL 7.1.0.

`CURLOPT_IPRESOLVE` (`int`)  
Permite a una aplicación seleccionar el tipo de direcciones IP a utilizar durante la resolución de nombres de host. Esto solo es interesante al utilizar nombres de host que resuelven direcciones usando más de una versión de IP. Definir en una de las constantes `CURL_IPRESOLVE_*`. El valor por omisión es `CURL_IPRESOLVE_WHATEVER`. Disponible a partir de cURL 7.10.8.

`CURLOPT_ISSUERCERT` (`int`)  
Si se define a un `string` que nombra un archivo que contiene un certificado CA en formato PEM, se realiza una verificación adicional contra el certificado del par para verificar que el emisor es el asociado con el certificado proporcionado por la opción. Para que el resultado de la verificación se considere un fracaso, esta opción debe usarse en combinación con la opción `CURLOPT_SSL_VERIFYPEER`. Disponible a partir de cURL 7.19.0.

`CURLOPT_ISSUERCERT_BLOB` (`int`)  
Pasar un `string` que contenga datos binarios de un certificado SSL CA en formato PEM. Si esta opción está definida, se realiza una verificación adicional del certificado de la entidad (peer) para verificar que el emisor es el asociado al certificado proporcionado por esta opción. Disponible a partir de PHP 8.1.0 y cURL 7.71.0.

`CURLOPT_KEEP_SENDING_ON_ERROR` (`int`)  
Definir en `true` para continuar enviando el cuerpo de la petición si el código HTTP devuelto es superior o igual a `300`. La acción por omisión es detener el envío y cerrar el flujo o la conexión. Adecuado para la autenticación NTLM manual. La mayoría de las aplicaciones no necesitan esta opción. Disponible a partir de PHP 7.3.0 y cURL 7.51.0.

`CURLOPT_KEYPASSWD` (`int`)  
Definir en un `string` con la contraseña requerida para usar el `CURLOPT_SSLKEY` o `CURLOPT_SSH_PRIVATE_KEYFILE`. Definir esta opción en `null` desactiva el uso de una contraseña para estas opciones. Disponible a partir de cURL 7.17.0.

`CURLOPT_KRB4LEVEL` (`int`)  
La seguridad KRB4 (Kerberos 4). Cualquier valor `string` siguiente (en orden del menos al más potente) es válido: `clear`, `safe`, `confidential`, `private` . Si el `string` no coincide con uno de estos valores, `private` es usado. Definir esta opción en `null` desactivará la seguridad KRB4. Actualmente, la seguridad KRB4 solo funciona con transacciones FTP. Disponible a partir de cURL 7.3.0 y obsoleto a partir de cURL 7.17.0.

`CURLOPT_KRBLEVEL` (`int`)  
Define el nivel de seguridad Kerberos para FTP y también activa el soporte de Kerberos. Esto debe definirse en una de las `string`s siguientes: `clear`, `safe`, `confidential`, `private` Si la opción `string` está definida pero no coincide con ninguna de estas valores, `private` es usado. Definir esta opción en `null` desactivará el soporte de Kerberos para FTP. Por omisión en `null`. Disponible a partir de cURL 7.16.4.

`CURLOPT_LOCALPORT` (`int`)  
Define el número de puerto local del socket usado para la conexión. Esta opción acepta cualquier valor que pueda convertirse en un `int` válido. Por omisión en `0`. Disponible a partir de cURL 7.15.2.

`CURLOPT_LOCALPORTRANGE` (`int`)  
El número de intentos que cURL hace para encontrar un número de puerto local funcional, comenzando por el definido con `CURLOPT_LOCALPORT`. Esta opción acepta cualquier valor que pueda convertirse en un `int` válido. Por omisión en `1`. Disponible a partir de cURL 7.15.2.

`CURLOPT_LOGIN_OPTIONS` (`int`)  
Puede usarse para definir opciones de conexión específicas del protocolo, tales como el mecanismo de autenticación preferido vía `AUTH=NTLM` o `AUTH=*`, y debe usarse en conjunción con la opción `CURLOPT_USERNAME`. Disponible a partir de PHP 7.0.7 y cURL 7.34.0.

`CURLOPT_LOW_SPEED_LIMIT` (`int`)  
La velocidad de transferencia, en bytes por segundo, que la transferencia debe ser inferior durante el conteo de `CURLOPT_LOW_SPEED_TIME` segundos antes de que PHP considere la transferencia demasiado lenta y la interrumpa. Esta opción acepta cualquier valor que pueda convertirse en un `int` válido. Disponible a partir de cURL 7.1.0.

`CURLOPT_LOW_SPEED_TIME` (`int`)  
El número de segundos que la velocidad de transferencia debe ser inferior a `CURLOPT_LOW_SPEED_LIMIT` antes de que PHP considere la transferencia demasiado lenta y la interrumpa. Esta opción acepta cualquier valor que pueda convertirse en un `int` válido. Disponible a partir de cURL 7.1.0.

`CURLOPT_MAIL_AUTH` (`int`)  
Define un `string` con la dirección de autenticación (identidad) de un mensaje enviado que es reenviado a otro servidor. Esta dirección no debe especificarse entre paréntesis (`<>`). Si se usa un `string` vacío, entonces se envía un par de paréntesis por cURL como requerido por la RFC 2554. Disponible a partir de cURL 7.25.0.

`CURLOPT_MAIL_FROM` (`int`)  
Define un `string` con la dirección de correo electrónico del remitente al enviar un correo SMTP. La dirección de correo electrónico debe especificarse con paréntesis (`<>`) alrededor de ella, que si no están especificados son añadidos automáticamente. Si este parámetro no está especificado, se envía una dirección vacía al servidor SMTP que podría causar el rechazo del correo. Disponible a partir de cURL 7.20.0.

`CURLOPT_MAIL_RCPT` (`int`)  
Define un `array` de `string`s con los destinatarios a enviar al servidor en una petición de correo SMTP. Cada destinatario debe especificarse entre paréntesis (`<>`). Si un paréntesis no es usado como primer carácter, cURL asume que se ha proporcionado una sola dirección de correo electrónico y la encierra entre paréntesis. Disponible a partir de cURL 7.20.0.

`CURLOPT_MAIL_RCPT_ALLLOWFAILS` (`int`)  
Definir en `1` para permitir que el comando `RCPT TO` falle para algunos destinatarios, lo que hace que cURL ignore los errores para los destinatarios individuales y continúe con los otros destinatarios aceptados. Si todos los destinatarios resultan en fallos y esta bandera está especificada, cURL interrumpe la conversación SMTP y devuelve el error recibido del último comando `RCPT TO`. Reemplazado por `CURLOPT_MAIL_RCPT_ALLOWFAILS` a partir de cURL 8.2.0. Disponible a partir de PHP 8.2.0 y cURL 7.69.0. Deprecado a partir de cURL 8.2.0.

`CURLOPT_MAXAGE_CONN` (`int`)  
El tiempo máximo de inactividad permitido para una conexión existente para ser considerada para reutilización. Por omisión, el tiempo máximo es definido en `118` segundos. Esta opción acepta cualquier valor que pueda convertirse en un `int` válido. Disponible a partir de PHP 8.2.0 y cURL 7.65.0

`CURLOPT_MAXCONNECTS` (`int`)  
El máximo de conexiones persistentes permitidas. Cuando se alcanza el límite, la más antigua en el caché es cerrada para evitar el aumento del número de conexiones abiertas. Esta opción acepta cualquier valor que pueda convertirse en un `int` válido. Disponible a partir de cURL 7.7.0.

`CURLOPT_MAXFILESIZE` (`int`)  
Define el tamaño máximo admitido (en bytes) de un archivo a descargar. Si el archivo solicitado se encuentra más grande que este valor, la transferencia es interrumpida y `CURLE_FILESIZE_EXCEEDED` es devuelto. Pasar `0` desactiva esta opción, y pasar un tamaño negativo devuelve una `CURLE_BAD_FUNCTION_ARGUMENT`. Si el tamaño del archivo no es conocido antes del inicio de la descarga, esta opción no tiene efecto. Para un límite de tamaño superior a `2GB`, `CURLOPT_MAXFILESIZE_LARGE` debe ser usado. a partir de cURL 8.4.0, esta opción también detiene las transferencias en curso si alcanzan este umbral. Esta opción acepta cualquier valor que pueda convertirse en un `int` válido. Por omisión en `0`. Disponible a partir de cURL 7.10.8.

`CURLOPT_MAXFILESIZE_LARGE` (`int`)  
El tamaño máximo en bytes permitido para la descarga. Si el archivo solicitado se encuentra más grande que este valor, la transferencia no comenzará y `CURLE_FILESIZE_EXCEEDED` será devuelto. El tamaño del archivo no siempre es conocido antes de la descarga, y para tales archivos esta opción no tiene ningún efecto incluso si la transferencia de archivo termina siendo más grande que este límite dado. Disponible a partir de PHP 8.2.0 y cURL 7.11.0

`CURLOPT_MAXLIFETIME_CONN` (`int`)  
El tiempo máximo en segundos, desde la creación de la conexión, permitido para una conexión existente para ser considerada para reutilización. Si se encuentra una conexión en el caché que es más antigua que este valor, será cerrada una vez que todas las transferencias en curso hayan terminado. Por omisión en `0` segundos, lo que significa que la opción está desactivada y todas las conexiones son elegibles para reutilización. Esta opción acepta cualquier valor que pueda convertirse en un `int` válido. Disponible a partir de PHP 8.2.0 y cURL 7.80.0

`CURLOPT_MAXREDIRS` (`int`)  
La cantidad máxima de redirecciones HTTP a seguir. Usar esta opción junto con `CURLOPT_FOLLOWLOCATION`. El valor por omisión de `20` está definido para evitar redirecciones infinitas. Definir en `-1` permite redirecciones infinitas, y `0` rechaza todas las redirecciones. Disponible a partir de cURL 7.5.0.

`CURLOPT_MAX_RECV_SPEED_LARGE` (`int`)  
Si una descarga supera esta velocidad (contada en bytes por segundo) en promedio acumulativo durante la transferencia, la transferencia será pausada para mantener la velocidad promedio inferior o igual al valor del parámetro. El valor por omisión es una velocidad ilimitada. Esta opción acepta cualquier valor que pueda convertirse en un `int` válido. Disponible a partir de cURL 7.15.5.

`CURLOPT_MAX_SEND_SPEED_LARGE` (`int`)  
Si un envío supera esta velocidad (contada en bytes por segundo) en promedio acumulativo durante la transferencia, la transferencia será pausada para mantener la velocidad promedio inferior o igual al valor del parámetro. El valor por omisión es una velocidad ilimitada. Esta opción acepta cualquier valor que pueda convertirse en un `int` válido. Disponible a partir de cURL 7.15.5.

`CURLOPT_MIME_OPTIONS` (`int`)  
Definir un valor a una máscara de bits de las constantes `CURLMIMEOPT_*`. Actualmente, solo hay una opción disponible: `CURLMIMEOPT_FORMESCAPE`. Disponible a partir de PHP 8.3.0 y cURL 7.81.0.

`CURLOPT_MUTE` (`int`)  
Definir en `true` para ser completamente silencioso con las funciones cURL. Usar `CURLOPT_RETURNTRANSFER` en su lugar. Disponible a partir de cURL 7.1.0, deprecado a partir de cURL 7.8.0 y último disponible a partir de cURL 7.15.5. Eliminado a partir de PHP 7.3.0.

`CURLOPT_NETRC` (`int`)  
Definir en `true` para escanear el archivo `~/.netrc` para encontrar un nombre de usuario y una contraseña para el sitio remoto con el que se establece una conexión. Disponible a partir de cURL 7.1.0.

`CURLOPT_NETRC_FILE` (`int`)  
Define un `string` que contiene el nombre completo del archivo `.netrc`. Si esta opción es omitida y `CURLOPT_NETRC` está definido, cURL verifica un archivo `.netrc` en el directorio personal del usuario actual. Disponible a partir de cURL 7.11.0.

`CURLOPT_NEW_DIRECTORY_PERMS` (`int`)  
Define el valor de los permisos (`int`) que son definidos en los directorios recién creados en el servidor remoto. El valor por omisión es `0755`. Los únicos protocolos que pueden usar esta opción son `sftp://`, `scp://` y `file://`. Disponible a partir de cURL 7.16.4.

`CURLOPT_NEW_FILE_PERMS` (`int`)  
Define el valor de los permisos (`int`) que son definidos en los archivos recién creados en el servidor remoto. El valor por omisión es `0644`. Los únicos protocolos que pueden usar esta opción son `sftp://`, `scp://` y `file://`. Disponible a partir de cURL 7.16.4.

`CURLOPT_NOBODY` (`int`)  
Definir en `true` para excluir el cuerpo de la salida. Para HTTP(S), cURL realiza una petición HEAD. Para la mayoría de los otros protocolos, cURL no solicita en absoluto los datos del cuerpo. Cambiar esto a `false` resultará en la inclusión de los datos del cuerpo en la salida. Disponible a partir de cURL 7.1.0.

`CURLOPT_NOPROGRESS` (`int`)  
Definir en `true` para desactivar la barra de progreso para las transferencias cURL.

> [!NOTE]
> PHP define automáticamente esta opción en `true`, esto solo debería ser cambiado por razones de depuración.

Disponible a partir de cURL 7.1.0.

`CURLOPT_NOPROXY` (`int`)  
Define un `string` consistente en una lista separada por comas de nombres de host que no requieren proxy para ser alcanzados. Cada nombre en esta lista es comparado ya sea como un dominio que contiene el nombre de host o el nombre de host mismo. El único carácter genérico disponibles en el `string` es un simple carácter `*` que coincide con todos los hosts, desactivando efectivamente el proxy. Definir esta opción en un `string` vacío activa el proxy para todos los nombres de host. a partir de cURL 7.86.0, las direcciones IP definidas con esta opción pueden ser proporcionadas usando la notación CIDR. Disponible a partir de cURL 7.19.4.

`CURLOPT_NOSIGNAL` (`int`)  
`true` para ignorar cualquier función cURL que envíe un señal al proceso PHP. Esto está activado por omisión en los SAPI multi-hilo para que las opciones de tiempo de espera puedan siempre ser usadas. Disponible a partir de cURL 7.10.

`CURLOPT_PASSWDFUNCTION` (`int`)  
Un `callable` con la siguiente firma:

```php
callback(resource $curlHandle, string $passwordPrompt, int $maximumPasswordLength): string
```php

`curlHandle`  
El manejador cURL.

`passwordPrompt`  
Un indicador de contraseña.

`maximumPasswordLength`  
La longitud máxima de la contraseña.

El callback debe devolver un `string` que contenga la contraseña. Disponible a partir de cURL 7.4.2, deprecado a partir de cURL 7.11.1 y último disponible a partir de cURL 7.15.5. Eliminado a partir de PHP 7.3.0.

`CURLOPT_PASSWORD` (`int`)  
Definir en un `string` que contenga la contraseña a usar para la autenticación. Disponible a partir de cURL 7.19.1.

`CURLOPT_PATH_AS_IS` (`int`)  
Definir en `true` para que cURL no altere los caminos de URL antes de transmitirlos al servidor. Por omisión es `false`, lo que aplana las secuencias de `/../` o `/./` que pueden existir en la parte camino de la URL y que están destinadas a ser eliminadas conforme a la sección 5.2.4 del RFC 3986. Disponible a partir de PHP 7.0.7 y cURL 7.42.0.

`CURLOPT_PINNEDPUBLICKEY` (`int`)  
Definir un `string` con la clave pública fijada. El `string` puede ser el nombre del archivo de la clave pública fijada en formato PEM o DER. El `string` también puede ser cualquier número de hachajes sha256 codificados en base64 precedidos por `sha256//` y separados por `;`. Disponible a partir de PHP 7.0.7 y cURL 7.39.0.

`CURLOPT_PIPEWAIT` (`int`)  
Establecer en `true` para esperar que una conexión existente confirme si puede hacer multiplexaje y usarlo si es el caso antes de crear y usar una nueva conexión. Disponible a partir de PHP 7.0.7 y cURL 7.43.0.

`CURLOPT_PORT` (`int`)  
Un `int` con un número de puerto alternativo para conectarse en lugar del especificado en la URL o del puerto por defecto para el protocolo utilizado. Disponible a partir de cURL 7.1.0.

`CURLOPT_POST` (`int`)  
Establecer en `true` para realizar una petición HTTP `POST`. Esta petición usa el encabezado `application/x-www-form-urlencoded`. Por omisión, es `false`. Disponible a partir de cURL 7.1.0.

`CURLOPT_POSTFIELDS` (`int`)  
Los datos completos a enviar en una operación HTTP `POST`. Este parámetro puede pasarse ya sea en forma de `string` urlencodada como '`para1=val1&para2=val2&...`' o en forma de un `array` con el nombre del campo como clave y los datos del campo como valor. Si `value` es un array, el encabezado `Content-Type` será establecido en `multipart/form-data`. Los archivos pueden ser enviados usando `CURLFile` o `CURLStringFile`, en cuyo caso `value` debe ser un `array`. Disponible a partir de cURL 7.1.0.

`CURLOPT_POSTQUOTE` (`int`)  
Un `array` de `string`s de comandos FTP a ejecutar en el servidor después de ejecutar la petición FTP. Disponible a partir de cURL 7.1.0.

`CURLOPT_POSTREDIR` (`int`)  
Establecer en un bitmask de `CURL_REDIR_POST_301`, `CURL_REDIR_POST_302` y `CURL_REDIR_POST_303` si el método HTTP `POST` debe mantenerse cuando `CURLOPT_FOLLOWLOCATION` está establecido y ocurre un tipo específico de redirección. Disponible a partir de cURL 7.19.1.

`CURLOPT_PRE_PROXY` (`int`)  
Establece una cadena `string` que contiene el nombre de host o la dirección IP numérica a usar como preproxy al que cURL se conecta antes de conectarse al proxy HTTP(S) especificado en la opción `CURLOPT_PROXY` para la próxima petición. El preproxy solo puede ser un proxy SOCKS y debe estar prefijado por `[scheme]://` para especificar qué tipo de calcetín se usa. Una dirección IP numérica IPv6 debe escribirse entre \[corchetes\]. Establecer el preproxy en un `string` vacío desactiva explícitamente el uso de un preproxy. Para especificar el número de puerto en este `string`, añadir `:[port]` al final del nombre de host. El número de puerto del proxy puede opcionalmente ser especificado con la opción separada `CURLOPT_PROXYPORT`. Por omisión, usa el puerto 1080 para los proxys si un puerto no está especificado. Disponible a partir de PHP 7.3.0 y cURL 7.52.0.

`CURLOPT_PREQUOTE` (`int`)  
Establece un array de comandos FTP a ejecutar en el servidor antes de la petición después de que la conexión FTP haya sido establecida. Estos comandos no se ejecutan cuando se solicita una lista de directorio, solo para las transferencias de archivos. Disponible a partir de cURL 7.9.5.

`CURLOPT_PRIVATE` (`int`)  
Cualquier dato que debería asociarse con este manejador cURL. Estos datos pueden luego ser recuperados con la opción `CURLINFO_PRIVATE` de `curl_getinfo`. cURL no hace nada con estos datos. Al usar un manejador cURL multi, estos datos privados son típicamente una clave única para identificar un manejador cURL estándar. Disponible a partir de cURL 7.10.3.

`CURLOPT_PROGRESSFUNCTION` (`int`)  
Un `callable` con la siguiente firma:

```php
callback(resource $curlHandle, int $bytesToDownload, int $bytesDownloaded, int $bytesToUpload, int $bytesUploaded): int
```

`curlHandle`  
El manejador cURL.

`bytesToDownload`  
El número total de bytes esperados a descargar durante esta transferencia.

`bytesDownloaded`  
El número de bytes descargados hasta ahora.

`bytesToUpload`  
El número total de bytes esperados a descargar durante esta transferencia.

`bytesUploaded`  
El número de bytes descargados hasta ahora.

La devolución de llamada debe devolver un `int` con un valor no nulo para interrumpir la transferencia y establecer un error `CURLE_ABORTED_BY_CALLBACK`.

> [!NOTE]
> La función es llamada cuando la opción `CURLOPT_NOPROGRESS` está establecida en `false`.

Disponible a partir de cURL 7.1.0 y obsoleto a partir de cURL 7.32.0. Usar `CURLOPT_XFERINFOFUNCTION` en su lugar.

`CURLOPT_PROTOCOLS` (`int`)  
Un bitmask de valores `CURLPROTO_*`. Si se usa, este bitmask limita los protocolos que cURL puede usar en la transferencia. Por omisión, esto vale `CURLPROTO_ALL`, es decir, cURL aceptará todos los protocolos que soporta. Ver `CURLOPT_REDIR_PROTOCOLS`. Disponible a partir de cURL 7.19.4 y depreciado a partir de cURL 7.85.0.

`CURLOPT_PROTOCOLS_STR` (`int`)  
Establecer en un `string` que contiene una lista separada por comas de nombres de protocolos insensibles a mayúsculas/minúsculas (esquemas de URL) permitidos en la transferencia. Establecer en `ALL` para activar todos los protocolos. Por omisión, cURL acepta todos los protocolos para los que ha sido construido con soporte. Los protocolos disponibles son: `DICT`, `FILE`, `FTP`, `FTPS`, `GOPHER`, `GOPHERS`, `HTTP`, `HTTPS`, `IMAP`, `IMAPS`, `LDAP`, `LDAPS`, `MQTT`, `POP3`, `POP3S`, `RTMP`, `RTMPE`, `RTMPS`, `RTMPT`, `RTMPTE`, `RTMPTS`, `RTSP`, `SCP`, `SFTP`, `SMB`, `SMBS`, `SMTP`, `SMTPS`, `TELNET`, `TFTP`, `WS`, `WSS` . Disponible a partir de PHP 8.3.0 y cURL 7.85.0.

`CURLOPT_PROXY` (`int`)  
Un `string` con el proxy HTTP a través del cual realizar las peticiones. Esto debe ser el nombre de host, la dirección IP numérica en notación decimal o una dirección IPv6 numérica escrita entre \[corchetes\]. Disponible a partir de cURL 7.1.0.

`CURLOPT_PROXYAUTH` (`int`)  
Un bitmask de los métodos de autenticación HTTP ( `CURLAUTH_*` ) a usar para la conexión al proxy. Para la autenticación por proxy, solo `CURLAUTH_BASIC` y `CURLAUTH_NTLM` están actualmente soportados. Por omisión, es `CURLAUTH_BASIC`. Disponible a partir de cURL 7.10.7.

`CURLOPT_PROXYHEADER` (`int`)  
Un `array` de encabezados HTTP personalizados como `string` a enviar al proxy. Disponible a partir de PHP 7.0.7 y cURL 7.37.0.

`CURLOPT_PROXYPASSWORD` (`int`)  
Establece un `string` con la contraseña a usar para la autenticación con el proxy. Disponible a partir de cURL 7.19.1.

`CURLOPT_PROXYPORT` (`int`)  
Un `int` con el número de puerto del proxy a usar para la conexión. Este número de puerto también puede ser establecido en `CURLOPT_PROXY`. Establecerlo en cero hace que cURL use el número de puerto por defecto del proxy o el número de puerto especificado en la cadena de caracteres de la URL del proxy. Disponible a partir de cURL 7.1.0.

`CURLOPT_PROXYTYPE` (`int`)  
Establece el tipo de proxy a una de las constantes `CURLPROXY_*`. Por omisión, es `CURLPROXY_HTTP`. Disponible a partir de cURL 7.10.

`CURLOPT_PROXYUSERNAME` (`int`)  
Establece un `string` con el nombre de usuario a usar para la autenticación con el proxy. Disponible a partir de cURL 7.19.1.

`CURLOPT_PROXYUSERPWD` (`int`)  
Un `string` que contiene un nombre de usuario y una contraseña en el formato `[nombre_usuario]:[contraseña]` a usar para la conexión al proxy. Disponible a partir de cURL 7.1.0.

`CURLOPT_PROXY_CAINFO` (`int`)  
La ruta al archivo de certificados de la Autoridad de Certificación (CA) del proxy. Establecer la ruta como un `string` que nombre un archivo que contenga uno o más certificados para verificar el proxy HTTPS. Esta opción es para conectarse a un proxy HTTPS, no a un servidor HTTPS. El valor por defecto es la ruta del sistema donde se supone que está almacenado el paquete cacert de cURL Disponible a partir de PHP 7.3.0 y cURL 7.52.0.

`CURLOPT_PROXY_CAINFO_BLOB` (`int`)  
Un `string` con el nombre del archivo PEM que contiene uno o más certificados para verificar el proxy HTTPS. Esta opción es para conectarse a un proxy HTTPS, no a un servidor HTTPS. Por defecto, la ruta del sistema donde se supone que está almacenado el paquete cacert de cURL. Disponible a partir de PHP 8.2.0 y cURL 7.77.0.

`CURLOPT_PROXY_CAPATH` (`int`)  
Un `string` con el directorio que contiene varios certificados CA para verificar el proxy HTTPS. Disponible a partir de PHP 7.3.0 y cURL 7.52.0.

`CURLOPT_PROXY_CRLFILE` (`int`)  
Establecer en un `string` con el nombre de archivo que contiene la lista de revocación de certificados (CRL) en formato PEM a usar en la validación del certificado que ocurre durante el intercambio SSL. Disponible a partir de PHP 7.3.0 y cURL 7.52.0.

`CURLOPT_PROXY_ISSUERCERT` (`int`)  
El nombre de archivo del certificado SSL del emisor del proxy como `string`. Disponible a partir de PHP 8.1.0 y cURL 7.71.0.

`CURLOPT_PROXY_ISSUERCERT_BLOB` (`int`)  
Un `string` con el certificado SSL del emisor del proxy a partir del blob de memoria. Disponible a partir de PHP 8.1.0 y cURL 7.71.0.

`CURLOPT_PROXY_KEYPASSWD` (`int`)  
Establece el `string` a usar como contraseña para cargar la clave privada `CURLOPT_PROXY_SSLKEY`. Una frase secreta no es necesaria para cargar un certificado, pero es requerida para cargar una clave privada. Esta opción es para conectarse a un proxy HTTPS, no a un servidor HTTPS. Disponible a partir de PHP 7.3.0 y cURL 7.52.0.

`CURLOPT_PROXY_PINNEDPUBLICKEY` (`int`)  
Establece la clave pública anclada para el proxy HTTPS. El `string` puede ser el nombre de archivo de la clave pública anclada que debe estar en formato `PEM` o `DER`. El `string` también puede ser cualquier número de hachados sha256 codificados en base64 precedidos por `sha256//` y separados por `;`. Disponible a partir de PHP 7.3.0 y cURL 7.52.0.

`CURLOPT_PROXY_SERVICE_NAME` (`int`)  
Un `string` con el nombre del servicio de autenticación del proxy. Disponible a partir de PHP 7.0.7, cURL 7.43.0 (para proxys HTTP) y cURL 7.49.0 (para proxys SOCKS5).

`CURLOPT_PROXY_SSLCERT` (`int`)  
Un `string` con el nombre de archivo del certificado cliente usado para conectarse al proxy HTTPS. El formato por defecto es `P12` en Secure Transport y `PEM` en otros motores, y puede ser cambiado con `CURLOPT_PROXY_SSLCERTTYPE`. Con NSS o Secure Transport, esto también puede ser el sobrenombre del certificado usado para la autenticación tal como está nombrado en la base de datos de seguridad. Si un archivo del directorio actual debe ser usado, debe ser precedido por `./` para evitar cualquier confusión con un sobrenombre. Disponible a partir de PHP 7.3.0 y cURL 7.52.0.

`CURLOPT_PROXY_SSLCERTTYPE` (`int`)  
Un `string` con el formato del certificado cliente usado al conectarse a un proxy HTTPS. Los formatos soportados son `PEM` y `DER`, excepto con Secure Transport. OpenSSL (versiones 0.9.3 y posteriores) y Secure Transport (en iOS 5 o posterior, o OS X 10.7 o posterior) también soportan `P12` para archivos codificados en PKCS#12. Por defecto, es `PEM`. Disponible a partir de PHP 7.3.0 y cURL 7.52.0.

`CURLOPT_PROXY_SSLCERT_BLOB` (`int`)  
Un `string` con el certificado cliente SSL del proxy. Disponible a partir de PHP 8.1.0 y cURL 7.71.0.

`CURLOPT_PROXY_SSLKEY` (`int`)  
Un `string` con el nombre de archivo de la clave privada usada para conectarse al proxy HTTPS. El formato por defecto es `PEM` y puede ser modificado con `CURLOPT_PROXY_SSLKEYTYPE`. (iOS y Mac OS X solo) Esta opción es ignorada si cURL ha sido compilado con Secure Transport. Disponible si compilado con TLS. Disponible a partir de PHP 7.3.0 y cURL 7.52.0.

`CURLOPT_PROXY_SSLKEYTYPE` (`int`)  
Un `string` con el formato de la clave privada. Los formatos soportados son: `PEM`, `DER`, `ENG` . Disponible a partir de PHP 7.3.0 y cURL 7.52.0.

`CURLOPT_PROXY_SSLKEY_BLOB` (`int`)  
Un `string` con la clave privada usada para conectarse al proxy HTTPS. Disponible a partir de PHP 8.1.0 y cURL 7.71.0.

`CURLOPT_PROXY_SSLVERSION` (`int`)  
Establece la versión TLS del proxy HTTPS preferida en una de las constantes `CURL_SSLVERSION_*`. Por defecto, esto corresponde a `CURL_SSLVERSION_DEFAULT`.

> [!WARNING]
> Es preferible no establecer esta opción y dejar el valor por defecto `CURL_SSLVERSION_DEFAULT` que intentará determinar la versión del protocolo SSL remoto.

Disponible a partir de PHP 7.3.0 y cURL 7.52.0.

`CURLOPT_PROXY_SSL_CIPHER_LIST` (`int`)  
Un `string` con una lista de cifrados separados por dos puntos a usar para la conexión al proxy HTTPS. Cuando se usa con OpenSSL, comas y espacios también son aceptables como separadores, y `!`, `-` y `+` pueden ser usados como operadores. Disponible a partir de PHP 7.3.0 y cURL 7.52.0.

`CURLOPT_PROXY_SSL_OPTIONS` (`int`)  
Establece las opciones de comportamiento SSL del proxy, que es un bitmask de las constantes `CURLSSLOPT_*`. Disponible a partir de PHP 7.3.0 y cURL 7.52.0.

`CURLOPT_PROXY_SSL_VERIFYHOST` (`int`)  
Establecer en `2` para verificar en los campos de nombre del certificado del proxy contra el nombre del proxy. Cuando se establece en `0`, la conexión tiene éxito independientemente de los nombres utilizados en el certificado. ¡Use esta capacidad con precaución! Establecer en `1` a partir de cURL 7.28.0 y versiones anteriores como opción de depuración. Establecer en `1` a partir de cURL 7.28.1 a 7.65.3 `CURLE_BAD_FUNCTION_ARGUMENT` es devuelto. A partir de cURL 7.66.0, `1` y `2` se tratan como el mismo valor. Por defecto, el valor de esta opción debe mantenerse en `2`. En entornos de producción, el valor de esta opción debe permanecer en `2`. Disponible a partir de PHP 7.3.0 y cURL 7.52.0.

`CURLOPT_PROXY_SSL_VERIFYPEER` (`int`)  
Establecer en `false` para detener cURL de verificar el certificado del proxy. Certificados alternativos a verificar pueden ser especificados con la opción `CURLOPT_PROXY_CAINFO` o un directorio de certificados puede ser especificado con la opción `CURLOPT_PROXY_CAPATH`. Cuando está definido en `false`, la verificación del certificado del proxy tiene éxito independientemente. `true` por defecto. Disponible a partir de PHP 7.3.0 y cURL 7.52.0

`CURLOPT_PROXY_TLS13_CIPHERS` (`int`)  
Una `string` con una lista de cifrados separados por dos puntos para usar en la conexión al proxy a través de TLS 1.3. Esta opción se usa actualmente solo cuando cURL está construido para usar OpenSSL 1.1.1 o una versión posterior. Al usar otro backend SSL, las suites de cifrado TLS 1.3 pueden ser definidas con la opción `CURLOPT_PROXY_SSL_CIPHER_LIST`. Disponible a partir de PHP 7.3.0 y cURL 7.61.0.

`CURLOPT_PROXY_TLSAUTH_PASSWORD` (`int`)  
Una `string` que contiene la contraseña a usar para el método de autenticación TLS especificado con el `CURLOPT_PROXY_TLSAUTH_TYPE`. Requiere también que la opción `CURLOPT_PROXY_TLSAUTH_USERNAME` esté definida. Disponible a partir de PHP 7.3.0 y cURL 7.52.0.

`CURLOPT_PROXY_TLSAUTH_TYPE` (`int`)  
El método de autenticación TLS usado para la conexión HTTPS. El método soportado es `SRP`.

> [!NOTE]
> La autenticación Secure Remote Password (SRP) para TLS proporciona autenticación mutua si ambas partes tienen un secreto compartido. Para usar TLS-SRP, las opciones `CURLOPT_PROXY_TLSAUTH_USERNAME` y `CURLOPT_PROXY_TLSAUTH_PASSWORD` también deben estar definidas.

Disponible a partir de PHP 7.3.0 y cURL 7.52.0.

`CURLOPT_PROXY_TLSAUTH_USERNAME` (`int`)  
El nombre de usuario a usar para el método de autenticación TLS del proxy HTTPS especificado con la opción `CURLOPT_PROXY_TLSAUTH_TYPE`. Requiere también que la opción `CURLOPT_PROXY_TLSAUTH_PASSWORD` esté definida. Disponible a partir de PHP 7.3.0 y cURL 7.52.0.

`CURLOPT_PROXY_TRANSFER_MODE` (`int`)  
Establecer en `1` para definir el modo de transferencia (binario o ASCII) para las transferencias FTP realizadas a través de un proxy HTTP, añadiendo `type=a` o `type=i` a la URL. Sin este parámetro o si está definido en `0`, `CURLOPT_TRANSFERTEXT` no tiene ningún efecto al usar FTP a través de un proxy. Por defecto en `0`. Disponible a partir de cURL 7.18.0.

`CURLOPT_PUT` (`int`)  
`true` para realizar una solicitud HTTP PUT de un archivo. El archivo a subir debe ser definido con `CURLOPT_READDATA` y `CURLOPT_INFILESIZE`. Disponible a partir de cURL 7.1.0 y obsoleto a partir de cURL 7.12.1.

`CURLOPT_QUICK_EXIT` (`int`)  
Establecer en `true` para que cURL ignore la limpieza de recursos al recuperar un tiempo límite. Esto permite una terminación rápida del proceso cURL a costa de una posible fuga de recursos asociados. Disponible a partir de PHP 8.3.0 y cURL 7.87.0.

`CURLOPT_QUOTE` (`int`)  
Un `array` de comandos FTP para ejecutar en el servidor antes de la solicitud FTP. Disponible a partir de cURL 7.1.0.

`CURLOPT_RANDOM_FILE` (`int`)  
Una `string` con un nombre de archivo para usar para inicializar el generador de números aleatorios para SSL. Disponible a partir de cURL 7.7.0 y obsoleto a partir de cURL 7.84.0.

`CURLOPT_RANGE` (`int`)  
Una `string` con el/los rango(s) de datos a recuperar en formato `X-Y`, donde X o Y son opcionales. Las transferencias HTTP también soportan múltiples intervalos, separados por comas en formato `X-Y,N-M`. Establecer en `null` para desactivar la solicitud de un rango de bytes. Disponible a partir de cURL 7.1.0.

`CURLOPT_READDATA` (`int`)  
Define un puntero de archivo `resource` que será usado por la función de lectura de archivo definida con `CURLOPT_READFUNCTION`. Disponible a partir de cURL 7.9.7.

`CURLOPT_READFUNCTION` (`int`)  
Un `callable` con la siguiente firma:

```php
callback(resource $curlHandle, resource $streamResource, int $maxAmountOfDataToRead): string
```php

`curlHandle`  
El manejador cURL.

`streamResource`  
Recurso de flujo `resource` proporcionado a cURL a través de la opción `CURLOPT_READDATA`.

`maxAmountOfDataToRead`  
La cantidad máxima de datos a leer.

La devolución de llamada debe devolver una `string` de una longitud igual o inferior a la cantidad de datos solicitados, típicamente leyéndola desde el `stream` de flujo pasado. Debe devolver una `string` vacía para indicar `fin de archivo`. Disponible a partir de cURL 7.1.0.

`CURLOPT_REDIR_PROTOCOLS` (`int`)  
Una máscara de bits de valores `CURLPROTO_*` que limita los protocolos que cURL puede usar en una transferencia que sigue en una redirección cuando `CURLOPT_FOLLOWLOCATION` está activado. Esto permite limitar ciertas transferencias para que solo usen un subconjunto de protocolos durante las redirecciones. A partir de cURL 7.19.4, por defecto, cURL permitirá todos los protocolos, excepto `FILE` y `SCP`. Antes de cURL 7.19.4, cURL seguía sin condición todos los protocolos soportados. Ver también `CURLOPT_PROTOCOLS` para los valores constantes de protocolo. Disponible a partir de cURL 7.19.4 y obsoleto a partir de cURL 7.85.0.

`CURLOPT_REDIR_PROTOCOLS_STR` (`int`)  
Establecer en una `string` con una lista separada por comas de nombres de protocolos insensibles a mayúsculas/minúsculas (esquemas de URL) para permitir durante una redirección cuando `CURLOPT_FOLLOWLOCATION` está activado. Establecer en `ALL` para activar todos los protocolos. A partir de cURL 7.65.2, esto por defecto es `FTP`, `FTPS`, `HTTP` y `HTTPS`. De cURL 7.40.0 a 7.65.1, esto por defecto es todos los protocolos excepto `FILE`, `SCP`, `SMB` y `SMBS`. Antes de cURL 7.40.0, esto por defecto es todos los protocolos excepto `FILE` y `SCP`. Los protocolos disponibles son: `DICT`, `FILE`, `FTP`, `FTPS`, `GOPHER`, `GOPHERS`, `HTTP`, `HTTPS`, `IMAP`, `IMAPS`, `LDAP`, `LDAPS`, `MQTT`, `POP3`, `POP3S`, `RTMP`, `RTMPE`, `RTMPS`, `RTMPT`, `RTMPTE`, `RTMPTS`, `RTSP`, `SCP`, `SFTP`, `SMB`, `SMBS`, `SMTP`, `SMTPS`, `TELNET`, `TFTP`, `WS`, `WSS` . Disponible a partir de PHP 8.3.0 y cURL 7.85.0.

`CURLOPT_REFERER` (`int`)  
Una `string` que contiene el contenido del encabezado `Referer:` para usar en una solicitud HTTP. Disponible a partir de cURL 7.1.0.

`CURLOPT_REQUEST_TARGET` (`int`)  
Una `string` para usar en la solicitud entrante en lugar de la ruta extraída de la URL. Disponible a partir de PHP 7.3.0 y cURL 7.55.0.

`CURLOPT_RESOLVE` (`int`)  
Proporcionar un `array` de `string`s separados por dos puntos con direcciones personalizadas para pares de host y puerto específicos en el siguiente formato: `array( "example.com:80:127.0.0.1", "example2.com:443:127.0.0.2", )` Disponible a partir de cURL 7.21.3.

`CURLOPT_RESUME_FROM` (`int`)  
El desplazamiento, en bytes, para reanudar una transferencia. Esta opción acepta cualquier valor que pueda convertirse en un `int` válido. Disponible a partir de cURL 7.1.0.

`CURLOPT_RETURNTRANSFER` (`int`)  
`true` para devolver la respuesta como `string` de la función `curl_exec` en lugar de mostrarla directamente.

`CURLOPT_RTSP_CLIENT_CSEQ` (`int`)  
Define un `int` con el número CSEQ para emitir en la próxima solicitud RTSP. Usar si la aplicación reanuda una conexión previamente interrumpida. El CSEQ se incrementa a partir de este nuevo número posteriormente. Por defecto en `0`. Disponible a partir de cURL 7.20.0.

`CURLOPT_RTSP_REQUEST` (`int`)  
Define el tipo de solicitud RTSP a realizar. Debe ser una de las constantes `CURL_RTSPREQ_*`. Disponible a partir de cURL 7.20.0.

`CURLOPT_RTSP_SERVER_CSEQ` (`int`)  
Define un `int` con el número CSEQ para esperar en la próxima solicitud RTSP del servidor. Esta funcionalidad (escuchar solicitudes del servidor) no está implementada. Por defecto en `0`. Disponible a partir de cURL 7.20.0.

`CURLOPT_RTSP_SESSION_ID` (`int`)  
Define un `string` con el valor del identificador de la sesión RTSP actual para el manejador. Una vez que este valor se establece en un valor no-`null`, cURL devuelve `CURLE_RTSP_SESSION_ERROR` si el identificador recibido del servidor no coincide. Si se establece en `null`, cURL define automáticamente el identificador la primera vez que el servidor lo define en una respuesta. Por defecto en `null` Disponible a partir de cURL 7.20.0.

`CURLOPT_RTSP_STREAM_URI` (`int`)  
Define un `string` con el URI del flujo sobre el que operar. Si no está definido, cURL define por defecto la operación en las opciones de servidor genéricas pasando `*` en lugar del URI del flujo RTSP. Al trabajar con RTSP, `CURLOPT_RTSP_STREAM_URI` indica qué URL enviar al servidor en el encabezado de solicitud mientras que `CURLOPT_URL` indica dónde establecer la conexión. Disponible a partir de cURL 7.20.0.

`CURLOPT_RTSP_TRANSPORT` (`int`)  
Define el encabezado `Transport:` para esta sesión RTSP. Disponible a partir de cURL 7.20.0.

`CURLOPT_SAFE_UPLOAD` (`int`)  
Siempre `true`, lo que desactiva el soporte del prefijo `"@"` para enviar archivos en `CURLOPT_POSTFIELDS`, lo que significa que los valores que comienzan con `"@"` pueden ser pasados de forma segura como campos. `CURLFile` puede ser usado para las subidas a la vez.

`CURLOPT_SASL_AUTHZID` (`int`)  
La identidad de autorización (authzid) `string` para la transferencia. Aplicable solo a SASL PLAIN donde es opcional. Cuando no se especifica, solo la identidad de autenticación (authcid) tal como se especifica por el nombre de usuario será enviada al servidor, con la contraseña. El servidor deducirá el authzid del authcid cuando no se proporcione, que luego usará internamente. Disponible a partir de PHP 8.2.0 y cURL 7.66.0.

`CURLOPT_SASL_IR` (`int`)  
`true` para habilitar la inicialización de la respuesta SASL (SASL Initial Response). Disponible a partir de PHP 7.0.7 y cURL 7.31.0.

`CURLOPT_SERVICE_NAME` (`int`)  
Un `string` con el nombre del servicio de autenticación. Disponible a partir de PHP 7.0.7 y cURL 7.43.0.

`CURLOPT_SHARE` (`int`)  
Un resultado de `curl_share_init`. Hace que el manejador cURL use los datos del manejador compartido. Disponible a partir de cURL 7.10.

`CURLOPT_SOCKS5_AUTH` (`int`)  
`CURLAUTH_BASIC`, `CURLAUTH_GSSAPI`, `CURLAUTH_NONE` . Cuando más de un método está definido, cURL consultará al servidor para ver qué métodos soporta y elegirá el mejor. Por defecto, `CURLAUTH_BASIC|CURLAUTH_GSSAPI`. Definir el nombre de usuario y la contraseña reales con la opción `CURLOPT_PROXYUSERPWD`. Disponible a partir de PHP 7.3.0 y cURL 7.55.0.

`CURLOPT_SOCKS5_GSSAPI_NEC` (`int`)  
Establecer en `1` para habilitar y en `0` para deshabilitar el intercambio no protegido de la negociación del modo de protección en el contexto de la negociación GSSAPI. Disponible a partir de cURL 7.19.4.

`CURLOPT_SOCKS5_GSSAPI_SERVICE` (`int`)  
Define un `string` que contiene el nombre del servicio SOCKSS. Por defecto en `rcmd`. Disponible a partir de cURL 7.19.4 y obsoleto a partir de cURL 7.49.0. Usar `CURLOPT_PROXY_SERVICE_NAME` en su lugar.

`CURLOPT_SSH_AUTH_TYPES` (`int`)  
Una máscara de bits compuesta por una o más de las siguientes constantes: `CURLSSH_AUTH_PUBLICKEY`, `CURLSSH_AUTH_PASSWORD`, `CURLSSH_AUTH_HOST`, `CURLSSH_AUTH_KEYBOARD`, `CURLSSH_AUTH_AGENT`, `CURLSSH_AUTH_ANY` . Por defecto, esto corresponde a `CURLSSH_AUTH_ANY`. Disponible a partir de cURL 7.16.1.

`CURLOPT_SSH_COMPRESSION` (`int`)  
`true` para habilitar, `false` para deshabilitar la compresión SSH integrada. Tenga en cuenta que el servidor puede ignorar esta solicitud. Por defecto, esto corresponde a `false`. Disponible a partir de PHP 7.3.0 y cURL 7.56.0.

`CURLOPT_SSH_HOSTKEYFUNCTION` (`int`)  
Un `callable` que será llamado cuando la verificación de la clave del host SSH sea necesaria. La devolución de llamada debe tener la siguiente firma:

```php
callback(resource $curlHandle, int $keyType, string $key, int $keyLength): int
```

`curlHandle`  
El manejador cURL.

`keyType`  
Uno de los tipos de clave `CURLKHTYPE_*`.

`key`  
La clave a verificar.

`keyLength`  
La longitud de la clave en bytes.

Esta opción reemplaza `CURLOPT_SSH_KNOWNHOSTS`. Disponible a partir de PHP 8.3.0 y cURL 7.84.0.

`CURLOPT_SSH_HOST_PUBLIC_KEY_MD5` (`int`)  
Una `string` que contiene 32 dígitos hexadecimales que deben contener el checksum MD5 de la clave pública del host remoto, y cURL rechazará la conexión al host a menos que las sumas de control md5 coincidan. Esta opción es únicamente para transferencias SCP y SFTP. Disponible a partir de cURL 7.17.1.

`CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256` (`int`)  
Una `string` con el hash SHA256 codificado en base64 de la clave pública del host remoto. La transferencia fallará si el hash proporcionado no coincide con el hash proporcionado por el host remoto. Disponible a partir de PHP 8.2.0 y cURL 7.80.0.

`CURLOPT_SSH_KNOWNHOSTS` (`int`)  
Define el nombre del archivo `known_host` a utilizar que debería usar el formato de archivo OpenSSH soportado por libssh2. Disponible a partir de cURL 7.19.6.

`CURLOPT_SSH_PRIVATE_KEYFILE` (`int`)  
El nombre del archivo de su clave privada. Si no se usa, cURL usa por omisión `$HOME/.ssh/id_dsa` si la variable de entorno HOME está definida, y solo `id_dsa` en el directorio actual si HOME no está definido. Si el archivo está protegido por contraseña, defina la contraseña con `CURLOPT_KEYPASSWD`. Disponible a partir de cURL 7.16.1.

`CURLOPT_SSH_PUBLIC_KEYFILE` (`int`)  
El nombre del archivo de su clave pública. Si no se usa, cURL usa por omisión `$HOME/.ssh/id_dsa.pub` si la variable de entorno HOME está definida, y solo `id_dsa.pub` en el directorio actual si HOME no está definido. Disponible a partir de cURL 7.16.1.

`CURLOPT_SSLCERT` (`int`)  
El nombre de un archivo que contiene un certificado en formato PEM. Disponible a partir de cURL 7.1.0.

`CURLOPT_SSLCERTPASSWD` (`int`)  
La contraseña requerida para usar el certificado `CURLOPT_SSLCERT`. Disponible a partir de cURL 7.1.0 y desaconsejado a partir de cURL 7.17.0.

`CURLOPT_SSLCERTTYPE` (`int`)  
Una `string` con el formato del certificado. Los formatos soportados son : `PEM`, `DER`, `ENG`, `P12` . `P12` (para archivos codificados en PKCS#12) está disponible a partir de OpenSSL 0.9.3. Por omisión, es `PEM`. Disponible a partir de cURL 7.9.3.

`CURLOPT_SSLCERT_BLOB` (`int`)  
Una `string` con el certificado SSL del cliente. Disponible a partir de PHP 8.1.0 y cURL 7.71.0.

`CURLOPT_SSLENGINE` (`int`)  
El identificador `string` para el motor criptográfico de la clave SSL privada especificada en `CURLOPT_SSLKEY`. Disponible a partir de cURL 7.9.3.

`CURLOPT_SSLENGINE_DEFAULT` (`int`)  
El identificador del motor de criptografía usado para las operaciones de criptografía asimétrica.

`CURLOPT_SSLKEY` (`int`)  
El nombre de un archivo que contiene una clave privada SSL. Disponible a partir de cURL 7.9.3.

`CURLOPT_SSLKEYPASSWD` (`int`)  
La contraseña requerida para usar la clave privada SSL especificada en `CURLOPT_SSLKEY`.

> [!NOTE]
> Dado que esta opción contiene una contraseña sensible, no olvide mantener el script PHP en el que está contenido seguro.

Disponible a partir de cURL 7.9.3 y desaconsejado a partir de cURL 7.17.0.

`CURLOPT_SSLKEYTYPE` (`int`)  
El tipo de clave privada SSL especificada en `CURLOPT_SSLKEY`. Los tipos de clave soportados son : `PEM`, `DER`, `ENG` . Por omisión, es `PEM`. Disponible a partir de cURL 7.9.3.

`CURLOPT_SSLKEY_BLOB` (`int`)  
Una `string` clave privada para el certificado del cliente. Disponible a partir de PHP 8.1.0 y cURL 7.71.0.

`CURLOPT_SSLVERSION` (`int`)  
Una de las constantes siguientes `CURL_SSLVERSION_*`.

> [!WARNING]
> Es preferible no definir esta opción y dejar los valores por omisión. Definir esta opción a `CURL_SSLVERSION_SSLv2` o `CURL_SSLVERSION_SSLv3` es muy peligroso, dado las vulnerabilidades conocidas en SSLv2 y SSLv3.

Por omisión, es `CURL_SSLVERSION_DEFAULT`. Disponible a partir de cURL 7.1.0.

`CURLOPT_SSL_CIPHER_LIST` (`int`)  
Una `string` separada por dos puntos de los cifrados a usar para la conexión TLS 1.2 (1.1, 1.0). Disponible a partir de cURL 7.9.

`CURLOPT_SSL_EC_CURVES` (`int`)  
Una lista de curvas elípticas delimitadas por dos puntos. Por ejemplo, `X25519:P-521` es una lista de dos curvas elípticas válidas. Esta opción define los algoritmos de intercambio de claves del cliente en el apretón de mano SSL, si el backend SSL de cURL está compilado para usarlo. Disponible a partir de PHP 8.2.0 y cURL 7.73.0.

`CURLOPT_SSL_ENABLE_ALPN` (`int`)  
`false` para deshabilitar ALPN en el apretón de mano SSL (si el backend SSL de cURL está compilado para usarlo), lo cual puede ser usado para negociar http2. Disponible a partir de PHP 7.0.7 y cURL 7.36.0.

`CURLOPT_SSL_ENABLE_NPN` (`int`)  
`false` para deshabilitar NPN en el apretón de mano SSL (si el backend SSL de cURL está compilado para usarlo), lo cual puede ser usado para negociar http2. Disponible a partir de PHP 7.0.7 y cURL 7.36.0, y obsoleto a partir de cURL 7.86.

`CURLOPT_SSL_FALSESTART` (`int`)  
`true` para habilitar y `false` para deshabilitar el inicio anticipado de TLS, que es un modo donde un cliente TLS comienza a enviar datos de aplicación antes de verificar el mensaje `Finished` del servidor. Disponible a partir de PHP 7.0.7 y cURL 7.42.0.

`CURLOPT_SSL_OPTIONS` (`int`)  
Definir las opciones de comportamiento SSL, que son una máscara de bits de las constantes `CURLSSLOPT_*`. Por omisión, ninguno de los bits está definido. Disponible a partir de PHP 7.0.7 y cURL 7.25.0.

`CURLOPT_SSL_SESSIONID_CACHE` (`int`)  
Definir a `0` para deshabilitar y a `1` para habilitar el caché de sesión SSL. Por omisión, todas las transferencias se realizan usando el caché habilitado. Disponible a partir de cURL 7.16.0.

`CURLOPT_SSL_VERIFYHOST` (`int`)  
`2` para verificar que un campo de nombre común o un campo de nombre alternativo en el certificado SSL del par coincide con el nombre de host proporcionado. `0` para no verificar los nombres. `1` no debe ser usado. En producción, el valor de esta opción debe mantenerse en `2` (valor por omisión). El soporte para el valor `1` fue eliminado a partir de cURL 7.28.1. Disponible a partir de cURL 7.8.1.

`CURLOPT_SSL_VERIFYPEER` (`int`)  
`false` para evitar que cURL verifique el certificado del par. Certificados alternativos a verificar pueden ser especificados con la opción `CURLOPT_CAINFO` o un directorio de certificados puede ser especificado con la opción `CURLOPT_CAPATH`. Por omisión, es `true` a partir de cURL 7.10. Paquete por omisión de certificados CA instalado a partir de cURL 7.10. Disponible a partir de cURL 7.4.2.

`CURLOPT_SSL_VERIFYSTATUS` (`int`)  
`true` para habilitar y `false` para deshabilitar la verificación del estado del certificado. Disponible a partir de PHP 7.0.7 y cURL 7.41.0.

`CURLOPT_STDERR` (`int`)  
Acepta un descriptor de archivo `resource` que apunta hacia una ubicación alternativa para enviar errores en lugar de `STDERR`. Disponible a partir de cURL 7.1.0.

`CURLOPT_STREAM_WEIGHT` (`int`)  
Definir el peso numérico del flujo (un número entre `1` y `256`). Disponible a partir de PHP 7.0.7 y cURL 7.46.0.

`CURLOPT_SUPPRESS_CONNECT_HEADERS` (`int`)  
`true` para suprimir los encabezados de respuesta proxy CONNECT de las funciones de devolución de llamada de usuario `CURLOPT_HEADERFUNCTION` y `CURLOPT_WRITEFUNCTION`, cuando `CURLOPT_HTTPPROXYTUNNEL` es usado y una petición CONNECT es realizada. Por omisión, es `false`. Disponible a partir de PHP 7.3.0 y cURL 7.54.0.

`CURLOPT_TCP_FASTOPEN` (`int`)  
`true` para habilitar y `false` para deshabilitar TCP Fast Open. Disponible a partir de PHP 7.0.7 y cURL 7.49.0.

`CURLOPT_TCP_KEEPALIVE` (`int`)  
Si se define a `1`, se enviarán sondas de mantenimiento de conexión TCP. El intervalo y la frecuencia de estas sondas pueden ser controladas por las opciones `CURLOPT_TCP_KEEPIDLE` y `CURLOPT_TCP_KEEPINTVL`, siempre que el sistema operativo las soporte. Si se define a `0` (por omisión), las sondas de mantenimiento de conexión están deshabilitadas. El número máximo de sondas puede ser definido con la opción `CURLOPT_TCP_KEEPCNT`. Disponible a partir de cURL 7.25.0.

`CURLOPT_TCP_KEEPIDLE` (`int`)  
Define el intervalo, en segundos, que el sistema operativo esperará mientras la conexión está inutilizada antes de enviar sondas de mantenimiento de conexión, si `CURLOPT_TCP_KEEPALIVE` está habilitado. No todos los sistemas operativos soportan esta opción. El valor por omisión es `60`. Disponible a partir de cURL 7.25.0.

`CURLOPT_TCP_KEEPINTVL` (`int`)  
Define el intervalo, en segundos, que el sistema operativo esperará entre el envío de sondas de mantenimiento de conexión, si `CURLOPT_TCP_KEEPALIVE` está habilitado. No todos los sistemas operativos soportan esta opción. El valor por omisión es `60`. Disponible a partir de cURL 7.25.0.

`CURLOPT_TCP_KEEPCNT` (`int`)  
Define el número máximo de sondas de mantenimiento de conexión TCP. El valor por omisión es `9`. Disponible a partir de PHP 8.4.0 y cURL 8.9.0.

`CURLOPT_TCP_NODELAY` (`int`)  
`true` para deshabilitar el algoritmo de Nagle TCP, que intenta minimizar el número de pequeños paquetes en la red. Por omisión, es `true`. Disponible a partir de cURL 7.11.2.

`CURLOPT_TELNETOPTIONS` (`int`)  
Define un `array` de `string`s a pasar a las negociaciones telnet. Estas variables deben estar en el formato `<option=valor>`. cURL soporta las opciones `TTYPE`, `XDISPLOC` y `NEW_ENV`. Disponible a partir de cURL 7.7.0.

`CURLOPT_TFTP_BLKSIZE` (`int`)  
Define el tamaño de bloque a usar para la transmisión de datos TFTP. El rango válido es de `8` a `65464` bytes. Por omisión, se usan `512` bytes si esta opción no está especificada. El tamaño de bloque especificado solo se usa si es soportado por el servidor remoto. SI el servidor no devuelve un ACK de opción o devuelve un ACK de opción sin tamaño de bloque, se usa el valor por omisión de `512` bytes. Disponible a partir de cURL 7.19.4.

`CURLOPT_TFTP_NO_OPTIONS` (`int`)  
`true` para no enviar solicitudes de opciones TFTP. Por omisión, es `false`. Disponible a partir de PHP 7.0.7 y cURL 7.48.0.

`CURLOPT_TIMECONDITION` (`int`)  
Definir cómo `CURLOPT_TIMEVALUE` es tratado. Usar `CURL_TIMECOND_IFMODSINCE` para devolver la página solo si ha sido modificada desde el tiempo especificado en `CURLOPT_TIMEVALUE`. Si no ha sido modificada, un encabezado `304 Not Modified` será devuelto asumiendo que `CURLOPT_HEADER` es `true`. Usar `CURL_TIMECOND_IFUNMODSINCE` para el efecto inverso. Usar `CURL_TIMECOND_NONE` para ignorar `CURLOPT_TIMEVALUE` y siempre devolver la página. `CURL_TIMECOND_NONE` es el valor por omisión. Antes de cURL 7.46.0, el valor por omisión era `CURL_TIMECOND_IFMODSINCE`. Disponible a partir de cURL 7.1.0.

`CURLOPT_TIMEOUT` (`int`)  
El número máximo de segundos a esperar para las funciones cURL. Por omisión, es `0`, lo que significa que las funciones nunca exceden el tiempo de espera durante la transferencia. Disponible a partir de cURL 7.1.0.

`CURLOPT_TIMEOUT_MS` (`int`)  
El número máximo de milisegundos a esperar para las funciones cURL se ejecutan. Si cURL está compilado para usar el resolutor de nombres estándar del sistema, esta parte de la conexión siempre usará una resolución de segundo completo para los tiempos de espera con un mínimo permitido de un segundo. Por omisión, es `0`, lo que significa que las funciones nunca exceden el tiempo de espera durante la transferencia. Disponible a partir de cURL 7.16.2.

`CURLOPT_TIMEVALUE` (`int`)  
El tiempo en segundos desde el 1 de enero de 1970. El tiempo será usado por `CURLOPT_TIMECONDITION`. Por omisión, es `0`. Disponible a partir de cURL 7.1.0.

`CURLOPT_TIMEVALUE_LARGE` (`int`)  
El tiempo en segundos desde el 1 de enero de 1970. El tiempo será usado por `CURLOPT_TIMECONDITION`. Por omisión, cero. La diferencia entre esta opción y `CURLOPT_TIMEVALUE` es el tipo del argumento. En sistemas donde 'long' solo tiene 32 bits de ancho, esta opción debe ser usada para definir fechas más allá del año 2038. Disponible a partir de PHP 7.3.0 y cURL 7.59.0

`CURLOPT_TLS13_CIPHERS` (`int`)  
Una `string` con una lista de cifrados separados por dos puntos a usar para la conexión TLS 1.3. Esta opción actualmente solo se usa cuando cURL está compilado con OpenSSL 1.1.1 o versión posterior. Al usar otro backend SSL, las suites de cifrado TLS 1.3 pueden ser definidas con la opción `CURLOPT_SSL_CIPHER_LIST`. Disponible a partir de PHP 7.3.0 y cURL 7.61.0.

`CURLOPT_TLSAUTH_PASSWORD` (`int`)  
El tiempo de espera para las respuestas `Expect: 100-continue` en milisegundos. Por omisión, `1000` milisegundos. Esta opción acepta cualquier valor que pueda convertirse en un `int` válido. Disponible a partir de PHP 7.0.7 y cURL 7.36.0.

`CURLOPT_TLSAUTH_TYPE` (`int`)  
Define una `string` con el método de autenticación TLS. El método soportado es `SRP` (autenticación TLS Secure Remote Password). Disponible a partir de cURL 7.21.4.

`CURLOPT_TLSAUTH_USERNAME` (`int`)  
Define un `string` con el nombre de usuario a utilizar para el método de autenticación TLS especificado con la opción `CURLOPT_TLSAUTH_TYPE`. Requiere que la opción `CURLOPT_TLSAUTH_PASSWORD` también esté definida. Esta funcionalidad se basa en TLS SRP que no funciona con TLS 1.3. Disponible a partir de cURL 7.21.4.

`CURLOPT_TRANSFER_ENCODING` (`int`)  
Define a `1` para activar y a `0` para desactivar la solicitud de `Transfer Encoding` comprimido en la solicitud HTTP saliente. Si el servidor responde con un `Transfer Encoding` comprimido, cURL lo descomprimirá automáticamente al recibirlo. Por omisión, es `0`. Disponible a partir de cURL 7.21.6.

`CURLOPT_TRANSFERTEXT` (`int`)  
`true` para usar el modo ASCII para transferencias FTP. Para LDAP, recupera los datos en texto sin formato en lugar de HTML. En sistemas Windows, no establecerá `STDOUT` en modo binario. Por omisión, es `false`. Disponible a partir de cURL 7.1.1.

`CURLOPT_UNIX_SOCKET_PATH` (`int`)  
Activa el uso de sockets de dominio Unix como punto de conexión y define la ruta del `string` dado. Definir en `null` para desactivar. Por omisión, es `null`. Disponible a partir de PHP 7.0.7 y cURL 7.40.0.

`CURLOPT_UNRESTRICTED_AUTH` (`int`)  
`true` para continuar enviando el nombre de usuario y la contraseña al seguir las ubicaciones (usando `CURLOPT_FOLLOWLOCATION`), incluso cuando el nombre de host ha cambiado. Por omisión, es `false`. Disponible a partir de cURL 7.10.4.

`CURLOPT_UPKEEP_INTERVAL_MS` (`int`)  
Algunos protocolos tienen mecanismos de "mantenimiento de la conexión". Estos mecanismos generalmente envían tráfico en las conexiones existentes para mantenerlas vivas. Esta opción define el intervalo de mantenimiento de la conexión. Actualmente, el único protocolo con un mecanismo de mantenimiento de la conexión es HTTP/2. Cuando el intervalo de mantenimiento de la conexión es excedido, un marco PING HTTP/2 es enviado en la conexión. Por omisión, es `CURL_UPKEEP_INTERVAL_DEFAULT` que actualmente es `60` segundos. Disponible a partir de PHP 8.2.0 y cURL 7.62.0.

`CURLOPT_UPLOAD` (`int`)  
`true` para preparar y realizar una subida. Por omisión, es `false`. Disponible a partir de cURL 7.1.0.

`CURLOPT_UPLOAD_BUFFERSIZE` (`int`)  
El tamaño de búfer preferido en bytes para la subida cURL. El tamaño de búfer de subida por omisión es de 64 kilobytes. El tamaño máximo de búfer permitido a ser definido es de 2 megabytes. El tamaño mínimo de búfer permitido a ser definido es de 16 kilobytes. Disponible a partir de PHP 8.2.0 y cURL 7.62.0.

`CURLOPT_URL` (`int`)  
La URL a recuperar. Esto también puede ser definido durante la inicialización de una sesión con `curl_init`. Disponible a partir de cURL 7.1.0.

`CURLOPT_USE_SSL` (`int`)  
Define el nivel de SSL/TLS deseado para la transferencia al utilizar FTP, SMTP, POP3, IMAP, etc. Estos son todos protocolos que comienzan en texto claro y son "mejorados" en SSL utilizando el comando STARTTLS. Definir en una de las constantes `CURLUSESSL_*`. Disponible a partir de cURL 7.17.0.

`CURLOPT_USERAGENT` (`int`)  
El contenido del encabezado `User-Agent:` a utilizar en una solicitud HTTP. Disponible a partir de cURL 7.1.0.

`CURLOPT_USERNAME` (`int`)  
El nombre de usuario a utilizar en la autenticación. Disponible a partir de cURL 7.19.1.

`CURLOPT_USERPWD` (`int`)  
El nombre de usuario y la contraseña en la forma `[username]:[password]` a utilizar para la conexión. Disponible a partir de cURL 7.1.0.

`CURLOPT_VERBOSE` (`int`)  
`true` para mostrar información detallada sobre la conexión. Escribe la salida en `STDERR`, o el archivo especificado utilizando `CURLOPT_STDERR`. Por omisión, es `false`. Disponible a partir de cURL 7.1.0.

`CURLOPT_WILDCARDMATCH` (`int`)  
Definir en `1` para transferir múltiples archivos según un patrón de nombre de archivo. El patrón puede ser especificado como parte de la opción `CURLOPT_URL`, utilizando un patrón similar a fnmatch (Shell Pattern Matching) en la última parte de la URL (nombre de archivo). Disponible a partir de cURL 7.21.0.

`CURLOPT_WRITEFUNCTION` (`int`)  
Un `callable` con la siguiente firma:

```php
callback(resource $curlHandle, string $data): int
```php

`curlHandle`  
El manejador cURL.

`data`  
Los datos a escribir.

Los datos deben ser almacenados por el callback y el callback debe devolver el número exacto de bytes escritos o la transferencia será cancelada con un error. Disponible a partir de cURL 7.1.0.

`CURLOPT_WRITEHEADER` (`int`)  
Acepta un manejador de archivo `resource` hacia el archivo en el cual la parte de encabezado de la transferencia es escrita. Disponible a partir de cURL 7.1.0.

`CURLOPT_WS_OPTIONS` (`int`)  
Acepta una máscara de bits para definir las opciones de comportamiento WebSocket. La única opción disponible es `CURLWS_RAW_MODE`. Por omisión, es `0`. Disponible a partir de PHP 8.3.0 y cURL 7.86.0.

`CURLOPT_XFERINFOFUNCTION` (`int`)  
Un `callable` con la siguiente firma:

```php
callback(resource $curlHandle, int $bytesToDownload, int $bytesDownloaded, int $bytesToUpload, int $bytesUploaded): int
```

`curlHandle`  
El manejador cURL.

`bytesToDownload`  
El número total de bytes que deberían ser descargados durante esta transferencia.

`bytesDownloaded`  
El número de bytes descargados hasta ahora.

`bytesToUpload`  
El número total de bytes que deberían ser subidos durante esta transferencia.

`bytesUploaded`  
El número de bytes subidos hasta ahora.

Devolver `1` para cancelar la transferencia y establecer un error `CURLE_ABORTED_BY_CALLBACK`. Disponible a partir de PHP 8.2.0 y cURL 7.32.0.

`CURLOPT_SERVER_RESPONSE_TIMEOUT` (`int`)  
Un tiempo de espera en segundos que cURL esperará para una respuesta de un servidor FTP, SFTP, IMAP, SCP, SMTP, o un servidor POP3. Esta opción reemplaza la opción existente `CURLOPT_FTP_RESPONSE_TIMEOUT` que está obsoleta a partir de cURL 7.85.0. Disponible a partir de PHP 8.4.0.

`CURLOPT_XOAUTH2_BEARER` (`int`)  
Especifica el token de acceso OAuth 2.0. Definir en `null` para desactivar. Por omisión, es `null`. Disponible a partir de PHP 7.0.7 y cURL 7.33.0.

`CURLOPT_PREREQFUNCTION` (`int`)  
Un `callable` con la siguiente firma que es llamada después de establecer la conexión, pero antes de que la carga útil de la solicitud (por ejemplo, la solicitud GET/POST/DELETE de una conexión HTTP) sea enviada, y que puede ser utilizada para cancelar o autorizar la conexión en función de la dirección IP de origen y los números de puerto de origen y destino:

```php
callback(CurlHandle $curlHandle, string $destination_ip, string $local_ip, int $destination_port, int $local_port): int
```php

`curlHandle`  
El manejador cURL.

`destination_ip`  
La dirección IP principal del servidor remoto establecido con esta conexión. Para FTP, es la IP de la conexión de control. Las direcciones IPv6 se representan sin corchetes.

`local_ip`  
La dirección IP de origen para esta conexión. Las direcciones IPv6 se representan sin corchetes.

`destination_port`  
El número de puerto principal en el servidor remoto establecido con esta conexión. Para FTP, es el puerto de la conexión de control. Esto puede ser un número de puerto TCP o UDP dependiendo del protocolo.

`local_port`  
El número de puerto de origen para esta conexión. Esto puede ser un número de puerto TCP o UDP dependiendo del protocolo.

Devolver `CURL_PREREQFUNC_OK` para autorizar la solicitud, o `CURL_PREREQFUNC_ABORT` para cancelar la transferencia. Disponible a partir de PHP 8.4.0 y cURL 7.80.0.

`CURLOPT_DEBUGFUNCTION` (`int`)  
Disponible a partir de PHP 8.4.0. Esta opción requiere la opción `CURLOPT_VERBOSE` activada. Un `callable` para reemplazar la salida verbose estándar de cURL. Este callback es llamado en diferentes etapas de la solicitud con información de depuración detallada. El callback debe coincidir con la siguiente firma:

```php
callback(CurlHandle $curlHandle, int $type, string $data): void
```

`curlHandle`  
El manejador cURL.

`type`  
Una de las siguientes constantes que indica el tipo del valor `data`:

`CURLINFO_TEXT` (`int`)  
Texto informativo.

`CURLINFO_HEADER_IN` (`int`)  
Datos de encabezado (o similares a los encabezados) recibidos del par.

`CURLINFO_HEADER_OUT` (`int`)  
Datos de encabezado (o similares a los encabezados) enviados al par.

`CURLINFO_DATA_IN` (`int`)  
Datos de protocolo sin procesar recibidos del par. Incluso si los datos están codificados o comprimidos, no se proporcionan decodificados ni descomprimidos a este callback.

`CURLINFO_DATA_OUT` (`int`)  
Datos de protocolo enviados al par.

`CURLINFO_SSL_DATA_IN` (`int`)  
Datos SSL/TLS (binarios) recibidos del par.

`CURLINFO_SSL_DATA_OUT` (`int`)  
Datos SSL/TLS (binarios) enviados al par.

`data`  
Datos de depuración detallados del tipo indicado por el parámetro `type`.
