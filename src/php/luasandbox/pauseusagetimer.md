---
title: LuaSandbox::pauseUsageTimer
description: Pausa el temporizador de uso de la CPU
source_url: https://www.php.net/manual/es/luasandbox.pauseusagetimer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/luasandbox/luasandbox/pauseusagetimer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: luasandbox
translation_status: ready
translation_reviewed: false
translation_revision: 9c40251a8
order: 44010
---

LuaSandbox::pauseUsageTimer

Pausa el temporizador de uso de la CPU

## Descripción

```php
public LuaSandbox::pauseUsageTimer(): bool
```php

Pausa el temporizador de uso de la CPU.

Esto solo tiene efecto cuando se llama desde una retrollamada de Lua. Cuando la ejecución vuelve a Lua, el temporizador se reiniciará automáticamente. Si se realiza una nueva llamada a Lua, el temporizador se reiniciará durante la duración de esa llamada.

Si una retrollamada PHP llama nuevamente a Lua con el temporizador sin pausar, y esa función Lua llama nuevamente a PHP, la segunda llamada PHP no podrá pausar el temporizador. La lógica es que incluso si la segunda llamada PHP evita contar el uso de la CPU contra el límite, la primera llamada sigue contándolo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `bool` indicando si el temporizador está ahora en pausa.

## Ejemplos

Manipulando el temporizador de uso

```
<?php

// Crear un nuevo LuaSandbox y definir un límite de CPU
$sandbox = new LuaSandbox();
$sandbox->setCPULimit( 1 );

function doWait( $t ) {
    $end = microtime( true ) + $t;
    while ( microtime( true ) < $end ) {
        // gasta ciclos de CPU
    }
}

// Registrar una función de retrollamada PHP
$sandbox->registerLibrary( 'php', [
    'test' => function () use ( $sandbox ) {
        $sandbox->pauseUsageTimer();
        doWait( 5 );

        $sandbox->unpauseUsageTimer();
        doWait( 0.1 );
    },
    'test2' => function () use ( $sandbox ) {
        $sandbox->pauseUsageTimer();
        $sandbox->unpauseUsageTimer();
        doWait( 1.1 );
    }
] );

echo "Esto no debería agotar el tiempo...\n";
$sandbox->loadString( 'php.test()' )->call();

echo "Esto debería agotar el tiempo.\n";
try {
    $sandbox->loadString( 'php.test2()' )->call();
    echo "¿No lo hizo?\n";
} catch ( LuaSandboxTimeoutError $ex ) {
    echo "¡Lo hizo! " . $ex->getMessage() . "\n";
}

?>

   
```php

El ejemplo anterior mostrará:

    Esto no debería agotar el tiempo...
    Esto debería agotar el tiempo.
    ¡Lo hizo! El tiempo máximo de ejecución para este script fue excedido

## Véase también

LuaSandbox::setCPULimit

LuaSandbox::unpauseUsageTimer
