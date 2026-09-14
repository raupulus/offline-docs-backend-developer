---
title: ibase_service_detach
description: Desconexión del gestor de servicio
source_url: https://www.php.net/manual/es/function.ibase-service-detach.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-service-detach.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30540
---

ibase_service_detach

Desconexión del gestor de servicio

## Descripción

```php
ibase_service_detach(resource $service_handle): bool
```php

## Parámetros

`service_handle`  
Una conexión al servidor de base de datos creada previamente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `ibase_service_detach`

```
<?php
    // Adjuntar al servidor Firebird remoto por una dirección IP
    if (($service = ibase_service_attach('10.1.1.199', 'sysdba', 'masterkey')) != FALSE) {

        // Adjuntado con éxito.
        // Recuperar la versión del servidor (algo como 'LI-V3.0.4.33054 Firebird 3.0')
        $server_version  = ibase_server_info($service, IBASE_SVC_SERVER_VERSION);

        // Recuperar la implementación del servidor (algo como 'Firebird/Linux/AMD/Intel/x64')
        $server_implementation = ibase_server_info($service, IBASE_SVC_IMPLEMENTATION);

        // Desconectar del servidor (desconexión)
        if(ibase_service_detach($service) == FALSE) {
            echo "Error en la desconexión del servicio.";
        }
        else {
            echo "Desconexión del servicio realizada con éxito.";
        }

    }
    else {
        // Mostrar un mensaje en caso de error
        $conn_error = ibase_errmsg();
        die($conn_error);
    }

?>

   
```php
