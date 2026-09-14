---
title: mcrypt_enc_get_key_size
description: Devuelve el tamaño máximo de la clave para un modo
source_url: https://www.php.net/manual/es/function.mcrypt-enc-get-key-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-enc-get-key-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45750
---

mcrypt_enc_get_key_size

Devuelve el tamaño máximo de la clave para un modo

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_enc_get_key_size(resource $td): int
```php

Devuelve el tamaño máximo de la clave para un modo dado.

## Parámetros

`td`  
El gestor de fichero.

## Valores devueltos

Devuelve el tamaño máximo de la clave para el modo dado.
