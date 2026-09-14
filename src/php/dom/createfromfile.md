---
title: Dom\HTMLDocument::createFromFile
description: Analiza un documento HTML a partir de un fichero
source_url: https://www.php.net/manual/es/dom-htmldocument.createfromfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/htmldocument/createfromfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: a8b6f4dd3
order: 12540
---

Dom\HTMLDocument::createFromFile

Analiza un documento

HTML

a partir de un fichero

## Descripción

```php
public static Dom\HTMLDocument::createFromFile(string $path, [int $options], [string $overrideEncoding]): Dom\HTMLDocument
```php

Analiza un documento HTML a partir de un fichero, según la norma vigente.

## Parámetros

`path`  
La ruta de acceso del fichero a analizar.

`options`  
[Operación a nivel de bits `OR`](#language.operators.bitwise) de las [constantes de opción libxml](#libxml.constants).

También es posible pasar `Dom\HTML_NO_DEFAULT_NS` para desactivar el uso del espacio de nombres HTML y del elemento template. Esto solo debería ser utilizado si las implicaciones son correctamente comprendidas.

`overrideEncoding`  
El codificado en el cual el documento fue creado. Si no se proporciona, intentará determinar el codificado más probable utilizado.

## Valores devueltos

El documento analizado en forma de una instancia de `Dom\HTMLDocument`.

## Errores/Excepciones

- Genera una ValueError si `path` contiene bytes nulos o contiene `"%00"`.

- Levanta una excepción ValueError si `options` contiene una opción inválida.

- Levanta una excepción ValueError si `overrideEncoding` utiliza un codificado desconocido.

- Genera una ValueError si el fichero no ha podido ser abierto.

## Notas

> [!NOTE]
> Los espacios en blanco en las etiquetas `html` y `head` no son considerados significativos y pueden perder su formato.

## Véase también

Dom\HTMLDocument::createEmpty

Dom\HTMLDocument::createFromString
