---
title: Usar PHP
source_url: https://www.php.net/manual/es/faq.using.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: faq/using.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: faq
translation_status: ready
translation_reviewed: false
translation_revision: 1709768e9
order: 1520
---

## Usar PHP

Esta sección reúne varios errores que puede encontrar al escribir sus scripts PHP.

**Q:** No recuerdo el orden de los parámetros en las funciones PHP, ¿son aleatorios?

**A:** PHP reúne cientos de bibliotecas externas y a veces puede parecer desconcertante. Sin embargo, una regla simple para recordar:

Los parámetros relacionados con las [funciones de arrays](#book.array) están en el orden "*needle, haystack*" mientras que los parámetros de las [funciones que manejan cadenas](#book.strings) son exactamente al revés, "*haystack, needle*".

A partir de PHP 8.0, los [argumentos con nombre](#functions.named-arguments) permiten pasar argumentos por nombre de parámetro, haciendo que el orden de los parámetros sea menos importante.

**Q:** Me gustaría escribir un script PHP genérico que pudiera procesar datos de cualquier formulario. ¿Cómo puedo saber qué variables del método POST están disponibles?

**A:** PHP proporciona varias [ variables predefinidas](#language.variables.predefined), como la superglobal `$_POST`. Puede iterar sobre `$_POST` ya que es un array asociativo de todos los valores enviados por el método POST. Por ejemplo, podemos iterar sobre él simplemente con [`foreach`](#control-structures.foreach), verificar los valores vacíos y mostrarlos.

```php
<?php
$empty = $post = array();
foreach ($_POST as $varname => $varvalue) {
    if (empty($varvalue)) {
        $empty[$varname] = $varvalue;
    } else {
        $post[$varname] = $varvalue;
    }
}

echo '<pre>';
if (empty($empty)) {
    print "Ningún valor POST está vacío, valores posteados:\n";
    var_dump($post);
} else {
    print "Tenemos " . count($empty) . " valores vacíos\n";
    print "Posteados :\n"; var_dump($post);
    print "Vacíos :\n";  var_dump($empty);
    exit;
}
echo '</pre>';
?>

      
```

**Q:** Necesito convertir todas las comillas simples (') en una barra invertida seguida de una comilla simple (\\). ¿Cómo hacerlo con una expresión regular? También me gustaría convertir " en \\ y \\ en \\.

**A:** Si asumimos que es para una base de datos, use el mecanismo de escape proporcionado con la base de datos. Por ejemplo, use la función `mysql_real_escape_string` con MySQL y `pg_escape_string` con PostgreSQL. También hay funciones genéricas como `addslashes` y `stripslashes`, que son más comunes con el antiguo código PHP.

Escapar valores manualmente es propenso a errores y depende del contexto. Es preferible utilizar las API de bases de datos que soportan sentencias preparadas y vinculación de parámetros en lugar de construir consultas concatenando cadenas escapadas.

**Q:** Cuando hago lo siguiente, la salida se muestra en el orden incorrecto:

```php
<?php
function myfunc($argument)
{
    echo $argument + 10;
}
$variable = 10;
echo "myfunc($variable) = " . myfunc($variable);
?>

    
```

¿Qué está pasando?

**A:** Para poder usar el resultado de su función en una expresión (como concatenarlo con una cadena como en este ejemplo), debe devolver el valor con `return`, y no imprimirlo con `echo`.

**Q:** Hey, ¿dónde están mis nuevas líneas?

```php
<pre>
<?php echo "Esta es mi primera línea."; ?>
<?php echo "Esta debería mostrarse debajo de la primera."; ?>
</pre>

      
```

**A:** En PHP, el final de un bloque de código es "?\>" o "?\>\n" (donde \n significa una nueva línea). Entonces, en el ejemplo anterior, las frases se mostrarán en una sola línea, porque PHP omite las nuevas líneas después del final del bloque. Esto significa que debe insertar una nueva línea adicional después de cada bloque de código PHP para que se muestre.

¿Por qué PHP hace esto? Porque al formatear HTML, esto le facilita la vida, ya que no desea esa nueva línea, pero debe crear líneas muy largas o hacer que el código fuente de la página sea ilegible para lograr este efecto.

**Q:** Obtengo el mensaje 'Warning: Cannot send session cookie - headers already sent...' o 'Cannot add header information - headers already sent...'.

**A:** Las funciones `header`, `setcookie`, y las [funciones de sesión](#ref.session) deben agregar encabezados al flujo de salida, pero estos solo pueden enviarse antes que el resto del contenido. No debe haber ninguna salida antes de usar estas funciones, como HTML, por ejemplo. La función `headers_sent` verificará si su script ya ha enviado encabezados. Vea también [las funciones de almacenamiento en búfer de salida](#ref.outcontrol).

**Q:** Necesito acceder a la información en el encabezado de solicitud directamente. ¿Cómo puedo hacerlo?

**A:** La función `getallheaders` lo hará si está ejecutando PHP como un módulo de Apache. El siguiente código le mostrará todos los encabezados de solicitud:

```php
<?php
$headers = getallheaders();
foreach ($headers as $name => $content) {
    echo "headers[$name] = $content<br />\n";
}
?>

      
```

Vea también `apache_lookup_uri`, `apache_response_headers` y `fsockopen`.

**Q:** Cuando intento usar la autenticación con IIS obtengo `'No Input file specified'`.

**A:** El modelo de seguridad de IIS es el culpable. Es un problema común para todos los programas CGI que se ejecutan con IIS. Una alternativa es crear un archivo HTML (no ejecutado por PHP) como página de entrada en el directorio donde se requiere la autenticación. Luego, use una etiqueta META para redirigir a la página PHP, o proporcione un enlace a ella. PHP reconocerá entonces la autenticación correctamente. Esto no debería afectar a otros servidores NT. Para más información, vea: <http://support.microsoft.com/kb/q160422/> y la sección del manual sobre la [autenticación HTTP](#features.http-auth).

**Q:** Windows: No puedo acceder a los archivos compartidos en otra computadora usando IIS.

**A:** Debe modificar el servicio `Ir a Servicios de Internet Information`. Localice su archivo PHP y edite sus propiedades. Vaya a la pestaña `Seguridad del archivo`, `Editar -< Control de acceso anónimo y autenticación`.

Puede resolver este problema desmarcando la casilla `Acceso anónimo` y dejando la casilla `Autenticación integrada de Windows` marcada, o marcando la casilla `Acceso anónimo` y editando el usuario que no debe tener los derechos de acceso.

**Q:** ¿Cómo mezclar XML y PHP? PHP se queja de mis etiquetas \<?xml !

**A:** Para incluir \<?xml en su código PHP, deberá desactivar las etiquetas cortas configurando la directiva PHP [short_open_tags](#ini.short-open-tag) a `0`. No puede cambiar esta directiva con `ini_set`. Ya sea que [ short_open_tags](#ini.short-open-tag) esté activado o desactivado, siempre puede hacer esto: `<?php echo '<?xml'; ?>`. El valor predeterminado para esta directiva es `On`.

**Q:** ¿Dónde puedo encontrar una lista completa de las variables predefinidas que puedo usar en mis scripts PHP?

**A:** Lea la página del manual que trata sobre las [ variables predefinidas](#language.variables.predefined) ya que presenta una lista parcial de las variables predefinidas disponibles en su script. Una lista completa de las variables disponibles (y mucha información) puede verse llamando a la función `phpinfo`. Lea la sección del manual que trata sobre las [variables no provenientes de PHP](#language.variables.external), que describe escenarios comunes para las variables externas, como las provenientes de un formulario HTML, una cookie y la URL.

**Q:** ¿Cómo puedo generar archivos PDF sin usar las bibliotecas no libres PDFLib? Me gustaría una manera gratuita y que no requiera bibliotecas PDF externas.

**A:** Hay algunas alternativas escritas en PHP como [FPDF](http://www.fpdf.org/) y [TCPDF](http://www.tcpdf.org/).

**Q:** Algunas directivas PHP pueden tomar nombres literales, y no solo valores `int`. ¿Cuáles son todas las abreviaturas disponibles?

**A:** Las opciones disponibles son K (para kilobytes) y M (para megabyte) y G (para gigabyte), y no distinguen entre mayúsculas y minúsculas. Cualquier otra sintaxis se supone que representa bytes. `1M` equivale a un megabyte o `1048576` bytes. `1K` equivale a un kilobyte o `1024` bytes. Estas notaciones abreviadas pueden usarse en el archivo `php.ini` y en la función `ini_set`. Tenga en cuenta que el valor numérico se convierte en `int` ; por ejemplo, `0.5M` se interpreta como `0`.

> [!NOTE]
> La notación PHP describe un kilobyte como igual a 1024 bytes, mientras que el estándar IEC lo considera un kibibyte (kibibyte). En resumen: k y K = 1024 bytes.
