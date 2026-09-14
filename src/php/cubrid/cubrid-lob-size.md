---
title: cubrid_lob_size
description: Recupera el tamaño de los datos BLOB/CLOB
source_url: https://www.php.net/manual/es/function.cubrid-lob-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-lob-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9190
---

cubrid_lob_size

Recupera el tamaño de los datos BLOB/CLOB

## Descripción

```php
cubrid_lob_size(resource $lob_identifier): string
```php

La función `cubrid_lob_size` se utiliza para recuperar el tamaño de los datos BLOB/CLOB.

## Parámetros

`lob_identifier`  
Identificador LOB.

## Valores devueltos

Una cadena representando el tamaño de los datos LOB, cuando la operación ha tenido éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | El tipo del valor devuelto ha cambiado. Antes era un entero, ahora es una cadena de caracteres. |

## Ejemplos

Ejemplo con `cubrid_lob_size`

```
<?php
$lobs = cubrid_lob_get($con, "SELECT doc_content FROM doc WHERE doc_id=5");
echo "Tamaño de la documentación :".cubrid_lob_size($lobs[0]);
cubrid_lob_export($conn, $lobs[0], "doc_5.txt");
cubrid_lob_close($lobs);
?>

   
```php

## Véase también

cubrid_lob_get

cubrid_lob_close

cubrid_lob_export

cubrid_lob_send
