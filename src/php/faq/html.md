---
title: PHP y HTML
source_url: https://www.php.net/manual/es/faq.html.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: faq/html.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: faq
translation_status: ready
translation_revision: 9e6c3416c
order: 1460
---

## PHP y HTML

PHP y HTML interactúan mucho: PHP puede generar HTML, y HTML puede pasar información a PHP. Antes de leer esta sección, es importante que aprenda cómo obtener [ variables desde fuentes externas](#language.variables.external). La página del manual sobre este tema incluye muchos ejemplos también.

**Q:** ¿Qué codificación/decodificación es necesaria al pasar un valor a través de un formulario/URL?

**A:** Existen varios escenarios en los que la codificación es importante. Asumiendo que se tiene un valor `$datos` de tipo `string`, el cual contiene la cadena que desea pasar sin codificar, existen los escenarios relevantes:

- Interpretación de HTML. Para especificar una cadena aleatoria, *es necesario* incluirla entre comillas dobles, y aplicar `htmlspecialchars` sobre el valor completo.

- URL: Un URL consta de varias partes. Si los datos han de ser interpretados como un elemento, *es necesario* codificarlo con `urlencode`.

Un elemento oculto de un formulario HTML

```php
<?php
    echo '<input type="hidden" value="' . htmlspecialchars($datos) . '" />'."\n";
?>

      
```

> [!NOTE]
> No es correcto aplicar `urlencode` sobre `$datos`, ya que es responsabilidad de los navegadores codificar los datos. Todos los navegadores populares lo realizan correctamente. Observe que esto ocurrirá independientemente del método (es decir, GET o POST). Aunque solo se observará esto en el caso de una petición GET, ya que las peticiones POST normalmente están ocultas.

Datos a editar por el usuario

```php
<?php
    echo "<textarea name='misdatos'>\n";
    echo htmlspecialchars($datos)."\n";
    echo "</textarea>";
?>

      
```

> [!NOTE]
> Los datos son mostrados en el navegador como se esperaba, ya que el navegador interpretará los símbolos HTML escapados.
>
> Durante el envío, ya sea mediante GET o POST, los datos serán codificados por el navegador para su transferencia, y serán decodificados directamente por PHP. Por lo tanto, no será necesario realizar ninguna codificación/decodificación, todo es manejado automáticamente.

En un URL

```php
<?php
    echo '<a href="' . htmlspecialchars("/siguientepagina.php?etapa=23&datos=" .
        urlencode($datos)) . '">'."\n";
?>

      
```

> [!NOTE]
> De hecho, se está imitando una petición GET de HTML, por lo que no es necesario aplicar `urlencode` manualmente a los datos.

> [!NOTE]
> Es necesario usar `htmlspecialchars` sobre el URL completo, ya que el URL se da como un valor de un atributo HTML. En este caso, el navegador primero reemplazará los caracteres HTML especiales por los caracteres correctos del valor, y luego pasará el URL. PHP entenderá el URL correctamente, ya que ya se utilizó `urlencode` sobre los datos.
>
> Se observará que el caracter `&` en el URL es reemplazado por `&amp;`. Aunque la mayoría de navegadores entenderán el carácter si se olvida esto, no siempre es posible que ocurra. Así que, incluso si un URL no es dinámico, *es necesario* usar `htmlspecialchars` sobre el URL.

**Q:** Estoy intentando usar una etiqueta \<input type="image"\>, pero las variables `$foo.x` y `$foo.y` no están disponibles. `$_GET['foo.x']` tampoco existe. ¿Dónde están?

**A:** Cuando se envía un formulario, es posible usar una imagen en lugar del botón de envío estándar con una etiqueta como esta:

```php
<input type="image" src="imagen.gif" name="foo" />

     
```

Cuando un usuario pulsa sobre la imagen, el formulario al que pertenece será transmitido al servidor con dos variables adicionales: `foo.x` y `foo.y`.

Dado que `foo.x` y `foo.y` habrían representado nombres de variable inválidos en PHP, éstas son convertidas automáticamente a `foo_x` y `foo_y`. Es decir, los puntos son reemplazados con caracteres de subrayado. Por lo tanto, es posible acceder a estas variables como cualquier otra descrita en la sección sobre la recuperación de [variables desde fuentes externas](#language.variables.external). Por ejemplo, `$_GET['foo_x']`.

> [!NOTE]
> Los espacios en nombres de variables de petición son convertidos a caracteres de subrayado.

**Q:** ¿Cómo creo arrays en un \<form\> de HTML?

**A:** Para hacer que el resultado de \<form\> sea enviado como un [array](#language.types.array) a un script de PHP, se deben nombrar los elementos \<input\>, \<select\> o \<textarea\> de esta forma:

```php
<input name="MiArray[]" />
<input name="MiArray[]" />
<input name="MiArray[]" />
<input name="MiArray[]" />

     
```

Observe los corchetes después del nombre de la variable; ellos son los que la convierten en un array. Es posible agrupar los elementos en diferentes arrays asignando el mismo nombre a elementos diferentes:

```php
<input name="MiArray[]" />
<input name="MiArray[]" />
<input name="MiOtroArray[]" />
<input name="MiOtroArray[]" />

     
```

Esto produce dos array, MiArray y MiOtroArray, que son enviados al script PHP. También es posible asignar claves específicas a los arrays:

```php
<input name="OtroArray[]" />
<input name="OtroArray[]" />
<input name="OtroArray[email]" />
<input name="OtroArray[telefono]" />

     
```

El array OtroArray ahora tendrá las claves 0, 1, email y telefono.

> [!NOTE]
> La especificación de claves de arrays es opcional en HTML. Si no se especifican las claves, el array será rellenado en el orden en que aparecen los elementos en el formulario. Nuestro primer ejemplo contendrá las claves 0, 1, 2 y 3.

Véase también [Funciones de arrays](#ref.array) y [Variables desde fuentes externas](#language.variables.external).

**Q:** ¿Cómo obtengo todos los resultados de una etiqueta de selección múltiple en HTML?

**A:** La etiqueta de selección múltiple en una construcción HTML permite a los usuarios elegir varios elementos de una lista. Estos elementos son pasados entonces al gestor de la acción del formulario. El problema es que todos son pasados con el mismo nombre de control. Es decir,

```php
<select name="var" multiple="yes">

     
```

Cada opción elegida llegará al gestor de la acción como:

          var=opcion1
          var=opcion2
          var=opcion3
         

Cada opción sobrescribirá el contenido de la variable `$var` anterior. La solución es usar la característica "array desde un elemento de formulario" de PHP. Debería usarse la siguiente forma:

```php
<select name="var[]" multiple="yes">

     
```

Esto le indica a PHP que debe tratar `$var` como un array y que cada asignación de un valor a var\[\] añade un elemento al array. El primer elemento se convierte en `$var[0]`, el siguiente en `$var[1]`, etc. La función `count` puede usarse para determinar cuántas opciones fueron seleccionadas, y la función `sort` puede usarse para ordenar el array de opciones si fuera necesario.

Observe que si se está usando JavaScript, los caracteres `[]` en el nombre del elemento podrían causar problemas al intentar referirse al elemento por su nombre. Use el ID numérico del elemento del formulario en su lugar, o encierre el nombre de la variable entre comillas simples y úselo como índice del array de elementos, por ejemplo:

          variable = document.forms[0].elements['var[]'];
         

**Q:** ¿Cómo puedo pasar una variable de Javascript a PHP?

**A:** Ya que Javascript es una tecnología (usualmente) del lado del cliente, y PHP es (usualmente) una tecnología del lado del servidor, y dado que HTTP es un protocolo "sin estados", los dos lenguajes no pueden compartir variables directamente.

Sin embargo, es posible pasar variables entre los dos. Una forma de hacerlo es generar código Javascript con PHP, y hacer que el navegador se refresque a sí mismo, volviendo a pasar variables específicas al script de PHP. El ejemplo de abajo muestra precisamente cómo hacer esto; permite que el código de PHP capture el alto y el ancho de la pantalla, algo que normalmente sólo es posible en el lado del cliente.

Generación de Javascript con PHP

```php
<?php
if (isset($_GET['ancho']) AND isset($_GET['alto'])) {
  // imprimir las variables de geometría
  echo "El ancho de la pantalla es: ". $_GET['ancho'] ."<br />\n";
  echo "El alto de la pantalla es: ". $_GET['alto'] ."<br />\n";
} else {
  // pasar las variables de geometría
  // (preservar la cadena de consulta original
  //   -- las variables post deberán ser manejadas de otra forma)

  echo "<script language='javascript'>\n";
  echo "  location.href=\"{$_SERVER['SCRIPT_NAME']}?{$_SERVER['QUERY_STRING']}"
            . "&ancho=\" + screen.width + \"&alto=\" + screen.height;\n";
  echo "</script>\n";
  exit();
}
?>

      
```
