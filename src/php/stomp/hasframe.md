---
title: Stomp::hasFrame
description: Indica si existe o no una trama lista para leer
source_url: https://www.php.net/manual/es/stomp.hasframe.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stomp/stomp/hasframe.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stomp
translation_status: ready
translation_reviewed: false
translation_revision: 9c7e8795c
order: 87620
---

Stomp::hasFrame

stomp_has_frame

Indica si existe o no una trama lista para leer

## Descripción

Estilo orientado a objetos (método):

```php
public Stomp::hasFrame(): bool
```php

Estilo procedimental:

```php
stomp_has_frame(resource $link): bool
```

Indica si existe o no una trama lista para leer.

## Parámetros

`link`  
Estilo procedimental únicamente: El identificador stomp devuelto por la función`stomp_connect`.

## Valores devueltos

Devuelve `true` si hay una trama lista para leer, o `false` en caso contrario.
