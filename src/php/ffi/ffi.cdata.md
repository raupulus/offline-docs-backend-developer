---
title: Gestor de datos C
source_url: https://www.php.net/manual/es/class.ffi-cdata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ffi/ffi.cdata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ffi
translation_status: ready
translation_reviewed: false
translation_revision: 37d269b8f
order: 23060
---

## Introducción

Los objetos `FFI\CData` pueden ser utilizados de diferentes maneras, como datos PHP normales:

- Los datos C de tipo escalar pueden ser leídos y asignados a través de la propiedad \$cdata, por ejemplo. `$x = FFI::new('int'); $x->cdata = 42;`

- Los campos de tipo struct y union pueden ser accedidos como propiedades de objetos PHP ordinarios, por ejemplo `$cdata->field`

- Los elementos de un array C son accesibles como los elementos de un array PHP, por ejemplo. `$cdata[$offset]`

- Los arrays C pueden ser iterados utilizando instrucciones [`foreach`](#control-structures.foreach).

- Los arrays C pueden ser utilizados como argumentos de `count`.

- Los punteros C pueden ser desreferenciados como arrays, por ejemplo `$cdata[0]`

- Los punteros C pueden ser comparados utilizando operadores de comparación ordinarios (`<`, `<=`, `==`, `!=`, `>=`, `>`).

- Los punteros C pueden ser incrementados y decrementados utilizando operaciones ordinarias ( `+`/`-`/ / ). `++`/`--`, por ejemplo `$cdata += 5`

- Los punteros C pueden ser sustraídos de otro utilizando operaciones ordinarias `-`.

- Los punteros C hacia funciones pueden ser llamados como una clausura PHP clásica, por ejemplo `$cdata()`

- Cualquier dato C puede ser duplicado utilizando el operador [clone](#language.oop5.cloning), por ejemplo `$cdata2 = clone $cdata;`

- Todos los datos C pueden ser visualizados utilizando `var_dump`, `print_r`, etc.

- `FFI\CData` puede ahora ser atribuido a estructuras y campos a partir de PHP 8.3.0.

> [!NOTE]
> Las limitaciones notables son que las instancias de `FFI\CData` no soportan las funciones `isset`, `empty` y `unset`, y que las structs y unions C envueltas no implementan Traversable.

## Sinopsis de la clase

FFI

final

CData

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.3.0   | `FFI\CData` puede ahora ser atribuido a estructuras y campos. |
