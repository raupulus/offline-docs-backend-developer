---
title: oci_set_client_info
description: Define la información del cliente
source_url: https://www.php.net/manual/es/function.oci-set-client-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-set-client-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_revision: 729d3d6ef
order: 57620
---

oci_set_client_info

Define la información del cliente

## Descripción

```php
oci_set_client_info(resource $connection, string $client_info): bool
```php

Define la información del cliente para el trazado de Oracle.

La información del cliente se registra en la base de datos durante el próximo intercambio 'round-trip' desde PHP hacia la base de datos; típicamente, cuando se ejecuta una consulta SQL.

La información del cliente puede ser consultada posteriormente desde la vista de administración de la base de datos `V$SESSION`.

El valor se conserva mediante el mecanismo de conexiones persistentes.

## Parámetros

`connection`  
Un identificador de conexión Oracle, devuelto por la función `oci_connect`, `oci_pconnect` o la función `oci_new_connect`.

`client_info`  
Cadena de caracteres de hasta 64 bytes de longitud.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Define la información del cliente

```
<?php

$c = oci_connect('hr', 'welcome', 'localhost/XE');

// Registra la información del cliente
oci_set_client_info($c, 'My Application Version 2');

// Código que genera un intercambio (round-trip), por ejemplo, una consulta:
$s = oci_parse($c, 'select * from dual');
oci_execute($s);
oci_fetch_all($s, $res);

sleep(30);

?>

    
```php

    // Durante la ejecución de este script, el administrador puede ver la información
    // del cliente:

    sqlplus system/welcome
    SQL> select client_info from v$session;

## Notas

> [!NOTE]
> Esta función está disponible si PHP está vinculado a partir de la versión 10*g* de la biblioteca de la base de datos Oracle.

> [!TIP]
> Con versiones antiguas de OCI8 o bases de datos Oracle antiguas, la información del cliente puede ser definida usando el paquete Oracle `DBMS_APPLICATION_INFO`. Esto es menos eficiente que usar la función `oci_set_client_info`.

> [!CAUTION]
> Algunas funciones OCI8 requieren ida y vuelta con la base de datos. Estas ida y vuelta pueden ser evitadas al usar consultas cuyo resultado es almacenado en caché.

## Véase también

`oci_set_module_name`, `oci_set_action`, `oci_set_client_identifier`, `oci_set_db_operation`
