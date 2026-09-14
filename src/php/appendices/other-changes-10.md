---
title: Otros cambios
source_url: https://www.php.net/manual/es/migration84.other-changes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration84/other-changes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: 858400b07
order: 1150
---

## Otros cambios

## Cambios en el núcleo

### Clausuras

Los nombres de las clausuras se han ajustado para incluir el nombre de la función padre y la línea de definición para hacerlos más fáciles de distinguir, por ejemplo, en las trazas de pila.

### Fibras

Ahora se permiten las conmutaciones de fibras durante la ejecución del destructor. Esto estaba previamente bloqueado debido a conflictos con la recolección de basura.

Los destructores ahora pueden ejecutarse en una fibra separada:

Cuando el recolector de basura se activa en una fibra, los destructores llamados por el recolector de basura se ejecutan en una fibra separada: la gc_destructor_fiber. Si esta fibra se suspende, se crea una nueva para ejecutar los destructores restantes. La gc_destructor_fiber anterior ya no es referenciada por el recolector de basura y puede ser recolectada si ya no es referenciada en otro lugar. Los objetos cuyo destructor está suspendido no serán recolectados hasta que el destructor regrese o hasta que la `Fiber` sea recolectada.

### Manejadores de salida

Los flags de estado de los manejadores de salida pasados al parámetro `flags` de `ob_start` ahora se borran.

`output_add_rewrite_var` ahora usa [`url_rewriter.hosts`](#ini.url-rewriter.hosts) en lugar de [`session.trans_sid_hosts`](#ini.session.trans-sid-hosts) para la selección de los hosts que serán reescritos.

## Cambios en los módulos SAPI

### apache2handler

Se ha eliminado el soporte para Apache 2.0 y 2.2 EOL. La versión mínima de Apache requerida ahora es 2.4.

### CLI

El servidor integrado busca un archivo índice de manera recursiva recorriendo los directorios padres si no se puede localizar el archivo especificado. Este proceso anteriormente se ignoraba si la ruta parecía referirse a un archivo, es decir, si el último componente de la ruta contenía un punto. En ese caso, se devolvía un error 404. El comportamiento se ha modificado para buscar un archivo índice en todos los casos.

### FPM

Ahora se tendrá éxito al vaciar las cabeceras sin cuerpo.

La página de estado ahora tiene un nuevo campo para mostrar un pico de memoria.

Se ha eliminado la configuración `/dev/poll` de `events.mechanism` para Solaris/Illumos.

## Funciones cambiadas

### Núcleo

`trigger_error` y `user_error` ahora tienen un tipo de retorno de `true` en lugar de `bool`.

### DOM

DOMDocument::registerNodeClass ahora tiene un tipo de retorno de `true` en lugar de `bool`. Solo podía devolver `true` en la práctica.

### Hash

`hash_update` ahora tiene un tipo de retorno de `true` en lugar de `bool`. Solo podía devolver `true` en la práctica.

### Intl

`NumberFormatter::ROUND_TOWARD_ZERO` y `NumberFormatter::ROUND_AWAY_FROM_ZERO` se han añadido como alias para `NumberFormatter::ROUND_DOWN` y `NumberFormatter::ROUND_UP` para ser coherentes con los nuevos modos `PHP_ROUND_*`.

ResourceBundle::get ahora tiene un tipo de retorno provisional de `ResourceBundle|array|string|int|null`.

Las funciones `idn_to_ascii` y `idn_to_utf8` ahora siempre lanzan excepciones ValueError si el nombre de `domain` está vacío o es demasiado largo.

Las funciones `idn_to_ascii` y `idn_to_utf8` ahora siempre lanzan excepciones ValueError si el parámetro `variant` no es `INTL_IDNA_VARIANT_UTS46`.

### LibXML

`libxml_set_streams_context` ahora lanza inmediatamente una TypeError cuando se pasa un recurso no contextual de flujo a la función, en lugar de lanzar más tarde cuando se usa el contexto de flujo.

### MBString

El comportamiento de `mb_strcut` ahora es más coherente en cadenas UTF-8 y UTF-16 no válidas. No hay cambio de comportamiento para cadenas UTF-8 y UTF-16 válidas.

### ODBC

El `row` de `odbc_fetch_object`, `odbc_fetch_array`, de `odbc_fetch_into` ahora tiene un valor predeterminado de `null`, manteniéndose coherente con `odbc_fetch_row`. Anteriormente, los valores predeterminados eran `-1`, `-1`, y `0`, respectivamente.

### OpenSSL

El `extra_attributes` en `openssl_csr_new` establece los atributos del CSR en lugar del DN del sujeto, lo cual se hacía incorrectamente antes.

El `dn` en `openssl_csr_new` permite establecer un `array` de valores para una sola entrada.

Se ha añadido un nuevo `serial_hex` a `openssl_csr_sign` para permitir establecer números de serie en formato hexadecimal.

Analizar un ASN.1 UTCTime con `openssl_x509_parse` falla si se omiten los segundos para versiones de OpenSSL anteriores a 3.2 (`-1` se devuelve para dichos campos). Las versiones de OpenSSL superiores a 3.3 ya no cargaban dichos certificados.

### PDO

Ahora es posible recuperar el valor del atributo `PDO::ATTR_STRINGIFY_FETCHES` con PDO::getAttribute.

Se ha añadido una nueva constante `Pdo\Pgsql::ATTR_RESULT_MEMORY_SIZE` para recuperar el uso de memoria de los resultados de consulta con PDO::getAttribute para los controladores que lo soportan.

### PDO_FIREBIRD

Ahora es posible recuperar el valor de los atributos `FB_ATTR_DATE_FORMAT`, `FB_ATTR_TIME_FORMAT`, `FB_ATTR_TIMESTAMP_FORMAT`, con PDO::getAttribute.

Se han añadido nuevos atributos para especificar el nivel de aislamiento de transacción y el modo de acceso. Se han añadido cinco constantes relacionadas con esta funcionalidad: `Pdo\Firebird::TRANSACTION_ISOLATION_LEVEL`, `Pdo\Firebird::READ_COMMITTED`, `Pdo\Firebird::REPEATABLE_READ`, `Pdo\Firebird::SERIALIZABLE`, `Pdo\Firebird::WRITABLE_TRANSACTION`

Al usar conexiones persistentes, ahora hay una verificación de liveness en el constructor.

El contenido que se construye cambia según el valor de `FB_API_VER` en `ibase.h`. Un nuevo método estático Pdo\Firebird::getApiVersion puede usarse para obtener esta información. Esta información también se referencia ahora en `phpinfo`.

Ahora hay cinco nuevos tipos de datos disponibles: `INT128`, `DEC16`, `DEC34`, `TIMESTAMP_TZ`, `TIME_TZ` . Estos están disponibles a partir de Firebird 4.0.

### PDO_MYSQL

Ahora es posible recuperar el valor del atributo `PDO::ATTR_FETCH_TABLE_NAMES` con PDO::getAttribute.

### PDO_PGSQL

Soporte para recuperar el uso de memoria de consultas para `Pdo\Pgsql::ATTR_RESULT_MEMORY_SIZE`.

Si la columna es de tipo `FLOAT4OID` o `FLOAT8OID` el valor ahora se devolverá como `float` en lugar de una `string`.

### PGSQL

El parámetro `conditions` de `pg_select` ahora es opcional y acepta un array vacío.

### Phar

Los métodos Phar::setAlias, Phar::setDefaultStub ahora pueden tener un tipo de retorno provisional de `true` en lugar de `bool`.

### POSIX

`posix_isatty` ahora establece el número de error cuando el argumento del descriptor de archivo/flujo es inválido.

### Reflection

ReflectionGenerator::getFunction ahora puede ser llamado después de que el generador haya terminado de ejecutarse.

### Sockets

El parámetro `backlog` de `socket_create_listen` ahora tiene un valor predeterminado de `SOMAXCONN`. Anteriormente, era `128`.

### Sodium

Las funciones `sodium_crypto_aead_aes256gcm_*` ahora están disponibles en procesadores aarch64 con extensiones criptográficas ARM.

### SPL

Los métodos SplPriorityQueue::insert, SplPriorityQueue::recoverFromCorruption, SplHeap::insert, SplHeap::recoverFromCorruption ahora pueden tener un tipo de retorno provisional de `true` en lugar de `bool`.

`SplObjectStorage` ahora implementa SeekableIterator.

### Estándar

El valor predeterminado del `'cost'` para el algoritmo de hashing `PASSWORD_BCRYPT` usado por la función `password_hash` se ha incrementado de `10` a `12`.

`debug_zval_dump` ahora indica si un array está compactado.

`long2ip` ahora tiene un tipo de retorno de `string` en lugar de `string|false`.

`highlight_string` ahora tiene un tipo de retorno de `string|true` en lugar de `string|bool`.

`print_r` ahora tiene un tipo de retorno de `string|true` en lugar de `string|bool`.

#### Redondeo con `round`

El parámetro `mode` de la función `round` se ha ampliado para aceptar `RoundingMode|int`, aceptando instancias de un nuevo enumerador `RoundingMode`.

Se han añadido cuatro nuevos modos a la función `round`: RoundingMode::PositiveInfinity, RoundingMode::NegativeInfinity, RoundingMode::TowardsZero, RoundingMode::AwayFromZero

La implementación interna del redondeo a enteros se ha reescrito para ser más fácil de verificar para la corrección y más fácil de mantener. Se corrigieron algunos errores de redondeo como resultado de la reescritura. Por ejemplo, anteriormente, redondear `0.49999999999999994` al entero más cercano habría dado `1.0` en lugar del resultado correcto `0.0`. Otras entradas también podrían verse afectadas y dar resultados diferentes en comparación con versiones anteriores de PHP.

Se corrigió un error causado por el "preredondeo" de la función `round`. Anteriormente, usando "preredondeo" para manejar un valor como `0.285` (en realidad `0.28499999999999998`) como un número decimal y redondearlo a `0.29`. Sin embargo, el "preredondeo" redondeaba incorrectamente algunos números, por lo que esta corrección elimina el "preredondeo" y cambia la forma en que se comparan los números, por lo que los valores se redondean correctamente como números decimales.

El número máximo de dígitos significativos que `round` puede manejar se ha ampliado en un dígito. Por ejemplo, `round(4503599627370495.5)` devolvía `4503599627370495.5`, pero ahora devuelve `4503599627370496`.

## Otros cambios en las extensiones

### cURL

La versión mínima requerida de libcurl ahora es 7.61.0.

La opción `CURLOPT_DNS_USE_GLOBAL_CACHE` ya no tiene ningún efecto y se ignora silenciosamente. Esta funcionalidad subyacente se desaprobó en libcurl 7.11.1, y se eliminó en libcurl 7.62.0.

### GMP

Cambiar el tipo de un objeto `GMP` a `bool` ahora es posible en lugar de generar un `E_RECOVERABLE_ERROR`. El comportamiento de conversión está sobrecargado de manera que un objeto `GMP` que represente el valor `0` se convierte en `false`.

### LibXML

La versión mínima requerida de libxml2 ahora es 2.9.4.

### Intl

El comportamiento de la clase Intl se ha normalizado para siempre lanzar excepciones Error al intentar usar un objeto no inicializado, o cuando la clonación falla.

### MBString

Las tablas de datos Unicode se han actualizado a Unicode 16.0.

### MySQLnd

Se ha añadido soporte para el nuevo tipo de datos VECTOR de MySQL 9.

### OpenSSL

La versión mínima requerida de OpenSSL ahora es 1.1.1.

### PDO_PGSQL

La versión mínima requerida de libpq ahora es 10.0.

### PGSQL

La versión mínima requerida de libpq ahora es 10.0.

### SPL

Los accesos fuera de límites en `SplFixedArray` ahora lanzan excepciones de tipo OutOfBoundsException en lugar de RuntimeException. Como OutOfBoundsException es una clase hija de RuntimeException, no se observa ningún cambio de comportamiento al intentar capturar estas excepciones.

### XSL

Las propiedades tipadas XSLTProcessor::\$cloneDocument y XSLTProcessor::\$doXInclude ahora están declaradas.

### Zlib

La versión mínima requerida de zlib ahora es 1.2.11.

## Rendimiento

### Núcleo

Mejora del rendimiento del análisis y la generación de números de punto flotante en construcciones ZTS bajo cargas muy concurrentes. Esto afecta a las funciones `printf` así como a las funciones de serialización como `json_encode` o `serialize`.

`sprintf` usando solo `%s` y la interpolación de cadena `%d` se compilará en la interpolación de cadena equivalente, evitando los costos de una llamada a función y el análisis repetido de la cadena de formato.

### BCMath

Mejora del rendimiento de las conversiones de números y las operaciones.

### DOM

El rendimiento de DOMNode::C14N se mejora enormemente para el caso sin consulta xpath. Esto puede dar una mejora de tiempo fácilmente de dos órdenes de magnitud para documentos con decenas de miles de nodos.

Mejora del rendimiento y reducción del consumo de memoria de la serialización XML.

Reducción del consumo de memoria de las clases de nodos.

### FTP

Mejora del rendimiento de las subidas FTP hasta un factor de 10x para las subidas voluminosas.

### Hash

Se han añadido las implementaciones SSE2 y SHA-NI de SHA-256. Esto mejora el rendimiento en procesadores compatibles de ~1.3x (SSE2), y 3x - 5x (SHA-NI). Crédito a Colin Percival / Tarsnap por esta optimización.

### MBString

`mb_strcut` ahora es mucho más rápido para cadenas UTF-8 y UTF-16.

La búsqueda de nombres de codificación mbstring ahora es mucho más rápida.

El rendimiento de la conversión de SJIS-win a Unicode se mejora enormemente.

### MySQLnd

Mejora del rendimiento de la cotización MySQLnd.

### PCRE

Mejora del rendimiento de los grupos de captura nombrados.

### Random

Mejora del rendimiento de `Random\Randomizer`, con un enfoque específico en los métodos Random\Randomizer::getBytes, y Random\Randomizer::getBytesFromString().

### SimpleXML

Mejora del rendimiento y reducción del consumo de memoria de la serialización XML.

### Estándar

El rendimiento de `strspn` y `strcspn` se mejora enormemente. Ahora se ejecutan en tiempo lineal en lugar de estar limitados por un tiempo cuadrático.

Mejora del rendimiento de `strpbrk`.

`get_browser` ahora es mucho más rápido, hasta 1.5x - 2.5x para algunos casos de prueba.
