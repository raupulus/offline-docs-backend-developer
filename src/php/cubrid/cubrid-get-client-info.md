---
title: cubrid_get_client_info
description: Devolver la versión de la biblioteca cliente
source_url: https://www.php.net/manual/es/function.cubrid-get-client-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-get-client-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9080
---

cubrid_get_client_info

Devolver la versión de la biblioteca cliente

## Descripción

```php
cubrid_get_client_info(): string
```php

Esta función devuelve una cadena que representa la versión de la biblioteca cliente.

## Parámetros

## Valores devueltos

Una cadena que representa la versión de la biblioteca cliente; en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `cubrid_get_client_info`

```
<?php
printf("%-30s %s\n", "CUBRID PHP Version:", cubrid_version());

printf("\n");

$conn = cubrid_connect("localhost", 33088, "demodb");

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

printf("%-30s %s\n", "Server Info:", $server_info);
printf("%-30s %s\n", "Client Info:", $client_info);

printf("\n");

$charset = cubrid_get_charset($conn);

printf("%-30s %s\n", "CUBRID Charset:", $charset);

cubrid_disconnect($conn);

?>

   
```php

El ejemplo anterior mostrará:

    CUBRID PHP Version:            9.1.0.0001

    PARAM_ISOLATION_LEVEL          3
    LOCK_TIMEOUT                   -1
    MAX_STRING_LENGTH              1073741823
    PARAM_AUTO_COMMIT              0

    Server Info:                   9.1.0.0212
    Client Info:                   9.1.0

    CUBRID Charset:                iso8859-1
