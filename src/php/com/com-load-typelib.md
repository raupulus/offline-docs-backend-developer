---
title: com_load_typelib
description: Carga un Typelib
source_url: https://www.php.net/manual/es/function.com-load-typelib.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/functions/com-load-typelib.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: b9043112d
order: 7710
---

com_load_typelib

Carga un Typelib

## Descripción

```php
com_load_typelib(string $typelib, [bool $case_insensitive]): bool
```php

Carga un Typelib y registra su contenido en el motor, como si hubieran sido definidos utilizando `define`.

Tenga en cuenta que es más eficiente utilizar [com.typelib-file](#ini.com.typelib-file) `php.ini` la opción de configuración para precargar y registrar las constantes, aunque esto es menos flexible.

Si [com.autoregister-typelib](#ini.com.autoregister-typelib) está activado, entonces PHP intentará registrar automáticamente las constantes asociadas al objeto COM cuando se cree el objeto. Esto dependerá de la interfaz proporcionada por el propio objeto COM y no siempre será posible.

## Parámetros

`typelib`  
`typelib` puede ser uno de los siguientes valores:

- El nombre de un fichero `.tlb` o el módulo ejecutable que contiene el Typelib.

- El GUID del Typelib, seguido del número de versión; por ejemplo `{00000200-0000-0010-8000-00AA006D2EA4},2,0`.

- El nombre del Typelib, e.g `Microsoft OLE DB ActiveX Data Objects 1.0 Library`.

PHP intentará resolver el Typelib en este orden, y el proceso consumirá más recursos a medida que avance en la lista; la búsqueda del Typelib por su nombre se maneja físicamente enumerando el registro hasta que se encuentre un resultado.

`case_insensitive`  
El parámetro `case_insensitive` se comporta de manera inversa al parámetro `$case_insensitive` de la función `define`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
