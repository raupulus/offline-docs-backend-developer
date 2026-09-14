---
title: oci_set_call_timeout
description: Define un tiempo de espera en milisegundos para las llamadas a la base
  de datos
source_url: https://www.php.net/manual/es/function.oci-set-call-timout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-set-call-timeout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: e2db993fb
order: 57600
---

oci_set_call_timeout

Define un tiempo de espera en milisegundos para las llamadas a la base de datos

## Descripción

```php
oci_set_call_timeout(resource $connection, int $timeout): bool
```php

Define un tiempo de espera que limita el tiempo máximo que puede tomar un intercambio de base de datos utilizando esta conexión.

Cada operación OCI8 puede realizar cero o más llamadas a la biblioteca cliente de Oracle. Estas llamadas internas pueden luego realizar cero o más intercambios con la base de datos Oracle. Si alguno de estos intercambios toma más de `time_out` milisegundos, entonces la operación se cancela y se devuelve un error a la aplicación.

El valor `time_out` se aplica a cada intercambio individualmente, y no a la suma de todos los intercambios. El tiempo pasado procesando en PHP OCI8 antes o después de la finalización de cada intercambio no se cuenta.

Cuando una llamada es interrumpida, Oracle intentará limpiar la conexión para su reutilización. Esta operación está permitida para ejecutarse durante otro período de `time_out`. Dependiendo del resultado de la limpieza, la conexión puede o no ser reutilizable.

Cuando se utilizan conexiones persistentes, el valor del tiempo de espera será conservado entre las consultas PHP.

La función `oci_set_call_timeout` está disponible cuando OCI8 utiliza las bibliotecas clientes de Oracle 18 (o posteriores).

## Parámetros

`connection`  
Un identificador de conexión Oracle, devuelto por la función `oci_connect`, `oci_pconnect` o la función `oci_new_connect`.

`timeout`  
El tiempo máximo en milisegundos que puede tomar un intercambio entre PHP y la base de datos Oracle.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Configuración del tiempo de espera

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
oci_set_call_timeout($conn, 5000);

?>

    
```php
