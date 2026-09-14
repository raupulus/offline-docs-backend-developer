---
title: SimpleXMLElement::__construct
description: Crea un nuevo objeto SimpleXMLElement
source_url: https://www.php.net/manual/es/simplexmlelement.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: c1f37a6c2
order: 74480
---

SimpleXMLElement::\_\_construct

Crea un nuevo objeto SimpleXMLElement

## Descripción

```php
public SimpleXMLElement::__construct(string $data, [int $options], [bool $dataIsURL], [string $namespaceOrPrefix], [bool $isPrefix])
```php

Crea un nuevo objeto `SimpleXMLElement`.

## Parámetros

`data`  
Una cadena XML bien formada o la ruta de acceso o un URL que apunta a un documento XML si `dataIsURL` vale `true`.

`options`  
Opcionalmente utilizado para especificar [parámetros adicionales de Libxml](#libxml.constants), que afectan la lectura de documentos XML. Las opciones que afectan la salida de los documentos XML (por ejemplo `LIBXML_NOEMPTYTAG`) son ignoradas silenciosamente.

> [!NOTE]
> Puede ser necesario pasar `LIBXML_PARSEHUGE` para poder tratar nodos de texto profundamente anidados o muy voluminosos.

`dataIsURL`  
Por omisión, `dataIsURL` vale `false`. Utilice `true` para especificar que el parámetro `data` es una ruta de acceso o un URL que apunta a un documento XML en lugar de una cadena de datos.

`namespaceOrPrefix`  
Prefijo de espacio de nombres o URI.

`isPrefix`  
`true` si `namespaceOrPrefix` es un prefijo, `false` en caso contrario. Valor por omisión: `false`.

## Errores/Excepciones

Produce un mensaje de error de tipo `E_WARNING` para cada error encontrado en los datos XML y lanza también una `exception` si los datos XML no pueden ser analizados.

> [!TIP]
> Utilice la función `libxml_use_internal_errors` para suprimir todos los errores XML y la función `libxml_get_errors` para recorrerlos.

## Ejemplos

> [!NOTE]
> Los ejemplos listados incluyen a veces `examples/simplexml-data.php`, esto hace referencia a la cadena XML del primer ejemplo de [el uso básico](#simplexml.examples-basic).

Crea un objeto SimpleXMLElement

```
<?php

include 'examples/simplexml-data.php';

$sxe = new SimpleXMLElement($xmlstr);
echo $sxe->movie[0]->title;

?>

    
```php

El ejemplo anterior mostrará:

    PHP: Behind the Parser

Crea un objeto SimpleXMLElement a partir de un URL

```
<?php

$sxe = new SimpleXMLElement('http://example.org/document.xml', 0, true);
echo $sxe->asXML();

?>

    
```php

## Véase también

[???](#simplexml.examples-basic), `simplexml_load_string`, `simplexml_load_file`, [???](#simplexml.examples-errors), `libxml_use_internal_errors`, `libxml_set_streams_context`
