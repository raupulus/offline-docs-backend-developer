---
title: Memcached::getDelayedByKey
description: Lee varios elementos en un servidor
source_url: https://www.php.net/manual/es/memcached.getdelayedbykey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/getdelayedbykey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46560
---

Memcached::getDelayedByKey

Lee varios elementos en un servidor

## Descripción

```php
public Memcached::getDelayedByKey(string $server_key, array $keys, [bool $with_cas], [callable $value_cb]): bool
```php

`Memcached::getDelayedByKey` es funcionalmente equivalente a Memcached::getDelayed, pero la variable libre `server_key` puede ser utilizada para dirigir la clave `key` a un servidor específico.

## Parámetros

`server_key`  
La clave que identifica el servidor donde almacenar o recuperar el valor. En lugar de calcular el hash sobre la clave real del elemento, se calcula el hash sobre la clave del servidor al decidir con qué servidor memcached comunicarse. Esto permite agrupar elementos relacionados en un solo servidor para mayor eficiencia con operaciones múltiples.

`keys`  
Un array de claves a leer.

`with_cas`  
Si también se deben leer los CAS.

`value_cb`  
Una función de retrollamada de resultados, o `null`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Utilice Memcached::getResultCode si es necesario.

## Véase también

Memcached::getDelayed, Memcached::fetch, Memcached::fetchAll
