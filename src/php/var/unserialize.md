---
title: unserialize
description: Crea una variable PHP a partir de un valor serializado
source_url: https://www.php.net/manual/es/function.unserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/unserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: false
translation_revision: 8af3521cb
order: 100770
---

unserialize

Crea una variable PHP a partir de un valor serializado

## Descripción

```php
unserialize(string $data, [array $options]): mixed
```php

`unserialize` toma una variable serializada (ver `serialize`) y la convierte en una variable PHP.

> [!WARNING]
> No se debe pasar una entrada de usuario no confiable a la función `unserialize` independientemente del valor de `allowed_classes` en `options`. La deserialización puede resultar en la ejecución de código cargado y ejecutado durante la instanciación y la autocarga de objetos, y así, un usuario malintencionado podría ser capaz de explotar este comportamiento. Utilice un estándar de intercambio seguro, como JSON (a través de las funciones `json_decode` y `json_encode`) si necesita pasar datos serializados al usuario.
>
> Si necesita deserializar datos serializados almacenados externamente, considere el uso de `hash_hmac` para validar los datos. Asegúrese de que los datos no hayan sido modificados por nadie más que usted.

## Parámetros

`data`  
La cadena serializada.

Si la variable deserializada es un objeto, después de reconstruirlo con éxito, PHP intentará automáticamente llamar a los métodos [\_\_unserialize()](#object.unserialize) o [\_\_wakeup](#object.wakeup) (si alguno de ellos existe).

> [!NOTE]
> La retrollamada especificada en la directiva [unserialize_callback_func](#ini.unserialize-callback-func) es llamada cuando una clase no definida es deserializada. Si no se especifica ninguna retrollamada, el objeto será instanciado como `__PHP_Incomplete_Class`.

`options`  
Cualquier opción a proporcionar a `unserialize`, en forma de un array asociativo.

<table>
<caption>Opciones válidas</caption>
<thead>
<tr>
<th>Nombre</th>
<th>Tipo</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>allowed_classes</code></td>
<td><code>arraybool</code></td>
<td><p>Puede ser un <code>array</code> de nombres de clases que deben ser aceptados, <code>false</code> para no aceptar ninguna clase, o <code>true</code> para aceptar todas las clases. Si esta opción está definida, y <code>unserialize</code> encuentra un objeto de una clase que no está aceptada, entonces el objeto será instanciado como <code>__PHP_Incomplete_Class</code>.</p>
<p>Omitir esta opción equivale a definirla como <code>true</code>: PHP intentará instanciar objetos de cualquier clase.</p>
<p>Esta opción no afecta a las <a href="#language.enumerations">Enumeraciones</a>.</p></td>
</tr>
<tr>
<td><code>max_depth</code></td>
<td><code>int</code></td>
<td><p>La profundidad máxima permitida de las estructuras durante la deserialización, que está destinada a prevenir desbordamientos de pila. El límite de profundidad por defecto es de <code>4096</code> y puede ser desactivado definiendo <code>max_depth</code> a <code>0</code>.</p></td>
</tr>
</tbody>
</table>

## Valores devueltos

El valor convertido es retornado por la función, y puede ser un `bool`, `int`, `float`, `string`, `array` o `object`.

Si la cadena pasada no puede ser deserializada, esta función retorna `false` y se emite un error `E_WARNING`.

## Errores/Excepciones

Los objetos pueden lanzar `Throwable`s en su gestor de deserialización.

A partir de PHP 8.4.0, si el elemento `allowed_classes` de `options` no es un `array` de nombres de clases, `unserialize` lanza TypeError y ValueError.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Ahora lanza TypeError y ValueError si el elemento `allowed_classes` de `options` no es un `array` de nombres de clases. |
| 8.4.0 | Deserializar cadenas usando la etiqueta `"S"` en mayúscula ahora está obsoleto; en su lugar, utilice la etiqueta `"s"` en minúscula. |
| 8.3.0 | Ahora emite un `E_WARNING` cuando la cadena de entrada contiene datos no consumidos. |
| 8.3.0 | Ahora emite un `E_WARNING` cuando la cadena proporcionada no es deserializable; previamente, se emitía un `E_NOTICE`. |
| 7.4.0 | Se agregó el elemento `max_depth` a `options` para definir la profundidad máxima permitida de las estructuras durante la deserialización. |
| 7.1.0 | El elemento `allowed_classes` de `options` ahora está estrictamente tipado, es decir, si se proporciona algo que no sea un array `array` o un `bool` `unserialize` retorna `false` y emite una `E_WARNING`. |

## Ejemplos

Ejemplo con `unserialize`

```
<?php
// Aquí, se utiliza <function>unserialize</function> para cargar los datos de sesión
// desde la base de datos, en $session_data. Este ejemplo complementa
// el proporcionado con <function>serialize</function>.

$conn = odbc_connect("webdb", "php", "chicken");
$stmt = odbc_prepare($conn, "SELECT data FROM sessions WHERE id = ?");
$sqldata = array($_SERVER['PHP_AUTH_USER']);
if (!odbc_execute($stmt, $sqldata) || !odbc_fetch_into($stmt, $tmp)) {
    // si la preparación o la lectura fallan, se crea un array vacío
    $session_data = array();
} else {
    // los datos guardados están en $tmp[0].
    $session_data = unserialize($tmp[0]);
    if (!is_array($session_data)) {
        // Error... inicialización de un array vacío
        $session_data = array();
    }
}
?>

    
```php

Ejemplo con la directiva unserialize_callback_func

```
<?php
$serialized_object='O:1:"a":1:{s:5:"value";s:3:"100";}';

ini_set('unserialize_callback_func', 'mycallback');

function mycallback($classname)
{
    // Simplemente incluya un archivo que contenga su definición de clase
    // sabrá qué clase gracias a $classname
    var_dump($classname);
}

unserialize($serialized_object);
?>

    
```php

## Notas

> [!WARNING]
> `false` es retornado en los casos donde ocurre un error y si se intenta deserializar un valor serializado igual a `false`. Es posible interceptar este caso especial comparando `data` con `serialize(false)` o atrapando el error `E_WARNING` emitido.

## Véase también

`json_encode`, `json_decode`, `hash_hmac`, `serialize`, [Autoloading Classes](#language.oop5.autoload), [unserialize_callback_func](#ini.unserialize-callback-func), [unserialize_max_depth](#ini.unserialize-max-depth), [\_\_wakeup()](#object.wakeup), [\_\_serialize()](#object.serialize), [\_\_unserialize()](#object.unserialize)
