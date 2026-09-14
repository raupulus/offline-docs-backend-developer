---
title: Instalación
source_url: https://www.php.net/manual/es/ref.pdo-mysql.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_mysql/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_mysql
translation_status: ready
translation_reviewed: false
translation_revision: 70ef72d94
order: 62360
---

## Instalación

Las distribuciones Linux incluyen versiones binarias de PHP que pueden ser instaladas. Incluso si estos binarios son construidos con las extensiones MySQL, las bibliotecas clientes deben ser a menudo instaladas mediante un paquete adicional. Verifique si es el caso para su distribución.

Por ejemplo, en Ubuntu el paquete `php5-mysql` instala las extensiones PHP ext/mysql, ext/mysqli, y pdo_mysql. En CentOS, el paquete `php-mysql` también instala estas tres extensiones PHP.

Alternativamente, puede compilar esta extensión usted mismo. Construir PHP desde las fuentes permite especificar las extensiones MySQL a incluir, así como las bibliotecas clientes de cada extensión.

Durante la compilación utilice `--with-pdo-mysql[=DIR]` para instalar la extensión PDO MySQL, donde `[=DIR]` es la ruta de la biblioteca base de MySQL. [Mysqlnd](#book.mysqlnd) y la biblioteca por defecto. Para más detalles sobre la elección de la biblioteca, ver [Elegir una biblioteca MySQL](#mysqlinfo.library.choosing).

Opcionalmente, la opción `--with-mysql-sock[=DIR]` define la ruta hacia el socket Unix MySQL para todas las extensiones MySQL, incluyendo PDO_MYSQL. Si no se especifica, se utilizarán las rutas por defecto.

Opcionalmente, la opción `--with-zlib-dir[=DIR]` será utilizada para definir el prefijo de instalación zlib.

    $ ./configure --with-pdo-mysql --with-mysql-sock=/var/mysql/mysql.sock

      

El soporte SSL es activado utilizando las constantes `Pdo\Mysql::ATTR_SSL_*`, lo cual equivale a llamar a la función API C [mysql_ssl_set()](https://dev.mysql.com/doc/c-api/8.4/en/mysql-ssl-set.html). Además, SSL no puede ser activado con PDO::setAttribute ya que la conexión ya existe. Ver también la documentación MySQL sobre [la conexión a MySQL con SSL](https://dev.mysql.com/doc/en/using-encrypted-connections.html).
