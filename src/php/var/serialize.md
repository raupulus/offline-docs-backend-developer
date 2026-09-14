---
title: serialize
description: Genera una representación almacenable de un valor
source_url: https://www.php.net/manual/es/function.serialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/serialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: false
translation_revision: d816a0fad
order: 100740
---

serialize

Genera una representación almacenable de un valor

## Descripción

```php
serialize(mixed $value): string
```php

Devuelve un array en forma de string.

Es una técnica útil para almacenar o pasar valores PHP entre scripts sin perder su estructura ni su tipo.

Para recuperar una variable serializada y obtener un valor PHP, se debe utilizar `unserialize`.

## Parámetros

`value`  
El valor a serializar. `serialize` acepta todos los tipos excepto los de tipo `resource` y ciertos `object`s (ver nota a continuación). Asimismo, es posible serializar un array que contenga referencias a sí mismo. Las referencias cíclicas en arrays/objetos también serán almacenadas. Todas las demás referencias se perderán.

Al serializar un objeto, PHP intentará llamar a las funciones miembro [\_\_serialize()](#object.serialize) o [\_\_sleep()](#object.sleep) antes de serializar. Esto permite al objeto realizar una última limpieza, etc. antes de ser serializado. De manera similar, cuando el objeto es restaurado utilizando `unserialize`, se llama a la función miembro [\_\_unserialize()](#object.unserialize) o [\_\_wakeup()](#object.wakeup).

> [!NOTE]
> Los atributos privados de un objeto tendrán el nombre de la clase prefijado al nombre del atributo; los atributos protegidos serán prefijados con un asterisco '\*'. Estos valores prefijados tienen caracteres nulos a ambos lados.

## Valores devueltos

Devuelve un string que contiene una representación en forma de flujo de bytes de `value` que puede ser almacenada en cualquier lugar.

Cabe señalar que se trata de una cadena binaria que puede incluir bytes nulos, y por lo tanto debe ser almacenada y gestionada como tal. Por ejemplo, la salida de `serialize` generalmente debe ser almacenada en un campo de tipo BLOB de una base de datos, en lugar de en un campo de tipo CHAR o TEXT.

## Ejemplos

Ejemplo con `serialize`

```
<?php
// $session_data contiene un array multidimensional, con la información de sesión del usuario actual. Se utiliza serialize() para almacenarlos en una base de datos

$conn = odbc_connect("webdb", "php", "chicken");
$stmt = odbc_prepare($conn,
      "UPDATE sessions SET data = ? WHERE id = ?");
$sqldata = array (serialize($session_data), $_SERVER['PHP_AUTH_USER']);
if (!odbc_execute($stmt, $sqldata)) {
    $stmt = odbc_prepare($conn,
     "INSERT INTO sessions (id, data) VALUES(?, ?)");
    if (!odbc_execute($stmt, array_reverse($sqldata))) {
        /* ¡Ha ocurrido un problema! */
    }
}
?>

    
```php

## Notas

> [!NOTE]
> Cabe señalar que muchos objetos internos de PHP no pueden ser serializados. Sin embargo, aquellos que pueden implementan ya sea la interfaz Serializable o los métodos mágicos [\_\_serialize()](#object.serialize)/[\_\_unserialize()](#object.unserialize) o [\_\_sleep()](#object.sleep)/[\_\_wakeup()](#object.wakeup). Si una clase interna no cumple ninguna de estas condiciones, no puede ser serializada de manera confiable.
>
> Existen excepciones históricas a esta regla, donde los objetos internos pueden ser serializados aunque no implementen la interfaz o expongan los métodos mágicos previstos para este efecto.

> [!WARNING]
> Cuando la función `serialize` serializa objetos, la barra invertida final no está incluida en el espacio de nombres del nombre de la clase, y esto es para una máxima compatibilidad.

## Véase también

`unserialize`, `var_export`, `json_encode`, [Serializing Objects](#language.oop5.serialization), [\_\_sleep()](#object.sleep), [\_\_wakeup()](#object.wakeup), [\_\_serialize()](#object.serialize), [\_\_unserialize()](#object.unserialize)
