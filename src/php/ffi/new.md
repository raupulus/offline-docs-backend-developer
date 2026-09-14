---
title: FFI::new
description: Crea una estructura de datos C
source_url: https://www.php.net/manual/es/ffi.new.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ffi/new.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 23000
---

FFI::new

Crea una estructura de datos C

## Descripción

```php
public FFI::new(FFI\CType $type, [bool $owned], [bool $persistent]): FFI\CData
```php

Crea una estructura de datos nativa del tipo C dado. Cualquier tipo declarado para la instancia está permitido.

## Parámetros

`type`  
`type` es una declaración C válida como `string`, o una instancia de `FFI\CType` que ya ha sido creada.

`owned`  
Creación de datos gestionados o no gestionados. Los datos gestionados viven con el objeto `FFI\CData` devuelto, y son liberados cuando la última referencia a este objeto es liberada por el conteo de referencias ordinario de PHP o el recolector de basura. Los datos no gestionados deben ser liberados llamando a FFI::free, cuando ya no sean necesarios.

`persistent`  
Asignar la estructura de datos C de manera permanente en el montón del sistema (utilizando `malloc`), o en el montón de las peticiones PHP (utilizando `emalloc`).

## Valores devueltos

Devuelve el objeto `FFI\CData` recién creado, o `null` en caso de fallo.

## Historial de cambios

| Versión | Descripción                                         |
|---------|-----------------------------------------------------|
| 8.3.0   | La llamada estática a FFI::new ahora está obsoleta. |
