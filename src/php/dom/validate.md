---
title: DOMDocument::validate
description: Valida un documento basado en su DTD
source_url: https://www.php.net/manual/es/domdocument.validate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/validate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: c1f37a6c2
order: 13300
---

DOMDocument::validate

Valida un documento basado en su DTD

## Descripción

```php
public DOMDocument::validate(): bool
```php

Valida un documento basado en su DTD.

Puede utilizarse la propiedad `validateOnParse` de la clase `DOMDocument` para realizar una validación DTD.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Si el documento no tiene ninguna DTD asociada, este método retornará `false`.

## Ejemplos

Ejemplo de validación DTD

```
<?php
$dom = new DOMDocument;
$dom->load('examples/book.xml');
if ($dom->validate()) {
    echo "¡Este documento es válido!\n";
}
?>

    
```php

Asimismo, puede validarse el fichero XML al cargarlo:

```
<?php
$dom = new DOMDocument;
$dom->validateOnParse = true;
$dom->load('examples/book.xml');
?>

    
```php

## Véase también

DOMDocument::schemaValidate, DOMDocument::schemaValidateSource, DOMDocument::relaxNGValidate, DOMDocument::relaxNGValidateSource
