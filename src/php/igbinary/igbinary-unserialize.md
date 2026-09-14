---
title: igbinary_unserialize
description: Crea una variable PHP a partir de un valor serializado por igbinary_serialize
source_url: https://www.php.net/manual/es/function.igbinary-unserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/igbinary/functions/igbinary-unserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: igbinary
translation_status: ready
translation_reviewed: false
translation_revision: 43dd38b94
order: 31310
---

igbinary_unserialize

Crea una variable PHP a partir de un valor serializado por

igbinary_serialize

## Descripción

```php
igbinary_unserialize(string $str): mixed
```php

`igbinary_unserialize` toma una variable serializada por `igbinary_serialize` y la convierte en una variable PHP.

> [!WARNING]
> Las entradas de usuario no confiables no deben pasarse a la función `igbinary_unserialize`. La deserialización puede resultar en la ejecución de código cargado y ejecutado durante la instanciación y el autochargado de objetos, y así, un usuario malintencionado puede ser capaz de explotar este comportamiento. En su lugar, un estándar de intercambio seguro como JSON (a través de `json_decode` y `json_encode`) debe usarse para pasar datos serializados al usuario.
>
> Si es indispensable deserializar datos serializados provenientes del exterior, la función `hash_hmac` puede usarse para validar los datos. Es importante verificar que nadie haya alterado los datos.

> [!WARNING]
> El protocolo de serialización por igbinary no permite distinguir entre los diferentes grupos de referencias. Todas las referencias PHP a un valor dado son vistas como miembros de un mismo grupo durante la deserialización, incluso si pertenecían a grupos diferentes antes de la serialización.

## Parámetros

`str`  
La cadena serializada, generada por `igbinary_serialize`.

Si la variable deserializada es un `object`, después de reconstruirla con éxito, PHP intentará automáticamente llamar a los métodos mágicos [\_\_unserialize()](#object.unserialize) o [\_\_wakeup()](#object.wakeup) (si alguno de ellos existe).

> [!NOTE]
> La función de retrollamada especificada en la directiva [unserialize_callback_func](#ini.unserialize-callback-func) es llamada cuando una clase no definida es deserializada. Si ninguna función de retrollamada es especificada, el objeto será instanciado como `__PHP_Incomplete_Class`.

## Valores devueltos

El valor convertido es retornado por la función, y puede ser de tipo `bool`, `int`, `float`, `string`, `array`, `object`, o de tipo `null`.

Si la cadena pasada no puede ser deserializada, esta función retorna `false` y un diagnóstico `E_NOTICE` o `E_WARNING` es emitido.

## Errores/Excepciones

Los objetos pueden lanzar un `Throwable` en su gestor de deserialización.

## Notas

> [!WARNING]
> `null` o `false` es retornado ya sea en caso de error o después de deserializar el resultado de la serialización de `null` o `false`. Es posible discriminar entre estos dos casos especiales comparando el valor del parámetro `str` con el resultado de la ejecución de `igbinary_serialize(null)` o de `igbinary_serialize(false)` o bien atrapando un diagnóstico `E_NOTICE`.

## Véase también

unserialize

json_encode

json_decode

hash_hmac

igbinary_serialize

Autocargado de clases

unserialize_callback_func

\_\_wakeup()

\_\_serialize()

\_\_unserialize()
