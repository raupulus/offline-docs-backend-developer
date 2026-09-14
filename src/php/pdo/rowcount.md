---
title: PDOStatement::rowCount
description: Devuelve el número de filas afectadas por la última llamada a la función
  PDOStatement::execute()
source_url: https://www.php.net/manual/es/pdostatement.rowcount.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/rowcount.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: a5950d8ae
order: 62180
---

PDOStatement::rowCount

Devuelve el número de filas afectadas por la última llamada a la función PDOStatement::execute()

## Descripción

```php
public PDOStatement::rowCount(): int
```php

PDOStatement::rowCount devuelve el número de filas afectadas por la última consulta DELETE, INSERT o UPDATE ejecutada por el objeto `PDOStatement` correspondiente.

Si la última consulta SQL ejecutada por el objeto `PDOStatement` asociado es una consulta de tipo SELECT, algunas bases de datos devolverán el número de filas devueltas por dicha consulta. No obstante, este comportamiento no está garantizado para todas las bases de datos y no debería ser utilizado para aplicaciones portables.

> [!NOTE]
> Este método siempre devuelve "0" (cero) con el controlador PostgreSQL, cuando el atributo de declaración `PDO::ATTR_CURSOR` está definido como `PDO::CURSOR_SCROLL`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de filas.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_WARNING`.

Lanza una excepción `PDOException` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_EXCEPTION`.

## Ejemplos

Devuelve el número de filas eliminadas

PDOStatement::rowCount devuelve el número de filas afectadas por una consulta DELETE, INSERT, o UPDATE.

```
<?php
/* Eliminación de todas las filas de la tabla FRUIT */
$del = $dbh->prepare('DELETE FROM fruit');
$del->execute();

/* Devuelve el número de filas eliminadas */
print "Devuelve el número de filas eliminadas :\n";
$count = $del->rowCount();
print "Eliminación de $count filas.\n";
?>

    
```php

Resultado del ejemplo anterior es similar a:

     
    Devuelve el número de filas eliminadas :
    Eliminación de 9 filas.

Conteo de filas devueltas por una consulta SELECT

Para la mayoría de las bases de datos, PDOStatement::rowCount no devuelve el número de filas afectadas por una consulta SELECT. En su lugar, utilice PDO::query para hacer una consulta SELECT COUNT(\*), luego utilice PDOStatement::fetchColumn para recuperar el número de filas correspondientes.

```
  
<?php
$sql = "SELECT COUNT(*) FROM fruit WHERE calories > 100";
$res = $conn->query($sql);
$count = $res->fetchColumn();

print "Hay " .  $count . " fila(s) correspondiente(s).";
?>

     
```php

Resultado del ejemplo anterior es similar a:

    Hay  2 fila(s) correspondiente(s).

## Véase también

PDOStatement::columnCount, PDOStatement::fetchColumn, PDO::query
