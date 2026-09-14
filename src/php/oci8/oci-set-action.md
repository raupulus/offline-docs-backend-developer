---
title: oci_set_action
description: Define el nombre de la acción
source_url: https://www.php.net/manual/es/function.oci-set-action.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-set-action.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_revision: ed6de1ae2
order: 57590
---

oci_set_action

Define el nombre de la acción

## Descripción

```php
oci_set_action(resource $connection, string $action): bool
```php

Define el nombre de la acción para un seguimiento de Oracle.

El nombre de la acción se registra en la base de datos durante el próximo intercambio 'round-trip' desde PHP hacia la base de datos; típicamente, cuando se ejecuta una consulta SQL.

El nombre de la acción puede ser consultado posteriormente desde la vista de administración de la base de datos `V$SESSION`. Puede ser utilizado para rastrear y monitorear otras vistas como `V$SQLAREA` y `DBMS_MONITOR.SERV_MOD_ACT_STAT_ENABLE`.

El valor puede ser conservado a través de las conexiones persistentes.

## Parámetros

`connection`  
Un identificador de conexión Oracle, devuelto por la función `oci_connect`, `oci_pconnect` o la función `oci_new_connect`.

`action`  
String seleccionado por el usuario de hasta 32 caracteres de longitud.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Definición de una acción

```
<?php

$c = oci_connect('hr', 'welcome', 'localhost/XE');

// Registra la acción
oci_set_action($c, 'Friend Lookup');

// Código que genera un intercambio (round-trip), por ejemplo, una consulta:
$s = oci_parse($c, 'select * from dual');
oci_execute($s);
oci_fetch_all($s, $res);

sleep(30);

?>

    
```php

    // Durante la ejecución del script, el administrador puede ver las acciones
    // en curso de ejecución:

    sqlplus system/welcome
    SQL> select action from v$session;

## Notas

> [!NOTE]
> Esta función está disponible si PHP está vinculado a partir de la versión 10*g* de la biblioteca de la base de datos Oracle.

> [!TIP]
> Con versiones antiguas de OCI8 o bases de datos Oracle antiguas, la información del cliente puede ser definida usando el paquete Oracle `DBMS_APPLICATION_INFO`. Esto es menos eficiente que usar la función `oci_set_client_info`.

> [!CAUTION]
> Algunas funciones OCI8 requieren ida y vuelta con la base de datos. Estas ida y vuelta pueden ser evitadas al usar consultas cuyo resultado es almacenado en caché.

## Véase también

`oci_set_module_name`, `oci_set_client_info`, `oci_set_client_identifier`, `oci_set_db_operation`
