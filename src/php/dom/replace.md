---
title: Dom\TokenList::replace
description: Reemplaza un token en la lista por otro
source_url: https://www.php.net/manual/es/dom-tokenlist.replace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/tokenlist/replace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: ffd2ef754
order: 12720
---

Dom\TokenList::replace

Reemplaza un token en la lista por otro

## Descripción

```php
public Dom\TokenList::replace(string $token, string $newToken): bool
```php

Reemplaza un token en la lista por otro.

## Parámetros

`token`  
El token a reemplazar.

`newToken`  
El nuevo token.

## Valores devueltos

Devuelve `true` si `token` estaba en la lista, en caso contrario `false`.

## Errores/Excepciones

- Levanta una ValueError si un token contiene bytes nulos.

- Levanta una Dom\DOMException con el código `Dom\SYNTAX_ERR` si un token es una cadena vacía.

- Levanta una Dom\DOMException con el código `Dom\INVALID_CHARACTER_ERR` si un token contiene espacios ASCII.

## Ejemplos

Ejemplo de Dom\TokenList::replace

Reemplaza un token en el párrafo por otro.

```
<?php
$dom = Dom\HTMLDocument::createFromString('<p class="font-bold important"></p>', LIBXML_NOERROR);
$p = $dom->body->firstChild;

$p->classList->replace('font-bold', 'font-small');

echo $dom->saveHtml($p);
?>

   
```php

El ejemplo anterior mostrará:

    <p class="font-small important"></p>
