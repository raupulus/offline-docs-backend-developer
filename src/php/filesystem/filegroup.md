---
title: filegroup
description: Leer el nombre del grupo
source_url: https://www.php.net/manual/es/function.filegroup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/filegroup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 871a231f4
order: 23520
---

filegroup

Leer el nombre del grupo

## Descripción

```php
filegroup(string $filename): int
```php

Lee el nombre del grupo. El identificador de grupo se devuelve en formato numérico, utilice `posix_getgrgid` para recuperar el nombre del grupo.

## Parámetros

`filename`  
Ruta de acceso al fichero.

## Valores devueltos

Devuelve el grupo que posee el fichero `filename`, o `false` si ocurre un error. El identificador de grupo se devuelve en formato numérico, utilice `posix_getgrgid` para recuperar el nombre del grupo. En caso de error, se devuelve `false`.

## Errores/Excepciones

Si ocurre un error, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Buscar el grupo de un fichero

```
<?php
$filename = 'index.php';
print_r(posix_getgrgid(filegroup($filename)));
?>

    
```php

## Notas

> [!NOTE]
> Los resultados de esta función se almacenan en caché. Véase la función `clearstatcache` para más detalles.

> [!TIP]
> A partir de PHP 5.0.0, esta función también puede ser utilizada con *algunos* protocolos url. Lea [???](#wrappers) para conocer los protocolos que soportan la familia de funcionalidades de `stat`.

## Véase también

`fileowner`, `posix_getgrgid`
