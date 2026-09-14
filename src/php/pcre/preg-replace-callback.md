---
title: preg_replace_callback
description: Buscar y reemplazar mediante expresión regular estándar utilizando una
  función de retrollamada
source_url: https://www.php.net/manual/es/function.preg-replace-callback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcre/functions/preg-replace-callback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcre
translation_status: ready
translation_reviewed: true
translation_revision: c1f37a6c2
order: 61650
---

preg_replace_callback

Buscar y reemplazar mediante expresión regular estándar utilizando una función de retrollamada

## Descripción

```php
preg_replace_callback(string $pattern, callable $callback, string $subject, [int $limit], [int $count], [int $flags]): string
```php

El comportamiento de esta función es casi idéntico al de `preg_replace`, con la excepción de que en lugar del argumento `replacement`, se debe especificar una función de retrollamada `callback` que será llamada con los elementos encontrados como argumentos.

## Parámetros

`pattern`  
El patrón a buscar. Puede ser una cadena o un array que contenga cadenas.

`callback`  
La función de retrollamada que recibirá el array de elementos encontrados en la cadena `subject`. La función de retrollamada debe devolver la cadena de reemplazo. Esta es la firma de la función de retrollamada:

```php
handler(array $matches): string
```

Con frecuencia, la función `callback` se utiliza con `preg_replace_callback` en un solo lugar. En este caso, puede simplemente utilizar una [función anónima](#functions.anonymous) para declarar una función de retrollamada para `preg_replace_callback`. Al hacer esto, se concentran todas las rutinas relacionadas con el reemplazo en un solo lugar, y no se contamina el espacio de nombres de funciones con funciones de un solo uso.

`preg_replace_callback` y función anónima

```php
<?php
// Un filtro de línea de comandos Unix para convertir la primera letra
// de los párrafos (que comienzan con "<p>") a minúscula

$fp = fopen("php://stdin", "r") or die("No se puede leer la línea de comandos");
while (!feof($fp)) {
    $line = fgets($fp);
    $line = preg_replace_callback(
        '|<p>\s*\w|',
        function ($matches) {
            return strtolower($matches[0]);
        },
        $line
    );
    echo $line;
}
fclose($fp);
?>

        
```

`subject`  
La cadena o el array de cadenas a buscar y reemplazar.

`limit`  
El número máximo de reemplazos para cada patrón en cada cadena `subject`. Por omisión, vale `-1` (sin límite).

`count`  
Si se proporciona, esta variable será rellenada con el número de reemplazos realizados.

`flags`  
`flags` puede ser una combinación de los indicadores `PREG_OFFSET_CAPTURE` y `PREG_UNMATCHED_AS_NULL`, que influyen en el formato del array de coincidencias. Consulte la descripción de `preg_match` para más detalles.

## Valores devueltos

`preg_replace_callback` devuelve un array si el argumento `subject` es un array, o de lo contrario, una cadena. Si ocurre un error, el valor devuelto será `null`.

Si se encuentran coincidencias, se devuelve el nuevo sujeto, de lo contrario `subject` se devuelve sin cambios.

## Errores/Excepciones

Si el patrón regex pasado no se compila a una regex válida, se emite una `E_WARNING`.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 7.4.0   | Se añadió el argumento `flags`. |

## Ejemplos

Ejemplo con `preg_replace_callback`

```php
<?php
// Este texto era cierto en 2002
// queremos actualizarlo para 2003
$text = "El primer abril es el 04/01/2002\n";
$text.= "La última navidad fue el 12/24/2001\n";

// Función de retrollamada
function next_year($matches)
{
  // como de costumbre: $matches[0] representa el valor total
  // $matches[1] representa el primer paréntesis capturante
  return $matches[1].($matches[2]+1);
}
echo preg_replace_callback(
            "|(\d{2}/\d{2}/)(\d{4})|",
            "next_year",
            $text);

?>

    
```

El ejemplo anterior mostrará:

    El primer abril es el 04/01/2003
    La última navidad fue el 12/24/2002

Ejemplo con `preg_replace_callback` utilizando una estructura recursiva para manejar BB code

```php
<?php
$input = "plain [indent] deep [indent] deeper [/indent] deep [/indent] plain";

function parseTagsRecursive($input)
{

    $regex = '#\[indent]((?:[^[]|\[(?!/?indent])|(?R))+)\[/indent]#';

    if (is_array($input)) {
        $input = '<div style="margin-left: 10px">'.$input[1].'</div>';
    }

    return preg_replace_callback($regex, 'parseTagsRecursive', $input);
}

$output = parseTagsRecursive($input);

echo $output;
?>

    
```

## Véase también

[Patrones PCRE](#pcre.pattern), `preg_replace_callback_array`, `preg_quote`, `preg_replace`, `preg_last_error`, [Las funciones anónimas](#functions.anonymous)
