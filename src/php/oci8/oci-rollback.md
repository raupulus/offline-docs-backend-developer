---
title: oci_rollback
description: Anula las transacciones Oracle en curso
source_url: https://www.php.net/manual/es/function.oci-rollback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-rollback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: 5e41012cf
order: 57570
---

oci_rollback

Anula las transacciones Oracle en curso

## Descripción

```php
oci_rollback(resource $connection): bool
```php

Anula todas las modificaciones no confirmadas para una conexión `connection` Oracle y finaliza la transacción actual. Todos los bloqueos serán liberados asimismo. Todos los puntos de guardado Oracle (`SAVEPOINTS`) serán eliminados.

Una transacción comienza cuando la primera consulta SQL que modifica datos es ejecutada con la función `oci_execute` utilizando el flag `OCI_NO_AUTO_COMMIT`. Las modificaciones siguientes realizadas por otras consultas se convierten en parte de la misma transacción. Las modificaciones realizadas durante una transacción son temporales hasta que la transacción sea confirmada o anulada. Los demás usuarios de la base de datos no verán estas modificaciones hasta la confirmación de la transacción.

Al insertar o actualizar datos, el uso de transacciones es altamente recomendado para garantizar la consistencia relacional de los datos, pero también por razones de rendimiento.

## Parámetros

`connection`  
Un identificador de conexión Oracle, devuelto por la función `oci_connect`, `oci_pconnect` o `oci_new_connect`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `oci_rollback`

```
<?php

// Inserción en múltiples tablas, luego, anulación de las modificaciones si ocurren errores

$conn = oci_connect('hr', 'welcome', 'localhost/XE');

$stid = oci_parse($conn, "INSERT INTO mysalary (id, name) VALUES (1, 'Chris')");

// El flag OCI_NO_AUTO_COMMIT indica a Oracle no confirmar la inserción inmediatamente.
$r = oci_execute($stid, OCI_NO_AUTO_COMMIT);
if (!$r) {
    $e = oci_error($stid);
    trigger_error(htmlentities($e['message']), E_USER_ERROR);
}

$stid = oci_parse($conn, 'INSERT INTO myschedule (startday) VALUES (12)');
$r = oci_execute($stid, OCI_NO_AUTO_COMMIT);
if (!$r) {
    $e = oci_error($stid);
    oci_rollback($conn);  // Anulación de las modificaciones en las 2 tablas
    trigger_error(htmlentities($e['message']), E_USER_ERROR);
}

// Confirmación de las modificaciones en las 2 tablas
$r = oci_commit($conn);
if (!$r) {
    $e = oci_error($conn);
    trigger_error(htmlentities($e['message']), E_USER_ERROR);
}

?>

    
```php

Ejemplo de retorno a un punto de guardado (`SAVEPOINT`)

```
<?php
$stid = oci_parse($conn, 'UPDATE mytab SET id = 1111');
oci_execute($stid, OCI_NO_AUTO_COMMIT);

// creación del punto de guardado
$stid = oci_parse($conn, 'SAVEPOINT mysavepoint');
oci_execute($stid, OCI_NO_AUTO_COMMIT);

$stid = oci_parse($conn, 'UPDATE mytab SET id = 2222');
oci_execute($stid, OCI_NO_AUTO_COMMIT);

// utiliza una consulta SQL explícita para realizar el retorno al punto de guardado
$stid = oci_parse($conn, 'ROLLBACK TO SAVEPOINT mysavepoint');
oci_execute($stid, OCI_NO_AUTO_COMMIT);

oci_commit($conn);  // mytab tiene ahora un id de 1111
?>

    
```php

## Notas

> [!NOTE]
> Las transacciones son anuladas automáticamente al cerrar la conexión, o cuando el script finaliza, cualquiera de los dos que ocurra primero. Debe llamarse explícitamente a la función `oci_commit` para confirmar la conexión.
>
> Todas las llamadas a la función `oci_execute` que utilizan el modo `OCI_COMMIT_ON_SUCCESS`, ya sea por defecto o de forma explícita, confirmarán todas las transacciones pendientes.
>
> Todas las consultas Oracle como `CREATE` o `DROP` confirmarán asimismo, automáticamente, todas las transacciones pendientes.

## Véase también

`oci_commit`, `oci_execute`
