---
title: readgzfile
description: Lee todo el archivo comprimido
source_url: https://www.php.net/manual/es/function.readgzfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/readgzfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: true
translation_revision: aa120f36c
order: 108980
---

readgzfile

Lee todo el archivo comprimido

## Descripción

```php
readgzfile(string $filename, [bool $use_include_path]): int
```php

`readgzfile` lee el archivo `filename`, lo descomprime y muestra el resultado.

`readgzfile` también puede utilizarse para leer un archivo que no está comprimido: en este caso, `readgzfile` leerá el archivo sin descomprimirlo.

## Parámetros

`filename`  
El nombre del fichero. Este fichero deberá ser abierto desde el sistema de ficheros y su contenido será mostrado.

`use_include_path`  
Cuando se define como `true` la ruta [include_path](#ini.include-path) será utilizada para determinar el fichero a abrir.

## Valores devueltos

Devuelve el número de bytes (descomprimidos) leídos desde el fichero en caso de éxito, o `false` si ocurre un error

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | `use_include_path` es ahora de tipo `bool`. Anteriormente, era de tipo `int`. |

## Véase también

`gzpassthru`, `gzfile`, `gzopen`
