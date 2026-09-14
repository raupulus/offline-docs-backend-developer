---
title: ps_set_info
description: Establecer los campos de información del documento
source_url: https://www.php.net/manual/es/function.ps-set-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-set-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: c6fb604f3
order: 66020
---

ps_set_info

Establecer los campos de información del documento

## Descripción

```php
ps_set_info(resource $psdoc, string $key, string $value): bool
```php

Establece ciertos campos de información del documento. Estos campos se mostrarán como un comentario en la cabecera del fichero PostScript. Si el documento es convertido a pdf, estos campos también se usarán para la información del documento.

El campo `BoundingBox` normalmente se establece al valor dado a la primera página. Esto sólo funciona si no se ha llamado antes a la función `ps_findfont`. En tal caso BoundingBox estará sin establecer a menos que se establezca explícitamente con esta función.

Esta función ya no tendrá efecto cuando la cabecera del fichero postscript ha sido escrita. Debe ser llamada antes de la primera página o de la primera llamada a la función `ps_findfont`.

## Parámetros

`psdoc`  
Un identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`key`  
El nombre del campo de información a establecer. Los valores que se pueden establecer son `Keywords` (palabras clave), `Subject` (asunto), `Title` (título), `Creator` (creador), `Author` (autor), `BoundingBox` (caja circundante), y `Orientation` (orientación). Tenga en cuenta que algunos de ellos tienen un significado para los visualizadoes de PostScript.

`value`  
El valor del campo de información. El campo `Orientation` puede ser establecido a `Portrait` (horizontal) o `Landscape` (vertical). El campo `BoundingBox` es una cadena de caracteres que consiste en cuatro números. Los dos primeros son las coordenadas de la esquina inferior izquierda de la página. Los dos últimos son las coordenadas de la esquina superior derecha.

> [!NOTE]
> Hasta la versión 0.2.6 de pslib, los campos BoundingBox y Orientation eran sobrescritos por la función `ps_begin_page`, a menos que se llamara antes a la función `ps_findfont`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_findfont`, `ps_begin_page`
