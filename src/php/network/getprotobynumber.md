---
title: getprotobynumber
description: Devuelve el nombre de protocolo asociado a un número de protocolo
source_url: https://www.php.net/manual/es/function.getprotobynumber.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/getprotobynumber.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 56340
---

getprotobynumber

Devuelve el nombre de protocolo asociado a un número de protocolo

## Descripción

```php
getprotobynumber(int $protocol): string
```php

`getprotobynumber` devuelve el nombre de protocolo asociado al protocolo `protocol`, como se describe en `/etc/protocols`.

## Parámetros

`protocol`  
El número del protocolo.

## Valores devueltos

Devuelve el nombre del protocolo, en forma de `string` o `false` si ocurre un error.

## Véase también

`getprotobyname`
