---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/simdjson.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simdjson/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simdjson
translation_status: ready
translation_reviewed: false
translation_revision: 5e062629d
order: 74280
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`SIMDJSON_ERR_CAPACITY` (`int`)  
Este analizador no puede manejar un documento tan voluminoso. Se lanza al analizar una cadena JSON de más de 4 GiB.

`SIMDJSON_ERR_TAPE_ERROR` (`int`)  
El documento JSON tiene una estructura incorrecta: comas faltantes o superfluas, llaves, claves faltantes, etc.

`SIMDJSON_ERR_DEPTH_ERROR` (`int`)  
El documento JSON era demasiado profundo (demasiados objetos y arrays anidados)

`SIMDJSON_ERR_STRING_ERROR` (`int`)  
Problema al analizar una cadena

`SIMDJSON_ERR_T_ATOM_ERROR` (`int`)  
Problema al analizar un átomo que comienza con la letra 't'

`SIMDJSON_ERR_F_ATOM_ERROR` (`int`)  
Problema al analizar un átomo que comienza con la letra 'f'

`SIMDJSON_ERR_N_ATOM_ERROR` (`int`)  
Problema al analizar un átomo que comienza con la letra 'n'

`SIMDJSON_ERR_NUMBER_ERROR` (`int`)  
Problema al analizar un número

`SIMDJSON_ERR_UTF8_ERROR` (`int`)  
La entrada no es un UTF-8 válido

`SIMDJSON_ERR_UNINITIALIZED` (`int`)  
El analizador utilizado por simdjson no está inicializado. No debería ocurrir.

`SIMDJSON_ERR_EMPTY` (`int`)  
Vacío: no se encontró JSON

`SIMDJSON_ERR_UNESCAPED_CHARS` (`int`)  
Con las cadenas, algunos caracteres deben ser escapados, se encontraron caracteres no escapados

`SIMDJSON_ERR_UNCLOSED_STRING` (`int`)  
Una cadena está abierta, pero nunca cerrada.

`SIMDJSON_ERR_UNSUPPORTED_ARCHITECTURE` (`int`)  
simdjson no tiene una implementación compatible con esta arquitectura CPU (¿tal vez un CPU no-SIMD?).

`SIMDJSON_ERR_INCORRECT_TYPE` (`int`)  
No debería ocurrir.

`SIMDJSON_ERR_NUMBER_OUT_OF_RANGE` (`int`)  
El número JSON es demasiado grande o demasiado pequeño para caber en el tipo solicitado. Es importante señalar que la biblioteca C simdjson es un fork y que este error es ignorado para coincidir con la gestión de PHP de los números JSON que son demasiado grandes o demasiado pequeños.

`SIMDJSON_ERR_INDEX_OUT_OF_BOUNDS` (`int`)  
No debería ocurrir.

`SIMDJSON_ERR_NO_SUCH_FIELD` (`int`)  
No debería ocurrir.

`SIMDJSON_ERR_IO_ERROR` (`int`)  
No debería ocurrir.

`SIMDJSON_ERR_INVALID_JSON_POINTER` (`int`)  
Sintaxis de puntero JSON inválida en `simdjson_key_value` y otras funciones que aceptan un puntero JSON `$key`.

`SIMDJSON_ERR_INVALID_URI_FRAGMENT` (`int`)  
Sintaxis de fragmento URI inválida.

`SIMDJSON_ERR_UNEXPECTED_ERROR` (`int`)  
Error inesperado, considere reportar este problema ya que puede haber encontrado un bug en el PECL simdjson

`SIMDJSON_ERR_PARSER_IN_USE` (`int`)  
No debería ocurrir.

`SIMDJSON_ERR_OUT_OF_ORDER_ITERATION` (`int`)  
No debería ocurrir.

`SIMDJSON_ERR_INSUFFICIENT_PADDING` (`int`)  
No debería ocurrir.

`SIMDJSON_ERR_INCOMPLETE_ARRAY_OR_OBJECT` (`int`)  
El documento JSON terminó prematuramente en medio de un objeto o un array.

`SIMDJSON_ERR_SCALAR_DOCUMENT_AS_VALUE` (`int`)  
No debería ocurrir.

`SIMDJSON_ERR_OUT_OF_BOUNDS` (`int`)  
Intento de acceder a una ubicación fuera del documento.

`SIMDJSON_ERR_TRAILING_CONTENT` (`int`)  

`SIMDJSON_ERR_KEY_COUNT_NOT_COUNTABLE` (`int`)  

`SIMDJSON_ERR_INVALID_PROPERTY` (`int`)  
Nombre de propiedad inválido para un `stdClass` al decodificar un valor con `simdjson_decode` o `simdjson_key_value`
