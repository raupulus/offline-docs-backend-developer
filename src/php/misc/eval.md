---
title: eval
description: Ejecuta una cadena como un script PHP
source_url: https://www.php.net/manual/es/function.eval.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/eval.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: 78d17c25e
order: 47060
---

eval

Ejecuta una cadena como un script PHP

## Descripción

```php
eval(string $code): mixed
```php

Evalúa el `code` proporcionado como código PHP.

El código en evaluación hereda el [ámbito de las variables](#language.variables.scope) de la línea en la que se realiza la llamada a `eval`. Todas las variables disponibles en esa línea serán accesibles en lectura y modificación en el código evaluado. Sin embargo, todas las funciones y clases definidas se definirán en el espacio de nombres global. En otras palabras, el compilador considera el código evaluado como si se tratara de un [archivo incluido](#function.include) separado.

> [!CAUTION]
> La construcción de lenguaje `eval` es *muy peligrosa* ya que permite la ejecución de código PHP arbitrario. *Su uso se desaconseja encarecidamente.* Si se ha verificado cuidadosamente que no hay otras opciones que utilizarla, se debe prestar una atención especial *a no pasar datos provenientes de un usuario* sin haberlos validado previamente de manera minuciosa.

## Parámetros

`code`  
Código PHP válido a evaluar.

El código no debe estar rodeado de [etiquetas PHP](#language.basic-syntax.phpmode) de apertura y cierre, es decir, `'echo "Hi!";'` debe ser pasado en lugar de `'<?php echo "Hi!"; >'`. Siempre es posible salir y volver al modo PHP utilizando las etiquetas PHP apropiadas, es decir, `'echo "En modo PHP !"; ?>En modo HTML !<?php echo "Retorno al modo PHP !";'`.

Además de esto, el código PHP pasado debe ser válido. Esto incluye que todas las instrucciones deben terminar con un punto y coma. `'echo "Hi!"'` por ejemplo resultará en un error fatal, mientras que `'echo "Hi!";'` funcionará.

Una instrucción `return` terminará inmediatamente la evaluación del código.

El código se ejecutará en el ámbito del código que llama a la función `eval`. Por lo tanto, todas las variables definidas o modificadas en la llamada a la función `eval` seguirán siendo visibles después de la finalización de la ejecución de la función.

## Valores devueltos

`eval` devuelve `null` a menos que `return` sea llamado en el código evaluado, en cuyo caso el valor pasado a `return` es devuelto. A partir de PHP 7, si hay un error de sintaxis en el código evaluado, `eval` lanza una excepción `ParseError`. Antes de PHP 7, en este caso `eval` devuelve `false` y la ejecución del código siguiente continúa normalmente. No es posible capturar el error de análisis de la función `eval` utilizando la función `set_error_handler`.

## Ejemplos

Ejemplo con `eval` - concatenación de texto

```
<?php
$string = 'taza';
$name = 'café';
$str = 'Esto es un $string con mi $name dentro.<br />';
echo $str;
eval( "\$str = \"$str\";" );
echo $str;
?>

    
```php

El ejemplo anterior mostrará:

    Esto es un $string con mi $name dentro.
    Esto es una taza con mi café dentro.

## Notas

> [!NOTE]
> Como esto es una estructura del lenguaje, y no una función, no es posible llamarla con las [funciones variables](#functions.variable-functions) o [argumentos nombrados](#functions.named-arguments).

> [!TIP]
> Al igual que con cualquier cosa que envíe sus resultados directamente al navegador, las [funciones de control de salida](#book.outcontrol) se pueden usar para capturar la salida de esta función y guardarla en un `string` (por ejemplo).

> [!NOTE]
> En caso de un error fatal en el código evaluado, todo el script se terminará.

## Véase también

`call_user_func`
