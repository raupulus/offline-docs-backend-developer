---
title: zlib://
description: Flujos de compresión
source_url: https://www.php.net/manual/es/wrappers.compression.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/wrappers/compression.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 8bc832a46
order: 4610
---

zlib://

bzip2://

zip://

Flujos de compresión

## Descripción

`compress.zlib://` y `compress.bzip2://`

`zlib:` funciona como `gzopen`, excepto que el flujo puede ser utilizado directamente con `fread` y otras funciones del sistema de archivos. Esta notación está obsoleta debido a ambigüedades con nombres de archivos que contienen dos puntos ':'. Utilice en su lugar `compress.zlib://`.

`compress.zlib://` y `compress.bzip2://` son equivalentes respectivamente a `gzopen` y `bzopen`, y funcionan incluso en sistemas que no soportan fopencookie.

La [extensión ZIP](#book.zip) proporciona el envoltorio `zip:`. A partir de PHP 7.2.0 y libzip 1.2.0+, se ha añadido el soporte para contraseñas en archivos cifrados, permitiendo que las contraseñas sean proporcionadas por contextos de flujo. Las contraseñas pueden ser definidas en un flujo utilizando la opción de contexto `'password'`.

## Uso

- `compress.zlib://file.gz`

- `compress.bzip2://file.bz2`

- `zip://archive.zip#dir/file.txt`

## Opciones

| Atributo | Soportado |
|----|----|
| Limitado por [allow_url_fopen](#ini.allow-url-fopen) | No |
| Permite la lectura | Sí |
| Permite la escritura | Sí (excepto `zip://`) |
| Permite la adición | Sí (excepto `zip://`) |
| Permite la lectura y escritura simultáneamente | No |
| Soporte de la función `stat` | No, utilice el gestor `file://` para obtener información sobre archivos comprimidos. |
| Soporte de la función `unlink` | No, utilice el gestor `file://` para obtener información sobre archivos comprimidos. |
| Soporte de la función `rename` | No |
| Soporte de la función `mkdir` | No |
| Soporte de la función `rmdir` | No |

Resumen de envolturas {role="stream_wrapper"}

## Véase también
