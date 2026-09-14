---
title: Otros cambios
source_url: https://www.php.net/manual/es/migration85.other-changes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration85/other-changes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: '750153283'
order: 1250
---

## Otros cambios

## Cambios en el núcleo

### Núcleo

El temporizador de alta resolución (`hrtime`) en macOS ahora utiliza la API recomendada `clock_gettime_nsec_np(CLOCK_UPTIME_RAW)` en lugar de `mach_absolute_time()`.

### CGI/CLI

Se ha eliminado la opción `-z` o `--zend-extension` ya que no funcionaba. En su lugar, utilice `-d zend_extension=[ruta]`.

### PDO_ODBC

Se ha modificado el comportamiento de recuperación de datos para columnas de mayor tamaño. En lugar de recuperar bloques de 256 bytes, PDO_ODBC intentará recuperar bloques de mayor tamaño; actualmente, este tamaño corresponde al tamaño de página menos la sobrecarga de cadena. Los controladores que devuelven SQL_NO_TOTAL en SQLGetData también se gestionan mejor. Esto debería mejorar la compatibilidad y el rendimiento.

## Changes in SAPI Modules

### CLI

Intentar establecer un título de proceso demasiado largo con `cli_set_process_title` ahora fallará en lugar de truncar silenciosamente el título dado.

Se agregó una nueva opción `--ini=diff` para imprimir la configuración INI modificada con respecto al valor predeterminado integrado.

### FPM

FPM con httpd ProxyPass decodifica opcionalmente la ruta completa del script. Se ha añadido la configuración INI fastcgi.script_path_encoded para evitar este nuevo comportamiento.

El límite de registro de acceso de FPM ahora respeta el valor [log_limit](#log-limit).

## Funciones modificadas

### Intl

`grapheme_extract` asigna correctamente el valor de `next` al omitir bytes iniciales no válidos. Anteriormente, en ocasiones apuntaba al inicio del límite del grafema en lugar de al final.

Se ha eliminado `false` de la unión de tipos de retorno de `transliterator_get_error_code`, `transliterator_get_error_message`, TransLiterator::getErrorCode, y TransLiterator::getErrorMessage. Devolver `false` nunca fue posible.

Las siguientes funciones ahora admiten un argumento `locale`: `grapheme_strpos`, `grapheme_stripos`, `grapheme_strrpos`, `grapheme_strripos`, `grapheme_substr`, `grapheme_strstr` y `grapheme_stristr`

### LDAP

`ldap_get_option` ahora acepta una conexión `null`, como `ldap_set_option`, para permitir la recuperación de opciones globales.

### libxml

`libxml_set_external_entity_loader` ahora tiene un tipo de retorno formal de `true`.

### OpenSSL

`openssl_public_encrypt` y `openssl_private_decrypt` tienen un nuevo parámetro `digest_algo` que permite especificar el algoritmo de resumen hash para el relleno OAEP.

`openssl_sign` y `openssl_verify` tienen un nuevo parámetro `padding` para permitir el uso de un relleno RSA PSS más seguro.

`openssl_cms_encrypt` el parámetro `cipher_algo` puede ser un string con el nombre del algoritmo de cifrado. Esto permite usar más algoritmos, incluidos los algoritmos de cifrado AES y GCM, para datos cifrados con autenticación.

### PCNTL

`pcntl_exec` ahora tiene un tipo de retorno formal de `false`.

`pcntl_waitid` toma un argumento resource_usage adicional para recopilar varias métricas específicas de la plataforma sobre el proceso hijo.

### PDO_PGSQL

Pdo\Pgsql::copyFromArray ahora admite entradas `iterable`.

Pdo\Pgsql::setAttribute y Pdo\Pgsql::prepare permiten establecer `PDO::ATTR_PREFETCH` en 0, lo que activa el modo de carga diferida. En este modo, las sentencias no se pueden ejecutar en paralelo.

### PostgreSQL

`pg_copy_from` ahora admite entradas `iterable`.

`pg_connect` comprueba si el argumento connection_string contiene algún byte nulo.

`pg_close_stmt` comprueba si el argumento statement_name contiene algún byte nulo.

### POSIX

`posix_ttyname` establece last_error en EBADF cuando encuentra un descriptor de archivo no válido.

`posix_isatty` genera un mensaje `E_WARNING` cuando encuentra un descriptor de archivo no válido.

`posix_fpathconf` comprueba los descriptores de archivo no válidos y establece last_error en EBADF y genera un mensaje `E_WARNING`.

### Reflection

La salida de ReflectionClass::\_\_toString para enumeraciones ha cambiado para indicar mejor que la clase es una enumeración y que los casos de enumeración son casos de enumeración en lugar de constantes de clase normales.

La salida de ReflectionProperty::\_\_toString para propiedades con hooks ha cambiado para indicar qué hooks tiene la propiedad, si son finales y si la propiedad es virtual. Esto también afecta al resultado de ReflectionClass::\_\_toString cuando una clase contiene propiedades con hooks.

### Sockets

`socket_create`/`socket_bind` puede crear sockets de la familia `AF_PACKET`.

`socket_getsockname` obtiene el índice de la interfaz y su representación de string con el socket `AF_PACKET`.

### Zlib

El argumento `use_include_path` para las funciones `gzfile`, `gzopen` y `readgzfile` se ha cambiado de `int` a `bool`.

Las funciones `gzfile`, `gzopen` y `readgzfile` ahora respetan el contexto de flujo predeterminado.

## Otros cambios en las extensiones

### cURL

`curl_setopt` con el valor de la opción `CURLOPT_FOLLOWLOCATION` ya no se trata como booleano, sino como entero para manejar `CURLFOLLOW_OBEYCODE` y `CURLFOLLOW_FIRSTONLY`.

### Fileinfo

Actualizado file de 5.45 a 5.46.

El tipo de retorno de `finfo_close` se ha cambiado a `true`, en lugar de `bool`.

### Intl

El mecanismo interno de errores de Intl se ha modernizado para indicar con mayor precisión qué sitio de llamada causó qué error. Además, algunas excepciones de extensión/fecha ahora se encapsulan dentro de una `IntlException`.

### Lexbor

Se ha añadido una extensión Lexbor siempre habilitada. Contiene la biblioteca Lexbor que se separó de [ext/dom](#book.dom) para su reutilización en otras extensiones. La nueva extensión no está expuesta directamente al espacio de usuario.

### PCRE

Se actualizó pcre2lib de 10.44 a 10.46.

### PDO_Sqlite

Se incrementó el soporte de versión mínima de lanzamiento de 3.7.7 a 3.7.17.

### Readline

Los tipos de retorno de `readline_add_history`, `readline_clear_history` y `readline_callback_handler_install` se han cambiado a `true`, en lugar de `bool`.

### Reflection

`ReflectionConstant` ya no es final.

## Cambios en el manejo de archivos INI

### Núcleo

Añadido [fatal_error_backtraces](#ini.fatal-error-backtraces) para controlar si los errores fatales deben incluir un seguimiento de pila.

Añadida la configuración INI max_memory_limit, solo para el inicio, para controlar el máximo memory_limit que se puede configurar al inicio o durante la ejecución. Si se supera este valor, se genera una advertencia, a menos que se establezca en -1, lo cual establece memory_limit al valor actual de max_memory_limit.

### Opcache

Añadido opcache.file_cache_read_only para admitir un directorio [opcache.file_cache](#ini.opcache.file-cache) de solo lectura, para su uso con sistemas de archivos de solo lectura (p. ej., contenedores Docker de solo lectura). Se recomienda usarlo con `opcache.validate_timestamps=0`, `opcache.enable_file_override=1` y `opcache.file_cache_consistency_checks=0`.

> [!NOTE]
> Es posible que se ignore una caché generada con una compilación diferente de PHP, una ruta de archivo diferente, o una configuración diferente (incluidas las extensiones que se cargan).

El valor predeterminado de [opcache.jit_hot_loop](#ini.opcache.jit-hot-loop) ahora es 61 (un número primo) para evitar que sea múltiplo del número de iteraciones del bucle. Se recomienda establecer este parámetro en un número primo.

Modificar [opcache.memory_consumption](#ini.opcache.memory-consumption) cuando OPcache SHM ya está configurado ahora informará correctamente un fallo en lugar de no hacer nada silenciosamente y mostrar valores engañosos en PHPInfo.

### OpenSSL

Añadido openssl.libctx para seleccionar el tipo de contexto de la biblioteca OpenSSL. Se puede usar un contexto de biblioteca personalizado para cada hilo o un único contexto de biblioteca global (predeterminado). Se puede utilizar una biblioteca libctx personalizada para cada hilo o una única biblioteca libctx global (predeterminada).

## Rendimiento

### Núcleo

Eliminados los OPcodes para comparaciones de identidad con valores booleanos, en particular para el patrón `match(true)`.

Añadida especialización de OPcode para comparaciones `=== []` y `!== []`.

La creación de objetos de excepción ahora es mucho más rápida.

Las partes del código que utilizaban SSE2 se han adaptado para utilizar también SIMD con ARM NEON.

Se introdujo la máquina virtual TAILCALL, habilitada por defecto al compilar con Clang\>=19 en x86_64 o aarch64. La máquina virtual TAILCALL es tan rápida como la máquina virtual HYBRID utilizada al compilar con GCC. Esto hace que los binarios de PHP compilados con Clang\>=19 sean tan rápidos como los binarios compilados con GCC. El rendimiento de la máquina virtual CALL, utilizada con otros compiladores, también ha mejorado considerablemente.

### Intl

Ahora se evita la creación de copias adicionales de strings al convertir strings para su uso en el intercalador.

### MBString

Las partes del código que utilizaban SSE2 se han adaptado para utilizar también SIMD con ARM NEON.

### Opcache

Mejora del rendimiento en la recuperación de variables TLS en código compilado con JIT en compilaciones que no utilizan Glibc.

### Reflection

Mejorado el rendimiento de los siguientes métodos: ReflectionProperty::getValue, ReflectionProperty::getRawValue, ReflectionProperty::isInitialized, ReflectionProperty::isInitialized, ReflectionProperty::setValue, ReflectionProperty::setRawValue

### SPL

Mejorado el rendimiento de los métodos y accesores de dimensiones de `SplFixedArray`.

### Estándar

Mejorado el rendimiento de las funciones array con funciones de devoluciones de llamada (`array_find`, `array_filter`, `array_map`, `usort`, ...).

Mejorado el rendimiento de `urlencode` y `rawurlencode`.

Mejorado el rendimiento de `unpack` con repeticiones sin nombre al evitar la creación de strings temporales y su posterior análisis.

Mejorado el rendimiento de `pack`.

Mejoras menores en el rendimiento de `array_chunk`.

### XML

Mejorado el rendimiento del acceso a las propiedades de `XMLReader`.

Mejorado el rendimiento de `XMLWriter` y consumo de memoria reducido.
