---
title: opcache_invalidate
description: Invalida un script almacenado en caché
source_url: https://www.php.net/manual/es/function.opcache-invalidate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/opcache/functions/opcache-invalidate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: opcache
translation_status: ready
translation_reviewed: false
translation_revision: 87d6bb1bb
order: 58600
---

opcache_invalidate

Invalida un script almacenado en caché

## Descripción

```php
opcache_invalidate(string $filename, [bool $force]): bool
```php

Esta función invalida un script particular desde el caché opcode. Si el argumento `force` no está definido o vale `false`, el script solo se invalidará si la fecha/hora de modificación del script es más reciente que el opcode en caché. Esta función solo invalida el caché en memoria y no el caché de ficheros.

## Parámetros

`filename`  
La ruta de acceso al script a invalidar.

`force`  
Si vale `true`, el script se invalidará independientemente de si la invalidación es necesaria o no.

## Valores devueltos

Devuelve `true` si el caché opcode para el `filename` ha sido invalidado, o si no había nada que invalidar, o bien `false` si el caché opcode está desactivado.

## Véase también

opcache_compile_file

opcache_reset
