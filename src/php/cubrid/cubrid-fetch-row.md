---
title: cubrid_fetch_row
description: Devuelve un array numérico con los valores de la fila actual
source_url: https://www.php.net/manual/es/function.cubrid-fetch-row.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-fetch-row.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8710
---

cubrid_fetch_row

Devuelve un array numérico con los valores de la fila actual

## Descripción

```php
cubrid_fetch_row(resource $result, [int $type]): array
```php

Esta función devuelve un array numérico con los valores de la fila actual del conjunto de resultados, comenzando en 0 y desplaza el puntero interno de datos.

## Parámetros

`result`  
El argumento `result` proviene de una llamada a la función `cubrid_execute`

`type`  
El tipo solo puede ser CUBRID_LOB; este argumento será utilizado únicamente cuando se necesite utilizar un objeto lob.

## Valores devueltos

Un array numérico en caso de éxito.

`false` cuando no hay más filas, NULL si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_fetch_row`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");
$req = cubrid_execute($conn, "SELECT name,area,seats,address FROM stadium WHERE nation_code='GRE' AND seats > 10000");

printf("%-40s %-10s %-6s %-20s\n", "name", "area", "seats", "address");
while ($row = cubrid_fetch_row($req)) {
    printf("%-40s %-10s %-6s %-20s\n", $row[0], $row[1], $row[2], $row[3]);
}

// Si se desea utilizar un objeto lob, se puede utilizar
// cubrid_fetch_row($req, CUBRID_LOB)

cubrid_close_request($req);

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    name                                     area       seats  address
    Panathinaiko Stadium                     86300.00   50000  Athens, Greece
    Olympic Stadium                          54700.00   13000  Athens, Greece
    Olympic Indoor Hall                      34100.00   18800  Athens, Greece
    Olympic Hall                             52400.00   21000  Athens, Greece
    Olympic Aquatic Centre                   42500.00   11500  Athens, Greece
    Markopoulo Olympic Equestrian Centre     64000.00   15000  Markopoulo, Athens, Greece
    Faliro Coastal Zone Olympic Complex      34650.00   12171  Faliro, Athens, Greece
    Athens Olympic Stadium                   120400.00  71030  Maroussi, Athens, Greece
    Ano Liossia                              34000.00   12000  Ano Liosia, Athens, Greece

## Véase también

cubrid_execute

cubrid_fetch

cubrid_fetch_array

cubrid_fetch_assoc

cubrid_fetch_object
