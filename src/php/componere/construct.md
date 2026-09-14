---
title: Componere\Definition::__construct
description: Constructor Definition
source_url: https://www.php.net/manual/es/componere-definition.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/componere/componere/definition/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: componere
translation_status: ready
translation_revision: 6dcc757d9
order: 8100
---

Componere\Definition::\_\_construct

Constructor Definition

## Descripción

```php
public Componere\Definition::__construct(string $name)
```php

```php
public Componere\Definition::__construct(string $name, string $parent)
```

```php
public Componere\Definition::__construct(string $name, array $interfaces)
```php

```php
public Componere\Definition::__construct(string $name, string $parent, array $interfaces)
```

## Parámetros

`name`  
Un nombre de clase insensible a las mayúsculas y minúsculas

`parent`  
Un nombre de clase insensible a las mayúsculas y minúsculas

`interfaces`  
Un array de nombres de clase insensibles a las mayúsculas y minúsculas

## Excepciones

> [!WARNING]
> Lanzará `InvalidArgumentException` si se intenta reemplazar una clase interna

> [!WARNING]
> Lanzará `InvalidArgumentException` si se intenta sustituir una interface

> [!WARNING]
> Lanzará `InvalidArgumentException` si se intenta reemplazar un rasgo

> [!WARNING]
> Lanzará `RuntimeException` si una clase en `interfaces` no se puede encontrar

> [!WARNING]
> Lanzará `RuntimeException` si una clase en `interfaces` no es una interface
