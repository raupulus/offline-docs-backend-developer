---
title: mysqli::$protocol_version
description: Devuelve la versión del protocolo MySQL utilizado
source_url: https://www.php.net/manual/es/mysqli.get-proto-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/get-proto-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 3e82f5030
order: 55110
---

mysqli::\$protocol_version

mysqli_get_proto_info

Devuelve la versión del protocolo MySQL utilizado

## Descripción

Estilo orientado a objetos

string

mysqli-\>protocol_version

Estilo procedimental

```php
mysqli_get_proto_info(mysqli $mysql): int
```php

Devuelve un integer que representa la versión del protocolo MySQL utilizado por la conexión representada por el argumento `mysql`.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Devuelve un integer que representa la versión del protocolo.

## Ejemplos

Ejemplo con `$mysqli->protocol_version`

Estilo orientado a objetos

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password");

/* Muestra la versión del protocolo */
printf("Versión del protocolo: %d\n", $mysqli->protocol_version);

   
```php

Estilo procedimental

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password");

/* Muestra la versión del protocolo */
printf("Versión del protocolo: %d\n", mysqli_get_proto_info($link));

   
```php

Los ejemplos anteriores mostrarán:

    Versión del protocolo: 10

## Véase también

`mysqli_get_host_info`
