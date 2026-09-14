---
title: match
source_url: https://www.php.net/manual/es/control-structures.match.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/control-structures/match.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 840bdb9be
order: 2210
---

## match

La expresión `match` permite realizar una evaluación basada en el control de identidad de un valor. De manera similar a una instrucción `switch`, una expresión `match` tiene una expresión sujeto que es comparada con varias alternativas. A diferencia de `switch`, se evalúa a un valor, como las expresiones ternarias. A diferencia de `switch`, la comparación es una verificación de identidad (`===`) en lugar de un control de igualdad débil (`==`). Las expresiones Match están disponibles a partir de PHP 8.0.0.

Estructura de una expresión `match`

```php
<?php
$return_value = match (subject_expression) {
    single_conditional_expression => return_expression,
    conditional_expression1, conditional_expression2 => return_expression,
};
?>

  
```

Uso básico de las expresiones `match`

```php
<?php
$food = 'cake';

$return_value = match ($food) {
    'apple' => 'This food is an apple',
    'bar' => 'This food is a bar',
    'cake' => 'This food is a cake',
};

var_dump($return_value);
?>

  
```

El ejemplo anterior mostrará:

    string(19) "This food is a cake"

Ejemplo de uso de `match` con operadores de comparación

```php
<?php
$age = 18;

$output = match (true) {
    $age < 2 => "Bebé",
    $age < 13 => "Niño",
    $age <= 19 => "Adolescente",
    $age >= 40 => "Adulto",
    $age > 19 => "Adulto joven",
};

var_dump($output);
?>

  
```

El ejemplo anterior mostrará:

    string(12) "Adolescente"

> [!NOTE]
> El resultado de una expresión `match` no necesita ser utilizado.

> [!NOTE]
> Cuando una expresión `match` se utiliza como una expresión autónoma, *debe* ser terminada por un punto y coma `;`.

La expresión `match` es similar a una instrucción `switch` pero presenta algunas diferencias esenciales:

- Una expresión `match` compara los valores de manera estricta (`===`) y no de manera débil como lo hace la instrucción switch.

- Una expresión `match` devuelve un valor.

- Las expresiones `match` no pasan a los casos siguientes como lo hacen las instrucciones `switch`.

- Una expresión `match` debe ser exhaustiva.

Al igual que las instrucciones `switch`, las expresiones `match` se ejecutan brazo por brazo. Al principio, ningún código se ejecuta. Las expresiones condicionales solo se evalúan si todas las expresiones condicionales anteriores no coinciden con la expresión del sujeto. Solo la expresión de retorno correspondiente a la expresión condicional correspondiente será evaluada. Por ejemplo:

```php
<?php
$result = match ($x) {
    foo() => 'value',
    $this->bar() => 'value', // $this->bar() no es llamado si foo() === $x
    $this->baz => beep(), // beep() no es llamado a menos que $x === $this->baz
    // etc.
};
?>

   
```

Los brazos de la expresión de `match` pueden contener múltiples expresiones separadas por una coma. Se trata de un OU lógico y de una abreviación para múltiples brazos que utilizan la misma expresión como resultado.

```php
<?php
$result = match ($x) {
    // Este brazo
    $a, $b, $c => 5,
    // Es equivalente a estos tres brazos:
    $a => 5,
    $b => 5,
    $c => 5,
};
?>

   
```

El patrón `default` es un caso particular. Este patrón coincide con todo lo que no ha sido buscado previamente. Por ejemplo:

```php
<?php
$expressionResult = match ($condition) {
    1, 2 => foo(),
    3, 4 => bar(),
    default => baz(),
};
?>

   
```

> [!NOTE]
> El uso de múltiples patrones por defecto provocará un error `E_FATAL_ERROR`.

Una expresión `match` debe ser exhaustiva. Si la expresión no es tratada por ningún brazo de `match`, se lanza un error `UnhandledMatchError`.

Ejemplo de una expresión match no manejada

```php
<?php
$condition = 5;

try {
    match ($condition) {
        1, 2 => foo(),
        3, 4 => bar(),
    };
} catch (\UnhandledMatchError $e) {
    var_dump($e);
}
?>

  
```

El ejemplo anterior mostrará:

    object(UnhandledMatchError)#1 (7) {
      ["message":protected]=>
      string(33) "Unhandled match value of type int"
      ["string":"Error":private]=>
      string(0) ""
      ["code":protected]=>
      int(0)
      ["file":protected]=>
      string(9) "/in/ICgGK"
      ["line":protected]=>
      int(6)
      ["trace":"Error":private]=>
      array(0) {
      }
      ["previous":"Error":private]=>
      NULL
    }

## Uso de expresiones match para manejar controles de no identidad

Es posible utilizar una expresión `match` para tratar los casos condicionales de no identidad utilizando `true` como expresión sujeto.

Uso de una expresión match generalizada para realizar ramificaciones sobre rangos de enteros

```php
<?php

$age = 23;

$result = match (true) {
    $age >= 65 => 'senior',
    $age >= 25 => 'adult',
    $age >= 18 => 'young adult',
    default => 'kid',
};

var_dump($result);
?>

   
```

El ejemplo anterior mostrará:

    string(11) "young adult"

Uso de una expresión match generalizada para realizar ramificaciones sobre el contenido de una cadena de caracteres

```php
<?php

$text = 'Bienvenidos a nuestra casa';

$result = match (true) {
    str_contains($text, 'Welcome'), str_contains($text, 'Hello') => 'en',
    str_contains($text, 'Bienvenidos'), str_contains($text, 'Hola') => 'es',
    // ...
};

var_dump($result);
?>

   
```

El ejemplo anterior mostrará:

    string(2) "es"
