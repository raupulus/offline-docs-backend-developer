---
title: OCICollection::trim
description: Elimina los últimos elementos de una colección Oracle
source_url: https://www.php.net/manual/es/ocicollection.trim.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocicollection/trim.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57780
---

OCICollection::trim

Elimina los últimos elementos de una colección Oracle

## Descripción

```php
public OCICollection::trim(int $num): bool
```php

Elimina los `num` últimos elementos de una colección.

## Parámetros

`num`  
El número de elementos a eliminar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Collection` ha sido renombrada a `OCICollection` para alinearse con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocicollection.size)
