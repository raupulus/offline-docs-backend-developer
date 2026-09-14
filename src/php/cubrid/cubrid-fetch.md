---
title: cubrid_fetch
description: Obtener la siguiente fila de un conjunto de resultados
source_url: https://www.php.net/manual/es/function.cubrid-fetch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-fetch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_revision: 22492de2e
order: 9030
---

cubrid_fetch

Obtener la siguiente fila de un conjunto de resultados

## Descripción

```php
cubrid_fetch(resource $result, [int $type]): mixed
```php

La función `cubrid_fetch` se usa para obtener una única fila del resultado de la consulta. El cursor se mueve automáticamente a la siguiente columna después de obtener el resultado.

## Parámetros

`result`  
`result` proviene de una llamada a la función `cubrid_execute`.

`type`  
Tipo de array del resultado obtenido: CUBRID_NUM, CUBRID_ASSOC, CUBRID_BOTH, CUBRID_OBJECT. Si se operan con objetos lob, se puede usar CUBRID_LOB.

## Valores devueltos

Un array de resultados u objeto, cuando el proceso tiene éxito.

`false`, cuando no existen más filas; NULL, cuando el proceso no tiene éxito.

El resultado se puede recibir como array o como objeto, por lo que se puede decidir qué tipo de datos usar estableciendo el argumento `type`. La variable `type` se puede establecer a uno de los siguientes valores:

CUBRID_NUM : Array numérico (basado en 0)

CUBRID_ASSOC : Array asociativo

CUBRID_BOTH : Array numérico y asociativo (predeterminado)

CUBRID_OBJECT : Objeto que tiene el nombre del atributo como el nombre de la columna del resultado de la consulta

Cuando se omite el argumento `type`, el resultado será recibido usando la opción predeterminada CUBRID_BOTH. Cuando se quiere recibir el resultado de la consulta como objeto, el nombre de la columna del resultado debe obedecer las reglas de nombres de los identificadores de PHP. Por ejemplo, un nombre de columna como "count(\*)" no puede ser recibido como objeto.

## Ejemplos

Ejemplo de `cubrid_fetch`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");
$solicitud = cubrid_execute($conexión, "SELECT * FROM stadium WHERE nation_code='GRE' AND seats > 10000");

printf("%-40s %-10s %-6s %-20s\n", "name", "area", "seats", "address");
while ($fila = cubrid_fetch($solicitud)) {
    printf("%-40s %-10s %-6s %-20s\n",
        $fila["name"], $fila["area"], $fila["seats"], $fila["address"]);
}

// si se operan con objetos lob, se puede usar cubrid_fetch($solicitud, CUBRID_LOB)

cubrid_close_request($solicitud);

cubrid_disconnect($conexión);
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

cubrid_fetch_array

cubrid_fetch_row

cubrid_fetch_assoc

cubrid_fetch_object
