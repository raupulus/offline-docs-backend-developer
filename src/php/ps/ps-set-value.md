---
title: ps_set_value
description: Establecer ciertos valores
source_url: https://www.php.net/manual/es/function.ps-set-value.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-set-value.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 66050
---

ps_set_value

Establecer ciertos valores

## Descripción

```php
ps_set_value(resource $psdoc, string $name, float $value): bool
```php

Establece varios valores que son utilizados por muchas funciones. Los parámetros son por definición valores de tipo float.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`name`  
El nombre dado por `name` puede ser uno de los siguientes:

textrendering  
La manera en que se muestra el texto.

textx  
La coordenada x para la impresión del texto.

texty  
La coordenada y para la impresión del texto.

wordspacing  
La distancia entre palabras relativa al ancho de un espacio.

leading  
La distancia entre líneas en píxeles.

`value`  
El valor del parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_get_value`, `ps_set_parameter`
