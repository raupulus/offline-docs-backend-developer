---
title: Precarga
source_url: https://www.php.net/manual/es/opcache.preloading.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/opcache/preload.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: opcache
translation_status: ready
translation_reviewed: true
translation_revision: 87d6bb1bb
order: 58660
---

## Precarga

A partir de PHP 7.4.0, PHP puede ser configurado para precargar scripts en el opcache cuando el motor se inicia. Todas las funciones, clases, interfaces o traits (pero no las constantes) de estos ficheros se volverán entonces disponibles globalmente para todas las peticiones sin necesidad de ser explícitamente incluidas. Esto intercambia la comodidad y el rendimiento (ya que el código está siempre disponible) por el uso de la memoria base. Asimismo, requiere reiniciar el proceso PHP para eliminar los scripts precargados, lo que significa que esta funcionalidad solo es práctica en producción, no en un entorno de desarrollo.

Tenga en cuenta que el compromiso óptimo entre rendimiento y memoria puede variar según la aplicación. "Precargar todo" puede ser la estrategia más simple, pero no necesariamente la mejor. Además, la precarga solo es útil cuando hay un proceso persistente de una petición a otra. Esto significa que aunque pueda funcionar en un script CLI si el opcache está activado, generalmente es inútil. La excepción es al utilizar la precarga en las [bibliotecas FFI](#ffi.examples-complete).

> [!NOTE]
> La precarga no está soportada en Windows.

La configuración de la precarga implica dos pasos, y requiere que el opcache esté activado. En primer lugar, defina el valor [opcache.preload](#ini.opcache.preload) en `php.ini`:

```php
opcache.preload=preload.php

  
```

`preload.php` es un fichero arbitrario que se ejecutará una vez al inicio del servidor (PHP-FPM, mod_php, etc.) y cargará código en memoria persistente. En los servidores que se inician como root antes de cambiar a un usuario del sistema no privilegiado, o si PHP se ejecuta como root (no recomendado), el valor [opcache.preload_user](#ini.opcache.preload-user) puede especificar el usuario del sistema para ejecutar la precarga. La ejecución de la precarga como root no está permitida por defecto. Defina `opcache.preload_user=root` para permitirlo explícitamente.

En el script `preload.php`, cualquier fichero referenciado por `include`, `include_once`, `require`, `require_once`, o `opcache_compile_file` serán analizados en la memoria persistente. En el siguiente ejemplo, todos los ficheros `.php` del directorio `src` serán precargados, excepto si son un fichero `Test`.

```php
<?php
$directory = new RecursiveDirectoryIterator(__DIR__ . '/src');
$fullTree = new RecursiveIteratorIterator($directory);
$phpFiles = new RegexIterator($fullTree, '/.+((?<!Test)+\.php$)/i', RecursiveRegexIterator::GET_MATCH);

foreach ($phpFiles as $key => $file) {
    require_once $file[0];
}
?>

  
```

`include` y `opcache_compile_file` funcionarán ambos, pero tienen implicaciones diferentes en la forma en que el código es gestionado.

- `include` ejecutará el código del fichero, mientras que `opcache_compile_file` no lo hará. Esto significa que solo el primero soporta la declaración condicional (las funciones declaradas dentro de un bloque if).

- Debido a que `include` ejecutará el código, los ficheros incluidos de manera anidada también serán analizados y sus declaraciones precargadas.

- `opcache_compile_file` puede cargar ficheros en cualquier orden. Es decir, si `a.php` define la clase `A` y `b.php` define la clase `B` que extiende `A`, entonces `opcache_compile_file` puede cargar estos dos ficheros en cualquier orden. Al utilizar `include`, sin embargo, `a.php` *debe* ser incluido primero.

- En ambos casos, si un script posterior incluye un fichero que ya ha sido precargado, entonces su contenido siempre se ejecutará, pero los símbolos que define no se volverán a definir. El uso de `include_once` no evitará que el fichero sea incluido una segunda vez. Puede ser necesario cargar un fichero nuevamente para incluir las constantes globales definidas en él, ya que no son gestionadas por la precarga.

Cuál enfoque es el mejor depende, por lo tanto, del comportamiento deseado. Con código que utilizaría de otro modo un cargador automático, `opcache_compile_file` permite una mayor flexibilidad. Con código que sería cargado manualmente de otro modo, `include` será más robusto.
