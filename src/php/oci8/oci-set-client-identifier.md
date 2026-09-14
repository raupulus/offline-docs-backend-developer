---
title: oci_set_client_identifier
description: Define el identificador del cliente
source_url: https://www.php.net/manual/es/function.oci-set-client-identifier.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-set-client-identifier.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_revision: ed6de1ae2
order: 57610
---

oci_set_client_identifier

Define el identificador del cliente

## Descripción

```php
oci_set_client_identifier(resource $connection, string $client_id): bool
```php

Define el identificador del cliente, utilizado por numerosos componentes de la base de datos para identificar a los usuarios de la aplicación que se autentican con el mismo nombre de usuario de la base de datos.

El identificador del cliente se registra en la base de datos durante el próximo intercambio 'round-trip' desde PHP hacia la base de datos; típicamente, la ejecución de una consulta SQL.

El identificador puede ser consultado posteriormente, por ejemplo, con la consulta `SELECT SYS_CONTEXT('USERENV','CLIENT_IDENTIFIER') FROM DUAL`. Una vista de administración de la base de datos, como la vista `V$SESSION` también contiene el valor. Puede ser utilizado con `DBMS_MONITOR.CLIENT_ID_TRACE_ENABLE` en el contexto de un trazado. Asimismo, puede ser utilizado en el marco de un audit.

El valor puede ser conservado a lo largo de las diferentes consultas de las páginas que utilizan la misma conexión persistente.

## Parámetros

`connection`  
Un identificador de conexión Oracle, devuelto por la función `oci_connect`, `oci_pconnect` o la función `oci_new_connect`.

`client_id`  
Cadena de caracteres elegida por el usuario de hasta 64 bytes de longitud.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Define el identificador del cliente como el usuario de la aplicación

```
<?php

// Recupera el nombre utilizado para la identificación del usuario de la aplicación
session_start();
$un = my_validate_session($_SESSION['username']);
$c = oci_connect('myschema', 'welcome', 'localhost/XE');

// Informa a Oracle sobre este usuario
oci_set_client_identifier($c, $un);

// El próximo intercambio (round-trip) hacia la base de datos validará este identificador
$s = oci_parse($c, 'select mydata from mytable');
oci_execute($s);

// ...

?>

    
```php

## Notas

> [!CAUTION]
> Algunas funciones OCI8 requieren ida y vuelta con la base de datos. Estas ida y vuelta pueden ser evitadas al usar consultas cuyo resultado es almacenado en caché.

## Véase también

`oci_set_module_name`, `oci_set_action`, `oci_set_client_info`, `oci_set_db_operation`
