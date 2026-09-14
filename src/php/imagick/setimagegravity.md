---
title: Imagick::setImageGravity
description: Establece la gravedad de la imagen
source_url: https://www.php.net/manual/es/imagick.setimagegravity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimagegravity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35380
---

Imagick::setImageGravity

Establece la gravedad de la imagen

## Descripción

```php
public Imagick::setImageGravity(int $gravity): bool
```php

Establece la propiedad gravedad de la imagen actual. Este método se puede usar para establecer la propiedad gravedad de una sóla secuencia de imágenes. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.4 o superior.

## Parámetros

`gravity`  
La propiedad gravedad. Consulte esta lista de [constantes de gravedad](#imagick.constants.gravity).

## Valores devueltos

No se retorna ningún valor.
