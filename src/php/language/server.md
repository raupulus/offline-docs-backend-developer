---
title: $_SERVER
description: Variables de servidor y de ejecución
source_url: https://www.php.net/manual/es/reserved.variables.server.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/variables/server.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 6b413423c
order: 4220
---

\$\_SERVER

Variables de servidor y de ejecución

## Descripción

`$_SERVER` es un `array` que contiene información como encabezados, rutas y ubicaciones de script. Las entradas de este array son creadas por el servidor web, por lo que no hay garantía de que cada servidor web proporcione toda esta información; los servidores pueden omitir algunas o proporcionar otras no listadas aquí. Sin embargo, la mayoría de estas variables están contempladas en la especificación [CGI/1.1](https://datatracker.ietf.org/doc/html/rfc3875) y es probable que estén definidas.

> [!NOTE]
> Cuando PHP se ejecuta en línea de comandos [command line](#features.commandline), la mayoría de estas entradas no estarán disponibles o no tendrán sentido.

Además de los elementos enumerados a continuación, PHP creará elementos adicionales con valores provenientes de los encabezados de la petición. Estas entradas se nombrarán `HTTP_` seguido del nombre del encabezado, en mayúsculas y con guiones bajos en lugar de guiones. Por ejemplo, el encabezado `Accept-Language` estará disponible como `$_SERVER['HTTP_ACCEPT_LANGUAGE']`.

## Índices

'`PHP_SELF`'  
El nombre del archivo del script en ejecución, relativo a la raíz web. Por ejemplo, `$_SERVER['PHP_SELF']` en el script ubicado en `http://example.com/foo/bar.php` será `/foo/bar.php`. La constante [\_\_FILE\_\_](#language.constants.magic) contiene la ruta completa y el nombre del archivo (incluido) actual.

Si PHP funciona en línea de comandos, esta variable contiene el nombre del script.

'[argv](#reserved.variables.argv)'  
Array de argumentos pasados al script. Cuando el script es llamado en línea de comandos, esto da acceso a los argumentos, como en lenguaje C. Cuando el script es llamado con el método GET, este array contendrá la cadena de consulta.

'[argc](#reserved.variables.argc)'  
Contiene el número de parámetros de línea de comandos pasados al script (si el script funciona en línea de comandos).

'`GATEWAY_INTERFACE`'  
Número de revisión de la interfaz CGI del servidor. Por ejemplo `'CGI/1.1'`.

'`SERVER_ADDR`'  
La dirección IP del servidor bajo el cual el script actual está siendo ejecutado.

'`SERVER_NAME`'  
El nombre del servidor host que ejecuta el script siguiente. Si el script es ejecutado en un host virtual, esto será el valor definido para ese host virtual.

> [!NOTE]
> En Apache 2, `UseCanonicalName = On` y `ServerName` deben ser definidos. De lo contrario, este valor refleja el nombre de host proporcionado por el cliente, que puede ser falsificado. No es seguro confiar en este valor en contextos dependientes de la seguridad.

'`SERVER_SOFTWARE`'  
Cadena de identificación del servidor, que es dada en los encabezados al responder a las peticiones.

'`SERVER_PROTOCOL`'  
Nombre y revisión del protocolo de comunicación; por ejemplo `HTTP/1.0`;

'`REQUEST_METHOD`'  
Método de petición utilizado para acceder a la página; por ejemplo `GET`, `HEAD`, `POST`, `PUT`.

> [!NOTE]
> El script PHP termina después de enviar los encabezados (es decir, después de producir cualquier salida sin bufferización de salida) si el método de la petición era `HEAD`.

'`REQUEST_TIME`'  
El timestamp Unix del inicio de la petición.

'`REQUEST_TIME_FLOAT`'  
El timestamp del inicio de la petición, con precisión a microsegundos.

'`QUERY_STRING`'  
La cadena de consulta, si existe, que es utilizada para acceder a la página.

'`DOCUMENT_ROOT`'  
La raíz bajo la cual el script actual está siendo ejecutado, como se define en la configuración del servidor.

'`HTTPS`'  
Definido a un valor no vacío si el script fue llamado vía el protocolo HTTPS.

'`REMOTE_ADDR`'  
La dirección IP del cliente que solicita la página actual.

'`REMOTE_HOST`'  
El nombre del host que lee el script actual. La resolución DNS inversa se basa en el valor de `REMOTE_ADDR`.

> [!NOTE]
> El servidor web debe estar configurado para crear esta variable. Por ejemplo, en Apache, `HostnameLookups On` debe ser definido dentro de `httpd.conf` para que exista. Ver también `gethostbyaddr`.

'`REMOTE_PORT`'  
El puerto utilizado por la máquina cliente para comunicarse con el servidor web.

'`REMOTE_USER`'  
El usuario autenticado.

'`REDIRECT_REMOTE_USER`'  
El usuario autenticado si la petición fue redirigida internamente.

'`SCRIPT_FILENAME`'  
La ruta absoluta hacia el archivo que contiene el script en ejecución.

> [!NOTE]
> Si un script es ejecutado con el CLI, con una ruta relativa, como `file.php` o `../file.php`, `$_SERVER['SCRIPT_FILENAME']` contendrá la ruta relativa especificada por el usuario.

'`SERVER_ADMIN`'  
El valor dado a la directiva SERVER_ADMIN (para Apache), en el archivo de configuración. Si el script es ejecutado por un host virtual, esto será la valor definido por el host virtual.

'`SERVER_PORT`'  
El puerto de la máquina servidor utilizado para las comunicaciones. Por defecto, es `'80'`. Usando SSL, por ejemplo, será reemplazado por el número de puerto HTTP seguro.

> [!NOTE]
> En Apache 2, `UseCanonicalName = On`, así como `UseCanonicalPhysicalPort = On` deben ser definidos para obtener el puerto físico real, de lo contrario este valor puede ser falsificado y puede o no devolver el valor del puerto físico. No es seguro confiar en este valor en contextos dependientes de la seguridad.

'`SERVER_SIGNATURE`'  
Cadena que contiene el número de versión del servidor y el nombre de host virtual, que son añadidos a las páginas generadas por el servidor, si esta opción está activada.

'`PATH_TRANSLATED`'  
Ruta en el sistema de archivos (no el document-root) hasta el script actual, una vez que el servidor ha hecho una traducción de ruta virtual a real.

> [!NOTE]
> Los usuarios de Apache 2 deben usar `AcceptPathInfo = On` en su `httpd.conf` para definir `PATH_INFO`.

'`SCRIPT_NAME`'  
Contiene el nombre del script actual. Esto sirve cuando las páginas deben llamarse a sí mismas. La constante [\_\_FILE\_\_](#language.constants.magic) contiene la ruta completa y el nombre del archivo (incluido) actual.

'`REQUEST_URI`'  
El URI que fue proporcionado para acceder a esta página. Por ejemplo: '`/index.html`'.

'`PHP_AUTH_DIGEST`'  
Cuando se utiliza la autenticación HTTP Digest, esta variable es definida en el encabezado `"Authorization"` enviado por el cliente (que debe ser utilizado para realizar la validación apropiada).

'`PHP_AUTH_USER`'  
Cuando se utiliza la autenticación HTTP, esta variable es definida al usuario proporcionado por el usuario.

'`PHP_AUTH_PW`'  
Cuando se utiliza la autenticación HTTP, esta variable es definida a la contraseña proporcionada por el usuario.

'`AUTH_TYPE`'  
Cuando se utiliza la autenticación HTTP, esta variable es definida al tipo de identificación.

'`PATH_INFO`'  
Contiene la información sobre el nombre de la ruta proporcionada por el cliente respecto al nombre del archivo que ejecuta el script actual, sin la cadena relativa a la consulta si existe. Actualmente, si el script actual es ejecutado vía el URI `http://www.example.com/php/path_info.php/some/stuff?foo=bar`, entonces la variable `$_SERVER['PATH_INFO']` contendrá `/some/stuff`.

'`ORIG_PATH_INFO`'  
Versión original de '`PATH_INFO`' antes de ser analizada por PHP.

## Ejemplos

Ejemplo con `$_SERVER`

```php
<?php
echo $_SERVER['SERVER_NAME'];
?>

    
```

Resultado del ejemplo anterior es similar a:

    www.example.com

## Notas

> [!NOTE]
> Esto es una 'superglobal', o variable global automática. Esto significa simplemente que esta variable está disponible en todos los contextos del script. No es necesario hacer `global $variable;` para acceder a ella en las funciones o los métodos.

## Véase también

[La extensión sobre filtros](#book.filter)
