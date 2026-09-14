---
title: php_ini_scanned_files
description: Devuelve la lista de ficheros .ini analizados en los directorios de configuración
  adicionales
source_url: https://www.php.net/manual/es/function.php-ini-scanned-files.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/php-ini-scanned-files.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: false
translation_revision: 8dd14a886
order: 39130
---

php_ini_scanned_files

Devuelve la lista de ficheros .ini analizados en los directorios de configuración adicionales

## Descripción

```php
php_ini_scanned_files(): string
```php

`php_ini_scanned_files` devuelve una lista de nombres de ficheros de configuración analizados después de `php.ini`. Esta lista está en formato CSV. Los directorios examinados son definidos por una opción de configuración durante la compilación, y opcionalmente por una variable de entorno durante la ejecución: más información está disponible en el [guía de instalación](#configuration.file.scan).

Los ficheros de configuración devueltos incluyen la ruta completa.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `string` donde los ficheros .ini están separados por comas en caso de éxito. Cada coma es seguida por un retorno de línea. Si la directiva de configuración `--with-config-file-scan-dir` no ha sido definida y la variable de entorno `PHP_INI_SCAN_DIR` no está definida, `false` es devuelto. Si estaba definida y el directorio estaba vacío, una cadena vacía es devuelta. Si un fichero es ilegible, el fichero será igualmente incluido en el `string` devuelto pero también provocará un error PHP. Este error PHP será visible tanto durante la compilación como al utilizar `php_ini_scanned_files`.

## Ejemplos

Un ejemplo de lista devuelta por `php_ini_scanned_files`

```
<?php
if ($filelist = php_ini_scanned_files()) {
    if (strlen($filelist) > 0) {
        $files = explode(',', $filelist);

        foreach ($files as $file) {
            echo "<li>" . trim($file) . "</li>\n";
        }
    }
}
?>

    
```php

## Véase también

`ini_set`, `phpinfo`, `php_ini_loaded_file`
