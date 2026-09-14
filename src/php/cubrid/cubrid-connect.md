---
title: cubrid_connect
description: Abrir una conexión al servidor CUBRID
source_url: https://www.php.net/manual/es/function.cubrid-connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_revision: 22492de2e
order: 8950
---

cubrid_connect

Abrir una conexión al servidor CUBRID

## Descripción

```php
cubrid_connect(string $host, int $port, string $dbname, [string $userid], [string $passwd], [bool $new_link]): resource
```php

La función `cubrid_connect` se usa para establecer el entorno para la conexión al servidor usando la dirección del servidor, número de puerto, nombre de la base de datos, nombre de usuario, y contraseña. Si no se dan el nombre de usuario y la contraseña, se realizará la conexión "PUBLIC" por defecto.

## Parámetros

`host`  
Nombre del host o dirección IP del servidor CAS de CUBRID.

`port`  
Número de puerto del servidor CAS de CUBRID (BROKER_PORT configurado en \$CUBRID/conf/cubrid_broker.conf).

`dbname`  
Nombre de la base de datos.

`userid`  
Nombre de usuario para la base de datos. Si no se da, el valor por omisión es "public".

`passwd`  
Contraseña del usuario. Si no se da, el valor por omisión es "".

`new_link`  
Si se hace una segunda llamada a `cubrid_connect` con los mismos argumentos, no se establecerá una nueva conexión, en su lugar, se devolverá el identificador de conexión de la conexión ya abierta. El parámetro `new_link` modifica este comportamiento y hace que `cubrid_connect` abra siempre una nueva conexión, incluso si `cubrid_connect` fue llamada antes con los mismos parámetros.

## Valores devueltos

El identificador de conexión, cuando el proceso tiene éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `cubrid_connect`

```
<?php
printf("%-30s %s\n", "CUBRID PHP Version:", cubrid_version());

printf("\n");

$conn = cubrid_connect("localhost", 33000, "demodb", "dba");

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

printf("%-30s %s\n", "Información del Servidor:", $server_info);
printf("%-30s %s\n", "Información del Cliente:", $client_info);

printf("\n");

$charset = cubrid_get_charset($conn);

printf("%-30s %s\n", "Conjunto de carac.:", $charset);

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    CUBRID PHP Version:            9.1.0.0001

    PARAM_ISOLATION_LEVEL          3
    LOCK_TIMEOUT                   -1
    MAX_STRING_LENGTH              1073741823
    PARAM_AUTO_COMMIT              0

    Información del Servidor:      9.1.0.0212
    Información del Cliente:       9.1.0

    Conjunto de carac. de CUBRID:  iso8859-1

## Véase también

cubrid_pconnect

cubrid_connect_with_url

cubrid_pconnect_with_url

cubrid_disconnect

cubrid_close
