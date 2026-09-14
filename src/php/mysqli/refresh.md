---
title: mysqli::refresh
description: Actualiza
source_url: https://www.php.net/manual/es/mysqli.refresh.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/refresh.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 9b1673cf1
order: 55310
---

mysqli::refresh

mysqli_refresh

Actualiza

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.4.0. Depender de esta función está altamente desaconsejado.

## Descripción

Estilo orientado a objetos

```php
#[\Deprecated] public mysqli::refresh(int $flags): bool
```php

Estilo procedimental

```php
#[\Deprecated] mysqli_refresh(mysqli $mysql, int $flags): bool
```

Actualiza las tablas o las cachés, o reinicia la información del servidor de réplica.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`flags`  
Las opciones de actualización, utilizando las constantes MYSQLI_REFRESH\_\* como se documenta en la documentación sobre las [constantes MySQLi](#mysqli.constants).

Consulte también la documentación oficial sobre [la actualización en MySQL](https://dev.mysql.com/doc/c-api/8.4/en/mysql-refresh.html).

## Valores devueltos

`true` si la actualización se realizó con éxito, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Los métodos mysqli::refresh y `mysqli_refresh` están ahora obsoletos. Utilice los comandos SQL `FLUSH` en su lugar. |

## Véase también

`mysqli_poll`
