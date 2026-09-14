---
title: fileowner
description: Lee el identificador del propietario de un fichero
source_url: https://www.php.net/manual/es/function.fileowner.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fileowner.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 871a231f4
order: 23550
---

fileowner

Lee el identificador del propietario de un fichero

## Descripción

```php
fileowner(string $filename): int
```php

Lee el identificador del propietario de un fichero.

## Parámetros

`filename`  
Ruta de acceso al fichero.

## Valores devueltos

Devuelve el identificador del propietario del fichero `filename`, o `false` si ocurre un error. El identificador del propietario es numérico: es necesario utilizar `posix_getpwuid` para obtener el nombre de usuario.

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Búsqueda del propietario de un fichero

```
<?php
$filename = 'index.php';
print_r(posix_getpwuid(fileowner($filename)));
?>

    
```php

## Notas

> [!NOTE]
> Los resultados de esta función se almacenan en caché. Véase la función `clearstatcache` para más detalles.

> [!TIP]
> A partir de PHP 5.0.0, esta función también puede ser utilizada con *algunos* protocolos url. Lea [???](#wrappers) para conocer los protocolos que soportan la familia de funcionalidades de `stat`.

## Véase también

`filegroup`, `stat`, `posix_getpwuid`
