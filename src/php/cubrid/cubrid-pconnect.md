---
title: cubrid_pconnect
description: Establece una conexión persistente con un servidor CUBRID
source_url: https://www.php.net/manual/es/function.cubrid-pconnect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-pconnect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 184764a63
order: 9400
---

cubrid_pconnect

Establece una conexión persistente con un servidor CUBRID

## Descripción

```php
cubrid_pconnect(string $host, int $port, string $dbname, [string $userid], [string $passwd]): resource
```php

Establece una conexión persistente con un servidor CUBRID.

`cubrid_pconnect` funciona de manera similar a `cubrid_connect` con dos diferencias principales.

En primer lugar, al establecer la conexión, la función intentará primero encontrar un enlace (persistente) ya abierto con el mismo nombre de host, en el mismo puerto, utilizando la misma base de datos dbname y el mismo userid. Si se encuentra un enlace de este tipo, su identificador será devuelto en lugar de abrir una nueva conexión.

En segundo lugar, la conexión con el servidor CUBRID no se cerrará cuando finalice el script. En su lugar, el enlace permanecerá abierto para su uso futuro (`cubrid_close` o `cubrid_disconnect` no cerrarán los enlaces establecidos con `cubrid_pconnect`).

Este tipo de enlace se denominaba anteriormente 'persistente'.

## Parámetros

`host`  
Nombre del host o dirección IP del servidor CUBRID CAS.

`port`  
Número de puerto del servidor CUBRID CAS (BROKER_PORT configurado en \$CUBRID/conf/cubrid_broker.conf).

`dbname`  
Nombre de la base de datos.

`userid`  
Nombre de usuario para la base de datos.

`passwd`  
Contraseña asociada al nombre de usuario.

## Valores devueltos

Identificador de conexión en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_pconnect`

```
<?php
printf("%-30s %s\n", "Versión de CUBRID PHP:", cubrid_version());

printf("\n");

$conn = cubrid_pconnect("localhost", 33000, "demodb", "dba");

if (!$conn) {
    die('Error de conexión ('. cubrid_error_code() .')' . cubrid_error_msg());
}

$db_params = cubrid_get_db_parameter($conn);

while (list($param_name, $param_value) = each($db_params)) {
    printf("%-30s %s\n", $param_name, $param_value);
}

printf("\n");

$server_info = cubrid_get_server_info($conn);
$client_info = cubrid_get_client_info();

printf("%-30s %s\n", "Información del servidor:", $server_info);
printf("%-30s %s\n", "Información del cliente:", $client_info);

printf("\n");

$charset = cubrid_get_charset($conn);

printf("%-30s %s\n", "Juego de caracteres CUBRID:", $charset);

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    Versión de CUBRID PHP:            9.1.0.0001

    PARAM_ISOLATION_LEVEL          3
    LOCK_TIMEOUT                   -1
    MAX_STRING_LENGTH              1073741823
    PARAM_AUTO_COMMIT              1

    Información del servidor:      9.1.0.0212
    Información del cliente:       9.1.0

    Juego de caracteres CUBRID:     iso8859-1

## Véase también

cubrid_connect

cubrid_connect_with_url

cubrid_pconnect_with_url

cubrid_disconnect

cubrid_close
