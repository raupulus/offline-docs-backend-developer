---
title: gzfile
description: Lee un archivo gz completo en una matriz
source_url: https://www.php.net/manual/es/function.gzfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gzfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_revision: aa120f36c
order: 108790
---

gzfile

Lee un archivo gz completo en una matriz

## Descripción

```php
gzfile(string $filename, [bool $use_include_path]): array
```php

Está función es identica a `readgzfile`, excepto que retorna el archivo en una matriz.

## Parámetros

`filename`  
El nombre del archivo.

`use_include_path`  
Si se establece a `true`, también se buscan los archivos en la ruta [include_path](#ini.include-path).

## Valores devueltos

Una matriz que contiene el archivo, una línea por celda, incluidas líneas vacías, y con líneas nuevas aún unidas, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | `use_include_path` es ahora de tipo `bool`. Anteriormente, era de tipo `int`. |

## Ejemplos

Ejemplo de `gzfile`

```
<?php
$lines = gzfile('somefile.gz');
foreach ($lines as $line) {
    echo $line;
}
?>

    
```php

## Véase también

`readgzfile`, `gzopen`
