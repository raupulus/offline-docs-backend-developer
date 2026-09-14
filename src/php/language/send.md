---
title: Generator::send
description: Enviar un valor al generador
source_url: https://www.php.net/manual/es/generator.send.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/generator/send.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 8fee3ae97
order: 3600
---

Generator::send

Enviar un valor al generador

## Descripción

```php
public Generator::send(mixed $value): mixed
```php

Envía el valor dado al generador como resultado de la expresión [`yield`](#control-structures.yield) actual y reanuda la ejecución del generador.

Si el generador no es una expresión [`yield`](#control-structures.yield) en el momento de invocar a este método, se permitirá avanzar a la primera expresión [`yield`](#control-structures.yield) antes de enviar el valor. Por tanto, no es necesario «preparar» generadores de PHP con una llamada a Generator::next (como se hace en Python).

## Parámetros

`value`  
El valor a enviar al generador. Este valor será el valor devuelto de la expresión [`yield`](#control-structures.yield) en la que está actualmente el generador.

## Valores devueltos

Devuelve el valor producido.

## Ejemplos

Empleo de Generator::send para inyectar valores

```
<?php
function printer() {
    echo "¡Soy una impresora!".PHP_EOL;
    while (true) {
        $string = yield;
        echo $string.PHP_EOL;
    }
}

$printer = printer();
$printer->send('¡Hola mundo!');
$printer->send('¡Adiós mundo!');
?>

    
```php

El ejemplo anterior mostrará:

    ¡Soy una impresora!
    ¡Hola mundo!
    ¡Adiós mundo!
