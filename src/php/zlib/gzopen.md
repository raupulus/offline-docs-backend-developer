---
title: gzopen
description: Abre un archivo gz
source_url: https://www.php.net/manual/es/function.gzopen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gzopen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_revision: aa120f36c
order: 108840
---

gzopen

Abre un archivo gz

## Descripción

```php
gzopen(string $filename, string $mode, [bool $use_include_path]): resource
```php

Abre un archivo gzip (.gz) para lectura o escritura.

`gzopen` se puede usar para leer un archivo el cual no esté en formato gzip; en este caso `gzread` leerá directamente el archivo sin descomprimirlo.

## Parámetros

`filename`  
El nombre del archivo.

`mode`  
Como en `fopen` (`rb` o `wb`) pero también puede incluir un nivel de compresión (`wb9`) u una estrategia: `f` para datos filtrados como en `wb6f`, `h` para `compresión Huffman solamente` como en `wb1h`. (Ver la descripción de `deflateInit2` en `zlib.h` para más información sobre el parámetro de estrategia.)

`use_include_path`  
Si se define como `true`, también se busca el archivo en la ruta [include_path](#ini.include-path).

## Valores devueltos

Retorna un apuntador hacia el archivo abierto, después de eso, cualquier cosa que se lea desde este descriptor de archivo sera descomprimido de forma transparente y lo que se escriba será comprimido.

Si falla la apertura, la función retorna `false`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | `use_include_path` es ahora de tipo `bool`. Anteriormente, era de tipo `int`. |

## Ejemplos

Ejemplo de `gzopen`

```
<?php
$fp = gzopen("/tmp/file.gz", "r");
?>

    
```php

## Véase también

`gzclose`
