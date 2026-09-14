---
title: Ejemplos
source_url: https://www.php.net/manual/es/errorfunc.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/errorfunc/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: errorfunc
translation_status: ready
translation_revision: fa6e19697
order: 17580
---

## Ejemplos

Abajo podemos ver un ejemplo del uso de las capacidades del manejo de errores de PHP. Definimos una función de gestión de errores que registra la información en un archivo (usado un foramto XML), y envía un e-mail a los desarrolladores en caso de que suceda un error crítico en la lógica.

Usar el manejo de errores en un script

```php
<?php
// haremos nuestro propio manejo de errores
error_reporting(0);

// función de gestión de errores definida por el usuario
function gestorErrores($númerr, $menserr, $nombrearchivo, $númlínea, $vars)
{
    // marca de tiempo para la entrada del error
    $fh = date("Y-m-d H:i:s (T)");

    // definir una matriz asociativa de cadena de error
    // en realidad las únicas entradas que deberíamos
    // considerar son E_WARNING, E_NOTICE, E_USER_ERROR,
    // E_USER_WARNING y E_USER_NOTICE
    $tipoerror = array (
                E_ERROR              => 'Error',
                E_WARNING            => 'Warning',
                E_PARSE              => 'Parsing Error',
                E_NOTICE             => 'Notice',
                E_CORE_ERROR         => 'Core Error',
                E_CORE_WARNING       => 'Core Warning',
                E_COMPILE_ERROR      => 'Compile Error',
                E_COMPILE_WARNING    => 'Compile Warning',
                E_USER_ERROR         => 'User Error',
                E_USER_WARNING       => 'User Warning',
                E_USER_NOTICE        => 'User Notice',
                E_STRICT             => 'Runtime Notice',
                E_RECOVERABLE_ERROR  => 'Catchable Fatal Error'
                );
    // conjunto de errores por el cuál se guardará un seguimiento de una variable
    $errores_usuario = array(E_USER_ERROR, E_USER_WARNING, E_USER_NOTICE);

    $err = "<errorentry>\n";
    $err .= "\t<datetime>" . $fh . "</datetime>\n";
    $err .= "\t<errornum>" . $númerr . "</errornum>\n";
    $err .= "\t<errortype>" . $tipoerror[$númerr] . "</errortype>\n";
    $err .= "\t<errormsg>" . $menserr . "</errormsg>\n";
    $err .= "\t<scriptname>" . $nombrearchivo . "</scriptname>\n";
    $err .= "\t<scriptlinenum>" . $númlínea . "</scriptlinenum>\n";

    if (in_array($númerr, $errores_usuario)) {
        $err .= "\t<vartrace>" . wddx_serialize_value($vars, "Variables") . "</vartrace>\n";
    }
    $err .= "</errorentry>\n\n";

    // para probar
    // echo $err;

    // guardar al registro de errores, y enviarme un e-mail si hay un error crítico de usuario
    error_log($err, 3, "/usr/local/php4/error.log");
    if ($númerr == E_USER_ERROR) {
        mail("phpdev@example.com", "Error Crítico de Usuario", $err);
    }
}

function distancia($vect1, $vect2)
{
    if (!is_array($vect1) || !is_array($vect2)) {
        trigger_error("Parámetros incorrectos, se esperaba una matriz", E_USER_ERROR);
        return NULL;
    }

    if (count($vect1) != count($vect2)) {
        trigger_error("Los vectores necesitan ser del mismo tamaño", E_USER_ERROR);
        return NULL;
    }

    for ($i=0; $i<count($vect1); $i++) {
        $c1 = $vect1[$i]; $c2 = $vect2[$i];
        $d = 0.0;
        if (!is_numeric($c1)) {
            trigger_error("La coordenada $i del vector 1 no es un número, se usará cero",
                            E_USER_WARNING);
            $c1 = 0.0;
        }
        if (!is_numeric($c2)) {
            trigger_error("La coordenada $i del vector 2 no es un número, se usará cero",
                            E_USER_WARNING);
            $c2 = 0.0;
        }
        $d += $c2*$c2 - $c1*$c1;
    }
    return sqrt($d);
}

$gestor_error_antiguo = set_error_handler("gestorErrores");

// constante no definida, genera una advertencia
$t = NO_ESTOY_DEFINIDA;

// definir algunos "vectores"
$a = array(2, 3, "foo");
$b = array(5.5, 4.3, -1.6);
$c = array(1, -3);

// generar un error de usuario
$t1 = distancia($c, $b) . "\n";

// generar otro error de usuario
$t2 = distancia($b, "no soy una matriz") . "\n";

// generar una advertencia
$t3 = distancia($a, $b) . "\n";

?>

    
```
