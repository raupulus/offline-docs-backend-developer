---
title: Imagick::setImageIndex
description: Establece la posición del iterador
source_url: https://www.php.net/manual/es/imagick.setimageindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setimageindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35400
---

Imagick::setImageIndex

Establece la posición del iterador

> [!WARNING]
> Esta función está *DEPRECADA* a partir de Imagick 3.4.4. Depender de esta funcionalidad está fuertemente desaconsejado.

## Descripción

```php
public Imagick::setImageIndex(int $index): bool
```php

Establece la posición del iterador en la lista de imágenes especificada con el parámetro index.

Este método ha quedado obsoleto. Véase `Imagick::setIteratorIndex`.

## Parámetros

`index`  
La posición donde se va a establecer el iterador

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
