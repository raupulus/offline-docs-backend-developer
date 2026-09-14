---
title: get_browser
description: Indica las capacidades del navegador cliente
source_url: https://www.php.net/manual/es/function.get-browser.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/get-browser.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: 3c699fad2
order: 47080
---

get_browser

Indica las capacidades del navegador cliente

## Descripción

```php
get_browser([string $user_agent], [bool $return_array]): object
```php

`get_browser` intenta determinar las capacidades del navegador cliente. Esto se realiza leyendo las informaciones en el archivo `browscap.ini`.

## Parámetros

`user_agent`  
El encabezado user agent a analizar. Por omisión, se utiliza el valor del encabezado `User-Agent`; sin embargo, puede alterarse (es decir, buscar otras informaciones sobre el navegador) pasando este argumento.

Puede anularse este parámetro pasando el valor `null`.

`return_array`  
Si se define como `true`, esta función retornará un `array` en lugar de un `object`.

## Valores devueltos

Las informaciones se retornan en forma de un objeto, cuyos diferentes miembros contendrán informaciones, tales como las versiones mayores y menores y cadenas de identificación; booleanos para características como frames, JavaScript, y cookies; y así sucesivamente.

El valor `cookies` indica simplemente que el navegador es capaz de aceptar cookies, y no indica si el usuario las ha activado en su navegador. El único medio de probar la activación de cookies es establecer una con la función `setcookie`, recargar la página y verificar que el cookie aún existe.

Retorna `false` si no se puede recuperar ninguna información, tal como cuando la opción de configuración [browscap](#ini.browscap) en `php.ini` no ha sido definida.

## Ejemplos

Ejemplo con `get_browser`: lista de capacidades del navegador del cliente web

```
<?php
echo $_SERVER['HTTP_USER_AGENT'] . "\n\n";

$browser = get_browser(null, true);
print_r($browser);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7) Gecko/20040803 Firefox/0.9.3

    Array
    (
        [browser_name_regex] => ^mozilla/5\.0 (windows; .; windows nt 5\.1; .*rv:.*) gecko/.* firefox/0\.9.*$
        [browser_name_pattern] => Mozilla/5.0 (Windows; ?; Windows NT 5.1; *rv:*) Gecko/* Firefox/0.9*
        [parent] => Firefox 0.9
        [platform] => WinXP
        [browser] => Firefox
        [version] => 0.9
        [majorver] => 0
        [minorver] => 9
        [cssversion] => 2
        [frames] => 1
        [iframes] => 1
        [tables] => 1
        [cookies] => 1
        [backgroundsounds] =>
        [vbscript] =>
        [javascript] => 1
        [javaapplets] => 1
        [activexcontrols] =>
        [cdf] =>
        [aol] =>
        [beta] => 1
        [win16] =>
        [crawler] =>
        [stripper] =>
        [wap] =>
        [netclr] =>
    )

## Notas

> [!NOTE]
> Para poder funcionar, la directiva de configuración [browscap](#ini.browscap) en el archivo `php.ini` debe apuntar al archivo `browscap.ini` del sistema.
>
> `browscap.ini` no se distribuye con PHP, pero puede descargarse en [php_browscap.ini](http://browscap.org/).
>
> Aunque `browscap.ini` contiene informaciones sobre un gran número de navegadores, corresponde al usuario mantener su base de datos actualizada. El formato del archivo es muy sencillo de comprender.
