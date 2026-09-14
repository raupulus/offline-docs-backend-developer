---
title: mysqli::$server_info
description: Devuelve la versión del servidor MySQL
source_url: https://www.php.net/manual/es/mysqli.get-server-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/get-server-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 1a7e56aa8
order: 55120
---

mysqli::\$server_info

mysqli::get_server_info

mysqli_get_server_info

Devuelve la versión del servidor MySQL

## Descripción

Estilo orientado a objetos

string

mysqli-\>server_info

```php
public mysqli::get_server_info(): string
```php

Estilo procedimental

```php
mysqli_get_server_info(mysqli $mysql): string
```

Devuelve un string que representa la versión del servidor MySQL al cual la extensión MySQLi está conectada (representado por el argumento `link`).

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Un `string` que representa la versión del servidor.

## Ejemplos

Ejemplo con `$mysqli->server_info`

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password");

/* Muestra la versión del servidor */
printf("Versión del servidor: %s\n", $mysqli->server_info);

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password");

/* Muestra la versión del servidor */
printf("Versión del servidor: %s\n", mysqli_get_server_info($link));

   
```

Los ejemplos anteriores mostrarán algo similar a:

    Versión del servidor: 8.0.21

## Véase también

`mysqli_get_client_info`, `mysqli_get_client_version`, `mysqli_get_server_version`
