---
title: ReflectionClass::resetAsLazyGhost
description: Reinicia un objeto y lo marca como perezoso
source_url: https://www.php.net/manual/es/reflectionclass.resetaslazyghost.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/resetaslazyghost.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 44b94f510
order: 69650
---

ReflectionClass::resetAsLazyGhost

Reinicia un objeto y lo marca como perezoso

## Descripción

```php
public ReflectionClass::resetAsLazyGhost(object $object, callable $initializer, [int $options]): void
```php

Reinicia un `objeto` existente y lo marca como perezoso.

El destructor del objeto es llamado (si existe) a menos que se especifique el flag `ReflectionClass::SKIP_DESTRUCTOR`. En el caso particular donde el objeto es un proxy inicializado, la instancia real es desvinculada del proxy. Si la instancia real ya no es referenciada en otro lugar, su destructor es llamado independientemente del flag `SKIP_DESTRUCTOR`.

Las propiedades dinámicas son eliminadas, y el valor de las propiedades declaradas en la clase es descartado como si `unset` fuera llamada, y marcadas como perezosas. Esto implica que si el objeto es una instancia de una subclase con propiedades adicionales, estas propiedades no son modificadas y no son marcadas como perezosas. Las [propiedades readonly](#language.oop5.properties.readonly-properties) no son modificadas y no son marcadas como perezosas si son `final` o si la clase misma es `final`.

Si ninguna propiedad es marcada como perezosa, el objeto no es marcado como perezoso. Ver también [Ciclo de vida de los objetos perezosos](#language.oop5.lazy-objects.lifecycle).

De lo contrario, después de la llamada a este método, el comportamiento del objeto es el mismo que un objeto creado por ReflectionClass::newLazyGhost (excepto para las propiedades de subclase y las propiedades readonly, como se describe anteriormente).

El objeto no es reemplazado por otro, y su identidad permanece inalterada. Las funcionalidades como `spl_object_id`, `spl_object_hash`, `SplObjectStorage`, `WeakMap`, `WeakReference`, o [el operador de identidad (`===`)](#language.oop5.object-comparison) no son afectadas.

## Parámetros

`object`  
Un objeto no perezoso, o un objeto perezoso inicializado.

`initializer`  
Una función de retrollamada con la misma firma y propósito que en ReflectionClass::newLazyGhost.

`options`  
`options` puede ser una combinación de los siguientes flags:

`ReflectionClass::SKIP_INITIALIZATION_ON_SERIALIZE`  
Por omisión, la serialización de un objeto perezoso desencadena su inicialización. Definir este flag evita la inicialización, permitiendo que los objetos perezosos sean serializados sin ser inicializados.

`ReflectionClass::SKIP_DESTRUCTOR`  
Por omisión, el destructor del objeto es llamado (si existe) antes de marcarlo como perezoso. Este flag desactiva este comportamiento, permitiendo que los objetos sean reiniciados como perezosos sin llamar al destructor.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Una `ReflectionException` si el objeto es perezoso y no está inicializado.

Una `Error` si el objeto está en proceso de inicialización, o si las propiedades del objeto son iteradas con [`foreach`](#control-structures.foreach).

## Véase también

ReflectionClass::newLazyGhost

ReflectionClass::resetAsLazyProxy
