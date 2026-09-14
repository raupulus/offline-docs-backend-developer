---
title: eio_custom
description: Ejecutar una petición personalizada como cualquier otra llamada eio_*
source_url: https://www.php.net/manual/es/function.eio-custom.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-custom.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 16730
---

eio_custom

Ejecutar una petición personalizada como cualquier otra llamada

eio\_\*

## Descripción

```php
eio_custom(callable $execute, int $pri, callable $callback, [mixed $data]): resource
```php

`eio_custom` ejecuta una función personalizada especificada por `execute` procesándola igual que cualquier otra llamada *eio\_\**.

## Parámetros

`execute`  
Especifica la función de petición que debería coincidir con el siguiente prototipo:

          mixed execute(mixed data);
          

`callback` es una llamada de retorno de finalización de evento que debería coincidir con el siguiente prototipo:

          void callback(mixed data, mixed result);
          

`data` son los datos pasados a `execute` mediante el argumento `data` sin modificaciones `result` valor devuelto por `execute`

`pri`  
La prioridad de la petición: `EIO_PRI_DEFAULT`, `EIO_PRI_MIN`, `EIO_PRI_MAX`, o `null`. Si `null` es pasado, el parámetro `pri`, internamente, es definido a `EIO_PRI_DEFAULT`.

`callback`  
La función de retrollamada `callback` es llamada cuando la petición está terminada. Debe corresponder al siguiente prototipo:

```
void callback(mixed $data, int $result[, resource $req]);
```php

`data`  
representa los datos personalizados pasados a la petición.

`result`  
representa el valor resultante específico de la petición; básicamente, el valor retornado por la llamada al sistema correspondiente.

`req`  
es el recurso opcional de la petición que puede ser utilizado con funciones como `eio_get_last_error`.

`data`  
Variable arbitraria pasada a `callback`.

## Valores devueltos

`eio_custom` devuelve un recurso de petición en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `eio_custom`

```
<?php
/* Llamada de retorno para la llamada de retorno personalizada */
function mi_llamada_retorno_personalizada($datos, $resultado) {
    var_dump($datos);
    var_dump(count($resultado));
    var_dump($resultado['datos_modificados']);
    var_dump($resultado['resultado']);
}

/* La petición personalizada */
function mi_personalizada($datos) {
    var_dump($datos);

    $resultado = array(
        'resultado'         => 1001,
        'datos_modificados' => "mis datos personalizados",
    );

    return $resultado;
}

$datos = "mis_datos_personalizados";
$petición = eio_custom("mi_personalizada", EIO_PRI_DEFAULT, "mi_llamada_retorno_personalizada", $datos);
var_dump($petición);
eio_event_loop();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    resource(4) of type (EIO Request Descriptor)
    string(24) "mis_datos_personalizados"
    string(24) "mis_datos_personalizados"
    int(2)
    string(24) "mis datos personalizados"
    int(1001)
