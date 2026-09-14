---
title: db2_conn_errormsg
description: Devuelve el último mensaje de error de conexión junto con el valor de
  SQLCODE
source_url: https://www.php.net/manual/es/function.db2-conn-errormsg.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-conn-errormsg.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30700
---

db2_conn_errormsg

Devuelve el último mensaje de error de conexión junto con el valor de SQLCODE

## Descripción

```php
db2_conn_errormsg([resource $connection]): string
```php

`db2_conn_errormsg` devuelve un mensaje de error y el valor de SQLCODE que representa la razón por la cual el último intento de conexión a la base de datos ha fallado. Cuando `db2_connect` devuelve `false` en caso de un intento de conexión fallido, no se debe pasar ningún argumento a `db2_conn_errormsg` para obtener el mensaje de error y el valor de SQLCODE.

Si, por el contrario, la conexión fue exitosa pero se ha vuelto inválida con el tiempo, puede pasarse el argumento de conexión `connection` para obtener el mensaje de error y el valor de SQLCODE para la conexión específica.

## Parámetros

`connection`  
Un recurso de conexión asociado a la conexión que previamente fue exitosa, pero que se ha vuelto inválida con el tiempo.

## Valores devueltos

Devuelve una cadena que contiene el mensaje de error y el valor de SQLCODE resultante de un intento de conexión fallido. Devuelve una cadena vacía si no hay error asociado con el último intento de conexión.

## Ejemplos

Obtención del mensaje de error devuelto por un intento de conexión fallido

El siguiente ejemplo muestra cómo devolver un mensaje de error junto con el valor de SQLCODE después de pasar un argumento inválido a la función `db2_connect`.

```
<?php
$conn = db2_connect('mauvaisnom', 'mauvaisutilisateur', 'mauvaismotdepasse');
if (!$conn) {
    print db2_conn_errormsg();
}
?>

   
```php

El ejemplo anterior mostrará:

    [IBM][CLI Driver] SQL1013N  The database alias name
    or database name "MAUVAISNOM" could not be found.  SQLSTATE=42705
     SQLCODE=-1013

## Véase también

db2_conn_error

db2_connect

db2_stmt_error

db2_stmt_errormsg
