---
title: Yaf_View_Interface::setScriptPath
description: El propósito de setScriptPath
source_url: https://www.php.net/manual/es/yaf-view-interface.setscriptpath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_view_interface/setscriptpath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 107220
---

Yaf_View_Interface::setScriptPath

El propósito de setScriptPath

## Descripción

```php
abstract public Yaf_View_Interface::setScriptPath(string $template_dir): void
```php

Establece el directorio base de plantillas. Normalmente es llamado por `Yaf_Dispatcher`

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`template_dir`  
Una ruta absoluta al directorio de plantillas, por omisión, `Yaf_Dispatcher` usa [application.directory](#configuration.yaf.directory) . "/views" como este parámetro.

## Valores devueltos
