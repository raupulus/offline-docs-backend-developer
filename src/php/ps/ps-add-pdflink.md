---
title: ps_add_pdflink
description: Añadir un vínculo hacia una página de un segundo documento PDF
source_url: https://www.php.net/manual/es/function.ps-add-pdflink.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-add-pdflink.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 14af302c9
order: 65580
---

ps_add_pdflink

Añadir un vínculo hacia una página de un segundo documento PDF

## Descripción

```php
ps_add_pdflink(resource $psdoc, float $llx, float $lly, float $urx, float $ury, string $filename, int $page, string $dest): bool
```php

Coloca un hipervínculo, en la posición dada, que apunta a un segundo documento pdf. Al hacer clic sobre el vínculo se irá a la página dada del segundo documento. La primera página de un documento tiene el número 1.

La posición origen del hipervículo es un rectángulo que tiene su esquina inferior izquierda en (`llx`, `lly`) y su esquina superior derecha en (`urx`, `ury`). El rectángulo tiene por defecto un borde fino azul.

La nota no será visible si el documento es impreso o mostrado, pero será visible si el documento es convertido a PDF, ya sea por Acrobat Distiller™, o por Ghostview.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`llx`  
La coordenada x de la esquina inferior izquierda.

`lly`  
La coordenada y de la esquina inferior izquierda.

`urx`  
La coordenada x de la esquina superior derecha.

`ury`  
La coordenada y de la esquina superior derecha.

`filename`  
El nombre del documento pdf a abrir cuando se haga clic en este vínculo.

`page`  
El número de página del documento pdf destino

`dest`  
El parámetro `dest` determina cómo visualizar el documento. Puede ser `fitpage`, `fitwidth`, `fitheight`, o `fitbbox`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_add_launchlink`, `ps_add_locallink`, `ps_add_weblink`
