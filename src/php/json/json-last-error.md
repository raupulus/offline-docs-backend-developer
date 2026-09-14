---
title: json_last_error
description: Devuelve el último error JSON
source_url: https://www.php.net/manual/es/function.json-last-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/json/functions/json-last-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: json
translation_status: ready
translation_reviewed: false
translation_revision: 058ea1e84
order: 42860
---

json_last_error

Devuelve el último error JSON

## Descripción

```php
json_last_error(): int
```php

Devuelve el último error, si ha ocurrido, durante la última operación de validación/codificación/decodificación JSON, que no haya especificado `JSON_THROW_ON_ERROR`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una de las siguientes constantes:

| Constante | Significado | Disponibilidad |
|----|----|----|
| `JSON_ERROR_NONE` | No ha ocurrido ningún error |  |
| `JSON_ERROR_DEPTH` | Se ha alcanzado la profundidad máxima de la pila |  |
| `JSON_ERROR_STATE_MISMATCH` | JSON inválido o mal formado |  |
| `JSON_ERROR_CTRL_CHAR` | Error durante el control de caracteres; probablemente un codificación incorrecta |  |
| `JSON_ERROR_SYNTAX` | Error de sintaxis |  |
| `JSON_ERROR_UTF8` | Caracteres UTF-8 malformados, posiblemente mal codificados |  |
| `JSON_ERROR_RECURSION` | Una o más referencias recursivas están presentes en el valor a codificar |  |
| `JSON_ERROR_INF_OR_NAN` | Una o más valores [`NAN`](#language.types.float.nan) o [`INF`](#function.is-infinite) están presentes en el valor a codificar. |  |
| `JSON_ERROR_UNSUPPORTED_TYPE` | Se ha proporcionado un valor de un tipo que no puede ser codificado |  |
| `JSON_ERROR_INVALID_PROPERTY_NAME` | Se ha proporcionado un nombre de propiedad que no puede ser codificado |  |
| `JSON_ERROR_UTF16` | Caracteres UTF-16 mal formados, probablemente mal codificados |  |
| `JSON_ERROR_NON_BACKED_ENUM` | El valor contiene un enum sin valores (non-backed enum) que no se puede serializar. Disponible a partir de PHP 8.1.0. |  |

Códigos de error JSON

## Ejemplos

Ejemplo con `json_last_error`

```
<?php
// Una cadena JSON válida
$json[] = '{"Organisation": "Équipe de Documentation PHP"}';

// Una cadena json inválida que va a generar un error de sintaxis,
// aquí, uso de ' en lugar de "
$json[] = "{'Organisation': 'Équipe de Documentation PHP'}";

foreach ($json as $string) {
    echo 'Decodificación: ' . $string;
    json_decode($string);

    switch (json_last_error()) {
        case JSON_ERROR_NONE:
            echo ' - Sin errores';
        break;
        case JSON_ERROR_DEPTH:
            echo ' - Profundidad máxima alcanzada';
        break;
        case JSON_ERROR_STATE_MISMATCH:
            echo ' - Inadecuación de modos o underflow';
        break;
        case JSON_ERROR_CTRL_CHAR:
            echo ' - Error durante el control de caracteres';
        break;
        case JSON_ERROR_SYNTAX:
            echo ' - Error de sintaxis; JSON malformado';
        break;
        case JSON_ERROR_UTF8:
            echo ' - Caracteres UTF-8 malformados, probablemente un error de codificación';
        break;
        default:
            echo ' - Error desconocido';
        break;
    }

    echo PHP_EOL;
}
?>

    
```php

El ejemplo anterior mostrará:

    Decodificación: {"Organisation": "Équipe de Documentation PHP"} - Sin errores
    Decodificación: {'Organisation': 'Équipe de Documentation PHP'} - Error de sintaxis; JSON malformado

`json_last_error` con `json_encode`

```
<?php
// Una secuencia UTF8 inválida
$text = "\xB1\x31";

$json  = json_encode($text);
$error = json_last_error();

var_dump($json, $error === JSON_ERROR_UTF8);
?>

    
```php

El ejemplo anterior mostrará:

    string(4) "null"
    bool(true)

`json_last_error` y `JSON_THROW_ON_ERROR`

```
<?php
// Una secuencia UTF8 inválida que causa JSON_ERROR_UTF8
json_encode("\xB1\x31");

// Esto no produce un error JSON
json_encode('okay', JSON_THROW_ON_ERROR);

// El estado de error global no ha sido modificado por el json_encode() anterior
var_dump(json_last_error() === JSON_ERROR_UTF8);
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)

## Véase también

`json_last_error_msg`, `json_decode`, `json_encode`
