---
title: Imagick::clipPathImage
description: Recorta a lo largo de trazados nominados desde un perfil 8BIM
source_url: https://www.php.net/manual/es/imagick.clippathimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/clippathimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32830
---

Imagick::clipPathImage

Recorta a lo largo de trazados nominados desde un perfil 8BIM

## Descripción

```php
public Imagick::clipPathImage(string $pathname, bool $inside): bool
```php

Recorta a lo largo de trazados nominados desde un perfil 8BIM, si está presente. Las operaiones posteriores toman efecto dentro del trazado. Puede ser un número si está precedido de \#, para trabajar con un trazado numerado, p.ej., "#1" para usar el primer trazado.

## Parámetros

`pathname`  
El nombre del trazado

`inside`  
Si es `true` las operaciones posteriores toman efecto dentro del patrón de recorte. De otro modo, las operaciones toman efecto fuera del patrón de recorte.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
