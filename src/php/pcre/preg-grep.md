---
title: preg_grep
description: Devuelve un array con los resultados de la búsqueda
source_url: https://www.php.net/manual/es/function.preg-grep.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcre/functions/preg-grep.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcre
translation_status: ready
translation_reviewed: true
translation_revision: d6f54016d
order: 61580
---

preg_grep

Devuelve un array con los resultados de la búsqueda

## Descripción

```php
preg_grep(string $pattern, array $array, [int $flags]): array
```php

Devuelve el array que contiene los elementos de `array` que satisfacen el patrón `pattern`.

## Parámetros

`pattern`  
El patrón a buscar, en forma de cadena.

`array`  
El array de entrada.

`flags`  
Si esta opción tiene el valor `PREG_GREP_INVERT`, esta función devuelve los elementos del array de entrada que *no* coinciden con el patrón `pattern`.

## Valores devueltos

Devuelve un array indexado, utilizando las claves del `array` de entrada, o `false` si ocurre un error.

## Errores/Excepciones

Si el patrón regex pasado no se compila a una regex válida, se emite una `E_WARNING`.

## Ejemplos

Ejemplo con `preg_grep`

```
<?php
$array = [ "4", M_PI, "2.74", 42 ];

// devuelve todos los elementos del array que contienen números de punto flotante
$fl_array = preg_grep("/^(\d+)?\.\d+$/", $array);

var_dump($fl_array);
?>

    
```php

## Véase también

Los [Patrones PCRE](#pcre.pattern), `preg_quote`, `preg_match_all`, `preg_filter`, `preg_last_error`
