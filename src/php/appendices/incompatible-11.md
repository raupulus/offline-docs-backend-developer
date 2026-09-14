---
title: Cambios incompatibles con versiones anteriores
source_url: https://www.php.net/manual/es/migration84.incompatible.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration84/incompatible.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: 64dc79d6c
order: 1110
---

## Cambios incompatibles con versiones anteriores

Salvo mención contraria en esta sección, cada nueva [función](#migration84.new-functions), [clase, interfaz, enumeración](#migration84.new-classes), o [constante](#migration84.constants) puede provocar el lanzamiento de una excepción de redeclaración Error.

## Núcleo de PHP

### Cambio de comportamiento de `exit`

Las construcciones de lenguaje `exit` (y `die`) ahora se comportan más como una función. Esto significa que ahora pueden pasarse como `callable`s, son afectadas por la instrucción `strict_types`, y ahora realizan las coerciones de tipo habituales en lugar de convertir cualquier valor no entero en una cadena.

En consecuencia, pasar tipos no válidos a `exit` y `die` ahora siempre provoca el lanzamiento de una excepción TypeError.

### Recursión al comparar

Encontrar una recursión al comparar ahora provoca una excepción Error en lugar de un error fatal `E_ERROR`.

### Modificación indirecta de propiedades de solo lectura

La modificación indirecta de propiedades de solo lectura en `__clone()` ya no está permitida, por ejemplo, `$ref = &$this->readonly`. Ya estaba prohibido para la inicialización de solo lectura, y era un descuido en la implementación de la "reinicialización de solo lectura al clonar".

### Cambio de tipo de constantes

Las constantes `PHP_DEBUG` y `PHP_ZTS` ahora son de tipo `bool`. Anteriormente, eran de tipo `int`.

### Longitud del nombre de archivo temporal

El nombre de los archivos volcados y de los archivos creados por la función `tempnam` ahora es más largo en 13 bytes. La longitud total sigue dependiendo de la plataforma.

### Supresión del nivel de error `E_STRICT`

El nivel de error `E_STRICT` ha sido eliminado, porque ya no se utilizaba en el motor PHP. La constante `E_STRICT` también ha sido desaprobada.

## Constantes de clase de extensión ahora tipificadas

Las siguientes clases de extensión ahora declaran un tipo en sus constantes: [Date](#book.datetime), [Intl](#book.intl), [PDO](#book.pdo), [Reflection](#book.reflection), [SPL](#book.spl), [Sqlite](#book.sqlite3), [XMLReader](#book.xmlreader)

## Migración de recursos a objetos

Varios `resource`s han sido migrados a `object`s. La verificación del valor de retorno con `is_resource` debe ser reemplazada por verificaciones de `false`, a menos que se indique lo contrario.

### DBA

Las funciones [DBA](#book.dba) ahora aceptan y devuelven `Dba\Connection` en lugar de `resource`s `dba_connection`.

### ODBC

Las funciones [ODBC](#book.uodbc) ahora aceptan y devuelven `Odbc\Result` en lugar de `resource`s `odbc_result`.

Las funciones [ODBC](#book.uodbc) ahora aceptan y devuelven `Odbc\Connection` en lugar de `resource`s `odbc_connection`.

### SOAP

La propiedad SoapClient::\$httpurl ahora es un objeto `Soap\Url` en lugar de una `resource` `soap_url`. Las verificaciones con `is_resource` (por ejemplo `is_resource($client->httpurl)`) deben ser reemplazadas por verificaciones de `null` (por ejemplo `$client->httpurl !== null`).

La propiedad SoapClient::\$sdl ahora es un objeto `Soap\Sdl` en lugar de una `resource` `soap_sdl`. Las verificaciones con `is_resource` (por ejemplo `is_resource($client->sdl)`) deben ser reemplazadas por verificaciones de `null` (por ejemplo `$client->sdl !== null`).

## Nuevas alertas y excepciones

Se han añadido nuevas alertas y excepciones para señalar errores de programación, es decir, valores no válidos proporcionados como argumentos.

### Curl

`curl_multi_select` ahora lanza una ValueError si el parámetro `timeout` es inferior a `0` o superior a `PHP_INT_MAX`.

### Gd

`imagejpeg`, `imagewebp`, `imagepng`, `imageavif` ahora lanzan una ValueError si se pasa una `quality` no válida.

`imageavif` ahora lanza una ValueError si se pasa un parámetro `speed` no válido.

`imagescale` ahora lanza una ValueError si los parámetros `width` o `height` están fuera de los límites.

`imagescale` ahora lanza una ValueError si se pasa un valor de `mode` no válido.

`imagefilter` ahora lanza una ValueError con el filtro `IMG_FILTER_SCATTER` si los parámetros `sub` o `plus` están fuera de los límites.

### Gettext

`bind_textdomain_codeset`, `textdomain`, `d*gettext` ahora lanzan una ValueError si se pasa un `domain` no válido.

### Intl

`resourcebundle_get`, ResourceBundle::get, y el acceso a índices en un `ResourceBundle` ahora lanzan: TypeError para tipos de offset no válidos, ValueError para una cadena vacía, ValueError si el índice entero no cabe en un entero con signo de 32 bits

IntlDateFormatter::\_\_construct lanza una ValueError si el `locale` es no válido.

NumberFormatter::\_\_construct lanza una ValueError si el `locale` es no válido.

### MBString

`mb_encode_numericentity` y `mb_decode_numericentity` ahora verifican que `map` está compuesto únicamente por `int`s, si no es el caso, se lanza una ValueError.

`mb_http_input` ahora lanza una ValueError si el `type` es no válido.

`mb_http_output` ahora verifica que `encoding` no contiene caracteres nulos, si es el caso, se lanza una ValueError.

### ODBC

`odbc_fetch_row` devuelve `false` cuando `row` es inferior o igual a `0`. Ahora se emite una alerta en este caso.

### PCNTL

Las funciones `pcntl_sigprocmask`, `pcntl_sigwaitinfo`, y `pcntl_sigtimedwait` ahora lanzan: Una ValueError si el array `signals` está vacío (excepto para `pcntl_sigprocmask` si el `mode` es `SIG_SETMASK`), Una TypeError si un valor del array `signals` no es un `int`, Una ValueError si el valor de `signals` no es un número de señal válido

La función `pcntl_sigprocmask` ahora lanza una ValueError si el `mode` no es uno de los `SIG_BLOCK`, `SIG_UNBLOCK`, o `SIG_SETMASK`.

La función `pcntl_sigtimedwait` ahora lanza: Una ValueError si `seconds` es inferior a `0`, Una ValueError si `nanoseconds` es inferior a `0` o superior a `1e9`, Una ValueError si ambos `seconds` y `nanoseconds` son `0`

### Sesión

Establecer un valor no positivo para [session.gc_divisor](#ini.session.gc-divisor) o un valor negativo para [session.gc_probability](#ini.session.gc-probability) emite ahora una advertencia.

### SimpleXML

Llamar a `simplexml_import_dom` con un objeto no-XML ahora lanza una TypeError en lugar de una ValueError.

### Estándar

La función `round` ahora verifica el valor del `mode` y lanza una ValueError para modos no válidos. Anteriormente, los modos no válidos se interpretaban como `PHP_ROUND_HALF_UP`.

La función `str_getcsv` ahora lanza una ValueError si los argumentos `separator` y `enclosure` no tienen un byte de largo, o si el argumento `escape` no tiene un byte de largo o es una cadena vacía. Esto alinea el comportamiento para que sea idéntico al de `fputcsv` y `fgetcsv`.

La función `php_uname` ahora lanza una ValueError si el `mode` es no válido.

La opción `"allowed_classes"` para `unserialize` ahora lanza TypeError y ValueError si no es un `array` de nombres de clase.

### XMLReader

Pasar un codificado de caracteres no válido a XMLReader::open o XMLReader::XML ahora lanza una ValueError.

Pasar una cadena que contiene bytes nulos anteriormente emitía una alerta y ahora lanza una ValueError.

### XMLWriter

Pasar una cadena que contiene bytes nulos anteriormente emitía una alerta y ahora lanza una ValueError.

### XSL

XSLTProcessor::setParameter ahora lanza una ValueError cuando sus argumentos contienen bytes nulos. Esto nunca funcionó correctamente en primer lugar, por lo que ahora se lanza una excepción.

Llamar a XSLTProcessor::importStylesheet con un objeto no-XML ahora lanza una TypeError en lugar de una ValueError.

El fallo al llamar a una función de devolución de llamada PHP durante la evaluación ahora lanza una excepción en lugar de emitir una alerta.

## Fecha

`number` símbolos en [formatos relativos](#datetime.formats.relative) aceptan nuevamente múltiples signos, por ejemplo, `+-2`.

## DOM

Algunos métodos DOM anteriormente devolvían `false` o una DOMException `PHP_ERR` si no se podía agregar un nuevo nodo. Ahora siempre lanzan una DOMException `INVALID_STATE_ERR`. Esta situación es extremadamente improbable y la probabilidad de verse afectado es baja. En consecuencia, DOMImplementation::createDocument ahora tiene un tipo de retorno provisional de `DOMDocument` en lugar de `DOMDocument|false`.

Anteriormente, los objetos `DOMXPath` podían ser clonados, pero resultaban en un objeto inutilizable. Esto ya no es posible, y clonar un objeto `DOMXPath` ahora lanza una Error.

El método DOMImplementation::getFeature ha sido eliminado.

## GMP

La clase `GMP` ahora es final y ya no puede ser extendida.

## MBString

En caso de cadenas no válidas (aquellas con errores de codificación), `mb_substr` ahora interpreta los índices de caracteres de la misma manera que la mayoría de las otras funciones mbstring. Esto significa que los índices de caracteres devueltos por `mb_strpos` pueden pasarse a `mb_substr`.

Para las cadenas SJIS-Mac (MacJapanese), los índices de caracteres pasados a `mb_substr` ahora se refieren a los índices de los puntos de código Unicode que se producen cuando la cadena se convierte a Unicode. Esto es significativo porque aproximadamente 40 caracteres SJIS-Mac se convierten en una secuencia de múltiples puntos de código Unicode.

## MySQLi

La constante no utilizada y no documentada `MYSQLI_SET_CHARSET_DIR` ha sido eliminada.

La constante `MYSQLI_STMT_ATTR_UPDATE_MAX_LENGTH` ha sido eliminada. Esta funcionalidad no está disponible con mysqlnd.

Las constantes `MYSQLI_STMT_ATTR_CURSOR_TYPE` y `MYSQLI_STMT_ATTR_PREFETCH_ROWS` han sido eliminadas. Estas funcionalidades nunca fueron implementadas, ni con mysqlnd ni con libmysql.

La constante no utilizada `MYSQLI_TYPE_INTERVAL`, que actualmente es un stub y un alias para `MYSQLI_TYPE_ENUM`, ha sido eliminada.

## MySQLnd

El código de error reportado para los tiempos de espera del servidor MySQL ha cambiado de `2006` a `4031` para las versiones del servidor MySQL 8.0.24 y superiores.

## Opcache

El valor máximo de la configuración [opcache.interned_strings_buffer](#ini.opcache.interned-strings-buffer) en arquitecturas de 64 bits ahora es `32767`. Anteriormente, era `4095`.

### JIT

El valor por defecto de la configuración JIT ha cambiado de [`opcache.jit=tracing`](#ini.opcache.jit) y [`opcache.jit_buffer_size=0`](#ini.opcache.jit-buffer-size) a [`opcache.jit=disable`](#ini.opcache.jit) y [`opcache.jit_buffer_size=64M`](#ini.opcache.jit-buffer-size), respectivamente.

Esto no afecta el comportamiento observable por defecto, porque el JIT sigue estando desactivado por defecto. Sin embargo, ahora se desactiva a través de la configuración [opcache.jit](#ini.opcache.jit), en lugar de [opcache.jit_buffer_size](#ini.opcache.jit-buffer-size). Esto puede afectar a los usuarios que anteriormente habían activado el JIT a través de [opcache.jit_buffer_size](#ini.opcache.jit-buffer-size) exclusivamente, sin especificar también un modo JIT usando [opcache.jit](#ini.opcache.jit). Para habilitar la compilación JIT, defina el valor de configuración [opcache.jit](#ini.opcache.jit) en consecuencia.

Si la compilación JIT está habilitada, PHP ahora finalizará con un error fatal al iniciar si la inicialización del compilador JIT falla por cualquier motivo.

## PCNTL

Las funciones `pcntl_sigprocmask`, `pcntl_sigwaitinfo`, y `pcntl_sigtimedwait` ahora devuelven sistemáticamente `false` en caso de fallo. En algunos casos anteriores, podían devolver el valor `-1`.

## PCRE

La versión de pcre2lib incluida se ha actualizado a la versión 10.44. Esto significa que `{,3}` ahora se reconoce como un cuantificador en lugar de un texto. Además, la significación de algunas clases de caracteres en modo UCP ha cambiado. Consulte el [registro de cambios de PCRE2](https://github.com/PCRE2Project/pcre2/blob/master/NEWS) para obtener un registro de cambios completo.

## PDO_DBLIB

Los atributos `Pdo\Dblib::ATTR_STRINGIFY_UNIQUEIDENTIFIER` y `Pdo\Dblib::ATTR_DATETIME_CONVERT` ahora actúan como atributos booleanos en lugar de atributos enteros. Por lo tanto, definir el atributo a través de PDO::setAttribute y recuperarlo a través de PDO::getAttribute espera y devuelve un `bool`.

## PDO_FIREBIRD

El atributo `PDO::ATTR_AUTOCOMMIT` ahora actúa como un atributo booleano en lugar de un atributo entero. Por lo tanto, definir el atributo a través de PDO::setAttribute y recuperarlo a través de PDO::getAttribute espera y devuelve un `bool`.

La extensión ahora expone ciertas API C++ de Firebird, por lo que la construcción de esta extensión ahora requiere un compilador C++. Además, la extensión ahora debe compilarse contra fbclient 3.0 o superior.

## PDO_MYSQL

Los atributos `PDO::ATTR_AUTOCOMMIT` `PDO::ATTR_EMULATE_PREPARES`, y `PDO::MYSQL_ATTR_DIRECT_QUERY` ahora actúan como atributos booleanos en lugar de atributos enteros. Por lo tanto, definir el atributo a través de PDO::setAttribute y recuperarlo a través de PDO::getAttribute espera y devuelve un `bool`.

## PDO_PGSQL

La información de conexión DSN, cuando se define, ahora tiene prioridad sobre los argumentos del constructor PDO, estando más cerca de lo que indica la documentación.

## SimpleXML

`SimpleXMLElement` no es solo una representación de un elemento XML, sino que también es un `RecursiveIterator`. Antes de PHP 8.4.0, algunos de sus métodos (por ejemplo, SimpleXMLElement::asXML o SimpleXMLElement::getName) y la conversión de tales instancias a `string` reinicializaban implícitamente el iterador.

Esto podía provocar bucles infinitos no intencionados porque el iterador se reinicializaba. Por ejemplo:

```php
<?php

$xmlString = "<root><a><b>1</b><b>2</b><b>3</b></a></root>";
$xml = simplexml_load_string($xmlString);

$nodes = $xml->a->b;
foreach ($nodes as $nodeData) {
    echo "nodeData: " . $nodeData . "\n";

    $xml = $nodes->asXml();
}

    
```

causaba un bucle infinito.

    nodeData: 1
    nodeData: 2
    nodeData: 2
    nodeData: 2
    nodeData: 2
    nodeData: 2
    nodeData: 2
    // ...

        

Sin embargo, este comportamiento ha sido corregido, y un `SimpleXMLElement` ya no reinicializará implícitamente el iterador, a menos que se restablezca explícitamente a cero. Esto significa que el ejemplo anterior ahora daría:

    nodeData: 1
    nodeData: 2
    nodeData: 3

## SOAP

SoapClient::\$typemap ahora es un `array` en lugar de una `resource`. Las verificaciones con `is_resource` (es decir, `is_resource($client->typemap)`) deben ser reemplazadas por verificaciones de `null` (es decir, `$client->typemap !== null`).

La extensión SOAP ha adquirido una dependencia opcional de la extensión [session](#book.session). Si PHP se compila sin la extensión session y con la opción de configuración `--enable-rtld-now` activada, se producirán errores de inicio si también se utiliza la extensión [SOAP](#book.soap). Para resolver este problema, no utilice rtld-now o cargue la extensión session.

## Estándar

Al usar `strcspn` con `characters` siendo una cadena vacía, ahora se devuelve la longitud de la cadena en lugar de detenerse en el primer byte nulo.

`http_build_query` ahora maneja correctamente las enumeraciones

`stream_bucket_make_writeable` y `stream_bucket_new` ahora devuelven una instancia de `StreamBucket` en lugar de una instancia de `stdClass`.

## Tidy

Los errores en el constructor ahora lanzan excepciones en lugar de emitir advertencias y tener un objeto roto.

## XML

Las funciones `xml_set_*_handler` ahora declaran y verifican una firma efectiva de `callablestringnull` para los parámetros `handler`. Además, los valores de tipo `string` que corresponden a nombres de método, de objeto definido con `xml_set_object` ahora se verifican para ver si el método existe en la clase del objeto previamente pasado. Esto significa que `xml_set_object` ahora siempre debe ser llamada antes de definir nombres de método como `callable`. Pasar una cadena vacía para deshabilitar el manejador sigue estando permitido, pero está desaprobado.

Además, con `xml_set_object` y el paso de cadenas no-`callable` está desaprobado. Se recomienda reemplazar tales instancias con un `callable` que se refiera directamente al método.
