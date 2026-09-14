---
title: db2_result
description: Devuelve un valor de una columna de una fila de un conjunto de resultados
source_url: https://www.php.net/manual/es/function.db2-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 31030
---

db2_result

Devuelve un valor de una columna de una fila de un conjunto de resultados

## Descripción

```php
db2_result(resource $stmt, int $column): mixed
```php

Utilice `db2_result` para devolver un valor de una columna específica en la fila actual de un conjunto de resultados. Debe llamarse a `db2_fetch_row` antes de llamar a `db2_result` para almacenar los valores apuntados del conjunto de resultados.

## Parámetros

`stmt`  
Un recurso `stmt` válido.

`column`  
Un array de enteros que comienza con el índice 0 que apunta a los campos del conjunto de resultados o una cadena que representa el nombre de la columna.

## Valores devueltos

Devuelve el valor del campo solicitado si el campo existe en el conjunto de resultados. Devuelve `null` si el campo no existe y genera una alerta PHP.

## Ejemplos

Ejemplo de uso de `db2_result`

El siguiente ejemplo demuestra cómo iterar a través de un conjunto de resultados con la función `db2_fetch_row` y recuperar las columnas del conjunto de resultados con `db2_result`.

```
<?php
$sql = 'SELECT nom, race FROM animales WHERE poids < ?';
$stmt = db2_prepare($conn, $sql);
db2_execute($stmt, array(10));
while (db2_fetch_row($stmt)) {
    $nom = db2_result($stmt, 0);
    $race = db2_result($stmt, 'RACE');
    print "$nom $race";
}
?>

   
```php

El ejemplo anterior mostrará:

    chat Pook
    cyprin doré Bubbles
    perruche Gizmo
    chèvre Rickety Ride

## Véase también

db2_fetch_array

db2_fetch_assoc

db2_fetch_both

db2_fetch_object

db2_fetch_row
