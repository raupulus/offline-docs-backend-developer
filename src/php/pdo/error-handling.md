---
title: Los errores y su gestión
source_url: https://www.php.net/manual/es/pdo.error-handling.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/error-handling.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: true
translation_revision: 1508d46d0
order: 61790
---

## Los errores y su gestión

PDO ofrece 3 formas diferentes de gestionar los errores para adaptarse mejor a la aplicación.

- `PDO::ERRMODE_SILENT`

  Anterior a PHP 8.0.0, este es el modo por omisión. PDO define simplemente el código de error para ser inspeccionado mediante los métodos PDO::errorCode y PDO::errorInfo en los objetos que representan las consultas, así como en los que representan las bases de datos; si el error resulta de una llamada al objeto que representa la consulta, se puede llamar al método PDOStatement::errorCode o al método PDOStatement::errorInfo en el objeto. Si el error resulta de una llamada al objeto que representa una base de datos, también se pueden llamar estos dos mismos métodos en el objeto.

- `PDO::ERRMODE_WARNING`

  Además de definir el código de error, PDO emitirá un mensaje E_WARNING tradicional. Esta configuración es útil durante las pruebas y el depurado, si se desea ver el problema sin interrumpir la aplicación.

- `PDO::ERRMODE_EXCEPTION`

  A partir de PHP 8.0.0, este es el modo por omisión. Además de definir el código de error, PDO lanzará una excepción `PDOException` y definirá las propiedades para representar el código de error y la información complementaria. Esta configuración es igualmente útil durante el depurado, ya que permitirá "saltar" el punto crítico del código, mostrando rápidamente el problema encontrado (recuerde: las transacciones son automáticamente revertidas si la excepción hace que el script termine).

  El modo "excepción" es también muy útil ya que permite estructurar el gestor de errores de forma más clara que con las alertas tradicionales de PHP y, además, con menos código que cuando se ejecuta el código en modo silencio, y se verifica sistemáticamente los valores devueltos después de cada llamada a la base de datos.

  Ver el capítulo sobre las [excepciones](#language.exceptions) para más información sobre las excepciones en PHP.

PDO utiliza los códigos de error SQL-92 SQLSTATE; cada controlador PDO es responsable de vincular sus códigos nativos a los códigos SQLSTATE apropiados. El método PDO::errorCode devuelve un código SQLSTATE único. Si se necesitan información específica sobre el error, PDO también ofrece el método PDO::errorInfo que devuelve un array conteniendo el código SQLSTATE, el código de error específico del controlador y la cadena describiendo el error proveniente del controlador.

Creación de una instancia PDO y definición del modo de error

```php
<?php
$dsn = 'mysql:dbname=testdb;host=127.0.0.1';
$user = 'dbuser';
$password = 'dbpass';

$dbh = new PDO($dsn, $user, $password);
$dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Esto provocará una PDOException (cuando la tabla no existe).
$dbh->query("SELECT wrongcolumn FROM wrongtable");
?>

   
```

El ejemplo anterior mostrará:

    Fatal error: Uncaught PDOException: SQLSTATE[42S02]: Base table or view not found: 1146 Table 'testdb.wrongtable' doesn't exist in /tmp/pdo_test.php:10
    Stack trace:
    #0 /tmp/pdo_test.php(10): PDO->query('SELECT wrongcol...')
    #1 {main}
      thrown in /tmp/pdo_test.php on line 10

> [!NOTE]
> PDO::\_\_construct siempre lanza una excepción `PDOException` si la conexión falla, independientemente de la configuración de `PDO::ATTR_ERRMODE`.

Crea una instancia PDO y define el modo de error desde el constructor

```php
<?php
$dsn = 'mysql:dbname=test;host=127.0.0.1';
$user = 'googleguy';
$password = 'googleguy';

$dbh = new PDO($dsn, $user, $password, array(PDO::ATTR_ERRMODE => PDO::ERRMODE_WARNING));

// Esto hará que PDO lance un error de nivel E_WARNING en lugar de una excepción (cuando la tabla no existe)
$dbh->query("SELECT wrongcolumn FROM wrongtable");
?>

   
```

El ejemplo anterior mostrará:

    Warning: PDO::query(): SQLSTATE[42S02]: Base table or view not found: 1146 Table 'test.wrongtable' doesn't exist in
    /tmp/pdo_test.php on line 9
