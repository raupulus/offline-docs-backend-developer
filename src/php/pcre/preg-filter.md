---
title: preg_filter
description: Búsqueda y reemplazo con una expresión regular
source_url: https://www.php.net/manual/es/function.preg-filter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcre/functions/preg-filter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcre
translation_status: ready
translation_reviewed: true
translation_revision: 2ad251ea7
order: 61570
---

preg_filter

Búsqueda y reemplazo con una expresión regular

## Descripción

```php
preg_filter(string $pattern, string $replacement, string $subject, [int $limit], [int $count]): string
```php

`preg_filter` es idéntica a `preg_replace`, pero solo devuelve las ocurrencias encontradas (eventualmente transformadas). Para más detalles sobre el funcionamiento de esta función, véase `preg_replace`.

## Parámetros

Los parámetros están descritos en la documentación de `preg_replace`.

## Valores devueltos

Devuelve un `array` si el parámetro `subject` es de tipo `array` o una `string` en otro caso.

Si ninguna ocurrencia es encontrada o si ocurre un error, un `array` vacío será devuelto cuando el parámetro `subject` es un `array` o `null` en otro caso.

## Errores/Excepciones

Si el patrón regex pasado no se compila a una regex válida, se emite una `E_WARNING`.

## Ejemplos

Ejemplo de comparación de `preg_filter` con `preg_replace`

```
<?php
$subject = array('1', 'a', '2', 'b', '3', 'A', 'B', '4');
$pattern = array('/\d/', '/[a-z]/', '/[1a]/');
$replace = array('A:$0', 'B:$0', 'C:$0');

echo "preg_filter devuelve\n";
print_r(preg_filter($pattern, $replace, $subject));

echo "preg_replace devuelve\n";
print_r(preg_replace($pattern, $replace, $subject));
?>

    
```php

El ejemplo anterior mostrará:

    preg_filter devuelve
    Array
    (
        [0] => A:C:1
        [1] => B:C:a
        [2] => A:2
        [3] => B:b
        [4] => A:3
        [7] => A:4
    )
    preg_replace devuelve
    Array
    (
        [0] => A:C:1
        [1] => B:C:a
        [2] => A:2
        [3] => B:b
        [4] => A:3
        [5] => A
        [6] => B
        [7] => A:4
    )

## Véase también

Los [Patrones PCRE](#pcre.pattern), `preg_quote`, `preg_replace`, `preg_replace_callback`, `preg_grep`, `preg_last_error`
