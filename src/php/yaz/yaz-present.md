---
title: yaz_present
description: Se prepara para la recuperación (Z39.50 presente)
source_url: https://www.php.net/manual/es/function.yaz-present.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-present.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_revision: 96c9d88ba
order: 107880
---

yaz_present

Se prepara para la recuperación (Z39.50 presente)

## Descripción

```php
yaz_present(resource $id): bool
```php

Esta función se prepara para la recuperación de archivos después de una búsqueda exitosa.

La función `yaz_range` debe ser llamado antes de esta función para especificar el rango de registros a ser recuperados.

## Parámetros

`id`  
El recurso de conexión devuelto por `yaz_connect`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
