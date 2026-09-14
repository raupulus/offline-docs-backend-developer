---
title: OCILob::read
description: Lee una parte de un LOB Oracle
source_url: https://www.php.net/manual/es/ocilob.read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/ocilob/read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: 665c1d6da
order: 57900
---

OCILob::read

Lee una parte de un LOB Oracle

## Descripción

```php
public OCILob::read(int $length): string
```php

Lee `length` bytes (BLOB) o caracteres (CLOB) a partir de la posición actual del LOB.

La lectura se detiene cuando `length` bytes han sido leídos para un BLOB, cuando `length` caracteres han sido leídos para un CLOB, o cuando se alcanza el final del LOB. El puntero del LOB será desplazado por esta lectura del número de bytes/caracteres leídos.

## Parámetros

`length`  
El tamaño de los datos a leer, en bytes para un BLOB, en caracteres para un CLOB. Los valores grandes serán redondeados al MB inferior.

## Valores devueltos

Devuelve el contenido, en forma de un `string` o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL OCI8 3.0.0 | La clase `OCI-Lob` ha sido renombrada a `OCILob` para alinearse con los estándares de nomenclatura de PHP. |

## Véase también

[???](#ocilob.load), [???](#ocilob.write)
