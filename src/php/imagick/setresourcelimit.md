---
title: Imagick::setResourceLimit
description: Define la limitación para una recurso particular
source_url: https://www.php.net/manual/es/imagick.setresourcelimit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setresourcelimit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 3193e2e78
order: 35690
---

Imagick::setResourceLimit

Define la limitación para una recurso particular

## Descripción

```php
public static Imagick::setResourceLimit(int $type, int $limit): bool
```php

Este método se utiliza para modificar las limitaciones de la recurso de la biblioteca subyacente ImageMagick.

## Parámetros

`type`  
Consulte la lista de [ constantes de tipo de recursos](#imagick.constants.resourcetypes).

`limit`  
Una de las [ constantes de tipo de recursos](#imagick.constants.resourcetypes). La unidad depende del tipo de la recurso a limitar.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Véase también

Imagick::getResourceLimit
