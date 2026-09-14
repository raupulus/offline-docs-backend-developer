---
title: PDOStatement::nextRowset
description: Avance al siguiente conjunto de resultados de un manejador de conjuntos
  de resultados múltiples
source_url: https://www.php.net/manual/es/pdostatement.nextrowset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/nextrowset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 661e6858a
order: 62170
---

PDOStatement::nextRowset

Avance al siguiente conjunto de resultados de un manejador de conjuntos de resultados múltiples

## Descripción

```php
public PDOStatement::nextRowset(): bool
```php

Algunas bases de datos soportan procedimientos almacenados que retornan más de un conjunto de resultados (también conocido como juegos de resultados). PDOStatement::nextRowset permite acceder al segundo y siguientes conjuntos de resultados asociados con el objeto PDOStatement. Cada conjunto de resultados tiene diferentes juegos de columnas desde el conjunto de resultados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Recuperación de múltiples conjuntos de resultados retornados por un procedimiento almacenado

El siguiente ejemplo muestra cómo llamar a un procedimiento almacenado, `MULTIPLE_ROWSETS`, que retorna tres conjuntos de resultados. Un ciclo [do-while](#control-structures.do.while) es utilizado para recorrer el método PDOStatement::nextRowset, que retorna `false` y termina el ciclo cuando no hay más conjuntos de resultados disponibles.

```
<?php
$sql = 'CALL multiple_rowsets()';
$stmt = $conn->query($sql);
$i = 1;
do {
    $rowset = $stmt->fetchAll(PDO::FETCH_NUM);
    if ($rowset) {
        printResultSet($rowset, $i);
    }
    $i++;
} while ($stmt->nextRowset());

function printResultSet(&$rowset, $i) {
    print "Conjunto de resultados $i:\n";
    foreach ($rowset as $row) {
        foreach ($row as $col) {
            print $col . "\t";
        }
        print "\n";
    }
    print "\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    Conjunto de resultados 1:
    apple    red
    banana   yellow

    Conjunto de resultados 2:
    orange   orange    150
    banana   yellow    175

    Conjunto de resultados 3:
    lime     green
    apple    red
    banana   yellow

## Véase también

PDOStatement::columnCount, PDOStatement::execute, PDOStatement::getColumnMeta, PDO::query
