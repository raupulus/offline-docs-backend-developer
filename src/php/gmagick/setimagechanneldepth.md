---
title: Gmagick::setimagechanneldepth
description: Define la profundidad de un canal particular de la imagen
source_url: https://www.php.net/manual/es/gmagick.setimagechanneldepth.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/setimagechanneldepth.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27540
---

Gmagick::setimagechanneldepth

Define la profundidad de un canal particular de la imagen

## Descripción

```php
public Gmagick::setimagechanneldepth(int $channel, int $depth): Gmagick
```php

Define la profundidad de un canal particular de la imagen.

## Parámetros

`channel`  
Una de las constantes [de canales](#gmagick.constants.channel) (`Gmagick::CHANNEL_*`).

`depth`  
La profundidad de la imagen, en bytes.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
