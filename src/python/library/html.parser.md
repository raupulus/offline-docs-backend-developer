---
title: '"html.parser" --- Simple HTML and XHTML parser'
source_url: https://docs.python.org/es/3
source_path: library/html.parser.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2830
---

# "html.parser" --- Simple HTML and XHTML parser

**Código fuente:** Lib/html/parser.py

======================================================================

Este módulo define una clase "HTMLParser" que sirve como base para
analizar archivos de texto formateados en HTML (*HyperText Mark-up
Language*) y XHTML.

class html.parser.HTMLParser(*, convert_charrefs=True, scripting=False)

   Cree una instancia de analizador capaz de analizar marcado no
   válido.

   If *convert_charrefs* is true (the default), all character
   references (except the ones in elements like "script" and "style")
   are automatically converted to the corresponding Unicode
   characters.

   If *scripting* is false (the default), the content of the
   "noscript" element is parsed normally; if it's true, it's returned
   as is without being parsed.

   Una instancia de "HTMLParser" se alimenta de datos HTML y llama a
   métodos de manejo cuando se encuentran etiquetas de inicio,
   etiquetas finales, texto, comentarios y otros elementos de marcado.
   El usuario debe subclasificar "HTMLParser" y anular sus métodos
   para implementar el comportamiento deseado.

   Este analizador no verifica que las etiquetas finales coincidan con
   las etiquetas iniciales ni llame al manejador de etiquetas finales
   para los elementos que se cierran implícitamente al cerrar un
   elemento externo.

   Distinto en la versión 3.4: argumento de palabra clave
   *convert_charrefs* agregado.

   Distinto en la versión 3.5: El valor predeterminado para el
   argumento *convert_charrefs* ahora es "True".

   Distinto en la versión 3.14.1: Added the *scripting* parameter.

## Aplicación ejemplo de un analizador sintáctico (*parser*) de HTML

As a basic example, below is a simple HTML parser that uses the
"HTMLParser" class to print out start tags, end tags, and data as they
are encountered:

   from html.parser import HTMLParser

   class MyHTMLParser(HTMLParser):
       def handle_starttag(self, tag, attrs):
           print("Encountered a start tag:", tag)

       def handle_endtag(self, tag):
           print("Encountered an end tag :", tag)

       def handle_data(self, data):
           print("Encountered some data  :", data)

   parser = MyHTMLParser()
   parser.feed('<html><head><title>Test</title></head>'
               '<body><h1>Parse me!</h1></body></html>')

La salida será entonces:

   Encountered a start tag: html
   Encountered a start tag: head
   Encountered a start tag: title
   Encountered some data  : Test
   Encountered an end tag : title
   Encountered an end tag : head
   Encountered a start tag: body
   Encountered a start tag: h1
   Encountered some data  : Parse me!
   Encountered an end tag : h1
   Encountered an end tag : body
   Encountered an end tag : html

## Métodos "HTMLParser"

instancias de "HTMLParser" tienen los siguientes métodos:

HTMLParser.feed(data)

   Alimente un poco de texto al analizador. Se procesa en la medida en
   que consta de elementos completos; los datos incompletos se
   almacenan en el búfer hasta que se introducen más datos o se llama
   a "close()". *data* debe ser "str".

HTMLParser.close()

   Fuerce el procesamiento de todos los datos almacenados como si
   fueran seguidos por una marca de fin de archivo. Este método puede
   ser redefinido por una clase derivada para definir un procesamiento
   adicional al final de la entrada, pero la versión redefinida
   siempre debe llamar a "HTMLParser" método de clase base "close()".

HTMLParser.reset()

   Restablecer la instancia. Pierde todos los datos no procesados.
   Esto se llama implícitamente en el momento de la instanciación.

HTMLParser.getpos()

   Retorna el número de línea actual y el desplazamiento.

HTMLParser.get_starttag_text()

   Retorna el texto de la etiqueta de inicio abierta más
   recientemente. Normalmente, esto no debería ser necesario para el
   procesamiento estructurado, pero puede ser útil para tratar con
   HTML "como implementado" o para volver a generar entradas con
   cambios mínimos (se puede preservar el espacio en blanco entre los
   atributos, etc.).

Los siguientes métodos se invocan cuando se encuentran datos o
elementos de marcado y deben anularse en una subclase. Las
implementaciones de la clase base no hacen nada (excepto
"handle_startendtag()"):

HTMLParser.handle_starttag(tag, attrs)

   This method is called to handle the start tag of an element (e.g.
   "<div id="main">").

   The *tag* argument is the name of the tag converted to lower case.
   The *attrs* argument is a list of "(name, value)" pairs containing
   the attributes found inside the tag's "<>" brackets.  The *name*
   will be translated to lower case, and quotes in the *value* have
   been removed, and character and entity references have been
   replaced.  For empty attributes, *value* is "None".

   Por ejemplo, para la etiqueta "<A HREF="https://www.cwi.nl/">",
   este método se llamaría como "handle_starttag('a', [('href', 'https
   : //www.cwi.nl/ ')])".

   Todas las referencias de entidad de "html.entities" se reemplazan
   en los valores de los atributos.

HTMLParser.handle_endtag(tag)

   Este método se llama para manejar la etiqueta final de un elemento
   (por ejemplo, "</div>")

   El argumento *tag* es el nombre de la etiqueta convertida a
   minúsculas.

HTMLParser.handle_startendtag(tag, attrs)

   Similar a "handle_starttag()", pero llamado cuando el analizador
   encuentra una etiqueta vacía de estilo XHTML ("<img .../>"). Este
   método puede ser anulado por subclases que requieren esta
   información léxica particular; la implementación predeterminada
   simplemente llama "handle_starttag()" y "handle_endtag()".

HTMLParser.handle_data(data)

   This method is called to process arbitrary data (e.g. text nodes
   and the content of elements like "script" and "style").

HTMLParser.handle_entityref(name)

   This method is called to process a named character reference of the
   form "&name;" (e.g. "&gt;"), where *name* is a general entity
   reference (e.g. "'gt'"). This method is only called if
   *convert_charrefs* is false.

HTMLParser.handle_charref(name)

   This method is called to process decimal and hexadecimal numeric
   character references of the form "&#*NNN*;" and "&#x*NNN*;".  For
   example, the decimal equivalent for "&gt;" is "&#62;", whereas the
   hexadecimal is "&#x3E;"; in this case the method will receive
   "'62'" or "'x3E'". This method is only called if *convert_charrefs*
   is false.

HTMLParser.handle_comment(data)

   Este método se llama cuando se encuentra un comentario (por
   ejemplo, "<!--comment-->").

   Por ejemplo, el comentario "<! - comment ->" hará que se llame a
   este método con el argumento "'comment'".

   El contenido de los comentarios condicionales de Internet Explorer
   (*condcoms*) también se enviará a este método, por lo tanto, para
   "<!--[if IE 9]>IE9-specific content<![endif]-->", este método
   recibirá "'[if IE 9]>IE9-specific content<![endif]'".

HTMLParser.handle_decl(decl)

   Este método se llama para manejar una declaración de tipo de
   documento HTML (por ejemplo, "<!DOCTYPE html>").

   El parámetro *decl* será todo el contenido de la declaración dentro
   del "<!...>" *markup* (por ejemplo, "'DOCTYPE html'").

HTMLParser.handle_pi(data)

   Método llamado cuando se encuentra una instrucción de
   procesamiento. El parámetro *data* contendrá toda la instrucción de
   procesamiento. Por ejemplo, para la instrucción de procesamiento
   "<?proc color='red'>", este método se llamaría como
   "handle_pi("proc color='red'")". Está destinado a ser anulado por
   una clase derivada; La implementación de la clase base no hace
   nada.

   Nota:

     La clase "HTMLParser" utiliza las reglas sintácticas SGML para
     procesar instrucciones. Una instrucción de procesamiento XHTML
     que use el "'?'" final hará que se incluya el "'?'" en *data*.

HTMLParser.unknown_decl(data)

   Se llama a este método cuando el analizador lee una declaración no
   reconocida.

   El parámetro *data* será el contenido completo de la declaración
   dentro del marcado "<! [...]>". A veces es útil ser reemplazado por
   una clase derivada. La implementación de la clase base no hace
   nada.

## Ejemplos

The following class implements a parser that will be used to
illustrate more examples:

   from html.parser import HTMLParser
   from html.entities import name2codepoint

   class MyHTMLParser(HTMLParser):
       def handle_starttag(self, tag, attrs):
           print("Start tag:", tag)
           for attr in attrs:
               print("     attr:", attr)

       def handle_endtag(self, tag):
           print("End tag  :", tag)

       def handle_data(self, data):
           print("Data     :", data)

       def handle_comment(self, data):
           print("Comment  :", data)

       def handle_entityref(self, name):
           c = chr(name2codepoint[name])
           print("Named ent:", c)

       def handle_charref(self, name):
           if name.startswith('x'):
               c = chr(int(name[1:], 16))
           else:
               c = chr(int(name))
           print("Num ent  :", c)

       def handle_decl(self, data):
           print("Decl     :", data)

   parser = MyHTMLParser()

Parsing a doctype:

   >>> parser.feed('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
   ...             '"http://www.w3.org/TR/html4/strict.dtd">')
   Decl     : DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"

Parsing an element with a few attributes and a title:

   >>> parser.feed('<img src="python-logo.png" alt="The Python logo">')
   Start tag: img
        attr: ('src', 'python-logo.png')
        attr: ('alt', 'The Python logo')
   >>>
   >>> parser.feed('<h1>Python</h1>')
   Start tag: h1
   Data     : Python
   End tag  : h1

The content of elements like "script" and "style" is returned as is,
without further parsing:

   >>> parser.feed('<style type="text/css">#python { color: green }</style>')
   Start tag: style
        attr: ('type', 'text/css')
   Data     : #python { color: green }
   End tag  : style

   >>> parser.feed('<script type="text/javascript">'
   ...             'alert("<strong>hello! &#9786;</strong>");</script>')
   Start tag: script
        attr: ('type', 'text/javascript')
   Data     : alert("<strong>hello! &#9786;</strong>");
   End tag  : script

Attribute names are converted to lowercase, quotes from attribute
values removed, and "None" is returned as *value* for empty attributes
(such as "checked"):

   >>> parser.feed("<input TYPE='checkbox' checked required='' disabled=disabled>")
   Start tag: input
        attr: ('type', 'checkbox')
        attr: ('checked', None)
        attr: ('required', '')
        attr: ('disabled', 'disabled')

Parsing comments:

   >>> parser.feed('<!--a comment-->'
   ...             '<!--[if IE 9]>IE-specific content<![endif]-->')
   Comment  : a comment
   Comment  : [if IE 9]>IE-specific content<![endif]

Parsing named and numeric character references and converting them to
the correct char (note: these 3 references are all equivalent to
"'>'"):

   >>> parser = MyHTMLParser()
   >>> parser.feed('&gt;&#62;&#x3E;')
   Data     : >>>

   >>> parser = MyHTMLParser(convert_charrefs=False)
   >>> parser.feed('&gt;&#62;&#x3E;')
   Named ent: >
   Num ent  : >
   Num ent  : >

Feeding incomplete chunks to "feed()" works, but "handle_data()" might
be called more than once if *convert_charrefs* is false:

   >>> for chunk in ['<sp', 'an>buff', 'ered', ' text</s', 'pan>']:
   ...     parser.feed(chunk)
   ...
   Start tag: span
   Data     : buff
   Data     : ered
   Data     :  text
   End tag  : span

Parsing invalid HTML (e.g. unquoted attributes) also works:

   >>> parser.feed('<p><a class=link href=#main>tag soup</p ></a>')
   Start tag: p
   Start tag: a
        attr: ('class', 'link')
        attr: ('href', '#main')
   Data     : tag soup
   End tag  : p
   End tag  : a
