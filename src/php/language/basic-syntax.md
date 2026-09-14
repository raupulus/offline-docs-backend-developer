---
title: La sintaxis básica
source_url: https://www.php.net/manual/es/language.basic-syntax.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/basic-syntax.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: ee1ce6a0e
order: 1970
---

## La sintaxis básica

## Etiquetas PHP

Cuando PHP procesa un fichero, reconoce las etiquetas de apertura y de cierre, `<?php` y `?>`, para definir los límites de la ejecución del código PHP. El contenido fuera de las etiquetas es ignorado por el analizador PHP, permitiendo a PHP integrarse de manera transparente en diversos tipos de documentos.

Un carácter de espacio (espacio, tabulación, o nueva línea) debe seguir `<?php` para asegurar una separación correcta de los tokens. Omitir este espacio en blanco resultará en un error de sintaxis.

PHP incluye también la etiqueta corta echo `<?=`, que es un atajo para `<?php echo`.

Etiquetas de apertura y cierre PHP

```php
     
1.  <?php echo 'Si se desea integrar código PHP en documentos XHTML o XML, utilice estas etiquetas'; ?>

2.  Se puede utilizar la etiqueta corta para <?= 'escribir este texto' ?>.
    Es equivalente a <?php echo 'escribir este texto' ?>.

3.  <? echo 'este código está entre etiquetas cortas'; ?>
    El siguiente código <?= 'texto' ?> es un atajo para <? echo 'texto' ?>

    
```

Las etiquetas cortas (tercer ejemplo) están disponibles por omisión, pero pueden ser desactivadas a través de la opción [short_open_tag](#ini.short-open-tag) del fichero de configuración `php.ini`, o están desactivadas por omisión si PHP es compilado con la opción `--disable-short-tags`.

> [!NOTE]
> Como las etiquetas cortas pueden ser desactivadas, se recomienda utilizar solo las etiquetas normales (`<?php ?>` y `<?= ?>`) para maximizar la compatibilidad.

Si un fichero termina con código PHP, es preferible no colocar la etiqueta de cierre al final del fichero. Esto permite evitar olvidar un espacio o una nueva línea después de la etiqueta de cierre de PHP, lo cual causaría efectos no deseados ya que PHP comenzará a mostrar la salida, lo cual no es a menudo el caso deseado.

Fichero que contiene solo código PHP

```php
<?php
echo "Hola mundo\n";

// ... más código

echo "Última instrucción\n";

// el script termina aquí, sin la etiqueta de cierre PHP

    
```

## Escape desde HTML

Todo lo que se encuentra fuera de un par de etiquetas de apertura/cierre es ignorado por el analizador PHP, lo que permite tener ficheros PHP mezclando contenidos. Esto permite a PHP estar contenido en documentos HTML, para crear por ejemplo plantillas.

Integrar PHP en HTML

```php
<p>Esto será ignorado por PHP y mostrado en el navegador.</p>
<?php echo 'Mientras que esto será analizado por PHP.'; ?>
<p>Esto también será ignorado por PHP y mostrado en el navegador.</p>

    
```

Esto funciona como se espera porque cuando el intérprete PHP encuentra la etiqueta de cierre ?\>, simplemente comienza a mostrar lo que encuentra (a excepción de la nueva línea que es inmediatamente seguida: ver la [instrucción de separación](#language.basic-syntax.instruction-separation)) hasta que encuentre otra etiqueta de apertura incluso si PHP se encuentra en medio de una instrucción condicional, en cuyo caso, el intérprete determinará la condición a tener en cuenta antes de tomar una decisión sobre lo que debe ser mostrado. Ver el siguiente ejemplo.

Uso de estructuras con condiciones

Escape avanzado usando condiciones

```php
<?php if ($expression == true): ?>
  Esto será mostrado si la expresión es verdadera.
<?php else: ?>
  De lo contrario, esto será mostrado.
<?php endif; ?>

    
```

En este ejemplo, PHP ignorará los bloques donde la condición no se cumpla, incluso si están fuera de las etiquetas de apertura/cierre de PHP. PHP los ignorará según la condición ya que el intérprete PHP pasará los bloques que contienen lo que no se cumple por la condición.

Para mostrar grandes bloques de texto, es más eficiente salir del modo de análisis de PHP en lugar de enviar el texto a través de la función `echo` o `print`.

> [!NOTE]
> Si PHP está integrado en un documento XML o XHTML, la etiqueta PHP estándar `<?php ?>` debe ser utilizada para mantener la conformidad con los estándares.

## Separación de instrucciones

Al igual que en C o en Perl, PHP requiere que las instrucciones sean terminadas por un punto y coma al final de cada instrucción. La etiqueta de cierre de un bloque de código PHP implica automáticamente un punto y coma; por lo tanto, no es necesario utilizar un punto y coma para terminar la última línea de un bloque PHP. La etiqueta de cierre de un bloque incluye el carácter de nueva línea seguido inmediatamente si uno está presente.

Ejemplo que muestra que la etiqueta de cierre incluye la nueva línea que sigue

```php
<?php echo "Algún texto"; ?>
Sin nueva línea
<?= "Pero nueva línea ahora" ?>

    
```

El ejemplo anterior mostrará:

    Algún textoSin nueva línea
    Pero nueva línea ahora

Ejemplos de entrada y salida del analizador PHP

```php
<?php
    echo 'Esto es una prueba\n';
?>

<?php echo 'Esto es una prueba\n' ?>

<?php echo 'Omitimos la última etiqueta de cierre\n';

    
```

> [!NOTE]
> La etiqueta de cierre de un bloque PHP al final de un fichero es opcional, y a veces es útil omitirla cuando se utiliza la función `include` o la función `require`, ya que los espacios no deseados no aparecerán al final de los ficheros, y así, siempre se podrán agregar encabezados a la respuesta más tarde. Esto es útil también si se desea utilizar la visualización del búfer y no se desea ver espacios en blanco añadidos al final de las partes generadas por los ficheros incluidos.

## Comentarios

PHP soporta los comentarios de tipo C, C++ y Shell Unix (también llamado estilo Perl). Por ejemplo :

Comentarios

```php
<?php
    echo 'Esto es una prueba\n'; // Esto es un comentario de una sola línea, estilo c++
    /* Esto es un comentario de
       varias líneas */
    echo 'Esto es otra prueba\n';
    echo 'Y una prueba final\n'; # Esto es un comentario de una sola línea estilo shell
?>

    
```

Los comentarios de una sola línea solo comentan hasta el final de la línea del bloque PHP actual. Esto significa que el código HTML después de `// ... ?>` o después de `# ... ?>` SERÁ mostrado: ?\> terminará el modo PHP y volverá al modo HTML, y `//` o `#` no influirá en ello.

Los comentarios van hasta el final de la línea

```php
<h1>Esto es un ejemplo <?php # echo 'simple';?></h1>
<p>La línea anterior mostrará 'Esto es un ejemplo'.</p>

    
```

Los comentarios estilo 'C' comentan hasta que se encuentre el primer `*/`. Se debe tener cuidado con los comentarios estilo 'C' anidados en grandes bloques cuando se comentan.

```php
<?php
 /*
    echo 'Esto es una prueba'; /* Este comentario causará un problema */
 */
?>

    
```
