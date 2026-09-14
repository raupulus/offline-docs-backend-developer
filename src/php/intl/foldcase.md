---
title: IntlChar::foldCase
description: Realiza el plegado de mayúsculas/minúsculas sobre un punto de código
source_url: https://www.php.net/manual/es/intlchar.foldcase.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/foldcase.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: c142be811
order: 40790
---

IntlChar::foldCase

Realiza el plegado de mayúsculas/minúsculas sobre un punto de código

## Descripción

```php
public static IntlChar::foldCase(int $codepoint, [int $options]): int
```php

El carácter dado se mapea a su equivalente de plegado de mayúsculas/minúsculas; si el carácter no tiene equivalente de plegado de mayúsculas/minúsculas, se devuelve el carácter mismo.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

`options`  
Puede ser `IntlChar::FOLD_CASE_DEFAULT` (valor por omisión) o `IntlChar::FOLD_CASE_EXCLUDE_SPECIAL_I`.

## Valores devueltos

Devuelve el *plegado de mayúsculas/minúsculas simple* del punto de código, si está disponible; de lo contrario, el punto de código mismo en caso de éxito, o `null` en caso de fallo.
