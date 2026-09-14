---
title: CommonMark\Interfaces\IVisitor::leave
description: Visitación
source_url: https://www.php.net/manual/es/commonmark-interfaces-ivisitor.leave.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cmark/commonmark/interfaces/ivisitor/leave.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cmark
translation_status: ready
translation_reviewed: false
translation_revision: 876a6a393
order: 6970
---

CommonMark\Interfaces\IVisitor::leave

Visitación

## Descripción

```php
abstract public CommonMark\Interfaces\IVisitor::leave(IVisitable $visitable): int
```php

## Parámetros

`visitable`  
El `CommonMark\Interfaces\IVisitable` actual en curso de salida

## Valores devueltos

Devolver `CommonMark\Interfaces\IVisitor::Done` provocará la salida del iterador subyacente.

Devolver `CommonMark\Interfaces\IVisitor::Enter` reinicializará el iterador subyacente al entrar en el `IVisitable` actual

Devolver `CommonMark\Interfaces\IVisitor::Leave` reinicializará el iterador subyacente al salir del `IVisitable` actual

Devolver un `IVisitable` reinicializará el iterador subyacente al entrar en el `IVisitable` dado

No devolver nada permitirá al iterador subyacente continuar

## Véase también
