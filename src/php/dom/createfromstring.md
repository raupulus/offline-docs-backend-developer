---
title: Dom\HTMLDocument::createFromString
description: Analiza un documento HTML a partir de un string
source_url: https://www.php.net/manual/es/dom-htmldocument.createfromstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/htmldocument/createfromstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: a8b6f4dd3
order: 12550
---

Dom\HTMLDocument::createFromString

Analiza un documento

HTML

a partir de un string

## Descripción

```php
public static Dom\HTMLDocument::createFromString(string $source, [int $options], [string $overrideEncoding]): Dom\HTMLDocument
```php

Analiza un documento HTML a partir de un string, según la norma vigente.

## Parámetros

`source`  
El string que contiene el HTML a analizar.

`options`  
[Operación a nivel de bits `OR`](#language.operators.bitwise) de las [constantes de opción libxml](#libxml.constants).

También es posible pasar `Dom\HTML_NO_DEFAULT_NS` para desactivar el uso del espacio de nombres HTML y del elemento template. Esto solo debería ser utilizado si las implicaciones son correctamente comprendidas.

`overrideEncoding`  
El codificado en el cual el documento fue creado. Si no se proporciona, intentará determinar el codificado más probable utilizado.

## Valores devueltos

El documento analizado en forma de una instancia de `Dom\HTMLDocument`.

## Errores/Excepciones

- Levanta una excepción ValueError si `options` contiene una opción inválida.

- Levanta una excepción ValueError si `overrideEncoding` utiliza un codificado desconocido.

## Ejemplos

Ejemplo de Dom\HTMLDocument::createFromString

Analiza un documento de ejemplo.

```
<?php
$dom = Dom\HTMLDocument::createFromString(<<<'HTML'
<!DOCTYPE html>
<html>
<body>
   <p>Hello, world!</p>
</body>
</html>
HTML);
echo $dom->saveHtml();
?>

   
```php

El ejemplo anterior mostrará:

    <!DOCTYPE html><html><head></head><body>
        <p>Hello, world!</p>

    </body></html>

## Notas

> [!NOTE]
> Los espacios en blanco en las etiquetas `html` y `head` no son considerados significativos y pueden perder su formato.

## Véase también

Dom\HTMLDocument::createEmpty

Dom\HTMLDocument::createFromFile
