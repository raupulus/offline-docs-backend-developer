---
title: cubrid_lob2_tell
description: Recupera la posición del cursor en un objeto LOB
source_url: https://www.php.net/manual/es/function.cubrid-lob2-tell.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-lob2-tell.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9300
---

cubrid_lob2_tell

Recupera la posición del cursor en un objeto LOB

## Descripción

```php
cubrid_lob2_tell(resource $lob_identifier): int
```php

La función `cubrid_lob2_tell` se utiliza para recuperar la posición del cursor en el objeto LOB.

## Parámetros

`lob_identifier`  
Un identificador LOB, recuperado desde la función `cubrid_lob2_new` o desde el juego de resultados.

## Valores devueltos

Devuelve la posición del cursor en el objeto LOB en caso de éxito, o `false` si ocurre un error.

## Véase también

cubrid_lob2_read

cubrid_lob2_write

cubrid_lob2_seek

cubrid_lob2_seek64

cubrid_lob2_tell64

cubrid_lob2_size

cubrid_lob2_size64
