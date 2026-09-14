---
title: cubrid_affected_rows
description: Devolver el número de filas afectadas por la última sentencia SQL
source_url: https://www.php.net/manual/es/function.cubrid-affected-rows.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-affected-rows.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: ee1ce6a0e
order: 8590
---

cubrid_affected_rows

Devolver el número de filas afectadas por la última sentencia SQL

## Descripción

```php
cubrid_affected_rows([resource $conn_identifier]): int
```php

```php
cubrid_affected_rows([resource $req_identifier]): int
```

La función `cubrid_affected_rows` se usa para obtener el número de filas afectadas por la última sentencia SQL (INSERT, DELETE, UPDATE).

## Parámetros

`conn_identifier`  
La conexión CUBRID. Si no se especifica el identificador de conexión, se asume el último enlace abierto por `cubrid_connect`.

`req_identifier`  
Identificador de petición. Podría ser devuelto desde `cubrid_prepare` o `cubrid_execute`. Si el identificador de petición no se especifica, se asume el último identificador solicitado por `cubrid_prepare` o `cubrid_execute`.

## Valores devueltos

El número de filas afectadas por la sentencia SQL, cuando el proceso tiene éxito.

-1, cuando la sentencia SQL no es INSERT, DELETE o UPDATE.

`false`, cuando el identificador de solicitud no está especificado, y no existe una última petición.

## Ejemplos

Ejemplo de `cubrid_affected_rows`

```php
<?php
$conn = cubrid_connect('localhost', 33000, 'demodb', 'dba', '');
cubrid_execute($conn, "DROP TABLE IF EXISTS cubrid_test");
cubrid_execute($conn, "CREATE TABLE cubrid_test (d varchar)");
$sql_stmt = "INSERT INTO cubrid_test(d) VALUES('php-test')";
$req = cubrid_prepare($conn, $sql_stmt);

for ($i = 0; $i < 10; $i++) {
    cubrid_execute($req);
}
cubrid_commit($conn);

$req = cubrid_execute($conn, "DELETE FROM cubrid_test WHERE d='php-test'", CUBRID_ASYNC);
var_dump(cubrid_affected_rows());
var_dump(cubrid_affected_rows($conn));
var_dump(cubrid_affected_rows($req));

cubrid_disconnect($conn);

print "¡Hecho!";
?>

   
```

El ejemplo anterior mostrará:

    int(10)
    int(10)
    int(10)
    done!

## Véase también

cubrid_execute
