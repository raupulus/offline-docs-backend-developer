---
title: cubrid_get_db_parameter
description: Devuelve los parámetros de la base de datos CUBRID
source_url: https://www.php.net/manual/es/function.cubrid-get-db-parameter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-get-db-parameter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_revision: 22492de2e
order: 9090
---

cubrid_get_db_parameter

Devuelve los parámetros de la base de datos CUBRID

## Descripción

```php
cubrid_get_db_parameter(resource $conn_identifier): array
```php

Esta función devuelve los parámetros de la base de datos CUBRID , o `false` si ocurre un error. Devuelve un array asociativo con los valores de los siguientes parámetros:

PARAM_ISOLATION_LEVEL

PARAM_LOCK_TIMEOUT

PARAM_MAX_STRING_LENGTH

PARAM_AUTO_COMMIT

| Parámetro | Descripción |
|----|----|
| PARAM_ISOLATION_LEVEL | El nivel de aislamiento de la transacción. |
| LOCK_TIMEOUT | CUBRID proporciona la característica de bloqueo de tiempo de espera, que establece el tiempo de espera (en segundos) para el bloqueo hasta que el ajuste de bloqueo de transacción se permite. El valor predeterminado del parámetro lock_timeout_in_secs es -1, lo que significa que la aplicación cliente esperará indefinidamente hasta que se permita el bloqueo de transacción. |
| PARAM_AUTO_COMMIT | En CUBRID PHP, el modo de auto consigna es desabilitado por omisión por el gestor de transacciones. Puede establecerse usando la función `cubrid_set_autocommit`. |

Parámetros de la base de datos

La siguiente tabla muestra los niveles de aislamiento desde 1 hasta 6. Consiste en esquema de tabla (fila) y nivel de aislamiento:

| Nombre | Descripción |
|----|----|
| SERIALIZABLE (6) | En este nivel de aislamiento, los problemas concernientes a la concurrencia (p.ej. lectura basura, lectura no repetible, lectura fantasma, etc.) no ocurren. |
| CLASE DE LECTURA REPETIBLE con INSTANCIAS DE LECTURA REPETIBLE (5) | Otra transacción T2 no puede actualizar el esquema de una tabla A mientras la transacción T1 está viendo la tabla A. La transacción T1 puede experimentar lectura fantasma para el registro R que fue insertado por otra transacción T2 cuando está obtenido repetidamente un registro especificado. |
| CLASE DE LECTURA REPETIBLE con INSTANCIAS CONSIGNADAS DE LECTURA (o ESTABILIDAD DE CURSOR) (4) | Otra transacción T2 no puede actualizar el esquema de una tabla A mientras la transacción T1 está viendo la tabla A. La transacción T1 puede experimentar lectura R (lectura no repetible) que fue actualizada y consignada por otra transacción T2 cuando está obteniendo repetidamente el registro R. |
| CLASE DE LECTURA REPETIBLE con INSTANCIAS NO CONSIGNADAS DE LECTURA (3) | Nivel de aislamiento predeterminado. Otra transacción T2 no puede actualizar el esquema de la tabla A mientras la transacción T1 está viendo la tabla A. La transacción T1 puede experimentar lectura R' (lectura basura) para el registro que fue actualizado pero no consignado por otra transacción T2. |
| CLASE CONSIGNADA DE LECTURA con INSTANCIAS CONSIGNADAS DE LECTURA (2) | La transacción T1 puede experimentar lectura A' (lectura no repetible) para la tabla que fue actualizada y consignada por otra transacción T2 mientras que está viendo la tabla A repetidamente. La transacción T1 puede experimentar lectura R' (lectura no repetible) para el registro que fue actualizado y consignado por otra transacción T2 mientras se está obteniendo el registro R repetidamente. |
| CLASE CONSIGNADA DE LECTURA con INSTANCIAS NO CONSIGNADAS DE LECTURA (1) | La transacción T1 puede experimentar lectura A' (lectura no repetible) para la tabla que fue actualizada y consignada por otra transacción T2 mientras que se ve repetidamente la tabla A. La transacción T1 puede experimentar lectura R' (lectura basura) para el registro qeu fue actualizado pero no consignado por otra transacción T2. |

Niveles de Aislamiento Soportados por CUBRID

## Parámetros

`conn_identifier`  
La conexión CUBRID. Si el identificador de conexión no se especifica, se asume el último enlace abierto por `cubrid_connect`.

## Valores devueltos

Una matriz asociativa con los parámetros de la base de datos CUBRID; en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Cambia LOCK_TIMEOUT a PARAM_LOCK_TIMEOUT, y MAX_STRING_LENGTH a PARAM_MAX_STRING_LENGTH en el resultado. |

## Ejemplos

Ejemplo de `cubrid_get_db_parameter`

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
    PARAM_AUTO_COMMIT              1

    Server Info:                   9.1.0.0212
    Client Info:                   9.1.0

    CUBRID Charset:                iso8859-1

## Véase también

cubrid_set_db_parameter

cubrid_get_autocommit
