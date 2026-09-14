---
title: Seguridad del Sistema de Archivos
source_url: https://www.php.net/manual/es/security.filesystem.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: security/filesystem.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: security
translation_status: ready
translation_revision: 91570644f
order: 109940
---

## Seguridad del Sistema de Archivos

PHP está sujeto a la seguridad integrada en la mayoría de sistemas de servidores con respecto a los permisos de archivos y directorios. Esto permite controlar qué archivos en el sistema de archivos se pueden leer. Se debe tener cuidado con los archivos que son legibles para garantizar que son seguros para la lectura por todos los usuarios que tienen acceso al sistema de archivos.

Desde que PHP fue diseñado para permitir el acceso a nivel de usuarios para el sistema de archivos, es perfectamente posible escribir un script PHP que le permita leer archivos del sistema como `/etc/passwd`, modificar sus conexiones de red, enviar trabajos de impresión masiva, etc. Esto tiene algunas implicaciones obvias, es necesario asegurarse que los archivos que se van a leer o escribir son los apropiados.

Considere el siguiente script, donde un usuario indica que quiere borrar un archivo en su directorio home. Esto supone una situación en la que una interfaz web en PHP es usada regularmente para gestionar archivos, por lo que es necesario que el usuario Apache pueda borrar archivos en los directorios home de los usuarios.

Un control pobre puede llevar a ....

```php
<?php

// eliminar un archivo del directorio personal del usuario
$username = $_POST['user_submitted_name'];
$userfile = $_POST['user_submitted_filename'];
$homedir  = "/home/$username";

unlink("$homedir/$userfile");

echo "El archivo ha sido eliminado!";
?>

     
```

Dado que el nombre de usuario y el nombre del archivo son enviados desde un formulario, estos pueden representar un nombre de archivo y un nombre de usuario que pertenecen a otra persona, incluso se podría borrar el archivo a pesar que se supone que no estaría permitido hacerlo. En este caso, usted desearía usar algún otro tipo de autenticación. Considere lo que podría suceder si las variables enviadas son `"../etc/"` y `"passwd"`. El código entonces se ejecutaría efectivamente como:

... Un ataque al sistema de archivos

```php
<?php

// elimina un archivo desde cualquier lugar en el disco duro al que
// el usuario de PHP tiene acceso. Si PHP tiene acceso de root:
$username = $_POST['user_submitted_name']; // "../etc"
$userfile = $_POST['user_submitted_filename']; // "passwd"
$homedir  = "/home/$username"; // "/home/../etc"

unlink("$homedir/$userfile"); // "/home/../etc/passwd"

echo "El archivo ha sido eliminado!";
?>

     
```

Hay dos medidas importantes que usted debe tomar para prevenir estas cuestiones.

- Únicamente permisos limitados al usuario web de PHP.

- Revise todas las variables que se envían.

Aquí está una versión mejorada del script:

Comprobación más segura del nombre de archivo

```php
<?php

// elimina un archivo del disco duro al que
// el usuario de PHP tiene acceso.
$username = $_SERVER['REMOTE_USER']; // usando un mecanismo de autenticación
$userfile = basename($_POST['user_submitted_filename']);
$homedir  = "/home/$username";

$filepath = "$homedir/$userfile";

if (file_exists($filepath) && unlink($filepath)) {
    $logstring = "Se ha eliminado $filepath\n";
} else {
    $logstring = "No se ha podido eliminar $filepath\n";
}

$fp = fopen("/home/logging/filedelete.log", "a");
fwrite($fp, $logstring);
fclose($fp);

echo htmlentities($logstring, ENT_QUOTES);

?>

     
```

Sin embargo, incluso esto no está exento de defectos. Si la autenticación del sistema permite a los usuarios crear sus propios inicios de sesión de usuario, y un usuario eligió la entrada `"../etc/"`, el sistema está expuesto una vez más. Por esta razón, puede que prefiera escribir un chequeo más personalizado:

Comprobación más segura del nombre de archivo

```php
<?php

$username     = $_SERVER['REMOTE_USER']; // usando un mecanismo de autenticación
$userfile     = $_POST['user_submitted_filename'];
$homedir      = "/home/$username";

$filepath     = "$homedir/$userfile";

if (!ctype_alnum($username) || !preg_match('/^(?:[a-z0-9_-]|\.(?!\.))+$/iD', $userfile)) {
    die("nombre de usuario o nombre de archivo incorrecto");
}

// etc.

?>

     
```

Dependiendo de sus sistema operativo, hay una gran variedad de archivos a los que debe estar atento, esto incluye las entradas de dispositivos (`/dev/` o `COM1`), archivos de configuracion (archivos `/etc/` y archivos `.ini`), las muy conocidas carpetas de almacenamiento (`/home/`, `My Documents`), etc. Por esta razón, por lo general es más fácil crear una política en donde se prohíba todo excepto lo que expresamente se permite.

## Cuestiones relacionadas a bytes nulos

Como PHP utiliza las funciones de C para operaciones relacionadas al sistema de archivos, se podría manejar bytes nulos de manera bastante inesperada. Como un byte nulo denota el fin de una cadena en C, las cadenas que contengan estos no serán consideradas por completo, sino sólo hasta que ocurra un byte nulo. El siguiente ejemplo muestra un código vulnerable que presenta este problema:

Script vulnerable a bytes nulos

```php
<?php

$file = $_GET['file']; // "../../etc/passwd\0"
if (file_exists('/home/wwwrun/' . $file . '.php')) {
    // file_exists devolverá true si el archivo /home/wwwrun/../../etc/passwd existe
    include '/home/wwwrun/' . $file . '.php';
    // el archivo /etc/passwd se incluirá
}

?>

     
```

Por lo tanto, cualquier cadena que se utiliza en una operación de sistema de archivos siembre deben ser validados correctamente. He aquí una versión mejorada del ejemplo anterior:

Validando correctamente la entrada

```php
<?php

$file = $_GET['file'];

// Lista blanca de valores posibles
switch ($file) {
    case 'main':
    case 'foo':
    case 'bar':
        include '/home/wwwrun/include/'.$file.'.php';
        break;
    default:
        include '/home/wwwrun/include/main.php';
}

?>

     
```
