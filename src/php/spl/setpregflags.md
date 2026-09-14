---
title: RegexIterator::setPregFlags
description: Define los flags de la expresión regular
source_url: https://www.php.net/manual/es/regexiterator.setpregflags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/regexiterator/setpregflags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 83720
---

RegexIterator::setPregFlags

Define los flags de la expresión regular

## Descripción

```php
public RegexIterator::setPregFlags(int $pregFlags): void
```php

Define los flags de la expresión regular.

## Parámetros

`pregFlags`  
Los flags de la expresión regular. Ver el método RegexIterator::\_\_construct para una lista de todos los flags disponibles.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `RegexIterator::setPregFlags`

Crea un nuevo objeto RegexIterator que filtra todas las entradas cuyos claves comienzan por 'test'.

```
<?php
$test = array ('test 1', 'another test', 'test 123');

$arrayIterator = new ArrayIterator($test);
$regexIterator = new RegexIterator($arrayIterator, '/^test/', RegexIterator::GET_MATCH);

$regexIterator->setPregFlags(PREG_OFFSET_CAPTURE);

foreach ($regexIterator as $key => $value) {
    var_dump($value);
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(1) {
      [0]=>
      array(2) {
        [0]=>
        string(4) "test"
        [1]=>
        int(0)
      }
    }
    array(1) {
      [0]=>
      array(2) {
        [0]=>
        string(4) "test"
        [1]=>
        int(0)
      }
    }

## Véase también

RegexIterator::getPregFlags
