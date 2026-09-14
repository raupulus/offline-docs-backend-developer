---
title: oci_close
description: Cierra una conexión Oracle
source_url: https://www.php.net/manual/es/function.oci-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: 5e41012cf
order: 57220
---

oci_close

Cierra una conexión Oracle

## Descripción

```php
oci_close(resource $connection): bool
```php

Cierra una conexión `connection` Oracle. La conexión será cerrada si ninguna recurso la utiliza y si fue creada con la función `oci_connect` o la función `oci_new_connect`.

Se recomienda cerrar las conexiones que ya no sean necesarias, liberando así más recursos para otros usuarios.

## Parámetros

`connection`  
Un identificador de conexión Oracle, retornado por la función `oci_connect`, `oci_pconnect`, o `oci_new_connect`.

## Valores devueltos

Retorna `null` cuando [oci8.old_oci_close_semantics](#ini.oci8.old-oci-close-semantics) está activado, `true` en caso contrario.

## Ejemplos

Cierre de una conexión

Los recursos asociados con una conexión deben ser cerrados para asegurar a la base de datos subyacente el fin de las operaciones y así liberar los recursos.

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT * FROM departments');
$r = oci_execute($stid);
oci_fetch_all($stid, $res);
var_dump($res);

// Liberación del identificador de consulta al cerrar la conexión
oci_free_statement($stid);
oci_close($conn);

?>

   
```php

Las conexiones a la base de datos son cerradas cuando las referencias lo son

El identificador interno que cuenta las conexiones debe valer cero para poder cerrar la conexión.

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT * FROM departments');  // esto incrementa el contador interno $conn
oci_execute($stid);
oci_fetch_all($stid, $res);
var_dump($res);

oci_close($conn);

// $conn ya no es utilizable en el script pero la conexión subyacente a
// la base de datos sigue abierta mientras $stid no sea liberada.
var_dump($conn);  // muestra NULL

// Mientras PHP espera, el hecho de consultar la vista V$SESSION de Oracle
// en un terminal mostrará que un usuario sigue conectado.
sleep(10);

// Cuando $stid es liberada, la conexión a la base de datos será físicamente cerrada
oci_free_statement($stid);

// Mientras PHP espera, el hecho de consultar la vista V$SESSION de Oracle
// en un terminal mostrará que el usuario se ha desconectado.
sleep(10);

?>

   
```php

Cierre de una conexión abierta más de una vez

Cuando se reutilizan identificadores de base de datos, todas las conexiones deben ser cerradas antes de que la conexión subyacente a la base de datos lo sea realmente.

```
<?php

$conn1 = oci_connect('hr', 'welcome', 'localhost/XE');

// La utilización de los mismos identificadores reutiliza la misma conexión subyacente a la base de datos.
// Todas las modificaciones no confirmadas realizadas sobre $conn1 serán visibles sobre $conn2.
$conn2 = oci_connect('hr', 'welcome', 'localhost/XE');

// Mientras PHP espera, el hecho de consultar la vista V$SESSION de Oracle
// en un terminal mostrará que un solo usuario está conectado.
sleep(10);

oci_close($conn1); // no cierra la conexión subyacente a la base de datos
var_dump($conn1);  // muestra NULL ya que la variable $conn1 ya no es utilizable
var_dump($conn2);  // muestra que $conn2 sigue siendo un recurso de conexión válido

?>

   
```php

Las conexiones son cerradas cuando las variables salen del contexto

Cuando todas las variables que referencian una conexión salen del contexto y son liberadas por PHP, se produce un rollback (si es necesario) y la conexión subyacente a la base de datos es cerrada.

```
<?php

function myfunc() {
    $conn = oci_connect('hr', 'hrpwd', 'localhost/XE');
    if (!$conn) {
        $e = oci_error();
        trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
    }

    $stid = oci_parse($conn, 'UPDATE mytab SET id = 100');
    oci_execute($stid, OCI_NO_AUTO_COMMIT);
    return "Finished";
}

$r = myfunc();
// En este momento, se produce un rollback y la conexión subyacente a la base de datos es cerrada.

print $r;  // muestra el valor de retorno de la función "Finished"

?>

   
```php

## Notas

> [!NOTE]
> Las variables que dependen del identificador de conexión, como los identificadores de consulta retornados por la función `oci_parse`, deben ser liberadas antes de intentar cerrar la conexión subyacente a la base de datos.

> [!NOTE]
> La función `oci_close` no cierra las conexiones subyacentes a la base de datos creadas por la función `oci_pconnect`.

## Véase también

`oci_connect`, `oci_free_statement`
