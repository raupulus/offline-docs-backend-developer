---
title: Diferencias con Lua estándar
source_url: https://www.php.net/manual/es/reference.luasandbox.differences.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/luasandbox/differences.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: luasandbox
translation_status: ready
translation_reviewed: false
translation_revision: 9c40251a8
order: 43890
---

## Diferencias con Lua estándar

LuaSandbox proporciona un entorno seguro que difiere en algunos aspectos de Lua 5.1 estándar.

## Funcionalidades no disponibles

- Los paquetes `dofile()`, `loadfile()`, y `io`, ya que permiten acceso directo al sistema de ficheros. Si es necesario, el acceso al sistema de ficheros debe realizarse a través de funciones de retrollamada PHP.

- El paquete `package`, incluyendo `require()` y `module()`, ya que depende en gran medida del acceso directo al sistema de ficheros. Una reescritura pura de Lua como la utilizada en la extensión MediaWiki Scribunto puede ser utilizada en su lugar.

- `load()` y `loadstring()`, para permitir el análisis estático del código Lua.

- `print()`, ya que escribe en la salida estándar. Si es necesario, la salida debe realizarse a través de funciones de retrollamada PHP.

- La mayoría del paquete `os`, ya que permite la manipulación del proceso y la ejecución de otros procesos.

  - `os.clock()`, `os.date()`, `os.difftime()`, y `os.time()` siguen estando disponibles.

- La mayoría del paquete `debug`, ya que permite la manipulación del estado Lua y de los metadatos de manera que puede romper el aislamiento.

  - `debug.traceback()` sigue estando disponible.

- `string.dump()`, ya que puede exponer datos internos.

- El paquete `collectgarbage()`, `gcinfo()`, y `coroutine` no han sido examinados en cuanto a seguridad.

## Funcionalidades que han sido modificadas

- `pcall()` y `xpcall()` no pueden capturar ciertos errores, en particular los errores de tiempo límite.

- `tostring()` no incluye las direcciones de puntero.

- `string.match()` ha sido parcheado para limitar la profundidad de recursión y para verificar periódicamente un tiempo límite.

- `math.random()` y `math.randomseed()` son reemplazados por versiones que no comparten el estado con `rand()` de PHP.

- Las meta métodos de Lua 5.2 `__pairs` y `__ipairs` son soportadas por `pairs()` y `ipairs()`.
