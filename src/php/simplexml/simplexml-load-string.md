---
title: simplexml_load_string
description: Interpreta un string XML en un objeto
source_url: https://www.php.net/manual/es/function.simplexml-load-string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/functions/simplexml-load-string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_revision: c142be811
order: 74410
---

simplexml_load_string

Interpreta un string XML en un objeto

## Descripción

```php
simplexml_load_string(string $data, [string $class_name], [int $options], [string $namespace_or_prefix], [bool $is_prefix]): SimpleXMLElement
```php

Convierte la cadena XML `data` y devuelve un objeto de la clase `SimpleXMLElement`.

## Parámetros

`data`  
Una cadena XML válida

`class_name`  
Puede utilizarse el parámetro opcional y, así, la función `simplexml_load_string` devolverá un objeto de la clase especificada. Esta clase debe extender la clase `SimpleXMLElement`.

`options`  
[Operación a nivel de bits `OR`](#language.operators.bitwise) de las [constantes de opción libxml](#libxml.constants).

`namespace_or_prefix`  
Prefijo o URI del espacio de nombres.

`is_prefix`  
`true` si `namespace_or_prefix` es un prefijo, `false` si es la URI.

## Valores devueltos

Devuelve un `object` de la clase `SimpleXMLElement` cuyas propiedades contienen los datos del documento XML, o `false` si ocurre un error.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Errores/Excepciones

Produce un mensaje de error de nivel `E_WARNING` para cada error encontrado en los datos XML.

> [!TIP]
> Utilice la función `libxml_use_internal_errors` para suprimir todos los errores XML, y la función `libxml_get_errors` para recorrerlos.

## Ejemplos

Convertir una cadena XML

```
<?php
$string = <<<XML

<document>
 <title>Forty What?</title>
 <from>Joe</from>
 <to>Jane</to>
 <body>
  I know that's the answer -- but what's the question?
 </body>
</document>
XML;

$xml = simplexml_load_string($string);

print_r($xml);
?>

    
```php

El ejemplo anterior mostrará:

    SimpleXMLElement Object
    (
      [title] => Forty What?
      [from] => Joe
      [to] => Jane
      [body] =>
       I know that's the answer -- but what's the question?
    )

        

A partir de ahí, puede utilizarse `$xml->body` y cualquier otro elemento.

## Véase también

`simplexml_load_file`, SimpleXMLElement::\_\_construct, [???](#simplexml.examples-errors), `libxml_use_internal_errors`, [???](#simplexml.examples-basic)
