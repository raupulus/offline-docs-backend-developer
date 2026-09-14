---
title: ps_show_boxed
description: Escritura de texto en una caja
source_url: https://www.php.net/manual/es/function.ps-show-boxed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-show-boxed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: cdc9d28d3
order: 66200
---

ps_show_boxed

Escritura de texto en una caja

## Descripción

```php
ps_show_boxed(resource $psdoc, string $text, float $left, float $bottom, float $width, float $height, string $hmode, [string $feature]): int
```php

`ps_show_boxed` escribe texto en una caja dada. La esquina inferior izquierda de la caja se encuentra en (`left`, `bottom`). Se insertarán saltos de línea donde sea necesario. Los espacios múltiples se tratan como uno solo. Las tabulaciones se tratan como espacios.

El texto será ligado si el parámetro `hyphenation` está fijado a `true` y el parámetro `hyphendict` contiene un archivo válido para un archivo de ligadura. El espacio entre líneas se toma de la valor `leading`. Los párrafos pueden ser separados por una línea vacía como en TeX. Si el valor `parindent` está fijado a un valor \> 0.0, entonces las primeras n líneas serán indentadas. El número n de líneas está fijado por el parámetro `numindentlines`. Para prever la indentación de los primeros m párrafos, fije el valor `parindentskip` a un número positivo.

## Parámetros

`psdoc`  
Identificador de un archivo PostScript devuelto por `ps_new`.

`text`  
El texto a ser mostrado en la caja dada.

`left`  
La posición x de la esquina inferior izquierda de la caja.

`bottom`  
La posición y de la esquina inferior izquierda de la caja.

`width`  
Ancho de la caja.

`height`  
Altura de la caja.

`hmode`  
El parámetro `hmode` puede ser `justify`, `fulljustify`, `right`, `left`, o `center`. La diferencia entre `justify` y `fulljustify` afecta simplemente a la última línea de la caja. En el modo `fulljustify`, la última línea será justificada de izquierda a derecha a menos que sea también la última línea del párrafo. En el modo `"justify"`, el texto será siempre justificado a la izquierda.

`feature`  

## Parámetros utilizados

La escritura de `ps_show_boxed` puede ser configurada con varios parámetros y valores que pueden ser fijados por `ps_set_parameter` o `ps_set_value`. Además de los parámetros y valores que afectan la escritura del texto, los siguientes parámetros y valores son evaluados.

leading (valor)  
Distancia entre las líneas de base de dos líneas consecutivas.

linebreak (parámetro)  
Fijado a `true` si se desea un retorno de carro para iniciar una nueva línea en lugar de tratarlo como un espacio. Por omisión, este parámetro vale `false`.

parbreak (parámetro)  
Fijado a `true` si se desea un retorno de carro de una sola línea para iniciar un nuevo párrafo en lugar de tratarlo como un espacio. Por omisión, este parámetro vale `true`.

hyphenation (parámetro)  
Fijado a `true` para activar las ligaduras. Esto requiere un diccionario fijado por el parámetro `hyphendict`. Por omisión, este parámetro vale `false`.

hyphendict (parámetro)  
Archivo del diccionario utilizado para un patrón de ligadura (ver más abajo).

hyphenminchar (valor)  
El número de caracteres que debe haber al menos a la izquierda antes o después del guión. Esto implica que solo las palabras con al menos el doble de este valor pueden ser ligadas. El valor por omisión es tres. Fijar un valor de cero resultará en el valor por omisión.

parindent (valor)  
Fija el número de espacio en píxeles para la indentación de las primeras m líneas de un párrafo. m puede ser configurado con el valor `numindentlines`.

parskip (valor)  
Fija el número de espacio extra en píxeles entre los párrafos. Por omisión, al poner `0`, el resultado será una distancia normal entre las líneas.

numindentlines (valor)  
Número de líneas desde el inicio del párrafo que serán indentadas. Por omisión, este valor vale `1`.

parindentskip (valor)  
Número de párrafos en la caja a los cuales las primeras líneas no serán indentadas. Por omisión, este valor vale `0`. Esto es útil para los párrafos inmediatamente después de una sección de encabezado o texto que comienza en una segunda caja. En ambos casos, debe ser fijado a `1`.

linenumbermode (parámetro)  
Fija cómo se numeran las líneas. Los valores posibles son `box` para numerar las líneas en toda la caja o `paragraph` para numerar las líneas en cada párrafo.

linenumberspace (valor)  
El espacio para la columna dejado de las líneas numeradas que contiene el número de línea. El número de las líneas será justificado a la derecha en esta columna. Por omisión, este valor vale `20`.

linenumbersep (valor)  
El espacio entre la columna con el número de líneas y la línea misma. Por omisión, este valor vale `5`.

## Ligadura

El texto es ligado si el parámetro `hyphenation` está fijado a `true` y un diccionario válido de ligadura está fijado. pslib no proporciona su propio diccionario de ligadura, sino que utiliza uno de openoffice, scribus o koffice. Puede encontrar estos diccionarios para diferentes idiomas en uno de los siguientes directorios si el programa está instalado: `/usr/share/apps/koffice/hyphdicts/`, `/usr/lib/scribus/dicts/`, `/usr/lib/openoffice/share/dict/ooo/` Actualmente, Scribus parece tener los diccionarios de ligadura más completos.

## Valores devueltos

Número de caracteres que no pueden ser escritos.

## Véase también

`ps_continue_text`
