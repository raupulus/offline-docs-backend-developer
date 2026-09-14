---
title: PDOStatement::fetchColumn
description: Devuelve una columna de la siguiente fila de un conjunto de resultados
source_url: https://www.php.net/manual/es/pdostatement.fetchcolumn.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/fetchcolumn.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 28529d353
order: 62120
---

PDOStatement::fetchColumn

Devuelve una columna de la siguiente fila de un conjunto de resultados

## Descripción

```php
public PDOStatement::fetchColumn([int $column]): mixed
```php

Devuelve una columna de la siguiente fila de un conjunto de resultados o `false` si no hay más filas.

> [!NOTE]
> PDOStatement::fetchColumn no debe usarse para recuperar columnas que contengan valores booleanos, ya que no es posible distinguir un valor `false` de un retorno sin filas para recuperar. Utilice PDOStatement::fetch en su lugar.

## Parámetros

`column`  
Número de la columna que se desea recuperar de la fila (comenzando en 0). Si no se proporciona ningún valor, PDOStatement::fetchColumn recuperará la primera columna.

## Valores devueltos

PDOStatement::fetchColumn devuelve una columna de la siguiente fila de un conjunto de resultados o `false` si no hay más filas.

> [!WARNING]
> No existe solución para recuperar otra columna de la misma fila si se utiliza la función PDOStatement::fetchColumn para obtener los datos.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_WARNING`.

Lanza una excepción `PDOException` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_EXCEPTION`.

## Ejemplos

Devuelve la primera columna de la siguiente fila

```
<?php
$sth = $dbh->prepare("SELECT nom, couleur FROM fruit");
$sth->execute();

/* Recupera la primera columna de la primera fila de un conjunto de resultados */
print "Recupera la primera columna de la primera fila de un conjunto de resultados :\n";
$result = $sth->fetchColumn();
print "nom=$result\n");

print "Recupera la segunda columna de la segunda fila de un conjunto de resultados :\n";
$result = $sth->fetchColumn(1);
print "couleur=$result\n";
?>

    
```php

El ejemplo anterior mostrará:

    Recupera la primera columna de la primera fila de un conjunto de resultados :
    nom=lemon
    Recupera la segunda columna de la segunda fila de un conjunto de resultados :
    couleur=orange

## Véase también

PDO::query, PDOStatement::fetch, PDOStatement::fetchAll, PDO::prepare, PDOStatement::setFetchMode
