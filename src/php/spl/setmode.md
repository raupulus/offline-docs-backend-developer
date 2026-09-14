---
title: RegexIterator::setMode
description: Establece el modo de operación
source_url: https://www.php.net/manual/es/regexiterator.setmode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/regexiterator/setmode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 83710
---

RegexIterator::setMode

Establece el modo de operación

## Descripción

```php
public RegexIterator::setMode(int $mode): void
```php

Establecer el modo de operación.

## Parámetros

`mode`  
El modo de operación.

Los modos disponibles se enumeran a continuación. El verdadero significado de estos modos se describe en las [constantes predefinidas](#regexiterator.constants).

| value | constant                                                           |
|-------|--------------------------------------------------------------------|
| 0     | [RegexIterator::MATCH](#regexiterator.constants.match)             |
| 1     | [RegexIterator::GET_MATCH](#regexiterator.constants.get-match)     |
| 2     | [RegexIterator::ALL_MATCHES](#regexiterator.constants.all-matches) |
| 3     | [RegexIterator::SPLIT](#regexiterator.constants.split)             |
| 4     | [RegexIterator::REPLACE](#regexiterator.constants.replace)         |

Modos `RegexIterator`

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de RegexIterator::setMode

```
<?php
$test = array ('str1' => 'test 1', 'test str2' => 'otro test', 'str3' => 'test 123');

$arrayIterator = new ArrayIterator($test);
// Filtra todo lo que empiece con 'test ' seguido por uno o más números.
$regexIterator = new RegexIterator($arrayIterator, '/^test (\d+)/');
// Modo de operación: Reemplaza el valor actual con las coincidencias
$regexIterator->setMode(RegexIterator::GET_MATCH);

foreach ($regexIterator as $clave => $valor) {
    // imprime el o los números que coincidan
    echo $key . ' => ' . $value[1] . PHP_EOL;
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    str1 => 1
    str3 => 123

## Véase también

RegexIterator::getMode
