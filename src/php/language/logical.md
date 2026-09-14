---
title: Los operadores lógicos
source_url: https://www.php.net/manual/es/language.operators.logical.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/operators/logical.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 43d07782b
order: 2740
---

## Los operadores lógicos

| Ejemplo | Nombre | Resultado |
|----|----|----|
| \$a and \$b | And (Y) | `true` si `$a` Y `$b` valen `true`. |
| \$a or \$b | Or (O) | `true` si `$a` O `$b` valen `true`. |
| \$a xor \$b | XOR | `true` si `$a` O `$b` es `true`, pero no ambos a la vez. |
| ! \$a | Not (No) | `true` si `$a` no es `true`. |
| \$a && \$b | And (Y) | `true` si `$a` Y `$b` son `true`. |
| \$a \|\| \$b | Or (O) | `true` si `$a` O `$b` es `true`. |

Los operadores lógicos

La razón por la cual existen dos tipos de "Y" y de "O" es que tienen diferentes prioridades. Ver el párrafo [precedencia de operadores](#language.operators.precedence).

Ilustración de los operadores lógicos

```php
<?php

// --------------------
// foo() nunca será llamada, ya que estos operadores se anulan

$a = (false && foo());
$b = (true  || foo());
$c = (false and foo());
$d = (true  or  foo());

// --------------------
// "||" tiene una precedencia superior a "or"

// El resultado de la expresión (false || true) es asignado a $e
// Actúa como: ($e = (false || true))
$e = false || true;

// La constante false es asignada a $f antes de que aparezca la operación "or"
// Actúa como: (($f = false) or true)
$f = false or true;

var_dump($e, $f);

// --------------------
// "&&" tiene una precedencia superior a "and"

// El resultado de la expresión (true && false) es asignado a $g
// Actúa como: ($g = (true && false))
$g = true && false;

// La constante true es asignada a $h antes de que aparezca la operación "and"
// Actúa como: (($h = true) and false)
$h = true and false;

var_dump($g, $h);
?>

  
```

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(false)
    bool(false)
    bool(true)
