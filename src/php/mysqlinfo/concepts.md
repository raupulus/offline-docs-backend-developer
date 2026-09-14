---
title: Conceptos
source_url: https://www.php.net/manual/es/mysqlinfo.concepts.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqlinfo/concepts.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqlinfo
translation_status: ready
translation_reviewed: false
translation_revision: 7cff4d34f
order: 56100
---

## Conceptos

Estos conceptos son específicos para los drivers MySQL para PHP.

## Consultas con o sin almacenamiento en memoria

Las consultas utilizan por omisión el modo de almacenamiento en memoria. Esto significa que el resultado de las consultas se transfiere inmediatamente del servidor MySQL a PHP y se conserva en la memoria del proceso PHP. Esto permite operaciones complementarias como contar el número de resultados, y desplazar el puntero de resultado actual. También permite ejecutar consultas adicionales sobre la misma conexión mientras se trabaja con el conjunto de resultados. La desventaja del almacenamiento en memoria es que los conjuntos de resultados grandes pueden requerir mucha más memoria. La memoria permanecerá ocupada hasta que todas las referencias a los conjuntos de resultados sean desactivadas o que los conjuntos de resultados sean liberados explícitamente, lo cual ocurre de manera automática al final del proceso. La terminología "store result" también se utiliza con el modo de almacenamiento en memoria, ya que la totalidad de los resultados se almacenan a la vez.

> [!NOTE]
> Cuando se utiliza libmysqlclient como biblioteca, el límite de memoria de PHP no contará la memoria utilizada para los conjuntos de resultados a menos que los datos sean leídos en las variables PHP. Con mysqlnd, la memoria utilizada incluirá el conjunto de resultados completo.

Las consultas sin almacenamiento en memoria, las consultas MySQL ejecutan su consulta y luego esperan que los datos del servidor MySQL sean recuperados. Esto utiliza menos memoria en el lado de PHP, pero puede aumentar la carga en el servidor. A menos que el conjunto de resultados completo haya sido recuperado desde el servidor, ninguna otra consulta puede ser enviada sobre la misma conexión. Las consultas sin almacenamiento en memoria también pueden hacer referencia a un "use result". Una vez que todas las líneas del conjunto de resultados han sido recuperadas, el conjunto de resultados desaparece y ya no es posible recorrerlo nuevamente.

Siguiendo estas características, las consultas sin almacenamiento en memoria deben ser utilizadas únicamente cuando se espera obtener un gran conjunto de resultados que será procesado secuencialmente. Las consultas sin almacenamiento en memoria presentan varias trampas que las hacen más difíciles de utilizar, por ejemplo el número de líneas en el conjunto de resultados no es conocido antes de que la última línea sea recuperada.

Debido a que las consultas son almacenadas en memoria por omisión, los ejemplos a continuación muestran cómo ejecutar consultas, con cada API, sin almacenamiento en memoria.

Ejemplo de consultas sin almacenamiento en memoria: mysqli

```php
<?php
$mysqli  = new mysqli("localhost", "my_user", "my_password", "world");
$unbufferedResult = $mysqli->query("SELECT Name FROM City", MYSQLI_USE_RESULT);

foreach ($unbufferedResult as $row) {
    echo $row['Name'] . PHP_EOL;
}
?>

   
```

Ejemplo de consultas sin almacenamiento en memoria: pdo_mysql

```php
<?php
$pdo = new PDO("mysql:host=localhost;dbname=world", 'my_user', 'my_password');
$pdo->setAttribute(PDO::MYSQL_ATTR_USE_BUFFERED_QUERY, false);

$unbufferedResult = $pdo->query("SELECT Name FROM City");
foreach ($unbufferedResult as $row) {
    echo $row['Name'] . PHP_EOL;
}
?>

   
```

## Juegos de caracteres

Idealmente, un juego de caracteres adecuado debe ser definido a nivel del servidor, operación descrita en la sección [Configuración del juego de caracteres](http://dev.mysql.com/doc/mysql/en/charset-configuration.html) del manual del servidor MySQL. Alternativamente, cada API MySQL ofrece un método para definir el juego de caracteres durante la ejecución.

> [!CAUTION]
> El juego de caracteres debe ser comprendido y definido, sabiendo que tiene un efecto en cada acción, y tiene implicaciones a nivel de seguridad. Por ejemplo, el mecanismo de escape (i.e. `mysqli_real_escape_string` para mysqli, y PDO::quote para PDO_MySQL) utilizará esta configuración. Es importante tener en cuenta que estas funciones no utilizarán el juego de caracteres definido con una consulta, por lo tanto, el ejemplo siguiente no tendrá ningún efecto sobre el juego de caracteres:

Problemas al definir el juego de caracteres con SQL

```php
<?php

$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

// NO afectará $mysqli->real_escape_string();
$mysqli->query("SET NAMES utf8mb4");

// NO afectará $mysqli->real_escape_string();
$mysqli->query("SET CHARACTER SET utf8mb4");

// Pero esto afectará $mysqli->real_escape_string();
$mysqli->set_charset('utf8mb4');

// Pero esto NO lo afectará (UTF-8 en comparación con utf8mb4) -- no utilice guiones aquí
$mysqli->set_charset('UTF-8');
?>

   
```

A continuación, los ejemplos que demuestran cómo modificar correctamente el juego de caracteres durante la ejecución utilizando cada una de las APIs.

> [!NOTE]
> Debido a que los nombres de los juegos de caracteres en MySQL no contienen guiones, la cadena "utf8" es correcta en MySQL y definirá el juego de caracteres en UTF-8. La cadena "UTF-8" no es correcta, y utilizar "utf-8" fallará al modificar el juego de caracteres.

Ejemplo de definición del juego de caracteres: mysqli

```php
<?php
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

echo 'Juego de caracteres inicial: ' . $mysqli->character_set_name() . "\n";

if (!$mysqli->set_charset('utf8mb4')) {
    printf("Error al cargar el juego de caracteres utf8mb4: %s\n", $mysqli->error);
    exit;
}

echo 'Su juego de caracteres actual es: ' . $mysqli->character_set_name() . "\n";
?>

   
```

Ejemplo de definición del juego de caracteres: [pdo_mysql](#ref.pdo-mysql.connection)

```php
<?php
$pdo = new PDO("mysql:host=localhost;dbname=world;charset=utf8mb4", 'my_user', 'my_pass');
?>

   
```
