---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/json.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/json/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: json
translation_status: ready
translation_reviewed: false
translation_revision: 40e4bf862
order: 42820
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

Las constantes siguientes indican el tipo de error devuelto por `json_last_error` o almacenado como `code` de una `JsonException`.

`JSON_ERROR_NONE` (`int`)  
No se ha producido ningún error.

`JSON_ERROR_DEPTH` (`int`)  
Se ha alcanzado la profundidad máxima de la pila.

`JSON_ERROR_STATE_MISMATCH` (`int`)  
Ocurre con un underflow o con una inadaptación de los modos.

`JSON_ERROR_CTRL_CHAR` (`int`)  
Error al controlar los caracteres, probablemente codificados incorrectamente.

`JSON_ERROR_SYNTAX` (`int`)  
Error de sintaxis.

`JSON_ERROR_UTF8` (`int`)  
Caracteres UTF-8 mal formados, probablemente codificados incorrectamente.

`JSON_ERROR_RECURSION` (`int`)  
El objeto o el array pasado a la función `json_encode` incluye referencias recursivas y no pueden ser codificadas. Si se ha proporcionado la opción `JSON_PARTIAL_OUTPUT_ON_ERROR`, `null` será codificado en lugar de la referencia recursiva.

`JSON_ERROR_INF_OR_NAN` (`int`)  
El valor pasado a la función `json_encode` incluye [`NAN`](#language.types.float.nan), o [`INF`](#function.is-infinite). Si se ha proporcionado la opción `JSON_PARTIAL_OUTPUT_ON_ERROR`, `0` será codificado en lugar de estos números especiales.

`JSON_ERROR_UNSUPPORTED_TYPE` (`int`)  
Se ha proporcionado un valor de un tipo no soportado a la función `json_encode`, como por ejemplo una `resource`. Si se ha proporcionado la opción `JSON_PARTIAL_OUTPUT_ON_ERROR`, `null` será codificado en lugar del valor no soportado.

`JSON_ERROR_INVALID_PROPERTY_NAME` (`int`)  
Una clave que comienza con el carácter \u0000 estaba presente en la cadena de caracteres pasada a `json_decode` durante la decodificación de un objeto JSON en un objeto PHP.

`JSON_ERROR_UTF16` (`int`)  
Sustituto UTF-16 simple no apareado en el escape unicode contenido en la cadena de caracteres JSON pasada a `json_decode`.

`JSON_ERROR_NON_BACKED_ENUM` (`int`)  
El valor pasado a `json_encode` incluye una enumeración no soportada que no puede ser serializada. Disponible a partir de PHP 8.1.0.

Las constantes siguientes pueden ser combinadas para formar las opciones de `json_decode`.

`JSON_BIGINT_AS_STRING` (`int`)  
Decodifica los enteros grandes como una cadena de caracteres.

`JSON_OBJECT_AS_ARRAY` (`int`)  
Decodifica un objeto JSON en array PHP. Esta opción puede ser añadida automáticamente llamando a `json_decode` con el segundo argumento igual a `true`.

Las constantes siguientes pueden ser combinadas para formar las opciones de `json_encode`.

`JSON_HEX_TAG` (`int`)  
Todos los caracteres \< y \> son convertidos en secuencias \u003C y \u003E.

`JSON_HEX_AMP` (`int`)  
Todos los caracteres & son convertidos en \u0026.

`JSON_HEX_APOS` (`int`)  
Todos los apóstrofes ' son convertidos en \u0027.

`JSON_HEX_QUOT` (`int`)  
Todas las comillas dobles " son convertidas en \u0022.

`JSON_FORCE_OBJECT` (`int`)  
Produce un objeto en lugar de un array, cuando se utiliza un array no asociativo. Esto es especialmente útil cuando el destinatario del resultado espera un objeto, y el array está vacío.

`JSON_NUMERIC_CHECK` (`int`)  
Codifica las cadenas numéricas como números.

`JSON_PRETTY_PRINT` (`int`)  
Utiliza espacios en los datos devueltos para formatearlos.

`JSON_UNESCAPED_SLASHES` (`int`)  
No escapar los caracteres `/`.

`JSON_UNESCAPED_UNICODE` (`int`)  
Codifica los caracteres multioctetos Unicode literalmente (el comportamiento por defecto es escaparles con \uXXXX).

`JSON_PARTIAL_OUTPUT_ON_ERROR` (`int`)  
Sustituye ciertos valores no codificables en lugar de fallar.

`JSON_PRESERVE_ZERO_FRACTION` (`int`)  
Asegura que los valores de tipo `float` siempre sean codificados como valor flotante.

`JSON_UNESCAPED_LINE_TERMINATORS` (`int`)  
Los terminadores de línea son conservados sin escapar cuando `JSON_UNESCAPED_UNICODE` es proporcionado. Utiliza el mismo comportamiento como si fuera antes de PHP 7.1 sin esta constante. Disponible a partir de PHP 7.1.0.

Las constantes siguientes pueden ser combinadas para formar las opciones de `json_decode` y `json_encode`.

`JSON_INVALID_UTF8_IGNORE` (`int`)  
Ignora los caracteres UTF-8 inválidos. Disponible a partir de PHP 7.2.0.

`JSON_INVALID_UTF8_SUBSTITUTE` (`int`)  
Convierte los caracteres UTF-8 inválidos en \0xfffd (Carácter Unicode 'REPLACEMENT CHARACTER'). Disponible a partir de PHP 7.2.0.

`JSON_THROW_ON_ERROR` (`int`)  
Emite una `JsonException` si ocurre un error en lugar de establecer el estado de error global que es recuperado mediante `json_last_error` y `json_last_error_msg`. `JSON_PARTIAL_OUTPUT_ON_ERROR` tiene prioridad sobre `JSON_THROW_ON_ERROR`. Disponible a partir de PHP 7.3.0.
