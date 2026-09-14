---
title: file://
description: Acceso al sistema de ficheros local
source_url: https://www.php.net/manual/es/wrappers.file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/wrappers/file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 0592e6316
order: 4640
---

file://

Acceso al sistema de ficheros local

## Descripción

`file://` es la envoltura por defecto utilizada con PHP y representa el sistema de ficheros local. Cuando se especifica una ruta relativa (una ruta que no comienza con `/`, `\`, `\\`, o una letra de unidad Windows), la ruta proporcionada se aplicará al directorio de trabajo actual. En muchos casos, se trata del directorio en el que se encuentra el script, a menos que haya sido modificado. Con el CLI SAPI, esto por defecto corresponde al directorio desde el cual se llamó al script.

Con ciertas funciones como `fopen` y `file_get_contents`, `include_path` puede eventualmente ser analizada para encontrar los ficheros, si se proporciona una ruta relativa.

## Uso

- `/ruta/al/fichero.ext`

- `ruta/relativa/al/fichero.ext`

- `ficheroEnCwd.ext`

- `C:/ruta/al/ficheroWindows.ext`

- `C:\ruta\al\ficheroWindows.ext`

- `\\smbserver\compartido\ruta\al\ficheroWindows.ext`

- `file:///ruta/al/fichero.ext`

## Opciones

| Atributo                                                | Soportado |
|---------------------------------------------------------|-----------|
| Restringido por [allow_url_fopen](#ini.allow-url-fopen) | No        |
| Permite la lectura                                      | Sí        |
| Permite la escritura                                    | Sí        |
| Permite la adición                                      | Sí        |
| Permite simultáneamente la lectura y la escritura       | Sí        |
| Soporte de la función `stat`                            | Sí        |
| Soporte de la función `unlink`                          | Sí        |
| Soporte de la función `rename`                          | Sí        |
| Soporte de la función `mkdir`                           | Sí        |
| Soporte de la función `rmdir`                           | Sí        |

Resumen de la envoltura {role="stream_wrapper"}
