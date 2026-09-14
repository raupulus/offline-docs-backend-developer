---
title: Imagick::writeImageFile
description: Escribe una imagen en un descriptor de archivo
source_url: https://www.php.net/manual/es/imagick.writeimagefile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/writeimagefile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 20ddc39b6
order: 36100
---

Imagick::writeImageFile

Escribe una imagen en un descriptor de archivo

## Descripción

```php
public Imagick::writeImageFile(resource $filehandle, [string $format]): bool
```php

Escribe la secuencia de la imagen en un descriptor de archivo abierto. El descriptor debe haber sido abierto con, por ejemplo, la función fopen. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

## Parámetros

`filehandle`  
Descriptor de archivo en el cual la imagen será escrita.

`format`  
El formato de la imagen. La lista de especificadores de formato válidos depende del conjunto de funcionalidades compilado de ImageMagick, y puede ser consultada en tiempo de ejecución mediante Imagick::queryFormats.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Véase también

Imagick::queryFormats
