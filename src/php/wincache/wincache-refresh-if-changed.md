---
title: wincache_refresh_if_changed
description: Actualiza las entradas del caché para los archivos almacenados en caché
source_url: https://www.php.net/manual/es/function.wincache-refresh-if-changed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-refresh-if-changed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: 07e42841b
order: 101650
---

wincache_refresh_if_changed

Actualiza las entradas del caché para los archivos almacenados en caché

## Descripción

```php
wincache_refresh_if_changed([array $files]): bool
```php

Actualiza las entradas del caché para los archivos cuyos nombres se han pasado en los argumentos de entrada. Si no se especifica ningún argumento, entonces se actualizan todas las entradas del caché.

## Parámetros

`files`  
Array de nombres de archivos para los archivos que necesitan ser actualizados. Se puede usar una ruta de archivo absoluta o relativa.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

WinCache realiza verificaciones regulares en los archivos almacenados en caché para asegurarse de que, si un archivo ha cambiado, la entrada correspondiente en la memoria caché se actualice. Por defecto, esta verificación se realiza cada 30 segundos. Si, por ejemplo, un script PHP actualiza otro script PHP donde se almacenan las configuraciones de la aplicación, entonces puede ocurrir que, después de que los cambios de configuración se hayan guardado, la aplicación siga utilizando los parámetros antiguos durante algún tiempo hasta que el caché se actualice. En este caso, es preferible actualizar el caché justo después de que el archivo haya sido modificado. El ejemplo siguiente muestra cómo hacerlo.

Un ejemplo de `wincache_refresh_if_changed`

```
<?php
$filename = 'C:\inetpub\wwwroot\config.php';
$handle = fopen($filename, 'w+');
if ($handle === FALSE) die('Failed to open file '.$filename.' for writing');
fwrite($handle, '<?php $setting=something; ?>');
fclose($handle);
wincache_refresh_if_changed(array($filename));
?>

    
```php

## Véase también

`wincache_fcache_fileinfo`, `wincache_fcache_meminfo`, `wincache_ocache_fileinfo`, `wincache_ocache_meminfo`, `wincache_rplist_fileinfo`, `wincache_rplist_meminfo`, `wincache_ucache_meminfo`, `wincache_ucache_info`
