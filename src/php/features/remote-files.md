---
title: Uso de ficheros a distancia
source_url: https://www.php.net/manual/es/features.remote-files.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: features/remote-files.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: features
translation_status: ready
translation_reviewed: true
translation_revision: a0ae28d3b
order: 1600
---

## Uso de ficheros a distancia

Mientras el soporte de los gestores de URL ("URL fopen wrapper") esté activado en el `php.ini`, con la opción `allow_url_fopen`, se puede utilizar URL (HTTP y FTP) con la mayoría de las funciones que utilizan un nombre de fichero como argumento. Esto incluye especialmente `include`, `include_once`, `require` y `require_once` (`allow_url_include` debe estar activo para utilizarlos). Consulte [???](#wrappers) para más información sobre los protocolos soportados por PHP.

Por ejemplo, se puede seguir el siguiente ejemplo para abrir un fichero en un servidor web distante, analizar los resultados para extraer la información que se necesita, y luego utilizarla en una consulta de base de datos, o simplemente editar la información en el estilo del sitio.

Conocer el título de una página distante

```php
<?php
$file = fopen ("http://www.example.com/", "r");
if (!$file) {
  echo "<p>Imposible leer la página.\n";
  exit;
}
while (!feof ($file)) {
    $line = fgets ($file, 1024);
    /* Esto solo funciona si las etiquetas Title están correctamente utilizadas */
    if (preg_match ("@\<title\>(.*)\</title\>@i", $line, $out)) {
        $title = $out[1];
        break;
    }
}
fclose($file);
?>

   
```

También se puede escribir ficheros en un servidor FTP siempre que se esté conectado con un usuario con los derechos de acceso adecuados, aunque el fichero no existiera aún.

Para conectarse con un usuario distinto de anónimo, se debe especificar un nombre de usuario (y probablemente la contraseña) en la URL, como `ftp://user:password@ftp.example.com/path/to/file`. (Se puede utilizar el mismo tipo de sintaxis para acceder a los ficheros vía HTTP cuando requieren una identificación simple).

Almacenar datos en un servidor distante

```php
<?php
$file = fopen ("ftp://ftp.example.com/incoming/outputfile", "w");
if (!$file) {
  echo "<p>Imposible abrir el fichero distante para escritura.\n";
  exit;
}
/* Escritura de los datos. */
fputs ($file, $_SERVER['HTTP_USER_AGENT'] . "\n");
fclose ($file);
?>

   
```

> [!NOTE]
> Nota: se puede tener la idea, a partir del ejemplo anterior, de utilizar la misma técnica para escribir en un log distante, pero como se mencionó anteriormente solo se puede escribir en un nuevo fichero utilizando las funciones `fopen` con una URL. Para hacer logs distribuidos, se recomienda consultar la parte `syslog`.
