---
title: IntlChar::charAge
description: Devuelve la "edad" del punto de código
source_url: https://www.php.net/manual/es/intlchar.charage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/charage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40680
---

IntlChar::charAge

Devuelve la "edad" del punto de código

## Descripción

```php
public static IntlChar::charAge(int $codepoint): array
```php

Devuelve la "edad" del punto de código.

La "edad" es la versión Unicode cuando el punto de código fue designado por primera vez (como un no-carácter o para uso privado) o asignado a un carácter. Esto puede ser útil para evitar emitir puntos de código a procesos de recepción que no aceptan caracteres más recientes.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

La versión Unicode, en forma de un `array`. Por ejemplo, la versión *1.3.31.2* sería representada por `[1, 3, 31, 2]`. Devuelve `null` en caso de fallo.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::charage("\u{2603}"));
var_dump(IntlChar::charage("\u{1F576}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    array(4) {
      [0]=>
      int(1)
      [1]=>
      int(1)
      [2]=>
      int(0)
      [3]=>
      int(0)
    }
    array(4) {
      [0]=>
      int(7)
      [1]=>
      int(0)
      [2]=>
      int(0)
      [3]=>
      int(0)
    }

## Véase también

`IntlChar::getUnicodeVersion`, `IntlChar::getIntPropertyMinValue`, `IntlChar::getIntPropertyValue`
