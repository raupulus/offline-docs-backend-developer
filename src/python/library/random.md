---
title: '"random" --- Generate pseudo-random numbers'
source_url: https://docs.python.org/es/3
source_path: library/random.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3630
---

# "random" --- Generate pseudo-random numbers

**Código fuente:** Lib/random.py

======================================================================

Este módulo implementa generadores de números pseudoaleatorios para
varias distribuciones.

Para los enteros, existe una selección uniforme dentro de un rango.
Para las secuencias, existe una selección uniforme de un elemento
aleatorio, una función para generar una permutación aleatoria de una
lista *in-situ* y una función para el muestreo aleatorio sin
reemplazo.

Para números reales, existen funciones para calcular distribuciones
uniformes, normales (Gaussianas), log-normales, exponenciales
negativas, gamma y beta. Para generar distribuciones angulares está
disponible la distribución de von Mises.

Almost all module functions depend on the basic function "random()",
which generates a random float uniformly in the half-open range "0.0
<= X < 1.0". Python uses the Mersenne Twister as the core generator.
It produces 53-bit precision floats and has a period of 2**19937-1.
The underlying implementation in C is both fast and threadsafe.  The
Mersenne Twister is one of the most extensively tested random number
generators in existence.  However, being completely deterministic, it
is not suitable for all purposes, and is completely unsuitable for
cryptographic purposes.

Las funciones proporcionadas por este módulo en realidad son métodos
enlazados a instancias ocultas a la clase "random.Random". Puedes
instanciar tus propias instancias de "Random" para obtener generadores
que no compartan estado.

Class "Random" can also be subclassed if you want to use a different
basic generator of your own devising: see the documentation on that
class for more details.

The "random" module also provides the "SystemRandom" class which uses
the system function "os.urandom()" to generate random numbers from
sources provided by the operating system.

Advertencia:

  Los generadores pseudoaleatorios de este módulo no deben ser
  utilizados con fines de seguridad. Para usos de seguridad o
  criptográficos, consulta el módulo "secrets".

Ver también:

  M. Matsumoto and T. Nishimura, "Mersenne Twister: A
  623-dimensionally equidistributed uniform pseudorandom number
  generator", ACM Transactions on Modeling and Computer Simulation
  Vol. 8, No. 1, January pp.3--30 1998.

  Complementary-Multiply-with-Carry recipe for a compatible
  alternative random number generator with a long period and
  comparatively simple update operations.

Nota:

  The global random number generator and instances of "Random" are
  thread-safe. However, in the free-threaded build, concurrent calls
  to the global generator or to the same instance of "Random" may
  encounter contention and poor performance. Consider using separate
  instances of "Random" per thread instead.

## Funciones de contabilidad

random.seed(a=None, version=2)

   Inicializa el generador de números aleatorios.

   Si *a* es omitida o "None", se utilizará la hora actual del
   sistema. Si las fuentes de aleatoriedad vienen del sistema
   operativo, éstas se usarán en vez de la hora del sistema (ver la
   función "os.urandom()" para detalles sobre su disponibilidad).

   If *a* is an int, its absolute value is used directly.

   Con la versión 2 (la versión por defecto), un objeto "str",
   "bytes", o "bytearray" se convierte en "int" y se usarán todos sus
   bits.

   Con la versión 1 (proporcionada para reproducir secuencias
   aleatorias desde versiones anteriores de Python), el algoritmo para
   "str" y "bytes" genera un rango de semillas más estrecho.

   Distinto en la versión 3.2: El esquema que usa todos los bits en
   una semilla de tipo cadena, se ha movido a la versión 2.

   Distinto en la versión 3.11: The *seed* must be one of the
   following types: "None", "int", "float", "str", "bytes", or
   "bytearray".

random.getstate()

   Retorna un objeto capturando el estado interno del generador. Este
   objeto puede pasarse a "setstate()" para restaurar su estado.

random.setstate(state)

   El *state* debería haberse obtenido de una llamada previa a
   "getstate()", y "setstate()" reestablece el estado interno del
   generador al que tenia cuando se llamó a la función "getstate()".

## Funciones para los bytes

random.randbytes(n)

   Genera *n* bytes aleatorios.

   Este método no debe utilizarse para generar tokens de seguridad.
   Utilice "secrets.token_bytes()" en su lugar.

   Added in version 3.9.

## Funciones para enteros

random.randrange(stop)
random.randrange(start, stop[, step])

   Return a randomly selected element from "range(start, stop, step)".

   This is roughly equivalent to "choice(range(start, stop, step))"
   but supports arbitrarily large ranges and is optimized for common
   cases.

   The positional argument pattern matches the "range()" function.

   Keyword arguments should not be used because they can be
   interpreted in unexpected ways. For example "randrange(start=100)"
   is interpreted as "randrange(0, 100, 1)".

   Distinto en la versión 3.2: "randrange()" es más sofisticado
   produciendo valores igualmente distribuidos. Anteriormente
   utilizaba un estilo como "int(random()*n)" el cual puede producir
   distribuciones ligeramente desiguales.

   Distinto en la versión 3.12: Automatic conversion of non-integer
   types is no longer supported. Calls such as "randrange(10.0)" and
   "randrange(Fraction(10, 1))" now raise a "TypeError".

random.randint(a, b)

   Retorna un entero aleatorio *N* tal que "a <= N <= b". Alias de
   "randrange(a, b+1)".

random.getrandbits(k)

   Returns a non-negative Python integer with *k* random bits. This
   method is supplied with the Mersenne Twister generator and some
   other generators may also provide it as an optional part of the
   API. When available, "getrandbits()" enables "randrange()" to
   handle arbitrarily large ranges.

   Distinto en la versión 3.9: Este método ahora acepta cero para *k*.

## Funciones para secuencias

random.choice(seq)

   Retorna un elemento aleatorio de una secuencia *seq* no vacía. Si
   *seq* está vacía, lanza "IndexError".

random.choices(population, weights=None, *, cum_weights=None, k=1)

   Retorna una lista de elementos de tamaño *k* elegidos de la
   *population* con reemplazo. Si la *population* está vacía, lanza
   "IndexError".

   Si se especifica una secuencia *weights*, las selecciones se
   realizan de acuerdo con las ponderaciones relativas.
   Alternativamente, si se da una secuencia *cum_weights*, las
   selecciones se harán según los pesos cumulativos (posiblemente se
   calculen usando "itertools.accumulate()"). Por ejemplo, los pesos
   relativos "[10, 5, 30, 5]" son equivalentes a los pesos cumulativos
   "[10, 15, 45, 50]". Internamente, los pesos relativos se convierten
   en pesos cumulativos antes de hacer selecciones, por lo cual suplir
   los pesos cumulativos ahorra trabajo.

   Si ni *weights* ni *cum_weights* están especificadas, las
   selecciones se realizan con la misma probabilidad. Si se
   proporciona una secuencia de ponderaciones, debe tener la misma
   longitud que la secuencia *population*. Es un "TypeError"
   especificar ambas *weights* y *cum_weights*.

   Los *weights* o los *cum_weights* pueden utilizar cualquier tipo
   numérico que interactúe con los valores "float" retornados por
   "random()" (eso incluye enteros, flotantes y fracciones pero
   excluye decimales). Se asume que los pesos son no negativos y
   finitos.  Se lanza un "ValueError" si todos los pesos son cero.

   For a given seed, the "choices()" function with equal weighting
   typically produces a different sequence than repeated calls to
   "choice()".  The algorithm used by "choices()" uses floating-point
   arithmetic for internal consistency and speed.  The algorithm used
   by "choice()" defaults to integer arithmetic with repeated
   selections to avoid small biases from round-off error.

   Added in version 3.6.

   Distinto en la versión 3.9: Genera un "ValueError" si todos los
   pesos son cero.

random.shuffle(x)

   Mezcla la secuencia *x* in-situ.

   Para mezclar una secuencia inmutable y retornar una nueva lista
   mezclada, utilice "muestra(x, k=len(x))" en su lugar.

   Tenga en cuenta que incluso para pequeños "len(x)", el número total
   de permutaciones de *x* puede crecer rápidamente más que el periodo
   de muchos generadores de números aleatorios. Esto implica que la
   mayoría de las permutaciones de una secuencia larga nunca se pueden
   generar. Por ejemplo, una secuencia de longitud 2080 es la más
   grande que cabe dentro del período del generador de números
   aleatorios de Mersenne Twister.

   Distinto en la versión 3.11: Removed the optional parameter
   *random*.

random.sample(population, k, *, counts=None)

   Return a *k* length list of unique elements chosen from the
   population sequence.  Used for random sampling without replacement.

   Retorna una nueva lista que contiene elementos de la población sin
   modificar la población original. La lista resultante está en orden
   de selección de forma que todos los subsectores también son
   muestras aleatorias válidas. Esto permite que los ganadores de la
   rifa (la muestra) se dividan en primer premio y ganadores del
   segundo lugar (los subsectores).

   Los miembros de la población no tienen porqué ser *hashable* o
   únicos. Si la población incluye repeticiones, entonces cada
   ocurrencia es una posible selección en la muestra.

   Los elementos repetidos pueden especificarse de uno en uno o con el
   parámetro opcional *counts*, que es una palabra clave.  Por
   ejemplo, "sample(['red', 'blue'], counts=[4, 2], k=5)" es
   equivalente a "sample(['red', 'red', 'red', 'red', 'blue', 'blue'],
   k=5)".

   Para escoger una muestra de un rango de enteros, use un objeto
   "range()" como argumento. Esto es especialmente rápido y eficiente
   en espacio para el muestreo de poblaciones grandes:
   "sample(range(10000000), k=60)".

   Si el tamaño de la muestra es mayor que el tamaño de la población,
   se lanzará un "ValueError".

   Distinto en la versión 3.9: Se añadió el parámetro *counts*.

   Distinto en la versión 3.11: La población debe ser una secuencia.
   La conversión automática de sets a listas ya no es compatible.

## Discrete distributions

The following function generates a discrete distribution.

random.binomialvariate(n=1, p=0.5)

   Binomial distribution. Return the number of successes for *n*
   independent trials with the probability of success in each trial
   being *p*:

   Mathematically equivalent to:

      sum(random() < p for i in range(n))

   The number of trials *n* should be a non-negative integer. The
   probability of success *p* should be between "0.0 <= p <= 1.0". The
   result is an integer in the range "0 <= X <= n".

   Added in version 3.12.

## Distribuciones para los nombres reales

Las siguientes funciones generan distribuciones específicas para
números reales. Los parámetros de la función reciben el nombre de las
variables correspondientes en la ecuación de distribución, tal y como
se utilizan en la práctica matemática común.; la mayoría de estas
ecuaciones se pueden encontrar en cualquier texto estadístico.

random.random()

   Return the next random floating-point number in the range "0.0 <= X
   < 1.0"

random.uniform(a, b)

   Return a random floating-point number *N* such that "a <= N <= b"
   for "a <= b" and "b <= N <= a" for "b < a".

   The end-point value "b" may or may not be included in the range
   depending on floating-point rounding in the expression "a + (b-a) *
   random()".

random.triangular(low, high, mode)

   Return a random floating-point number *N* such that "low <= N <=
   high" and with the specified *mode* between those bounds.  The
   *low* and *high* bounds default to zero and one.  The *mode*
   argument defaults to the midpoint between the bounds, giving a
   symmetric distribution.

random.betavariate(alpha, beta)

   Distribución beta. Las condiciones de los parámetros son "alpha >
   0" y "beta > 0". Retorna valores dentro del rango entre 0 y 1.

random.expovariate(lambd=1.0)

   Distribución exponencial. *lambd* es 1.0 dividido entre la media
   deseada. Debe ser distinto a cero (El parámetro debería llamarse
   "lambda" pero esa es una palabra reservada en Python). Retorna
   valores dentro del rango de 0 a infinito positivo si *lambd* es
   positivo, y de infinito negativo a 0 si *lambd* es negativo.

   Distinto en la versión 3.12: Added the default value for "lambd".

random.gammavariate(alpha, beta)

   Gamma distribution.  (*Not* the gamma function!)  The shape and
   scale parameters, *alpha* and *beta*, must have positive values.
   (Calling conventions vary and some sources define 'beta' as the
   inverse of the scale).

   La función de distribución de la probabilidad es:

                x ** (alpha - 1) * math.exp(-x / beta)
      pdf(x) =  --------------------------------------
                  math.gamma(alpha) * beta ** alpha

random.gauss(mu=0.0, sigma=1.0)

   Normal distribution, also called the Gaussian distribution. *mu* is
   the mean, and *sigma* is the standard deviation.  This is slightly
   faster than the "normalvariate()" function defined below.

   Nota sobre el multithreading: Cuando dos hilos llaman a esta
   función simultáneamente, es posible que reciban el mismo valor de
   retorno.  Esto se puede evitar de tres maneras. 1) Hacer que cada
   hilo utilice una instancia diferente del generador de números
   aleatorios. 2) Poner bloqueos alrededor de todas las llamadas. 3)
   Utilizar la función "normalvariate()", más lenta pero segura para
   los hilos, en su lugar.

   Distinto en la versión 3.11: *mu* y *sigma* ahora tienen argumentos
   predeterminados.

random.lognormvariate(mu, sigma)

   Logaritmo de la distribución normal. Si se usa un logaritmo natural
   de esta distribución, se obtendrá una distribución normal con media
   *mu* y desviación estándar *sigma*. *mu* puede tener cualquier
   valor, y *sigma* debe ser mayor que cero.

random.normalvariate(mu=0.0, sigma=1.0)

   Distribución normal. *mu* es la media y *sigma* es la desviación
   estándar.

   Distinto en la versión 3.11: *mu* y *sigma* ahora tienen argumentos
   predeterminados.

random.vonmisesvariate(mu, kappa)

   *mu* es el ángulo medio, expresado en radiantes entre 0 y 2**pi*, y
   *kappa* es el parámetro de concentración, que debe ser mayor o
   igual a cero. Si *kappa* es igual a cero, esta distribución se
   reduce a un ángulo aleatorio uniforme sobre el rango de 0 a 2**pi*.

random.paretovariate(alpha)

   Distribución de Pareto. *alpha* es el parámetro de forma.

random.weibullvariate(alpha, beta)

   Distribución de Weibull. *alpha* es el parámetro de escala y *beta*
   es el parámetro de forma.

## Generador alternativo

class random.Random([seed])

   Class that implements the default pseudo-random number generator
   used by the "random" module.

   Distinto en la versión 3.11: Formerly the *seed* could be any
   hashable object.  Now it is limited to: "None", "int", "float",
   "str", "bytes", or "bytearray".

   Subclasses of "Random" should override the following methods if
   they wish to make use of a different basic generator:

   seed(a=None, version=2)

      Override this method in subclasses to customise the "seed()"
      behaviour of "Random" instances.

   getstate()

      Override this method in subclasses to customise the "getstate()"
      behaviour of "Random" instances.

   setstate(state)

      Override this method in subclasses to customise the "setstate()"
      behaviour of "Random" instances.

   random()

      Override this method in subclasses to customise the "random()"
      behaviour of "Random" instances.

   Optionally, a custom generator subclass can also supply the
   following method:

   getrandbits(k)

      Override this method in subclasses to customise the
      "getrandbits()" behaviour of "Random" instances.

   randbytes(n)

      Override this method in subclasses to customise the
      "randbytes()" behaviour of "Random" instances.

class random.SystemRandom([seed])

   Clase que utiliza la función "os.urandom()" para generar números
   aleatorios a partir de fuentes proporcionadas por el sistema
   operativo. No está disponible en todos los sistemas. No se basa en
   el estado del software y las secuencias no son reproducibles. En
   consecuencia, el método "seed()" no tiene efecto y es ignorado. Los
   métodos "getstate()" y "setstate()" lanzan "NotImplementedError" si
   se les llama.

## Notas sobre la Reproducibilidad

Sometimes it is useful to be able to reproduce the sequences given by
a pseudo-random number generator.  By reusing a seed value, the same
sequence should be reproducible from run to run as long as multiple
threads are not running.

Muchos de los algoritmos y de las funciones de generación de semillas
del módulo aleatorio pueden cambiar entre versiones de Python, pero se
garantiza que dos aspectos no cambien:

* Si se añade un nuevo método de generación de semilla, se ofrecerá un
  generador de semilla retrocompatible.

* El método generador "random()" continuará produciendo la misma
  secuencia cuando se le da la misma semilla al generador de semilla
  compatible.

## Ejemplos

Ejemplos básicos:

   >>> random()                          # Random float:  0.0 <= x < 1.0
   0.37444887175646646

   >>> uniform(2.5, 10.0)                # Random float:  2.5 <= x <= 10.0
   3.1800146073117523

   >>> expovariate(1 / 5)                # Interval between arrivals averaging 5 seconds
   5.148957571865031

   >>> randrange(10)                     # Integer from 0 to 9 inclusive
   7

   >>> randrange(0, 101, 2)              # Even integer from 0 to 100 inclusive
   26

   >>> choice(['win', 'lose', 'draw'])   # Single random element from a sequence
   'draw'

   >>> deck = 'ace two three four'.split()
   >>> shuffle(deck)                     # Shuffle a list
   >>> deck
   ['four', 'two', 'ace', 'three']

   >>> sample([10, 20, 30, 40, 50], k=4) # Four samples without replacement
   [40, 10, 50, 30]

Simulaciones:

   >>> # Six roulette wheel spins (weighted sampling with replacement)
   >>> choices(['red', 'black', 'green'], [18, 18, 2], k=6)
   ['red', 'green', 'black', 'black', 'red', 'black']

   >>> # Deal 20 cards without replacement from a deck
   >>> # of 52 playing cards, and determine the proportion of cards
   >>> # with a ten-value:  ten, jack, queen, or king.
   >>> deal = sample(['tens', 'low cards'], counts=[16, 36], k=20)
   >>> deal.count('tens') / 20
   0.15

   >>> # Estimate the probability of getting 5 or more heads from 7 spins
   >>> # of a biased coin that settles on heads 60% of the time.
   >>> sum(binomialvariate(n=7, p=0.6) >= 5 for i in range(10_000)) / 10_000
   0.4169

   >>> # Probability of the median of 5 samples being in middle two quartiles
   >>> def trial():
   ...     return 2_500 <= sorted(choices(range(10_000), k=5))[2] < 7_500
   ...
   >>> sum(trial() for i in range(10_000)) / 10_000
   0.7958

Ejemplo de statistical bootstrapping utilizando el remuestreo con
reemplazo para estimar un intervalo de confianza para la media de una
muestra:

   # https://www.thoughtco.com/example-of-bootstrapping-3126155
   from statistics import fmean as mean
   from random import choices

   data = [41, 50, 29, 37, 81, 30, 73, 63, 20, 35, 68, 22, 60, 31, 95]
   means = sorted(mean(choices(data, k=len(data))) for i in range(100))
   print(f'The sample mean of {mean(data):.1f} has a 90% confidence '
         f'interval from {means[5]:.1f} to {means[94]:.1f}')

Ejemplo de un test de permutación en remuestreo (en) para determinar
la significación estadística o p-valor de una diferencia observada
entre los efectos de un fármaco y un placebo:

   # Example from "Statistics is Easy" by Dennis Shasha and Manda Wilson
   from statistics import fmean as mean
   from random import shuffle

   drug = [54, 73, 53, 70, 73, 68, 52, 65, 65]
   placebo = [54, 51, 58, 44, 55, 52, 42, 47, 58, 46]
   observed_diff = mean(drug) - mean(placebo)

   n = 10_000
   count = 0
   combined = drug + placebo
   for i in range(n):
       shuffle(combined)
       new_diff = mean(combined[:len(drug)]) - mean(combined[len(drug):])
       count += (new_diff >= observed_diff)

   print(f'{n} label reshufflings produced only {count} instances with a difference')
   print(f'at least as extreme as the observed difference of {observed_diff:.1f}.')
   print(f'The one-sided p-value of {count / n:.4f} leads us to reject the null')
   print(f'hypothesis that there is no difference between the drug and the placebo.')

Simulación de tiempos de llegada y entrega de servicios para una cola
de múltiples servidores:

   from heapq import heapify, heapreplace
   from random import expovariate, gauss
   from statistics import mean, quantiles

   average_arrival_interval = 5.6
   average_service_time = 15.0
   stdev_service_time = 3.5
   num_servers = 3

   waits = []
   arrival_time = 0.0
   servers = [0.0] * num_servers  # time when each server becomes available
   heapify(servers)
   for i in range(1_000_000):
       arrival_time += expovariate(1.0 / average_arrival_interval)
       next_server_available = servers[0]
       wait = max(0.0, next_server_available - arrival_time)
       waits.append(wait)
       service_duration = max(0.0, gauss(average_service_time, stdev_service_time))
       service_completed = arrival_time + wait + service_duration
       heapreplace(servers, service_completed)

   print(f'Mean wait: {mean(waits):.1f}   Max wait: {max(waits):.1f}')
   print('Quartiles:', [round(q, 1) for q in quantiles(waits)])

Ver también:

  *Statistics for Hackers* un video tutorial de Jake Vanderplas sobre
  análisis estadístico usando sólo algunos conceptos fundamentales
  incluyendo simulación, muestreo, baraja y validación cruzada.

  Economics Simulation a simulation of a marketplace by Peter Norvig
  that shows effective use of many of the tools and distributions
  provided by this module (gauss, uniform, sample, betavariate,
  choice, triangular, and randrange).

  A Concrete Introduction to Probability (using Python) a tutorial by
  Peter Norvig covering the basics of probability theory, how to write
  simulations, and how to perform data analysis using Python.

## Recetas

Estas recetas muestran cómo hacer de manera eficiente selecciones
aleatorias de los iteradores combinatorios en el módulo "itertools":

   import random

   def random_product(*iterables, repeat=1):
       "Random selection from itertools.product(*iterables, repeat=repeat)"
       pools = tuple(map(tuple, iterables)) * repeat
       return tuple(map(random.choice, pools))

   def random_permutation(iterable, r=None):
       "Random selection from itertools.permutations(iterable, r)"
       pool = tuple(iterable)
       r = len(pool) if r is None else r
       return tuple(random.sample(pool, r))

   def random_combination(iterable, r):
       "Random selection from itertools.combinations(iterable, r)"
       pool = tuple(iterable)
       n = len(pool)
       indices = sorted(random.sample(range(n), r))
       return tuple(pool[i] for i in indices)

   def random_combination_with_replacement(iterable, r):
       "Choose r elements with replacement.  Order the result to match the iterable."
       # Result will be in set(itertools.combinations_with_replacement(iterable, r)).
       pool = tuple(iterable)
       n = len(pool)
       indices = sorted(random.choices(range(n), k=r))
       return tuple(pool[i] for i in indices)

   def random_derangement(iterable):
       "Choose a permutation where no element stays in its original position."
       seq = tuple(iterable)
       if len(seq) < 2:
           if not seq:
               return ()
           raise IndexError('No derangments to choose from')
       perm = list(range(len(seq)))
       start = tuple(perm)
       while True:
           random.shuffle(perm)
           if all(p != q for p, q in zip(start, perm)):
               return tuple([seq[i] for i in perm])

La función "random()" por defecto devuelve múltiplos de 2⁻⁵³ en el
rango *0.0 ≤ x < 1.0*.  Todos estos números están espaciados
uniformemente y son representables exactamente como flotantes de
Python.  Sin embargo, muchos otros flotadores representables en ese
intervalo no son selecciones posibles.  Por ejemplo,
"0.05954861408025609" no es un múltiplo entero de 2⁻⁵³.

La siguiente receta adopta un enfoque diferente.  Todos los flotantes
en el intervalo son selecciones posibles.  La mantisa proviene de una
distribución uniforme de enteros en el rango *2⁵² ≤ mantisa < 2⁵³*.
El exponente proviene de una distribución geométrica en la que los
exponentes menores de *-53* ocurren con la mitad de frecuencia que el
siguiente exponente mayor.

   from random import Random
   from math import ldexp

   class FullRandom(Random):

       def random(self):
           mantissa = 0x10_0000_0000_0000 | self.getrandbits(52)
           exponent = -53
           x = 0
           while not x:
               x = self.getrandbits(32)
               exponent += x.bit_length() - 32
           return ldexp(mantissa, exponent)

Todas las distribuciones de valor real de la clase utilizarán el nuevo
método:

   >>> fr = FullRandom()
   >>> fr.random()
   0.05954861408025609
   >>> fr.expovariate(0.25)
   8.87925541791544

La receta es conceptualmente equivalente a un algoritmo que elige
entre todos los múltiplos de 2⁻¹⁰⁷⁴ en el rango *0,0 ≤ x < 1,0*.
Todos esos números son uniformes, pero la mayoría tienen que ser
redondeados al flotante de Python representable más cercano.  (El
valor 2⁻¹⁰⁷⁴ es el menor flotante positivo no normalizado y es igual a
"math.ulp(0.0)".)

Ver también:

  Generating Pseudo-random Floating-Point Values un artículo de Allen
  B. Downey en el que se describen formas de generar flotantes más
  refinados que los generados normalmente por "random()".

## Command-line usage

Added in version 3.13.

The "random" module can be executed from the command line.

   python -m random [-h] [-c CHOICE [CHOICE ...] | -i N | -f N] [input ...]

The following options are accepted:

-h, --help

   Show the help message and exit.

-c CHOICE [CHOICE ...]
--choice CHOICE [CHOICE ...]

   Print a random choice, using "choice()".

-i <N>
--integer <N>

   Print a random integer between 1 and N inclusive, using
   "randint()".

-f <N>
--float <N>

   Print a random floating-point number between 0 and N inclusive,
   using "uniform()".

If no options are given, the output depends on the input:

* String or multiple: same as "--choice".

* Integer: same as "--integer".

* Float: same as "--float".

## Command-line example

Here are some examples of the "random" command-line interface:

   $ # Choose one at random
   $ python -m random egg bacon sausage spam "Lobster Thermidor aux crevettes with a Mornay sauce"
   Lobster Thermidor aux crevettes with a Mornay sauce

   $ # Random integer
   $ python -m random 6
   6

   $ # Random floating-point number
   $ python -m random 1.8
   1.7080016272295635

   $ # With explicit arguments
   $ python  -m random --choice egg bacon sausage spam "Lobster Thermidor aux crevettes with a Mornay sauce"
   egg

   $ python -m random --integer 6
   3

   $ python -m random --float 1.8
   1.5666339105010318

   $ python -m random --integer 6
   5

   $ python -m random --float 6
   3.1942323316565915
