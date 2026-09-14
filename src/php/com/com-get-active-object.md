---
title: com_get_active_object
description: Devuelve un objeto que representa la instancia actual de un objeto COM
source_url: https://www.php.net/manual/es/function.com-get-active-object.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/functions/com-get-active-object.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 20216b916
order: 7700
---

com_get_active_object

Devuelve un objeto que representa la instancia actual de un objeto COM

## Descripción

```php
com_get_active_object(string $prog_id, [int $codepage]): variant
```php

`com_get_active_object` es similar a la creación de una nueva instancia [???](#class.com) de un objeto COM, excepto que solo devolverá un objeto al script si el objeto está actualmente instanciado. Las aplicaciones OLE utilizan algo conocido como "`Running Object Table`" que permite a las aplicaciones conocidas ser ejecutadas solo una vez; esta función expone la función GetActiveObject() de la biblioteca COM para recuperar un objeto de una instancia en uso.

## Parámetros

`prog_id`  
El parámetro `prog_id` debe ser el ProgID o el CLSID del objeto al que se desea acceder (por ejemplo, `Word.Application`).

`codepage`  
utiliza las mismas reglas que en la [???](#class.com) clase.

## Valores devueltos

Si el objeto solicitado está en ejecución, la función devolverá al script lo que cualquier otro objeto COM devolvería.

## Errores/Excepciones

Hay muchas razones por las cuales esta función puede fallar. En esta situación, el código de error de la excepción debería ser `MK_E_UNAVAILABLE`; se puede utilizar el método `getCode` del objeto excepción para verificar el código de la excepción.

## Historial de cambios

| Versión | Descripción                   |
|---------|-------------------------------|
| 8.0.0   | `codepage` es ahora nullable. |

## Notas

> [!WARNING]
> Utilizar la función `com_get_active_object` en un servidor web no siempre es la mejor idea. La mayoría de las aplicaciones COM/OLE no están diseñadas para manejar más de un cliente concurrente, como (¡¡y especialmente!!) Microsoft Office. Se debe leer las [consideraciones para los automatismos lado-servidor para Office](http://support.microsoft.com/kb/257757) para obtener más información sobre los comportamientos generales.
