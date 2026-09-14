---
title: WeakMap::offsetExists
description: Verifica si un cierto objeto se encuentra en el diccionario
source_url: https://www.php.net/manual/es/weakmap.offsetexists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/weakmap/offsetexists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: d27fdfe8f
order: 4280
---

WeakMap::offsetExists

Verifica si un cierto objeto se encuentra en el diccionario

## Descripción

```php
public WeakMap::offsetExists(object $object): bool
```php

Verifica si el objeto transmitido está referenciado en el diccionario.

## Parámetros

`object`  
Objeto a verificar.

## Valores devueltos

Devuelve `true` si el objeto está contenido en el diccionario, `false` en caso contrario.
