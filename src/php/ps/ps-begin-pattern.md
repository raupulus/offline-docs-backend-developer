---
title: ps_begin_pattern
description: Inicia un nuevo patrón
source_url: https://www.php.net/manual/es/function.ps-begin-pattern.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-begin-pattern.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: c6fb604f3
order: 65630
---

ps_begin_pattern

Inicia un nuevo patrón

## Descripción

```php
ps_begin_pattern(resource $psdoc, float $width, float $height, float $xstep, float $ystep, int $painttype): int
```php

Inicia un nuevo patrón. Un patrón es como una página que contiene, por ejemplo, un dibujo que puede ser utilizado para rellenar sectores. Se utiliza como un color al llamar a `ps_setcolor` y configurando la posición del color en el `patrón`.

## Parámetros

`psdoc`  
Identificador de un archivo postscript devuelto por `ps_new`.

`width`  
El ancho del patrón en píxeles.

`height`  
La altura del patrón en píxeles.

`xstep`  
La distancia en píxeles de la posición del patrón en la dirección horizontal.

`ystep`  
La distancia en píxeles de la posición del patrón en la dirección vertical.

`painttype`  
Debe ser 1 o 2.

## Valores devueltos

El identificador del patrón o `false` si ocurre un error.

## Ejemplos

Creación y utilización de un patrón

```
<?php
$ps = ps_new();

if (!ps_open_file($ps, "pattern.ps")) {
  print "Imposible abrir el archivo PostScript\n";
  exit;
}

ps_set_parameter($ps, "warning", "true");
ps_set_info($ps, "Creator", "pattern.php");
ps_set_info($ps, "Author", "Uwe Steinmann");
ps_set_info($ps, "Title", "Ejemplo de Patrón");

$pspattern = ps_begin_pattern($ps, 10.0, 10.0, 10.0, 10.0, 1);
ps_setlinewidth($ps, 0.2);
ps_setcolor($ps, "stroke", "rgb", 0.0, 0.0, 1.0, 0.0);
ps_moveto($ps, 0, 0);
ps_lineto($ps, 7, 7);
ps_stroke($ps);
ps_moveto($ps, 0, 7);
ps_lineto($ps, 7, 0);
ps_stroke($ps);
ps_end_pattern($ps);

ps_begin_page($ps, 596, 842);
ps_setcolor($ps, "both", "pattern", $pspattern, 0.0, 0.0, 0.0);
ps_rect($ps, 50, 400, 200, 200);
ps_fill($ps);
ps_end_page($ps);

ps_close($ps);
ps_delete($ps);
?>

    
```php

## Véase también

`ps_end_pattern`, `ps_setcolor`, `ps_shading_pattern`
