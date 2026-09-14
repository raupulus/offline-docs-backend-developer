---
title: Otros cambios
source_url: https://www.php.net/manual/es/migration83.other-changes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration83/other-changes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: 4de6272a1
order: 1060
---

## Otros cambios

## Cambios en el núcleo

### FFI

FFI::load ahora está permitido durante la precarga cuando [opcache.preload_user](#ini.opcache.preload-user) es el usuario del sistema actual. Anteriormente, llamar a FFI::load no era posible durante la precarga si la directiva [opcache.preload_user](#ini.opcache.preload-user) estaba definida.

### FPM

Las pruebas CLI de FPM ahora fallan si la ruta del socket es más larga de lo que el SO soporta.

### Opcache

En las SAPI CLI y phpdbg, la precarga ya no requiere que la directiva [opcache.preload_user](#ini.opcache.preload-user) esté definida cuando PHP se ejecuta como root. En otras SAPI, esta directiva es requerida cuando PHP se ejecuta como root porque la precarga se realiza antes de que la SAPI cambie a un usuario no privilegiado.

### Streams

Bloquear `fread` en una conexión de socket ahora devuelve inmediatamente si hay datos almacenados en búfer en lugar de esperar más datos.

Un stream de memoria ya no devuelve un error si el desplazamiento de búsqueda está más allá del final. En su lugar, la memoria se incrementará en la próxima escritura y los datos entre el final anterior y el desplazamiento se llenarán con ceros, similar a cómo funcionan los archivos.

Las operaciones de acceso `stat` como `file_exists` y similares ahora usarán la ruta real en lugar de la ruta del stream. Esto es coherente con la apertura del stream.

## Cambios en los módulos SAPI

### CLI

Los streams `STDOUT`, `STDERR` y `STDIN` ya no se cierran al destruir el recurso lo cual ocurre principalmente cuando el CLI termina. Sin embargo, aún es posible cerrar explícitamente estos streams usando `fclose` y similares.

## Funciones cambiadas

### Núcleo

`gc_status` ha añadido los siguientes 8 campos: `"running"` =\> bool, `"protected"` =\> bool, `"full"` =\> bool, `"buffer_size"` =\> int, `"application_time"` =\> float: El tiempo total de aplicación, en segundos (incluyendo el tiempo de recolección), `"collector_time"` =\> float: El tiempo pasado recolectando ciclos, en segundos (incluyendo el tiempo de destructor y el tiempo de liberación), `"destructor_time"` =\> float: El tiempo pasado ejecutando los destructores durante la recolección de ciclos, en segundos, `"free_time"` =\> float: El tiempo pasado liberando valores durante la recolección de ciclos, en segundos

`class_alias` ahora soporta la creación de un alias en clases internas.

Cambiar [open_basedir](#ini.open-basedir) en tiempo de ejecución usando `ini_set('open_basedir', ...);` ya no acepta rutas que contengan el directorio padre (`..`). Anteriormente, solo las rutas que comenzaban con `..` estaban prohibidas. Esto podía ser fácilmente eludido prefijando la ruta con `./`.

Los manejadores de excepciones de usuario ahora capturan excepciones durante el apagado.

El HTML resultante de `highlight_string` y `highlight_file` ha cambiado. Los espacios entre las etiquetas HTML externas son eliminados. Los saltos de línea y los espacios ya no se convierten en entidades HTML. Todo el HTML ahora está envuelto en una etiqueta `<pre>`. La etiqueta `<span>` externa se ha fusionado con la etiqueta `<code>`.

### Calendar

`easter_date` ahora soporta años desde 1970 a 2,000,000,000 en sistemas de 64 bits, anteriormente solo soportaba años desde 1970 a 2037.

### Curl

`curl_getinfo` ahora soporta dos nuevas constantes: `CURLINFO_CAPATH` y `CURLINFO_CAINFO`. Si la opción es `null`, las siguientes claves estarán presentes: `"capath"` y `"cainfo"`.

### DOM

El tipo de retorno de DOMCharacterData::appendData ha sido cambiado a `true`.

DOMDocument::loadHTML, DOMDocument::loadHTMLFile, y DOMDocument::loadXML ahora tienen un tipo de retorno provisional de `bool`. Anteriormente, esto estaba documentado como teniendo un tipo de retorno de `DOMDocument|bool`, pero, desde PHP 8.0.0, `DOMDocument` no puede ser devuelto porque ya no es llamable estáticamente.

### Gd

La firma de `imagerotate` ha cambiado. El parámetro `ignore_transparent` ha sido eliminado, porque ha sido ignorado desde PHP 5.5.0.

### Intl

`datefmt_set_timezone` (y sus alias IntlDateformatter::setTimeZone) ahora devuelve `true` en caso de éxito, anteriormente devolvía `null`.

IntlBreakiterator::setText ahora devuelve `false` en caso de fallo, anteriormente devolvía `null`. Ahora devuelve `true` en caso de éxito, anteriormente devolvía `null`.

IntlChar::enumCharNames ahora devuelve un booleano. Anteriormente, devolvía `null` en caso de éxito y `false` en caso de fallo.

IntlDateFormatter::\_\_construct lanza una excepción `U_ILLEGAL_ARGUMENT_ERROR` cuando se establece una localización inválida.

### MBString

`mb_strtolower` y `mb_convert_case` implementan reglas de conversión de mayúsculas condicionales para la letra griega sigma. Para `mb_strtolower`, la conversión condicional se aplica solo a los modos `MB_CASE_LOWER`, y `MB_CASE_TITLE`, no a los modos `MB_CASE_LOWER_SIMPLE` y `MB_CASE_TITLE_SIMPLE`.

`mb_decode_mimeheader` interpreta los guiones bajos en las palabras codificadas MIME QPrint como requiere la RFC 2047; se convierten en espacios. Los guiones bajos deben ser codificados como `"=5F"` en tales palabras codificadas MIME.

En raros casos, `mb_encode_mimeheader` codificará su cadena de entrada donde la pasaría como ASCII puro en PHP 8.2.

`mb_encode_mimeheader` ya no elimina los bytes NUL (cero) al codificar QPrint de la cadena de entrada. Esto anteriormente corrompía las cadenas en algunos codificados de texto, especialmente UTF-16 y UTF-32, por mb_encode_mimeheader.

`mb_detect_encoding` en modo "no estricto" ahora se comporta como se describe en la documentación. Anteriormente, devolvía `false` si el mismo byte (por ejemplo, el primer byte) de la cadena de entrada era inválido en todos los codificados candidatos. Más generalmente, eliminaba los codificados candidatos de la consideración cuando se veía un byte inválido, y si el mismo byte de entrada eliminaba todos los codificados restantes aún bajo consideración, devolvía `false`. Por otro lado, si todos los codificados candidatos excepto uno eran eliminados de la consideración, devolvía el último restante sin tener en cuenta el número de errores de codificación que podrían encontrarse más adelante en la cadena. Esto es diferente del comportamiento descrito en la documentación, que dice: "Si strict está definido en false, se devolverá el codificado más cercano."

### mysqli

`mysqli_fetch_object` ahora lanza una `ValueError` en lugar de una `Exception` cuando el argumento `constructor_args` no está vacío con la clase no teniendo un constructor.

`mysqli_poll` ahora lanza una `ValueError` cuando ni el argumento `read` ni el argumento `error` son pasados.

`mysqli_field_seek` y mysqli_result::field_seek ahora especifican el tipo de retorno como `true` en lugar de `bool`.

### ODBC

`odbc_autocommit` ahora acepta `null` para el parámetro `enable`. Pasar `null` tiene el mismo comportamiento que pasar un solo parámetro, indicando si la funcionalidad autocommit está habilitada o no.

### PGSQL

`pg_fetch_object` ahora lanza una `ValueError` en lugar de una `Exception` cuando el argumento `constructor_args` no está vacío con la clase no teniendo un constructor.

`pg_insert` ahora lanza una `ValueError` en lugar de una `E_WARNING` cuando la tabla especificada es inválida.

`pg_insert` y `pg_convert` lanzan una `ValueError` o una `TypeError` en lugar de un `E_WARNING` cuando el valor/tipo de un campo no coincide correctamente con el tipo de PostgreSQL.

El parámetro `row` de `pg_fetch_result`, `pg_field_prtlen`, y `pg_field_is_null` ahora es nullable.

### Random

Cambio de `mt_srand` y `srand` para no verificar el número de argumentos para determinar si se debe usar una semilla aleatoria. Pasar `null` generará una semilla aleatoria, `0` usará cero como semilla. Las funciones ahora son coherentes con Random\Engine\Mt19937::\_\_construct.

### Reflection

El tipo de retorno de ReflectionClass::getStaticProperties ya no es nullable.

### Estándar

El `E_NOTICE` emitido por `unserialize` ha sido promovido a `E_WARNING`.

`unserialize` ahora emite un `E_WARNING` si la entrada contiene bytes no consumidos.

`array_pad` ya no está limitado solo por el número máximo de elementos que un array puede contener. Anteriormente, solo era posible añadir un máximo de 1,048,576 elementos a la vez.

`strtok` ahora lanza un `E_WARNING` si el token no es proporcionado al iniciar la tokenización.

`password_hash` ahora encadena la excepción subyacente Random\RandomException como ValueError's `previous` Exception cuando falla la generación de sal.

Si un array es usado como `command` para `proc_open`, debe tener al menos un elemento no vacío. De lo contrario, se lanza una `ValueError`.

`proc_open` ahora devuelve `false` si el array `command` es un comando inválido en lugar de un objeto de recurso que produce una advertencia más tarde. Esto ya era el caso para Windows, pero ahora también es el caso si se usa una implementación posix_spawn (la mayoría de las plataformas Linux, BSD y MacOS). Sigue habiendo algunas plataformas antiguas donde este comportamiento no ha cambiado porque posix_spawn no es soportado allí.

`array_sum` y `array_product` ahora emiten una advertencia cuando los valores del array no pueden ser convertidos en int/float. Anteriormente, los arrays y los objetos eran ignorados mientras que cada otro valor era convertido en int. Además, los objetos que definen una conversión numérica (por ejemplo [GMP](#book.gmp)) ahora son convertidos en lugar de ser ignorados.

El `decimals` de `number_format` ahora maneja enteros negativos. Redondear con un valor negativo para `decimals` significa que `num` es redondeado a `decimals` dígitos significativos antes del separador decimal. Anteriormente, los enteros negativos para `decimals` eran silenciosamente ignorados y el número era redondeado a cero decimales.

Se ha añadido un nuevo argumento `before_needle` a `strrchr`. Se comporta como su homólogo en las funciones `strstr` o `stristr`.

`str_getcsv` y `fgetcsv` ahora devuelven una cadena vacía en lugar de una cadena con un solo byte nulo para el último campo que solo contiene un cierre no terminado.

## Otros cambios en las extensiones

### Núcleo

Usar los operadores de [incremento/decremento](#language.operators.increment) (`++`/`--`) en valores de tipo `bool` ahora emite advertencias. Esto se debe a que actualmente no tiene ningún efecto, pero se comportará como `$bool += 1` en el futuro.

Usar el operador de [decremento](#language.operators.increment) (`--`) en valores de tipo `null` ahora emite advertencias. Esto se debe a que actualmente no tiene ningún efecto, pero se comportará como `$null -= 1` en el futuro.

Los objetos internos que implementan un cast \_IS_NUMBER pero no un gestionador do_operator que reemplace la adición y la sustracción ahora pueden ser incrementados y decrementados como si se hiciera `$o += 1` o `$o -= 1`.

### DOM

El mecanismo de duración de vida del DOM ha sido retrabajado de tal manera que los nodos implícitamente eliminados aún pueden ser recuperados. Anteriormente, esto causaba una excepción.

### SQLite3

La clase `SQLite3` ahora lanza una `SQLite3Exception` (extensión de `Exception`) en lugar de `Exception`.

El código de error SQLite ahora se pasa en el código de error de la excepción en lugar de estar incluido en el mensaje de error.

## Cambio en la gestión del archivo INI

- Los parámetros INI `assert.*` han sido depreciados. Esto incluye los siguientes parámetros INI: [assert.active](#ini.assert.active), [assert.bail](#ini.assert.bail), [assert.callback](#ini.assert.callback), [assert.exception](#ini.assert.exception), [assert.warning](#ini.assert.warning) Si el valor del parámetro es igual al valor por defecto, no se emite ninguna advertencia de depreciación. El parámetro INI [zend.assertions](#ini.zend.assertions) debería usarse en su lugar.

- [zend.max_allowed_stack_size](#ini.zend.max-allowed-stack-size) es una nueva directiva INI para definir el tamaño máximo de la pila permitida. Los valores posibles son `0` (detectar el tamaño máximo de la pila del proceso o del hilo), `-1` (sin límite), o un número positivo de bytes. El valor por defecto es `0`. Cuando no es posible detectar el tamaño máximo de la pila del proceso o del hilo, se usa un valor por defecto del sistema conocido. Definir este valor demasiado alto tiene el mismo efecto que deshabilitar el límite de tamaño de la pila. Las fibras usan [fiber.stack_size](#ini.fiber.stack-size) como tamaño máximo de la pila permitida. Se lanza una `Error` cuando la pila de llamadas del proceso excede [zend.max_allowed_stack_size](#ini.zend.max-allowed-stack-size)-[zend.reserved_stack_size](#ini.zend.reserved-stack-size) bytes, para evitar errores de segmentación debidos a un desbordamiento de pila, con el objetivo de facilitar la depuración. El tamaño de la pila aumenta durante las recursiones no controladas que involucran funciones internas o los métodos mágicos [\_\_toString()](#object.tostring), [\_\_clone()](#object.clone), [\_\_sleep()](#object.sleep), [\_\_destruct()](#object.destruct). Esto no está relacionado con los desbordamientos de buffer de pila, y no es una característica de seguridad.

- [zend.reserved_stack_size](#ini.zend.reserved-stack-size) es una nueva directiva INI para definir el tamaño de la pila reservada, en bytes. Esto se resta del tamaño máximo de la pila permitida, como un buffer, al verificar el tamaño de la pila.

## Rendimiento

### DOM

Iterar sobre un `DOMNodeList` ahora usa un caché. Por lo tanto, solicitar elementos ya no toma tiempo cuadrático por defecto.

Obtener el contenido textual de los nodos ahora evita una asignación, lo que resulta en una mejora de rendimiento.

DOMChildNode::remove ahora se ejecuta en O(1) rendimiento.

### Estándar

La bandera `file` para la verificación de errores ahora es aproximadamente un 7% más rápida.

### SPL

`RecursiveDirectoryIterator` ahora realiza menos E/S al recorrer un directorio.
