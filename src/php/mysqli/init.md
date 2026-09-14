---
title: mysqli::init
description: Inicializa MySQLi y devuelve un objeto para usar con mysqli_real_connect()
source_url: https://www.php.net/manual/es/mysqli.init.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/init.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 9b1673cf1
order: 55160
---

mysqli::init

mysqli_init

Inicializa MySQLi y devuelve un objeto para usar con mysqli_real_connect()

## Descripción

Estilo orientado a objetos

```php
#[\Deprecated] public mysqli::init(): bool
```php

Estilo procedimental

```php
mysqli_init(): mysqli
```

Asigna o inicializa un objeto MySQL utilizable para las funciones `mysqli_options` y `mysqli_real_connect`.

> [!NOTE]
> Todas las llamadas siguientes a cualquier función MySQLi (excepto `mysqli_options` y `mysqli_ssl_set`) fallarán hasta que la función `mysqli_real_connect` sea llamada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

mysqli::init devuelve `null` en caso de éxito, o `false` si ocurre un error. `mysqli_init` devuelve un objeto en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El método mysqli::init de estilo orientado a objetos ha sido deprecado. Reemplace las llamadas a parent::init por parent::\_\_construct. |

## Ejemplos

Ver `mysqli_real_connect`.

## Véase también

`mysqli_options`, `mysqli_close`, `mysqli_real_connect`, `mysqli_connect`
