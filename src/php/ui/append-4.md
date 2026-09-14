---
title: UI\Controls\Form::append
description: Añade un control
source_url: https://www.php.net/manual/es/ui-controls-form.append.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ui/ui/controls/form/append.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ui
translation_status: ready
translation_reviewed: false
translation_revision: b8758b060
order: 96660
---

UI\Controls\Form::append

Añade un control

## Descripción

```php
public UI\Controls\Form::append(string $label, UI\Control $control, [bool $stretchy]): int
```php

Añade el control al formulario y define la etiqueta

## Parámetros

`label`  
El texto de la etiqueta

`control`  
Un control

`stretchy`  
Debe establecerse en true para estirar el control

## Valores devueltos

Devuelve el índice del control añadido, puede ser 0
