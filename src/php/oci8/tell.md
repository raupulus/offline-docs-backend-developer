---
title: OCILob::tell
description: Devuelve la posición actual del puntero de LOB
source_url: https://www.php.net/manual/es/ocilob.tell.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocilob/tell.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57970
---

OCILob::tell

Devuelve la posición actual del puntero de LOB

## Descripción

```php
public OCILob::tell(): int
```php

Devuelve la posición actual del puntero de LOB.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la posición actual del puntero interno del LOB, o bien `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Lob` ha sido renombrada a `OCILob` para alinearse con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocilob.rewind), [???](#ocilob.size), [???](#ocilob.eof)
