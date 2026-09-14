---
title: Seguridad
source_url: https://www.php.net/manual/es/mongodb.security.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/security.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_revision: 6047c10c1
order: 51750
---

## Seguridad

## Ataques por inyección de peticiones

Si está pasando parámetros de `$_GET` (o `$_POST`) a sus consultas, asegúrese de que primero se conviertan a strings. Los usuarios pueden insertar arrays asociativos en peticiones GET y POST, lo que podría convertirse en consultas no deseadas con operadores \$-.

Un ejemplo bastante inocuo: supongamos que está buscando la información de un usuario con la petición *http://www.example.com?username=bob*. Su aplicación crea la consulta `$q = new \MongoDB\Driver\Query( [ 'username' => $_GET['username'] ])`.

Alguien podría subvertir esto mediante *http://www.example.com?username\[\$ne\]=foo*, que PHP convertirá mágicamente en un array asociativo, convirtiendo su consulta en `$q = new \MongoDB\Driver\Query( [ 'username' => [ '$ne' => 'foo' ] ] )`, lo que devolverá todos los usuarios que no se llamen "foo" (probablemente todos sus usuarios).

Este es un ataque bastante fácil de defender: asegúrese de que los parámetros de \$\_GET y \$\_POST sean del tipo que espera antes de enviarlos a la base de datos. PHP tiene la función `filter_var` para ayudar con esto.

Tenga en cuenta que este tipo de ataque puede usarse con cualquier interacción con la base de datos que localice un documento, incluyendo actualizaciones, upserts, eliminaciones y comandos findAndModify.

Consulte [la documentación principal](https://www.mongodb.com/docs/manual/security/) para obtener más información sobre problemas similares a la inyección SQL con MongoDB.

## Ataques por inyección de scripts

Si está usando JavaScript, asegúrese de que cualquier variable que cruce el límite entre PHP y JavaScript se pase en el campo `scope` de `MongoDB\BSON\Javascript`, no interpolada en la cadena de JavaScript. Esto puede ocurrir al usar cláusulas `$where` en consultas, comandos mapReduce y group, y cualquier otro momento en que pase JavaScript a la base de datos.

Por ejemplo, supongamos que tenemos algo de JavaScript para saludar a un usuario en los registros de la base de datos. Podríamos hacer:

```php
<?php
$m = new MongoDB\Driver\Manager;

// ¡No haga esto!
$username = $_GET['field'];

$cmd = new \MongoDB\Driver\Command( [
    'eval' => "print('Hola, $username!');"
] );

$r = $m->executeCommand( 'dramio', $cmd );
?>

  
```

Sin embargo, ¿qué pasaría si un usuario malicioso pasa algo de JavaScript?

```php
<?php
$m = new MongoDB\Driver\Manager;

// ¡No haga esto!
$username = $_GET['field'];
// $username se establece en "'); db.users.drop(); print('"

$cmd = new \MongoDB\Driver\Command( [
    'eval' => "print('Hola, $username!');"
] );

$r = $m->executeCommand( 'dramio', $cmd );
?>

  
```

Ahora MongoDB ejecuta la cadena de JavaScript `"print('Hola, '); db.users.drop(); print('!');"`. Este ataque es fácil de evitar: use `args` para pasar variables de PHP a JavaScript:

```php
<?php
$m = new MongoDB\Driver\Manager;

$_GET['field'] = 'derick';
$args = [ $_GET['field'] ];

$cmd = new \MongoDB\Driver\Command( [
    'eval' => "function greet(username) { print('Hola, ' + username + '!'); }",
    'args' => $args,
] );

$r = $m->executeCommand( 'dramio', $cmd );
?>

  
```

Esto añade un argumento al ámbito de JavaScript, que se usa como argumento para la función `greet`. Ahora si alguien intenta enviar código malicioso, MongoDB imprimirá inocuamente `Hola, '); db.dropDatabase(); print('!`.

Usar argumentos ayuda a prevenir que la entrada maliciosa se ejecute en la base de datos. Sin embargo, debe asegurarse de que su código no vuelva a ejecutar la entrada de todos modos. Lo mejor es evitar ejecutar *cualquier* JavaScript en el servidor desde el principio.

Se recomienda encarecidamente evitar el uso de la cláusula [`$where`](https://www.mongodb.com/docs/manual/reference/operator/query/where/#considerations) en consultas, ya que afecta significativamente al rendimiento. Siempre que sea posible, use operadores de consulta normales o el [Marco de Agregación](https://www.mongodb.com/docs/manual/core/aggregation-pipeline).

Como alternativa al [MapReduce](https://www.mongodb.com/docs/manual/core/map-reduce/), que usa JavaScript, considere usar el [Marco de Agregación](https://www.mongodb.com/docs/manual/core/aggregation-pipeline). A diferencia de Map/Reduce, usa un lenguaje idiomático para construir consultas, sin tener que escribir y usar el enfoque más lento de JavaScript que requiere Map/Reduce.

El comando [eval](https://www.mongodb.com/docs/manual/reference/command/eval/) ha sido deprecado desde MongoDB 3.0 y también debe evitarse.
