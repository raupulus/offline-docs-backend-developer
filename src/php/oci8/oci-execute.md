---
title: oci_execute
description: Ejecuta un comando SQL de Oracle
source_url: https://www.php.net/manual/es/function.oci-execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_revision: 5e41012cf
order: 57270
---

oci_execute

Ejecuta un comando SQL de Oracle

## Descripción

```php
oci_execute(resource $statement, [int $mode]): bool
```php

Ejecuta una consulta `statement` previamente devuelta por la función `oci_parse`.

Tras la ejecución, las consultas como `INSERT` tendrán por omisión los datos validados (cometidos) en la base de datos. Para consultas como `SELECT`, la ejecución realiza la lógica de la consulta. Los resultados de la consulta pueden ser recuperados por PHP con funciones como `oci_fetch_array`.

Cada consulta analizada puede ser ejecutada varias veces, por lo que no es necesario analizarlas de nuevo. Esto es práctico para consultas de tipo `INSERT` cuando los datos están vinculados mediante la función `oci_bind_by_name`.

## Parámetros

`statement`  
Un identificador de consulta OCI válido.

`mode`  
Un segundo argumento opcional puede tomar una de las constantes siguientes:

| Constante | Descripción |
|----|----|
| `OCI_COMMIT_ON_SUCCESS` | Validación automática en la conexión cuando la consulta ha sido ejecutada con éxito. Este es el comportamiento por omisión. |
| `OCI_DESCRIBE_ONLY` | Hace disponibles los metadatos de la consulta a funciones como `oci_field_name` pero no crea un conjunto de resultados. Cualquier llamada a funciones de recuperación como `oci_fetch_array` fallará. |
| `OCI_NO_AUTO_COMMIT` | No valida automáticamente las modificaciones. |

Modos de ejecución

El uso del modo `OCI_NO_AUTO_COMMIT` inicia o continúa una transacción. Las transacciones son automáticamente anuladas cuando la conexión se cierra o cuando el script termina. Llame explícitamente a la función `oci_commit` para validar la transacción o a la función `oci_rollback` para anularla.

Al insertar o actualizar datos, el uso de transacciones es altamente recomendado para garantizar la consistencia relacional de los datos, así como por un significativo aumento de rendimiento.

Si el modo `OCI_NO_AUTO_COMMIT` es utilizado para todas las operaciones incluyendo consultas, y las funciones `oci_commit` y `oci_rollback` nunca son llamadas, OCI8 realizará una anulación al final del script incluso si los datos han cambiado. Para evitar este comportamiento, la mayoría de los scripts no utiliza el modo `OCI_NO_AUTO_COMMIT` para consultas o procedimientos almacenados PL/SQL. Asegúrese de la consistencia transaccional apropiada de sus aplicaciones al utilizar la función `oci_execute` con diferentes modos en el mismo script.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `oci_execute` para consultas

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');

$stid = oci_parse($conn, 'SELECT * FROM employees');
oci_execute($stid);

echo "<table border='1'>\n";
while ($row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_NULLS)) {
    echo "<tr>\n";
    foreach ($row as $item) {
        echo "    <td>" . ($item !== null ? htmlentities($item, ENT_QUOTES) : "") . "</td>\n";
    }
    echo "</tr>\n";
}
echo "</table>\n";

?>

    
```php

Ejemplo con `oci_execute` sin especificar modo

```
<?php

// Antes de la ejecución, cree la tabla:
//   CREATE TABLE MYTABLE (col1 NUMBER);

$conn = oci_connect('hr', 'welcome', 'localhost/XE');

$stid = oci_parse($conn, 'INSERT INTO mytab (col1) VALUES (123)');

oci_execute($stid); // La fila es validada y es inmediatamente visible por otros usuarios

?>

    
```php

Ejemplo con `oci_execute` y `OCI_NO_AUTO_COMMIT`

```
<?php

// Antes de la ejecución, cree la tabla:
//   CREATE TABLE MYTABLE (col1 NUMBER);

$conn = oci_connect('hr', 'welcome', 'localhost/XE');

$stid = oci_parse($conn, 'INSERT INTO mytab (col1) VALUES (:bv)');
oci_bind_by_name($stid, ':bv', $i, 10);
for ($i = 1; $i <= 5; ++$i) {
    oci_execute($stid, OCI_NO_AUTO_COMMIT);
}
oci_commit($conn);  // valida todos los nuevos valores: 1, 2, 3, 4, 5

?>

    
```php

Ejemplo con `oci_execute` y diferentes modos en el mismo script

```
<?php

// Antes de la ejecución, cree la tabla:
//   CREATE TABLE MYTABLE (col1 NUMBER);

$conn = oci_connect('hr', 'welcome', 'localhost/XE');

$stid = oci_parse($conn, 'INSERT INTO mytab (col1) VALUES (123)');
oci_execute($stid, OCI_NO_AUTO_COMMIT);  // datos no cometidos

$stid = oci_parse($conn, 'INSERT INTO mytab (col1) VALUES (456)');
oci_execute($stid);  // valida tanto los valores 123 como 456

?>

    
```php

Ejemplo con `oci_execute` y `OCI_DESCRIBE_ONLY`

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');

$stid = oci_parse($conn, 'SELECT * FROM locations');
oci_execute($s, OCI_DESCRIBE_ONLY);
for ($i = 1; $i <= oci_num_fields($stid); ++$i) {
    echo oci_field_name($stid, $i) . "<br>\n";
}

?>

    
```php

## Notas

> [!NOTE]
> Las transacciones son automáticamente anuladas cuando las conexiones se cierran, o cuando el script termina, según lo que ocurra primero. Llame explícitamente a la función `oci_commit` para validar una transacción.
>
> Cualquier llamada a la función `oci_execute` que utilice el modo `OCI_COMMIT_ON_SUCCESS` explícita o implícitamente validará todas las transacciones en curso.
>
> Todas las consultas Oracle DDL como `CREATE` o `DROP` validarán todas las transacciones en curso.

> [!NOTE]
> Debido a que la función `oci_execute` generalmente envía la consulta a la base de datos, la función `oci_execute` puede identificar errores de sintaxis de la consulta que la función `oci_parse` pudo no detectar.

## Véase también

`oci_parse`
