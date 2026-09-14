---
title: parallel\Runtime::run
description: Ejecución
source_url: https://www.php.net/manual/es/parallel-runtime.run.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/runtime/run.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60200
---

parallel\Runtime::run

Ejecución

## Descripción

```php
public parallel\Runtime::run(Closure $task): Future
```php

Planifica `task` para la ejecución en paralelo.

```php
public parallel\Runtime::run(Closure $task, array $argv): Future
```

Planifica `task` para la ejecución en paralelo, pasando `argv` en el momento de la ejecución.

## Parámetros

`task`  
Una `Closure` con características específicas.

`argv`  
Un `array` de argumentos con características específicas para pasar a `task` en el momento de la ejecución.

## Características de la tarea

Las cierres planificadas para la ejecución en paralelo no deben: aceptar o devolver por referencia, aceptar o devolver objetos internos (ver notas), ejecutar un conjunto limitado de instrucciones

Las instrucciones prohibidas en los cierres destinados a la ejecución en paralelo son: yield, usar by-reference, declarar clases, declarar funciones nombradas

> [!NOTE]
> Los cierres anidados pueden usar yield o by-reference, pero no deben contener declaraciones de clases o funciones nombradas.

> [!NOTE]
> Ninguna instrucción está prohibida en los ficheros que la tarea puede incluir.

## Características de los argumentos

Los argumentos no deben: contener referencias, contener recursos, contener objetos internos (ver notas)

> [!NOTE]
> En el caso de los recursos de flujo de ficheros, el recurso será convertido en descriptor de fichero y pasado en `int` si es posible, esto no está soportado en Windows.

## Notas sobre los objetos internos

Los objetos internos utilizan generalmente una estructura personalizada que no puede ser copiada de manera segura por valor, PHP carece actualmente de mecanismos para hacerlo (sin serialización) y por lo tanto solo los objetos que no utilizan una estructura personalizada pueden ser compartidos.

Algunos objetos internos no utilizan una estructura personalizada, por ejemplo `parallel\Events\Event` y por lo tanto pueden ser compartidos.

Los cierres son un tipo especial de objeto interno y soportan ser copiados por valor, y por lo tanto pueden ser compartidos.

Los canales son centrales para la escritura de código paralelo y soportan el acceso y la ejecución concurrentes por necesidad, y por lo tanto pueden ser compartidos.

> [!WARNING]
> Una clase de usuario que extiende una clase interna puede usar una estructura personalizada tal como está definida por la clase interna, en cuyo caso no puede ser copiada de manera segura por valor, y por lo tanto no puede ser compartida.

## Valores devueltos

> [!WARNING]
> El `Future` devuelto no debe ser ignorado cuando la tarea contiene una declaración de retorno o de lanzamiento.

## Excepciones

> [!WARNING]
> Lanza una `parallel\Runtime\Error\Closed` si `parallel\Runtime` estaba cerrado.

> [!WARNING]
> Lanza una `parallel\Runtime\Error\IllegalFunction` si `task` es un cierre creado a partir de una función interna.

> [!WARNING]
> Lanza una `parallel\Runtime\Error\IllegalInstruction` si `task` contiene instrucciones ilegales.

> [!WARNING]
> Lanza una `parallel\Runtime\Error\IllegalParameter` si `task` acepta o `argv` contiene variables ilegales.

> [!WARNING]
> Lanza una `parallel\Runtime\Error\IllegalReturn` si `task` devuelve de manera ilegal.
