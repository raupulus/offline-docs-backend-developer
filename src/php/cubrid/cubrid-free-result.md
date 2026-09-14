---
title: cubrid_free_result
description: Liberar la memoria ocupada por los datos del resultado
source_url: https://www.php.net/manual/es/function.cubrid-free-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-free-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_revision: 22492de2e
order: 9040
---

cubrid_free_result

Liberar la memoria ocupada por los datos del resultado

## Descripción

```php
cubrid_free_result(resource $req_identifier): bool
```php

Esta función libera la memoria ocupada por los datos del resultado. Devuelve `true` en caso de éxito o `false` en caso de error. Observe que sólo se puede liberar el buffer de obtención del cliente, y si se quiere liberar toda la memoria, use la función `cubrid_close_request`.

## Parámetros

`req_identifier`  
Éste es el identificador de solicitud.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `cubrid_free_result`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");

$req = cubrid_execute($conn, "SELECT * FROM history WHERE host_year=2004 ORDER BY event_code");
$row = cubrid_fetch_assoc($req);
var_dump($row);

cubrid_free_result($req);
cubrid_close_request($req);
cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    array(5) {
      ["event_code"]=>
      string(5) "20005"
      ["athlete"]=>
      string(12) "Hayes Joanna"
      ["host_year"]=>
      string(4) "2004"
      ["score"]=>
      string(5) "12.37"
      ["unit"]=>
      string(4) "time"
    }
