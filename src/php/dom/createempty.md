---
title: Dom\HTMLDocument::createEmpty
description: Crear un documento HTML vacío
source_url: https://www.php.net/manual/es/dom-htmldocument.createempty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/htmldocument/createempty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: a8b6f4dd3
order: 12530
---

Dom\HTMLDocument::createEmpty

Crear un documento

HTML

vacío

## Descripción

```php
public static Dom\HTMLDocument::createEmpty([string $encoding]): Dom\HTMLDocument
```php

Crear un documento HTML vacío sin ningún elemento.

## Parámetros

`encoding`  
El juego de caracteres del documento, utilizado para la serialización al llamar a los métodos de guardado.

## Valores devueltos

Un documento HTML vacío.

## Ejemplos

Ejemplo de Dom\HTMLDocument::createEmpty

Crear un documento vacío y serializarlo.

```
<?php
$dom = Dom\HTMLDocument::createEmpty();
var_dump($dom->saveHtml());
?>

   
```php

El ejemplo anterior mostrará:

    string(0) ""

## Véase también

Dom\HTMLDocument::createFromString

Dom\HTMLDocument::createFromFile
