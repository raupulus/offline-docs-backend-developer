---
title: ps_add_bookmark
description: Añadir un marcapáginas a la página actual
source_url: https://www.php.net/manual/es/function.ps-add-bookmark.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-add-bookmark.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 14af302c9
order: 65540
---

ps_add_bookmark

Añadir un marcapáginas a la página actual

## Descripción

```php
ps_add_bookmark(resource $psdoc, string $text, [int $parent], [int $open]): int
```php

Añade un marcapáginas a la página actual. Los marcapáginas normalmente aparecen en los visualizadores de PDF a la izquierda de la página como un árbol jerárquico. Al hacer clic en un marcapáginas saltará a la página en cuestión.

La nota no será visible si el documento es impreso o mostrado, pero será visible si el documento es convertido a PDF, ya sea por Acrobat Distiller™, o por Ghostview.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`text`  
El texto usado para mostrar el marcapáginas.

`parent`  
Un marcapáginas previamente creado por esta función que se usa como padre del nuevo marcapáginas.

`open`  
Si `open` es distinto de cero, el visualizador de PDF mostrará el marcapáginas abierto.

## Valores devueltos

El valor devuelto es una referencia al marcapáginas. Sólo se utiliza si el marcapáginas se usa como padre. El valor es mayor que cero si la función tiene éxito. En caso de error se devolverá cero.

## Véase también

`ps_add_launchlink`, `ps_add_pdflink`, `ps_add_weblink`
