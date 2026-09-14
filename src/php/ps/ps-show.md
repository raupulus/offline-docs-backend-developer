---
title: ps_show
description: Imprimir texto
source_url: https://www.php.net/manual/es/function.ps-show.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-show.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66230
---

ps_show

Imprimir texto

## Descripción

```php
ps_show(resource $psdoc, string $text): bool
```php

Imprime un texto en la posición de texto actual. La posición de texto puede ser establecida almacenado las coordenadas x e y en los valores `textx` y `texty` con la función `ps_set_value`. La función emitirá un error si no se estableció antes una fuente con la función `ps_setfont`.

`ps_show` evalúa los siguientes parámetros y valores establecidos por las funciones `ps_set_parameter` y `ps_set_value`:

charspacing (valor)  
Distancia entre dos glifos consecutivos. Si este valor es distinto de cero todas las ligaduras serán resueltas. Están permitidos valores menores que cero.

kerning (parámetro)  
Establecer este parámetro a "false" desactivará el interletraje. El interletraje está activado por defecto.

ligatures (parámetro)  
Establecer esta parámetro a "false" desactivará el uso de ligaduras. Las ligaduras están activadas por defecto.

underline (parámetro)  
Establecer esta parámetro a "true" activará el subrayado. El subrayado está desctivado por defecto.

overline (parámetro)  
Establecer esta parámetro a "true" activará el suprarayado. El suprarayado está desctivado por defecto.

strikeout (parámetro)  
Establecer esta parámetro a "true" activará el tachado. El tachado está desctivado por defecto.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`text`  
El texto a imprimir.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_continue_text`, `ps_show_xy`, `ps_setfont`
