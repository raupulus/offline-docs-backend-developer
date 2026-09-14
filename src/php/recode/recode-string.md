---
title: recode_string
description: Recodifica una string según la petición
source_url: https://www.php.net/manual/es/function.recode-string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/recode/functions/recode-string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: recode
translation_status: ready
translation_reviewed: false
translation_revision: 72f847e07
order: 68880
---

recode_string

Recodifica una string según la petición

## Descripción

```php
recode_string(string $request, string $string): string
```php

Recodifica la string `string` según la petición `request`.

## Parámetros

`request`  
El tipo de petición de recodificación deseado

`string`  
La string a recodificar

## Valores devueltos

Devuelve la string recodificada en caso de éxito y false en caso contrario.

## Ejemplos

Ejemplo con `recode_string`

```
<?php
echo recode_string("us..flat", "El carácter siguiente es diacrítico: á");
?>

   
```php

## Notas

Una petición simple de recodificación puede ser "lat1..iso646-de".

## Véase también

Consulte la documentación GNU Recode de su instalación para más detalles sobre las peticiones.

mb_convert_encoding

UConverter::transcode

iconv
