---
title: ibase_server_info
description: Solicita información sobre un servidor de base de datos
source_url: https://www.php.net/manual/es/function.ibase-server-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-server-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30520
---

ibase_server_info

Solicita información sobre un servidor de base de datos

## Descripción

```php
ibase_server_info(resource $service_handle, int $action): string
```php

## Parámetros

`service_handle`  
Una conexión al servidor de base de datos creada previamente.

`action`  
Una constante válida.

## Valores devueltos

Devuelve diferentes tipos dependiendo del contexto.

## Ejemplos

Ejemplo con `ibase_service_attach`

```
<?php
    // Adjuntar al servidor Firebird remoto
    if (($service = ibase_service_attach('10.1.1.254/3050', 'sysdba', 'masterkey')) != FALSE) {

        // Adjuntado con éxito.

        // Mostrar la información
        echo "Versión del servidor: " . ibase_server_info($service, IBASE_SVC_SERVER_VERSION) . "\n";
        echo "Implementación del servidor: " . ibase_server_info($service, IBASE_SVC_IMPLEMENTATION) . "\n";
        echo "Usuarios del servidor: " . print_r(ibase_server_info($service, IBASE_SVC_GET_USERS), true) . "\n";
        echo "Directorio del servidor: " . ibase_server_info($service, IBASE_SVC_GET_ENV) . "\n";
        echo "Ruta de bloqueo del servidor: " . ibase_server_info($service, IBASE_SVC_GET_ENV_LOCK) . "\n";
        echo "Ruta de la biblioteca del servidor: " . ibase_server_info($service, IBASE_SVC_GET_ENV_MSG) . "\n";
        echo "Ruta de la base de datos del usuario: " . ibase_server_info($service, IBASE_SVC_USER_DBPATH) . "\n";
        echo "Conexiones establecidas: " . print_r(ibase_server_info($service, IBASE_SVC_SVR_DB_INFO),true) . "\n";

        // Desadjuntar del servidor (desconexión)
        ibase_service_detach($service);

    }
    else {
        // Mostrar un mensaje en caso de error
        $conn_error = ibase_errmsg();
        die($conn_error);
    }
?>

   
```php

El ejemplo anterior mostrará:

    Versión del servidor: LI-V3.0.4.33054 Firebird 3.0
    Implementación del servidor: Firebird/Linux/AMD/Intel/x64
    Usuarios del servidor: Array
    (
        [0] => Array
            (
                [user_name] => SYSDBA
                [first_name] => Sql
                [middle_name] => Server
                [last_name] => Administrator
                [user_id] => 0
                [group_id] => 0
            )

    )

    Directorio del servidor: /etc/firebird/
    Ruta de bloqueo del servidor: /tmp/firebird/
    Ruta de la biblioteca del servidor: /usr/lib64/firebird/lib/
    Ruta de la base de datos del usuario: /var/lib/firebird/secdb/security3.fdb
    Conexiones establecidas: Array
    (
        [attachments] => 3
        [databases] => 2
        [0] => /srv/firebird/poss.fdb
        [1] => /srv/firebird/employees.fdb
    )
