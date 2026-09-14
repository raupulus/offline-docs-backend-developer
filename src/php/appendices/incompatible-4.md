---
title: Cambios incompatibles con versiones anteriores
source_url: https://www.php.net/manual/es/migration72.incompatible.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration72/incompatible.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 8859c8b96
order: 550
---

## Cambios incompatibles con versiones anteriores

## Evitar que `number_format` devuelva cero negativo

Anteriormente, era posible que la función `number_format` devolviera `-0`. Aunque esto es perfectamente válido según la norma "IEEE 754 floating point specification", esta rareza no era deseable para la visualización de números formateados en una forma legible por el ser humano.

```php
<?php

var_dump(number_format(-0.01)); // ahora muestra string(1) "0" en lugar de string(2) "-0"

   
```

## Conversión de claves numéricas en objetos y arrays durante el casting

Las claves numéricas ahora son mejor manejadas durante el casting de un array a un objeto y de un objeto a un array (casting explícito o por la función `settype`).

Esto significa que las claves representadas por un entero (o un entero en forma de texto) de un array convertido en objeto ahora son accesibles:

```php
<?php

// array a objeto
$arr = [0 => 1];
$obj = (object) $arr;
var_dump(
    $obj,
    $obj->{'0'}, // ahora accesible
    $obj->{0} // ahora accesible
);

   
```

El ejemplo anterior mostrará:

    object(stdClass)#1 (1) {
      ["0"]=>    // ahora clave de texto en lugar de clave entera
      int(1)
    }
    int(1)
    int(1)

Y las claves en formato entero (o entero en forma de texto) de objetos convertidos en arrays ahora son accesibles:

```php
<?php

// objeto a array
$obj = new class {
    public function __construct()
    {
        $this->{0} = 1;
    }
};
$arr = (array) $obj;
var_dump(
    $arr,
    $arr[0], // ahora accesible
    $arr['0'] // ahora accesible
);

   
```

El ejemplo anterior mostrará:

    array(1) {
      [0]=>    // ahora clave entera en lugar de clave de texto
      int(1)
    }
    int(1)
    int(1)

## Prohibir pasar `null` a `get_class`

Anteriormente, pasar `null` a la función `get_class` devolvía el nombre de la clase en curso. Este comportamiento ha sido eliminado, se muestra un error `E_WARNING` en su lugar. Para recuperar el mismo comportamiento que antes, el argumento debería simplemente ser eliminado.

## Advertir al contar tipos no contables

Se emitirá un `E_WARNING` al intentar utilizar la función `count` en un tipo no contable (esto incluye la función alias `sizeof`).

```php
<?php

var_dump(
    count(null), // NULL no es contable
    count(1), // un entero no es contable
    count('abc'), // un string no es contable
    count(new stdClass), // un objeto que no implementa la interfaz Countable no es contable
    count([1,2]) // un array es contable
);

   
```

El ejemplo anterior mostrará:

    Warning: count(): Parameter must be an array or an object that implements Countable in %s on line %d

    Warning: count(): Parameter must be an array or an object that implements Countable in %s on line %d

    Warning: count(): Parameter must be an array or an object that implements Countable in %s on line %d

    Warning: count(): Parameter must be an array or an object that implements Countable in %s on line %d
    int(0)
    int(1)
    int(1)
    int(1)
    int(2)

## Reemplazo de ext/hash de recursos a objetos

En el marco de la migración a largo plazo de los recursos, la extensión [Hash](#book.hash) ha sido actualizada para utilizar los objetos en lugar de recursos. El cambio debería ser transparente para los desarrolladores PHP, excepto donde se hayan realizado verificaciones con `is_resource` (será necesario reemplazar por `is_object`).

## Mejorar los valores por defecto SSL/TLS

Se han realizado las siguientes modificaciones respecto a los valores por defecto:

- `tls://` ahora por defecto TLSv1.0 o TLSv1.1 o TLSv1.2

- `ssl://` es un alias de `tls://`

- `STREAM_CRYPTO_METHOD_TLS_*` constantes por defecto de TLSv1.0 o TLSv1.1 + TLSv1.2, en lugar de solo TLSv1.0.

## `gettype` valor de retorno en recursos cerrados

Anteriormente, el uso de `gettype` en un recurso cerrado devolvía una cadena `"unknown type"`. Ahora, la cadena `"resource (closed)"` será devuelta.

## `is_object` y `__PHP_Incomplete_Class`

Anteriormente, el uso de `is_object` en la clase `__PHP_Incomplete_Class` devolvía `false`. Ahora, `true` será devuelto.

## Aumento del nivel de error de las constantes no definidas

Las referencias no cualificadas a constantes no definidas ahora generarán un `E_WARNING` (en lugar de un `E_NOTICE`). En la próxima versión mayor de PHP, generarán una excepción `Error`.

## Soporte de Windows

Las versiones mínimas oficialmente soportadas para Windows son Windows 7/ Server 2008 R2.

## Verificación de los valores por defecto de las propiedades de los traits

Los controles de compatibilidad en los valores por defecto de las propiedades de trait ya no realizarán la conversión.

## `object` para los nombres de clases

El nombre `object` estaba anteriormente soft-reservado en PHP 7.0. Ahora está reservado, prohibiendo su uso como nombre de clase, trait o interfaz.

## Soporte de NetWare

El soporte de NetWare ha sido eliminado.

## `array_unique` con `SORT_STRING`

Mientras que `array_unique` con `SORT_STRING` anteriormente copiaba el array y eliminaba elementos no únicos (sin envolver el array después), ahora se construye un nuevo array añadiendo los elementos únicos. Esto puede resultar en índices numéricos diferentes.

## `bcmod` cambia para números decimales

La función `bcmod` ya no trunca los números fraccionarios a enteros. Como tal, su comportamiento ahora sigue `fmod`, en lugar del operador `%`. Por ejemplo, `bcmod('4', '3.5')` ahora devuelve `0.5` en lugar de `1`.

## Funciones de hachage y hachages no criptográficos

Las funciones `hash_hmac`, `hash_hmac_file`, `hash_pbkdf2`, y `hash_init` (con `HASH_HMAC`) ya no aceptan hachages no criptográficos.

## Opciones de la función `json_decode`

La opción `JSON_OBJECT_AS_ARRAY` de la función `json_decode` ahora se utiliza si el segundo parámetro (assoc) es `null`. Anteriormente `JSON_OBJECT_AS_ARRAY` siempre fue ignorado.

## Salida de `rand` y `mt_rand`

Las secuencias generadas por `rand` y `mt_rand` para casos específicos pueden diferir de PHP 7.1 en máquinas de 64 bits (debido a la corrección de un error en la implementación de la polarización del módulo).

## Eliminación del parámetro INI [`sql.safe_mode`](#ini.sql.safe-mode)

El parámetro INI `sql.safe_mode` ha sido eliminado.

## Cambio en `date_parse` y `date_parse_from_format`

El elemento de `zone` del array devuelto por `date_parse` y `date_parse_from_format` representa segundos en lugar de minutos, y su signo está invertido. Por ejemplo, `-120` ahora es `7200`.

## Cookies entrantes

Desde PHP 7.2.34, los *nombres* de las cookies entrantes ya no se decodifican URL por razones de seguridad.
