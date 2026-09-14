---
title: Operadores de string
source_url: https://www.php.net/manual/es/language.operators.string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/operators/string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 16934048f
order: 2760
---

## Operadores de string

Existen dos operadores de string `string`. El primero es el operador de concatenación ('.'), que devuelve la concatenación de sus dos argumentos. El segundo es el operador de asignación concatenante (`.=`). Ver [operadores de asignación](#language.operators.assignment) para más detalles.

Concatenación de string

```php
<?php
$a = "Hello ";
$b = $a . "World!"; // $b contiene ahora "Hello World!"
var_dump($b);

$a = "Hello ";
$a .= "World!";     // $a contiene ahora "Hello World!"
var_dump($a);
?>

   
```

## Véase también

[El tipo string](#language.types.string), [Las funciones de string](#ref.strings)
