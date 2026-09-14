---
title: ReflectionClassConstant::getName
description: Obtiene el nombre de la constante
source_url: https://www.php.net/manual/es/reflectionclassconstant.getname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclassconstant/getname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69760
---

ReflectionClassConstant::getName

Obtiene el nombre de la constante

## Descripción

```php
public ReflectionClassConstant::getName(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre de la constante.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Se lanza un `Error` cuando la propiedad name no ha sido inicializada. Anteriormente, el método devolvía `false` en caso de fallo. |
