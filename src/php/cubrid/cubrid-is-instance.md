---
title: cubrid_is_instance
description: Comprobar si existe la instancia apuntada por OID
source_url: https://www.php.net/manual/es/function.cubrid-is-instance.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-is-instance.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_revision: 22492de2e
order: 9140
---

cubrid_is_instance

Comprobar si existe la instancia apuntada por OID

## Descripción

```php
cubrid_is_instance(resource $conn_identifier, string $oid): int
```php

La función `cubrid_is_instance` se usa para comprobar si existe la instancia apuntada por el `oid` dado o no.

## Parámetros

`conn_identifier`  
Identificador de conexión.

`oid`  
OID de la instancia que se quiere comprobar su existencia.

## Valores devueltos

1, si tal instancia existe;

0, si tal instancia no existe;

-1, en caso de error

## Ejemplos

Ejemplo de `cubrid_is_instance`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");

$sql = <<<EOD
SELECT host_year, medal, game_date
FROM game
WHERE athlete_code IN
    (SELECT code FROM athlete WHERE name='Thorpe Ian');
EOD;

$req = cubrid_execute($conn, $sql, CUBRID_INCLUDE_OID);
$oid = cubrid_current_oid($req);

$res = cubrid_is_instance ($conn, $oid);
if ($res == 1) {
    echo "La instancia a puntada por $oid existe.\n";
} else if ($res == 0){
    echo "La instancia a puntada por $oid no existe.\n";
} else {
    echo "error\n";
}

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    La instancia apuntada por @0|0|0 no existe.

## Véase también

cubrid_drop

cubrid_get_class_name
