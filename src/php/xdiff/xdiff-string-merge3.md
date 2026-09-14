---
title: xdiff_string_merge3
description: Unir tres cadenas en una
source_url: https://www.php.net/manual/es/function.xdiff-string-merge3.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xdiff/functions/xdiff-string-merge3.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xdiff
translation_status: ready
translation_reviewed: false
translation_revision: 14af302c9
order: 102230
---

xdiff_string_merge3

Unir tres cadenas en una

## Descripción

```php
xdiff_string_merge3(string $old_data, string $new_data1, string $new_data2, [string $error]): mixed
```php

Une tres cadenas en una y devuelve el resultado. El parámetro `old_data` es una versión original de los datos mientras `new_data1` y `new_data2` son versiones modificadas de un original. El parámetro opcional `error` es utilizado para admitir cualquier fragmento erróneo durante el proceso de unión.

## Parámetros

`old_data`  
Primera cadena con información. Esta actúa como "vieja" información.

`new_data1`  
Segunda cadena con información. Esta actúa como versión modificada del `old_data`.

`new_data2`  
La tercera cadena con información. Esta actúa como versión modificada del `old_data`.

`error`  
Si se produce algún fragmento erróneo entonces se almacenan dentro de esta variable.

## Valores devueltos

Devuelve la cadena unida, `false` si se produce un error interno, o `true` si la cadena unida está vacía.

## Véase también

`xdiff_file_merge3`
