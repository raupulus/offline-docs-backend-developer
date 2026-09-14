---
title: ps_add_locallink
description: Añadir un vínculo hacia una página del mismo documento
source_url: https://www.php.net/manual/es/function.ps-add-locallink.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-add-locallink.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 14af302c9
order: 65560
---

ps_add_locallink

Añadir un vínculo hacia una página del mismo documento

## Descripción

```php
ps_add_locallink(resource $psdoc, float $llx, float $lly, float $urx, float $ury, int $page, string $dest): bool
```php

Coloca un hipervínculo, en la posición dada, que apunta a una página del mismo documento. Al hacer clic sobre el vínculo se irá a la página en cuestión. La primera página de un documento tiene el número 1.

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

`page`  
El número de la página mostrada al hacer clic en el vínculo.

`dest`  
El parámetro `dest` determina cómo visualizar el documento. Puede ser `fitpage`, `fitwidth`, `fitheight`, o `fitbbox`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_add_launchlink`, `ps_add_pdflink`, `ps_add_weblink`
