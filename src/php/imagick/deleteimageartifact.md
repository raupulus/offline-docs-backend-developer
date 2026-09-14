---
title: Imagick::deleteImageArtifact
description: Borra un artefacto de imagen
source_url: https://www.php.net/manual/es/imagick.deleteimageartifact.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/deleteimageartifact.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33070
---

Imagick::deleteImageArtifact

Borra un artefacto de imagen

## Descripción

```php
public Imagick::deleteImageArtifact(string $artifact): bool
```php

Borra un artefacto asociado con la imagen. La diferencia entre las propiedades de imagen y los artefactos de imagen es que las propiedades son públicas y los artefactos son privados. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.5.7 o superior.

## Parámetros

`artifact`  
El nombre del artefacto a borrar.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Véase también

`Imagick::setImageArtifact`, `Imagick::getImageArtifact`
