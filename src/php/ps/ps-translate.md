---
title: ps_translate
description: Establecer una traslación
source_url: https://www.php.net/manual/es/function.ps-translate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-translate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: d3294c38b
order: 66310
---

ps_translate

Establecer una traslación

## Descripción

```php
ps_translate(resource $psdoc, float $x, float $y): bool
```php

Establece un nuevo punto inicial del sistema de coordenadas.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`x`  
La coordenada x del origen del sistema de coordenadas trasladado.

`y`  
La coordenada y del origen del sistema de coordenadas trasladado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Traslación del sistema de coordenadas

```
<?php
function rectángulo($ps) {
    ps_moveto($ps, 0, 0);
    ps_lineto($ps, 0, 50);
    ps_lineto($ps, 50, 50);
    ps_lineto($ps, 50, 0);
    ps_lineto($ps, 0, 0);
    ps_stroke($ps);
}

$ps = ps_new();
if (!ps_open_file($ps, "traslación.ps")) {
  print "No se puede abrir el fichero PostScript\n";
  exit;
}

ps_set_info($ps, "Creator", "traslación.php");
ps_set_info($ps, "Author", "Uwe Steinmann");
ps_set_info($ps, "Title", "Ejemplo de traslación");
ps_set_info($ps, "BoundingBox", "0 0 596 842");

$psfont = ps_findfont($ps, "Helvetica", "", 0);

ps_begin_page($ps, 596, 842);
ps_set_text_pos($ps, 100, 100);
ps_translate($ps, 500, 750);
rectángulo($ps);
ps_translate($ps, -500, -750);
ps_setfont($ps, $psfont, 8.0);
ps_show($ps, "Texto en posición inicial");
ps_end_page($ps);

ps_begin_page($ps, 596, 842);
ps_set_text_pos($ps, 100, 100);
ps_save($ps);
ps_translate($ps, 500, 750);
rectángulo($ps);
ps_restore($ps);
ps_setfont($ps, $psfont, 8.0);
ps_show($ps, "Texto en posición inicial");
ps_end_page($ps);

ps_delete($ps);
?>

    
```php

El ejemplo anterior demuestra dos maneras posibles de colocar un gráfico (en este caso un rectángulo) en cualquier posición de la página, mientras que el gráfico mismo utiliza su propio sistema de coordenadas. El truco está en cambiar el origen del sistema de coordenadas actual antes de dibujar el rectángulo. La traslación tiene que ser deshecha después de dibujar el gráfico.

En la segunda página se aplica un enfoque algo diferente y más elegante. En vez de deshacer la traslación con una segunda llamada a la función `ps_translate` el contexto de gráficos se guarda antes de modificar el sistema de coordenadas y se restaura después de dibujar el rectángulo.

## Véase también

`ps_scale`, `ps_rotate`
