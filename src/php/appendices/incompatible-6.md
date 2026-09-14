---
title: Cambios incompatibles con versiones anteriores
source_url: https://www.php.net/manual/es/migration74.incompatible.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration74/incompatible.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: c308ed37a
order: 700
---

## Cambios incompatibles con versiones anteriores

## Núcleo de PHP

### Acceso de tipo array a no-arrays

Intentar utilizar valores de tipo `null`, `bool`, `int`, `float` o `recurso` como un array (como `$null["clave"]`) generará ahora un aviso.

### Función `get_declared_classes`

La función `get_declared_classes` ya no devuelve las clases anónimas que no han sido instanciadas.

### Palabra clave `fn`

`fn` es ahora una palabra clave reservada. En particular, ya no puede ser utilizada como una función o un nombre de clase. Puede seguir siendo utilizada como una método o un nombre de constante de clase.

### `<?php` etiqueta al final del fichero

`<?php` al final del fichero (sin nueva línea) será ahora interpretado como una etiqueta PHP de apertura. Anteriormente, era interpretado como una etiqueta corta de apertura seguida de una `php` literal y resultaba en un error de sintaxis (con `short_open_tag=1`) o era interpretado como una cadena `<?php` (con `short_open_tag=0`).

### Filtros de flujo

Al utilizar include/require en un flujo, streamWrapper::stream_set_option será invocado con la opción `STREAM_OPTION_READ_BUFFER`. Las implementaciones de filtros de flujo personalizados pueden necesitar implementar el método streamWrapper::stream_set_option para evitar un aviso (devolver siempre `false` es una implementación suficiente).

### Serialización

El formato `o` de serialización ha sido eliminado. Como nunca es producido por PHP, esto solo puede romper la deserialización de cadenas construidas manualmente.

### Constantes de algoritmo de contraseña

Los identificadores de algoritmo de hash de contraseña son ahora cadenas nullables en lugar de enteros.

- `PASSWORD_DEFAULT` era el entero 1; ahora es la cadena '2y' (en PHP 7.4.0, 7.4.1, y 7.4.2 era `null`)

- `PASSWORD_BCRYPT` era el entero 1; ahora es '2y'

- `PASSWORD_ARGON2I` era el entero 2; ahora es 'argon2i'

- `PASSWORD_ARGON2ID` era el entero 3; ahora es 'argon2id'

Las aplicaciones que utilizan correctamente las constantes PASSWORD_DEFAULT, PASSWORD_BCRYPT, PASSWORD_ARGON2I, y PASSWORD_ARGON2ID continuarán funcionando correctamente.

### Función `htmlentities`

`htmlentities` generará ahora un aviso (en lugar de un aviso de normas estrictas) si se utiliza con una codificación para la cual solo la sustitución de entidad básica es soportada, en cuyo caso es equivalente a `htmlspecialchars`.

### Funciones `fread` y `fwrite`

`fread` y `fwrite` devolverán ahora `false` si la operación falla. Anteriormente, una cadena vacía o 0 era devuelta. EAGAIN/EWOULDBLOCK no son considerados como fallos.

Estas funciones también generan un aviso en caso de fallo, por ejemplo, cuando se intenta escribir en un recurso de fichero de solo lectura.

## BCMath: matemáticas de precisión arbitraria

Las funciones BCMath advertirán ahora si se adopta un número mal formado, como `"32foo"`. El argumento será interpretado como cero, como antes.

## CURL

Intentar serializar una clase `CURLFile` generará ahora una excepción. Anteriormente, la excepción solo era lanzada en la deserialización.

El uso de `CURLPIPE-HTTP1` está deprecado y ya no es soportado a partir de cURL 7.62.0.

El parámetro `$version` de `curl_version` está deprecado. Si un valor no es igual al valor por omisión `CURLVERSION_NOW` es pasado, se genera un aviso y el parámetro es ignorado.

## Fecha y hora

Llamar a `var_dump` o similar en una instancia de `DateTime` o `DateTimeImmutable` ya no dejará propiedades accesibles en el objeto.

La comparación de objetos `DateInterval` (utilizando `==`, `<`, etc.) generará ahora un aviso y siempre devolverá `false`. Anteriormente, todos los objetos `DateInterval` eran considerados como iguales, a menos que tuvieran propiedades.

## Intl

El valor por omisión del parámetro de `idn_to_ascii` y `idn_to_utf8` es ahora `INTL_IDNA_VARIANT_UTS46` en lugar del valor desaconsejado `INTL_IDNA_VARIANT_2003`.

## MySQLi

La funcionalidad del servidor integrado ha sido eliminada. Ha estado rota desde al menos PHP 7.0.

La propiedad no documentada `mysqli::$stat` ha sido eliminada en favor de mysqli::stat.

## OpenSSL

La función `openssl_random_pseudo_bytes` lanza una excepción en situaciones de error, similar a `random_bytes`. En particular, una `Error` es lanzada si el número de bytes solicitados es inferior o igual a cero, y una `Exception` es lanzada si no se puede recoger un carácter aleatorio suficiente. El argumento de salida `$crypto_strong` está garantizado de ser siempre `true` si la función no lanza una excepción, por lo que no es necesario verificarlo explícitamente.

## Expresiones regulares (compatible Perl)

Cuando se utiliza el modo `PREG_UNMATCHED_AS_NULL`, los grupos de captura no encontrados serán ahora también establecidos a `null` (o `[null, -1]` si la captura offset está activada). Esto significa que el tamaño de `$matches` será siempre el mismo.

## PHP Data Objects (PDO)

Un intento de serialización de una instancia de `PDO` o `PDOStatement` generará ahora una `Exception` en lugar de una `PDOException`, compatible con otras clases internas que no soportan la serialización.

## Reflection

Los objetos Reflection generan ahora una excepción si se intenta serializarlos. La serialización de objetos Reflection nunca ha sido soportada y ha dado lugar a objetos Reflection corruptos. Ha sido explícitamente prohibido ahora.

El valor de las constantes de clase de `ReflectionClassConstant`, `ReflectionMethod` y `ReflectionProperty` han sido cambiados.

## Biblioteca PHP estándar (SPL)

La llamada `get_object_vars` en una instancia de `ArrayObject` devolverá siempre las propiedades del `ArrayObject` mismo (o de una subclase). Anteriormente, devolvía los valores del array/objeto a menos que el flag `ArrayObject::STD_PROP_LIST` hubiera sido especificado.

Las otras operaciones afectadas son las siguientes:

- ReflectionObject::getProperties

- `reset`, `current`, etc. Utilizar en su lugar los métodos de Iterator.

- Potencialmente otras funciones que trabajan en las propiedades del objeto como una lista, e.g. `array_walk`.

Las modificaciones de tipo `(array)` no están afectadas. Continuarán devolviendo ya sea el array envuelto, ya sea las propiedades `ArrayObject`, dependiendo de si el flag `ArrayObject::STD_PROP_LIST` es utilizado.

SplPriorityQueue::setExtractFlags lanzará una excepción si se pasa cero. Anteriormente, esto generaría un error fatal recuperable en la próxima operación de extracción.

`ArrayObject`, `ArrayIterator`, `SplDoublyLinkedList` y `SplObjectStorage` manejan ahora `__serialize()` y `__unserialize()` además de la interfaz Serializable. Esto significa que las cargas útiles de serialización creadas en versiones antiguas de PHP pueden seguir siendo deserializadas, pero las nuevas cargas útiles creadas por PHP 7.4 no serán compatibles con las versiones antiguas.

## Tokenizer

`token_get_all` emitirá ahora un token `T-BAD-CHARACTER` para caracteres inesperados en lugar de dejar agujeros en el flujo de tokens.

## Cookies entrantes

Desde PHP 7.4.11, los *nombres* de las cookies entrantes ya no son url-decodificados por razones de seguridad.
