---
title: ReflectionExtension::__construct
description: Construye un nuevo objeto ReflectionExtension
source_url: https://www.php.net/manual/es/reflectionextension.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionextension/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: e62098163
order: 70160
---

ReflectionExtension::\_\_construct

Construye un nuevo objeto ReflectionExtension

## Descripción

```php
public ReflectionExtension::__construct(string $name)
```php

Construye un `object` `ReflectionExtension`.

## Parámetros

`name`  
Nombre de la extensión.

## Errores/Excepciones

Lanza una `ReflectionException` si la extensión a reflejar no existe.

## Ejemplos

Ejemplo con `ReflectionExtension`

```
<?php
$ext = new ReflectionExtension('Reflection');

printf('Extensión: %s (versión: %s)', $ext->getName(), $ext->getVersion());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Extensión: Reflection (versión: 8.3.17)

## Véase también

ReflectionExtension::info, [Los constructores](#language.oop5.decon.constructor)
