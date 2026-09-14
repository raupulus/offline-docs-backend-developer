---
title: ZipArchive::getExternalAttributesName
description: Obtener los atributos externos de una entrada definida por su nombre
source_url: https://www.php.net/manual/es/ziparchive.getexternalattributesname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/getexternalattributesname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: false
translation_revision: 963af75fa
order: 108300
---

ZipArchive::getExternalAttributesName

Obtener los atributos externos de una entrada definida por su nombre

## Descripción

```php
public ZipArchive::getExternalAttributesName(string $name, int $opsys, int $attr, [int $flags]): bool
```php

Obtener los atributos externos de una entrada definida por su nombre.

## Parámetros

`name`  
El nombre de la entrada.

`opsys`  
En caso de éxito, recibe el código del sistema operativo definido por una de las constantes ZipArchive::OPSYS\_.

`attr`  
En caso de éxito, recibe los atributos externos. El valor depende del sistema operativo.

`flags`  
Si flags se establece a `ZipArchive::FL_UNCHANGED`, se devuelven los atributos originales sin cambios.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
