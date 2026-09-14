---
title: db2_fetch_both
description: Devuelve un array, indexado por nombre de columna y posición, que representa
  una fila del conjunto de resultados
source_url: https://www.php.net/manual/es/function.db2-fetch-both.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-fetch-both.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: true
translation_revision: 020edc73b
order: 30780
---

db2_fetch_both

Devuelve un array, indexado por nombre de columna y posición, que representa una fila del conjunto de resultados

## Descripción

```php
db2_fetch_both(resource $stmt, [int $row_number]): array
```php

Devuelve un array, indexado por nombre de columna y posición, que representa una fila del conjunto de resultados. Tenga en cuenta que la fila devuelta por `db2_fetch_both` requiere más memoria que los arrays simplemente indexados devueltos por `db2_fetch_assoc` o `db2_fetch_array`.

## Parámetros

`stmt`  
Un recurso `stmt` válido que contiene el conjunto de resultados.

`row_number`  
Solicita una fila específica indexada numéricamente que comienza con el valor 1 en el conjunto de resultados. Al proporcionar este argumento, se generará una alerta PHP si el conjunto de resultados utiliza un cursor de avance solo.

## Valores devueltos

Devuelve un array asociativo con los valores de las columnas indexados por el nombre de las columnas y el número de las columnas comenzando por 0. El array representa la siguiente fila o la fila solicitada del conjunto de resultados. Devuelve `false` si no hay una fila disponible en el conjunto de resultados o si la fila solicitada por `row_number` no existe en el conjunto de resultados.

## Ejemplos

Iteración con un cursor de avance solo

Si se llama a `db2_fetch_both` sin el número de una fila específica, se recuperará automáticamente la siguiente fila del conjunto de resultados. El siguiente ejemplo accede a las columnas devueltas en el array mediante el método de nombres de columna y por índice numérico.

```
<?php

$sql = "SELECT id, nom, race, poids FROM animaux ORDER BY race";
$stmt = db2_prepare($conn, $sql);
$result = db2_execute($stmt);

while ($row = db2_fetch_both($stmt)) {
    printf ("%-5d %-16s %-32s %10s\n",
        $row['ID'], $row[0], $row['RACE'], $row[3]);
}
?>

    
```php

El ejemplo anterior mostrará:

    0     Pook             chat                                   3.20
    5     Rickety Ride     chèvre                                 9.70
    2     Smarty           cheval                               350.00

Recuperación de filas específicas con `db2_fetch_both` a partir de un cursor flotante

Si su conjunto de resultados utiliza un cursor flotante, puede llamar a la función `db2_fetch_assoc` con un número de fila específico. El siguiente ejemplo recupera cada fila par en el conjunto de resultados, comenzando con la segunda fila.

```
<?php

$sql = "SELECT id, nom, race, poids FROM animaux ORDER BY race";
$result = db2_exec($stmt, $sql, array('cursor' => DB2_SCROLLABLE));

$i=2;
while ($row = db2_fetch_both($result, $i)) {
    printf ("%-5d %-16s %-32s %10s\n",
        $row[0], $row['NOM'], $row[2], $row['POIDS']);
    $i = $i + 2;
}
?>

    
```php

El ejemplo anterior mostrará:

    0     Pook             chat                                   3.20
    5     Rickety Ride     chèvre                                 9.70
    2     Smarty           cheval                               350.00

## Véase también

db2_fetch_array

db2_fetch_assoc

db2_fetch_object

db2_fetch_row

db2_result
