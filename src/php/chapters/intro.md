---
title: Introducción ¿Qué es PHP y qué puede hacer?
source_url: https://www.php.net/manual/es/introduction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: chapters/intro.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: chapters
translation_status: ready
translation_reviewed: true
translation_revision: 0bae88c19
order: 1360
---

## ¿Qué es PHP y qué puede hacer?

## ¿Qué es PHP?

PHP (oficialmente, este sigle es un acrónimo recursivo para *PHP Hypertext Preprocessor*) es un lenguaje de scripts generalista y Open Source, especialmente concebido para el desarrollo de aplicaciones web. Puede ser integrado fácilmente al HTML.

Bien... pero ¿qué significa esto? Un ejemplo:

```php
<!DOCTYPE html>
<html>
<head>
<title>Ejemplo</title>
</head>
<body>

<?php
echo "Hola, soy un script PHP!";
?>

</body>
</html>

    
```

En lugar de utilizar toneladas de comandos para mostrar HTML (como en C o en Perl), las páginas PHP contienen fragmentos HTML con código que hace \<"algo"\> (en este caso, mostrará `"Hola, soy un script PHP!"`). El código PHP está incluido entre [una etiqueta de inicio `<?php` y una etiqueta de fin `?>`](#language.basic-syntax.phpmode) que permiten al servidor web pasar al “modo PHP”.

Lo que distingue a PHP de los lenguajes de script como JavaScript, es que el código se ejecuta en el servidor, generando así el HTML, que será luego enviado al cliente. El cliente solo recibe el resultado del script, sin ningún medio de acceso al código que produjo dicho resultado. Se puede configurar el servidor web para que analice todos los ficheros HTML como ficheros PHP. Así, no hay manera de distinguir las páginas que son producidas dinámicamente de las páginas estáticas. Un servidor web puede incluso ser configurado para procesar todos los ficheros HTML con PHP, y no hay manera para los usuarios de saber que PHP está siendo utilizado.

La gran ventaja de PHP es que es extremadamente simple para los principiantes, pero ofrece funcionalidades avanzadas para los expertos. No tema leer la larga lista de funcionalidades PHP. Con PHP, casi todo el mundo puede comenzar rápidamente y escribir scripts simples en poco tiempo.

Aunque el desarrollo de PHP está orientado hacia la programación para sitios web, se puede hacer mucho más con PHP. Lea la sección [¿Qué puede hacer PHP?](#intro-whatcando) o el [tutorial de introducción](#tutorial) para pasar directamente al aprendizaje de la programación web.

## ¿Qué puede hacer PHP?

Todo. PHP está principalmente concebido para servir como lenguaje de script del lado del servidor, por lo que puede hacer todo lo que cualquier otro programa CGI puede hacer, como recolectar datos de formularios, generar contenido dinámico, o gestionar cookies. Pero PHP puede hacer mucho más.

Hay dos ámbitos diferentes donde PHP puede destacar.

- Lenguaje de script del lado del servidor. Este es el uso más tradicional, y también el principal objetivo de PHP. Tres componentes son necesarios para explotarlo: un analizador PHP (CGI o módulo del servidor), un servidor web y un navegador web. Se debe ejecutar el servidor web en correlación con PHP. Se puede acceder al programa PHP con la ayuda del navegador web. Todo esto puede funcionar en una máquina local solo para experimentar la programación PHP. Vea la sección [de instalación](#install) para más información.

- Lenguaje de programación en línea de comandos. Un script PHP puede ser ejecutado en línea de comandos, sin la ayuda del servidor web y de un navegador. Solo se necesita el ejecutable PHP. Este uso es ideal para los scripts que se ejecutan regularmente con un `cron` en Unix o Linux o un gestor de tareas (en Windows). Estos scripts también pueden ser utilizados para realizar operaciones en ficheros de texto. Vea la sección sobre el uso de PHP en [línea de comandos](#features.commandline) para más información.

PHP es [utilizable](#install) en la mayoría de los sistemas operativos, como Linux, muchas variantes Unix (incluyendo HP-UX, Solaris y OpenBSD), Microsoft Windows, macOS, RISC OS y otros más. PHP también soporta la mayoría de los servidores web actuales como Apache, IIS y muchos otros. Y esto incluye todos los servidores web que pueden utilizar el binario PHP FastCGI, como lighttpd y nginx. PHP funciona como módulo, o como procesador CGI.

Con PHP, los desarrolladores tienen la opción del sistema operativo y del servidor web. Además, también tienen la opción de utilizar la programación procedimental u orientada a objetos (OOP), o incluso una mezcla de ambas.

Con PHP, no se limita a la producción de código HTML. Las capacidades de PHP incluyen la creación de tipos de ficheros ricos, como imágenes o ficheros PDF, el cifrado de datos y el envío de correos electrónicos. También puede generar fácilmente cualquier texto, como JSON o XML. PHP puede generar automáticamente estos ficheros y guardarlos en el sistema de ficheros en lugar de imprimirlos, formando así una caché del lado del servidor para contenido dinámico.

Una de las fortalezas más significativas de PHP es que soporta [enormemente bases de datos](#refs.database). Escribir una página web que utilice una base de datos se vuelve extremadamente simple, utilizando una de las extensiones específicas para bases de datos (i.e., para [mysql](#book.mysqli)), o utilizando una clase de abstracción como [PDO](#book.pdo), o una conexión a cualquier base de datos que soporte la conexión estándar abierta a través de la extensión [ODBC](#book.uodbc). Otras bases de datos pueden utilizar la extensión [cURL](#book.curl) o [sockets](#book.sockets) como CouchDB.

PHP soporta numerosos protocolos como LDAP, IMAP, SNMP, NNTP, POP3, HTTP, COM (en Windows) y muchos otros. También puede abrir sockets de red e interactuar con cualquier otro protocolo.

PHP posee funcionalidades útiles en el [tratamiento de texto](#refs.basic.text), incluyendo las expresiones regulares compatibles con Perl ([PCRE](#book.pcre)), así como un gran número de extensiones y utilidades para [analizar y acceder a documentos XML](#refs.xml). PHP estandariza todas las extensiones XML sobre la sólida base de [libxml2](#book.libxml), y extiende el conjunto de funcionalidades añadiendo soporte para [SimpleXML](#book.simplexml), [XMLReader](#book.xmlreader) y [XMLWriter](#book.xmlwriter).

Muchas otras extensiones existen, categorizadas [alfabéticamente](#extensions) y por [categoría](#funcref). Y finalmente, existen [extensiones PECL](#install.pecl.intro) que pueden (o no) estar documentadas en el manual PHP, como [XDebug](http://xdebug.org/).

Esta página no es lo suficientemente grande para listar todas las potentes funcionalidades de PHP. Lea la sección sobre [la instalación de PHP](#install) y estudie la [lista de funciones](#funcref) para obtener más detalles sobre todas estas tecnologías.
