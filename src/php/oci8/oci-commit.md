---
title: oci_commit
description: Valida las transacciones Oracle en curso
source_url: https://www.php.net/manual/es/function.oci-commit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-commit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_revision: 5e41012cf
order: 57230
---

oci_commit

Valida las transacciones Oracle en curso

## Descripción

```php
oci_commit(resource $connection): bool
```php

Valida todas las transacciones en curso en la conexión Oracle `connection`. Una validación hace permanentes todas las modificaciones, liberando todos los bloqueos.

Una transacción comienza cuando se ejecuta la primera consulta SQL que modifica datos con la función `oci_execute` utilizando el flag `OCI_NO_AUTO_COMMIT`. Las modificaciones siguientes realizadas por otras consultas forman parte de la misma transacción. Los datos modificados por una transacción son temporales hasta que la transacción sea validada o revertida. Otros usuarios de la base de datos no verán estas modificaciones hasta que la transacción sea validada.

Al insertar o actualizar datos, el uso de transacciones es recomendado para garantizar la consistencia relacional de los datos, así como para mejorar el rendimiento.

## Parámetros

`connection`  
Un identificador de conexión Oracle, devuelto por la función `oci_connect`, `oci_pconnect`, o `oci_new_connect`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `oci_commit`

```
<?php

// Inserción en múltiples tablas, con cancelación de las modificaciones si ocurren errores

$conn = oci_connect('hr', 'welcome', 'localhost/XE');

$stid = oci_parse($conn, "INSERT INTO mysalary (id, name) VALUES (1, 'Chris')");

// El flag OCI_NO_AUTO_COMMIT indica a Oracle que no valide las inserciones automáticamente.
$r = oci_execute($stid, OCI_NO_AUTO_COMMIT);
if (!$r) {
    $e = oci_error($stid);
    trigger_error(htmlentities($e['message']), E_USER_ERROR);
}

$stid = oci_parse($conn, 'INSERT INTO myschedule (startday) VALUES (12)');
$r = oci_execute($stid, OCI_NO_AUTO_COMMIT);
if (!$r) {
    $e = oci_error($stid);
    oci_rollback($conn);  // Cancelación de las modificaciones en las 2 tablas
    trigger_error(htmlentities($e['message']), E_USER_ERROR);
}

// Valida las modificaciones en las 2 tablas
$r = oci_commit($conn);
if (!$r) {
    $e = oci_error($conn);
    trigger_error(htmlentities($e['message']), E_USER_ERROR);
}

?>

    
```php

## Notas

> [!NOTE]
> Las transacciones son automáticamente revertidas al cerrar la conexión, o cuando el script finaliza, cualquiera de los dos que ocurra primero. Debe llamarse explícitamente a la función `oci_commit` para validar la transacción.
>
> Cada llamada a la función `oci_execute` que utiliza el modo `OCI_COMMIT_ON_SUCCESS` explícitamente o por omisión, validará todas las transacciones no validadas hasta ese punto.
>
> Todas las consultas Oracle como `CREATE` o `DROP` también validarán todas las transacciones no validadas.

## Véase también

`oci_execute`, `oci_rollback`
