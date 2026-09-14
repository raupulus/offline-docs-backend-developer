---
title: ReflectionMethod::getClosure
description: Devuelve una función anónima creada dinámicamente para el método
source_url: https://www.php.net/manual/es/reflectionmethod.getclosure.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionmethod/getclosure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ca840c9a6
order: 70950
---

ReflectionMethod::getClosure

Devuelve una función anónima creada dinámicamente para el método

## Descripción

```php
public ReflectionMethod::getClosure([object $object]): Closure
```php

Crea una función anónima que llamará a este método.

## Parámetros

`object`  
Prohibido para los métodos estáticos, requerido para los demás métodos.

## Valores devueltos

Devuelve un objeto `Closure` recién creado.

## Errores/Excepciones

Genera una `ValueError` si `object` es `null` pero el método no es estático.

Genera una `ReflectionException` si `object` no es una instancia de la clase de la que este método fue declarado.

## Historial de cambios

| Versión | Descripción                 |
|---------|-----------------------------|
| 8.0.0   | `object` ahora es nullable. |

## Véase también

Sintaxis callable de primera clase
