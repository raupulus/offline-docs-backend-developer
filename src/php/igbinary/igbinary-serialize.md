---
title: igbinary_serialize
description: Genera una representación binaria almacenable y compacta de un valor
source_url: https://www.php.net/manual/es/function.igbinary-serialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/igbinary/functions/igbinary-serialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: igbinary
translation_status: ready
translation_reviewed: false
translation_revision: 43dd38b94
order: 31300
---

igbinary_serialize

Genera una representación binaria almacenable y compacta de un valor

## Descripción

```php
igbinary_serialize(mixed $value): string
```php

Genera una representación almacenable de un valor.

Es una técnica práctica para almacenar o pasar valores PHP entre scripts, sin perder su estructura ni su tipo.

Para reconvertir la cadena sérializada en un valor PHP, la función `igbinary_unserialize` puede ser utilizada.

## Parámetros

`value`  
El valor a serializar. `igbinary_serialize` gestiona todos los tipos excepto los `recurso`s y ciertos `objeto`s (confiere la nota a continuación). Incluso los `array`x que contienen referencias a sí mismos pueden ser serializados con `igbinary_serialize`. Las referencias circulares dentro de un `array` o de un `object` a serializar serán igualmente almacenadas. Cualquier otra referencia será perdida.

Al serializar objetos, igbinary intentará llamar a los métodos mágicos [\_\_serialize()](#object.serialize) o [\_\_sleep()](#object.sleep) antes de la serialización. Esto permitirá al objeto realizar una limpieza de último momento, etc., antes de ser serializado. De igual manera, cuando el objeto es restaurado utilizando la función `igbinary_unserialize`, uno de los métodos mágicos [\_\_unserialize()](#object.unserialize) o [\_\_wakeup()](#object.wakeup) es llamado.

> [!NOTE]
> Los atributos privados de un objeto tendrán el nombre de la clase prefijado al nombre del atributo; los atributos protegidos serán prefijados con un asterisco `'*'`. Estos valores prefijados tienen caracteres nulos en ambos lados.

## Valores devueltos

Retorna una cadena de caracteres que contiene una representación del parámetro `value` en forma de flujo de bytes que puede ser almacenado en cualquier lugar.

Es de notar que es una cadena binaria que puede incluir caracteres nulos, y debe por lo tanto ser almacenada y gestionada como tal. Por ejemplo, en una base de datos, la salida de la función `igbinary_serialize` debe, en general, ser almacenada en un campo de tipo `BLOB` en lugar de en un campo de tipo `CHAR` o `TEXT`.

## Ejemplos

Ejemplo con `igbinary_serialize`

```
<?php
$ser = igbinary_serialize(['test', 'test']);
echo urlencode($ser), "\n";
var_export(igbinary_unserialize($ser));
?>

   
```php

El ejemplo anterior mostrará:

    %00%00%00%02%14%02%06%00%11%04test%06%01%0E%00
    array (
      0 => 'test',
      1 => 'test',
    )

## Notas

> [!NOTE]
> Es de notar que muchos objetos internos de PHP no pueden ser serializados. Sin embargo, aquellos que pueden implementan ya sea la interfaz Serializable o los métodos mágicos [\_\_serialize()](#object.serialize)/[\_\_unserialize()](#object.unserialize) o [\_\_sleep()](#object.sleep)/[\_\_wakeup()](#object.wakeup). Si una clase interna no cumple ninguna de estas condiciones, no puede ser serializada de manera fiable.
>
> Existen excepciones históricas a esta regla, donde objetos internos pueden ser serializados sin implementar ni la interfaz ni los métodos mágicos.

## Véase también

serialize

igbinary_unserialize

var_export

json_encode

Serialización de objetos

\_\_sleep()

\_\_wakeup()

\_\_serialize()

\_\_unserialize()
