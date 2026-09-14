---
title: cubrid_errno
description: Devuelve el valor numérico del mensaje de error de la operación de CUBRID
  previa
source_url: https://www.php.net/manual/es/function.cubrid-errno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-errno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8640
---

cubrid_errno

Devuelve el valor numérico del mensaje de error de la operación de CUBRID previa

## Descripción

```php
cubrid_errno([resource $conn_identifier]): int
```php

Devuelve el número de error de la última función CUBRID.

La función `cubrid_errno` se usa para obtener el código de error que ocurrió durante la ejecución de la API. Normalmente, obtiene el error cuando la API devuelve false como su valor de retorno.

## Parámetros

`conn_identifier`  
El identificador de conexión de CUBRID. Si el identificador de conexión no se especifica, se asume la última conexión abierta por `cubrid_connect`.

## Valores devueltos

Devuelve el número de error de la última función CUBRID, o `0` (cero) si no ocurrio ningún error.

## Ejemplos

Ejemplo de `cubrid_errno`

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

    Código de error: -493 Mensaje de error:: Syntax: Unknown class "person". select id, [name] from person

## Véase también

cubrid_error

cubrid_error_code

cubrid_error_msg
