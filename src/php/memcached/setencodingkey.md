---
title: Memcached::setEncodingKey
description: Establece la clave de cifrado AES para los datos en Memcached
source_url: https://www.php.net/manual/es/memcached.setencodingkey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/setencodingkey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 7e6d80ad1
order: 46780
---

Memcached::setEncodingKey

Establece la clave de cifrado AES para los datos en Memcached

## Descripción

```php
public Memcached::setEncodingKey(string $key): bool
```php

Este método establece la clave de cifrado/descifrado AES para los datos escritos y leídos desde Memcached.

## Parámetros

`key`  
La clave AES.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

Memcached::get

Memcached::add

Memcached::set
