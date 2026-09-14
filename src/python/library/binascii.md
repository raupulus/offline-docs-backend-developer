---
title: '"binascii" --- Convert between binary and ASCII'
source_url: https://docs.python.org/es/3
source_path: library/binascii.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1850
---

# "binascii" --- Convert between binary and ASCII

======================================================================

The "binascii" module contains a number of methods to convert between
binary and various ASCII-encoded binary representations. Normally, you
will not use these functions directly but use wrapper modules like
"base64" instead. The "binascii" module contains low-level functions
written in C for greater speed that are used by the higher-level
modules.

Nota:

  Las funciones "a2b_*" aceptan cadenas Unicode que contienen solo
  caracteres ASCII. Otras funciones solo aceptan *objetos tipo
  binarios* (como "bytes", "bytearray" y otros objetos que admiten el
  protocolo de búfer).

  Distinto en la versión 3.3: Las cadenas unicode con sólo caracteres
  ASCII son ahora aceptadas por las funciones "a2b_*".

The "binascii" module defines the following functions:

binascii.a2b_uu(string)

   Convierte una sola línea de datos uuencoded de nuevo a binarios y
   retorna los datos binarios. Las líneas normalmente contienen 45
   bytes (binarios), excepto por la última línea. Los datos de línea
   pueden ir seguidos de espacios en blanco.

binascii.b2a_uu(data, *, backtick=False)

   Convierte datos binarios a una línea de caracteres ASCII, el valor
   retornado es la línea convertida, incluido un carácter de nueva
   línea. La longitud de *data* debe ser como máximo 45. Si *backtick*
   es verdadero, los ceros se representan mediante "'`'" en lugar de
   espacios.

   Distinto en la versión 3.7: Se ha añadido el parámetro *backtick*.

binascii.a2b_base64(string, /, *, strict_mode=False)

   Convierte un bloque de datos en base64 de nuevo a binario y retorna
   los datos binarios. Se puede pasar más de una línea a la vez.

   Si *strict_mode* es verdadero, solo se convertirán los datos en
   base64 válidos. Los datos en base64 no válidos lanzarán
   "binascii.Error".

   base64 válido:

   * De acuerdo a **RFC 3548**.

   * Contiene solo caracteres del alfabeto base64.

   * No contiene exceso de datos después del relleno (incluye el
     exceso de relleno, nuevas líneas, etc.).

   * No empieza con un relleno.

   Distinto en la versión 3.11: Se ha añadido el parámetro
   *strick_mode*.

binascii.b2a_base64(data, *, newline=True)

   Convierte datos binarios en una línea de caracteres ASCII en
   codificación base64. El valor retornado es la línea convertida,
   incluido un carácter de nueva línea si *newline* es verdadero.  La
   salida de esta función se ajusta a **RFC 3548**.

   Distinto en la versión 3.6: Se ha añadido el parámetro *newline*.

binascii.a2b_qp(data, header=False)

   Convierte un bloque de datos imprimibles entre comillas a binario y
   retorna los datos binarios. Se puede pasar más de una línea a la
   vez. Si el argumento opcional *header* está presente y es
   verdadero, los guiones bajos se decodificarán como espacios.

binascii.b2a_qp(data, quotetabs=False, istext=True, header=False)

   Convierte datos binarios en una(s) línea(s) de caracteres ASCII en
   codificación imprimible entre comillas. El valor de retorno son las
   líneas convertidas. Si el argumento opcional *quotetabs* está
   presente y es verdadero, se codificarán todas los tabs y espacios.
   Si el argumento opcional *istext* está presente y es verdadero, las
   nuevas líneas no se codifican, pero se codificarán los espacios en
   blanco finales. Si el argumento opcional *header* está presente y
   es verdadero, los espacios se codificarán como guiones bajos por:
   rfc: *1522*. Si el argumento opcional *header* está presente y es
   falso, los caracteres de nueva línea también se codificarán; de lo
   contrario, la conversión de salto de línea podría dañar el flujo de
   datos binarios.

binascii.crc_hqx(data, value)

   Calcula un valor CRC de 16 bits de *data*, comenzando con *value*
   como el CRC inicial, y retorna el resultado. Utiliza el polinomio
   CRC-CCITT *x*^16 + *x*^12 + *x*^5 + 1, a menudo representado como
   0x1021. Este CRC se utiliza en el formato binhex4.

binascii.crc32(data[, value])

   Calcula CRC-32, la suma de comprobación de 32 bits de *data* que no
   tiene signo, comenzando con un CRC inicial de *value*. El CRC
   inicial predeterminado es cero. El algoritmo es consistente con la
   suma de verificación del archivo ZIP. Dado que el algoritmo está
   diseñado para usarse como un algoritmo de suma de verificación, no
   es adecuado para usarlo como algoritmo hash general. Úselo de la
   siguiente manera:

      print(binascii.crc32(b"hello world"))
      # Or, in two pieces:
      crc = binascii.crc32(b"hello")
      crc = binascii.crc32(b" world", crc)
      print('crc32 = {:#010x}'.format(crc))

   Distinto en la versión 3.0: El resultado siempre es sin signo.

binascii.b2a_hex(data[, sep[, bytes_per_sep=1]])
binascii.hexlify(data[, sep[, bytes_per_sep=1]])

   Retorna la representación hexadecimal del binario *data*. Cada byte
   de *data* se convierte en la representación hexadecimal de 2
   dígitos correspondiente. Por lo tanto, el objeto de bytes retornado
   es el doble de largo que la longitud de *data*.

   Una funcionalidad similar (pero que retorna una cadena de texto)
   también es convenientemente accesible usando el método
   "bytes.hex()".

   Si se especifica *sep*, debe ser un solo carácter *str* o un objeto
   de bytes. Se insertará en la salida después de cada *bytes_per_sep*
   bytes de entrada . La ubicación del separador se cuenta desde el
   extremo derecho de la salida de forma predeterminada; si desea
   contar desde el izquierdo, proporcione un valor negativo
   *bytes_per_sep*.

   >>> import binascii
   >>> binascii.b2a_hex(b'\xb9\x01\xef')
   b'b901ef'
   >>> binascii.hexlify(b'\xb9\x01\xef', '-')
   b'b9-01-ef'
   >>> binascii.b2a_hex(b'\xb9\x01\xef', b'_', 2)
   b'b9_01ef'
   >>> binascii.b2a_hex(b'\xb9\x01\xef', b' ', -2)
   b'b901 ef'

   Distinto en la versión 3.8: Se agregaron los parámetros *sep* y
   *bytes_per_sep*.

binascii.a2b_hex(hexstr)
binascii.unhexlify(hexstr)

   Retorna los datos binarios representados por la cadena hexadecimal
   *hexstr*.  Esta función es la inversa de "b2a_hex()". *hexstr* debe
   contener un número par de dígitos hexadecimales (que pueden ser
   mayúsculas o minúsculas), de lo contrario se produce una excepción
   "Error".

   Similar functionality (but more liberal towards whitespace) is also
   accessible using the "bytes.fromhex()" class method.

exception binascii.Error

   Excepción provocada por errores. Estos suelen ser errores de
   programación.

exception binascii.Incomplete

   Excepción provocada por datos incompletos. Por lo general, estos no
   son errores de programación, pero se pueden controlar leyendo un
   poco más de datos e intentándolo de nuevo.

Ver también:

  Módulo "base64"
     Soporte para compatibilidad con RFC de codificación de estilo
     base64 en base 16, 32, 64 y 85.

  Módulo "quopri"
     Soporte para codificación imprimible entre comillas utilizada en
     mensajes de correo electrónico MIME.
