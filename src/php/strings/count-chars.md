---
title: count_chars
description: Devuelve estadísticas sobre los caracteres utilizados en un string
source_url: https://www.php.net/manual/es/function.count-chars.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/count-chars.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: eb3c7d0d6
order: 88680
---

count_chars

Devuelve estadísticas sobre los caracteres utilizados en un string

## Descripción

```php
count_chars(string $string, [int $mode]): array
```php

`count_chars` cuenta el número de ocurrencias de todos los bytes presentes en el string `string` y devuelve diferentes estadísticas.

## Parámetros

`string`  
El string analizado.

`mode`  
Ver los valores devueltos.

## Valores devueltos

Según el valor de `mode`, `count_chars` devuelve la siguiente información:

- 0: un array con el byte como índice y la frecuencia correspondiente para cada byte.

- 1: idéntico a 0, pero solo se listan las frecuencias mayores que cero.

- 2: idéntico a 0, pero solo se listan las frecuencias nulas.

- 3: un string que contiene todos los bytes utilizados es devuelto.

- 4: un string que contiene todos los bytes no utilizados es devuelto.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Anterior a esta versión, la función devolvía `false` en caso de error. |

## Ejemplos

Ejemplo con `count_chars`

```
<?php
$data = "Deux D et un F.";

foreach (count_chars($data, 1) as $i => $val) {
   echo "Hay $val ocurrencia(s) de \"" , chr($i) , "\" en la frase.\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    Hay 4 ocurrencia(s) de " " en la frase.
    Hay 1 ocurrencia(s) de "." en la frase.
    Hay 2 ocurrencia(s) de "D" en la frase.
    Hay 1 ocurrencia(s) de "F" en la frase.
    Hay 2 ocurrencia(s) de "e" en la frase.
    Hay 1 ocurrencia(s) de "n" en la frase.
    Hay 1 ocurrencia(s) de "t" en la frase.
    Hay 2 ocurrencia(s) de "u" en la frase.
    Hay 1 ocurrencia(s) de "x" en la frase.

## Véase también

`strpos`, `substr_count`
