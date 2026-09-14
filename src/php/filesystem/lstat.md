---
title: lstat
description: Devuelve información sobre un fichero o un enlace simbólico
source_url: https://www.php.net/manual/es/function.lstat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/lstat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 871a231f4
order: 23860
---

lstat

Devuelve información sobre un fichero o un enlace simbólico

## Descripción

```php
lstat(string $filename): array
```php

Devuelve información sobre un fichero o un enlace simbólico.

## Parámetros

`filename`  
Ruta de acceso a un fichero o un enlace simbólico.

## Valores devueltos

Consúltese la página del manual de `stat` para obtener más información sobre la estructura del array devuelto por `lstat`. Esta función es idéntica a la función `stat` excepto que si `filename` es un enlace simbólico, la información se basará en el enlace simbólico.

En caso de error, se devuelve `false`.

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Comparación entre `stat` y `lstat`

```
<?php
symlink('uploads.php', 'uploads');

// Se destaca la diferencia de información
array_diff(stat('uploads'), lstat('uploads'));
?>

    
```php

Resultado del ejemplo anterior es similar a:

Información que difiere entre los 2 ficheros.

    Array
    (
        [ino] => 97236376
        [mode] => 33188
        [size] => 34
        [atime] => 1223580003
        [mtime] => 1223581848
        [ctime] => 1223581848
        [blocks] => 8
    )

## Notas

> [!NOTE]
> Los resultados de esta función se almacenan en caché. Véase la función `clearstatcache` para más detalles.

> [!TIP]
> A partir de PHP 5.0.0, esta función también puede ser utilizada con *algunos* protocolos url. Lea [???](#wrappers) para conocer los protocolos que soportan la familia de funcionalidades de `stat`.

## Véase también

`stat`
