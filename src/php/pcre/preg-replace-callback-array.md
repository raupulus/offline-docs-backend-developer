---
title: preg_replace_callback_array
description: Realiza una búsqueda de coincidencia con una expresión regular y reemplaza
  mediante una función de devolución de llamada
source_url: https://www.php.net/manual/es/function.preg-replace-callback-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcre/functions/preg-replace-callback-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcre
translation_status: ready
translation_reviewed: false
translation_revision: 41c8533ff
order: 61640
---

preg_replace_callback_array

Realiza una búsqueda de coincidencia con una expresión regular y reemplaza mediante una función de devolución de llamada

## Descripción

```php
preg_replace_callback_array(array $pattern, string $subject, [int $limit], [int $count], [int $flags]): string
```php

El comportamiento de esta función es similar a `preg_replace_callback`, con la excepción de que las funciones de devolución de llamada se ejecutan para cada patrón.

## Parámetros

`pattern`  
Un array asociativo que establece una relación entre los patrones (claves) y las funciones de devolución de llamada `callable` (valores).

`subject`  
La cadena o un array que contiene las cadenas a buscar y reemplazar.

`limit`  
El número máximo de reemplazos para cada patrón en cada `subject`. Por omisión `-1` (sin límite).

`count`  
Si se proporciona, esta variable será rellenada con el número de reemplazos realizados.

`flags`  
`flags` puede ser una combinación de los indicadores `PREG_OFFSET_CAPTURE` y `PREG_UNMATCHED_AS_NULL`, que influyen en el formato del array de coincidencias. Ver la descripción de `preg_match` para más detalles.

## Valores devueltos

`preg_replace_callback_array` devuelve un array si el parámetro `subject` es un array, o de lo contrario una cadena. En caso de error, el valor devuelto es `null`.

Si se encuentran coincidencias, el nuevo sujeto será devuelto, de lo contrario `subject` será devuelto sin cambios.

## Errores/Excepciones

Si el patrón regex pasado no se compila a una regex válida, se emite una `E_WARNING`.

## Historial de cambios

| Versión | Descripción                           |
|---------|---------------------------------------|
| 7.4.0   | El parámetro `flags` ha sido añadido. |

## Ejemplos

Ejemplo de `preg_replace_callback_array`

```
<?php
$subject = 'Aaaaaa Bbb';

preg_replace_callback_array(
    [
        '~[a]+~i' => function ($match) {
            echo strlen($match[0]), ' coincidencias de "a" encontradas', PHP_EOL;
        },
        '~[b]+~i' => function ($match) {
            echo strlen($match[0]), ' coincidencias de "b" encontradas', PHP_EOL;
        }
    ],
    $subject
);
?>

    
```php

El ejemplo anterior mostrará:

    6 coincidencias de "a" encontradas
    3 coincidencias de "b" encontradas

## Véase también

[Patrones PCRE](#pcre.pattern), `preg_replace_callback`, `preg_quote`, `preg_replace`, `preg_last_error`, [Funciones anónimas](#functions.anonymous)
