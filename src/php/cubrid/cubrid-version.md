---
title: cubrid_version
description: Obtener la versión del módulo de PHP de CUBRID
source_url: https://www.php.net/manual/es/function.cubrid-version.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-version.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9530
---

cubrid_version

Obtener la versión del módulo de PHP de CUBRID

## Descripción

```php
cubrid_version(): string
```php

La función `cubrid_version` se usa para obtener la versión del módulo de PHP de CUBRID.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Información de la versión (p.ej. "8.3.1.0001").

## Ejemplos

Ejemplo de `cubrid_version`

```
<?php
printf("%-30s %s\n", "CUBRID PHP Version:", cubrid_version());

printf("\n");

$conn = cubrid_connect("localhost", 33088, "demodb", "dba");

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
    PARAM_AUTO_COMMIT              1

    Server Info:                   9.1.0.0212
    Client Info:                   9.1.0

    CUBRID Charset:                iso8859-1

## Véase también

cubrid_error_code

cubrid_error_code_facility
