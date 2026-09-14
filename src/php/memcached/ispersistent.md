---
title: Memcached::isPersistent
description: Verifica si una conexión persistente hacia memcache está en uso
source_url: https://www.php.net/manual/es/memcached.ispersistent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/ispersistent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_revision: 6047c10c1
order: 46680
---

Memcached::isPersistent

Verifica si una conexión persistente hacia memcache está en uso

## Descripción

```php
public Memcached::isPersistent(): bool
```php

`Memcached::isPersistent` verifica si las conexiones a los servidores memcache son conexiones persistentes.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la instancia Memcache utiliza una conexión persistente, `false` en caso contrario.

## Véase también

Memcached::isPristine
