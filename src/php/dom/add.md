---
title: Dom\TokenList::add
description: Añade los tokens dados a la lista
source_url: https://www.php.net/manual/es/dom-tokenlist.add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/tokenlist/add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: ffd2ef754
order: 12660
---

Dom\TokenList::add

Añade los tokens dados a la lista

## Descripción

```php
public Dom\TokenList::add(string ...$tokens): void
```php

Añade los `tokens` dados a la lista, pero no aquellos que ya estaban presentes.

## Parámetros

`tokens`  
Los tokens a añadir.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

- Levanta una ValueError si un token contiene bytes nulos.

- Levanta una Dom\DOMException con el código `Dom\SYNTAX_ERR` si un token es una cadena vacía.

- Levanta una Dom\DOMException con el código `Dom\INVALID_CHARACTER_ERR` si un token contiene espacios ASCII.

## Ejemplos

Ejemplo de Dom\TokenList::add

Añade dos clases a un elemento párrafo recién creado.

```
<?php
$dom = Dom\HTMLDocument::createEmpty();
$p = $dom->createElement('p');

$classList = $p->classList;
$classList->add('font-bold', 'important');

echo $dom->saveHtml($p);
?>

   
```php

El ejemplo anterior mostrará:

    <p class="font-bold important"></p>
