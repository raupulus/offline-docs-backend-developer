---
title: Fibers
source_url: https://www.php.net/manual/es/language.fibers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/fibers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 376d3f9c2
order: 2340
---

## Fibers

## Descripción general de Fibers

Los Fibers representan funciones de pila completa e interrumpibles. Los Fibers pueden suspenderse desde cualquier lugar en la pila de llamadas, pausando su ejecución dentro del Fiber hasta que se reanude más tarde.

Los Fibers pausan toda la pila de ejecución, por lo que el llamador directo de la función no necesita cambiar la forma en que invoca la función

La ejecución puede interrumpirse en cualquier lugar de la pila de llamadas utilizando Fiber::suspend (es decir, la llamada a Fiber::suspend puede estar en una función profundamente anidada o incluso no existir en absoluto)

A diferencia de los `Generator`s sin pila, cada `Fiber` tiene su propia pila de llamadas, lo que permite que se pausen dentro de llamadas a funciones profundamente anidadas. Una función que declara un punto de interrupción (es decir, que llama a Fiber::suspend) no necesita cambiar su tipo de retorno, a diferencia de una función que utiliza [`yield`](#control-structures.yield) y debe devolver una instancia de `Generator`.

Los Fibers pueden suspenderse en cualquier llamada a función, incluidas aquellas realizadas desde la Máquina Virtual de PHP, como las funciones proporcionadas a `array_map` o los métodos llamados por [`foreach`](#control-structures.foreach) en un objeto `Iterator`.

Una vez suspendido, la ejecución del Fiber puede reanudarse con cualquier valor utilizando Fiber::resume o lanzando una excepción en el Fiber utilizando Fiber::throw. El valor se devuelve (o la excepción se lanza) desde Fiber::suspend.

> [!NOTE]
> Antes de PHP 8.4.0, no se permitía cambiar Fibers durante la ejecución de un [destructor](#language.oop5.decon.destructor) de objeto.

Uso básico

```php
    
<?php
$fiber = new Fiber(function (): void {
   $value = Fiber::suspend('fiber');
   echo "Valor utilizado para reanudar el Fiber: ", $value, PHP_EOL;
});

$value = $fiber->start();

echo "Valor del Fiber al suspenderse: ", $value, PHP_EOL;

$fiber->resume('test');
?>

   
```

El ejemplo anterior mostrará:

        
    Valor del Fiber al suspenderse: fiber
    Valor utilizado para reanudar el Fiber: test
