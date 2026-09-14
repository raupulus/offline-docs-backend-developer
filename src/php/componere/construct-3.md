---
title: Componere\Patch::__construct
description: Constructor Patch
source_url: https://www.php.net/manual/es/componere-patch.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/componere/componere/patch/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: componere
translation_status: ready
translation_revision: 6dcc757d9
order: 8210
---

Componere\Patch::\_\_construct

Constructor Patch

## Descripción

```php
public Componere\Patch::__construct(object $instance)
```php

```php
public Componere\Patch::__construct(object $instance, array $interfaces)
```

## Parámetros

`instance`  
El objetivo de este Patch

`interfaces`  
Un array de nombres de clase insensibles a las mayúsculas y minúsculas

## Excepciones

> [!WARNING]
> Lanzará `RuntimeException` si una clase en `interfaces` no se puede encontrar

> [!WARNING]
> Lanzará `RuntimeException` si una clase en `interfaces` no es una interface
