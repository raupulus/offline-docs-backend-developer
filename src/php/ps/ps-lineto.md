---
title: ps_lineto
description: Dibujar una línea
source_url: https://www.php.net/manual/es/function.ps-lineto.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-lineto.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65850
---

ps_lineto

Dibujar una línea

## Descripción

```php
ps_lineto(resource $psdoc, float $x, float $y): bool
```php

Añade una línea recta al trazado actual desde el punto actual hasta las coordenadas dadas. Use la función `ps_moveto` para establecer el punto de inicio de la línea.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`x`  
La coordenada x del punto final de la línea.

`y`  
La coordenada y del punto final de la línea.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Dibujar un rectángulo

```
<?php
$ps = ps_new();
if (!ps_open_file($ps, "rectángulo.ps")) {
  print "No se puede abrir el fichero PostScript\n";
  exit;
}

ps_set_info($ps, "Creator", "rectángulo.php");
ps_set_info($ps, "Author", "Uwe Steinmann");
ps_set_info($ps, "Title", "Ejemplo de lineto");

ps_begin_page($ps, 596, 842);
ps_moveto($ps, 100, 100);
ps_lineto($ps, 100, 200);
ps_lineto($ps, 200, 200);
ps_lineto($ps, 200, 100);
ps_lineto($ps, 100, 100);
ps_stroke($ps);
ps_end_page($ps);

ps_delete($ps);
?>

    
```php

## Véase también

`ps_moveto`
