---
title: CommonMark\Interfaces\IVisitor::enter
description: Visitación
source_url: https://www.php.net/manual/es/commonmark-interfaces-ivisitor.enter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cmark/commonmark/interfaces/ivisitor/enter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cmark
translation_status: ready
translation_reviewed: false
translation_revision: 876a6a393
order: 6960
---

CommonMark\Interfaces\IVisitor::enter

Visitación

## Descripción

```php
abstract public CommonMark\Interfaces\IVisitor::enter(IVisitable $visitable): int
```php

## Parámetros

`visitable`  
El `CommonMark\Interfaces\IVisitable` actual en curso de entrada

## Valores devueltos

Devolver `CommonMark\Interfaces\IVisitor::Done` provocará la salida del iterador subyacente.

Devolver `CommonMark\Interfaces\IVisitor::Enter` reinicializará el iterador subyacente al entrar en el `IVisitable` actual

Devolver `CommonMark\Interfaces\IVisitor::Leave` reinicializará el iterador subyacente al salir del actual `IVisitable`

Devolver un `IVisitable` reinicializará el iterador subyacente al entrar en el `IVisitable` dado

No devolver nada permitirá que el iterador subyacente continúe

## Véase también
