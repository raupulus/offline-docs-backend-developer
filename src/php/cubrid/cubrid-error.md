---
title: cubrid_error
description: Se usa para obtener el mensaje de error
source_url: https://www.php.net/manual/es/function.cubrid-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8650
---

cubrid_error

Se usa para obtener el mensaje de error

## Descripción

```php
cubrid_error([resource $connection]): string
```php

La función `cubrid_error` se usa para obtener el mensaje de error que ocurrió durante el uso de la API CUBRID. Normalmente, obtiene el mensaje de error cuando la API devuelve false como su valor de retorno.

## Parámetros

`connection`  
La conexión CUBRID

## Valores devueltos

Mensaje de error que ocurrió.

## Ejemplos

Ejemplo de `cubrid_error`

```
<?php
$con = cubrid_connect('localhost', 33000, 'demodb', 'dba', '');
$req = cubrid_execute($con, "select id, name from person");
if ($req) {
    while (list ($id, $name) = cubrid_fetch($req))
    echo $id, $name;
} else {
    echo "Código de error: ", cubrid_errno($con);
    echo "Mensaje de error: ", cubrid_error($con);
}
?>

   
```php

El ejemplo anterior mostrará:

    Código de error: -493 Mensaje de error: Syntax: Unknown class "person". select id, [name] from person

## Véase también

cubrid_errno

cubrid_error_code

cubrid_error_msg
