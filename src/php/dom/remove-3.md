---
title: Dom\TokenList::remove
description: Elimina los tokens dados de la lista
source_url: https://www.php.net/manual/es/dom-tokenlist.remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/tokenlist/remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: ffd2ef754
order: 12710
---

Dom\TokenList::remove

Elimina los tokens dados de la lista

## Descripción

```php
public Dom\TokenList::remove(string ...$tokens): void
```php

Elimina los `tokens` dados de la lista, pero ignora aquellos que no estaban presentes.

## Parámetros

`tokens`  
Los tokens a eliminar.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

- Levanta una ValueError si un token contiene bytes nulos.

- Levanta una Dom\DOMException con el código `Dom\SYNTAX_ERR` si un token es una cadena vacía.

- Levanta una Dom\DOMException con el código `Dom\INVALID_CHARACTER_ERR` si un token contiene espacios ASCII.

## Ejemplos

Ejemplo de Dom\TokenList::remove

Elimina dos clases del párrafo.

```
<?php
$dom = Dom\HTMLDocument::createFromString('<p class="font-bold important"></p>', LIBXML_NOERROR);
$p = $dom->body->firstChild;

$p->classList->remove('font-bold', 'important');

echo $dom->saveHtml($p);
?>

   
```php

El ejemplo anterior mostrará:

    <p class=""></p>
