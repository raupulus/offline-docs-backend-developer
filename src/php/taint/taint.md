---
title: taint
description: Corrompe un string
source_url: https://www.php.net/manual/es/function.taint.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/taint/functions/taint.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: taint
translation_status: ready
translation_revision: 9e0f03ac3
order: 93800
---

taint

Corrompe un string

## Descripción

```php
taint(string $string, string ...$strings): bool
```php

Crea un string corrompido. Solamente se usa para realizar pruebas.

## Parámetros

`string`  

`strings`  

## Valores devueltos

Devuelve TRUE si la transformación se lleva a cabo. Siempre devuelve TRUE si la extensión taint no esta activada.
