---
title: mhash_get_hash_name
description: Devuelve el nombre del hash
source_url: https://www.php.net/manual/es/function.mhash-get-hash-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mhash/functions/mhash-get-hash-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mhash
translation_status: ready
translation_reviewed: false
translation_revision: 9b1673cf1
order: 46950
---

mhash_get_hash_name

Devuelve el nombre del hash

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.1.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] mhash_get_hash_name(int $algo): string
```php

Devuelve el nombre del `algo` especificado.

## Parámetros

`algo`  
El identificador del hash. Una de las constantes `MHASH_hashname`.

## Valores devueltos

Devuelve el nombre del hash o `false` si el hash no existe.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Esta función ha sido deprecada. Utilizar las [funciones `hash_*()`](#ref.hash) en su lugar. |

## Ejemplos

Ejemplo con `mhash_get_hash_name`

```
<?php

echo mhash_get_hash_name(MHASH_MD5); // MD5

?>

    
```php
