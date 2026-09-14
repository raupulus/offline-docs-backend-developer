---
title: strcspn
description: Encuentra un segmento de string que no contiene ciertos caracteres
source_url: https://www.php.net/manual/es/function.strcspn.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strcspn.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: 89990d658
order: 89280
---

strcspn

Encuentra un segmento de string que no contiene ciertos caracteres

## Descripción

```php
strcspn(string $string, string $characters, [int $offset], [int $length]): int
```php

Devuelve la longitud del primer segmento de `string` que no contiene *ninguno* de los caracteres de `characters`.

Si `offset` y `length` son omitidos, entonces se examinará la totalidad de `string`. Si se incluyen, el efecto será idéntico a llamar a `strcspn(substr($string, $offset, $length), $characters)` (ver [???](#function.substr) para más información).

## Parámetros

`string`  
El string a examinar.

`characters`  
El string que contiene todos los caracteres desactivados.

`offset`  
La posición en `string` desde la cual se comienza a buscar.

Si `offset` es proporcionado y no es negativo, entonces `strcspn` comenzará a examinar `string` en la posición `offset`. Por ejemplo, en el string '`abcdef`', el carácter en la posición `0` es '`a`', el carácter en la posición `2` es '`c`', y así sucesivamente.

Si `offset` es proporcionado y es negativo, entonces `strspn` comenzará a examinar `string` en la posición `offset` desde el final de `string`.

`length`  
La longitud del segmento de `string` a examinar.

Si `length` es proporcionado y no es negativo, entonces `string` será examinado desde `length` caracteres después de la posición de inicio.

Si `length` es proporcionado y es negativo, entonces `string` será examinado desde la posición de inicio hasta `length` caracteres desde el final de `string`.

## Valores devueltos

Devuelve la longitud del segmento inicial de `string` que contiene solo caracteres que no están *no* en `characters`.

> [!NOTE]
> Cuando el parámetro `offset` está definido, la longitud devuelta se cuenta desde esta posición, y no desde el inicio de `string`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Antes de PHP 8.4.0, cuando `characters` era un string vacío, la búsqueda se detenía incorrectamente en el primer byte nulo en `string`. |
| 8.0.0 | `length` ahora es nullable. |

## Ejemplos

Ejemplo con `strcspn`

```
<?php
$a = strcspn('banana', 'a');
$b = strcspn('banana', 'abcd');
$c = strcspn('banana', 'z');
$d = strcspn('abcdhelloabcd', 'a', -9);
$e = strcspn('abcdhelloabcd', 'a', -9, -5);

var_dump($a);
var_dump($b);
var_dump($c);
var_dump($d);
var_dump($e);
?>

   
```php

El ejemplo anterior mostrará:

    int(1)
    int(0)
    int(6)
    int(5)
    int(4)

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`strspn`
