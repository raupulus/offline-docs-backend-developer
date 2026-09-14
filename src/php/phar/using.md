---
title: Utilizar los archivos Phar
source_url: https://www.php.net/manual/es/phar.using.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/using.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: e9f972da6
order: 64930
---

## Utilizar los archivos Phar

## Utilizar los archivos Phar : Introducción

Los archivos Phar son idénticos en concepto a los archivos JAR de Java, pero están diseñados específicamente para las necesidades y la flexibilidad de las aplicaciones PHP. Un archivo Phar se utiliza para distribuir una aplicación PHP completa o una biblioteca en forma de un único archivo. Una aplicación en forma de archivo Phar se utiliza exactamente de la misma forma que cualquier otra aplicación PHP:

      
    php aplicacionesympa.phar
      
     

El uso de una biblioteca en forma de archivo Phar es el mismo que cualquier otra biblioteca PHP:

```php
<?php
include 'bibliothequesympa.phar';
?>

   
```

El flujo `phar` proporciona el núcleo de la extensión phar, y es descrito en detalle [aquí](#phar.using.stream). El flujo phar permite el acceso a los ficheros contenidos en un archivo phar mediante las funciones estándar de ficheros `fopen`, `opendir`, y cualquier otra que funcione con ficheros normales. El flujo `phar` soporta todas las operaciones de lectura/escritura tanto en ficheros como en directorios.

```php
<?php
include 'phar://bibliothequesympa.phar/fichero/interne.php';
header('Content-type: image/jpeg');
// los phars pueden ser alcanzados mediante la ruta completa o mediante alias
echo file_get_contents('phar:///ruta/completa/hacia/bibliothequesympa.phar/images/wow.jpg');
?>

   
```

La clase `Phar` implementa funcionalidades avanzadas para acceder a los ficheros y crear archivos phar. La clase Phar es descrita en detalle [aquí](#phar.using.object).

```php
<?php
try {
    // abre un phar existente
    $p = new Phar('bibliothequesympa.phar', 0);
    // Phar extiende la clase DirectoryIterator de SPL
    foreach (new RecursiveIteratorIterator($p) as $file) {
        // $file es una clase PharFileInfo y heredada de SplFileInfo
        echo $file->getFileName() . "\n";
        echo file_get_contents($file->getPathName()) . "\n"; // muestra el contenido;
    }
    if (isset($p['fichero/interne.php'])) {
        var_dump($p['fichero/interne.php']->getMetadata());
    }

    // crea un nuevo phar - phar.readonly debe ser 0 en php.ini
    // phar.readonly está activado por omisión por razones de seguridad.
    // En servidores de producción, los Phars no necesitan ser creados,
    // solo ejecutados.
    if (Phar::canWrite()) {
        $p = new Phar('nuevophar.tar.phar', 0, 'nuevophar.tar.phar');
        // Se crea un archivo Phar basado en tar, comprimido por gzip (.tar.gz)
        $p = $p->convertToExecutable(Phar::TAR, Phar::GZ);

        // crea una transacción - nada se escribe en nuevophar.phar
        // hasta que stopBuffering() sea llamado, aunque se requiere almacenamiento temporal
        $p->startBuffering();
        // añade todos los ficheros de /ruta/hacia/elproyecto en el phar con el prefijo "proyecto"
        $p->buildFromIterator(new RecursiveIteratorIterator(new RecursiveDirectoryIterator('/ruta/hacia/elproyecto')), '/ruta/hacia/');

        // añade un nuevo fichero utilizando la API de acceso por array
        $p['fichero1.txt'] = 'Información';
        $fp = fopen('grosfichero.dat', 'rb');
        // copia todos los datos del flujo
        $p['data/grosfichero.dat'] = $fp;

        if (Phar::canCompress(Phar::GZ)) {
            $p['data/grosfichero.dat']->compress(Phar::GZ);
        }

        $p['images/wow.jpg'] = file_get_contents('images/wow.jpg');
        // cualquier valor puede ser guardado como metadatos específicos del fichero
        $p['images/wow.jpg']->setMetadata(array('mime-type' => 'image/jpeg'));
        $p['index.php'] = file_get_contents('index.php');
        $p->setMetadata(array('bootstrap' => 'index.php'));

        // guarda el archivo phar en el disco
        $p->stopBuffering();
    }
} catch (Exception $e) {
    echo 'No ha podido abrir el Phar: ', $e;
}
?>

   
```

Por otro lado, la verificación del contenido del archivo phar puede realizarse utilizando uno de los algoritmos de firma simétrica (MD5, SHA1, SHA256 y SHA512 si ext/hash está activada) y utilizando la firma asimétrica por clave pública/privada de OpenSSL. Para aprovechar la firma OpenSSL, debe generarse un par de claves pública/privada y utilizar la clave privada para firmar con `Phar::setSignatureAlgorithm`. Además, la clave pública, extraída utilizando este código:

```php
   
<?php
$public = openssl_get_publickey(file_get_contents('private.pem'));
$pkey = '';
openssl_pkey_export($public, $pkey);
?>
   
  
```

debe ser guardada por separado del archivo phar que verifica. Si el archivo phar es guardado como `/ruta/hacia/mi.phar`, la clave pública debe ser guardada como `/ruta/hacia/mi.phar.pubkey`, de lo contrario phar no será capaz de verificar la firma OpenSSL.

La clase `Phar` también proporciona tres métodos estáticos, `Phar::webPhar`, `Phar::mungServer` y `Phar::interceptFileFuncs` que son cruciales para empaquetar aplicaciones PHP destinadas a ser utilizadas en un sistema de ficheros clásico o como aplicación web. `Phar::webPhar` implementa un controlador que enruta las llamadas HTTP al lugar correcto del archivo phar. `Phar::mungServer` se utiliza para modificar los valores del array `$_SERVER` para indicar a las aplicaciones que utilicen estos valores. `Phar::interceptFileFuncs` indica a Phar que intercepte las llamadas a `fopen`, `file_get_contents`, `opendir`, y a todas las funciones basadas en stat (`file_exists`, `is_readable`, etc) y enruta todos los caminos relativos a los lugares correctos del archivo phar.

Por ejemplo, empaquetar una versión de la famosa aplicación phpMyAdmin en un archivo phar requiere simplemente este script y, a partir de entonces, `phpMyAdmin.phar.tar.php` puede ser accedido como un fichero clásico desde su servidor web, después de haber modificado la pareja usuario/contraseña:

```php
    
<?php
@unlink('phpMyAdmin.phar.tar.php');
copy('phpMyAdmin-2.11.3-english.tar.gz', 'phpMyAdmin.phar.tar.php');
$a = new Phar('phpMyAdmin.phar.tar.php');
$a->startBuffering();
$a["phpMyAdmin-2.11.3-english/config.inc.php"] = '<?php
/* Servers configuration */
$i = 0;

/* Server localhost (config:root) [1] */
$i++;
$cfg[\'Servers\'][$i][\'host\'] = \'localhost\';
$cfg[\'Servers\'][$i][\'extension\'] = \'mysqli\';
$cfg[\'Servers\'][$i][\'connect_type\'] = \'tcp\';
$cfg[\'Servers\'][$i][\'compress\'] = false;
$cfg[\'Servers\'][$i][\'auth_type\'] = \'config\';
$cfg[\'Servers\'][$i][\'user\'] = \'root\';
$cfg[\'Servers\'][$i][\'password\'] = \'\';

/* End of servers configuration */
if (strpos(PHP_OS, \'WIN\') !== false) {
    $cfg[\'UploadDir\'] = getcwd();
} else {
    $cfg[\'UploadDir\'] = \'/tmp/pharphpmyadmin\';
    @mkdir(\'/tmp/pharphpmyadmin\');
    @chmod(\'/tmp/pharphpmyadmin\', 0777);
}';
$a->setStub('<?php
Phar::interceptFileFuncs();
Phar::webPhar("phpMyAdmin.phar", "phpMyAdmin-2.11.3-english/index.php");
echo "phpMyAdmin está destinado a ser ejecutado desde un navegador web\n";
exit -1;
__HALT_COMPILER();
');
$a->stopBuffering();
?>
    
   
```

## Utilizar los archivos Phar : el flujo phar

El flujo Phar soporta totalmente `fopen` para las lecturas/escrituras (no las concatenaciones), `unlink`, `stat`, `fstat`, `fseek`, `rename`, y las operaciones de flujo sobre los directorios `opendir`, y `rmdir` y `mkdir`.

La compresión y los metadatos individuales por fichero pueden también ser manipulados dentro del archivo Phar utilizando los contextos de flujo:

```php
<?php
$context = stream_context_create(array('phar' =>
                                    array('compress' => Phar::GZ)),
                                    array('metadata' => array('user' => 'cellog')));
file_put_contents('phar://mon.phar/unfichero.php', 0, $context);
?>

   
```

El flujo `phar` no actúa sobre los ficheros remotos y no puede considerar los ficheros remotos, etc... incluso si las opciones INI [allow_url_fopen](#ini.allow-url-fopen) y [allow_url_include](#ini.allow-url-include) están desactivadas.

Aunque es posible crear archivos phar desde cero utilizando solo las operaciones sobre los flujos, es preferible utilizar la funcionalidad incluida en la clase Phar. El flujo es mejor utilizado para las operaciones de lectura.

## Utilizar los archivos Phar : las clases Phar y PharData

La clase `Phar` soporta la lectura y la manipulación de los archivos Phar, así como la iteración a través de la funcionalidad heredada de la clase `RecursiveDirectoryIterator`. Con el soporte de la interfaz `ArrayAccess`, los ficheros contenidos en un archivo Phar pueden ser accedidos como si fueran miembros de un array asociativo.

La clase `PharData` extiende la clase `Phar`, y permite la creación y modificación de archivos tar y zip no ejecutables (datos) incluso si `phar.readonly`=1 en php.ini. Por lo tanto, `PharData::setAlias` y `PharData::setStub` están ambas desactivadas ya que los conceptos de alias y contenedor están restringidos a los archivos phar ejecutables.

Es importante señalar que cuando un archivo Phar es creado, la ruta completa debe ser pasada al constructor del objeto `Phar`. Una ruta relativa impediría la inicialización.

Suponiendo que `$p` es un objeto inicializado de esta forma:

```php
<?php
$p = new Phar('/ruta/hacia/miphar.phar', 0, 'miphar.phar');
?>

   
```

Un archivo Phar vacío será creado como `/ruta/hacia/miphar.phar`, o si `/ruta/hacia/miphar.phar` ya existe, será abierto de nuevo. El término `miphar.phar` demuestra el concepto de un alias que puede ser utilizado para referenciar `/ruta/hacia/miphar.phar` en URLs como esto:

```php
<?php
// estas dos llamadas a file_get_contents() son equivalentes si
// /ruta/hacia/miphar.phar tiene un alias explícito de "miphar.phar"
// en su manifiesto, o si el phar fue inicializado con la instanciación de
// el objeto Phar del ejemplo anterior
$f = file_get_contents('phar:///ruta/hacia/miphar.phar/algo.txt');
$f = file_get_contents('phar://miphar.phar/algo.txt');
?>

   
```

Con el objeto `Phar` `$p` recién creado, las siguientes cosas son posibles:

- `$a = $p['fichero.php']` crea una `PharFileInfo` que se refiere al contenido de `phar://miphar.phar/fichero.php`

- `$p['fichero.php'] = $v` crea un nuevo fichero (`phar://miphar.phar/fichero.php`), o sobrescribe un fichero existente dentro de `miphar.phar`. `$v` puede ser una cadena o un puntero a un fichero abierto, en cuyo caso el contenido del fichero será utilizado para crear el nuevo fichero. Tenga en cuenta que `$p->addFromString('fichero.php', $v)` es equivalente en términos de funcionalidad al caso anterior. También es posible añadir el contenido de un fichero con `$p->addFile('/ruta/hacia/fichero.php', 'fichero.php')`. Finalmente, un directorio vacío puede ser creado con `$p->addEmptyDir('vacío')`.

- `isset($p['fichero.php'])` puede ser utilizado para determinar si `phar://miphar.phar/fichero.php` existe dentro de `miphar.phar`.

- `unset($p['fichero.php'])` elimina `phar://miphar.phar/fichero.php` de `miphar.phar`.

Además, el objeto `Phar` es el único medio de acceder a los metadatos específicos de Phar, mediante `Phar::getMetadata`, y es también el único medio de establecer o recuperar el contenedor del cargador del archivo Phar mediante `Phar::getStub` y `Phar::setStub`. Además, la compresión para el archivo Phar completo puede ser manipulada solo mediante la clase `Phar`.

La lista completa de funcionalidades del objeto `Phar` está documentada a continuación.

La clase `PharFileInfo` extiende la clase `SplFileInfo` y añade varios métodos para manipular los metadatos específicos de Phar de un fichero contenido en un Phar, tales como manipular la compresión o los metadatos.
