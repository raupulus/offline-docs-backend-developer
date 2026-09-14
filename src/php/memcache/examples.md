---
title: Ejemplos
source_url: https://www.php.net/manual/es/memcache.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_revision: f4098e2ba
order: 46060
---

## Ejemplos

## Uso básico

Ejemplos de la extensión memcache extension

En este ejemplo, se guarda un objeto en cache y luego se devuelve de nuevo. Objetos y otros tipos no escalares se serializan antes de guardarse, por lo tanto es imposible guardar recursos. (ej. identificadores de conexión y otros tipos) en caché.

```php
<?php

$memcache = new Memcache;
$memcache->connect('localhost', 11211) or die ("No se pudo contectar");

$version = $memcache->getVersion();
echo "Versión del servidor: ".$version."<br/>\n";

$tmp_object = new stdClass;
$tmp_object->str_attr = 'test';
$tmp_object->int_attr = 123;

$memcache->set('key', $tmp_object, false, 10) or die ("Falló al intentar guardar datos en el servidor");
echo "Guarda datos en caché (los datos expirarán en 10 segundos)<br/>\n";

$get_result = $memcache->get('key');
echo "Datos desde la caché:<br/>\n";

var_dump($get_result);

?>

   
```

Usando el gestor de sesiones de memcache

```php
<?php

$session_save_path = "tcp://$host:$port?persistent=1&weight=2&timeout=2&retry_interval=10,  ,tcp://$host:$port  ";
ini_set('session.save_handler', 'memcache');
ini_set('session.save_path', $session_save_path);

?>

   
```
