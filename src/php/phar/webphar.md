---
title: Phar::webPhar
description: Redirige una solicitud desde un navegador web a un fichero interno en
  el archivo phar
source_url: https://www.php.net/manual/es/phar.webphar.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/webPhar.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: 5beaad988
order: 64420
---

Phar::webPhar

Redirige una solicitud desde un navegador web a un fichero interno en el archivo phar

## Descripción

```php
final public static Phar::webPhar([string $alias], [string $index], [string $fileNotFoundScript], [array $mimeTypes], [callable $rewrite]): void
```php

`Phar::webPhar` actúa como `Phar::mapPhar` para los phars orientados a web. Este método analiza `$_SERVER['REQUEST_URI']` y enruta las solicitudes de un navegador hacia un fichero interno del archivo. Esto simula un servidor web, enrutando solicitudes al fichero correcto, enviando los encabezados adecuados y analizando el fichero PHP como corresponde. Combinado con `Phar::mungServer` y `Phar::interceptFileFuncs`, cualquier aplicación web puede ser utilizada sin cambios a partir del archivo phar.

`Phar::webPhar` debe ser llamado únicamente desde el contenedor de carga de un archivo phar (consultar [esto](#phar.fileformat.stub) para obtener más información sobre los contenedores).

## Parámetros

`alias`  
El alias que puede ser utilizado en la URL `phar://` para referirse al archivo, en lugar de su ruta completa.

`index`  
La ubicación dentro del archivo del índice de directorio.

`fileNotFoundScript`  
La ubicación del script a ejecutar cuando un fichero no es encontrado. Este script debe enviar los encabezados HTTP 404 correctos.

`mimeTypes`  
Un array que hace corresponder extensiones de fichero adicionales a tipos MIME. Si las correspondencias por defecto son suficientes, se debe pasar un array vacío. Por defecto, estas correspondencias son las siguientes:

```
        
<?php
$mimes = array(
    'phps' => Phar::PHPS, // paso a highlight_file()
    'c' => 'text/plain',
    'cc' => 'text/plain',
    'cpp' => 'text/plain',
    'c++' => 'text/plain',
    'dtd' => 'text/plain',
    'h' => 'text/plain',
    'log' => 'text/plain',
    'rng' => 'text/plain',
    'txt' => 'text/plain',
    'xsd' => 'text/plain',
    'php' => Phar::PHP, // analizar como PHP
    'inc' => Phar::PHP, // analizar como PHP
    'avi' => 'video/avi',
    'bmp' => 'image/bmp',
    'css' => 'text/css',
    'gif' => 'image/gif',
    'htm' => 'text/html',
    'html' => 'text/html',
    'htmls' => 'text/html',
    'ico' => 'image/x-ico',
    'jpe' => 'image/jpeg',
    'jpg' => 'image/jpeg',
    'jpeg' => 'image/jpeg',
    'js' => 'application/x-javascript',
    'midi' => 'audio/midi',
    'mid' => 'audio/midi',
    'mod' => 'audio/mod',
    'mov' => 'movie/quicktime',
    'mp3' => 'audio/mp3',
    'mpg' => 'video/mpeg',
    'mpeg' => 'video/mpeg',
    'pdf' => 'application/pdf',
    'png' => 'image/png',
    'swf' => 'application/shockwave-flash',
    'tif' => 'image/tiff',
    'tiff' => 'image/tiff',
    'wav' => 'audio/wav',
    'xbm' => 'image/xbm',
    'xml' => 'text/xml',
);
?>
        
       
```php

`rewrite`  
La función de reescritura que se pasa toma como único argumento un string y debe devolver un `string` o false.

Si se utiliza fast-cgi o cgi, el argumento pasado a la función es el valor de la variable `$_SERVER['PATH_INFO']`. De lo contrario, el argumento pasado a la función es el valor de la variable `$_SERVER['REQUEST_URI']`.

Si se devuelve un string, será utilizado en la ruta interna del fichero. Si se devuelve false, entonces webPhar() enviará un código HTTP 403.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Levanta una excepción `PharException` cuando el fichero interno no puede ser abierto o si la llamada se realiza fuera de un contenedor. Si se pasa un valor de array no válido en `mimeTypes` o si se pasa una función de devolución de llamada inválida al parámetro `rewrite`, entonces se levanta una excepción `UnexpectedValueException`.

## Historial de cambios

| Versión | Descripción                                          |
|---------|------------------------------------------------------|
| 8.0.0   | `fileNotFoundScript` y `rewrite` ahora son nullable. |

## Ejemplos

Ejemplo con `Phar::webPhar`

En el ejemplo siguiente, el phar creado mostrará `Hola mundo` si alguien llama a `/miphar.phar/index.php` o `/miphar.phar`, y mostrará la fuente de `index.phps` si `/miphar.phar/index.phps` es llamado.

```
<?php
// el archivo phar es creado:
try {
    $phar = new Phar('miphar.phar');
    $phar['index.php'] = '<?php echo "Hola mundo"; ?>';
    $phar['index.phps'] = '<?php echo "Hola mundo"; ?>';
    $phar->setStub('<?php
Phar::webPhar();
__HALT_COMPILER(); ?>');
} catch (Exception $e) {
    // se manejan los errores aquí
}
?>

    
```php

## Véase también

`Phar::mungServer`, `Phar::interceptFileFuncs`
