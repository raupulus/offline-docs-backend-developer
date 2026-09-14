---
title: Yac::add
description: Guardar en caché
source_url: https://www.php.net/manual/es/yac.add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yac/yac/add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yac
translation_status: ready
translation_reviewed: false
translation_revision: 8e2cfbdce
order: 104290
---

Yac::add

Guardar en caché

## Descripción

```php
public Yac::add(string $keys, mixed $value, [int $ttl]): bool
```php

```php
public Yac::add(array $key_vals): bool
```

Añadir un artículo al caché.

## Parámetros

`keys`  
`string` clave

`value`  
valor mixto, Todo tipo de valor php podría ser almacenado excepto `resource`

`ttl`  
tiempo de expiración

## Valores devueltos

`bool`, `true` en caso de éxito, `false` en caso de fallar.

> [!NOTE]
> Yac::add puede fallar si el casillero no se puede obtener, así que, si necesitas que el valor se almacene correctamente, puedes escribir códigos como:
>
> <div class="example">
>
> <div class="title">
>
> Asegúrate de que el artículo se almacene
>
> </div>
>
> ```
>        
>        while(!$yac->set("key", "value"));
>        
>       
> ```
>
> </div>
