---
title: ReflectionProperty::setRawValueWithoutLazyInitialization
description: Define el valor bruto de una propiedad sin activar la inicialización
  perezosa
source_url: https://www.php.net/manual/es/reflectionproperty.setrawvaluewithoutlazyinitialization.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/setrawvaluewithoutlazyinitialization.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 790f63af6
order: 71790
---

ReflectionProperty::setRawValueWithoutLazyInitialization

Define el valor bruto de una propiedad sin activar la inicialización perezosa

## Descripción

```php
public ReflectionProperty::setRawValueWithoutLazyInitialization(object $object, mixed $value): void
```php

Define (cambia) el valor de la propiedad sin activar la inicialización perezosa ni llamar a las funciones de gancho. La propiedad se marca como no perezosa y puede ser accedida posteriormente sin activar la inicialización perezosa. La propiedad no debe ser dinámica, estática o virtual, y el objeto debe ser una instancia de una clase definida por el usuario o `stdClass`.

Si era la última propiedad perezosa, el objeto se marca como no perezoso y se desvincula el inicializador o la función de fábrica.

## Parámetros

`object`  
El objeto sobre el cual cambiar la propiedad.

`value`  
El nuevo valor.

## Valores devueltos

No se retorna ningún valor.

## Véase también

objetos perezosos

ReflectionProperty::skipLazyInitialization

ReflectionClass::newLazyGhost
