---
title: PDO::exec
description: Ejecuta una consulta SQL y devuelve el número de filas afectadas
source_url: https://www.php.net/manual/es/pdo.exec.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdo/exec.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_revision: 28529d353
order: 61880
---

PDO::exec

Ejecuta una consulta SQL y devuelve el número de filas afectadas

## Descripción

```php
public PDO::exec(string $statement): int
```php

PDO::exec ejecuta una consulta SQL en una sola llamada de función, devuelve el número de filas afectadas por la consulta.

PDO::exec no devuelve resultados para una consulta SELECT. Para una consulta SELECT que se necesite una sola vez en el programa, utilice en su lugar la función PDO::query. Para una consulta que se necesite varias veces, prepare un objeto PDOStatement con la función PDO::prepare y ejecute la consulta con la función PDOStatement::execute.

## Parámetros

`statement`  
La consulta a preparar y ejecutar.

Los datos contenidos en la consulta deben ser [properamente escapados](#pdo.quote).

## Valores devueltos

PDO::exec devuelve el número de filas que han sido modificadas o eliminadas por la consulta SQL ejecutada. Si ninguna fila es afectada, la función PDO::exec devolverá `0`.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

El siguiente ejemplo se basa incorrectamente en el valor devuelto por PDO::exec, donde una consulta que no afecta ninguna fila equivale a llamar a `die`:

```
<?php
$db->exec() or die(print_r($db->errorInfo(), true)); // incorrecto
?>

   
```php

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_WARNING`.

Lanza una excepción `PDOException` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_EXCEPTION`.

## Ejemplos

Ejecutar una consulta DELETE

Cuenta el número de filas eliminadas para una consulta DELETE con ninguna cláusula WHERE.

```
<?php
$dbh = new PDO('odbc:sample', 'db2inst1', 'ibmdb2');

/* Eliminación de todas las filas de la tabla FRUIT */
$count = $dbh->exec("DELETE FROM fruit");

/* Devuelve el número de filas eliminadas */
print "Eliminación de $count filas.\n";
?>

    
```php

El ejemplo anterior mostrará:

    Eliminación de 1 filas.

## Véase también

PDO::prepare, PDO::query, PDOStatement::execute
