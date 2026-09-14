---
title: EventConfig::setFlags
description: Define uno o varios flags para configurar la inicialización eventual
  de EventBase
source_url: https://www.php.net/manual/es/eventconfig.setflags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventconfig/setflags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 19710
---

EventConfig::setFlags

Define uno o varios flags para configurar la inicialización eventual de EventBase

## Descripción

```php
public EventConfig::setFlags(int $flags): bool
```php

Define uno o varios flags para configurar las partes de la inicialización eventual de EventBase que serán inicializadas, y cómo funcionarán.

## Parámetros

`flags`  
Una de las constantes `EventBase::LOOP_*`. Ver [constantes de EventBase](#eventbase.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

EventBase::getFeatures
