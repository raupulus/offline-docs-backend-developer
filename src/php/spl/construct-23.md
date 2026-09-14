---
title: RegexIterator::__construct
description: Crea un nuevo RegexIterator
source_url: https://www.php.net/manual/es/regexiterator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/regexiterator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: c142be811
order: 83650
---

RegexIterator::\_\_construct

Crea un nuevo RegexIterator

## Descripción

```php
public RegexIterator::__construct(Iterator $iterator, string $pattern, [int $mode], [int $flags], [int $pregFlags])
```php

Crea un nuevo `RegexIterator` que filtra un Iterator usando una expresión regular.

## Parámetros

`iterator`  
El iterador al que se le va a aplicar el filtro regex.

`pattern`  
la expresión regular a coincidir.

`mode`  
Modo de operación, véase RegexIterator::setMode para una lista de todos los modos.

`flags`  
Flags especiales, véase RegexIterator::setFlags para una lista de todas las flags disponibles.

`pregFlags`  
Las flags de expresión regular. Estas flags dependen de el parámetro de modo de operación.

| operation mode               | available flags         |
|------------------------------|-------------------------|
| `RegexIterator::ALL_MATCHES` | Véase `preg_match_all`. |
| `RegexIterator::GET_MATCH`   | Véase `preg_match`.     |
| `RegexIterator::MATCH`       | Véase `preg_match`.     |
| `RegexIterator::REPLACE`     | Nada.                   |
| `RegexIterator::SPLIT`       | Véase `preg_split`.     |

`RegexIterator` preg_flags

## Errores/Excepciones

Lanza una `InvalidArgumentException` si el argumento `pattern` es inválido.

## Ejemplos

Ejemplo de `RegexIterator::__construct`

Crea un nuevo RegexIterator que filtra todos los string que empiezan con 'test'.

```
<?php
$arrayIterator = new ArrayIterator(array('test 1', 'another test', 'test 123'));
$regexIterator = new RegexIterator($arrayIterator, '/^test/');

foreach ($regexIterator as $value) {
    echo $value . "\n";
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    test 1
    test 123

## Véase también

`preg_match`, `preg_match_all`, `preg_replace`, `preg_split`
