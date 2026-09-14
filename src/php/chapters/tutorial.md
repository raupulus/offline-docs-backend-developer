---
title: Un tutorial sencillo
source_url: https://www.php.net/manual/es/tutorial.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: chapters/tutorial.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: chapters
translation_status: ready
translation_reviewed: false
translation_revision: 1340d3595
order: 1370
---

## Un tutorial sencillo

Aquí nos gustaría mostrar los aspectos más básicos de PHP en un tutorial breve y sencillo. Este texto solo trata sobre la creación de páginas web dinámicas con PHP, aunque PHP no solo es capaz de crear páginas web. Consulte la sección titulada [¿Qué puede hacer PHP](#intro-whatcando) para obtener más información.

Las páginas web habilitadas para PHP se tratan exactamente igual que las páginas HTML regulares y puede crearlas y editarlas de la misma manera que normalmente crea páginas HTML regulares.

## Su primera página habilitada para PHP

Este tutorial asume que PHP ya está instalado. Las instrucciones de instalación se pueden encontrar en la [página de descargas](https://www.php.net/downloads.php).

Cree un fichero llamado `hello.php` con el siguiente contenido:

```php
<?php

echo "Hello World!";

?>

     
```

Usando su terminal, navegue hasta el directorio que contiene este fichero y inicie un servidor de desarrollo con el siguiente comando:

```php
php -S localhost:8000

     
```

Utilice su navegador para acceder al fichero con la URL de su servidor web, terminando con la referencia al fichero `/hello.php`. Según el comando anterior ejecutado, la URL será `http://localhost:8000/hello.php`. Si todo está configurado correctamente, este fichero será analizado por PHP y verá la salida "Hello World!" mostrada en su navegador.

PHP puede incrustarse dentro de una página web HTML normal. Esto significa que dentro de su documento HTML puede escribir las sentencias PHP, como se demuestra en el siguiente ejemplo:

```php
<!DOCTYPE html>
<html>
    <head>
        <title>Prueba de PHP</title>
    </head>
    <body>
        <?php echo '<p>Hello World</p>'; ?>
    </body>
</html>

     
```

Esto producirá la siguiente salida:

```php
<!DOCTYPE html>
<html>
    <head>
        <title>Prueba de PHP</title>
    </head>
    <body>
        <p>Hello World</p>
    </body>
</html>

     
```

Este programa es extremadamente simple y realmente no necesitaba usar PHP para crear una página como esta. Todo lo que hace es mostrar: `Hello World` usando la sentencia `echo` de PHP. Observe que el fichero *no necesita ser ejecutable* ni especial de ninguna manera. El servidor descubre que este fichero necesita ser interpretado por PHP porque usó la extensión ".php", que el servidor está configurado para pasar a PHP. Piense en esto como un fichero HTML normal que por casualidad tiene un conjunto de etiquetas especiales disponibles que hacen muchas cosas interesantes.

El objetivo del ejemplo es mostrar el formato especial de las etiquetas PHP. En este ejemplo usamos `<?php` para indicar el inicio de una etiqueta PHP. Luego pusimos la sentencia PHP y salimos del modo PHP añadiendo la etiqueta de cierre, `?>`. Puede entrar y salir del modo PHP en un fichero HTML como este donde quiera. Para más detalles, lea la sección del manual sobre la [sintaxis básica de PHP](#language.basic-syntax).

> [!NOTE]
> Los saltos de línea tienen poco significado en HTML, sin embargo sigue siendo una buena idea hacer que su HTML se vea bien y limpio poniendo saltos de línea. Un salto de línea que sigue inmediatamente después de un cierre `?>` será eliminado por PHP. Esto puede ser extremadamente útil cuando está poniendo muchos bloques de PHP o ficheros incluidos que contienen PHP y que no deberían mostrar nada. Al mismo tiempo puede ser un poco confuso. Puede poner un espacio después del cierre `?>` para forzar que se muestre un espacio y un salto de línea, o puede poner un salto de línea explícito en el último echo/print desde dentro de su bloque PHP.

> [!NOTE]
> Hay muchos editores de texto y Entornos de Desarrollo Integrados (IDE) que puede usar para crear, editar y gestionar ficheros PHP. Una lista parcial de estas herramientas se mantiene en [Lista de editores PHP](http://en.wikipedia.org/wiki/List_of_PHP_editors). Si desea recomendar un editor, por favor visite la página anterior y pídale al responsable de la página que añada el editor a la lista. Tener un editor con resaltado de sintaxis puede ser útil.

> [!NOTE]
> Los procesadores de texto como StarOffice Writer, Microsoft Word y Abiword no son óptimos para editar ficheros PHP. Si desea usar uno para este script de prueba, debe asegurarse de guardar el fichero como *texto plano* o PHP no podrá leer y ejecutar el script.

Ahora que ha creado con éxito un script PHP funcional, es hora de crear ¡el script PHP más famoso! Haga una llamada a la función `phpinfo` y verá mucha información útil sobre su sistema y configuración, como las [variables predefinidas](#language.variables.predefined) disponibles, los módulos PHP cargados y las [configuraciones](#configuration). Tómese su tiempo y revise esta información importante.

```php
<?php

phpinfo();

?>

     
```

## Algo útil

Ahora hagamos algo más útil. Vamos a comprobar qué tipo de navegador está usando el visitante. Para ello, comprobamos la cadena del agente de usuario que el navegador envía como parte de la petición HTTP. Esta información se almacena en una [variable](#language.variables). Las variables siempre comienzan con un signo de dólar en PHP. La variable que nos interesa ahora es `$_SERVER['HTTP_USER_AGENT']`.

> [!NOTE]
> `$_SERVER` es una variable especial reservada de PHP que contiene toda la información del servidor web. Se la conoce como superglobal. Consulte la página relacionada del manual sobre [superglobals](#language.variables.superglobals) para obtener más información.

Para mostrar esta variable, puede hacer simplemente:

```php
<?php

echo $_SERVER['HTTP_USER_AGENT'];

?>

    
```

Una salida de ejemplo de este script podría ser:

```php
Mozilla/5.0 (Linux) Firefox/112.0

    
```

Hay muchos [tipos](#language.types) de variables disponibles en PHP. En el ejemplo anterior imprimimos un elemento de un [array](#language.types.array) variable. Los arrays pueden ser muy útiles.

`$_SERVER` es solo una variable que PHP hace automáticamente disponible. Puede ver una lista en la sección [Variables Reservadas](#reserved.variables) del manual o puede obtener una lista completa de ellas mirando la salida de la función `phpinfo` usada en el ejemplo de la sección anterior.

Puede poner múltiples sentencias PHP dentro de una etiqueta PHP y crear pequeños bloques de código que hacen más que un simple echo. Por ejemplo, si quiere comprobar si se está usando Firefox puede hacer esto:

```php
<?php

if (str_contains($_SERVER['HTTP_USER_AGENT'], 'Firefox')) {
    echo 'Está usando Firefox.';
}

?>

     
```

Una salida de ejemplo de este script podría ser:

```php
Está usando Firefox.

     
```

Aquí introducimos un par de conceptos nuevos. Tenemos una sentencia [if](#control-structures.if). Si está familiarizado con la sintaxis básica usada por el lenguaje C, esto debería parecerle lógico. De lo contrario, debería leer un libro introductorio de PHP o los primeros capítulos, o leer la parte de [Referencia del Lenguaje](#langref) del manual.

El segundo concepto que introdujimos fue la llamada a la función `str_contains`. `str_contains` es una función integrada en PHP que determina si una cadena dada contiene otra cadena. En este caso estamos buscando `'Firefox'` (la llamada aguja) dentro de `$_SERVER['HTTP_USER_AGENT']` (la llamada pajar). Si la aguja se encuentra dentro del pajar, la función devuelve true. De lo contrario, devuelve `false`. Si devuelve `true`, la expresión [if](#control-structures.if) se evalúa como `true` y se ejecuta el código dentro de sus {llaves}. De lo contrario, el código no se ejecuta. Siéntase libre de crear ejemplos similares, con [if](#control-structures.if), [else](#control-structures.else), y otras funciones como `strtoupper` y `strlen`. Cada página relacionada del manual contiene ejemplos también. Si no está seguro de cómo usar funciones, querrá leer tanto la página del manual sobre [cómo leer una definición de función](#about.prototypes) como la sección sobre [funciones de PHP](#language.functions).

Podemos llevar esto un paso más allá y mostrar cómo puede entrar y salir del modo PHP incluso en medio de un bloque PHP:

```php
<?php
if (str_contains($_SERVER['HTTP_USER_AGENT'], 'Firefox')) {
    ?>
    <h3>str_contains() devolvió true</h3>
    <p>Está usando Firefox</p>
    <?php
} else {
    ?>
    <h3>str_contains() devolvió false</h3>
    <p>No está usando Firefox</p>
    <?php
}
?>

     
```

Una salida de ejemplo de este script podría ser:

```php
<h3>str_contains() devolvió true</h3>
<p>Está usando Firefox</p>

     
```

En lugar de usar una sentencia echo de PHP para mostrar algo, salimos del modo PHP y enviamos directamente HTML. El punto importante y potente a notar aquí es que el flujo lógico del script permanece intacto. Solo uno de los bloques HTML terminará siendo enviado al espectador dependiendo del resultado de `str_contains`. En otras palabras, depende de si la cadena `Firefox` fue encontrada o no.

## Tratar con formularios

Una de las características más poderosas de PHP es la forma en que maneja los formularios HTML. El concepto básico que es importante entender es que cualquier elemento de formulario estará automáticamente disponible para sus scripts PHP. Por favor, lea la sección del manual sobre [Variables desde fuentes externas](#language.variables.external) para obtener más información y ejemplos sobre el uso de formularios con PHP. Aquí hay un ejemplo de formulario HTML:

```php
<form action="action.php" method="post">
    <label for="name">Su nombre:</label>
    <input name="name" id="name" type="text">

    <label for="age">Su edad:</label>
    <input name="age" id="age" type="number">

    <button type="submit">Enviar</button>
</form>

     
```

No hay nada especial en este formulario. Es un formulario HTML directo sin ninguna etiqueta especial. Cuando el usuario rellena este formulario y pulsa el botón de enviar, se invoca la página `action.php`. En este fichero escribiría algo como esto:

```php
Hola <?php echo htmlspecialchars($_POST['name']); ?>.
Tiene <?php echo (int) $_POST['age']; ?> años.

     
```

Una salida de ejemplo de este script podría ser:

```php
Hola Joe. Tiene 22 años.

     
```

Aparte de las partes `htmlspecialchars` y `(int)`, debería ser obvio lo que hace esto. `htmlspecialchars` asegura que cualquier carácter que sea especial en HTML se codifique correctamente para que la gente no pueda inyectar etiquetas HTML o Javascript en su página. Para el campo de edad, ya que sabemos que es un número, podemos simplemente [convertirlo](#language.types.typecasting) a un `int` que automáticamente eliminará cualquier carácter adicional. También puede hacer que PHP haga esto automáticamente por usted usando la [extensión filter](#ref.filter). Las variables `$_POST['name']` y `$_POST['age']` son establecidas automáticamente por PHP. Anteriormente usamos la superglobal `$_SERVER`; arriba acabamos de introducir la superglobal `$_POST` que contiene todos los datos POST. Observe cómo el *método* de nuestro formulario es POST. Si hubiéramos usado el método *GET* entonces nuestra información del formulario viviría en la superglobal `$_GET` en su lugar. También puede usar la superglobal `$_REQUEST` si no le importa la fuente de sus datos de petición. Contiene la información combinada de los datos GET, POST y COOKIE.

## ¿Qué sigue?

Con sus nuevos conocimientos debería ser capaz de entender la mayoría del manual.

En particular puede que quiera explorar las siguientes características: Leer y escribir ficheros con las [funciones del sistema de ficheros](#book.filesystem), [Manejo de subidas de ficheros](#features.file-upload), Obtener páginas y ficheros remotos con [Curl](#book.curl), Almacenar y analizar datos en una base de datos con [PDO](#book.pdo) ([SQLite](#ref.pdo-sqlite) puede usarse sin ejecutar un servidor de base de datos), Persistir datos entre peticiones con [Sesiones](#book.session)

Hay un tesoro de bibliotecas y [marcos de referencia](https://packagist.org/search/?tags=framework) para cada ocasión en el repositorio [Packagist](https://packagist.org), todos instalables mediante el [gestor de paquetes Composer](#install.composer.intro).

Para obtener ayuda y consejos de la comunidad, consulte la [página de ayuda](https://www.php.net/support.php).

Para una variedad de podcasts, presentaciones y otros vídeos, consulte el [PeerTube de la comunidad](https://phpc.tv/).

Otros recursos de la comunidad que le ayudarán incluyen "listas increíbles" (directorios curados de enlaces) y "mapas de ruta para desarrolladores" (listas de temas relacionados).

Cuando se quede atascado sin saber por dónde empezar, intente dividir su proyecto o problema en partes más pequeñas, lo que le permitirá ver más fácilmente qué ya sabe hacer y qué necesita aprender. La lista puede ser tan detallada como necesite. Por ejemplo, construir un blog podría desglosarse en las siguientes partes:

- Listar y ver páginas

  - Leer registros (páginas) de una base de datos

- Crear páginas

  - Manejar el envío del formulario

  - Escribir registros (páginas) en una base de datos

- Acceso de administrador

  - Leer registros (usuarios) de una base de datos

  - Manejar contraseñas

  - Persistir datos (inicio de sesión de usuario) entre peticiones/páginas (sesiones)

Si no hay nada en particular que quiera construir, puede intentar buscar ejercicios de codificación como katas, desafíos y "code golf". Incluso cuando no están específicamente dirigidos a PHP, la mayoría deberían poder completarse y probablemente desafiarán sus conocimientos y pensamiento.
