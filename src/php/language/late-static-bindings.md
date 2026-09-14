---
title: Late Static Bindings (Resolución estática en tiempo de ejecución)
source_url: https://www.php.net/manual/es/language.oop5.late-static-bindings.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/late-static-bindings.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 009f215fc
order: 2500
---

## Late Static Bindings (Resolución estática en tiempo de ejecución)

PHP implementa una funcionalidad llamada late static binding, en español la resolución estática en tiempo de ejecución, que puede ser utilizada para referenciar la clase llamada en un contexto de herencia estática.

Más precisamente, las resoluciones estáticas en tiempo de ejecución funcionan registrando el nombre de la clase en la última "llamada no reenviada". En el caso de las llamadas de métodos estáticos, se trata de la clase explícitamente nombrada (generalmente, la que está a la izquierda del operador [`::`](#language.oop5.paamayim-nekudotayim)) ; en el caso de métodos no estáticos, se trata de la clase del objeto. Una "llamada reenviada" es una llamada estática introducida por `self::`, `parent::`, `static::`, o, subiendo en la jerarquía de clases, `forward_static_call`. La función `get_called_class` puede ser utilizada para recuperar una cadena que contiene el nombre de la clase llamada, y `static::` introduce su ámbito.

Esta funcionalidad ha sido bautizada como "late static bindings", con un punto de vista interno. "Late binding", literalmente resolución tardía, proviene del hecho de que los elementos `static::` no serán resueltos utilizando la clase donde el método ha sido definido, sino que será calculada utilizando la información en tiempo de ejecución. También se denomina "static binding" ya que puede ser utilizado para (sin estar limitado a) los métodos estáticos.

## Limitaciones de `self::`

Las referencias estáticas a la clase actual, con `self::` o `__CLASS__`, son resueltas utilizando la clase a la que pertenecen las funciones, es decir, donde fueron definidas:

Uso de `self::`

```php
<?php

class A
{
    public static function who()
    {
        echo __CLASS__;
    }

    public static function test()
    {
        self::who();
    }
}

class B extends A
{
    public static function who()
    {
         echo __CLASS__;
    }
}

B::test();

?>

    
```

El ejemplo anterior mostrará:

    A

## Uso de la resolución estática en tiempo de ejecución

La resolución estática en tiempo de ejecución intenta superar esta limitación introduciendo una palabra clave que hace referencia a la clase que ha sido llamada durante la ejecución. Para simplificar, esta palabra clave permite la referencia a `B` desde `test()`, en el ejemplo anterior. Se decidió no introducir una nueva palabra clave, sino más bien utilizar la palabra `static` que ya estaba reservada.

Uso simple de `static::`

```php
<?php

class A
{
    public static function who()
    {
        echo __CLASS__;
    }

    public static function test()
    {
        static::who(); // Aquí, resolución estática en tiempo de ejecución
    }
}

class B extends A
{
    public static function who()
    {
         echo __CLASS__;
    }
}

B::test();

?>

    
```

El ejemplo anterior mostrará:

    B

> [!NOTE]
> En contextos no estáticos, la clase llamada será la del objeto. Como `$this->` intentará llamar a métodos privados desde el mismo ámbito, utilizar `static::` podría dar resultados diferentes. Tenga en cuenta también que `static::` solo puede hacer referencia a propiedades estáticas.

Uso de `static::` en un contexto no estático

```php
<?php

class A
{
    private function foo()
    {
        echo "Success!\n";
    }

    public function test()
    {
        $this->foo();
        static::foo();
    }
}

class B extends A
{
   /* foo() será copiada en B, por lo tanto su ámbito será siempre A
    * y la llamada se realizará sin problemas */
}

class C extends A
{
    private function foo()
    {
        /* El método original es reemplazado; el ámbito es el de C */
    }
}

$b = new B();
$b->test();

$c = new C();
try {
    $c->test();
} catch (Error $e) {
    echo $e->getMessage();
}

?>

    
```

El ejemplo anterior mostrará:

    Success!
    Success!
    Success!
    Call to private method C::foo() from scope A

> [!NOTE]
> La resolución de estáticos en tiempo de ejecución se detendrá en una llamada estática completamente resuelta. Por otro lado, las llamadas estáticas utilizando una palabra clave como `parent::` o `self::` reenviarán la información de llamada.
>
> <div class="example">
>
> <div class="title">
>
> Llamadas con o sin reenvío
>
> </div>
>
> ```
> <?php
>
> class A
> {
>     public static function foo()
>     {
>         static::who();
>     }
>
>     public static function who()
>     {
>         echo __CLASS__."\n";
>     }
> }
>
> class B extends A
> {
>     public static function test()
>     {
>         A::foo();
>         parent::foo();
>         self::foo();
>     }
>
>     public static function who()
>     {
>         echo __CLASS__."\n";
>     }
> }
> class C extends B
> {
>     public static function who()
>     {
>         echo __CLASS__."\n";
>     }
> }
>
> C::test();
>
> ?>
>
>      
> ```
>
> El ejemplo anterior mostrará:
>
>     A
>     C
>     C
>
>          
>
> </div>
