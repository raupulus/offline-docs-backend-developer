---
title: tidy::getHtmlVer
description: Obtiene la versión detectada de HTML en un documento especificado
source_url: https://www.php.net/manual/es/tidy.gethtmlver.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/gethtmlver.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 2b84fa46e
order: 94040
---

tidy::getHtmlVer

tidy_get_html_ver

Obtiene la versión detectada de HTML en un documento especificado

## Descripción

Estilo orientado a objetos

```php
public tidy::getHtmlVer(): int
```php

Estilo procedimental

```php
tidy_get_html_ver(tidy $tidy): int
```

Devuelve la versión detectada HTML de un objeto `tidy` especificado.

## Parámetros

`tidy`  
El objeto `Tidy`

## Valores devueltos

Devuelve la versión detectada HTML.

> [!WARNING]
> Esta función aún no está implementada en la librería Tidylib, por tanto siempre devolverá `0`.
