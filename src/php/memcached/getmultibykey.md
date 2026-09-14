---
title: Memcached::getMultiByKey
description: Lee varios elementos de un servidor específico
source_url: https://www.php.net/manual/es/memcached.getmultibykey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/getmultibykey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46580
---

Memcached::getMultiByKey

Lee varios elementos de un servidor específico

## Descripción

```php
public Memcached::getMultiByKey(string $server_key, array $keys, [int $get_flags]): array
```php

`Memcached::getMultiByKey` es funcionalmente equivalente a Memcached::getMulti, pero la variable libre `server_key` puede ser utilizada para dirigir la clave `key` a un servidor específico.

## Parámetros

`server_key`  
La clave que identifica el servidor donde almacenar o recuperar el valor. En lugar de calcular el hash sobre la clave real del elemento, se calcula el hash sobre la clave del servidor al decidir con qué servidor memcached comunicarse. Esto permite agrupar elementos relacionados en un solo servidor para mayor eficiencia con operaciones múltiples.

`keys`  
Un array de claves a leer.

`get_flags`  
Las opciones de la operación.

## Valores devueltos

Devuelve el array de elementos encontrados o `false` si ocurre un error. Utilice Memcached::getResultCode si es necesario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL memcached 3.0.0 | El parámetro `cas_tokens` ha sido eliminado. `Memcached::GET_EXTENDED` ha sido añadida y cuando se pasa como flag asegura que los tokens CAS sean recuperados. |

## Véase también

Memcached::getMulti, Memcached::get, Memcached::getDelayed
