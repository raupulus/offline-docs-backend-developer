---
title: Conexiones y gestor de conexión
source_url: https://www.php.net/manual/es/pdo.connections.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/connections.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_revision: e7e4ffe9a
order: 61750
---

## Conexiones y gestor de conexión

Las conexiones se establecen creando instancias de la clase base de PDO. No importa qué controlador se desee utilizar; siempre se utiliza el nombre de la clase PDO. El constructor acepta argumentos para especificar la fuente de la base de datos (conocida como DSN) y opcionalmente, el nombre de usuario y la contraseña (si los hay).

Conexión a MySQL

```php
<?php
$dbh = new PDO('mysql:host=localhost;dbname=test', $user, $pass);
?>

   
```

Si existen errores de conexión, se lanza un objeto `PDOException`. Este error puede ser capturado si se desea gestionar la excepción, o bien puede ser tratado por el gestor global de excepciones definido mediante la función `set_exception_handler`.

Gestión de errores de conexión

```php
<?php
try {
    $dbh = new PDO('mysql:host=localhost;dbname=test', $user, $pass);
} catch (PDOException $e) {
    // intentar reintentar la conexión después de un cierto tiempo, por ejemplo
}

   
```

> [!WARNING]
> Al igual que todas las demás [excepciones](#language.exceptions), `PDOException` puede ser capturada ya sea explícitamente, mediante una instrucción [`catch`](#language.exceptions.catch), o implícitamente a través de `set_exception_handler`. De lo contrario, se producirá el comportamiento por defecto de convertir una excepción no capturada en una `E_FATAL_ERROR`. El error fatal contendrá un backtrace que podría revelar detalles sobre la conexión. Por lo tanto, la opción `php.ini` [`display_errors`](#ini.display-errors) debe estar configurada a `0` en un servidor de producción.

Cuando la conexión a la base de datos tiene éxito, se devuelve una instancia de la clase PDO al script. La conexión permanece activa mientras el objeto PDO lo esté. Para cerrar la conexión, se debe destruir el objeto asegurándose de que todas sus referencias sean eliminadas. Esto puede hacerse asignando `null` a la variable que gestiona el objeto. Si no se hace explícitamente, PHP cerrará automáticamente la conexión cuando el script llegue al final.

> [!NOTE]
> Si aún existen otras referencias a esta instancia PDO (por ejemplo, desde una instancia PDOStatement u otras variables que referencian la misma instancia PDO), estas también deben ser eliminadas (por ejemplo, asignando `null` a la variable que referencia el PDOStatement).

Cierre de una conexión

```php
<?php
$dbh = new PDO('mysql:host=localhost;dbname=test', $user, $pass);
// usar la conexión aquí
$sth = $dbh->query('SELECT * FROM foo');

// y ahora, cerrarla !
$sth = null;
$dbh = null;
?>

   
```

Muchas aplicaciones web utilizan conexiones persistentes a los servidores de base de datos. Las conexiones persistentes no se cierran al final del script, sino que se almacenan en caché y se reutilizan cuando otro script solicita una conexión utilizando los mismos parámetros. La caché de conexiones persistentes permite evitar establecer una nueva conexión cada vez que un script necesita acceder a una base de datos, lo que hace que la aplicación web sea más rápida.

Conexiones persistentes

```php
<?php
$dbh = new PDO('mysql:host=localhost;dbname=test', $user, $pass, array(
    PDO::ATTR_PERSISTENT => true
));
?>

   
```

El valor de la opción `PDO::ATTR_PERSISTENT` se convierte en `bool` (activar/desactivar conexiones persistentes), a menos que sea una `string` no numérica, en cuyo caso esto permite el uso de varios grupos de conexiones persistentes. Esto es útil si las conexiones diferentes utilizan parámetros incompatibles, por ejemplo, valores diferentes de `PDO::MYSQL_ATTR_USE_BUFFERED_QUERY`.

> [!NOTE]
> Si se desea utilizar conexiones persistentes, se debe utilizar el valor `PDO::ATTR_PERSISTENT` en el array de opciones del controlador pasado al constructor PDO. Si se establece este atributo con el método PDO::setAttribute después de la instanciación del objeto, el controlador no utilizará las conexiones persistentes.

> [!WARNING]
> PDO no realiza ninguna limpieza de las conexiones persistentes. Las tablas temporales, los bloqueos, las transacciones y otros cambios con estado pueden permanecer de usos anteriores de la conexión, causando problemas inesperados. Consulte la sección [Conexiones persistentes a bases de datos](#features.persistent-connections) para más información.

> [!NOTE]
> Si se utiliza el controlador PDO ODBC y si su librería ODBC soporta el pool de conexiones ODBC (tanto unixODBC como Windows lo soportan; puede ser más), entonces se recomienda no utilizar las conexiones persistentes PDO, sino dejar que el pool de conexiones ODBC almacene en caché las conexiones. El pool de conexiones ODBC es compartido con otros módulos en el proceso; si PDO almacena en caché la conexión, entonces esta conexión nunca será devuelta por el pool de conexiones ODBC, lo que hace que se creen múltiples conexiones para otros módulos.
