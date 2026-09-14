---
title: Memcached::getAllKeys
description: Recupera todas las claves almacenadas en todos los servidores
source_url: https://www.php.net/manual/es/memcached.getallkeys.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/getallkeys.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: false
translation_revision: 1d8068ecb
order: 46530
---

Memcached::getAllKeys

Recupera todas las claves almacenadas en todos los servidores

## Descripción

```php
public Memcached::getAllKeys(): array
```php

`Memcached::getAllKeys` consulta cada servidor memcache y recupera un array que contiene todas las claves almacenadas en cada uno de ellos. No se trata de una operación atómica, por lo que no proporciona una imagen realmente consistente de las claves en el instante dado. Dado que memcache no garantiza devolver todas las claves, no puede asegurarse de que todas las claves hayan sido devueltas.

> [!NOTE]
> Este método está destinado a fines de depuración y no debe utilizarse a gran escala.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve las claves almacenadas en todos los servidores en caso de éxito o `false` si ocurre un error.
