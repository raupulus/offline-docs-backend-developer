---
title: filetype
description: Devuelve el tipo de fichero
source_url: https://www.php.net/manual/es/function.filetype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/filetype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: e9c706885
order: 23580
---

filetype

Devuelve el tipo de fichero

## Descripción

```php
filetype(string $filename): string
```php

Devuelve el tipo de un fichero dado.

## Parámetros

`filename`  
Ruta de acceso al fichero.

## Valores devueltos

Devuelve el tipo del fichero. Las respuestas posibles son : `fifo`, `char`, `dir`, `block`, `link`, `file` `socket` y `unknown`.

Devuelve `false` en caso de error. `filetype` también emite un error `E_NOTICE` si el llamado a stat falla, o si el tipo de fichero es desconocido.

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Ejemplo con `filetype`

```
<?php

echo filetype('/etc/passwd');
echo "\n";
echo filetype('/etc/');
?>

    
```php

El ejemplo anterior mostrará:

    file
    dir

## Notas

> [!NOTE]
> Los resultados de esta función se almacenan en caché. Véase la función `clearstatcache` para más detalles.

> [!TIP]
> A partir de PHP 5.0.0, esta función también puede ser utilizada con *algunos* protocolos url. Lea [???](#wrappers) para conocer los protocolos que soportan la familia de funcionalidades de `stat`.

## Véase también

`is_dir`, `is_file`, `is_link`, `file_exists`, `mime_content_type`, `pathinfo`, `stat`
