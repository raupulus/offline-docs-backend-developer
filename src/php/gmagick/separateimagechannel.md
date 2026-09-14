---
title: Gmagick::separateimagechannel
description: Separa un canal de una imagen
source_url: https://www.php.net/manual/es/gmagick.separateimagechannel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/separateimagechannel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27480
---

Gmagick::separateimagechannel

Separa un canal de una imagen

## Descripción

```php
public Gmagick::separateimagechannel(int $channel): Gmagick
```php

Separa un canal de una imagen y devuelve una imagen en escala de grises. Un canal es un componente de un color particular de cada píxel de una imagen.

## Parámetros

`channel`  
Una de las constantes [de canales](#gmagick.constants.channel) (`Gmagick::CHANNEL_*`).

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
