---
title: mysqli::$host_info
description: Devuelve un string que contiene el tipo de conexión utilizada
source_url: https://www.php.net/manual/es/mysqli.get-host-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/get-host-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: fc16f84d9
order: 55100
---

mysqli::\$host_info

mysqli_get_host_info

Devuelve un string que contiene el tipo de conexión utilizada

## Descripción

Estilo orientado a objetos

string

mysqli-\>host_info

Estilo procedimental

```php
mysqli_get_host_info(mysqli $mysql): string
```php

`mysqli_get_host_info` devuelve un string de caracteres que describe la conexión representada por el argumento `mysql` (incluyendo el nombre de host del servidor).

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Un string que representa el nombre de host del servidor y el tipo de conexión.

## Ejemplos

Ejemplo con `$mysqli->host_info`

Estilo orientado a objetos

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Muestra información sobre el host */
printf("Información sobre el host: %s\n", $mysqli->host_info);

   
```php

Estilo procedimental

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

/* Muestra información sobre el host */
printf("Información sobre el host: %s\n", mysqli_get_host_info($link));

   
```php

Los ejemplos anteriores mostrarán:

    Información sobre el host: Localhost via UNIX socket

## Véase también

`mysqli_get_proto_info`
