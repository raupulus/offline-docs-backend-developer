---
title: OCILob::erase
description: Elimina una parte de un LOB Oracle
source_url: https://www.php.net/manual/es/ocilob.erase.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocilob/erase.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57830
---

OCILob::erase

Elimina una parte de un LOB Oracle

## Descripción

```php
public OCILob::erase([int $offset], [int $length]): int
```php

Elimina la parte del LOB Oracle comenzando en el desplazamiento `offset`, con una longitud de `length` bytes.

Para los BLOB, la eliminación significa que el valor existente del LOB es reemplazado por el carácter 0. Para los CLOB, se utilizan espacios.

## Parámetros

`offset`  

`length`  

## Valores devueltos

Devuelve el número de caracteres/bytes eliminados o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | `offset` y `length` ahora son nulos. |
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Lob` ha sido renombrada a `OCILob` para alinearse con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocilob.truncate)
