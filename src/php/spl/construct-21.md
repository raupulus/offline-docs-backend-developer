---
title: RecursiveRegexIterator::__construct
description: Crea un nuevo RecursiveRegexIterator
source_url: https://www.php.net/manual/es/recursiveregexiterator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/recursiveregexiterator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: c142be811
order: 83410
---

RecursiveRegexIterator::\_\_construct

Crea un nuevo RecursiveRegexIterator

## Descripción

```php
public RecursiveRegexIterator::__construct(RecursiveIterator $iterator, string $pattern, [int $mode], [int $flags], [int $pregFlags])
```php

Crea un nuevo iterador de expresión regular.

## Parámetros

`iterator`  
El iterador recursivo al que se le va a aplicar el filtro regex.

`pattern`  
La expresión regular a coincidir.

`mode`  
Modo de operación, véase RegexIterator::setMode para una lista de todos los modos.

`flags`  
Flags especiales, véase RegexIterator::setFlags para una lista de todas las flags disponibles.

`pregFlags`  
Las flags de expresión regular. De estas flags depende el parámetro de modo de funcionamiento.

| Modo de operación                     | flags disponibles       |
|---------------------------------------|-------------------------|
| `RecursiveRegexIterator::ALL_MATCHES` | Véase `preg_match_all`. |
| `RecursiveRegexIterator::GET_MATCH`   | Véase `preg_match`.     |
| `RecursiveRegexIterator::MATCH`       | Véase `preg_match`.     |
| `RecursiveRegexIterator::REPLACE`     | nada.                   |
| `RecursiveRegexIterator::SPLIT`       | Véase `preg_split`.     |

`RegexIterator` preg_flags

## Ejemplos

Ejemplo de `RecursiveRegexIterator::__construct`

Crear un nuevo RegexIterator que filtre todos los string que empiezan con 'test'

```
<?php
$rArrayIterator = new RecursiveArrayIterator(array('test1', array('tet3', 'test4', 'test5')));
$rRegexIterator = new RecursiveRegexIterator($rArrayIterator, '/^test/',
    RecursiveRegexIterator::ALL_MATCHES);

foreach ($rRegexIterator as $key1 => $value1) {

    if ($rRegexIterator->hasChildren()) {

        // print all children
        echo "Hijos: ";
        foreach ($rRegexIterator->getChildren() as $key => $value) {
            echo $value . " ";
        }
        echo "\n";
    } else {
        echo "No tiene hijos\n";
    }

}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    No tiene hijos
    Hijos: test4 test5

## Véase también

`preg_match`, `preg_match_all`, `preg_replace`, `preg_split`
