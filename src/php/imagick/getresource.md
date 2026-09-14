---
title: Imagick::getResource
description: Devuelve el consumo de memoria de la recurso
source_url: https://www.php.net/manual/es/imagick.getresource.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getresource.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 3193e2e78
order: 34240
---

Imagick::getResource

Devuelve el consumo de memoria de la recurso

## Descripción

```php
public static Imagick::getResource(int $type): int
```php

Devuelve el consumo de memoria de la recurso, en megabytes.

## Parámetros

`type`  
Véase la lista de [constantes de tipo de recursos](#imagick.constants.resourcetypes).

## Valores devueltos

Devuelve el consumo de memoria de la recurso, en megabytes.

## Errores/Excepciones

Lanza una ImagickException en caso de error.
