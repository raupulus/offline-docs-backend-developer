---
title: LuaSandboxFunction::call
description: Llama a una función Lua
source_url: https://www.php.net/manual/es/luasandboxfunction.call.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/luasandbox/luasandboxfunction/call.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: luasandbox
translation_status: ready
translation_reviewed: false
translation_revision: 9c40251a8
order: 44110
---

LuaSandboxFunction::call

Llama a una función Lua

## Descripción

```php
public LuaSandboxFunction::call(string ...$args): array
```php

Llama a una función Lua.

Los errores considerados como culpa del código PHP harán que la función devuelva el valor `false` y emita `E_WARNING`, por ejemplo, un tipo `resource` utilizado como argumento. Los errores Lua lanzarán una excepción `LuaSandboxRuntimeError`.

Los tipos PHP y Lua se convierten de la siguiente manera:

- Los `null` de PHP son Lua `nil`, y viceversa.

- Los `int`s de PHP y `float`s se convierten en números Lua. El infinito y `NAN` son soportados.

- Los números Lua sin parte fraccionaria entre aproximadamente `-2**53` y `2**53` se convierten en `int`s PHP, los demás se convierten en `float`s PHP.

- Los `bool`s de PHP son booleanos Lua, y viceversa.

- Los `string`s de PHP son cadenas Lua, y viceversa.

- Las funciones Lua son objetos PHP `LuaSandboxFunction`, y viceversa. Los `callable`s PHP generales no son soportados.

- Los `array`s de PHP se convierten en tablas Lua, y viceversa.

  - Se debe tener en cuenta que Lua indexa típicamente los arrays a partir de 1, mientras que PHP indexa los arrays a partir de 0. No se hace ningún ajuste para estas diferentes convenciones.

  - Los arrays auto-referenciales no son soportados en ambos sentidos.

  - Las referencias PHP son desreferenciadas.

  - Los `__pairs` y `__ipairs` de Lua son tratados. `__index` es ignorado.

  - Al convertir de PHP a Lua, las claves enteras entre `-2**53` y `2**53` se representan como números Lua. Todas las demás claves se representan como cadenas Lua.

  - Al convertir de Lua a PHP, las claves distintas de las cadenas y los números enteros resultarán en un error, así como las colisiones al convertir números en cadenas o viceversa (ya que PHP considera cosas como `$a[0]` y `$a["0"]` como equivalentes).

- Todos los demás tipos no son soportados y resultarán en un error/excepción, incluyendo los `object`s PHP generales y los tipos userdata y thread Lua.

Las funciones Lua devuelven intrínsecamente una lista de resultados. Por lo tanto, en caso de éxito, este método devuelve un `array` que contiene todos los valores devueltos por Lua, con claves `int` comenzando en cero. Lua puede no devolver ningún resultado, en cuyo caso se devuelve un array vacío.

## Parámetros

`args`  
Los argumentos pasados a la función.

## Valores devueltos

Devuelve un `array` de los valores devueltos por la función, que puede estar vacío, o `false` si ocurre un error.
