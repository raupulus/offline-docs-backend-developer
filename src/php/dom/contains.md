---
title: Dom\TokenList::contains
description: Indica si la lista contiene un token dado
source_url: https://www.php.net/manual/es/dom-tokenlist.contains.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/tokenlist/contains.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: ffd2ef754
order: 12670
---

Dom\TokenList::contains

Indica si la lista contiene un token dado

## Descripción

```php
public Dom\TokenList::contains(string $token): bool
```php

Indica si la lista contiene `token`.

## Parámetros

`token`  
El token.

## Valores devueltos

Devuelve `true` si la lista contiene `token`, en caso contrario `false`.

## Ejemplos

Ejemplo de Dom\TokenList::contains

Verifica si dos clases están presentes en el párrafo.

```
<?php
$dom = Dom\HTMLDocument::createFromString('<p class="font-bold important"></p>', LIBXML_NOERROR);
$p = $dom->body->firstChild;

$classList = $p->classList;
var_dump(
    $classList->contains('important'),
    $classList->contains('font-small'),
);
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)
