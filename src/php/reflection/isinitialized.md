---
title: ReflectionProperty::isInitialized
description: Verifica si una propiedad está inicializada
source_url: https://www.php.net/manual/es/reflectionproperty.isinitialized.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/isinitialized.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 71660
---

ReflectionProperty::isInitialized

Verifica si una propiedad está inicializada

## Descripción

```php
public ReflectionProperty::isInitialized([object $object]): bool
```php

Verifica si una propiedad está inicializada.

## Parámetros

`object`  
Si la propiedad no es estática, debe proporcionarse un objeto para recuperar la propiedad desde el mismo.

## Valores devueltos

Devuelve `false` para las propiedades tipadas antes de su inicialización, y para las propiedades que han sido explícitamente `unset`. Para todas las demás propiedades, `true` será devuelto.

## Errores/Excepciones

Lanza una `ReflectionException` si la propiedad es inaccesible. Es posible hacer accesible una propiedad protegida o privada utilizando ReflectionProperty::setAccessible.

## Historial de cambios

| Versión | Descripción                 |
|---------|-----------------------------|
| 8.0.0   | `object` ahora es nullable. |

## Ejemplos

Ejemplo de ReflectionProperty::isInitialized

```
<?php
class User
{
    public string $name;
}

$rp = new ReflectionProperty('User', 'name');
$user = new User;
var_dump($rp->isInitialized($user));
$user->name = 'Nikita';
var_dump($rp->isInitialized($user));
?>

   
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)

## Véase también

ReflectionProperty::hasType
