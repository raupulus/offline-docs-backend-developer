---
title: mysqli::$server_version
description: Devuelve un integer que representa la versión del servidor MySQL
source_url: https://www.php.net/manual/es/mysqli.get-server-version.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/get-server-version.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 7caf2b8df
order: 55130
---

mysqli::\$server_version

mysqli_get_server_version

Devuelve un integer que representa la versión del servidor MySQL

## Descripción

Estilo orientado a objetos

int

mysqli-\>server_version

Estilo procedimental

```php
mysqli_get_server_version(mysqli $mysql): int
```php

La función `mysqli_get_server_version` devuelve un integer que representa la versión del servidor al que se está conectado (representado por el argumento `mysql`).

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Un integer que representa la versión del servidor.

El formato de este número es `main_version * 10000 + minor_version * 100 + sub_version` (es decir, la versión 4.1.0 devolverá 40100).

## Ejemplos

Ejemplo con `$mysqli->server_version`

Estilo orientado a objetos

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password");

/* Muestra la versión del servidor */
printf("Versión del servidor: %d\n", $mysqli->server_version);

   
```php

Estilo procedimental

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password");

/* Muestra la versión del servidor */
printf("Versión del servidor: %d\n", mysqli_get_server_version($link));

   
```php

Los ejemplos anteriores mostrarán algo similar a:

    Versión del servidor: 80021

## Véase también

`mysqli_get_client_info`, `mysqli_get_client_version`, `mysqli_get_server_info`
