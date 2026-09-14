---
title: Yac::set
description: Guardar en el caché
source_url: https://www.php.net/manual/es/yac.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yac/yac/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yac
translation_status: ready
translation_reviewed: false
translation_revision: 338bf692d
order: 104370
---

Yac::set

Guardar en el caché

## Descripción

```php
public Yac::set(string $keys, mixed $value, [int $ttl]): bool
```php

```php
public Yac::add(array $key_vals): bool
```

Añade un elemento a la caché, si la clave ya existe, se sobreescribe.

## Parámetros

`keys`  
clave `string`

`value`  
valor mixed, Todo tipo de valor php podría ser almacenado excepto `resource`

`ttl`  
tiempo de expiración

## Valores devueltos

el valor de sí mismo
