---
title: db2_fetch_row
description: Modifica el puntero del conjunto de resultados a la siguiente línea o
  a la línea solicitada
source_url: https://www.php.net/manual/es/function.db2-fetch-row.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-fetch-row.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 30800
---

db2_fetch_row

Modifica el puntero del conjunto de resultados a la siguiente línea o a la línea solicitada

## Descripción

```php
db2_fetch_row(resource $stmt, [int $row_number]): bool
```php

Utilice `db2_fetch_row` para iterar a través de un conjunto de resultados o para apuntar a una línea específica de un conjunto de resultados si se ha solicitado un cursor flotante.

Para obtener campos individuales del conjunto de resultados, llame a la función `db2_result`.

En lugar de llamar a las funciones `db2_fetch_row` y `db2_result`, la mayoría de las aplicaciones van a llamar a la función `db2_fetch_assoc`, `db2_fetch_both` o `db2_fetch_array` para avanzar el puntero en el conjunto de resultados y devolver una línea completa como array.

## Parámetros

`stmt`  
Un recurso `stmt` válido que contiene el conjunto de resultados.

`row_number`  
Con cursores flotantes, puede solicitar un número de línea específico del conjunto de resultados. Los números de líneas comienzan con el índice 1

## Valores devueltos

Devuelve `true` si la línea solicitada existe en el conjunto de resultados. Devuelve `false` si la línea solicitada no existe en el conjunto de resultados.

## Ejemplos

Iterar a través de un conjunto de resultados

El siguiente ejemplo demuestra cómo iterar a través de un conjunto de resultados con la función `db2_fetch_row` y recuperar las columnas del conjunto de resultados con `db2_result`.

```
<?php
$sql = 'SELECT nom, race FROM animales WHERE peso < ?';
$stmt = db2_prepare($conn, $sql);
db2_execute($stmt, array(10));
while (db2_fetch_row($stmt)) {
    $nom = db2_result($stmt, 0);
    $race = db2_result($stmt, 1);
    print "$nom $race";
}
?>

    
```php

El ejemplo anterior mostrará:

    gato Pook
    carpa dorada Bubbles
    periquito Gizmo
    cabra Rickety Ride

Alternativas recomendadas i5/OS para db2_fetch_row/db2_result

En i5/OS, se recomienda que utilice `db2_fetch_both`, `db2_fetch_array` o `db2_fetch_object` en lugar de `db2_fetch_row`/`db2_result`. En general `db2_fetch_row`/`db2_result` tiene más problemas con tipos de columna variados en la traducción de `EBCDIC` a `ASCII`, incluyendo posible truncamiento en aplicaciones `DBCS`. También podría encontrar una mejor performance utilizando `db2_fetch_both`, `db2_fetch_array` y `db2_fetch_object` en lugar de `db2_fetch_row`/`db2_result`.

```
<?php
  $conn = db2_connect("","","");
  $sql = 'SELECT SPECIFIC_SCHEMA, SPECIFIC_NAME, ROUTINE_SCHEMA, ROUTINE_NAME, ROUTINE_TYPE, ROUTINE_CREATED, ROUTINE_BODY, IN_PARMS, OUT_PARMS, INOUT_PARMS, PARAMETER_STYLE, EXTERNAL_NAME, EXTERNAL_LANGUAGE FROM QSYS2.SYSROUTINES FETCH FIRST 2 ROWS ONLY';
  $stmt = db2_exec($conn, $sql, array('cursor' => DB2_SCROLLABLE));
  while ($row = db2_fetch_both($stmt)){
    echo "<br>db2_fetch_both {$row['SPECIFIC_NAME']} {$row['ROUTINE_CREATED']} {$row[5]}";
  }
  $stmt = db2_exec($conn, $sql, array('cursor' => DB2_SCROLLABLE));
  while ($row = db2_fetch_array($stmt)){
    echo "<br>db2_fetch_array {$row[1]}  {$row[5]}";
  }
  $stmt = db2_exec($conn, $sql, array('cursor' => DB2_SCROLLABLE));
  while ($row = db2_fetch_object($stmt)){
    echo "<br>db2_fetch_object {$row->SPECIFIC_NAME} {$row->ROUTINE_CREATED}";
  }
  db2_close($conn);
?>

    
```php

El ejemplo anterior mostrará:

    db2_fetch_both MATCH_ANIMAL 2006-08-25-17.10.23.775000 2006-08-25-17.10.23.775000
    db2_fetch_both MULTIRESULTS 2006-10-17-10.11.05.308000 2006-10-17-10.11.05.308000
    db2_fetch_array MATCH_ANIMAL 2006-08-25-17.10.23.775000
    db2_fetch_array MULTIRESULTS 2006-10-17-10.11.05.308000
    db2_fetch_object MATCH_ANIMAL 2006-08-25-17.10.23.775000
    db2_fetch_object MULTIRESULTS 2006-10-17-10.11.05.308000

## Véase también

db2_fetch_array

db2_fetch_assoc

db2_fetch_both

db2_fetch_object

db2_result
