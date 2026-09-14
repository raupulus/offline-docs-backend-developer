---
title: Instalación
source_url: https://www.php.net/manual/es/mysql.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_reviewed: true
translation_revision: 15d88bef8
order: 52000
---

## Instalación

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:

Para compilar, simplemente se debe utilizar la opción de configuración `--with-mysql[=DIR]` donde el parámetro opcional `[DIR]` apunta hacia el directorio de instalación de MySQL.

Aunque esta extensión MySQL sea compatible con MySQL 4.1.0 y superior, no soporta las funcionalidades adicionales que esta versión proporciona. Para ello, se recomienda utilizar la extensión [MySQLi](#book.mysqli).

Si se desea instalar la extensión mysqli al mismo tiempo que la extensión mysql, se debe utilizar la misma biblioteca cliente para evitar conflictos.

## Instalación en sistemas Linux

Nota: `[DIR]` es la ruta hacia la biblioteca cliente MySQL (*encabezados y bibliotecas*), que puede ser descargada desde el sitio de [MySQL](http://www.mysql.com/).

| PHP Versión | Por defecto | Opciones de configuración: [mysqlnd](#mysqlnd.overview) | Opciones de configuración: `libmysqlclient` | Historial de cambios |
|----|----|----|----|----|
| 4.x.x | libmysqlclient | No Disponible | `--without-mysql` para desactivar | MySQL está activo por omisión, las bibliotecas cliente MySQL están incluidas internamente |
| 5.0.x, 5.1.x, 5.2.x | libmysqlclient | No Disponible | `--with-mysql=[DIR]` | MySQL no está activo por omisión, y las bibliotecas cliente MySQL ya no están incluidas internamente |
| 5.3.x | libmysqlclient | `--with-mysql=mysqlnd` | `--with-mysql=[DIR]` | mysqlnd está ahora disponible |
| 5.4.x | mysqlnd | `--with-mysql` | `--with-mysql=[DIR]` | mysqlnd está ahora incluido por omisión |

Matriz de soporte de ext/mysql {#mysql.installation.compile.support}

## Instalación en sistemas Windows

### PHP 5.0.x, 5.1.x, 5.2.x

MySQL ya no está activado por omisión, por lo tanto, la biblioteca `php_mysql.dll` debe ser activada en el `php.ini`. Además, PHP debe tener acceso a la biblioteca cliente MySQL. Un fichero llamado `libmysql.dll` está incluido en la distribución de PHP para Windows y para que PHP pueda comunicarse con MySQL, este fichero debe estar disponible en el `PATH` del sistema Windows. Lea la FAQ titulada "[¿Dónde debo añadir mi directorio PHP a la variable `PATH` en Windows?](#faq.installation.addtopath)" para más información sobre cómo realizar esto. No obstante, copiar el fichero `libmysql.dll` en el directorio sistema de Windows funciona (ya que el directorio sistema está por omisión en el `PATH` del sistema), pero esto no es recomendado en absoluto.

Para activar cualquier extensión PHP (como `php_mysql.dll`), la directiva PHP [extension_dir](#ini.extension-dir) debe estar definida y debe apuntar hacia el directorio donde están almacenadas las extensiones PHP. Lea también el [manual de instalación en Windows](#install.windows.manual). Por ejemplo, aquí hay un valor posible para la directiva extension_dir en PHP 5: `c:\php\ext`

> [!NOTE]
> Si al iniciar el servidor web aparece un error similar a este: `"Unable to load dynamic library './php_mysql.dll'"`, es porque `php_mysql.dll` y/o `libmysql.dll` no pudieron ser encontrados por el sistema.

### PHP 5.3.0+

El [driver MySQL nativo](#mysqlnd.overview) está activado por omisión. Incluya `php_mysql.dll`, pero `libmysql.dll` ya no es necesario, ni utilizado.

## Notas sobre la instalación de MySQL

> [!WARNING]
> Pueden encontrarse fallos y problemas de inicio de PHP cuando se carga esta función al mismo tiempo que la extensión recode. Consulte la extensión [recode](#ref.recode) para más detalles.

> [!NOTE]
> Si se necesitan otros juegos de caracteres que el predeterminado (*latino*), se debe instalar la biblioteca externa libmysqlclient (no proporcionada), compilada con este juego de caracteres.
