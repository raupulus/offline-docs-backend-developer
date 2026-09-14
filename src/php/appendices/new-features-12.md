---
title: Nuevas características
source_url: https://www.php.net/manual/es/migration85.new-features.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration85/new-features.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 4de6272a1
order: 1230
---

## Nuevas características

## Núcleo de PHP

### Operador Pipe

Añadido el [Operador pipe (`|>`)](#language.operators.functional).

```php
<?php
$result = "Hola Mundo" |> strlen(...);
print $result . PHP_EOL;  // imprime "10"

    
```

### Cierres en expresiones constantes

Añadido soporte para [Closures](#class.closure) y [callable de primera clase](#functions.first_class_callable_syntax) en expresiones constantes. Esto incluye: Parámetros de atributos., Valores predeterminados de propiedades y parámetros., Constantes y constantes de clase.

### Atributo \#\[\NoDiscard\]

Añadido el atributo `NoDiscard` para indicar que el valor de retorno de una función es importante y debe ser consumido.

Además, se añadió la conversión `(void)` para indicar que no usar un valor es intencional. La conversión `(void)` no afecta la ejecución del programa por sí sola, pero puede usarse para suprimir las advertencias emitidas por `#[\NoDiscard]` y posiblemente también los diagnósticos emitidos por IDE externos o herramientas de análisis estático.

```php
<?php

#[\NoDiscard]
function concat(string $a, string $b): string {
     return $a . $b;
}

// Advertencia: El valor de retorno de la función concat() debe usarse o
// ignorarse intencionalmente convirtiéndolo a (void) en xxx.php
concat("a", "b");

// No hay advertencia, porque el valor de retorno es consumido por la asignación.
$results = concat("a", "b");

// No hay advertencia, porque se utiliza la conversión (void).
(void)concat("a", "b");

    
```

### Atributos en constantes

Añadido soporte para atributos en constantes no de clase en tiempo de compilación (p. ej. `const MY_CONST = 1;` en lugar de `define('MY_CONST', 1);`).

El atributo `Deprecated` ahora se puede usar en constantes.

### Atributo `#[\DelayedTargetValidation]`

El nuevo atributo `DelayedTargetValidation` permite suprimir los errores de compilación de los atributos principales (o de extensión) que se utilizan en destinos no válidos. Estos errores se notifican en tiempo de ejecución cuando se llama a ReflectionAttribute::newInstance.

### `#[\Override]` para propiedades

El atributo `Override` ahora se puede aplicar a las propiedades.

### Visibilidad asimétrica estática

Añadida compatibilidad con [ visibilidad asimétrica](#language.oop5.visibility-members-aviz) para propiedades estáticas.

### Seguimiento de pila para errores fatales

Los errores fatales (como exceder el tiempo máximo de ejecución) ahora incluyen un seguimiento de pila.

### Promoción del constructor para propiedades finales

La [promoción de propiedades en el constructor ahora](#language.oop5.decon.constructor.promotion) se puede utilizar para propiedades finales.

### Conversión en expresiones constantes

Añadida compatibilidad para conversiones en expresiones constantes.

```php
<?php
const T1 = (int) 0.3; // Anteriormente: "Fatal error: Constant expression contains invalid operations"
print T1 . PHP_EOL;   // Imprime "0"

    
```

### Función de clonación

La [construcción del lenguaje de clonación](#language.oop5.cloning) ahora es una función y admite la reasignación de propiedades (de solo lectura) durante la clonación a través del nuevo parámetro \$withProperties.

## cURL

Añadido soporte para [manejadores compartidos](#class.curlsharepersistenthandle) que se mantienen a través de múltiples solicitudes PHP, permitiendo de forma segura una reutilización más eficaz de las conexiones.

Añadido soporte para `CURLINFO_USED_PROXY` (libcurl \>= 8.7.0), `CURLINFO_HTTPAUTH_USED`, y `CURLINFO_PROXYAUTH_USED` (libcurl \>= 8.12.0) a la función `curl_getinfo`. Cuando `curl_getinfo` devuelve un array, la misma información está disponible como claves `"used_proxy"`, `"httpauth_used"` y `"proxyauth_used"`. `CURLINFO_USED_PROXY` se establece en cero si no se utilizó ningún proxy en la transferencia anterior o en un valor distinto de cero si se utilizó un proxy. `CURLINFO_HTTPAUTH_USED` y `CURLINFO_PROXYAUTH_USED` obtienen máscaras de bits que indican los métodos de autenticación HTTP y proxy que se utilizaron en la solicitud anterior. Véanse las constantes `CURLAUTH_*` para valores posibles.

Añadida la opción Curl `CURLOPT_INFILESIZE_LARGE`, que sustituye de forma segura a `CURLOPT_INFILESIZE`. En algunos sistemas, `CURLOPT_INFILESIZE` solo acepta un entero con signo de 32 bits como tamaño de archivo (2,0 GiB), incluso en sistemas de 64 bits. `CURLOPT_INFILESIZE_LARGE` acepta el valor entero más grande que el sistema puede manejar.

Añadidos los valores `CURLFOLLOW_OBEYCODE`, `CURLFOLLOW_FIRSTONLY` y `CURLFOLLOW_ALL` para la opción `CURLOPT_FOLLOWLOCATION` `curl_setopt`. `CURLFOLLOW_OBEYCODE` para seguir más estrictamente en lo que respecta a las redirecciones si están permitidas. `CURLFOLLOW_FIRSTONLY` para seguir solo la primera redirección, por lo que si hay alguna redirección posterior, no irá más allá. `CURLFOLLOW_ALL` es equivalente a establecer `CURLOPT_FOLLOWLOCATION` a true.

Añadida compatibilidad con `CURLINFO_CONN_ID` (libcurl \>= 8.2.0) a la función `curl_getinfo`. Esta constante permite recuperar el ID único de la conexión utilizada en una transferencia cURL. Resulta especialmente útil cuando se requiere lógica de reutilización o agrupación de conexiones en aplicaciones PHP. Cuando `curl_getinfo` devuelve un array, este valor está disponible como la clave `"conn_id"`.

Añadida compatibilidad con `CURLINFO_QUEUE_TIME_T` (libcurl \>= 8.6.0) a la función `curl_getinfo`. Esta constante permite obtener el tiempo (en microsegundos) que la solicitud permaneció en la cola de conexiones de libcurl antes de ser enviada. Este valor también se puede obtener pasando `CURLINFO_QUEUE_TIME_T` al parámetro `option` de la función `curl_getinfo`.

Añadido soporte para `CURLOPT_SSL_SIGNATURE_ALGORITHMS` para especificar los algoritmos de firma que se utilizarán para TLS.

## DOM

Añadida Dom\Element::\$outerHTML.

Añadida la propiedad \$children a las implementaciones de Dom\ParentNode.

## EXIF

Añadida compatibilidad con las etiquetas Exif `OffsetTime*`.

Añadida compatibilidad con HEIF/HEIC.

## Filtro

Añadida la nueva flag `FILTER_THROW_ON_FAILURE`, que se puede pasar a las funciones de filtro y fuerza el lanzamiento de una excepción cuando falla la validación. Esta nueva bandera no se puede combinar con `FILTER_NULL_ON_FAILURE`; si se intenta, se lanzará ValueError.

## Intl

Añadidas las constantes de clase `NumberFormatter::CURRENCY_ISO`, `NumberFormatter::CURRENCY_PLURAL`, `NumberFormatter::CASH_CURRENCY` y `NumberFormatter::CURRENCY_STANDARD` para varios formatos de números relacionados con monedas.

Añadidos Locale::addLikelySubtags y Locale::minimizeSubtags para manejar las etiquetas probables en una configuración regional determinada.

Añadida la clase `IntlListFormatter` para formatear, ordenar y puntuar una lista de elementos con una configuración regional determinada, los operandos `IntlListFormatter::TYPE_AND`, `IntlListFormatter::TYPE_OR`, `IntlListFormatter::TYPE_UNITS`, y los anchos `IntlListFormatter::WIDTH_WIDE`, `IntlListFormatter::WIDTH_SHORT` y `IntlListFormatter::WIDTH_NARROW`. Es compatible a partir de ICU 67.

## PDO_Sqlite

Añadida la constante de clase `Pdo\Sqlite::ATTR_BUSY_STATEMENT`.

Añadidas las constantes de clase `Pdo\Sqlite::ATTR_EXPLAIN_STATEMENT`, `Pdo\Sqlite::EXPLAIN_MODE_PREPARED`, `Pdo\Sqlite::EXPLAIN_MODE_EXPLAIN`, `Pdo\Sqlite::EXPLAIN_MODE_EXPLAIN_QUERY_PLAN`.

Añadido el atributo de conexión `Pdo\Sqlite::ATTR_TRANSACTION_MODE` con los valores posibles `Pdo\Sqlite::TRANSACTION_MODE_DEFERRED`, `Pdo\Sqlite::TRANSACTION_MODE_IMMEDIATE` y `Pdo\Sqlite::TRANSACTION_MODE_EXCLUSIVE`, lo que permite configurar el modo de transacción que se utilizará al llamar a beginTransaction().

## Sesiones

`session_set_cookie_params`, `session_get_cookie_params`, y `session_start` ahora admiten cookies particionadas mediante la clave `"partitioned"`.

## SOAP

Los casos de enumeración ahora se vuelcan en SoapClient::\_\_getTypes.

Añadida compatibilidad con el atributo xml:lang de Soap 1.2 Reason Text.

Por lo tanto, las firmas de SoapFault::\_\_construct y SoapServer::fault ahora incluyen un parámetro opcional `lang`. Esta compatibilidad resuelve el problema de compatibilidad con los clientes SOAP de .NET.

## Estándar

`mail` ahora devuelve el error real de sendmail y detecta si el proceso de sendmail finalizó inesperadamente. En tales casos, se emite una advertencia y la función devuelve false. Anteriormente, estos errores se ignoraban silenciosamente. Este cambio afecta únicamente al transporte de sendmail.

`getimagesize` ahora admite imágenes HEIF/HEIC.

`getimagesize` ahora admite imágenes SVG cuando también se carga ext-libxml. Del mismo modo, `image_type_to_extension` y `image_type_to_mime_type` ahora también admiten IMAGETYPE_SVG.

El array que devuelve `getimagesize` ahora incluye dos entradas adicionales: `"width_unit"` y `"height_unit"` para indicar las unidades en las que se expresan las dimensiones. Estas unidades son px por omisión. No tienen por qué ser iguales (por poner solo un ejemplo: una puede ser cm y la otra px).

`setcookie` y `setrawcookie` ahora admiten la clave `"partitioned"`.

## URI

Añadida una extensión URI siempre habilitada que se puede utilizar para manejar URI y URL de acuerdo con RFC 3986 y WHATWG URL.

## XSL

El argumento `namespace` de XSLTProcessor::getParameter, XSLTProcessor::setParameter y XSLTProcessor::removeParameter ahora funciona correctamente en lugar de considerarse vacío. Esto solo funciona si el argumento `name` no utiliza la notación Clark ni es un QName, ya que en esos casos el espacio de nombres se obtiene del espacio de nombres href o prefijo, respectivamente.

## Zlib

Ahora se admite `flock` en flujos zlib. Anteriormente, esta función siempre fallaba al realizar cualquier acción de bloqueo.
