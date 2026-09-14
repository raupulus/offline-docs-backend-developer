---
title: cubrid_ping
description: Hacer ping en una conexión al servidor o reconectar si no hay conexión
source_url: https://www.php.net/manual/es/function.cubrid-ping.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-ping.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: ee1ce6a0e
order: 8800
---

cubrid_ping

Hacer ping en una conexión al servidor o reconectar si no hay conexión

## Descripción

```php
cubrid_ping([resource $conn_identifier]): bool
```php

Verifica si la conexión al servidor está funcionando..

## Parámetros

`conn_identifier`  
El identificador de conexión de CUBRID. Si el identificador de conexión no se especifica, se asume la última conexión abierta por `cubrid_connect`.

## Valores devueltos

Devuelve `true` si la conexión al servidor CUBRID está funcionando, si no `false`.

## Ejemplos

Ejemplo de `cubrid_ping`

```
<?php
set_time_limit(0);

$con = cubrid_connect('localhost', 33000, 'demodb');

/* Se asume que esta consulta tomará mucho tiempo */
$sql = "select * from athlete";
$result = cubrid_query($sql);
if (!$result) {
    echo 'La consulta #1 falló, saliendo.';
    exit;
}

/* Asegurarse de que la conexión todavía perdura, si no, intentar reconectar */
if (!cubrid_ping($con)) {
    echo 'Conexión perdida, saliendo después de la consulta #1';
    exit;
}
cubrid_free_result($result);

/* Ya que la conexión aún perdura, vamos a ejecutar otra consulta */
$sql2 = "select * from code";
$result2 = cubrid_query($sql2);
?>

   
```php
