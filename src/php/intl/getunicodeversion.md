---
title: IntlChar::getUnicodeVersion
description: Devuelve la versión Unicode
source_url: https://www.php.net/manual/es/intlchar.getunicodeversion.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/getunicodeversion.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40930
---

IntlChar::getUnicodeVersion

Devuelve la versión Unicode

## Descripción

```php
public static IntlChar::getUnicodeVersion(): array
```php

Devuelve las informaciones de versión Unicode.

El array de versión se rellena con las informaciones de versión para la norma Unicode actualmente utilizada por ICU. Por ejemplo, la versión Unicode 3.1.1 se representa mediante un array con los valores `[3, 1, 1, 0]`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array que contiene el número de versión Unicode.

## Ejemplos

Probar diferentes propiedades

```
    
<?php
var_dump(IntlChar::getUnicodeVersion());
?>

   
```php

El ejemplo anterior mostrará:

        
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

`IntlChar::charAge`
