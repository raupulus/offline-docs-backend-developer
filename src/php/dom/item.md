---
title: Dom\TokenList::item
description: Devuelve un token de la lista
source_url: https://www.php.net/manual/es/dom-tokenlist.item.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/tokenlist/item.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: ffd2ef754
order: 12700
---

Dom\TokenList::item

Devuelve un token de la lista

## Descripción

```php
public Dom\TokenList::item(int $index): string
```php

Devuelve un token de la lista en el `index`.

## Parámetros

`index`  
El índice del token.

## Valores devueltos

Devuelve el token en el `index` o `null` cuando el índice está fuera de los límites.

## Ejemplos

Ejemplo de Dom\TokenList::item

Accede a un índice válido y a un índice inválido.

```
<?php
$dom = Dom\HTMLDocument::createFromString('<p class="font-bold important"></p>', LIBXML_NOERROR);
$p = $dom->body->firstChild;

$classList = $p->classList;
var_dump(
    $classList->item(0),
    $classList->item(100),
);
?>

   
```php

El ejemplo anterior mostrará:

    string(9) "font-bold"
    NULL

## Notas

> [!NOTE]
> Este método es equivalente al uso de la sintaxis de acceso a arrays.
