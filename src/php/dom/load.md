---
title: DOMDocument::load
description: Cargar un documento XML de un archivo.
source_url: https://www.php.net/manual/es/domdocument.load.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/load.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: c1f37a6c2
order: 13140
---

DOMDocument::load

Cargar un documento XML de un archivo.

## Descripción

```php
public DOMDocument::load(string $filename, [int $options]): bool
```php

Cargar un documento XML de un archivo.

> [!WARNING]
> Rutas tipo Unix con barras inclinadas hacia a delante, pueden causar una degradacion significativa de rendimiento en sistemas Windows; asegúrese de llamar `realpath` en es el caso.

## Parámetros

`filename`  
La ruta al documento XML.

`options`  
[Bit a bit `OR`](#language.operators.bitwise) de las [constantes de opción libxml](#libxml.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si se pasa un string vacío como el `filename` o se pasa el nombre de un archivo vacío, se generará una advertencia. Esta advertencia no es generada por libxml y no puede ser manejada utilizando las funciones de control de errores de libxml.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Esta función ahora tiene un tipo de retorno `bool` tentativo. |
| 8.0.0 | Llamar a esta función de forma estática ahora lanzará un `Error`. Anteriormente, se emitía un `E_DEPRECATED`. |

## Ejemplos

Creando un Documento

```
<?php
$doc = new DOMDocument();
$doc->load('examples/book.xml');
echo $doc->saveXML();
?>

    
```php

## Véase también

DOMDocument::loadXML, DOMDocument::save, DOMDocument::saveXML
