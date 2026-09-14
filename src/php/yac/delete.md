---
title: Yac::delete
description: Eliminar los artículos de la memoria caché
source_url: https://www.php.net/manual/es/yac.delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yac/yac/delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yac
translation_status: ready
translation_reviewed: false
translation_revision: 53242ee66
order: 104310
---

Yac::delete

Eliminar los artículos de la memoria caché

## Descripción

```php
public Yac::delete(string $keys, [int $ttl]): bool
```php

retira los artículos de la memoria caché

## Parámetros

`keys`  
clave string, o array de multiples claves para ser removidas.

`ttl`  
si se establece un retraso, la eliminación marcará los elementos como inválidos en ttl segundo.

## Valores devueltos
