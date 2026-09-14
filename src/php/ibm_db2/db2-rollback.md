---
title: db2_rollback
description: Cancelar una transacción
source_url: https://www.php.net/manual/es/function.db2-rollback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-rollback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 31040
---

db2_rollback

Cancelar una transacción

## Descripción

```php
db2_rollback(resource $connection): bool
```php

Cancela una transacción en progreso en el recurso de conexión especificado y comienza una nueva transacción. Comunmente las aplicaciones de PHP confirman las transacciones de manera automática por lo que la función `db2_rollback` no tendría efecto a menos que este modo haya sido desactivado para este recurso.

## Parámetros

`connection`  
Un recurso de conexión válido devuelto por `db2_connect` o `db2_pconnect`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Cancelando una sentencia DELETE

En el siguiente ejemplo se cuenta el número de filas en una tabla, se cancelan las confirmaciones automáticas en la conexión, se eliminan todas las filas de la tabla y devuelve el total de `0` para confirmar que las filas se han borrado. Cuando se llama a `db2_rollback` y se devuelve el total actualizado de filas en la tabla para demostrar que el número es igual al original (antes de ejecutar la sentancia DELETE). Esto demuestra que la cancelación de la transacción fue correcto.

```
<?php
$conn = db2_connect($database, $user, $password);

if ($conn) {
    $stmt = db2_exec($conn, "SELECT count(*) FROM animals");
    $res = db2_fetch_array( $stmt );
    echo $res[0] . "\n";

    // Desactivar AUTOCOMMIT
    db2_autocommit($conn, DB2_AUTOCOMMIT_OFF);

    // Eliminar todas las filas de ANIMALS
    db2_exec($conn, "DELETE FROM animals");

    $stmt = db2_exec($conn, "SELECT count(*) FROM animals");
    $res = db2_fetch_array( $stmt );
    echo $res[0] . "\n";

    // Deshacer la sentencia DELETE
    db2_rollback( $conn );

    $stmt = db2_exec( $conn, "SELECT count(*) FROM animals" );
    $res = db2_fetch_array( $stmt );
    echo $res[0] . "\n";
    db2_close($conn);
}
?>

   
```php

El ejemplo anterior mostrará:

    7
    0
    7

## Véase también

db2_autocommit

db2_commit
