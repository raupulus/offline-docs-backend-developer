---
title: iconv
description: Convierte una cadena de caracteres de un encodaje a otro
source_url: https://www.php.net/manual/es/function.iconv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/iconv/functions/iconv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: iconv
translation_status: ready
translation_reviewed: true
translation_revision: a22353190
order: 31260
---

iconv

Convierte una cadena de caracteres de un encodaje a otro

## Descripción

```php
iconv(string $from_encoding, string $to_encoding, string $string): string
```php

Convierte la cadena `string` desde `from_encoding` hacia el encodaje `to_encoding`.

## Parámetros

`from_encoding`  
El encodaje utilizado para interpretar `string`.

`to_encoding`  
El encodaje deseado del resultado.

Si la cadena `//TRANSLIT` es añadida al argumento `to_encoding`, entonces la transliteración es activada. Esto significa que cuando un carácter no puede ser representado en el juego de caracteres destino, podría ser representado aproximadamente a partir de uno o varios caracteres que representen el mismo carácter. Si la cadena `//IGNORE` es añadida, los caracteres que no puedan ser representados en el juego de caracteres destino serán simplemente ignorados. De lo contrario, se generará una alerta de nivel `E_NOTICE` y la función retornará `false`.

> [!CAUTION]
> Si y cómo `//TRANSLIT` funciona exactamente depende de la implementación iconv() del sistema (cf. `ICONV_IMPL`). Algunas implementaciones son conocidas por ignorar `//TRANSLIT`, por lo que la conversión de caracteres ilegales probablemente fallará para `to_encoding`.

`string`  
La `string` a convertir.

## Valores devueltos

Retorna la `string` convertida, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `iconv`

```
<?php
$text = "Ceci est le symbole de l'Euro '€'.";

echo 'Original : ', $text, PHP_EOL;
echo 'TRANSLIT : ', iconv("UTF-8", "ISO-8859-1//TRANSLIT", $text), PHP_EOL;
echo 'IGNORE   : ', iconv("UTF-8", "ISO-8859-1//IGNORE", $text), PHP_EOL;
echo 'Brut     : ', iconv("UTF-8", "ISO-8859-1", $text), PHP_EOL;
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Original : Ceci est le symbole de l'Euro '€'.
    TRANSLIT : Ceci est le symbole de l'Euro 'EUR'.
    IGNORE   : Ceci est le symbole de l'Euro ''.
    Brut     : Ceci est le symbole de l'Euro '
    Notice: iconv(): Detected an illegal character in input string in /Users/macbook/Desktop/- on line 8
    Ceci est le symbole de l'Euro '

## Notas

> [!NOTE]
> El encodaje de caracteres y las opciones disponibles dependen de la implementación de iconv. Si el argumento de `from_encoding` o `to_encoding` no es soportado en el sistema actual, `false` será retornado.

## Véase también

`mb_convert_encoding`, UConverter::transcode
