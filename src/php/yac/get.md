---
title: Yac::get
description: Recuperar los valores de caché
source_url: https://www.php.net/manual/es/yac.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yac/yac/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yac
translation_status: ready
translation_reviewed: false
translation_revision: 53242ee66
order: 104340
---

Yac::get

Recuperar los valores de caché

## Descripción

```php
public Yac::get(string $key, [int $cas]): mixed
```php

Recuperar los valores de caché

## Parámetros

`key`  
claves `string`, o `array` de multiples claves.

`cas`  
Si no es `null`, se ajustará al caso del artículo recuperado.

## Valores devueltos

mixed en caso de éxito, false en caso de error
