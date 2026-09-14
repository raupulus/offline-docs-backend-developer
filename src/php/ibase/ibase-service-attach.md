---
title: ibase_service_attach
description: Conexión al gestor de servicio
source_url: https://www.php.net/manual/es/function.ibase-service-attach.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-service-attach.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30530
---

ibase_service_attach

Conexión al gestor de servicio

## Descripción

```php
ibase_service_attach(string $host, string $dba_username, string $dba_password): resource
```php

## Parámetros

`host`  
El nombre o la dirección IP del host de la base de datos. El puerto puede ser definido añadiendo '/' y el número del puerto. Si no se especifica ningún puerto, se utilizará el puerto 3050.

`dba_username`  
El nombre de cualquier usuario válido.

`dba_password`  
La contraseña del usuario.

## Valores devueltos

Devuelve un identificador de enlace Interbase / Firebird en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `ibase_service_attach`

```
<?php
    // Conectarse al servidor Firebird remoto por una dirección IP
    if (($service = ibase_service_attach('10.1.1.199', 'sysdba', 'masterkey')) != FALSE) {

        // Conectado con éxito.
        // Obtener la versión del servidor (algo como 'LI-V3.0.4.33054 Firebird 3.0')
        $server_version  = ibase_server_info($service, IBASE_SVC_SERVER_VERSION);

        // Obtener la implementación del servidor (algo como 'Firebird/Linux/AMD/Intel/x64')
        $server_implementation = ibase_server_info($service, IBASE_SVC_IMPLEMENTATION);

        // Desconectarse del servidor
        ibase_service_detach($service);

        // Mostrar la información
        echo "Versión del servidor: " . $server_version . "<br/>";
        echo "Implementación del servidor: " . $server_implementation;
    }
    else {
        // Mostrar un mensaje en caso de error
        $conn_error = ibase_errmsg();
        die($conn_error);
    }

?>

   
```php

Ejemplo de`ibase_service_attach` utilizando la sintaxis `hostname/port`

```
<?php
    // Conectarse al servidor Firebird remoto por nombre. Utiliza el puerto 3050.
    if (($service = ibase_service_attach('FB-SRV-01.contoso.local/3050', 'sysdba', 'masterkey')) != FALSE) {

        // Conectado con éxito.
        // Obtener la versión del servidor (algo como 'LI-V3.0.4.33054 Firebird 3.0')
        $server_version  = ibase_server_info($service, IBASE_SVC_SERVER_VERSION);

        // Obtener la implementación del servidor (algo como 'Firebird/Linux/AMD/Intel/x64')
        $server_implementation = ibase_server_info($service, IBASE_SVC_IMPLEMENTATION);

        // Desconectarse del servidor
        ibase_service_detach($service);

        // Mostrar la información
        echo "Versión del servidor: " . $server_version . "<br/>";
        echo "Implementación del servidor: " . $server_implementation;
    }
    else {
        // Mostrar un mensaje en caso de error
        $conn_error = ibase_errmsg();
        die($conn_error);
    }

?>

   
```php

## Véase también

ibase_service_detach
