---
title: Memcached::setSaslAuthData
description: Define las credenciales a utilizar para la autenticación
source_url: https://www.php.net/manual/es/memcached.setsaslauthdata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/setsaslauthdata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: false
translation_revision: 1d8068ecb
order: 46830
---

Memcached::setSaslAuthData

Define las credenciales a utilizar para la autenticación

## Descripción

```php
public Memcached::setSaslAuthData(string $username, string $password): bool
```php

`Memcached::setSaslAuthData` define el nombre de usuario así como la contraseña a utilizar durante la autenticación SASL con los servidores memcache.

*Este método solo está disponible cuando la extensión memcache ha sido compilada con soporte SASL.* Para más información, consulte la sección sobre la [instalación de Memcache](#memcached.setup).

## Parámetros

`username`  
El nombre de usuario a utilizar para la autenticación.

`password`  
La contraseña a utilizar para la autenticación.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
