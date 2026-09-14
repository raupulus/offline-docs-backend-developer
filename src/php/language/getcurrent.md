---
title: Closure::getCurrent
description: Devuelve la closure actualmente en ejecución
source_url: https://www.php.net/manual/es/closure.getcurrent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/closure/getcurrent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 31e56c25f
order: 3090
---

Closure::getCurrent

Devuelve la closure actualmente en ejecución

## Descripción

```php
public static Closure::getCurrent(): Closure
```php

Devuelve la closure actualmente en ejecución. Este método es principalmente útil para implementar closures recursivas sin necesidad de capturar una referencia a la variable de la closure usando la palabra clave `use`.

Este método debe ser llamado desde dentro de una closure; llamarlo fuera de un contexto de closure resultará en `Error: Current function is not a closure.`

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la instancia de `Closure` actualmente en ejecución.

## Errores/Excepciones

Lanza un `Error` si se llama fuera de un contexto de closure.

## Ejemplos

Ejemplo de Closure::getCurrent

Uso de Closure::getCurrent para implementar una función de Fibonacci recursiva:

```
<?php
$fibonacci = function (int $n) {
    if ($n === 0 || $n === 1) {
        return $n;
    }

    $fn = Closure::getCurrent();
    return $fn($n - 1) + $fn($n - 2);
};

echo $fibonacci(10); // Muestra: 55
?>

   
```php

Comparación con el enfoque tradicional

Antes de PHP 8.5, implementar closures recursivas requería capturar una referencia a la variable de la closure usando la palabra clave `use`:

```
<?php
// Enfoque tradicional (aún funciona en PHP 8.5)
$fibonacci = function (int $n) use (&$fibonacci) {
    if ($n === 0) return 0;
    if ($n === 1) return 1;
    return $fibonacci($n - 1) + $fibonacci($n - 2);
};

echo $fibonacci(10); // Muestra: 55
?>

   
```php

El enfoque con Closure::getCurrent elimina la necesidad de declarar la variable con una referencia en la cláusula `use`, lo que hace el código más limpio y menos propenso a errores.
