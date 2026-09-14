---
title: Operadores de incremento y decremento
source_url: https://www.php.net/manual/es/language.operators.increment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/operators/increment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 16934048f
order: 2730
---

## Operadores de incremento y decremento

PHP soporta los operadores de pre- y post- incremento y decremento. Estos operadores unaires permiten aumentar o disminuir la valor de un.

| Ejemplo | Nombre          | Resultado                                 |
|---------|-----------------|-------------------------------------------|
| ++\$a   | Pre-incrementa  | Incrementa `$a` en 1, luego retorna `$a`. |
| \$a++   | Post-incrementa | Retorna `$a`, luego incrementa `$a` en 1. |
| --\$a   | Pre-decrementa  | Decrementa `$a` en 1, luego retorna `$a`. |
| \$a--   | Post-decrementa | Retorna `$a`, luego decrementa `$a` en 1. |

Operadores de incremento y decremento

A continuación, se presenta un ejemplo simple:

Ejemplos de incremento/decremento

```php
<?php
echo 'Post-incremento:', PHP_EOL;
$a = 5;
var_dump($a++);
var_dump($a);
echo 'Pre-incremento:', PHP_EOL;
$a = 5;
var_dump(++$a);
var_dump($a);
echo 'Post-decremento:', PHP_EOL;
$a = 5;
var_dump($a--);
var_dump($a);
echo 'Pre-decremento:';
$a = 5;
var_dump(--$a);
var_dump($a);
?>

   
```

El ejemplo anterior mostrará:

    Post-incremento:
    int(5)
    int(6)
    Pre-incremento:
    int(6)
    int(6)
    Post-decremento:
    int(5)
    int(4)
    Pre-decremento:
    int(4)
    int(4)

> [!WARNING]
> Los operadores de incremento y decremento no tienen ningún efecto sobre los valores de tipo `bool`. Un `E_WARNING` es emitido a partir de PHP 8.3.0, ya que esto convertirá implícitamente el valor en `int` en el futuro.
>
> El operador de decremento no tiene ningún efecto sobre los valores de tipo `null`. Un `E_WARNING` es emitido a partir de PHP 8.3.0, ya que esto convertirá implícitamente el valor en `int` en el futuro.
>
> El operador de decremento no tiene ningún efecto sobre los strings no- [numéricos](#language.types.numeric-strings). Un `E_WARNING` es emitido a partir de PHP 8.3.0, ya que una `TypeError` será levantada en el futuro.

> [!NOTE]
> Los objetos internos que soportan la sobrecarga de la adición y/o la sustracción pueden ser incrementados y/o decrementados asimismo. Un objeto interno de este tipo es `GMP`.

## Funcionalidad de incremento de strings PERL

> [!WARNING]
> Esta funcionalidad es deprecada de manera suave a partir de PHP 8.3.0. La función `str_increment` debe ser utilizada en su lugar.

Es posible incrementar un [string no numérico](#language.types.numeric-strings) en PHP. El string debe ser un string ASCII alfanumérico. Esto incrementa las letras hasta la siguiente letra, y cuando se alcanza la letra `Z`, el incremento se reporta al valor a la izquierda. Por ejemplo, `$a = 'Z'; $a++;` transforma `$a` en `'AA'`.

Ejemplo de incremento de string PERL

```php
<?php
echo '== Strings alfabéticos ==' . PHP_EOL;
$s = 'W';
for ($n=0; $n<6; $n++) {
    echo ++$s . PHP_EOL;
}
// Los strings alfanuméricos se comportan de manera diferente
echo '== Caracteres digitales ==' . PHP_EOL;
$d = 'A8';
for ($n=0; $n<6; $n++) {
    echo ++$d . PHP_EOL;
}
$d = 'A08';
for ($n=0; $n<6; $n++) {
    echo ++$d . PHP_EOL;
}
?>

   
```

El ejemplo anterior mostrará:

    == Strings alfabéticos ==
    X
    Y
    Z
    AA
    AB
    AC
    == Strings alfanuméricos ==
    A9
    B0
    B1
    B2
    B3
    B4
    A09
    A10
    A11
    A12
    A13
    A14

> [!WARNING]
> Si el string alfanumérico puede ser interpretado como un [string numérico](#language.types.numeric-strings), será convertido en `int` o en `float`. Esto es particularmente problemático con los strings que se asemejan a números de punto flotante escritos en notación exponencial. La función `str_increment` no sufre de estas conversiones de tipo implícitas.
>
> <div class="example">
>
> <div class="title">
>
> Conversión de string alfanumérico a flotante
>
> </div>
>
> ```
> <?php
> $s = "5d9";
> var_dump(++$s);
> var_dump(++$s);
> ?>
>
>     
> ```
>
> El ejemplo anterior mostrará:
>
>     string(3) "5e0"
>     float(6)
>
>         
>
> Esto se debe a que el valor `"5e0"` es interpretado como un `float` y convertido en el valor `5.0` antes de ser incrementado.
>
> </div>
