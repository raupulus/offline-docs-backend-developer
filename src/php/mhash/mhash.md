---
title: mhash
description: Calcula un hash
source_url: https://www.php.net/manual/es/function.mhash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mhash/functions/mhash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mhash
translation_status: ready
translation_reviewed: false
translation_revision: 9b1673cf1
order: 46970
---

mhash

Calcula un hash

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.1.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] mhash(int $algo, string $data, [string $key]): string
```php

`mhash` aplica la función de hash `algo` a los datos `data`.

## Parámetros

`algo`  
El identificador del hash. Uno de los constantes `MHASH_hashname`.

`data`  
La entrada del usuario, en forma de `string`.

`key`  
Especificado, la función devolverá el HMAC resultante. HMAC es un hash indexado utilizado para la identificación de mensaje, o bien un simple informe de mensaje, según la clave especificada. Algunos algoritmos soportados en mhash no son compatibles con el modo HMAC.

## Valores devueltos

Devuelve el hash resultante (también llamado "digest") o HMAC, en forma de `string` o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Esta función ha sido deprecada. Utilizar las [funciones `hash_*()`](#ref.hash) en su lugar. |
| 8.0.0 | `key` es ahora nullable. |
