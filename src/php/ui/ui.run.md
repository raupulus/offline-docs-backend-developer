---
title: UI\run
description: Entra en la bucle UI
source_url: https://www.php.net/manual/es/function.ui-run.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ui/functions/ui.run.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ui
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 96150
---

UI\run

Entra en la bucle UI

## Descripción

```php
UI\run([int $flags]): void
```php

Debe hacer que PHP entre en la bucle principal. Por omisión, el control no será devuelto a la función llamadora.

## Parámetros

`flags`  
Poner UI\Loop para devolver el control y UI\Wait para devolver el control después de la espera.

## Valores devueltos
