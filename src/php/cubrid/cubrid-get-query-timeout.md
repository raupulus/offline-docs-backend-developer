---
title: cubrid_get_query_timeout
description: Obtener el valor del tiempo de espera de consulta de la petición
source_url: https://www.php.net/manual/es/function.cubrid-get-query-timeout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-get-query-timeout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9100
---

cubrid_get_query_timeout

Obtener el valor del tiempo de espera de consulta de la petición

## Descripción

```php
cubrid_get_query_timeout(resource $req_identifier): int
```php

La función `cubrid_get_query_timeout` se usa para obtener el tiempo de espera de consulta de la petición.

## Parámetros

`req_identifier`  
Identificador de petición.

## Valores devueltos

Devuelve el valor de tiempo de espera de la consulta en milisegundos de la petición actual en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `cubrid_get_query_timeout`

```
<?php

$host = "localhost";
$port = 33000;
$db = "demodb";

$conn =
cubrid_connect_with_url("CUBRID:$host:$port:$db:::?login_timeout=50000&query_timeout=5000&disconnect_on_query_timeout=yes");

$req = cubrid_prepare($conn, "SELECT * FROM code");

$timeout = cubrid_get_query_timeout($req);
var_dump($timeout);

cubrid_set_query_timeout($req, 1000);
$timeout = cubrid_get_query_timeout($req);
var_dump($timeout);

cubrid_close($conn);
?>

   
```php

El ejemplo anterior mostrará:

    int(5000)
    int(1000)

## Véase también

cubrid_set_query_timeout
