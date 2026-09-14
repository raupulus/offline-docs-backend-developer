---
title: Imagick::count
description: Devuelve el número de imágenes
source_url: https://www.php.net/manual/es/imagick.count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 66d9935ec
order: 33000
---

Imagick::count

Devuelve el número de imágenes

## Descripción

```php
public Imagick::count([int $mode]): int
```php

Devuelve el número de imágenes.

## Parámetros

`mode`  
Un argumento no utilizado. Actualmente, existe una funcionalidad no particularmente bien definida en PHP donde la llamada a count() sobre un objeto contable podría (o no) requerir que este método acepte un parámetro. Este parámetro está aquí para ser conforme a la interfaz de countable, incluso si el parámetro no es utilizado.

## Valores devueltos

Devuelve el número de imágenes.
