---
title: ps_get_value
description: Recupera ciertos valores
source_url: https://www.php.net/manual/es/function.ps-get-value.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-get-value.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: '475439775'
order: 65820
---

ps_get_value

Recupera ciertos valores

## Descripción

```php
ps_get_value(resource $psdoc, string $name, [float $modifier]): float
```php

Recupera varios valores que han sido establecidos por `ps_set_value`. Los valores son, por definición, valores de `float`.

El argumento `name` puede tener uno de los siguientes valores.

`fontsize`  
El tamaño de la fuente actualmente activa o la fuente cuyo identificador se pasa en el argumento `modifier`.

`font`  
La fuente actualmente activa en sí misma.

`imagewidth`  
La anchura de la imagen cuyo identificador se pasa en el argumento `modifier`.

`imageheight`  
La altura de la imagen cuyo identificador se pasa en el argumento `modifier`.

`capheight`  
La altura de una letra mayúscula M en la fuente actualmente activa o la fuente cuyo identificador se pasa en el argumento `modifier`.

`ascender`  
La hampe de la fuente actualmente activa o la fuente cuyo identificador se pasa en el argumento `modifier`.

`descender`  
El jambage de la fuente actualmente activa o la fuente cuyo identificador se pasa en el argumento `modifier`.

`italicangle`  
El parámetro italicangle de la fuente actualmente activa o la fuente cuyo identificador se pasa en el argumento `modifier`.

`underlineposition`  
El parámetro underlineposition de la fuente actualmente activa o la fuente cuyo identificador se pasa en el argumento `modifier`.

`underlinethickness`  
El parámetro underlinethickness de la fuente actualmente activa o la fuente cuyo identificador se pasa en el argumento `modifier`.

`textx`  
La posición x actual de visualización del texto.

`texty`  
La posición y actual de visualización del texto.

`textrendering`  
El modo actual para el renderizado del texto.

`textrise`  
El espacio por el cual el texto es aumentado por encima de la línea de base.

`leading`  
La distancia entre las líneas de texto en puntos.

`wordspacing`  
El espacio entre las palabras como múltiplo de la anchura de un carácter de espacio.

`charspacing`  
El espacio entre los caracteres. Si charspacing es != 0.0, las ligaduras siempre estarán desactivadas.

`hyphenminchars`  
Número mínimo de caracteres antes de un guion al final de una palabra.

`parindent`  
La indentación de las primeras n líneas en un párrafo.

`numindentlines`  
Número de líneas en un párrafo a indentar si paraindent != 0.0.

`parskip`  
Distancia entre los párrafos.

`linenumberspace`  
Espacio general frente a cada línea para el número de línea.

`linenumbersep`  
Espacio entre las líneas y los números de línea.

`major`  
El número de versión mayor de pslib.

`minor`  
El número de versión menor de pslib.

`subminor`, `revision`  
El número de versión submenor de pslib.

## Parámetros

`psdoc`  
Identificador de un archivo postscript devuelto por `ps_new`.

`name`  
Nombre del valor.

`modifier`  
El argumento `modifier` especifica el recurso para el cual se recuperará el valor. Esto puede ser el ID de la fuente o una imagen.

## Valores devueltos

Devuelve el valor del parámetro o `false`.

## Véase también

`ps_set_value`
