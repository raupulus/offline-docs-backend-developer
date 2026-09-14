---
title: DOMDocument::loadXML
description: Carga de XML desde una cadena de caracteres
source_url: https://www.php.net/manual/es/domdocument.loadxml.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/loadxml.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: true
translation_revision: 765749a26
order: 13170
---

DOMDocument::loadXML

Carga de XML desde una cadena de caracteres

## Descripción

```php
public DOMDocument::loadXML(string $source, [int $options]): bool
```php

Carga un documento XML desde una cadena de caracteres.

## Parámetros

`source`  
La cadena de caracteres que contiene el XML.

`options`  
[El operador `OR`](#language.operators.bitwise) de las [constantes libxml](#libxml.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si se pasa una cadena vacía como argumento `source`, se generará una advertencia. Esta advertencia no es generada por libxml, y no puede ser gestionada utilizando las funciones de gestión de errores de libxml.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Esta función tiene ahora un tipo de retorno `bool` provisional. |
| 8.0.0 | La llamada estática a esta función levantará ahora una `Error`. Anteriormente, se generaba un error `E_DEPRECATED`. |

## Ejemplos

Creación de un Documento

```
<?php
$doc = new DOMDocument();
$doc->loadXML('<root><node/></root>');
echo $doc->saveXML();
?>

    
```php

## Véase también

DOMDocument::load, DOMDocument::save, DOMDocument::saveXML
