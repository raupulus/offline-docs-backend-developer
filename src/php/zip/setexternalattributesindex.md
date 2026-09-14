---
title: ZipArchive::setExternalAttributesIndex
description: Establece los atributos externos de una entrada definida por su índice
source_url: https://www.php.net/manual/es/ziparchive.setexternalattributesindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/setexternalattributesindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: false
translation_revision: 963af75fa
order: 108550
---

ZipArchive::setExternalAttributesIndex

Establece los atributos externos de una entrada definida por su índice

## Descripción

```php
public ZipArchive::setExternalAttributesIndex(int $index, int $opsys, int $attr, [int $flags]): bool
```php

Establece los atributos externos de una entrada definida por su índice.

## Parámetros

`index`  
El índice de la entrada.

`opsys`  
El código del sistema operativo definido por una de las constantes ZipArchive::OPSYS\_.

`attr`  
Los atributos externos. El valor depende del sistema operativo.

`flags`  
Banderas opcionales. Actualmente no se utiliza.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
