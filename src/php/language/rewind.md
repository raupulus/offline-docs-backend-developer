---
title: Generator::rewind
description: Ejecuta el generador hasta e incluyendo el primer yield
source_url: https://www.php.net/manual/es/generator.rewind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/generator/rewind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 5e6944e79
order: 3590
---

Generator::rewind

Ejecuta el generador hasta e incluyendo el primer yield

## Descripción

```php
public Generator::rewind(): void
```php

Ejecuta el generador hasta e incluyendo el *primer* [`yield`](#control-structures.yield). Si el generador ya está en el *primer* [`yield`](#control-structures.yield), no se realizará ninguna acción. Si el generador ha avanzado más allá de una expresión [`yield`](#control-structures.yield), este método lanzará una `Exception`.

> [!NOTE]
> Se trata del método *primero* llamado al inicio de un ciclo [`foreach`](#control-structures.foreach). *No* se *ejecutará* *después* de los ciclos [`foreach`](#control-structures.foreach).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de Generator::rewind

```
<?php

function generator(): Generator
{
    echo "¡Soy un generador!\n";

    for ($i = 1; $i <= 3; $i++) {
        yield $i;
    }
}

// Inicializar el generador
$generator = generator();

// Devolver el generador al inicio de la primera expresión yield,
// si no lo está ya
$generator->rewind(); // ¡Soy un generador!

// No ocurre nada aquí; el generador ya está reiniciado
$generator->rewind(); // Sin salida (NULL)

// Esto devuelve el generador al inicio de la primera expresión yield,
// si no lo está ya, e itera sobre el generador
foreach ($generator as $value) {
    // Después de devolver el primer valor, el generador permanece en
    // la primera expresión yield hasta que se reanude la ejecución y avance a la siguiente yield
    echo $value, PHP_EOL; // 1

    break;
}

// Reanudar y reiniciar nuevamente. No se produce ningún error ya que el generador no ha avanzado más allá del primer yield
$generator->rewind();

echo $generator->current(), PHP_EOL; // 1

// No se produce ningún error, el generador sigue en la primera yield
$generator->rewind();

// Esto hace avanzar el generador a la segunda expresión yield
$generator->next();

try {
    // Esto lanzará una excepción,
    // ya que el generador ya ha avanzado a la segunda yield
    $generator->rewind(); // Error fatal: Exception no capturada: No se puede devolver un generador que ya ha sido ejecutado
} catch (Exception $e) {
    echo $e->getMessage();
}

?>

    
```php

El ejemplo anterior mostrará:

    ¡Soy un generador!
    1
    1
    No se puede devolver un generador que ya ha sido ejecutado
