---
title: Transacciones y validación automática (autocommit)
source_url: https://www.php.net/manual/es/pdo.transactions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/transactions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: true
translation_revision: 969a4a706
order: 62240
---

## Transacciones y validación automática (autocommit)

Ahora que se ha establecido la conexión mediante PDO, es necesario comprender cómo PDO gestiona las transacciones antes de ejecutar consultas. Si nunca se han utilizado transacciones, estas ofrecen 4 características principales: Atomicidad, Consistencia, Aislamiento y Durabilidad (ACID). En otras palabras, cualquier trabajo realizado en una transacción, incluso si se efectúa por etapas, está garantizado de aplicarse a la base de datos sin riesgo y sin interferencia para otras conexiones, cuando se valida. El trabajo de las transacciones también puede ser automáticamente anulado a solicitud, siempre que no se haya validado nada aún, lo que facilita considerablemente la gestión de errores en los scripts.

Las transacciones se implementan típicamente para aplicar todas las modificaciones de una sola vez; esto tiene el efecto de mejorar radicalmente la eficiencia de las actualizaciones. En otras palabras, las transacciones hacen que los scripts sean más rápidos y potencialmente más robustos (deben usarse correctamente para disfrutar de estos beneficios).

Desafortunadamente, no todas las bases de datos soportan transacciones, por lo que PDO debe ejecutarse en modo "autocommit" al abrir la conexión por primera vez. El modo "autocommit" significa que todas las consultas que se ejecutan tienen sus transacciones implícitas, si la base de datos las soporta, o ninguna transacción si la base de datos no las soporta. Si se necesita una transacción, debe usarse el método PDO::beginTransaction para inicializarla. Si el controlador utilizado no soporta transacciones, se lanzará una excepción PDO (de acuerdo con el gestor de errores: esto siempre es un error grave). Una vez dentro de una transacción, debe usarse la función PDO::commit o la función PDO::rollBack para terminarla, según el éxito del código durante la transacción.

> [!WARNING]
> PDO solo verifica la posibilidad de usar transacciones al nivel del controlador. Si ciertas condiciones durante la ejecución impiden que las transacciones funcionen, PDO::beginTransaction devolverá `true` sin error si el servidor acepta iniciar una transacción.
>
> Un ejemplo sería usar transacciones en tablas con formato MyISAM del servidor de base de datos MySQL.

> [!WARNING]
> *Commit implícito con declaraciones DDL:* Algunas bases de datos emiten automáticamente un `COMMIT` implícito cuando se ejecuta una declaración de lenguaje de definición de base de datos (DDL), como `DROP TABLE` o `CREATE TABLE`, dentro de una transacción. Esto significa que todas las modificaciones anteriores realizadas en la misma transacción serán *automáticamente validadas* y no pueden ser anuladas.
>
> `MySQL` y `Oracle` son ejemplos de bases de datos que presentan este comportamiento.

Ejemplo de Commit implícito

```php
<?php
$pdo->beginTransaction();
$pdo->exec("INSERT INTO users (name) VALUES ('Rasmus')");
$pdo->exec("CREATE TABLE test (id INT PRIMARY KEY)"); // Un COMMIT implícito ocurre aquí
$pdo->rollBack(); // Esto NO anulará el INSERT/CREATE para MySQL o Oracle
?>

    
```

*Mejor práctica:* Evite ejecutar declaraciones DDL dentro de transacciones si se usan bases de datos que imponen este comportamiento. Si es necesario, separe las operaciones DDL de la lógica transaccional.

Cuando el script finaliza o cuando la conexión está a punto de cerrarse, si hay una transacción en curso, PDO la anulará automáticamente. Esta es una medida de seguridad para garantizar la integridad de los datos en caso de que el script finalice de manera inesperada. Si no se valida explícitamente la transacción, entonces se presume que algo salió mal y la anulación de la transacción ocurre para garantizar la seguridad de los datos.

> [!WARNING]
> La anulación automática ocurre si se inició la transacción mediante PDO::beginTransaction. Si se ejecutó manualmente una consulta que comienza una transacción, PDO no tiene forma de saberlo y por lo tanto, no anulará automáticamente esa transacción si algo salió mal.

Ejecución de un grupo en una transacción

En el siguiente ejemplo, supongamos que vamos a crear un conjunto de entradas para un nuevo empleado, cuyo número de ID será 23. Además de los datos básicos sobre esta persona, también se debe registrar su salario. Es muy simple realizar dos actualizaciones separadas, pero al encerrarlas en las llamadas a las funciones PDO::beginTransaction y PDO::commit, se garantiza que nadie pueda ver estas modificaciones hasta que estén completas. Si algo sale mal, el bloque de captura anulará todas las modificaciones realizadas desde el inicio de la transacción y mostrará un mensaje de error.

```php
<?php
try {
  $dbh = new PDO('odbc:SAMPLE', 'db2inst1', 'ibmdb2',
      array(PDO::ATTR_PERSISTENT => true));
  echo "Conectado\n";
} catch (Exception $e) {
  die("No se pudo conectar: " . $e->getMessage());
}

try {
  $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

  $dbh->beginTransaction();
  $dbh->exec("insert into staff (id, first, last) values (23, 'Joe', 'Bloggs')");
  $dbh->exec("insert into salarychange (id, amount, changedate)
      values (23, 50000, NOW())");
  $dbh->commit();

} catch (Exception $e) {
  $dbh->rollBack();
  echo "Falló: " . $e->getMessage();
}
?>

   
```

No hay límite en el número de actualizaciones en una transacción; también pueden realizarse consultas complejas y, por supuesto, usar estas informaciones para construir otras actualizaciones y consultas; durante la actividad de la transacción, se está seguro de que nadie más puede realizar modificaciones mientras se está en medio de las propias modificaciones. Para más información sobre transacciones, consulte la documentación proporcionada por su base de datos.
