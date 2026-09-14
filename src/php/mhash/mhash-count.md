---
title: mhash_count
description: Recupera el identificador máximo de hash
source_url: https://www.php.net/manual/es/function.mhash-count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mhash/functions/mhash-count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mhash
translation_status: ready
translation_reviewed: false
translation_revision: 9b1673cf1
order: 46930
---

mhash_count

Recupera el identificador máximo de hash

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.1.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] mhash_count(): int
```php

Recupera el identificador máximo de hash.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el identificador de hash máximo. Los hashes están numerados de 0 hasta este identificador.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Esta función ha sido deprecada. Utilizar las [funciones `hash_*()`](#ref.hash) en su lugar. |

## Ejemplos

Recorrer la lista de hashes

```
<?php

$nr = mhash_count();

for ($i = 0; $i <= $nr; $i++) {
    echo sprintf("El tamaño de bloque de %s es %d\n",
        mhash_get_hash_name($i),
        mhash_get_block_size($i));
}
?>

    
```php
