---
title: cubrid_fetch_array
description: Recupera una línea de resultado en forma de array asociativo, array numérico,
  o ambos
source_url: https://www.php.net/manual/es/function.cubrid-fetch-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-fetch-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8660
---

cubrid_fetch_array

Recupera una línea de resultado en forma de array asociativo, array numérico, o ambos

## Descripción

```php
cubrid_fetch_array(resource $result, [int $type]): array
```php

La función `cubrid_fetch_array` se utiliza para recuperar una sola línea desde el resultado de la consulta y devuelve un array. El cursor se mueve automáticamente a la siguiente línea una vez que el resultado ha sido recuperado.

## Parámetros

`result`  
El parámetro `Result` proviene de una llamada a la función `cubrid_execute`

`type`  
Tipo del array recuperado: CUBRID_NUM, CUBRID_ASSOC, CUBRID_BOTH. Si se necesita utilizar un objeto LOB, se puede utilizar CUBRID_LOB.

## Valores devueltos

Devuelve un array de strings correspondiente a la línea recuperada, cuando la operación tiene éxito.

`false` cuando no hay más líneas, NULL cuando ocurre un error.

El tipo del array devuelto depende del tipo que se haya definido. Utilizando CUBRID_BOTH (valor por defecto), se recuperará un array que contiene tanto índices asociativos como numéricos; se puede elegir explícitamente este tipo a través del argumento `type`. La variable `type` puede ser definida a uno de los siguientes valores:

CUBRID_NUM: Array numérico (comenzando en el índice 0)

CUBRID_ASSOC: Array asociativo

CUBRID_BOTH: Array asociativo y numérico (valor por defecto)

## Ejemplos

Ejemplo con `cubrid_fetch_array`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");
$req = cubrid_execute($conn, "SELECT name,area,seats,address FROM stadium WHERE nation_code='GRE' AND seats > 10000");

printf("%-40s %-10s %-6s %-20s\n", "name", "area", "seats", "address");
while ($row = cubrid_fetch_array($req, CUBRID_NUM)) {
    printf("%-40s %-10s %-6s %-20s\n", $row[0], $row[1], $row[2], $row[3]);
}

// Si se desea utilizar un objeto LOB, se puede utilizar
// cubrid_fetch_array($req, CUBRID_NUM | CUBRID_LOB)

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

cubrid_fetch_row

cubrid_fetch_assoc

cubrid_fetch_object
