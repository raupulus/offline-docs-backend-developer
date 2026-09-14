---
title: cubrid_lob2_tell64
description: Recupera la posición del cursor en el objeto LOB
source_url: https://www.php.net/manual/es/function.cubrid-lob2-tell64.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-lob2-tell64.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9310
---

cubrid_lob2_tell64

Recupera la posición del cursor en el objeto LOB

## Descripción

```php
cubrid_lob2_tell64(resource $lob_identifier): string
```php

La función `cubrid_lob2_tell64` se utiliza para recuperar la posición del cursor en el objeto LOB. Si la longitud del objeto LOB es mayor que la capacidad de almacenamiento de un entero, puede utilizarse esta función y devolverá la información en forma de string.

## Parámetros

`lob_identifier`  
Un identificador LOB, recuperado desde la función `cubrid_lob2_new` o desde el conjunto de resultados.

## Valores devueltos

Devuelve la posición del cursor en el objeto LOB, en forma de string en caso de éxito, o `false` si ocurre un error.

## Véase también

cubrid_lob2_read

cubrid_lob2_write

cubrid_lob2_seek

cubrid_lob2_seek64

cubrid_lob2_tell

cubrid_lob2_size

cubrid_lob2_size64
