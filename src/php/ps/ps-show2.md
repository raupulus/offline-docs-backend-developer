---
title: ps_show2
description: Imprimir texto en la posición actual
source_url: https://www.php.net/manual/es/function.ps-show2.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-show2.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_revision: a5db4a7ff
order: 66240
---

ps_show2

Imprimir texto en la posición actual

## Descripción

```php
ps_show2(resource $psdoc, string $text, int $len): bool
```php

Imprime texto en la posición actual. No imprime más de `len` caracteres.

## Parámetros

`psdoc`  
Un identificador de recurso del fichero postscript, como el devuelto por la función `ps_new`.

`text`  
El texto a imprimir.

`len`  
El número máximo de caracteres a imprimir.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
