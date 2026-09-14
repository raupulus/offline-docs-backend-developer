---
title: PDOStatement::columnCount
description: Devuelve el número de columnas en el conjunto de resultados
source_url: https://www.php.net/manual/es/pdostatement.columncount.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/columncount.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_revision: 28529d353
order: 62050
---

PDOStatement::columnCount

Devuelve el número de columnas en el conjunto de resultados

## Descripción

```php
public PDOStatement::columnCount(): int
```php

Utilice la función PDOStatement::columnCount para devolver el número de columnas en el conjunto de resultados representado por el objeto PDOStatement.

Si el objeto PDOStatement ha sido devuelto por la función PDO::query, el número de columnas es inmediatamente disponible.

Si el objeto PDOStatement ha sido devuelto por la función PDO::prepare, un conteo preciso de las columnas no estará disponible hasta que se invoque la función PDOStatement::execute.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de columnas en el conjunto de resultados representado por el objeto PDOStatement, incluso si el conjunto de resultados está vacío. Si no hay conjunto de resultados, PDOStatement::columnCount devolverá `0`.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_WARNING`.

Lanza una excepción `PDOException` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_EXCEPTION`.

## Ejemplos

Conteo de columnas

Este ejemplo demuestra cómo PDOStatement::columnCount funciona con o sin conjunto de resultados.

```
<?php
$dbh = new PDO('odbc:sample', 'db2inst1', 'ibmdb2');

$sth = $dbh->prepare("SELECT nom, couleur FROM fruit");

/* Cuenta el número de columnas en el conjunto de resultados (no existente) */
$colcount = $sth->columnCount();
print "Antes de execute(), el conjunto de resultados tenía $colcount columnas (debería ser 0)\n";

$sth->execute();

/* Cuenta el número de columnas en el conjunto de resultados */
$colcount = $sth->columnCount();
print "Después de execute(), el conjunto de resultados tiene $colcount columnas (debería ser 2)\n";

?>

    
```php

El ejemplo anterior mostrará:

    Antes de execute(), el conjunto de resultados tenía 0 columnas (debería ser 0)
    Después de execute(), el conjunto de resultados tiene 2 columnas (debería ser 2)

## Véase también

PDO::prepare, PDOStatement::execute, PDOStatement::rowCount
