---
title: cubrid_result
description: Devuelve el valor de un campo específico de una fila específica
source_url: https://www.php.net/manual/es/function.cubrid-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_revision: 22492de2e
order: 8830
---

cubrid_result

Devuelve el valor de un campo específico de una fila específica

## Descripción

```php
cubrid_result(resource $result, int $row, [mixed $field]): string
```php

Esta función devuelve el valor de un campo específico de una fila específica de un conjunto de resultados.

## Parámetros

`result`  
`result` proviene de una llamada a la función `cubrid_execute`

`row`  
El número de fila del resultado que está siendo traído. Los números de fila comienzan en 0.

`field`  
El nombre o índice del campo dado por `field` que está siendo obtenido. Puede ser el índice del campo, el nombre del campo, o la tabla del campo punto nombre del campo (nombretabla.nombrecampo). Si el nombre de la columna ha sido apodado ('select foo as bar from...'), use el alias en vez del nombre de la columna. Si no está definido se trae el primer campo.

## Valores devueltos

El valor de un campo específico, en caso de éxito (NULL si el valor es nulo).

`false` en caso de error.

## Ejemplos

Ejemplo de `cubrid_result`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");

$req = cubrid_execute($conn, "SELECT * FROM code");

$result = cubrid_result($req, 0);
var_dump($result);

$result = cubrid_result($req, 0, 1);
var_dump($result);

$result = cubrid_result($req, 5, "f_name");
var_dump($result);

cubrid_close_request($req);
cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    string(1) "X"
    string(5) "Mixed"
    string(4) "Gold"
