---
title: Seguridad en bases de datos
source_url: https://www.php.net/manual/es/security.database.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: security/database.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: security
translation_status: ready
translation_revision: 7204e2dbb
order: 109920
---

## Seguridad en bases de datos

Hoy en día, las bases de datos son componentes esenciales de cualquier aplicación web, permitiendo a los sitios web proveer variedad de contenido dinámico. Puesto que se puede almacenar información muy delicada o secreta en una base de datos, debería considerarse ampliamente proteger las bases de datos.

Para obtener o almacenar cualquier información, es necesario conectarse a la base de datos, enviar una consulta válida, obtener el resultado, y cerrar la conexión. Hoy en día, el lenguaje de consultas más utilizado en esta interacción es el Lenguaje Estructurado de Consultas (SQL, por sus siglas en inglés). Vea como un atacante puede [realizar manipulaciones maliciosas con una consulta SQL](#security.database.sql-injection).

Como es de suponer, PHP no puede proteger una base de datos por sí mismo. Las siguientes secciones tienen como objetivo ser una introducción básica de cómo acceder y manipular bases de datos dentro de scripts de PHP.

Tenga en mente esta sencilla regla: Protección en profundidad. En cuantos más sitios se tomen acciones para aumentar la protección de una base de datos, menor es la probabilidad de que un atacante tenga éxito en exponer o abusar de cualquier información que tenga almacenada. Un buen diseño del esquema de la base de datos y de la aplicación se ocupará de sus mayores temores.

## Diseño de bases de datos

El primer paso es siempre crear una base de datos, a menos que se quiera utilizar una de un tercero. Cuando se crea una base de datos, esta es asignada a un propietario, aquel que ejecutó la sentencia de creación. Usualmente, sólo el propietario (o un superusuario) puede hacer cualquier cosa con los objetos de esa base de datos. Para que otros usuarios puedan utilizarla, se les deben conceder privilegios.

Las aplicaciones nunca deberían conectarse a la base de datos como su propietario o como un superusuario, porque estos usuarios pueden ejecutar cualquier consulta a su antojo; por ejemplo, modificar el esquema (p.ej., eliminar tablas) o borrar su contenido por completo.

Se pueden crear distintos usuarios de una base de datos para cada aspecto de la aplicación con permisos muy limitados a los objetos de dicha base de datos. Solamente deberían otorgarse los privilegios necesarios, evitando así que el mismo usuario pueda interactuar con la base de datos en diferentes casos y uso. Esto significa que si un intruso obtiene acceso a una base de datos utilizando las credenciales de la aplicación, solamente puede efectuar los cambios que la aplicación permita.

## Conexión a una base de datos

Se pueden establecer las conexiones sobre SSL para cifrar las comunicaciones cliente/servidor y aumentar la seguridad, o también emplear ssh para cifrar la conexión de red entre los clientes y el servidor de bases de datos. Si se utiliza algunas de estas opciones, será difícil para un posible atacante la monitorización del tráfico y la obtención de información de la base de datos.

## Modelo de almacenamiento cifrado

SSL/SSH protege los datos que viajan desde el cliente al servidor: SSL/SSH no protege los datos persistentes almacenados en una base de datos. SSL es un protocolo que protege los datos mientras viajan por el cable.

Una vez que un atacante obtiene acceso directo a una base de datos (eludiendo el servidor web), los datos sensibles almacenados podrían ser divulgados o mal utilizados, a menos que la información esté protegida por la base de datos misma. Cifrar los datos es una buena forma de mitigar esta amenaza, pero muy pocas bases de datos ofrecen este tipo de cifrado de datos.

La forma más sencilla para evitar este problema es crear primero un paquete de cifrado propio y utilizarlo en los scripts de PHP. Hay muchas extensiones de PHP que pueden ser de ayuda para esto, tales como [OpenSSL](#book.openssl) y [Sodium](#book.sodium), cubriendo así una amplia variedad de algoritmos de cifrado. El script cifra los datos antes de insertarlos en la base de datos, y los descifra al obtenerlos. Véanse las referencias para ejemplos adicionales del funcionamiento del cifrado.

### 'Hashing'

En caso de datos que deban estar realmente ocultos, si no fuera necesaria su representación real, (es decir, que no sean mostrados), quizás convenga utilizar algoritmos hash. El ejemplo más típico del uso del hash es a la hora de almacenar el hash criptográfico de una contraseña en una base de datos, en lugar de almacenar la contraseña en sí.

Las funciones de [password](#ref.password) proporcionan una forma adecuada de utilizar hash con datos delicados y trabajar con estos hash.

`password_hash` se emplea para usar un hash con una cadena dada utilizando el algoritmo más fuerte actualmente disponible, mientras que `password_verify` comprueba si la contraseña dada coincide con el hash almacenado en la base de datos.

Campo de contraseña con hash

```php
<?php

// Almacenar el hash de la contraseña
$query  = sprintf("INSERT INTO users(name,pwd) VALUES('%s','%s');",
            pg_escape_string($nombre_usuario),
            password_hash($password, PASSWORD_DEFAULT));
$result = pg_query($connection, $query);

// Consultar si el usuario envió la contraseña correcta
$query = sprintf("SELECT pwd FROM users WHERE name='%s';",
                pg_escape_string($nombre_usuario));
$row = pg_fetch_assoc(pg_query($connection, $query));

if ($row && password_verify($contraseña, $row['pwd'])) {
    echo 'Bienvenido, ' . htmlspecialchars($username) . '!';
} else {
    echo 'La autenticación ha fallado para ' . htmlspecialchars($username) . '.';
}

?>

    
```

## Inyección de SQL

La inyección SQL es una técnica en la que un atacante aprovecha fallas en el código de la aplicación encargado de construir consultas SQL dinámicas. El atacante puede obtener acceso a secciones privilegiadas de la aplicación, recuperar toda la información de la base de datos, manipular datos existentes o incluso ejecutar comandos peligrosos a nivel del sistema en el host de la base de datos. La vulnerabilidad ocurre cuando los desarrolladores concatenan o interpolan entrada arbitraria en sus declaraciones SQL.

Dividir el conjunto de resultados en páginas ... y crear superusuarios (PostgreSQL)

En el siguiente ejemplo, la entrada del usuario se interpola directamente en la consulta SQL, lo que permite al atacante obtener una cuenta de superusuario en la base de datos.

```php
<?php

$offset = $_GET['offset']; // ¡Cuidado, no hay validación en la entrada de datos!
$query  = "SELECT id, name FROM products ORDER BY name LIMIT 20 OFFSET $offset;";
$result = pg_query($conn, $query);

?>

    
```

Un usuario común hace clic en los enlaces 'siguiente' o 'atrás' donde el `$índice` está codificado en el URL. El script espera que el `$índice` entrante sea un número. Sin embargo, Qué sucede si alguien intenta ingresar al añadir lo siguiente a la URL?

```php
0;
insert into pg_shadow(usename,usesysid,usesuper,usecatupd,passwd)
    select 'crack', usesysid, 't','t','crack'
    from pg_shadow where usename='postgres';
--

    
```

Si ocurriera, el script presentaría un acceso de superusuario al atacante. Observe que `0;` es para proveer un índcie válido a la consulta original y así finalizarla.

> [!NOTE]
> Es una técnica común forzar al analizador SQL a ignorar el resto de la consulta escrita por el desarrollador con `--`, lo cual representa un comentario en SQL.

Una forma factible de obtener contraseñas es burlar las páginas de búsqueda de resultados. Lo único que el atacante necesita hacer es ver si hay variables que hayan sido enviadas y sean empleadas en sentencias SQL que no sean manejadas apropiadamente. Estos filtros se pueden establecer comunmente en un formulario anterior para personalizar las cláusulas `WHERE, ORDER BY, LIMIT` y `OFFSET` en las sentencias `SELECT`. Si la base de datos admite el constructor `UNION`, el atacante podría intentar anteponer una consulta entera a la consulta original para enumerar las contraseñas de una tabla arbitraria. Se recomienda encarecidamente almacenar solo hashes seguros de contraseñas en lugar de las contraseñas mismas.

Enumerar artículos ... y algunas contraseñas (cualquier servidor de bases de datos)

```php
<?php

$query  = "SELECT id, name, inserted, size FROM products
           WHERE size = '$size'";
$result = odbc_exec($conexión, $query);

?>

    
```

La parte estática de la consulta se puede combinar con otra sentencia `SELECT` la cual revelará todas las contraseñas:

```php
'
union select '1', concat(uname||'-'||passwd) as name, '1971-01-01', '0' from usertable;
--

    
```

Las declaraciones `UPDATE` e `INSERT` también son susceptibles a este tipo de ataques.

Desde restablecer una contraseña ... hasta obtener más privilegios (cualquier servidor de bases de datos)

```php
<?php
$query = "UPDATE usertable SET pwd='$pwd' WHERE uid='$uid';";
?>

    
```

Si un usuario malicioso podría enviar el valor `' or uid like'%admin%` a `$uid` para cambiar la contraseña del administrador, o simplemente cambiar `$pwd` a `jejeje', trusted=100, admin='yes` para obtener más privilegios, entonces la consulta se tornaría:

```php
<?php

// $uid: ' or uid like '%admin%
$query = "UPDATE usertable SET pwd='...' WHERE uid='' or uid like '%admin%';";

// $pwd: jejeje', trusted=100, admin='yes
$query = "UPDATE usertable SET pwd='jejeje', trusted=100, admin='yes' WHERE
...;";

?>

    
```

Aunque sigue siendo evidente que un atacante debe poseer al menos cierto conocimiento de la arquitectura de la base de datos para llevar a cabo un ataque exitoso, obtener esta información a menudo es muy simple. Por ejemplo, el código puede ser parte de un software de código abierto y estar disponible públicamente. Esta información también puede ser revelada por código fuente cerrado, incluso si está codificado, ofuscado o compilado, e incluso por tu propio código a través de la visualización de mensajes de error. Otros métodos incluyen el uso de nombres de tablas y columnas típicos. Por ejemplo, un formulario de inicio de sesión que utiliza una tabla 'users' con nombres de columnas 'id', 'username' y 'password'.

Atacar el sistema operativo del host de la base de datos (MSSQL Server)

Un ejemplo alarmante de cómo los comandos a nivel del sistema operativo pueden ser accedidos en algunos hosts de bases de datos.

```php
<?php

$query  = "SELECT * FROM products WHERE id LIKE '%$prod%'";
$result = mssql_query($query);

?>

    
```

Si un atacante envía el valor `a%' exec master..xp_cmdshell 'net user test testpass /ADD' --` a `$prod`, la `$query` será:

```php
<?php

$query  = "SELECT * FROM products
              WHERE id LIKE '%a%'
              exec master..xp_cmdshell 'net user test testpass /ADD' --%'";
$result = mssql_query($query);

?>

    
```

El servidor MSSQL ejecuta la sentencia SQL en el lote incluyendo un comando para añadir un usuario nuevo a la base de datos de cuentas local. Si esta aplicación estaban siendo ejecutados como `sa` y el servicio MSSQLSERVER estaba ejecutando con los privilegios suficientes, el atacante ahora podría tener una cuenta con la cual acceder a esta máquina.

> [!NOTE]
> Algunos ejemplos anteriores están vinculados a un servidor de bases de datos específico, pero esto no significa que un ataque similar sea imposible contra otros productos. Tu servidor de bases de datos puede ser igualmente vulnerable de otra manera.

![Un ejemplo divertido de los problemas relacionados con la inyección SQL.](en/security/figures/xkcd-bobby-tables.png)

### Técnicas de evitación

La forma recomendada de evitar la inyección SQL es vincular todos los datos mediante declaraciones preparadas. Utilizar consultas parametrizadas no es suficiente para evitar por completo la inyección SQL, pero es la manera más fácil y segura de proporcionar datos a las declaraciones SQL. Todas las literales de datos dinámicos en las cláusulas `WHERE`, `SET`, y `VALUES` deben ser reemplazadas con marcadores de posición. Los datos reales se vincularán durante la ejecución y se enviarán por separado del comando SQL.

La vinculación de parámetros solo puede utilizarse para datos. Otras partes dinámicas de la consulta SQL deben filtrarse contra una lista conocida de valores permitidos.

Evitar la inyección SQL mediante el uso de declaraciones preparadas con PDO

```php
<?php

// La parte dinámica del SQL se valida contra valores esperados
$sortingOrder = $_GET['sortingOrder'] === 'DESC' ? 'DESC' : 'ASC';
$productId = $_GET['productId'];
// El SQL se prepara con un marcador de posición
$stmt = $pdo->prepare("SELECT * FROM products WHERE id LIKE ? ORDER BY price {$sortingOrder}");
// El valor se proporciona con comodines LIKE
$stmt->execute(["%{$productId}%"]);

?>

   
```

Las declaraciones preparadas son proporcionadas por [PDO](#pdo.prepared-statements), [MySQLi](#mysqli.quickstart.prepared-statements) y otras bibliotecas de bases de datos.

Los ataques de inyección SQL se basan principalmente en explotar código que no ha sido escrito teniendo en cuenta la seguridad. Nunca confíes en ninguna entrada, especialmente desde el lado del cliente, incluso si proviene de un cuadro de selección, un campo de entrada oculto o una cookie. El primer ejemplo muestra que una consulta tan simple puede causar desastres.

Una estrategia de defensa en profundidad implica varias buenas prácticas de codificación:

- Nunca te conectes a la base de datos como un superusuario o como el propietario de la base de datos. Utiliza siempre usuarios personalizados con privilegios mínimos.

- Verifica si la entrada proporcionada tiene el tipo de datos esperado. PHP tiene una amplia gama de funciones de validación de entrada, desde las más simples encontradas en [Funciones de Variables](#ref.var) y en [Funciones de Tipo de Carácter](#ref.ctype) (por ejemplo, `is_numeric`, `ctype_digit` respectivamente) hasta el soporte de [Expresiones Regulares Compatibles con Perl](#ref.pcre).

- Si la aplicación espera una entrada numérica, considera verificar los datos con `ctype_digit`, cambiar silenciosamente su tipo usando `settype`, o usar su representación numérica con `sprintf`.

- Si la capa de la base de datos no admite la vinculación de variables, entonces coloca comillas alrededor de cada valor proporcionado por el usuario que no sea numérico y que se pase a la base de datos con la función de escape de cadena específica de la base de datos (por ejemplo, `mysql_real_escape_string`, `sqlite_escape_string`, etc.). Las funciones genéricas como `addslashes` son útiles solo en un entorno muy específico (por ejemplo, MySQL en un conjunto de caracteres de un solo byte con `NO_BACKSLASH_ESCAPES` deshabilitado), así que es mejor evitarlas.

- No imprimas ninguna información específica de la base de datos, especialmente sobre el esquema, por las buenas o por las malas. Consulta también [Informes de Errores](#security.errors) y [Funciones de Manejo y Registro de Errores](#ref.errorfunc).

Además, se puede beneficiar del registro de consultas, ya sea dentro de un script o mediante la base de datos en sí misma, si es que lo soporta. Obviamente, llevar un registro no previene los intentos dañinos, aunque puede ser útil para realizar un seguimiento de las aplicación que han sido eludidas. El registro no es útil por sí mismo sino por la información que contiene. Normalmente cuantos más detalles, mejor.
