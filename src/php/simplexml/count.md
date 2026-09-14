---
title: SimpleXMLElement::count
description: Cuenta el número de hijos para un elemento
source_url: https://www.php.net/manual/es/simplexmlelement.count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simplexml/simplexmlelement/count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simplexml
translation_status: ready
translation_reviewed: false
translation_revision: 770c6faca
order: 74490
---

SimpleXMLElement::count

Cuenta el número de hijos para un elemento

## Descripción

```php
public SimpleXMLElement::count(): int
```php

Este método cuenta el número de hijos de un elemento.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de hijos de un elemento.

## Ejemplos

Conteo del número de hijos

```
<?php
$xml = <<<EOF
<people>
 <person name="Person 1">
  <child/>
  <child/>
  <child/>
 </person>
 <person name="Person 2">
  <child/>
  <child/>
  <child/>
  <child/>
  <child/>
 </person>
</people>
EOF;

$elem = new SimpleXMLElement($xml);

foreach ($elem as $person) {
    printf("%s has got %d children.\n", $person['name'], $person->count());
}
?>

    
```php

El ejemplo anterior mostrará:

    Person 1 has got 3 children.
    Person 2 has got 5 children.

## Véase también

SimpleXMLElement::children
