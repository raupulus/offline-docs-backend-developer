---
title: ps_get_parameter
description: Recupera ciertos parámetros
source_url: https://www.php.net/manual/es/function.ps-get-parameter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-get-parameter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: b95d28e6e
order: 65810
---

ps_get_parameter

Recupera ciertos parámetros

## Descripción

```php
ps_get_parameter(resource $psdoc, string $name, [float $modifier]): string
```php

Recupera varios parámetros que han sido establecidos directamente por `ps_set_parameter` o indirectamente por una o más funciones. Los parámetros son, por definición, valores de `string`. Esta función no puede ser utilizada para recuperar los recursos que también han sido establecidos por `ps_set_parameter`.

El parámetro `name` puede tener una de las siguientes valores.

`fontname`  
El nombre de la fuente actualmente activa o la fuente cuyo identificador es pasado en el parámetro `modifier`.

`fontencoding`  
La codificación de la fuente actualmente activa.

`dottedversion`  
La versión de la biblioteca subyacente pslib en el formato \<mayor\>.\<menor\>.\<submenor\>

`scope`  
El ámbito actual del dibujo. Puede ser un objeto, un documento, `null`, una página, un patrón, un camino, un modelo, un prólogo, una fuente, un glifo.

`ligaturedisolvechar`  
El carácter que descompone una ligadura. Si se utiliza una fuente que contiene una ligadura \`ff' y \`\|\` es el carácter para descomponer la ligadura, entonces \`f\|f' dará dos \`f' en lugar de la ligadura \`ff'.

`imageencoding`  
La codificación utilizada para codificar las imágenes. Puede ser `hex` o `85`. La codificación hex utiliza dos octetos en el archivo PostScript, cada octeto en una imagen. 85 representa la codificación Ascii85.

`linenumbermode`  
Se establece en `paragraph` si las líneas son numeradas dentro de un párrafo o `box` si son numeradas en una caja que las rodea.

`linebreak`  
Solo utilizado si el texto es mostrado con `ps_show_boxed`. Si se establece en `true`, un retorno de carro añadirá un salto de línea.

`parbreak`  
Solo utilizado si el texto es mostrado con `ps_show_boxed`. Si se establece en `true`, un retorno de carro iniciará un nuevo párrafo.

`hyphenation`  
Solo utilizado si el texto es mostrado con `ps_show_boxed`. Si se establece en `true`, el párrafo será dividido si un diccionario de guiones es establecido y existe.

`hyphendict`  
Nombre del archivo del diccionario utilizado para el patrón de guiones.

## Parámetros

`psdoc`  
Identificador de un archivo postscript devuelto por `ps_new`.

`name`  
Nombre del parámetro.

`modifier`  
Un identificador requerido si el parámetro de un recurso es requerido, por ejemplo, el tamaño de una imagen. En este caso, el identificador del recurso es pasado.

## Valores devueltos

Devuelve el valor del parámetro o `false` si ocurre un error.

## Véase también

`ps_set_parameter`
