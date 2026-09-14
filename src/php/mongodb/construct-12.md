---
title: MongoDB\BSON\Regex::__construct
description: Construye una nueva REGEX
source_url: https://www.php.net/manual/es/mongodb-bson-regex.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/regex/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48270
---

MongoDB\BSON\Regex::\_\_construct

Construye una nueva REGEX

## Descripción

```php
final public MongoDB\BSON\Regex::__construct(string $pattern, [string $flags])
```php

## Parámetros

`pattern` (`string`)  
La máscara de la expresión regular.

> [!NOTE]
> La máscara no debe estar rodeada de caracteres delimitadores.

`flags` (`string`)  
Los [ flags de la expresión regular](https://www.mongodb.com/docs/manual/reference/operator/query/regex/#op._S_options).

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

si

pattern

o

flags

contiene un byte nulo.

## Historial de cambios

<table>
<thead>
<tr>
<th>Versión</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>PECL mongodb 1.2.0</td>
<td><p>El argumento <code>flags</code> es opcional y el valor por omisión es una cadena vacía.</p>
<p>Los caracteres en el argumento <code>flags</code> serán ordenados alfabéticamente cuando se construya una Regex. Anteriormente, los caracteres se almacenaban en el orden proporcionado.</p>
<p><code>MongoDB\Driver\Exception\InvalidArgumentException</code> es lanzada si <code>pattern</code> o <code>flags</code> contiene un byte nulo. Anteriormente, los valores eran truncados en el primer byte nulo.</p></td>
</tr>
</tbody>
</table>

## Ejemplos

`MongoDB\BSON\Regex::__construct` ejemplo

```
<?php

$regex = new MongoDB\BSON\Regex('^foo', 'i');
var_dump($regex);

?>

   
```php

El ejemplo anterior mostrará:

    object(MongoDB\BSON\Regex)#1 (2) {
      ["pattern"]=>
      string(4) "^foo"
      ["flags"]=>
      string(1) "i"
    }

## Véase también

Los tipos BSON

Los flags soportados para las expresiones regulares
