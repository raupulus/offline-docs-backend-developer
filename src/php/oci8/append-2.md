---
title: OCILob::append
description: Añade datos a un LOB Oracle
source_url: https://www.php.net/manual/es/ocilob.append.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocilob/append.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57800
---

OCILob::append

Añade datos a un LOB Oracle

## Descripción

```php
public OCILob::append(OCILob $from): bool
```php

Añade datos a un LOB Oracle.

La escritura en un LOB con este método fallará si la bufferización ha sido previamente activada. Se debe desactivar la bufferización antes de añadir datos. Puede ser necesario vaciar los buffers con la función [???](#ocilob.flush) antes de desactivarla.

## Parámetros

`from`  
El LOB copiado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Lob` ha sido renombrada a `OCILob` para alinearse con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocilob.flush), [???](#ocilob.setbuffering), [???](#ocilob.getbuffering)
