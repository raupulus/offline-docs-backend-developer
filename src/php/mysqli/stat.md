---
title: mysqli::stat
description: Obtiene el estado actual del sistema
source_url: https://www.php.net/manual/es/mysqli.stat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/stat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 9e0a92ed2
order: 55390
---

mysqli::stat

mysqli_stat

Obtiene el estado actual del sistema

## Descripción

Estilo orientado a objetos

```php
public mysqli::stat(): string
```php

Estilo procedimental

```php
mysqli_stat(mysqli $mysql): string
```

`mysqli_stat` devuelve un string que contiene información similar al comando '`mysqladmin status`'. Esto incluye el tiempo de actividad, expresado en segundos y el número de hilos actuales, el número de comandos, las tablas recargadas y abiertas.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Un `string` que describe el estado del servidor. `false` es devuelto si ocurre un error.

## Ejemplos

Ejemplo con mysqli::stat

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

printf ("Estado del sistema: %s\n", $mysqli->stat());

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

printf("Estado del sistema: %s\n", mysqli_stat($link));

   
```

Los ejemplos anteriores mostrarán:

    Estado del sistema: Uptime: 272  Threads: 1  Questions: 5340  Slow queries: 0
    Opens: 13  Flush tables: 1  Open tables: 0  Queries per second avg: 19.632
    Memory in use: 8496K  Max memory used: 8560K

## Véase también

`mysqli_get_server_info`
