---
title: Funcionalidades obsoletas
source_url: https://www.php.net/manual/es/migration82.deprecated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration82/deprecated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 65716f476
order: 930
---

## Funcionalidades obsoletas

## Núcleo de PHP

### Uso de propiedades dinámicas

La creación de propiedades dinámicas es obsoleta, a menos que la clase lo permita utilizando el atributo `#[\AllowDynamicProperties]`. `stdClass` permite las propiedades dinámicas. El uso de los métodos mágicos [\_\_get()](#object.get)/[\_\_set()](#object.set) no se ve afectado por este cambio. La advertencia de obsolescencia de las propiedades dinámicas puede ser abordada: Declarando la propiedad (preferible)., Añadiendo el atributo `#[\AllowDynamicProperties]` a la clase (que se aplica también a todas las clases hijas)., Utilizando un `WeakMap` si se deben asociar datos adicionales a un objeto del cual no se es propietario.

### Callables relativos

Los callables que no son aceptados por la sintaxis `$callable()` (pero que son aceptados por `call_user_func`) son obsoletos. En particular: `"self::method"`, `"parent::method"`, `"static::method"`, `["self", "method"]`, `["parent", "method"]`, `["static", "method"]`, `["Foo", "Bar::method"]`, `[new Foo, "Bar::method"]` Esto no afecta a los callables de método normales como `"A::method"` o `["A", "method"]`.

### Interpolación de estilo `"${var}"` y `"${expr}"`.

Los estilos de interpolación de cadena `"${var}"` y `"${expr}"` son obsoletos. Utilice respectivamente `"$var"/"{$var}"` y `"{${expr}}"`.

## MBString

El uso de los formatos `QPrint`, `Base64`, `Uuencode` y `HTML-ENTITIES` es obsoleto para todas las funciones MBString. A diferencia de todos los otros encodings de texto soportados por MBString, estos no codifican una secuencia de puntos de código Unicode, sino más bien una secuencia de bytes en bruto. Los valores de retorno de la mayoría de las funciones MBString no son claros cuando se especifica uno de estos no-encodings. Además, PHP tiene implementaciones distintas para cada uno de ellos; por ejemplo, los datos UUencoded pueden ser manejados utilizando `convert_uuencode`/`convert_uudecode`.

## SPL

El método interno SplFileInfo::\_bad_state_ex ha sido declarado obsoleto.

## Estándar

`utf8_encode` y `utf8_decode` han sido declaradas obsoletas.
