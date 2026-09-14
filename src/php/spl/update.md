---
title: SplObserver::update
description: Recibe actualizaciones de sujeto
source_url: https://www.php.net/manual/es/splobserver.update.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobserver/update.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 85270
---

SplObserver::update

Recibe actualizaciones de sujeto

## Descripción

```php
public SplObserver::update(SplSubject $subject): void
```php

Este método es llamado cuando cualquier `SplSubject` se use para llamar llamadas adjuntas SplSubject::notify.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`subject`  
El objeto `SplSubject` notificando al observador de una actualización.

## Valores devueltos

No se retorna ningún valor.
