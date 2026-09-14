---
title: Reportando errores
source_url: https://www.php.net/manual/es/security.errors.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: security/errors.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: security
translation_status: ready
translation_revision: ae725a440
order: 109930
---

## Reportando errores

Con la seguridad de PHP, hay dos formas para reportar errores. Una es en beneficio, para incrementar la seguridad, y la otra es para perjudicar.

Una táctica estándar de ataque conlleva a perfilar un sistema; llenándolo de datos incorrectos, revisando los tipos y contextos de los errores que son devueltos. Esto le permite al atacante recolectar información acerca del servidor, para determinar posibles debilidades. Por ejemplo, si un atacante ha recogido información sobre una página basada en un envío previo, él podría intentar sobrescribir las variables, o modificarlas:

Atacando variables con una página HTML personalizada

```php
<form method="post" action="objetivodelataque?username=badfoo&amp;password=badfoo">
<input type="hidden" name="username" value="badfoo" />
<input type="hidden" name="password" value="badfoo" />
</form>

     
```

Los errores de PHP que normalmente son devueltos, pueden ser muy útiles para el desarrollador que está intentando depurar un script, indicando qué cosas, como por ejemplo, qué función o qué fichero de PHP falló, y el número de línea en donde la falla ocurrió. Toda esta es la información que puede ser explotada. Esto no es algo raro para un desarrollador de PHP que utilice las funciones `show_source`, `highlight_string`, o `highlight_file` como una medida de depuración, pero en un sitio en escena, esto puede exponer variables ocultas, sintáxis sin revisar, y otra información peligrosa. Es especialmente peligroso el código en ejecución de fuentes conocidas con manejadores de depuración incluidos, o utilizar técnicas comunes de depuración. Si los atacantes pueden determinar qué técnica en general usted está utilizando, ellos podrían tratar de usar fuerza bruta en una página, enviando varias cadenas comunes de depuración:

Explotando variables comunes de depuración

```php
<form method="post" action="objetivodelataque?errors=Y&amp;showerrors=1&amp;debug=1">
<input type="hidden" name="errors" value="Y" />
<input type="hidden" name="showerrors" value="1" />
<input type="hidden" name="debug" value="1" />
</form>

     
```

Sin importar el método de manejo de errores, la capacidad de probar errores en un sistema conlleva a proveer a un atacante con mas información.

Por ejemplo, el estilo común de un error genérico de PHP indica que un sistema ciertamente está ejecutando PHP. Si un atacante está en una página `.html`, y quiere probar qué motor hay tras de ese servidor (para buscar debilidades en el sistema), lo alimenta con datos erróneos que lo podrían habilitar a que determine que ese sistema fue construido con PHP.

El error de una función puede indicar ya sea, un sistema que puede estar ejecutando un motor específico de base de datos, o dar las pistas de cómo una página web puede estar programada o diseñada. Esto permite una investigación más profunda dentro de los puertos abiertos de la base de datos, o buscar errores específicos o debilidades en una página web. Pasando diferentes porciones de datos erróneos, por ejemplo, un atacante puede determinar el orden de autenticación en un script, (por medio del número de línea de los errores) como también probar exploits que pueden ser utilizados en diferentes ubicaciones del script.

Un error del sistema de archivos o un error general de PHP puede indicar qué permisos tiene el servidor web, así también la estructura y organización de ficheros en el servidor web. El código de error escrito por el desarrollador puede agravar este problema, conllevando a la explotación fácil de la, hasta entonces, información "oculta".

Hay tres grandes soluciones a este problema. La primera consiste en examinar todas las funciones, e intentar arreglar la mayoría de los errores. La segunda es deshabilitar completamente la notificación de errores de el código en ejecución. La tercera es utilizar las funciones de manejo de error propias de PHP para crear su propio manejador de errores. Dependiendo de su política de seguridad, puede ser que encuentre que las tres sean aplicables a su situación.

Una forma de detectar este problema por adelantado es hacer uso de la función propia de PHP `error_reporting`, para ayudarle a asegurar su código y encontrar el uso de variables que podrían ser peligrosas. Al probar su código, antes de distribuirlo, con `E_ALL`, usted puede encontrar rapidamente áreas donde sus variables pueden ser abiertas para envenenamiento o modificación en otras maneras. Una vez usted está listo para distribuirlo, debería deshabilitar completamente el reporte de errores poniendo el valor de `error_reporting` a 0, o apagar el visor de errores utilizando la opción `display_errors` del fichero `php.ini` para aislar su código de ataques. Si decide hacer esto último, también debería definir la ruta de acceso a su archivo de registros utilizando la directiva `error_log`, y poner `log_errors` en "on".

Buscando variables peligrosas con E_ALL

```php
<?php
if ($username) {  // No se ha inicializado o revisado antes de utilizar
    $good_login = 1;
}
if ($good_login == 1) { // Si la prueba anterior falla, los que no estén inicializados o comprobados antes de utilizar, tendrán acceso
    readfile("/ruta/hacia/datos/altamente/sensibles/index.html");
}
?>

     
```
