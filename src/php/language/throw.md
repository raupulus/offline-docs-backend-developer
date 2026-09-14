---
title: Fiber::throw
description: Reanuda la ejecución de la fibra con una excepción
source_url: https://www.php.net/manual/es/fiber.throw.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/fiber/throw.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: b3a0b9924
order: 3510
---

Fiber::throw

Reanuda la ejecución de la fibra con una excepción

## Descripción

```php
public Fiber::throw(Throwable $exception): mixed
```php

Reanuda la fibra lanzando la excepción dada desde la llamada Fiber::suspend en curso.

Si la fibra no está suspendida cuando se llama a este método, se emitirá una excepción `FiberError`.

## Parámetros

`exception`  
La excepción a lanzar en la fibra desde la llamada Fiber::suspend en curso.

## Valores devueltos

El valor proporcionado en la próxima llamada a Fiber::suspend o `null` si la fibra retorna. Si la fibra lanza una excepción antes de suspenderse, será emitida al llamar a este método.

## Ejemplos

```
<?php

$fiber = new Fiber(function () {
   try {
       // Suspende la ejecución de la fibra declarando un punto de interrupción
       Fiber::suspend();
   } catch (Throwable $e) {
       echo $e->getMessage();
   }
});

$fiber->start();

// Reanuda la ejecución de la fibra pasando
// la Excepción a lanzar en el punto de interrupción
$fiber->throw(new Exception('Mensaje de una excepción lanzada en el punto de interrupción actual'));

?>

   
```php

Resultado del ejemplo anterior es similar a:

    Mensaje de una excepción lanzada en el punto de interrupción actual
