---
title: OCILob::export
description: Exporta un LOB Oracle a un fichero
source_url: https://www.php.net/manual/es/ocilob.export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocilob/export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: deb6ee360
order: 57840
---

OCILob::export

Exporta un LOB Oracle a un fichero

## Descripción

```php
public OCILob::export(string $filename, [int $offset], [int $length]): bool
```php

Exporta un LOB Oracle a un fichero.

## Parámetros

`filename`  
La ruta de acceso al fichero.

`offset`  
Indica la posición a partir de la cual debe comenzar la exportación.

`length`  
Indica el tamaño de los datos a exportar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | `offset` y `length` ahora son nulos. |
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Lob` ha sido renombrada a `OCILob` para alinearse con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocilob.import)
