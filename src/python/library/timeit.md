---
title: '"timeit" --- Measure execution time of small code snippets'
source_url: https://docs.python.org/es/3
source_path: library/timeit.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4160
---

# "timeit" --- Measure execution time of small code snippets

**Código fuente:** Lib/timeit.py

======================================================================

Este módulo proporciona una forma sencilla de cronometrar pequeños
fragmentos de código Python. Tiene tanto una Interfaz de línea de
comandos como una invocable. Evita una serie de trampas comunes para
medir los tiempos de ejecución. Véase también la introducción de Tim
Peters al capítulo "Algoritmos" en la segunda edición de *Python
Cookbook*, publicado por O'Reilly.

## Ejemplos básicos

En el ejemplo siguiente se muestra cómo se puede utilizar Interfaz de
línea de comandos para comparar tres expresiones diferentes:

   $ python -m timeit "'-'.join(str(n) for n in range(100))"
   10000 loops, best of 5: 30.2 usec per loop
   $ python -m timeit "'-'.join([str(n) for n in range(100)])"
   10000 loops, best of 5: 27.5 usec per loop
   $ python -m timeit "'-'.join(map(str, range(100)))"
   10000 loops, best of 5: 23.2 usec per loop

Esto se puede lograr desde Interfaz de Python con:

   >>> import timeit
   >>> timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
   0.3018611848820001
   >>> timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
   0.2727368790656328
   >>> timeit.timeit('"-".join(map(str, range(100)))', number=10000)
   0.23702679807320237

Un invocable también se puede pasar desde el Interfaz de Python:

   >>> timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000)
   0.19665591977536678

Sin embargo, tenga en cuenta que "timeit()" determinará
automáticamente el número de repeticiones solo cuando se utiliza la
interfaz de línea de comandos.  En la sección Ejemplos puede encontrar
ejemplos más avanzados.

## Interfaz de Python

El módulo define tres funciones de conveniencia y una clase pública:

timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None)

   Cree una instancia de "Timer" con la instrucción dada, el código
   *setup* y la función *timer* y ejecute su método "timeit()" con las
   ejecuciones *number*. El argumento *globals* opcional especifica un
   espacio de nombres en el que se ejecutará el código.

   Distinto en la versión 3.5: El parámetro opcional *globals* fue
   añadido.

timeit.repeat(stmt='pass', setup='pass', timer=<default timer>, repeat=5, number=1000000, globals=None)

   Crea una instancia de "Timer" con la instrucción dada, el código
   *setup* y la función *timer* y ejecuta su método "repeat()" con las
   ejecuciones *repeat* y *number* dadas.  El argumento *globals*
   opcional especifica un espacio de nombres en el que se ejecutará el
   código.

   Distinto en la versión 3.5: El parámetro opcional *globals* fue
   añadido.

   Distinto en la versión 3.7: El valor por defecto para *repeat*
   cambió de 3 a 5.

timeit.default_timer()

   El temporizador por defecto, que es siempre time.perf_counter(),
   retorna segundos como un número de punto flotante. Como
   alternativa, time.perf_counter_ns retorna un número entero de
   nanosegundos.

   Distinto en la versión 3.3: "time.perf_counter()" es ahora el
   temporizador por defecto.

class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>, globals=None)

   Clase para la velocidad de tiempo de ejecución de pequeños
   fragmentos de código.

   El constructor toma una instrucción que se cronometra, una
   instrucción adicional utilizada para la instalación, y una función
   de temporizador.  Ambas instrucciones tienen como valor
   predeterminado "'pass'"; la función del temporizador depende de la
   plataforma (consulte la cadena *doc* del módulo). *stmt* y *setup*
   también pueden contener varias instrucciones separadas por ";" o
   líneas nuevas, siempre y cuando no contengan literales de cadena de
   varias líneas.  La instrucción se ejecutará de forma predeterminada
   dentro del espacio de nombres timeit; este comportamiento se puede
   controlar pasando un espacio de nombres a *globals*.

   Para medir el tiempo de ejecución de la primera instrucción,
   utilice el método "timeit()".  Los métodos "repeat()" y
   "autorange()" son métodos de conveniencia para llamar al método
   "timeit()" varias veces.

   El tiempo de ejecución de *setup* se excluye de la ejecución de
   tiempo total.

   Los parámetros *stmt* y *setup* también pueden tomar objetos a los
   que se puede llamar sin argumentos.  Esto embebe llamadas a ellos
   en una función de temporizador que luego será ejecutada por
   "timeit()".  Tenga en cuenta que la sobrecarga de tiempo es un poco
   mayor en este caso debido a las llamadas de función adicionales.

   Distinto en la versión 3.5: El parámetro opcional *globals* fue
   añadido.

   timeit(number=1000000)

      Registra la duración de *number* ejecuciones de la sentencia
      principal.  Esto ejecuta la sentencia *setup* una vez y, a
      continuación, retorna el tiempo que se tarda en ejecutar la
      sentencia principal varias veces. El temporizador por defecto
      retorna segundos como un número de punto flotante. El argumento
      es el número de veces que se ejecuta el bucle, tomando por
      defecto un millón.  La sentencia principal, la instrucción
      *setup* y la función *timer* que se va a utilizar se pasan al
      constructor.

      Nota:

        De forma predeterminada, "timeit()" desactiva temporalmente
        *garbage collection* durante la medición.  La ventaja de este
        enfoque es que hace que los tiempos independientes sean más
        comparables.  La desventaja es que GC puede ser un componente
        importante del rendimiento de la función que se está midiendo.
        Si es así, GC se puede volver a habilitar como la primera
        instrucción en la cadena *setup*.  Por ejemplo:

           timeit.Timer('for i in range(10): oct(i)', 'gc.enable()').timeit()

   autorange(callback=None)

      Determina automáticamente cuántas veces llamar a "timeit()".

      This is a convenience function that calls "timeit()" repeatedly
      so that the total time >= 0.2 second, returning the eventual
      (number of loops, time taken for that number of loops). It calls
      "timeit()" with increasing numbers from the sequence 1, 2, 5,
      10, 20, 50, ... until the time taken is at least 0.2 seconds.

      Si *callback* se da y no es "None", se llamará después de cada
      prueba con dos argumentos: "callback(number, time_taken)".

      Added in version 3.6.

   repeat(repeat=5, number=1000000)

      Llama a "timeit()" algunas veces.

      Esta es una función de conveniencia que llama a "timeit()"
      repetidamente, retornando una lista de resultados.  El primer
      argumento especifica cuántas veces se debe llamar a "timeit()".
      El segundo argumento especifica el argumento *number* para
      "timeit()".

      Nota:

        Es tentador calcular la media y la desviación estándar del
        vector de resultados e informar de estos.  Sin embargo, esto
        no es muy útil. En un caso típico, el valor más bajo
        proporciona un límite inferior para la rapidez con la que el
        equipo puede ejecutar el fragmento de código especificado;
        valores más altos en el vector de resultado normalmente no son
        causados por la variabilidad en la velocidad de Python, sino
        por otros procesos que interfieren con su precisión de
        sincronización. Así que el "min()" del resultado es
        probablemente el único número que debería estar interesado en.
        Después de eso, usted debe mirar todo el vector y aplicar el
        sentido común en lugar de las estadísticas.

      Distinto en la versión 3.7: El valor por defecto para *repeat*
      cambió de 3 a 5.

   print_exc(file=None)

      Ayudante para imprimir un seguimiento desde el código
      cronometrado.

      Uso típico:

         t = Timer(...)       # outside the try/except
         try:
             t.timeit(...)    # or t.repeat(...)
         except Exception:
             t.print_exc()

      La ventaja sobre el seguimiento estándar es que se mostrarán las
      líneas de origen de la plantilla compilada.  El argumento
      opcional *file* dirige dónde se envía el seguimiento; por
      defecto a "sys.stderr".

## Interfaz de línea de comandos

Cuando se llama como un programa desde la línea de comandos, se
utiliza el siguiente formulario:

   python -m timeit [-n N] [-r N] [-u U] [-s S] [-p] [-v] [-h] [statement ...]

Cuando las siguientes opciones son entendidas:

-n N, --number=N

   cuantas veces para ejecutar '*statement*'

-r N, --repeat=N

   cuantas veces se va a repetir el temporizador (predeterminado 5)

-s S, --setup=S

   instrucción a ser ejecutada una vez inicialmente (por defecto
   "pass")

-p, --process

   mide el tiempo de proceso, no el tiempo total de ejecución,
   utilizando "time.process_time()" en lugar de "time.perf_counter()",
   que es el valor predeterminado

   Added in version 3.3.

-u, --unit=U

   especifica una unidad de tiempo para la salida del temporizador;
   puede seleccionar "nsec", "usec", "msec" o "sec"

   Added in version 3.5.

-v, --verbose

   imprime los resultados de tiempo en bruto; repetir para más dígitos
   de precisión

-h, --help

   imprime un mensaje de uso corto y sale

Se puede dar una instrucción de varias líneas especificando cada línea
como un argumento de instrucción independiente; Las líneas con sangría
son posibles entrecomillando un argumento y utilizando espacios
iniciales.  Múltiples opciones "-s" se tratan de forma similar.

Si no se da "-n", se calcula un número adecuado de bucles intentando
aumentar los números de la secuencia 1, 2, 5, 10, 20, 50, ... hasta
que el tiempo total sea de al menos 0.2 segundos.

Las mediciones de "default_timer()" pueden verse afectadas por otros
programas que se ejecutan en la misma máquina, por lo que lo mejor que
se puede hacer cuando es necesario una medición de tiempo precisa es
repetir la medición un par de veces y utilizar el mejor tiempo.  La
opción "-r" es buena para esto; el valor predeterminado de 5
repeticiones es probablemente suficiente en la mayoría de los casos.
Puede usar "time.process_time()" para medir el tiempo de CPU.

Nota:

  Hay una cierta sobrecarga de línea base asociada con la ejecución de
  una instrucción pass. El código aquí no intenta ocultarlo, pero debe
  ser consciente de ello.  La sobrecarga de línea base se puede medir
  invocando el programa sin argumentos y puede diferir entre versiones
  de Python.

## Ejemplos

Es posible proporcionar una instrucción *setup* que se ejecuta solo
una vez al inicio:

   $ python -m timeit -s "text = 'sample string'; char = 'g'" "char in text"
   5000000 loops, best of 5: 0.0877 usec per loop
   $ python -m timeit -s "text = 'sample string'; char = 'g'" "text.find(char)"
   1000000 loops, best of 5: 0.342 usec per loop

En la salida, hay tres campos. El conteo del bucle, que indica cuántas
veces se ejecutó el cuerpo de la declaración por tiempo de repetición
del bucle. El conteo de repeticiones ("el mejor de 5") el cual indica
cuántas veces se repitió el ciclo de tiempo y, finalmente, el tiempo
promedio que tomó el cuerpo de la declaración dentro de la mejor
repetición del ciclo de tiempo. Es decir, el tiempo que tomó la
repetición más rápida dividido por el número de bucles.

   >>> import timeit
   >>> timeit.timeit('char in text', setup='text = "sample string"; char = "g"')
   0.41440500499993504
   >>> timeit.timeit('text.find(char)', setup='text = "sample string"; char = "g"')
   1.7246671520006203

Se puede hacer lo mismo usando la clase "Timer" y sus métodos:

   >>> import timeit
   >>> t = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')
   >>> t.timeit()
   0.3955516149999312
   >>> t.repeat()
   [0.40183617287970225, 0.37027556854118704, 0.38344867356679524, 0.3712595970846668, 0.37866875250654886]

En los ejemplos siguientes se muestra cómo cronometrar expresiones que
contienen varias líneas. Aquí comparamos el coste de usar "hasattr()"
frente a "try"/"except" para probar los atributos de objeto faltantes
y presentes:

   $ python -m timeit "try:" "  str.__bool__" "except AttributeError:" "  pass"
   20000 loops, best of 5: 15.7 usec per loop
   $ python -m timeit "if hasattr(str, '__bool__'): pass"
   50000 loops, best of 5: 4.26 usec per loop

   $ python -m timeit "try:" "  int.__bool__" "except AttributeError:" "  pass"
   200000 loops, best of 5: 1.43 usec per loop
   $ python -m timeit "if hasattr(int, '__bool__'): pass"
   100000 loops, best of 5: 2.23 usec per loop

   >>> import timeit
   >>> # attribute is missing
   >>> s = """\
   ... try:
   ...     str.__bool__
   ... except AttributeError:
   ...     pass
   ... """
   >>> timeit.timeit(stmt=s, number=100000)
   0.9138244460009446
   >>> s = "if hasattr(str, '__bool__'): pass"
   >>> timeit.timeit(stmt=s, number=100000)
   0.5829014980008651
   >>>
   >>> # attribute is present
   >>> s = """\
   ... try:
   ...     int.__bool__
   ... except AttributeError:
   ...     pass
   ... """
   >>> timeit.timeit(stmt=s, number=100000)
   0.04215312199994514
   >>> s = "if hasattr(int, '__bool__'): pass"
   >>> timeit.timeit(stmt=s, number=100000)
   0.08588060699912603

To give the "timeit" module access to functions you define, you can
pass a *setup* parameter which contains an import statement:

   def test():
       """Stupid test function"""
       L = [i for i in range(100)]

   if __name__ == '__main__':
       import timeit
       print(timeit.timeit("test()", setup="from __main__ import test"))

Otra opción es pasar "globals()" al parámetro *globals*, lo que hará
que el código se ejecute dentro del espacio de nombres global actual.
Esto puede ser más conveniente que especificar individualmente las
importaciones:

   def f(x):
       return x**2
   def g(x):
       return x**4
   def h(x):
       return x**8

   import timeit
   print(timeit.timeit('[func(42) for func in (f,g,h)]', globals=globals()))
