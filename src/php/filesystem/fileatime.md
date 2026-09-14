---
title: fileatime
description: Devuelve la fecha en la que el fichero fue accedido por última vez
source_url: https://www.php.net/manual/es/function.fileatime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fileatime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 871a231f4
order: 23500
---

fileatime

Devuelve la fecha en la que el fichero fue accedido por última vez

## Descripción

```php
fileatime(string $filename): int
```php

Devuelve la fecha en la que el fichero fue accedido por última vez.

## Parámetros

`filename`  
Ruta hacia el fichero.

## Valores devueltos

Devuelve la fecha en la que el fichero fue accedido por última vez o `false` si ocurre un error. La fecha se devuelve en formato timestamp Unix.

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Ejemplo con `fileatime`

```
<?php

// Muestra: somefile.txt fue accedido el: December 29 2002 22:16:23.

$filename = 'somefile.txt';
if (file_exists($filename)) {
    echo "$filename fue accedido el: " . date("F d Y H:i:s.", fileatime($filename));
}

?>

    
```php

## Notas

> [!NOTE]
> La fecha de última modificación de un fichero se supone que cambia cada vez que los bloques de datos del fichero comienzan a ser leídos. Esto puede ser muy costoso en términos de rendimiento cuando una aplicación accede regularmente a muchos ficheros o directorios.
>
> La mayoría de los sistemas de archivos Unix pueden ser montados con esta información desactivada para aumentar el rendimiento de una aplicación de este tipo; los nuevos `USENET` son un buen ejemplo. En tales sistemas de archivos, esta función se vuelve totalmente inútil.

> [!NOTE]
> Tenga en cuenta que la precisión temporal puede variar según el sistema de archivos utilizado.

> [!NOTE]
> Los resultados de esta función se almacenan en caché. Véase la función `clearstatcache` para más detalles.

> [!TIP]
> A partir de PHP 5.0.0, esta función también puede ser utilizada con *algunos* protocolos url. Lea [???](#wrappers) para conocer los protocolos que soportan la familia de funcionalidades de `stat`.

## Véase también

`filemtime`, `fileinode`, `date`
