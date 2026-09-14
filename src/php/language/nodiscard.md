---
title: El atributo NoDiscard
source_url: https://www.php.net/manual/es/class.nodiscard.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/attributes/nodiscard.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: e7f89579e
order: 2940
---

## Introducción

Este atributo se puede utilizar para indicar que el valor de retorno de una función o de un método no debe ser descartado. Si el valor de retorno no se utiliza de ninguna manera, se emitirá una advertencia.

Esto es útil para funciones en las que no comprobar el valor de retorno es probablemente un error.

Para descartar intencionalmente el valor de retorno de dicha función, utilice la conversión (void) para suprimir la advertencia.

> [!NOTE]
> Dado que los atributos están diseñados para ser retrocompatibles, `#[\NoDiscard]` se puede añadir a funciones y métodos incluso cuando se soportan PHP 8.4 o versiones anteriores, simplemente no hará nada. En PHP 8.5 y superiores se emitirá una advertencia si el resultado no se utiliza. Para suprimir la advertencia sin usar `(void)`, que no es soportado antes de PHP 8.5, considere usar una variable como `$_`.

> [!NOTE]
> `#[\NoDiscard]` se aplica a la declaración de función o método específica sobre la que está escrito, y la advertencia se emite en función de la declaración que realmente se llama. Como resultado, añadir `#[\NoDiscard]` a un método de interfaz o a un método abstracto no emite ninguna advertencia, porque el método que se invoca es el método de implementación o de sobrescritura. Del mismo modo, un método que sobrescribe un método `#[\NoDiscard]` no emite la advertencia a menos que esté marcado él mismo con el atributo. Por el contrario, un método importado desde un trait conserva el atributo, porque el método del trait se copia en la clase que lo usa como si estuviera declarado allí.

## Sinopsis de la clase

\#\[\Attribute\]

final

NoDiscard

Propiedades

public

readonly

string

null

message

Métodos

## Propiedades

`message`  
Un mensaje opcional que explica por qué el valor de retorno no debe ser descartado.

## Ejemplos

Uso básico

```php
<?php

/**
 * Processes all the given items and returns an array with the results of the
 * operation for each item. `null` indicates success and an Exception indicates
 * an error. The keys of the result array match the keys of the $items array.
 *
 * @param array<string> $items
 * @return array<null|Exception>
 */
#[\NoDiscard("as processing might fail for individual items")]
function bulk_process(array $items): array {
    $results = [];

    foreach ($items as $key => $item) {
        if (\random_int(0, 9999) < 9999) {
            // Pretend to do something useful with $item,
            // which will succeed in 99.99% of cases.
            echo "Processing {$item}", PHP_EOL;
            $error = null;
        } else {
            $error = new \Exception("Failed to process {$item}.");
        }

        $results[$key] = $error;
    }

    return $results;
}

bulk_process($items);

?>

    
```

La salida del ejemplo anterior en PHP 8.5 es similar a:

    Warning: The return value of function bulk_process() should either be used or intentionally ignored by casting it as (void), as processing might fail for individual items

Descartar intencionalmente el valor de retorno

```php
<?php

#[\NoDiscard]
function some_command(): int {
    return 1;
}

// Suprimir la advertencia usando (void) - PHP 8.5+
(void) some_command();

// Para compatibilidad con versiones de PHP anteriores a 8.5, usar una variable temporal
$_ = some_command();

?>

    
```

## Véase también

Visión general de los atributos
