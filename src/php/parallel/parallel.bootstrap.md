---
title: parallel\bootstrap
description: Inicialización
source_url: https://www.php.net/manual/es/parallel.bootstrap.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/functions/parallel.bootstrap.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 59950
---

parallel\bootstrap

Inicialización

## Descripción

```php
parallel\bootstrap(string $file): void
```php

Utiliza el `file` proporcionado para inicializar todas las ejecuciones creadas para la planificación automática a través de `parallel\run`.

## Parámetros

`file`  
La ruta del fichero para inicializar todas las ejecuciones.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

> [!WARNING]
> Lanza una excepción `parallel\Runtime\Error\Bootstrap` si ya ha sido llamado para este proceso.

> [!WARNING]
> Lanza una excepción `parallel\Runtime\Error\Bootstrap` si es llamado después de `parallel\run`.

## Véase también
