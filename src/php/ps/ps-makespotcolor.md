---
title: ps_makespotcolor
description: Crear un color directo
source_url: https://www.php.net/manual/es/function.ps-makespotcolor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-makespotcolor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65860
---

ps_makespotcolor

Crear un color directo

## Descripción

```php
ps_makespotcolor(resource $psdoc, string $name, [int $reserved]): int
```php

Crea un color directo desde el color de relleno actual. El color de relleno debe ser definido en los espacios de color RGB, CMYK o gris. El nombre del color directo puede ser un nombre arbitrario. Un color directo se puede establecer como cualquier otro color con la función `ps_setcolor`. Cuando el documento no se imprime, sino que se muestra con un visualizador de postscript, se utiliza el color dado en el espacio de color especificado.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`name`  
El nombre del color directo, p.ej. Pantone 5565.

## Valores devueltos

El ID del nuevo color directo o 0 en caso de error.

## Ejemplos

Crear y utilizar un color directo

```
<?php
$ps = ps_new();
if (!ps_open_file($ps, "color_directo.ps")) {
  print "No se puede abrir el fichero PostScript\n";
  exit;
}

ps_set_info($ps, "Creator", "color_directo.php");
ps_set_info($ps, "Author", "Uwe Steinmann");
ps_set_info($ps, "Title", "Ejemplo de color directo");

ps_begin_page($ps, 596, 842);
ps_setcolor($ps, "fill", "cmyk", 0.37, 0.0, 0.34, 0.34);
$color_directo = ps_makespotcolor($ps, "PANTONE 5565 C", 0);
ps_setcolor($ps, "fill", "spot", $color_directo, 0.5, 0.0, 0.0);
ps_moveto($ps, 100, 100);
ps_lineto($ps, 100, 200);
ps_lineto($ps, 200, 200);
ps_lineto($ps, 200, 100);
ps_lineto($ps, 100, 100);
ps_fill($ps);
ps_end_page($ps);

ps_delete($ps);
?>

    
```php

Este ejemplo crea el color directo "PANTONE 5565 C" que es un verde oscuro (oliva) y rellena un rectángulo con el 50% de intensidad.

## Véase también

`ps_setcolor`
