---
title: La clase MongoDB\Driver\Manager
source_url: https://www.php.net/manual/es/class.mongodb-driver-manager.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/manager.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49870
---

## Introducción

La clase `MongoDB\Driver\Manager` es el punto de entrada principal a la extensión. Es responsable de mantener las conexiones a MongoDB (ya sea un servidor independiente, un conjunto de réplicas o un clúster particionado).

No se realiza ninguna conexión a MongoDB al instanciar el Manager. Esto significa que el `MongoDB\Driver\Manager` siempre puede ser construido, incluso si uno o más servidores de MongoDB están caídos.

Cualquier escritura o consulta puede lanzar excepciones de conexión ya que las conexiones se crean de forma perezosa. Un servidor de MongoDB también puede volverse no disponible durante la ejecución del script. Por lo tanto, es importante envolver todas las acciones sobre el Manager en sentencias try/catch.

## Sinopsis de la clase

MongoDB\Driver\Manager

final

MongoDB\Driver\Manager

Métodos

## Ejemplos

Ejemplo básico de `MongoDB\Driver\Manager::__construct`

Realizar un `var_dump` de un `MongoDB\Driver\Manager` mostrará varios detalles sobre el gestor que normalmente no están expuestos. Esto puede ser útil para depurar cómo el controlador visualiza su configuración de MongoDB y qué opciones se están utilizando.

```php
<?php

$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017');
var_dump($manager);

?>

    
```

Resultado del ejemplo anterior es similar a:

    object(MongoDB\Driver\Manager)#1 (2) {
      ["uri"]=>
      string(26) "mongodb://127.0.0.1:27017/"
      ["cluster"]=>
      array(0) {
      }
    }
