---
title: ps_setpolydash
description: Establecer la apariencia de una línea discontinua
source_url: https://www.php.net/manual/es/function.ps-setpolydash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-setpolydash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66160
---

ps_setpolydash

Establecer la apariencia de una línea discontinua

## Descripción

```php
ps_setpolydash(resource $psdoc, float $arr): bool
```php

Establece la longitud de las porciones negras y blancas de una línea discontinua. La función `ps_setpolydash` se usa para establecer patrones discontinuos más complejos.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`arr`  
`arr` es una lista de elementos de longitud alternados para las porciones negras y blancas.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Dibujar una línea discontinua

```
<?php
$ps = ps_new();
if (!ps_open_file($ps, "poliraya.ps")) {
   print "No se puede abrir el fichero PostScript\n";
     exit;
}

ps_set_info($ps, "Creator", "poliraya.php");
ps_set_info($ps, "Author", "Uwe Steinmann");
ps_set_info($ps, "Title", "Ejemplo de poliraya");

ps_begin_page($ps, 596, 842);
ps_setpolydash($ps, array(10, 5, 2, 5));
ps_moveto($ps, 100, 100);
ps_lineto($ps, 200, 200);
ps_stroke($ps);
ps_end_page($ps);

ps_delete($ps);
?>

    
```php

Este ejemplo dibuja una línea con rayas de 10 y 2 puntos de longitud, y huecos de 5 puntos entre ellas.

## Véase también

`ps_setdash`
