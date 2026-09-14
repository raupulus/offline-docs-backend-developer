---
title: ps_rotate
description: Establecer el factor de rotación
source_url: https://www.php.net/manual/es/function.ps-rotate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-rotate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65960
---

ps_rotate

Establecer el factor de rotación

## Descripción

```php
ps_rotate(resource $psdoc, float $rot): bool
```php

Establece la rotación del sistema de coordenadas.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`rot`  
El ángulo de rotación en grados.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Rotación del sistema de coordenadas

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
if (!ps_open_file($ps, "rotación.ps")) {
  print "No se pudo abrir el fichero PostScript\n";
  exit;
}

ps_set_info($ps, "Creator", "rotación.php");
ps_set_info($ps, "Author", "Uwe Steinmann");
ps_set_info($ps, "Title", "Ejemplo de rotación");
ps_set_info($ps, "BoundingBox", "0 0 596 842");

$psfont = ps_findfont($ps, "Helvetica", "", 0);

ps_begin_page($ps, 596, 842);
ps_set_text_pos($ps, 100, 100);
ps_save($ps);
ps_translate($ps, 100, 100);
ps_rotate($ps, 45);
rectángulo($ps);
ps_restore($ps);
ps_setfont($ps, $psfont, 8.0);
ps_show($ps, "Texto sin rotación");
ps_end_page($ps);

ps_delete($ps);
?>

    
```php

El ejemplo anterior ilustra una forma muy común de rotar un gráfico (en este caso un rectángulo) simplemente rotando el sistema de coordenadas. Ya que se asume que el origen del sistema de coordenadas del gráfico es (0,0), el sistema de coordenadas de la página también es trasladado para colocar los gráficos no en el extremo de la pagina. Se debe poner atención en el orden de `ps_translate` y `ps_rotate`. En el caso anterior el rectángulo es rotado alrededor del punto (100, 100) en el sistema de coordenadas sin trasladar. Si se cambian las dos sentencias se obtendrá un resultado completamente diferente.

Para poder imprimir el texto siguiente en la posición original, todas las modificaciones del sistema de coordenadas son encapsuladas en las funciones `ps_save` y `ps_restore`.

## Véase también

`ps_scale`, `ps_translate`
