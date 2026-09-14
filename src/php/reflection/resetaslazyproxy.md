---
title: ReflectionClass::resetAsLazyProxy
description: Reinicia un objeto y lo marca como perezoso
source_url: https://www.php.net/manual/es/reflectionclass.resetaslazyproxy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/resetaslazyproxy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c0fa5077c
order: 69660
---

ReflectionClass::resetAsLazyProxy

Reinicia un objeto y lo marca como perezoso

## Descripción

```php
public ReflectionClass::resetAsLazyProxy(object $object, callable $factory, [int $options]): void
```php

El comportamiento de este método es el mismo que ReflectionClass::resetAsLazyGhost excepto que utiliza la estrategia de proxy.

El `object` mismo se convierte en el proxy. De manera similar a ReflectionClass::resetAsLazyGhost, el objeto no es reemplazado por otro, y su identidad no cambia, incluso después de la inicialización. El proxy y la instancia real son objetos distintos, con identidades distintas.

## Parámetros

`object`  
Un objeto no perezoso, o un objeto perezoso inicializado.

`factory`  
Una función de devolución de llamada con la misma firma y propósito que en ReflectionClass::newLazyProxy.

  

## Valores devueltos

No se retorna ningún valor.

## Véase también

ReflectionClass::newLazyProxy

ReflectionClass::resetAsLazyGhost
