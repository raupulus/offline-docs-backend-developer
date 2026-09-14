---
title: filemtime
description: Lee la fecha de última modificación del fichero
source_url: https://www.php.net/manual/es/function.filemtime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/filemtime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 871a231f4
order: 23540
---

filemtime

Lee la fecha de última modificación del fichero

## Descripción

```php
filemtime(string $filename): int
```php

Lee la fecha en la que el fichero fue modificado por última vez.

## Parámetros

`filename`  
Ruta de acceso al fichero.

## Valores devueltos

Devuelve el timestamp Unix de última modificación del fichero `filename` o `false` si ocurre un error. Utilice `date` sobre este resultado para obtener una fecha de modificación legible por humanos.

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Ejemplo con `filemtime`

```
<?php
// Mostrará: somefile.txt fue modificado el: December 29 2002 22:16:23.

$filename = 'somefile.txt';
if (file_exists($filename)) {
    echo "$filename fue modificado el: " . date ("F d Y H:i:s.", filemtime($filename));
}
?>

    
```php

## Notas

> [!NOTE]
> Tenga en cuenta que la precisión temporal puede variar según el sistema de archivos utilizado.

> [!NOTE]
> Los resultados de esta función se almacenan en caché. Véase la función `clearstatcache` para más detalles.

> [!TIP]
> A partir de PHP 5.0.0, esta función también puede ser utilizada con *algunos* protocolos url. Lea [???](#wrappers) para conocer los protocolos que soportan la familia de funcionalidades de `stat`.

## Véase también

`filectime`, `stat`, `touch`, `getlastmod`
