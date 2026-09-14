---
title: strnatcasecmp
description: Comparación de strings con el algoritmo de "orden natural" (insensible
  a mayúsculas/minúsculas)
source_url: https://www.php.net/manual/es/function.strnatcasecmp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strnatcasecmp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 9b68bf2b6
order: 89350
---

strnatcasecmp

Comparación de strings con el algoritmo de "orden natural" (insensible a mayúsculas/minúsculas)

## Descripción

```php
strnatcasecmp(string $string1, string $string2): int
```php

`strnatcasecmp` implementa el algoritmo de comparación que ordena los strings como lo haría un ser humano. Esta función es similar a la función `strnatcmp`, pero la comparación no es sensible a mayúsculas/minúsculas. Para más detalles, consulte [`Natural Order String Comparison`](https://github.com/sourcefrog/natsort) de Martin Pool (en inglés).

## Parámetros

`string1`  
El primer string.

`string2`  
El segundo string.

## Valores devueltos

Devuelve un valor inferior a 0 si `string1` es inferior a `string2`; un valor superior a 0 si `string1` es superior a `string2`, y `0` si son iguales. No se puede deducir ningún significado particular de este valor, excepto su signo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | Esta función ya no garantiza retornar `strlen($string1) - strlen($string2)` cuando las longitudes de las strings no son iguales, y puede retornar `-1` o `1` en su lugar. |

## Ejemplos

Ejemplo con `strnatcasecmp`

```
<?php

var_dump(strnatcasecmp('Apple', 'Banana'));
var_dump(strnatcasecmp('Banana', 'Apple'));
var_dump(strnatcasecmp('apple', 'Apple'));
?>

    
```php

El ejemplo anterior mostrará:

    int(-1)
    int(1)
    int(0)

## Véase también

`preg_match`, `strcmp`, `strcasecmp`, `substr`, `stristr`, `strncasecmp`, `strncmp`, `strstr`, `setlocale`
