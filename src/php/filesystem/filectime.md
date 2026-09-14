---
title: filectime
description: Devuelve la fecha de última modificación del inodo de un fichero
source_url: https://www.php.net/manual/es/function.filectime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/filectime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 871a231f4
order: 23510
---

filectime

Devuelve la fecha de última modificación del inodo de un fichero

## Descripción

```php
filectime(string $filename): int
```php

Devuelve la fecha de última modificación del inodo de un fichero.

## Parámetros

`filename`  
Ruta de acceso al fichero.

## Valores devueltos

Devuelve la fecha en la que el inodo fue modificado por última vez o `false` si ocurre un error. La hora se devuelve en formato timestamp Unix.

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Ejemplo con `filectime`

```
<?php

// Muestra: somefile.txt fue modificado el: December 29 2002 22:16:23.

$filename = 'somefile.txt';
if (file_exists($filename)) {
    echo "$filename fue modificado el: " . date("F d Y H:i:s.", filectime($filename));
}

?>

    
```php

## Notas

> [!NOTE]
> En la mayoría de servidores UNIX, un fichero se considera modificado si los datos de su inodo son modificados. Es decir, cuando los permisos (de usuario, grupo u otros) han sido modificados. Véase también `filemtime` (que puede ser utilizado cuando se creen indicaciones como "Última modificación: " en las páginas web) y `fileatime`.

> [!NOTE]
> Tenga en cuenta que en algunos sistemas UNIX, el `ctime` de un fichero de texto es considerado como su fecha de creación. ¡Esto es falso! No existe una fecha de creación de fichero en la mayoría de los sistemas UNIX.

> [!NOTE]
> Tenga en cuenta que la precisión temporal puede variar según el sistema de archivos utilizado.

> [!NOTE]
> Los resultados de esta función se almacenan en caché. Véase la función `clearstatcache` para más detalles.

> [!TIP]
> A partir de PHP 5.0.0, esta función también puede ser utilizada con *algunos* protocolos url. Lea [???](#wrappers) para conocer los protocolos que soportan la familia de funcionalidades de `stat`.

## Véase también

`filemtime`
