---
title: Imagick::getResourceLimit
description: Devuelve el límite de la recurso
source_url: https://www.php.net/manual/es/imagick.getresourcelimit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getresourcelimit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 3f91a9928
order: 34250
---

Imagick::getResourceLimit

Devuelve el límite de la recurso

## Descripción

```php
public static Imagick::getResourceLimit(int $type): int
```php

Devuelve el límite de la recurso.

## Parámetros

`type`  
Una de las [ constantes de tipo de recursos](#imagick.constants.resourcetypes).

## Valores devueltos

Devuelve el límite de recurso especificado. La unidad depende del tipo de recurso que está limitado.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Véase también

Imagick::setResourceLimit
