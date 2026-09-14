---
title: Memcached::appendByKey
description: Añade datos a un elemento
source_url: https://www.php.net/manual/es/memcached.appendbykey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/appendbykey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46390
---

Memcached::appendByKey

Añade datos a un elemento

## Descripción

```php
public Memcached::appendByKey(string $server_key, string $key, string $value): bool
```php

`Memcached::appendByKey` es funcionalmente equivalente a Memcached::append, pero la variable libre `server_key` puede ser utilizada para dirigir la clave `key` a un servidor específico.

## Parámetros

`server_key`  
La clave que identifica el servidor donde almacenar o recuperar el valor. En lugar de calcular el hash sobre la clave real del elemento, se calcula el hash sobre la clave del servidor al decidir con qué servidor memcached comunicarse. Esto permite agrupar elementos relacionados en un solo servidor para mayor eficiencia con operaciones múltiples.

`key`  
La clave del elemento al que se añaden datos.

`value`  
La cadena a añadir.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Devuelve `null` si la compresión está activada.

## Errores/Excepciones

Devuelve `null` y genera un `E_WARNING` si la compresión está activada.

## Véase también

Memcached::append, Memcached::prepend
