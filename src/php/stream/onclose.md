---
title: php_user_filter::onClose
description: Llamado cuando se cierra el filtro
source_url: https://www.php.net/manual/es/php-user-filter.onclose.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/php_user_filter/onclose.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 4f6742c6e
order: 88270
---

php_user_filter::onClose

Llamado cuando se cierra el filtro

## Descripción

```php
public php_user_filter::onClose(): void
```php

Este método es llamado bajo el cierre del filtro (normalmente también durante el cierre del flujo), y se ejecuta *después* de llamar al método `flush`. Si se asignó o inicializo cualquier recurso durante `onCreate()`, este sería el momento de destruirlo o deshacerse de él.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El valor de retorono es ignorado.
