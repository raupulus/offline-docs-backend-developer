---
title: strip_tags
description: Elimina las etiquetas HTML y PHP de un string
source_url: https://www.php.net/manual/es/function.strip-tags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strip-tags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: 8cdc6621f
order: 89290
---

strip_tags

Elimina las etiquetas HTML y PHP de un string

## Descripción

```php
strip_tags(string $string, [array $allowed_tags]): string
```php

`strip_tags` intenta devolver el string `string` después de eliminar todos los bytes nulos, todas las etiquetas PHP y HTML del código. Genera alertas si las etiquetas están incompletas o son erróneas. Utiliza el mismo motor de búsqueda que `fgetss`.

## Parámetros

`string`  
El string de entrada.

`allowed_tags`  
Puede utilizarse este argumento opcional para especificar las etiquetas que no deben ser eliminadas. Pueden ser proporcionadas como `string` o, a partir de PHP 7.4.0, como `array`. Consúltese los ejemplos a continuación para el formato de este argumento.

> [!NOTE]
> Los comentarios HTML y PHP también son eliminados. Este comportamiento no puede ser modificado con el argumento `allowed_tags`.

> [!NOTE]
> Las etiquetas XHTML auto-cerradas son ignoradas y solo las etiquetas que no son auto-cerradas deben ser utilizadas en el string `allowed_tags`. Por ejemplo, para permitir tanto `<br>` como `<br/>`, se debe utilizar:
>
> <div class="informalexample">
>
> ```
> <?php
> strip_tags($input, '<br>');
> ?>
>
>         
> ```
>
> </div>

## Valores devueltos

Devuelve el string escapado.

## Historial de cambios

| Versión | Descripción                              |
|---------|------------------------------------------|
| 8.0.0   | `allowed_tags` ahora puede ser nullable. |
| 7.4.0   | `allowed_tags` ahora acepta un `array`.  |

## Ejemplos

Ejemplo con `strip_tags`

```
<?php
$text = '<p>Test paragraph.</p><!-- Comment --> <a href="#fragment">Other text</a>';
echo strip_tags($text);
echo "\n";

// Permite <p> y <a>
echo strip_tags($text, '<p><a>');

// a partir de PHP 7.4.0 la línea anterior puede ser escrita como:
// echo strip_tags($text, ['p', 'a']);
?>

    
```php

El ejemplo anterior mostrará:

    Test paragraph. Other text
    <p>Test paragraph.</p> <a href="#fragment">Other text</a>

## Notas

> [!WARNING]
> Esta función no debería ser utilizada para prevenir ataques XSS. Utilizar funciones más apropiadas como `htmlspecialchars` u otros métodos según el contexto de la salida.

> [!WARNING]
> Como `strip_tags` no valida el HTML, las etiquetas parciales o rotas pueden conducir a la eliminación de más texto/datos de lo deseado.

> [!WARNING]
> `strip_tags` no modifica los atributos de las etiquetas que se autorizan mediante el argumento `allowed_tags`, incluyendo los atributos `style` y `onmouseover`, que usuarios malintencionados pueden utilizar.

> [!NOTE]
> Los nombres de las etiquetas en el HTML de entrada que son superiores a 1023 bytes de longitud serán tratados como inválidos, según el argumento `allowed_tags`.

## Véase también

`htmlspecialchars`
