---
title: RegexIterator::setFlags
description: Establece las flags
source_url: https://www.php.net/manual/es/regexiterator.setflags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/regexiterator/setflags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 83700
---

RegexIterator::setFlags

Establece las flags

## Descripción

```php
public RegexIterator::setFlags(int $flags): void
```php

Establece las flags.

## Parámetros

`flags`  
Las flags a establecer, un bitmask de constantes de la clase.

Las flags disponibles se enumeran a continuación. El verdadero significado de estas flags se describe en las [Constantes predefinidas](#regexiterator.constants).

| value | constant                                                   |
|-------|------------------------------------------------------------|
| 1     | [RegexIterator::USE_KEY](#regexiterator.constants.use-key) |

Flags `RegexIterator`

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de RegexIterator::setFlags

Crear un nuevo RegexIterator que filtre todas las entradas que empiecen con la palabra clave '`test`'.

```
<?php
$test = array ('str1' => 'test 1', 'teststr2' => 'otro test', 'str3' => 'test 123');

$arrayIterator = new ArrayIterator($test);
$regexIterator = new RegexIterator($arrayIterator, '/^test/');
$regexIterator->setFlags(RegexIterator::USE_KEY);

foreach ($regexIterator as $clave => $valor) {
    echo $clave . ' => ' . $valor . "\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    teststr2 => otro test

## Véase también

RegexIterator::getFlags
