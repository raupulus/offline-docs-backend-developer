---
title: ps_hyphenate
description: Une palabras
source_url: https://www.php.net/manual/es/function.ps-hyphenate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-hyphenate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 65830
---

ps_hyphenate

Une palabras

## Descripción

```php
ps_hyphenate(resource $psdoc, string $text): array
```php

Une la palabra pasada. `ps_hyphenate` evalúa la valor hyphenminchars (establecido por `ps_set_value`) y el argumento hyphendic (establecido por `ps_set_parameter`). hyphendict debe ser establecido antes de llamar a esta función.

Esta función requiere que la configuración local `LC_CTYPE` esté correctamente hecha. Esto se realiza cuando la extensión es inicializada utilizando las variables de entorno. En sistemas Unix, consulte las páginas de manual de locale para más información.

## Parámetros

`psdoc`  
Identificador de un archivo postscript devuelto por `ps_new`.

`text`  
`text` no debería contener caracteres no alfabéticos. Las posiciones posibles para los cortes son devueltas en un array de números enteros. Cada número es la posición del carácter en `text` después de que la unión pueda tener lugar.

## Valores devueltos

Un array de enteros que indica la posición de los cortes posibles en el texto o `false` si ocurre un error.

## Ejemplos

Corta un texto

```
<?php
$word = "Koordinatensystem";
$psdoc = ps_new();
ps_set_parameter($psdoc, "hyphendict", "hyph_de.dic");
$hyphens = ps_hyphenate($psdoc, $word);
for($i=0; $i<strlen($word); $i++) {
  echo $word[$i];
  if(in_array($i, $hyphens))
    echo "-";
}
ps_delete($psdoc);
?>

    
```php

El ejemplo anterior mostrará:

    Ko-ordi-na-ten-sys-tem

## Véase también

`ps_show_boxed`, locale(1)
