---
title: ps_begin_template
description: Iniciar una nueva plantilla
source_url: https://www.php.net/manual/es/function.ps-begin-template.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-begin-template.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65640
---

ps_begin_template

Iniciar una nueva plantilla

## Descripción

```php
ps_begin_template(resource $psdoc, float $width, float $height): int
```php

Inicia una nueva plantilla. A una plantilla se le conoce como forma en el lenguaje postscript. Se crea de forma similar a un patrón pero se utiliza como una imagen. Las plantilla a menudo se usan para dibujar algo que se coloca varias veces a lo largo de un documento, p.ej. el logotipo de una compañía. Se puede usar todas las funciones de dibujo dentro de una plantilla. La plantilla no será dibujada hasta que sea colocada mediante la función `ps_place_image`.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`width`  
El ancho de la plantilla en píxeles.

`height`  
El alto de la plantilla en píxeles.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Crear y utilizar una plantilla

```
<?php
$ps = ps_new();

if (!ps_open_file($ps, "plantilla.ps")) {
  print "No se puede abrir el fichero PostScript\n";
  exit;
}

ps_set_parameter($ps, "warning", "true");
ps_set_info($ps, "Creator", "plantilla.php");
ps_set_info($ps, "Author", "Uwe Steinmann");
ps_set_info($ps, "Title", "Ejemplo de plantilla");

$plantilla_ps = ps_begin_template($ps, 30.0, 30.0);
ps_moveto($ps, 0, 0);
ps_lineto($ps, 30, 30);
ps_moveto($ps, 0, 30);
ps_lineto($ps, 30, 0);
ps_stroke($ps);
ps_end_template($ps);

ps_begin_page($ps, 596, 842);
ps_place_image($ps, $plantilla_ps, 20.0, 20.0, 1.0);
ps_place_image($ps, $plantilla_ps, 50.0, 30.0, 0.5);
ps_place_image($ps, $plantilla_ps, 70.0, 70.0, 0.6);
ps_place_image($ps, $plantilla_ps, 30.0, 50.0, 1.3);
ps_end_page($ps);

ps_close($ps);
ps_delete($ps);
?>

    
```php

## Véase también

`ps_end_template`
