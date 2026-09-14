---
title: filesize
description: Obtiene el tamaño de un fichero
source_url: https://www.php.net/manual/es/function.filesize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/filesize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_revision: 871a231f4
order: 23570
---

filesize

Obtiene el tamaño de un fichero

## Descripción

```php
filesize(string $filename): int
```php

Obtiene el tamaño del fichero especificado.

## Parámetros

`filename`  
Ruta de acceso al fichero.

## Valores devueltos

Devuelve el tamaño del fichero `filename` en bytes, o `false` (y genera un error de nivel `E_WARNING`) en caso de error.

> [!NOTE]
> Como el tipo entero de PHP es firmado y que muchas plataformas utilizan enteros de 32 bits, algunas funciones relacionadas con el sistema de archivos pueden retornar resultados extraños para ficheros de tamaño superior a 2 Go.

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Ejemplo con `filesize`

```
<?php

// Muestra por ejemplo:  somefile.txt: 1024 bytes

$filename = 'somefile.txt';
echo $filename . ': ' . filesize($filename) . ' bytes';

?>

    
```php

## Notas

> [!NOTE]
> Los resultados de esta función se almacenan en caché. Véase la función `clearstatcache` para más detalles.

> [!TIP]
> A partir de PHP 5.0.0, esta función también puede ser utilizada con *algunos* protocolos url. Lea [???](#wrappers) para conocer los protocolos que soportan la familia de funcionalidades de `stat`.

## Véase también

`file_exists`
