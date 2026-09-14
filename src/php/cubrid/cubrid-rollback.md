---
title: cubrid_rollback
description: Anula una transacción
source_url: https://www.php.net/manual/es/function.cubrid-rollback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-rollback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9430
---

cubrid_rollback

Anula una transacción

## Descripción

```php
cubrid_rollback(resource $conn_identifier): bool
```php

La función `cubrid_rollback` anula la transacción en curso señalada por el argumento `conn_identifier`.

La conexión al servidor se cierra después de la llamada a la función `cubrid_rollback`. Sin embargo, el gestor de conexión permanece activo.

## Parámetros

`conn_identifier`  
Identificador de conexión.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_rollback`

```
<?php
$conn = cubrid_connect("127.0.0.1", 33000, "demodb", "dba");
cubrid_set_autocommit($conn,false);

@cubrid_execute($conn, "DROP TABLE publishers");

$sql = <<<EOD
CREATE TABLE publishers(
pub_id CHAR(3),
pub_name VARCHAR(20),
city VARCHAR(15),
state CHAR(2),
country VARCHAR(15)
)
EOD;

if (!cubrid_execute($conn, $sql)) {
    printf("Error facility: %d\nError code: %d\nError msg: %s\n", cubrid_error_code_facility(), cubrid_error_code(), cubrid_error_msg());

    cubrid_disconnect($conn);
    exit;
}

$req = cubrid_prepare($conn, "INSERT INTO publishers VALUES(?, ?, ?, ?, ?)");

$id_list = array("P01", "P02", "P03", "P04");
$name_list = array("Abatis Publishers", "Core Dump Books", "Schadenfreude Press", "Tenterhooks Press");
$city_list = array("New York", "San Francisco", "Hamburg", "Berkeley");
$state_list = array("NY", "CA", NULL, "CA");
$country_list = array("USA", "USA", "Germany", "USA");

for ($i = 0, $size = count($id_list); $i < $size; $i++) {
    cubrid_bind($req, 1, $id_list[$i]);
    cubrid_bind($req, 2, $name_list[$i]);
    cubrid_bind($req, 3, $city_list[$i]);
    cubrid_bind($req, 4, $state_list[$i]);
    cubrid_bind($req, 5, $country_list[$i]);

    if (!($ret = cubrid_execute($req))) {
        break;
    }
}

if (!$ret) {
    cubrid_rollback($conn);
} else {
    cubrid_commit($conn);

    $req = cubrid_execute($conn, "SELECT * FROM publishers");
    while ($result = cubrid_fetch_assoc($req)) {
        printf("%-3s %-20s %-15s %-3s %-15s\n",
            $result["pub_id"], $result["pub_name"], $result["city"], $result["state"], $result["country"]);
    }
}

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    P01 Abatis Publishers    New York        NY  USA
    P02 Core Dump Books      San Francisco   CA  USA
    P03 Schadenfreude Press  Hamburg             Germany
    P04 Tenterhooks Press    Berkeley        CA  USA

## Véase también

cubrid_commit

cubrid_disconnect
