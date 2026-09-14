---
title: Autocarga de clases
source_url: https://www.php.net/manual/es/language.oop5.autoload.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/autoload.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: c1f37a6c2
order: 2400
---

## Autocarga de clases

Muchos desarrolladores que escriben aplicaciones orientadas a objetos crean un fichero fuente por definición de clase. Uno de los mayores inconvenientes de este método es tener que escribir una larga lista de inclusiones de ficheros de clases al inicio de cada script: una inclusión por clase.

La función `spl_autoload_register` registra un número cualquiera de cargadores automáticos, lo que permite a las clases y a las interfaces ser automáticamente cargadas si no están definidas actualmente. Al registrar autocargadores, PHP da una última oportunidad de incluir una definición de clase o interfaz, antes de que PHP falle con un error.

Cualquier construcción similar a las clases puede ser autocargada de la misma manera. Esto incluye las clases, interfaces, traits y enumeraciones.

> [!CAUTION]
> Anterior a PHP 8.0.0, era posible utilizar `__autoload` para autocargar las clases y las interfaces. Sin embargo, es una alternativa menos flexible a `spl_autoload_register` y `__autoload` está obsoleto a partir de PHP 7.2.0, y eliminado a partir de PHP 8.0.0.

> [!NOTE]
> `spl_autoload_register` puede ser llamada varias veces para registrar varios autocargadores. Lanzar una excepción desde una función de autocarga, interrumpirá este proceso y no permitirá que las funciones de autocarga siguientes sean ejecutadas. Por esta razón, lanzar excepciones desde una función de autocarga es fuertemente desaconsejado.

Ejemplo de autocarga

Este ejemplo intenta cargar las clases `MiClase1` y `MiClase2`, respectivamente desde los ficheros `MiClase1.php` y `MiClase2.php`.

```php
<?php
spl_autoload_register(function ($class_name) {
    include $class_name . '.php';
});

$obj  = new MiClase1();
$obj2 = new MiClase2();
?>

   
```

Otro ejemplo de autocarga

Este ejemplo intenta cargar la interfaz `ITest`.

```php
<?php

spl_autoload_register(function ($name) {
    var_dump($name);
});

class Foo implements ITest {
}

/*
string(5) "ITest"

Fatal error: Interface 'ITest' not found in ...
*/
?>
    
    
```

Uso del autoloader de Composer

[Composer](https://getcomposer.org/) genera un fichero `vendor/autoload.php` configurado para cargar automáticamente los paquetes gestionados por Composer. Al incluir este fichero, estos paquetes pueden ser utilizados sin trabajo adicional.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$uuid = Ramsey\Uuid\Uuid::uuid7();

echo "Nuevo UUID generado -> ", $uuid->toString(), "\n";
?>

   
```

## Véase también

`unserialize`, [unserialize_callback_func](#ini.unserialize-callback-func), [unserialize_max_depth](#ini.unserialize-max-depth), `spl_autoload_register`, `spl_autoload`, `__autoload`
