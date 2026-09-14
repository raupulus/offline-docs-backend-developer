---
title: ps_set_text_pos
description: Establecer la posición de la salida de texto
source_url: https://www.php.net/manual/es/function.ps-set-text-pos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-set-text-pos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66040
---

ps_set_text_pos

Establecer la posición de la salida de texto

## Descripción

```php
ps_set_text_pos(resource $psdoc, float $x, float $y): bool
```php

Establece la posición de la siguiente salida de texto. Alternativamente se puede establecer los valores x e y por separado llamando a la función `ps_set_value` y eligiendo `textx` y `texty` respectivamente como el nombre del valor.

Si se ha de imprimir el texto en una cierta posición es más conveniente utilizar la función `ps_show_xy` en lugar de establecer la posición del texto y llamar a la función `ps_show`.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`x`  
La coordenada x de la nueva posición del texto.

`y`  
La coordenada y de la nueva posición del texto.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Colocar texto en una posición dada

```
<?php
$ps = ps_new();
if (!ps_open_file($ps, "texto.ps")) {
  print "No se pudo abrir el fichero PostScript\n";
  exit;
}

ps_set_info($ps, "Creator", "rectángulo.php");
ps_set_info($ps, "Author", "Uwe Steinmann");
ps_set_info($ps, "Title", "Ejemplo de colocación de texto");

ps_begin_page($ps, 596, 842);
$psfont = ps_findfont($ps, "Helvetica", "", 0);
ps_setfont($ps, $psfont, 8.0);
ps_show_xy($ps, "Algún texto en (100, 100)", 100, 100);

ps_set_value($ps, "textx", 100);
ps_set_value($ps, "texty", 120);
ps_show($ps, "Algún texto en (100, 120)");
ps_end_page($ps);

ps_delete($ps);
?>

    
```php

## Véase también

`ps_set_value`, `ps_show`
