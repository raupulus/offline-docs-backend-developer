---
title: db2_conn_error
description: Devuelve un string que contiene el valor de SQLSTATE devuelto por el
  último intento de conexión
source_url: https://www.php.net/manual/es/function.db2-conn-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-conn-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30690
---

db2_conn_error

Devuelve un string que contiene el valor de SQLSTATE devuelto por el último intento de conexión

## Descripción

```php
db2_conn_error([resource $connection]): string
```php

`db2_conn_error` devuelve el valor de SQLSTATE que representa la razón por la cual el último intento de conexión a la base de datos ha fallado. Cuando `db2_connect` devuelve `false` en caso de un intento de conexión fallido, no se debe pasar ningún argumento a `db2_conn_error` para obtener el valor de SQLSTATE.

Si por el contrario la conexión fue exitosa pero se ha vuelto inválida con el tiempo, se puede pasar el argumento de conexión `connection` para obtener el valor de SQLSTATE para la conexión específica.

Para entender los valores de SQLSTATE, se puede ingresar el siguiente comando en el procesador de línea de comandos de DB2: `db2 '? sqlstate-value'`. También se puede llamar a la función `db2_conn_errormsg` para obtener un mensaje de error explícito junto con el valor de SQLCODE asociado.

## Parámetros

`connection`  
Un recurso de conexión asociado a la conexión que previamente fue exitosa, pero que se ha vuelto inválida con el tiempo.

## Valores devueltos

Devuelve el valor de SQLSTATE resultante de un intento de conexión fallido. Devuelve un string vacío si no hay error asociado con el último intento de conexión.

## Ejemplos

Obtención del valor de SQLSTATE para un intento de conexión fallido

El siguiente ejemplo muestra cómo devolver un valor de SQLSTATE después de pasar un argumento inválido a la función `db2_connect`.

```
<?php
$conn = db2_connect('mauvaisnom', 'mauvaisutilisateur', 'mauvaismotdepasse');
if (!$conn) {
    print "Valor de SQLSTATE: " . db2_conn_error();
}
?>

   
```php

El ejemplo anterior mostrará:

    Valor de SQLSTATE: 08001

## Véase también

db2_conn_errormsg

db2_connect

db2_stmt_error

db2_stmt_errormsg
