---
title: db2_close
description: Cierra una conexión a base de datos
source_url: https://www.php.net/manual/es/function.db2-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_revision: 020edc73b
order: 30650
---

db2_close

Cierra una conexión a base de datos

## Descripción

```php
db2_close(resource $connection): bool
```php

Esta función cierra una conexión cliente DB2 creada con `db2_connect` y devuelve el recurso correspondiente al servidor de base de datos.

Si se tratara de cerrar una conexión de cliente DB2 persistente creada con `db2_pconnect`, la petición de cierre se ignoraría y la conexión de cliente DB2 permanecería disponible para la siguiente llamada.

## Parámetros

`connection`  
Especifica la conexión a cliente DB2 activa.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Cierre de una conexión

El siguiente ejemplo demuestra un intento de cierre exitoso de una conexión a una base de datos IBM DB2, Cloudscape, o Apache Derby.

```
<?php
$conn = db2_connect('SAMPLE', 'db2inst1', 'ibmdb2');
$rc = db2_close($conn);
if ($rc) {
    echo "Conexión cerrada con éxito.";
}
?>

   
```php

El ejemplo anterior mostrará:

    Conexión cerrada con éxito.

## Véase también

db2_connect

db2_pclose

db2_pconnect
