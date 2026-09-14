---
title: Imagick::resetImagePage
description: Reinicia una página de imagen
source_url: https://www.php.net/manual/es/imagick.resetimagepage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/resetimagepage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34940
---

Imagick::resetImagePage

Reinicia una página de imagen

## Descripción

```php
public Imagick::resetImagePage(string $page): bool
```php

La definición de página como un string. El string está en formato WxH+x+y (Ancho+Alto+x+y). Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

## Parámetros

`page`  
La definición de página. Por ejemplo `7168x5147+0+0`

## Valores devueltos

Devuelve `true` en caso de éxito.
