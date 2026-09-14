---
title: Dom\TokenList::toggle
description: Conmuta la presencia de un token en la lista
source_url: https://www.php.net/manual/es/dom-tokenlist.toggle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/tokenlist/toggle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: ffd2ef754
order: 12740
---

Dom\TokenList::toggle

Conmuta la presencia de un token en la lista

## Descripción

```php
public Dom\TokenList::toggle(string $token, [bool $force]): bool
```php

Conmuta la presencia del `token` en la lista.

## Parámetros

`token`  
El token a conmutar.

`force`  
Si `force` es proporcionado, al definirlo como `true` se añadirá el token, y al definirlo como `false` se eliminará.

## Valores devueltos

Devuelve `true` si el token está en la lista después de la llamada, en caso contrario `false`.

## Errores/Excepciones

- Levanta una ValueError si un token contiene bytes nulos.

- Levanta una Dom\DOMException con el código `Dom\SYNTAX_ERR` si un token es una cadena vacía.

- Levanta una Dom\DOMException con el código `Dom\INVALID_CHARACTER_ERR` si un token contiene espacios ASCII.

## Ejemplos

Ejemplo de Dom\TokenList::toggle

Conmuta tres clases, dos sin `force`, y una con.

```
<?php
$dom = Dom\HTMLDocument::createFromString('<p class="font-bold important"></p>', LIBXML_NOERROR);
$p = $dom->body->firstChild;

$classList = $p->classList;
$classList->toggle('font-bold', 'font-small');
$classList->toggle('important', force: true);

echo $dom->saveHtml($p);
?>

   
```php

El ejemplo anterior mostrará:

    <p class="font-bold important"></p>
