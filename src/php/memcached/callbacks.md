---
title: Funciones de retorno
source_url: https://www.php.net/manual/es/memcached.callbacks.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/callbacks.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: false
translation_revision: 80872147a
order: 46290
---

## Funciones de retorno

## Funciones de retorno de resultados

Las funciones de retorno de resultados (tipo `callable`) son invocadas por las funciones Memcached::getDelayed o Memcached::getDelayedBykey, para cada elemento del conjunto de resultados. Las funciones de retorno reciben un objeto Memcached y un array con la información sobre el elemento. La función de retorno no necesita devolver nada.

Ejemplo de función de retorno de resultados

```php
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);
$items = array(
    'key1' => 'value1',
    'key2' => 'value2',
    'key3' => 'value3'
);
$m->setMulti($items);
$m->getDelayed(array('key1', 'key3'), true, 'result_cb');

function result_cb($memc, $item)
{
    var_dump($item);
}
?>

   
```

Resultado del ejemplo anterior es similar a:

    array(3) {
      ["key"]=>
      string(4) "key1"
      ["value"]=>
      string(6) "value1"
      ["cas"]=>
      float(49)
    }
    array(3) {
      ["key"]=>
      string(4) "key3"
      ["value"]=>
      string(6) "value3"
      ["cas"]=>
      float(50)
    }

## Funciones de retorno para claves ausentes

Las funciones de retorno para claves ausentes son invocadas cuando un elemento no puede ser leído en el servidor. La función de retorno recibe un objeto Memcached, la clave solicitada, y un valor de variable por referencia. La función de retorno es entonces responsable de asignar el valor, y luego devolver `true` o `false`. Si la función de retorno devuelve `true` Memcached almacenará el valor así creado en el servidor, y lo devolverá a la función invocante. Solo Memcached::get y Memcached::getByKey soportan estas funciones, ya que el protocolo memcache no proporciona ninguna información sobre la ausencia de clave en una petición multiclave.

Funciones de retorno para claves ausentes

```php
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);

$profile_info = $m->get('user:'.$user_id, 'user_info_cb');

function user_info_cb($memc, $key, &$value)
{
    $user_id = substr($key, 5);
    /* Lee un perfil en una base de datos */
    /* ... */
    $value = $profile_info;
    return true;
}
?>

   
```
