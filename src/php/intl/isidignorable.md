---
title: IntlChar::isIDIgnorable
description: Verifica si un punto de código es un carácter ignorable
source_url: https://www.php.net/manual/es/intlchar.isidignorable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isidignorable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41030
---

IntlChar::isIDIgnorable

Verifica si un punto de código es un carácter ignorable

## Descripción

```php
public static IntlChar::isIDIgnorable(int $codepoint): bool
```php

Determina si el carácter especificado debe ser considerado como un carácter ignorable en un identificador.

`true` para los caracteres de categoría general "Cf" (controles de formato) así como los controles ISO no espacios (U+0000..U+0008, U+000E..U+001B, U+007F..U+009F).

> [!NOTE]
> Cabe señalar que Unicode simplemente recomienda ignorar Cf (controles de formato).

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` es ignorable en los identificadores, `false` en caso contrario. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isIDIgnorable("A"));
var_dump(IntlChar::isIDIgnorable(" "));
var_dump(IntlChar::isIDIgnorable("\u{007F}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(false)
    bool(false)
    bool(true)

## Véase también

`IntlChar::isIDStart`, `IntlChar::isIDPart`, `IntlChar::PROPERTY_DEFAULT_IGNORABLE_CODE_POINT`
