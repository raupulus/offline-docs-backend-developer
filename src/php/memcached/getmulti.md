---
title: Memcached::getMulti
description: Lee varios elementos
source_url: https://www.php.net/manual/es/memcached.getmulti.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/getmulti.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46570
---

Memcached::getMulti

Lee varios elementos

## Descripción

```php
public Memcached::getMulti(array $keys, [int $get_flags]): array
```php

`Memcached::getMulti` es similar al método Memcached::get, pero en lugar de un solo elemento, puede leer varios elementos especificados por el array `keys`.

> [!NOTE]
> Antes de la v3.0, un segundo argumento `cas_tokens` era utilizado. Era rellenado con los valores de los tokens CAS para los elementos encontrados. El parámetro `cas_tokens` fue eliminado en la v3.0 de la extensión. Fue reemplazado por un nuevo flag `Memcached::GET_EXTENDED` que debe ser utilizado como valor para `get_flags`.

El parámetro `get_flags` sirve para especificar opciones adicionales para `Memcached::getMulti`. `Memcached::GET_PRESERVE_ORDER` garantiza que las claves son devueltas en el mismo orden que el de su solicitud. `Memcached::GET_EXTENDED` garantiza que los tokens CAS serán también recuperados.

## Parámetros

`keys`  
Un array de claves a leer.

`get_flags`  
Las opciones para esta operación.

## Valores devueltos

Devuelve un array de elementos leídos o `false` si ocurre un error. Utilice Memcached::getResultCode si es necesario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL memcached 3.0.0 | El parámetro `cas_tokens` fue eliminado. `Memcached::GET_EXTENDED` fue añadido y cuando se pasa como flag asegura que los tokens CAS son recuperados. |

## Ejemplos

Ejemplo de `Memcached::getMulti` para Memcached v3

```
<?php
// Válido para la v3 de la extensión

$m = new Memcached();
$m->addServer('localhost', 11211);

$items = array(
    'key1' => 'value1',
    'key2' => 'value2',
    'key3' => 'value3'
);
$m->setMulti($items);
$result = $m->getMulti(array('key1', 'key3', 'badkey'));
var_dump($result);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(2) {
      ["key1"]=>
      string(6) "value1"
      ["key3"]=>
      string(6) "value3"
    }

Ejemplo de `Memcached::getMulti` para Memcached v1 y v2

```
<?php
// Válido para la v1 y v2 de la extensión

$m = new Memcached();
$m->addServer('localhost', 11211);

$items = array(
    'key1' => 'value1',
    'key2' => 'value2',
    'key3' => 'value3'
);
$m->setMulti($items);
$result = $m->getMulti(array('key1', 'key3', 'badkey'), $cas);
var_dump($result, $cas);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(2) {
      ["key1"]=>
      string(6) "value1"
      ["key3"]=>
      string(6) "value3"
    }
    array(2) {
      ["key1"]=>
      float(2360)
      ["key3"]=>
      float(2362)
    }

Ejemplo de `Memcached::GET_PRESERVE_ORDER` para Memcached v3

```
<?php
// Válido para la v3 de la extensión

$m = new Memcached();
$m->addServer('localhost', 11211);

$data = array(
    'foo' => 'foo-data',
    'bar' => 'bar-data',
    'baz' => 'baz-data',
    'lol' => 'lol-data',
    'kek' => 'kek-data',
);

$m->setMulti($data, 3600);

$keys = array_keys($data);
$keys[] = 'zoo';
$got = $m->getMulti($keys, Memcached::GET_PRESERVE_ORDER);

foreach ($got as $k => $v) {
    echo "$k $v\n";
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    foo foo-data
    bar bar-data
    baz baz-data
    lol lol-data
    kek kek-data
    zoo

Ejemplo de `Memcached::GET_PRESERVE_ORDER` para Memcached v1 y v2

```
<?php
// Válido para la v1 y v2 de la extensión

$m = new Memcached();
$m->addServer('localhost', 11211);

$data = array(
    'foo' => 'foo-data',
    'bar' => 'bar-data',
    'baz' => 'baz-data',
    'lol' => 'lol-data',
    'kek' => 'kek-data',
);

$m->setMulti($data, 3600);

$null = null;
$keys = array_keys($data);
$keys[] = 'zoo';
$got = $m->getMulti($keys, $null, Memcached::GET_PRESERVE_ORDER);

foreach ($got as $k => $v) {
    echo "$k $v\n";
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    foo foo-data
    bar bar-data
    baz baz-data
    lol lol-data
    kek kek-data
    zoo

## Véase también

Memcached::getMultiByKey, Memcached::get, Memcached::getDelayed
