---
title: mhash_get_block_size
description: Devuelve el tamaño del bloque del hash
source_url: https://www.php.net/manual/es/function.mhash-get-block-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mhash/functions/mhash-get-block-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mhash
translation_status: ready
translation_reviewed: false
translation_revision: 9b1673cf1
order: 46940
---

mhash_get_block_size

Devuelve el tamaño del bloque del hash

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.1.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] mhash_get_block_size(int $algo): int
```php

Devuelve el tamaño del bloque del `algo` especificado.

## Parámetros

`algo`  
El identificador del hash. Una de las constantes `MHASH_hashname`.

## Valores devueltos

Devuelve el tamaño, en bytes, o `false` si el `algo` no existe.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Esta función ha sido deprecada. Utilizar las [funciones `hash_*()`](#ref.hash) en su lugar. |

## Ejemplos

Ejemplo con `mhash_get_block_size`

```
<?php

echo mhash_get_block_size(MHASH_MD5); // 16

?>

    
```php
