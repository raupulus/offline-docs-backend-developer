---
title: OCILob::free
description: Destruye un puntero de LOB Oracle
source_url: https://www.php.net/manual/es/ocilob.free.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocilob/free.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57860
---

OCILob::free

Destruye un puntero de LOB Oracle

## Descripción

```php
public OCILob::free(): bool
```php

Libera los recursos asociados con el recurso, previamente asignado con `oci_new_descriptor`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Lob` ha sido renombrada a `OCILob` para alinearse con los estándares de nomenclatura de PHP. |
