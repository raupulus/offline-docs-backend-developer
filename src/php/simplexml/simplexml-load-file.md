---
title: simplexml_load_file
description: Interpreta un fichero XML en un objeto
source_url: https://www.php.net/manual/es/function.simplexml-load-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/functions/simplexml-load-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_revision: c142be811
order: 74400
---

simplexml_load_file

Interpreta un fichero XML en un objeto

## Descripción

```php
simplexml_load_file(string $filename, [string $class_name], [int $options], [string $namespace_or_prefix], [bool $is_prefix]): SimpleXMLElement
```php

Convierte el documento XML `filename` en un objeto de tipo `SimpleXMLElement`.

## Parámetros

`filename`  
Ruta hacia el fichero XML

`class_name`  
Puede utilizarse este parámetro opcional, y así, la función `simplexml_load_file` devolverá un objeto de la clase especificada. Esta clase debe extender la clase `SimpleXMLElement`.

`options`  
[Operación a nivel de bits `OR`](#language.operators.bitwise) de las [constantes de opción libxml](#libxml.constants).

`namespace_or_prefix`  
Prefijo o la URI del espacio de nombres.

`is_prefix`  
`true` si `namespace_or_prefix` es un prefijo, `false` si es la URI; por omisión, `false`.

## Valores devueltos

Devuelve un `object` de la clase `SimpleXMLElement` cuyas propiedades contienen los datos del documento XML, o `false` si ocurre un error.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Errores/Excepciones

Genera un mensaje de error de nivel `E_WARNING` para cada error encontrado en los datos XML.

> [!TIP]
> Utilice la función `libxml_use_internal_errors` para suprimir todos los errores XML, y la función `libxml_get_errors` para recorrerlos.

## Ejemplos

Interpretación de un documento XML

```
<?php
// El fichero examples/book.xml contiene un documento XML con un elemento raíz
// y al menos un elemento /[raíz]/title.

if (file_exists('examples/book.xml')) {
    $xml = simplexml_load_file('examples/book.xml');

    print_r($xml);
} else {
    exit('Fallo al abrir el fichero examples/test.xml.');
}
?>

    
```php

Este script mostrará, en caso de éxito:

    SimpleXMLElement Object
    (
      [book] => Array
      ...
    )

        

A partir de ahí, puede utilizarse `$xml->title` y cualquier otro elemento.

## Véase también

`simplexml_load_string`, SimpleXMLElement::\_\_construct, [???](#simplexml.examples-errors), `libxml_use_internal_errors`, [???](#simplexml.examples-basic), `libxml_set_streams_context`
