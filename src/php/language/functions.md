---
title: Functions
source_url: https://www.php.net/manual/es/language.functions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/functions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: e290572f2
order: 2350
---

## Functions

## User-defined functions

A function is defined using the `function` keyword, a name, a list of parameters (which might be empty) separated by commas (`,`) enclosed in parentheses, followed by the body of the function enclosed in curly braces, such as the following:

Declaring a new function named `foo`

```php
<?php
function foo($arg_1, $arg_2, /* ..., */ $arg_n)
{
    echo "Example function.\n";
    return $retval;
}

    
```

> [!NOTE]
> As of PHP 8.0.0, the list of parameters may have a trailing comma:
>
> <div class="informalexample">
>
> ```
> <?php
> function foo($arg_1, $arg_2,) { }
>
>       
> ```
>
> </div>

Any valid PHP code may appear inside the body of a function, even other functions and [class](#language.oop5.basic.class) definitions.

Function names follow the same rules as other labels in PHP. A valid function name starts with a letter or underscore, followed by any number of letters, numbers, or underscores. As a regular expression, it would be expressed thus: `^[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*$`.

> [!TIP]
> Véase también [???](#userlandnaming).

Functions need not be defined before they are referenced, *except* when a function is conditionally defined as shown in the two examples below.

When a function is defined in a conditional manner such as the two examples shown. Its definition must be processed *prior* to being called.

Conditional functions

```php
<?php
$makefoo = true;

/* We can't call foo() from here 
   since it doesn't exist yet,
   but we can call bar() */
if (function_exists('foo')) {
    foo();
} else {
    echo "Function foo does not exist (yet).\n";
}

bar();

if ($makefoo) {
  function foo()
  {
    echo "I don't exist until program execution reaches me.\n";
  }
}

/* Now we can safely call foo()
   since $makefoo evaluated to true */

if ($makefoo) foo();

function bar() 
{
  echo "I exist immediately upon program start.\n";
}

     
```

Functions within functions

```php
<?php
function foo() 
{
  function bar() 
  {
    echo "I don't exist until foo() is called.\n";
  }
}

/* We can't call bar() yet
   since it doesn't exist. */
if (function_exists('bar')) {
    bar();
}

foo();

/* Now we can call bar(),
   foo()'s processing has
   made it accessible. */

bar();

     
```

All functions and classes in PHP have the global scope - they can be called outside a function even if they were defined inside and vice versa.

PHP does not support function overloading, nor is it possible to undefine or redefine previously-declared functions.

> [!NOTE]
> Function names are case-insensitive for the ASCII characters `A` to `Z`, though it is usually good form to call functions as they appear in their declaration.

Both [variable number of arguments](#functions.variable-arg-list) and [default arguments](#functions.arguments.default) are supported in functions. See also the function references for `func_num_args`, `func_get_arg`, and `func_get_args` for more information.

It is possible to call recursive functions in PHP.

Recursive functions

```php
<?php
function recursion($a)
{
    if ($a < 20) {
        echo "$a\n";
        recursion($a + 1);
    }
}

recursion(17);

     
```

> [!NOTE]
> Recursive function/method calls with over 100-200 recursion levels can smash the stack and cause a termination of the current script. Especially, infinite recursion is considered a programming error.

## Function parameters and arguments

The function parameters are declared in the function signature. Information may be passed to functions via the argument list, which is a comma-delimited list of expressions. The arguments are evaluated from left to right and the result is assigned to the parameters of the function, before the function is actually called (*eager* evaluation).

PHP supports passing arguments by value (the default), [passing by reference](#functions.arguments.by-reference), and [default argument values](#functions.arguments.default). [Variable-length argument lists](#functions.variable-arg-list) and [Named Arguments](#functions.named-arguments) are also supported.

> [!NOTE]
> As of PHP 7.3.0, it is possible to have a trailing comma in the argument list for a function calls:
>
> <div class="informalexample">
>
> ```
> <?php
> $v = foo(
>     $arg_1,
>     $arg_2,
> );
>
>       
> ```
>
> </div>

As of PHP 8.0.0, the list of function parameters may include a trailing comma, which will be ignored. That is particularly useful in cases where the list of parameters is long or contains long variable names, making it convenient to list parameters vertically.

Function parameter list with trailing comma

```php
<?php
function takes_many_args(
    $first_arg,
    $second_arg,
    $a_very_long_argument_name,
    $arg_with_default = 5,
    $again = 'a default string', // This trailing comma was not permitted before 8.0.0.
)
{
    // ...
}

    
```

### Passing arguments by reference

By default, function arguments are passed by value (so that if the value of the argument within the function is changed, it does not get changed outside of the function). To allow a function to modify its arguments, they must be passed by reference.

To have an argument to a function always passed by reference, prepend an ampersand (&) to the parameter name in the function definition:

Passing function arguments by reference

```php
<?php
function add_some_extra(&$string)
{
    $string .= 'and something extra.';
}
$str = 'This is a string, ';
add_some_extra($str);
echo $str;    // outputs 'This is a string, and something extra.'

      
```

It is an error to pass a constant expression as an argument to a parameter that expects to be passed by reference.

### Default parameter values

A function may define default values for parameters using syntax similar to assigning a variable. The default is used only when the parameter's argument is not passed. Note that passing `null` does *not* assign the default value.

Use of default parameters in functions

```php
<?php
function makecoffee($type = "cappuccino")
{
    return "Making a cup of $type.\n";
}
echo makecoffee();
echo makecoffee(null);
echo makecoffee("espresso");

      
```

El ejemplo anterior mostrará:

    Making a cup of cappuccino.
    Making a cup of .
    Making a cup of espresso.

Default parameter values may be scalar values, `array`s, the special type `null`, and as of PHP 8.1.0, objects using the [new ClassName()](#language.oop5.basic.new) syntax.

Using non-scalar types as default values

```php
<?php
function makecoffee($types = array("cappuccino"), $coffeeMaker = NULL)
{
    $device = is_null($coffeeMaker) ? "hands" : $coffeeMaker;
    return "Making a cup of ".join(", ", $types)." with $device.\n";
}
echo makecoffee();
echo makecoffee(array("cappuccino", "lavazza"), "teapot");

      
```

El ejemplo anterior mostrará:

    Making a cup of cappuccino with hands.
    Making a cup of cappuccino, lavazza with teapot.

Using objects as default values (as of PHP 8.1.0)

```php
<?php
class DefaultCoffeeMaker {
    public function brew() {
        return "Making coffee.\n";
    }
}
class FancyCoffeeMaker {
    public function brew() {
        return "Crafting a beautiful coffee just for you.\n";
    }
}
function makecoffee($coffeeMaker = new DefaultCoffeeMaker)
{
    return $coffeeMaker->brew();
}
echo makecoffee();
echo makecoffee(new FancyCoffeeMaker);

      
```

El ejemplo anterior mostrará:

    Making coffee.
    Crafting a beautiful coffee just for you.

The default value must be a constant expression, not (for example) a variable, a class member or a function call.

Note that any optional parameters should be specified after any required parameters, otherwise they cannot be omitted from calls. Consider the following example:

Incorrect usage of default function parameters

```php
<?php
function makeyogurt($container = "bowl", $flavour)
{
    return "Making a $container of $flavour yogurt.\n";
}

echo makeyogurt("raspberry"); // "raspberry" is $container, not $flavour

      
```

El ejemplo anterior mostrará:

    Deprecated: makeyogurt(): Optional parameter $container declared before required parameter $flavour is implicitly treated as a required parameter in script on line 2

    Fatal error: Uncaught ArgumentCountError: Too few arguments to function makeyogurt(), 1 passed in script on line 7 and exactly 2 expected in script:2
    Stack trace:
    #0 script(7): makeyogurt('raspberry')
    #1 {main}
      thrown in script on line 2

Now, compare the above with this:

Correct usage of default function parameters

```php
<?php
function makeyogurt($flavour, $container = "bowl")
{
    return "Making a $container of $flavour yogurt.\n";
}

echo makeyogurt("raspberry"); // "raspberry" is $flavour

      
```

El ejemplo anterior mostrará:

    Making a bowl of raspberry yogurt.

As of PHP 8.0.0, [named arguments](#functions.named-arguments) can be used to skip over multiple optional parameters.

Correct usage of default function parameters

```php
<?php
function makeyogurt($container = "bowl", $flavour = "raspberry", $style = "Greek")
{
    return "Making a $container of $flavour $style yogurt.\n";
}

echo makeyogurt(style: "natural");

      
```

El ejemplo anterior mostrará:

    Making a bowl of raspberry natural yogurt.

As of PHP 8.0.0, declaring mandatory parameters after optional parameters is *deprecated*. This can generally be resolved by dropping the default value, since it will never be used. One exception to this rule are parameters of the form `Type $param = null`, where the `null` default makes the type implicitly nullable. This usage is deprecated as of PHP 8.4.0, and an explicit [nullable type](#language.types.declarations.nullable) should be used instead.

Declaring optional parameters after mandatory parameters

```php
<?php
function foo($a = [], $b) {}     // Default not used; deprecated as of PHP 8.0.0
function foo($a, $b) {}          // Functionally equivalent, no deprecation notice

function bar(A $a = null, $b) {} // As of PHP 8.1.0, $a is implicitly required
                                 // (because it comes before the required one),
                                 // but implicitly nullable (deprecated as of PHP 8.4.0),
                                 // because the default parameter value is null
function bar(?A $a, $b) {}       // Recommended

      
```

> [!NOTE]
> As of PHP 7.1.0, omitting a parameter which does not specify a default throws an `ArgumentCountError`; in previous versions it raised a Warning.

> [!NOTE]
> Parameters that expect the argument by reference may have a default value.

### Variable-length argument lists

PHP has support for variable-length argument lists in user-defined functions by using the `...` token.

Parameter lists may include the `...` token to denote that the function accepts a variable number of arguments. The arguments will be passed into the given variable as an `array`:

Using `...` to access variable arguments

```php
<?php
function sum(...$numbers) {
    $acc = 0;
    foreach ($numbers as $n) {
        $acc += $n;
    }
    return $acc;
}

echo sum(1, 2, 3, 4);

      
```

El ejemplo anterior mostrará:

    10

`...` can also be used when calling functions to unpack an `array` or `Traversable` variable or literal into the argument list:

Using `...` to provide arguments

```php
<?php
function add($a, $b) {
    return $a + $b;
}

echo add(...[1, 2])."\n";

$a = [1, 2];
echo add(...$a);

      
```

El ejemplo anterior mostrará:

    3
    3

You may specify normal positional parameters before the `...` token. In this case, only the trailing arguments that don't match a positional argument will be added to the array generated by `...`.

It is also possible to add a [type declaration](#language.types.declarations) before the `...` token. If this is present, then all arguments captured by `...` must match that parameter type.

Type declared variable arguments

```php
<?php
function total_intervals($unit, DateInterval ...$intervals) {
    $time = 0;
    foreach ($intervals as $interval) {
        $time += $interval->$unit;
    }
    return $time;
}

$a = new DateInterval('P1D');
$b = new DateInterval('P2D');
echo total_intervals('d', $a, $b).' days';

// This will fail, since null isn't a DateInterval object.
echo total_intervals('d', null);

      
```

El ejemplo anterior mostrará:

    3 days
    Fatal error: Uncaught TypeError: total_intervals(): Argument #2 must be of type DateInterval, null given, called in script on line 15 and defined in script:2
    Stack trace:
    #0 script(15): total_intervals('d', NULL)
    #1 {main}
      thrown in script on line 2

Finally, variable arguments can also be passed [by reference](#functions.arguments.by-reference) by prefixing the `...` with an ampersand (`&`).

### Named Arguments

PHP 8.0.0 introduced named arguments as an extension of the existing positional parameters. Named arguments allow passing arguments to a function based on the parameter name, rather than the parameter position. This makes the meaning of the argument self-documenting, makes the arguments order-independent and allows skipping default values arbitrarily.

Named arguments are passed by prefixing the value with the parameter name followed by a colon. Using reserved keywords as parameter names is allowed. The parameter name must be an identifier, specifying dynamically is not allowed.

Named argument syntax

```php
<?php
myFunction(paramName: $value);
array_foobar(array: $value);

// NOT supported.
function_name($variableStoringParamName: $value);

     
```

Positional arguments versus named arguments

```php
<?php
// Using positional arguments:
array_fill(0, 100, 50);

// Using named arguments:
array_fill(start_index: 0, count: 100, value: 50);

     
```

The order in which the named arguments are passed does not matter.

Same example as above with a different order of parameters

```php
<?php
array_fill(value: 50, count: 100, start_index: 0);

     
```

Named arguments can be combined with positional arguments. In this case, the named arguments must come after the positional arguments. It is also possible to specify only some of the optional arguments of a function, regardless of their order.

Combining named arguments with positional arguments

```php
<?php
htmlspecialchars($string, double_encode: false);
// Same as
htmlspecialchars($string, ENT_QUOTES | ENT_SUBSTITUTE | ENT_HTML401, 'UTF-8', false);

     
```

Passing an argument to the same named parameter multiple times results in an `Error` exception.

Error thrown when passing an argument to the same named parameter multiple times

```php
<?php
function foo($param) { ... }

foo(param: 1, param: 2);
// Error: Named parameter $param overwrites previous argument

foo(1, param: 2);
// Error: Named parameter $param overwrites previous argument

     
```

As of PHP 8.1.0, it is possible to use named arguments after unpacking the arguments. A named argument *must not* override an already unpacked argument.

Use named arguments after unpacking

```php
<?php
function foo($a, $b, $c = 3, $d = 4) {
  return $a + $b + $c + $d;
}

var_dump(foo(...[1, 2], d: 40)); // 46
var_dump(foo(...['b' => 2, 'a' => 1], d: 40)); // 46

var_dump(foo(...[1, 2], b: 20)); // Fatal error. Named parameter $b overwrites previous argument

     
```

## Returning values

Values are returned by using the optional return statement. Any type may be returned, including arrays and objects. This causes the function to end its execution immediately and pass control back to the line from which it was called. See `return` for more information.

> [!NOTE]
> If the `return` is omitted the value `null` will be returned.

### Use of return

Use of `return`

```php
<?php
function square($num)
{
    return $num * $num;
}
echo square(4);   // outputs '16'.

      
```

A function can not return multiple values, but similar results can be obtained by returning an array.

Returning an array to get multiple values

```php
<?php
function small_numbers()
{
    return [0, 1, 2];
}
// Array destructuring will collect each member of the array individually
[$zero, $one, $two] = small_numbers();
var_dump($zero, $one, $two);

// Prior to 7.1.0, the only equivalent alternative is using list() construct
list($zero, $one, $two) = small_numbers();

      
```

To return a reference from a function, use the reference operator & in both the function declaration and when assigning the returned value to a variable:

Returning a reference from a function

```php
<?php
function &returns_reference()
{
    return $someref;
}

$newref =& returns_reference();

      
```

For more information on references, please check out [References Explained](#language.references).

## Variable functions

PHP supports the concept of variable functions. This means that if a variable name has parentheses appended to it, PHP will look for a function with the same name as whatever the variable evaluates to, and will attempt to execute it. Among other things, this can be used to implement callbacks, function tables, and so forth.

Variable functions won't work with language constructs such as `echo`, `print`, `unset`, `isset`, `empty`, `include`, `require` and the like. Utilize wrapper functions to make use of any of these constructs as variable functions.

Variable function example

```php
<?php
function foo() {
    echo "In foo()\n";
}

function bar($arg = '')
{
    echo "In bar(); argument was '$arg'.\n";
}

// This is a wrapper function around echo
function echoit($string)
{
    echo $string;
}

$func = 'foo';
$func();        // This calls foo()

$func = 'bar';
$func('test');  // This calls bar()

$func = 'echoit';
$func('test');  // This calls echoit()

     
```

Object methods can also be called with the variable functions syntax.

Variable method example

```php
<?php
class Foo
{
    function Variable()
    {
        $name = 'Bar';
        $this->$name(); // This calls the Bar() method
    }
    
    function Bar()
    {
        echo "This is Bar";
    }
}

$foo = new Foo();
$funcname = "Variable";
$foo->$funcname();  // This calls $foo->Variable()

     
```

When calling static methods, the function call is stronger than the static property operator:

Variable method example with static properties

```php
<?php
class Foo
{
    static $variable = 'static property';
    static function Variable()
    {
        echo "Method Variable called\n";
    }
}

echo Foo::$variable ."\n"; // This prints 'static property'. It does need a $variable in this scope.
$variable = "Variable";
Foo::$variable();  // This calls $foo->Variable() reading $variable in this scope.

     
```

El ejemplo anterior mostrará:

    static property
    Method Variable called

Complex callables

```php
<?php
class Foo
{
    static function bar()
    {
        echo "bar\n";
    }
    function baz()
    {
        echo "baz\n";
    }
}

$func = array("Foo", "bar");
$func(); // prints "bar"
$func = array(new Foo, "baz");
$func(); // prints "baz"
$func = "Foo::bar";
$func(); // prints "bar"

     
```

### Véase también

`is_callable`, `call_user_func`, `function_exists`, [variable variables](#language.variables.variable)

## Internal (built-in) functions

PHP comes standard with many functions and constructs. There are also functions that require specific PHP extensions compiled in, otherwise fatal "undefined function" errors will appear. For example, to use [image](#ref.image) functions such as `imagecreatetruecolor`, PHP must be compiled with GD support. Or, to use `mysqli_connect`, PHP must be compiled with [MySQLi](#book.mysqli) support. There are many core functions that are included in every version of PHP, such as the [string](#ref.strings) and [variable](#ref.var) functions. A call to `phpinfo` or `get_loaded_extensions` will show which extensions are loaded into PHP. Also note that many extensions are enabled by default and that the PHP manual is split up by extension. See the [configuration](#configuration), [installation](#install), and individual extension chapters, for information on how to set up PHP.

Reading and understanding a function's prototype is explained within the manual section titled [how to read a function definition](#about.prototypes). It's important to realize what a function returns or if a function works directly on a passed in value. For example, `str_replace` will return the modified string while `usort` works on the actual passed in variable itself. Each manual page also has specific information for each function like information on function parameters, behavior changes, return values for both success and failure, and availability information. Knowing these important (yet often subtle) differences is crucial for writing correct PHP code.

> [!NOTE]
> If the parameters given to a function are not what it expects, such as passing an `array` where a `string` is expected, the return value of the function is undefined. In this case it will likely return `null` but this is just a convention, and cannot be relied upon. As of PHP 8.0.0, a `TypeError` exception is supposed to be thrown in this case.

> [!NOTE]
> Scalar types for built-in functions are nullable by default in coercive mode. As of PHP 8.1.0, passing `null` to an internal function parameter that is not declared nullable is discouraged and emits a deprecation notice in coercive mode to align with the behavior of user-defined functions, where scalar types need to be marked as nullable explicitly.
>
> For example, `strlen` function expects the parameter `$string` to be a non-nullable `string`. For historical reasons, PHP allows passing `null` for this parameter in coercive mode, and the parameter is implicitly cast to `string`, resulting in a `""` value. In contrast, a `TypeError` is emitted in strict mode.
>
> <div class="informalexample">
>
> ```
> <?php
> var_dump(strlen(null));
> // "Deprecated: Passing null to parameter #1 ($string) of type string is deprecated" as of PHP 8.1.0
> // int(0)
>
> var_dump(str_contains("foobar", null));
> // "Deprecated: Passing null to parameter #2 ($needle) of type string is deprecated" as of PHP 8.1.0
> // bool(true)
>
>      
> ```
>
> </div>

### Véase también

`function_exists`, [the function reference](#funcref), `get_extension_funcs`, `dl`

## Anonymous functions

Anonymous functions, also known as `closures`, allow the creation of functions which have no specified name. They are most useful as the value of `callable` parameters, but they have many other uses.

Anonymous functions are implemented using the [ `Closure`](#class.closure) class.

Anonymous function example

```php
<?php
echo preg_replace_callback('~-([a-z])~', function ($match) {
    return strtoupper($match[1]);
}, 'hello-world');
// outputs helloWorld

    
```

Closures can also be used as the values of variables; PHP automatically converts such expressions into instances of the `Closure` internal class. Assigning a closure to a variable uses the same syntax as any other assignment, including the trailing semicolon:

Anonymous function variable assignment example

```php
<?php
$greet = function($name) {
    printf("Hello %s\r\n", $name);
};

$greet('World');
$greet('PHP');

    
```

Closures may also inherit variables from the parent scope. Any such variables must be passed to the `use` language construct. As of PHP 7.1, these variables must not include [superglobals](#language.variables.predefined), `$this`, or variables with the same name as a parameter. A return type declaration of the function has to be placed *after* the `use` clause.

Inheriting variables from the parent scope

```php
<?php
$message = 'hello';

// No "use"
$example = function () {
    var_dump($message);
};
$example();

// Inherit $message
$example = function () use ($message) {
    var_dump($message);
};
$example();

// Inherited variable's value is from when the function
// is defined, not when called
$message = 'world';
$example();

// Reset message
$message = 'hello';

// Inherit by-reference
$example = function () use (&$message) {
    var_dump($message);
};
$example();

// The changed value in the parent scope
// is reflected inside the function call
$message = 'world';
$example();

// Closures can also accept regular arguments
$example = function ($arg) use ($message) {
    var_dump($arg . ' ' . $message);
};
$example("hello");

// Return type declaration comes after the use clause
$example = function () use ($message): string {
    return "hello $message";
};
var_dump($example());

    
```

Resultado del ejemplo anterior es similar a:

    Notice: Undefined variable: message in /example.php on line 6
    NULL
    string(5) "hello"
    string(5) "hello"
    string(5) "hello"
    string(5) "world"
    string(11) "hello world"
    string(11) "hello world"

As of PHP 8.0.0, the list of scope-inherited variables may include a trailing comma, which will be ignored.

Inheriting variables from the parent scope is *not* the same as using global variables. Global variables exist in the global scope, which is the same no matter what function is executing. The parent scope of a closure is the function in which the closure was declared (not necessarily the function it was called from). See the following example:

Closures and scoping

```php
<?php
// A basic shopping cart which contains a list of added products
// and the quantity of each product. Includes a method which
// calculates the total price of the items in the cart using a
// closure as a callback.
class Cart
{
    const PRICE_BUTTER  = 1.00;
    const PRICE_MILK    = 3.00;
    const PRICE_EGGS    = 6.95;

    protected $products = array();
    
    public function add($product, $quantity)
    {
        $this->products[$product] = $quantity;
    }
    
    public function getQuantity($product)
    {
        return isset($this->products[$product]) ? $this->products[$product] :
               FALSE;
    }
    
    public function getTotal($tax)
    {
        $total = 0.00;
        
        $callback =
            function ($quantity, $product) use ($tax, &$total)
            {
                $pricePerItem = constant(__CLASS__ . "::PRICE_" .
                    strtoupper($product));
                $total += ($pricePerItem * $quantity) * ($tax + 1.0);
            };
        
        array_walk($this->products, $callback);
        return round($total, 2);
    }
}

$my_cart = new Cart;

// Add some items to the cart
$my_cart->add('butter', 1);
$my_cart->add('milk', 3);
$my_cart->add('eggs', 6);

// Print the total with a 5% sales tax.
print $my_cart->getTotal(0.05) . "\n";
// The result is 54.29

    
```

Automatic binding of `$this`

```php
<?php
class Test
{
    public function testing()
    {
        return function() {
            var_dump($this);
        };
    }
}

$object = new Test;
$function = $object->testing();
$function();

    
```

El ejemplo anterior mostrará:

    object(Test)#1 (0) {
    }

When declared in the context of a class, the current class is automatically bound to it, making `$this` available inside of the function's scope. If this automatic binding of the current class is not wanted, then [static anonymous functions](#functions.anonymous-functions.static) may be used instead.

### Static anonymous functions

Anonymous functions may be declared statically. This prevents them from having the current class automatically bound to them. Objects may also not be bound to them at runtime.

Attempting to use `$this` inside a static anonymous function

```php
<?php
class Foo
{
    function __construct()
    {
        $func = static function() {
            var_dump($this);
        };
        $func();
    }
};
new Foo();

      
```

El ejemplo anterior mostrará:

    Fatal error: Uncaught Error: Using $this when not in object context in script:7
    Stack trace:
    #0 script(9): Foo::{closure:Foo::__construct():6}()
    #1 script(12): Foo->__construct()
    #2 {main}
      thrown in script on line 7

Attempting to bind an object to a static anonymous function

```php
<?php
$func = static function() {
    // function body
};
$func = $func->bindTo(new stdClass);
$func();

      
```

El ejemplo anterior mostrará:

    Warning: Cannot bind an instance to a static closure, this will be an error in PHP 9 in script on line 5

    Fatal error: Uncaught Error: Value of type null is not callable in script:6
    Stack trace:
    #0 {main}
      thrown in script on line 6

### Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Closures created from [magic methods](#language.oop5.magic) can accept named parameters. |
| 7.1.0 | Anonymous functions may not close over [superglobals](#language.variables.predefined), `$this`, or any variable with the same name as a parameter. |

### Notas

> [!NOTE]
> It is possible to use `func_num_args`, `func_get_arg`, and `func_get_args` from within a closure.

## Arrow Functions

Arrow functions were introduced in PHP 7.4 as a more concise syntax for [anonymous functions](#functions.anonymous).

Both anonymous functions and arrow functions are implemented using the `Closure` class.

Arrow functions have the basic form `fn (argument_list) => expr`.

Arrow functions support the same features as [anonymous functions](#functions.anonymous), except that using variables from the parent scope is always automatic.

When a variable used in the expression is defined in the parent scope it will be implicitly captured by-value. In the following example, the functions `$fn1` and `$fn2` behave the same way.

Arrow functions capture variables by value automatically

```php
<?php
$y = 1;

$fn1 = fn($x) => $x + $y;
// equivalent to using $y by value:
$fn2 = function ($x) use ($y) {
    return $x + $y;
};

var_export($fn1(3));

     
```

El ejemplo anterior mostrará:

    4

This also works if the arrow functions are nested:

Arrow functions capture variables by value automatically, even when nested

```php
<?php
$z = 1;
$fn = fn($x) => fn($y) => $x * $y + $z;
// Outputs 51
var_export($fn(5)(10));

     
```

Similarly to anonymous functions, the arrow function syntax allows arbitrary function signatures, including parameter and return types, default values, variadics, as well as by-reference passing and returning. All of the following are valid examples of arrow functions:

Examples of arrow functions

```php
<?php
fn(array $x) => $x;
static fn($x): int => $x;
fn($x = 42) => $x;
fn(&$x) => $x;
fn&($x) => $x;
fn($x, ...$rest) => $rest;

     
```

Arrow functions use by-value variable binding. This is roughly equivalent to performing a `use($x)` for every variable `$x` used inside the arrow function. A by-value binding means that it is not possible to modify any values from the outer scope. [Anonymous functions](#functions.anonymous) can be used instead for by-ref bindings.

Values from the outer scope cannot be modified by arrow functions

```php
<?php
$x = 1;
$fn = fn() => $x++; // Has no effect
$fn();
var_export($x);  // Outputs 1

     
```

### Historial de cambios

| Versión | Descripción                       |
|---------|-----------------------------------|
| 7.4.0   | Arrow functions became available. |

### Notas

> [!NOTE]
> It is possible to use `func_num_args`, `func_get_arg`, and `func_get_args` from within an arrow function.

## First class callable syntax

The first class callable syntax is introduced as of PHP 8.1.0, as a way of creating [anonymous functions](#functions.anonymous) from [callable](#language.types.callable). It supersedes existing callable syntax using strings and arrays. The advantage of this syntax is that it is accessible to static analysis, and uses the scope at the point where the callable is acquired.

`CallableExpr(...)` syntax is used to create a `Closure` object from callable. `CallableExpr` accepts any expression that can be directly called in the PHP grammar:

Simple first class callable syntax

```php
<?php
class Foo {
   public function method() {}
   public static function staticmethod() {}
   public function __invoke() {}
}

$obj = new Foo();
$classStr = 'Foo';
$methodStr = 'method';
$staticmethodStr = 'staticmethod';

$f1 = strlen(...);
$f2 = $obj(...);  // invokable object
$f3 = $obj->method(...);
$f4 = $obj->$methodStr(...);
$f5 = Foo::staticmethod(...);
$f6 = $classStr::$staticmethodStr(...);

// traditional callable using string, array
$f7 = 'strlen'(...);
$f8 = [$obj, 'method'](...);
$f9 = [Foo::class, 'staticmethod'](...);

     
```

> [!NOTE]
> The `...` is part of the syntax, and not an omission.

`CallableExpr(...)` has the same semantics as Closure::fromCallable. That is, unlike callable using strings and arrays, `CallableExpr(...)` respects the scope at the point where it is created:

Scope comparison of `CallableExpr(...)` and traditional callable

```php
<?php
class Foo {
    public function getPrivateMethod() {
        return [$this, 'privateMethod'];
    }

    private function privateMethod() {
        echo __METHOD__, "\n";
    }
}

$foo = new Foo;
$privateMethod = $foo->getPrivateMethod();
$privateMethod();
// Fatal error: Call to private method Foo::privateMethod() from global scope
// This is because call is performed outside from Foo and visibility will be checked from this point.

     
```

```php
<?php
class Foo1 {
    public function getPrivateMethod() {
        // Uses the scope where the callable is acquired.
        return $this->privateMethod(...); // identical to Closure::fromCallable([$this, 'privateMethod']);
    }

    private function privateMethod() {
        echo __METHOD__, "\n";
    }
}

$foo1 = new Foo1;
$privateMethod = $foo1->getPrivateMethod();
$privateMethod();  // Foo1::privateMethod

    
```

> [!NOTE]
> Object creation by this syntax (e.g `new Foo(...)`) is not supported, because `new Foo()` syntax is not considered a call.

> [!NOTE]
> The first-class callable syntax cannot be combined with the [nullsafe operator](#language.oop5.basic.nullsafe). Both of the following result in a compile-time error:
>
> <div class="informalexample">
>
> ```
> <?php
> $obj?->method(...);
> $obj?->prop->method(...);
>
>       
> ```
>
> </div>
