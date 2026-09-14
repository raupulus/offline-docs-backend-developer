---
title: ps_add_note
description: Añadir una nota a la página actual
source_url: https://www.php.net/manual/es/function.ps-add-note.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-add-note.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 14af302c9
order: 65570
---

ps_add_note

Añadir una nota a la página actual

## Descripción

```php
ps_add_note(resource $psdoc, float $llx, float $lly, float $urx, float $ury, string $contents, string $title, string $icon, int $open): bool
```php

Añade una nota en una cierta posición del página. Las notas son como pequeñas hojas rectangulares con texto dentro que pueden ser colocadas en cualquer lugar de una página. Se muestran tanto plegadas como desplegadas. Si están desplegadas se utiliza el icono especificado como marcador de posición.

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

`contents`  
El texto de la nota.

`title`  
El título de la nota a mostrar en la cabecera de la nota.

`icon`  
El icono mostrado si la nota está plegada. Este parámetro puede ser establecido a `comment`, `insert`, `note`, `paragraph`, `newparagraph`, `key`, o `help`.

`open`  
Si `open` es distinto de cero, la nota se mostrará desplegada después de abrir el documento con un visualizador de pdf.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_add_pdflink`, `ps_add_launchlink`, `ps_add_locallink`, `ps_add_weblink`
