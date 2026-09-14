---
title: strtok
description: Divide una cadena en segmentos
source_url: https://www.php.net/manual/es/function.strtok.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strtok.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: 45042fef6
order: 89470
---

strtok

Divide una cadena en segmentos

## Descripción

```php
strtok(string $string, string $token): string
```php

Firma alternativa (no soportada con argumentos nombrados):

```php
strtok(string $token): string
```

`strtok` divide la cadena `string` en segmentos, cada segmento está delimitado por `token`. Por ejemplo, si se tiene una cadena como `"Este es un buen ejemplo"`, se pueden extraer las diferentes palabras utilizando el espacio como `token`.

Tenga en cuenta que solo la primera llamada a `strtok` utiliza el argumento `string`. Todas las llamadas posteriores a `strtok` requieren únicamente el `token` a utilizar, ya que sabe dónde se encuentra en la cadena actual. Para reiniciar o dividir una nueva cadena, simplemente se puede llamar a `strtok` con el parámetro `string` nuevamente para inicializarlo. Cabe señalar que es posible incluir varios tokens en el parámetro `token`. La cadena `string` se dividirá tan pronto como se encuentre uno de los caracteres del argumento `token`.

> [!NOTE]
> Esta función se comporta de manera ligeramente diferente a lo que se podría esperar al estar familiarizado con `explode`. En primer lugar, una secuencia de dos o más caracteres `token` contiguos en la cadena analizada se considera como un único delimitador. Además, un `token` situado al inicio o al final de la cadena es ignorado. Por ejemplo, si la cadena `";aaa;;bbb;"` es utilizada, las llamadas sucesivas a `strtok` con `";"` como `token` devolverán las cadenas "aaa" y "bbb", y luego `false`. Por lo tanto, la cadena se dividirá simplemente en dos elementos, mientras que `explode(";", $string)` devolvería un array de 5 elementos.

## Parámetros

`string`  
La cadena a dividir en varias cadenas de menor tamaño (tokens).

`token`  
El delimitador utilizado para dividir `string`.

## Valores devueltos

Una `string` dividida, o `false` si no hay más tokens disponibles.

## Historial de cambios

| Versión | Descripción                                                       |
|---------|-------------------------------------------------------------------|
| 8.3.0   | Ahora emite un `E_WARNING` cuando el `token` no es proporcionado. |

## Ejemplos

Ejemplo con `strtok`

```php
<?php
$string = "This is\tan example\nstring";
// Utilice también las nuevas líneas y las tabulaciones
// como separador de palabras
$tok = strtok($string, " \n\t");

while ($tok !== false) {
    echo "Word={$tok}\n";
    $tok = strtok(" \n\t");
}
?>

    
```

Comportamiento de `strtok` al encontrar una parte vacía

```php
<?php
$first_token  = strtok('/something', '/');
$second_token = strtok('/');
var_dump($first_token, $second_token);
?>

    
```

El ejemplo anterior mostrará:

        string(9) "something"
        bool(false)

La diferencia entre `strtok` y `explode`

```php
<?php
$string = ";aaa;;bbb;";

$parts = [];
$tok = strtok($string, ";");
while ($tok !== false) {
    $parts[] = $tok;
    $tok = strtok(";");
}
echo json_encode($parts),"\n";

$parts = explode(";", $string);
echo json_encode($parts),"\n";

    
```

El ejemplo anterior mostrará:

    ["aaa","bbb"]
    ["","aaa","","bbb",""]

## Notas

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Véase también

`explode`
