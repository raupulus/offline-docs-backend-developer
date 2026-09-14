---
title: FFI::cast
description: Realiza una conversión de tipo C
source_url: https://www.php.net/manual/es/ffi.cast.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ffi/cast.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: e14fdcab8
order: 22920
---

FFI::cast

Realiza una conversión de tipo C

## Descripción

```php
public FFI::cast(FFI\CType $type, FFI\CData $ptr): FFI\CData
```php

FFI::cast crea un nuevo objeto `FFI\CData` que hace referencia a la misma estructura de datos C, pero que está asociada a un tipo diferente. El objeto resultante no posee los datos C y la fuente `ptr` debe sobrevivir al resultado. El tipo C puede ser especificado como `string` con cualquier declaración de tipo C válida o como objeto `FFI\CType`, creado previamente. Cualquier tipo declarado para la instancia está permitido.

## Parámetros

`type`  
Una declaración C válida como `string`, o una instancia de `FFI\CType` que ya ha sido creada.

`ptr`  
El gestor del puntero de una estructura de datos C.

## Valores devueltos

Devuelve el objeto `FFI\CData` recién creado.

## Historial de cambios

| Versión | Descripción                                          |
|---------|------------------------------------------------------|
| 8.3.0   | La llamada estática a FFI::cast ahora está obsoleta. |
