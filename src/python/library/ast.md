---
title: '"ast" --- Abstract syntax trees'
source_url: https://docs.python.org/es/3
source_path: library/ast.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1560
---

# "ast" --- Abstract syntax trees

**Código fuente:** Lib/ast.py

======================================================================

The "ast" module helps Python applications to process trees of the
Python abstract syntax grammar.  The abstract syntax itself might
change with each Python release; this module helps to find out
programmatically what the current grammar looks like.

Se puede generar un árbol de sintaxis abstracta pasando
"ast.PyCF_ONLY_AST" como un indicador de la función incorporada
"compile()", o usando el ayudante "parse()" provisto en este módulo.
El resultado será un árbol de objetos cuyas clases todas heredan de
"ast.AST". Se puede compilar un árbol de sintaxis abstracta en un
objeto de código Python utilizando la función incorporada "compile()".

## Abstract grammar

La gramática abstracta se define actualmente de la siguiente manera:

   -- ASDL's 4 builtin types are:
   -- identifier, int, string, constant

   module Python
   {
       mod = Module(stmt* body, type_ignore* type_ignores)
           | Interactive(stmt* body)
           | Expression(expr body)
           | FunctionType(expr* argtypes, expr returns)

       stmt = FunctionDef(identifier name, arguments args,
                          stmt* body, expr* decorator_list, expr? returns,
                          string? type_comment, type_param* type_params)
             | AsyncFunctionDef(identifier name, arguments args,
                                stmt* body, expr* decorator_list, expr? returns,
                                string? type_comment, type_param* type_params)

             | ClassDef(identifier name,
                expr* bases,
                keyword* keywords,
                stmt* body,
                expr* decorator_list,
                type_param* type_params)
             | Return(expr? value)

             | Delete(expr* targets)
             | Assign(expr* targets, expr value, string? type_comment)
             | TypeAlias(expr name, type_param* type_params, expr value)
             | AugAssign(expr target, operator op, expr value)
             -- 'simple' indicates that we annotate simple name without parens
             | AnnAssign(expr target, expr annotation, expr? value, int simple)

             -- use 'orelse' because else is a keyword in target languages
             | For(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment)
             | AsyncFor(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment)
             | While(expr test, stmt* body, stmt* orelse)
             | If(expr test, stmt* body, stmt* orelse)
             | With(withitem* items, stmt* body, string? type_comment)
             | AsyncWith(withitem* items, stmt* body, string? type_comment)

             | Match(expr subject, match_case* cases)

             | Raise(expr? exc, expr? cause)
             | Try(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody)
             | TryStar(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody)
             | Assert(expr test, expr? msg)

             | Import(alias* names)
             | ImportFrom(identifier? module, alias* names, int? level)

             | Global(identifier* names)
             | Nonlocal(identifier* names)
             | Expr(expr value)
             | Pass | Break | Continue

             -- col_offset is the byte offset in the utf8 string the parser uses
             attributes (int lineno, int col_offset, int? end_lineno, int? end_col_offset)

             -- BoolOp() can use left & right?
       expr = BoolOp(boolop op, expr* values)
            | NamedExpr(expr target, expr value)
            | BinOp(expr left, operator op, expr right)
            | UnaryOp(unaryop op, expr operand)
            | Lambda(arguments args, expr body)
            | IfExp(expr test, expr body, expr orelse)
            | Dict(expr?* keys, expr* values)
            | Set(expr* elts)
            | ListComp(expr elt, comprehension* generators)
            | SetComp(expr elt, comprehension* generators)
            | DictComp(expr key, expr value, comprehension* generators)
            | GeneratorExp(expr elt, comprehension* generators)
            -- the grammar constrains where yield expressions can occur
            | Await(expr value)
            | Yield(expr? value)
            | YieldFrom(expr value)
            -- need sequences for compare to distinguish between
            -- x < 4 < 3 and (x < 4) < 3
            | Compare(expr left, cmpop* ops, expr* comparators)
            | Call(expr func, expr* args, keyword* keywords)
            | FormattedValue(expr value, int conversion, expr? format_spec)
            | Interpolation(expr value, constant str, int conversion, expr? format_spec)
            | JoinedStr(expr* values)
            | TemplateStr(expr* values)
            | Constant(constant value, string? kind)

            -- the following expression can appear in assignment context
            | Attribute(expr value, identifier attr, expr_context ctx)
            | Subscript(expr value, expr slice, expr_context ctx)
            | Starred(expr value, expr_context ctx)
            | Name(identifier id, expr_context ctx)
            | List(expr* elts, expr_context ctx)
            | Tuple(expr* elts, expr_context ctx)

            -- can appear only in Subscript
            | Slice(expr? lower, expr? upper, expr? step)

             -- col_offset is the byte offset in the utf8 string the parser uses
             attributes (int lineno, int col_offset, int? end_lineno, int? end_col_offset)

       expr_context = Load | Store | Del

       boolop = And | Or

       operator = Add | Sub | Mult | MatMult | Div | Mod | Pow | LShift
                    | RShift | BitOr | BitXor | BitAnd | FloorDiv

       unaryop = Invert | Not | UAdd | USub

       cmpop = Eq | NotEq | Lt | LtE | Gt | GtE | Is | IsNot | In | NotIn

       comprehension = (expr target, expr iter, expr* ifs, int is_async)

       excepthandler = ExceptHandler(expr? type, identifier? name, stmt* body)
                       attributes (int lineno, int col_offset, int? end_lineno, int? end_col_offset)

       arguments = (arg* posonlyargs, arg* args, arg? vararg, arg* kwonlyargs,
                    expr?* kw_defaults, arg? kwarg, expr* defaults)

       arg = (identifier arg, expr? annotation, string? type_comment)
              attributes (int lineno, int col_offset, int? end_lineno, int? end_col_offset)

       -- keyword arguments supplied to call (NULL identifier for **kwargs)
       keyword = (identifier? arg, expr value)
                  attributes (int lineno, int col_offset, int? end_lineno, int? end_col_offset)

       -- import name with optional 'as' alias.
       alias = (identifier name, identifier? asname)
                attributes (int lineno, int col_offset, int? end_lineno, int? end_col_offset)

       withitem = (expr context_expr, expr? optional_vars)

       match_case = (pattern pattern, expr? guard, stmt* body)

       pattern = MatchValue(expr value)
               | MatchSingleton(constant value)
               | MatchSequence(pattern* patterns)
               | MatchMapping(expr* keys, pattern* patterns, identifier? rest)
               | MatchClass(expr cls, pattern* patterns, identifier* kwd_attrs, pattern* kwd_patterns)

               | MatchStar(identifier? name)
               -- The optional "rest" MatchMapping parameter handles capturing extra mapping keys

               | MatchAs(pattern? pattern, identifier? name)
               | MatchOr(pattern* patterns)

                attributes (int lineno, int col_offset, int end_lineno, int end_col_offset)

       type_ignore = TypeIgnore(int lineno, string tag)

       type_param = TypeVar(identifier name, expr? bound, expr? default_value)
                  | ParamSpec(identifier name, expr? default_value)
                  | TypeVarTuple(identifier name, expr? default_value)
                  attributes (int lineno, int col_offset, int end_lineno, int end_col_offset)
   }

## Clases nodo

class ast.AST

   This is the base of all AST node classes.  The actual node classes
   are derived from the "Parser/Python.asdl" file, which is reproduced
   above.  They are defined in the "_ast" C module and re-exported in
   "ast".

   Hay una clase definida para cada símbolo del lado izquierdo en la
   gramática abstracta (por ejemplo, "ast.stmt" o "ast.expr"). Además,
   hay una clase definida para cada constructor en el lado derecho;
   estas clases heredan de las clases para los árboles del lado
   izquierdo. Por ejemplo, "ast.BinOp" hereda de "ast.expr". Para las
   reglas de producción con alternativas (también conocidas como
   "sumas"), la clase del lado izquierdo es abstracta: solo se crean
   instancias de nodos de constructor específicos.

   _fields

      Each concrete class has an attribute "_fields" which gives the
      names of all child nodes.

      Cada instancia de una clase concreta tiene un atributo para cada
      nodo secundario, del tipo definido en la gramática. Por ejemplo,
      las instancias "ast.BinOp" tienen un atributo "left" de tipo
      "ast.expr".

      Si estos atributos están marcados como opcionales en la
      gramática (usando un signo de interrogación), el valor podría
      ser "None". Si los atributos pueden tener cero o más valores
      (marcados con un asterisco), los valores se representan como
      listas de Python. Todos los atributos posibles deben estar
      presentes y tener valores válidos al compilar un AST con
      "compile()".

   _field_types

      The "_field_types" attribute on each concrete class is a
      dictionary mapping field names (as also listed in "_fields") to
      their types.

         >>> ast.TypeVar._field_types
         {'name': <class 'str'>, 'bound': ast.expr | None, 'default_value': ast.expr | None}

      Added in version 3.13.

   lineno
   col_offset
   end_lineno
   end_col_offset

      Las instancias de las subclases "ast.expr" y "ast.stmt" tienen
      atributos "lineno", "col_offset", "lineno", y "col_offset".
      "lineno" y "end_lineno" son los números de la primera y última
      línea del intervalo de texto de origen (1 indexado, por lo que
      la primera línea es la línea 1), y "col_offset" y
      "end_col_offset" son las correspondientes compensaciones de
      bytes UTF-8 del primer y último token que generó el nodo. El
      desplazamiento UTF-8 se registra porque el analizador utiliza
      UTF-8 internamente.

      Tenga en cuenta que el compilador no requiere las posiciones
      finales y, por lo tanto, son opcionales. El desplazamiento final
      es *después* del último símbolo, por ejemplo, uno puede obtener
      el segmento fuente de un nodo de expresión de una línea usando
      "source_line[node.col_offset: node.end_col_offset]".

   El constructor de una clase "ast.T" analiza sus argumentos de la
   siguiente manera:

   * Si hay argumentos posicionales, debe haber tantos como elementos
     en "T._fields"; serán asignados como atributos de estos nombres.

   * Si hay argumentos de palabras clave, establecerán los atributos
     de los mismos nombres a los valores dados.

   Por ejemplo, para crear y completar un nodo "ast.UnaryOp", puede
   usar

      node = ast.UnaryOp(ast.USub(), ast.Constant(5, lineno=0, col_offset=0),
                         lineno=0, col_offset=0)

   If a field that is optional in the grammar is omitted from the
   constructor, it defaults to "None". If a list field is omitted, it
   defaults to the empty list. If a field of type "ast.expr_context"
   is omitted, it defaults to "Load()". If any other field is omitted,
   a "DeprecationWarning" is raised and the AST node will not have
   this field. In Python 3.15, this condition will raise an error.

Distinto en la versión 3.8: La clase "ast.Constant" ahora se usa para
todas las constantes.

Distinto en la versión 3.9: Los índices simples se representan por su
valor, los segmentos extendidos se representan como tuplas.

Distinto en la versión 3.13: AST node constructors were changed to
provide sensible defaults for omitted fields: optional fields now
default to "None", list fields default to an empty list, and fields of
type "ast.expr_context" default to "Load()". Previously, omitted
attributes would not exist on constructed nodes (accessing them raised
"AttributeError").

Distinto en la versión 3.14: The "__repr__()" output of "AST" nodes
includes the values of the node fields.

Deprecated since version 3.8, removed in version 3.14: Previous
versions of Python provided the AST classes "ast.Num", "ast.Str",
"ast.Bytes", "ast.NameConstant" and "ast.Ellipsis", which were
deprecated in Python 3.8. These classes were removed in Python 3.14,
and their functionality has been replaced with "ast.Constant".

Obsoleto desde la versión 3.9: Old classes "ast.Index" and
"ast.ExtSlice" are still available, but they will be removed in future
Python releases. In the meantime, instantiating them will return an
instance of a different class.

Deprecated since version 3.13, will be removed in version 3.15:
Previous versions of Python allowed the creation of AST nodes that
were missing required fields. Similarly, AST node constructors allowed
arbitrary keyword arguments that were set as attributes of the AST
node, even if they did not match any of the fields of the AST node.
This behavior is deprecated and will be removed in Python 3.15.

Nota:

  Las descripciones de las clases de nodo específicas mostradas aquí
  fueron adaptadas inicialmente del fantástico proyecto Green Tree
  Snakes y todos sus contribuidores.

### Nodos raíz

class ast.Module(body, type_ignores)

   Un módulo de Python, como con archivo-entrada. Tipo de nodo
   generado por "ast.parse()" en el modo por defecto ""exec""
   *mode*.*mode*.

   "body" is a "list" of the module's Declaraciones.

   "type_ignores" is a "list" of the module's type ignore comments;
   see "ast.parse()" for more details.

      >>> print(ast.dump(ast.parse('x = 1'), indent=4))
      Module(
          body=[
              Assign(
                  targets=[
                      Name(id='x', ctx=Store())],
                  value=Constant(value=1))])

class ast.Expression(body)

   Una única expression input de Python. Tipo de nodo generado por
   "ast.parse()" cuando *mode* es ""eval"".

   "body" is a single node, one of the expression types.

      >>> print(ast.dump(ast.parse('123', mode='eval'), indent=4))
      Expression(
          body=Constant(value=123))

class ast.Interactive(body)

   Una única entrada interactiva, como en Modo interactivo. Tipo de
   nodo generado por "ast.parse()" cuando *mode* es ""single"".

   "body" is a "list" of statement nodes.

      >>> print(ast.dump(ast.parse('x = 1; y = 2', mode='single'), indent=4))
      Interactive(
          body=[
              Assign(
                  targets=[
                      Name(id='x', ctx=Store())],
                  value=Constant(value=1)),
              Assign(
                  targets=[
                      Name(id='y', ctx=Store())],
                  value=Constant(value=2))])

class ast.FunctionType(argtypes, returns)

   Una interpretación de un comentario de tipo de estilo antiguo para
   funciones, ya que las versiones de Python anteriores a la 3.5 no
   soportaban anotaciones **PEP 484**. Tipo de nodo generado por
   "ast.parse()" cuando *mode* es ""func_type"".

   Los comentarios de este tipo tendrían el siguiente aspecto:

      def sum_two_number(a, b):
          # type: (int, int) -> int
          return a + b

   "argtypes" is a "list" of expression nodes.

   "returns" is a single expression node.

      >>> print(ast.dump(ast.parse('(int, str) -> List[int]', mode='func_type'), indent=4))
      FunctionType(
          argtypes=[
              Name(id='int', ctx=Load()),
              Name(id='str', ctx=Load())],
          returns=Subscript(
              value=Name(id='List', ctx=Load()),
              slice=Name(id='int', ctx=Load()),
              ctx=Load()))

   Added in version 3.8.

### Literales

class ast.Constant(value, kind)

   A constant value. The "value" attribute of the "Constant" literal
   contains the Python object it represents. The values represented
   can be instances of "str", "bytes", "int", "float", "complex", and
   "bool", and the constants "None" and "Ellipsis".

   The "kind" attribute is an optional string. For string literals
   with a "u" prefix, "kind" is set to "'u'". For all other constants,
   "kind" is "None".

      >>> print(ast.dump(ast.parse('123', mode='eval'), indent=4))
      Expression(
          body=Constant(value=123))
      >>> print(ast.dump(ast.parse("u'hello'", mode='eval'), indent=4))
      Expression(
          body=Constant(value='hello', kind='u'))

class ast.FormattedValue(value, conversion, format_spec)

   Nodo que representa un único campo de formato en una "f-string". Si
   la cadena de caracteres contiene un único campo de formato y nada
   más, el nodo puede estar aislado de otra manera aparece en
   "JoinedStr".

   * "value" es cualquier nodo de expresión (como un literal, una
     variable o una llamada a función).

   * "conversion" es un entero:

     * -1: sin formato

     * 97 ("ord('a')"): "!a" "ASCII" formatting

     * 114 ("ord('r')"): "!r" "repr()" formatting

     * 115 ("ord('s')"): "!s" "string" formatting

   * "format_spec" es un nodo "JoinedStr" que representa el formato
     del valor, o "None" si no se ha especificado un formato. Ambos,
     "conversion" y "format_spec", pueden estar especificados al mismo
     tiempo.

class ast.JoinedStr(values)

   Un f-string que comprende una serie de nodos "FormattedValue" y
   "Constant".

      >>> print(ast.dump(ast.parse('f"sin({a}) is {sin(a):.3}"', mode='eval'), indent=4))
      Expression(
          body=JoinedStr(
              values=[
                  Constant(value='sin('),
                  FormattedValue(
                      value=Name(id='a', ctx=Load()),
                      conversion=-1),
                  Constant(value=') is '),
                  FormattedValue(
                      value=Call(
                          func=Name(id='sin', ctx=Load()),
                          args=[
                              Name(id='a', ctx=Load())]),
                      conversion=-1,
                      format_spec=JoinedStr(
                          values=[
                              Constant(value='.3')]))]))

class ast.TemplateStr(values, /)

   Added in version 3.14.

   Node representing a template string literal, comprising a series of
   "Interpolation" and "Constant" nodes. These nodes may be any order,
   and do not need to be interleaved.

      >>> expr = ast.parse('t"{name} finished {place:ordinal}"', mode='eval')
      >>> print(ast.dump(expr, indent=4))
      Expression(
          body=TemplateStr(
              values=[
                  Interpolation(
                      value=Name(id='name', ctx=Load()),
                      str='name',
                      conversion=-1),
                  Constant(value=' finished '),
                  Interpolation(
                      value=Name(id='place', ctx=Load()),
                      str='place',
                      conversion=-1,
                      format_spec=JoinedStr(
                          values=[
                              Constant(value='ordinal')]))]))

class ast.Interpolation(value, str, conversion, format_spec=None)

   Added in version 3.14.

   Node representing a single interpolation field in a template string
   literal.

   * "value" is any expression node (such as a literal, a variable, or
     a function call). This has the same meaning as
     "FormattedValue.value".

   * "str" is a constant containing the text of the interpolation
     expression.

     If "str" is set to "None", then "value" is used to generate code
     when calling "ast.unparse()". This no longer guarantees that the
     generated code is identical to the original and is intended for
     code generation.

   * "conversion" es un entero:

     * -1: no conversion

     * 97 ("ord('a')"): "!a" "ASCII" conversion

     * 114 ("ord('r')"): "!r" "repr()" conversion

     * 115 ("ord('s')"): "!s" "string" conversion

     This has the same meaning as "FormattedValue.conversion".

   * "format_spec" is a "JoinedStr" node representing the formatting
     of the value, or "None" if no format was specified. Both
     "conversion" and "format_spec" can be set at the same time. This
     has the same meaning as "FormattedValue.format_spec".

class ast.List(elts, ctx)
class ast.Tuple(elts, ctx)

   Una lista o tupla. "elts" contiene una lista de nodos que
   representa a los elementos. "ctx" es "Store" si el contenedor es un
   objetivo de asignación (por ejemplo "(x,y)=something"), y "Load" en
   cualquier otro caso.

      >>> print(ast.dump(ast.parse('[1, 2, 3]', mode='eval'), indent=4))
      Expression(
          body=List(
              elts=[
                  Constant(value=1),
                  Constant(value=2),
                  Constant(value=3)],
              ctx=Load()))
      >>> print(ast.dump(ast.parse('(1, 2, 3)', mode='eval'), indent=4))
      Expression(
          body=Tuple(
              elts=[
                  Constant(value=1),
                  Constant(value=2),
                  Constant(value=3)],
              ctx=Load()))

class ast.Set(elts)

   Un set. "elts" contiene una lista de nodos que representa a un set
   de elementos.

      >>> print(ast.dump(ast.parse('{1, 2, 3}', mode='eval'), indent=4))
      Expression(
          body=Set(
              elts=[
                  Constant(value=1),
                  Constant(value=2),
                  Constant(value=3)]))

class ast.Dict(keys, values)

   Un diccionario. "keys" y "values" contienen listas de nodos que
   representan las claves y los valores respectivamente en el orden
   correspondiente (el orden que retornaría "dictionary.keys()" y
   "dictionary.values()").

   Cuando se desempaqueta un diccionario utilizando literales de
   diccionario, la expresión a ser expandida va en la lista "values",
   con "None" en la posición correspondiente en "keys".

      >>> print(ast.dump(ast.parse('{"a":1, **d}', mode='eval'), indent=4))
      Expression(
          body=Dict(
              keys=[
                  Constant(value='a'),
                  None],
              values=[
                  Constant(value=1),
                  Name(id='d', ctx=Load())]))

### Variables

class ast.Name(id, ctx)

   Un nombre de variable. "id" contiene el nombre de una cadena de
   caracteres y "ctx" es uno de los siguientes tipos.

class ast.Load
class ast.Store
class ast.Del

   Referencias a variables que pueden ser usadas para cargar el valor
   de una variable, asignar un nuevo valor o borrarlo. Las referencias
   a variables reciben un contexto para distinguir entre estos casos.

      >>> print(ast.dump(ast.parse('a'), indent=4))
      Module(
          body=[
              Expr(
                  value=Name(id='a', ctx=Load()))])

      >>> print(ast.dump(ast.parse('a = 1'), indent=4))
      Module(
          body=[
              Assign(
                  targets=[
                      Name(id='a', ctx=Store())],
                  value=Constant(value=1))])

      >>> print(ast.dump(ast.parse('del a'), indent=4))
      Module(
          body=[
              Delete(
                  targets=[
                      Name(id='a', ctx=Del())])])

class ast.Starred(value, ctx)

   Una referencia a variable "*var". "value" contiene la variable,
   típicamente un nodo "Name". Este tipo puede ser usado cuando se
   construye un nodo "Call" con "*args".

      >>> print(ast.dump(ast.parse('a, *b = it'), indent=4))
      Module(
          body=[
              Assign(
                  targets=[
                      Tuple(
                          elts=[
                              Name(id='a', ctx=Store()),
                              Starred(
                                  value=Name(id='b', ctx=Store()),
                                  ctx=Store())],
                          ctx=Store())],
                  value=Name(id='it', ctx=Load()))])

### Expresiones

class ast.Expr(value)

   Cuando una expresión, como un llamado a función, aparece como una
   declaración por sí misma sin que su valor de retorno se use o se
   almacene, está dentro de este contenedor. "value" contiene uno de
   los otros nodos en esta sección, un nodo "Constant", "Name",
   "Lambda", "Yield" o "YieldFrom".

      >>> print(ast.dump(ast.parse('-a'), indent=4))
      Module(
          body=[
              Expr(
                  value=UnaryOp(
                      op=USub(),
                      operand=Name(id='a', ctx=Load())))])

class ast.UnaryOp(op, operand)

   Una operación unaria. "op" es el operador y "operand" es cualquier
   nodo de expresión.

class ast.UAdd
class ast.USub
class ast.Not
class ast.Invert

   Tokens de operador unario. "Not" es la palabra clave "not",
   "Invert" es el operador "~".

      >>> print(ast.dump(ast.parse('not x', mode='eval'), indent=4))
      Expression(
          body=UnaryOp(
              op=Not(),
              operand=Name(id='x', ctx=Load())))

class ast.BinOp(left, op, right)

   Una operación binaria (como la suma o división(. "op" es el
   operador, y "left" y "right" son cualquier nodo de expresión.

      >>> print(ast.dump(ast.parse('x + y', mode='eval'), indent=4))
      Expression(
          body=BinOp(
              left=Name(id='x', ctx=Load()),
              op=Add(),
              right=Name(id='y', ctx=Load())))

class ast.Add
class ast.Sub
class ast.Mult
class ast.Div
class ast.FloorDiv
class ast.Mod
class ast.Pow
class ast.LShift
class ast.RShift
class ast.BitOr
class ast.BitXor
class ast.BitAnd
class ast.MatMult

   Tokens de operador binario.

class ast.BoolOp(op, values)

   Una operación booleana, 'or' y 'and'. "op" es "Or" o "And".
   "values" son los valores involucrados. Operaciones consecutivas con
   el mismo operador, como "a or b or c", colapsan en un nodo con
   varios valores.

   Esto no incluye "not", el cual es un "UnaryOp".

      >>> print(ast.dump(ast.parse('x or y', mode='eval'), indent=4))
      Expression(
          body=BoolOp(
              op=Or(),
              values=[
                  Name(id='x', ctx=Load()),
                  Name(id='y', ctx=Load())]))

class ast.And
class ast.Or

   Tokens de operador booleano.

class ast.Compare(left, ops, comparators)

   Una comparación de dos o más valores. "left" es el primer valor en
   la comparación, "ops" es la lista de operadores, y "comparators" es
   la lista de valores después de el primer elemento en la
   comparación.

      >>> print(ast.dump(ast.parse('1 <= a < 10', mode='eval'), indent=4))
      Expression(
          body=Compare(
              left=Constant(value=1),
              ops=[
                  LtE(),
                  Lt()],
              comparators=[
                  Name(id='a', ctx=Load()),
                  Constant(value=10)]))

class ast.Eq
class ast.NotEq
class ast.Lt
class ast.LtE
class ast.Gt
class ast.GtE
class ast.Is
class ast.IsNot
class ast.In
class ast.NotIn

   Tokens de operador de comparación.

class ast.Call(func, args, keywords)

   Un llamado a función. "func" is la función, la cual suele ser un
   objeto "Name" o "Attribute". De los argumentos:

   * "args" contiene una lista de argumentos pasados por posición.

   * "keywords" contiene una lista de objetos "keyword" que
     representan argumentos pasados por nombre clave.

   The "args" and "keywords" arguments are optional and default to
   empty lists.

      >>> print(ast.dump(ast.parse('func(a, b=c, *d, **e)', mode='eval'), indent=4))
      Expression(
          body=Call(
              func=Name(id='func', ctx=Load()),
              args=[
                  Name(id='a', ctx=Load()),
                  Starred(
                      value=Name(id='d', ctx=Load()),
                      ctx=Load())],
              keywords=[
                  keyword(
                      arg='b',
                      value=Name(id='c', ctx=Load())),
                  keyword(
                      value=Name(id='e', ctx=Load()))]))

class ast.keyword(arg, value)

   Un argumento de palabra clave para una llamada de función o
   definición de clase. "arg" es una cadena de caracteres sin formato
   del nombre del parámetro, "valor" es un nodo para pasar.

class ast.IfExp(test, body, orelse)

   Una expresión como "a if b else c". Cada campo contiene un único
   nodo, por lo que en el siguiente ejemplo, todos son nodos  "Name".

      >>> print(ast.dump(ast.parse('a if b else c', mode='eval'), indent=4))
      Expression(
          body=IfExp(
              test=Name(id='b', ctx=Load()),
              body=Name(id='a', ctx=Load()),
              orelse=Name(id='c', ctx=Load())))

class ast.Attribute(value, attr, ctx)

   Acceso a atributos, por ejemplo "d.keys". "value" es un nodo,
   típicamente un "Name". "attr" es una simple cadena de caracteres
   que da el nombre del atributo, y "ctx" es "Load", "Store" o "Del"
   de acuerdo a cómo se actúe sobre el atributo.

      >>> print(ast.dump(ast.parse('snake.colour', mode='eval'), indent=4))
      Expression(
          body=Attribute(
              value=Name(id='snake', ctx=Load()),
              attr='colour',
              ctx=Load()))

class ast.NamedExpr(target, value)

   Una expresión con nombre. Este nodo AST es producido por el
   operador de expresiones de asignación (también conocido como el
   operador walrus). A diferencia del nodo "Assign" en el cual el
   primer argumento puede ser varios nodos, en este caso "target" y
   "value" deben ser nodos únicos.

      >>> print(ast.dump(ast.parse('(x := 4)', mode='eval'), indent=4))
      Expression(
          body=NamedExpr(
              target=Name(id='x', ctx=Store()),
              value=Constant(value=4)))

   Added in version 3.8.

#### Subindexado

class ast.Subscript(value, slice, ctx)

   Un subíndice, como "l[1]". "value" es el objeto subindicado
   (usualmente una secuencia o mapeo). "slice" es un índice, un
   segmento o una clave. Este puede ser una "Tuple" y contener un
   "Slice". "ctx" es "Load", "Store" or "Del" de acuerdo a la acción
   tomada con el subíndice.

      >>> print(ast.dump(ast.parse('l[1:2, 3]', mode='eval'), indent=4))
      Expression(
          body=Subscript(
              value=Name(id='l', ctx=Load()),
              slice=Tuple(
                  elts=[
                      Slice(
                          lower=Constant(value=1),
                          upper=Constant(value=2)),
                      Constant(value=3)],
                  ctx=Load()),
              ctx=Load()))

class ast.Slice(lower, upper, step)

   Una segmentación regular (en la forma "lower:upper" o
   "lower:upper:step"). Puede ocurrir solamente dentro del campo
   *slice* de "Subscript", ya sea directamente o como un elemento de
   "Tuple".

      >>> print(ast.dump(ast.parse('l[1:2]', mode='eval'), indent=4))
      Expression(
          body=Subscript(
              value=Name(id='l', ctx=Load()),
              slice=Slice(
                  lower=Constant(value=1),
                  upper=Constant(value=2)),
              ctx=Load()))

#### Comprensiones

class ast.ListComp(elt, generators)
class ast.SetComp(elt, generators)
class ast.GeneratorExp(elt, generators)
class ast.DictComp(key, value, generators)

   Listas y sets por comprensión, expresiones de generadores, y
   diccionarios por comprensión. "elt" (o "key" y "value") es un único
   nodo que representa la parte que va a ser evaluada por cada item.

   "generators" es una lista de nodos "comprehension".

      >>> print(ast.dump(
      ...     ast.parse('[x for x in numbers]', mode='eval'),
      ...     indent=4,
      ... ))
      Expression(
          body=ListComp(
              elt=Name(id='x', ctx=Load()),
              generators=[
                  comprehension(
                      target=Name(id='x', ctx=Store()),
                      iter=Name(id='numbers', ctx=Load()),
                      is_async=0)]))
      >>> print(ast.dump(
      ...     ast.parse('{x: x**2 for x in numbers}', mode='eval'),
      ...     indent=4,
      ... ))
      Expression(
          body=DictComp(
              key=Name(id='x', ctx=Load()),
              value=BinOp(
                  left=Name(id='x', ctx=Load()),
                  op=Pow(),
                  right=Constant(value=2)),
              generators=[
                  comprehension(
                      target=Name(id='x', ctx=Store()),
                      iter=Name(id='numbers', ctx=Load()),
                      is_async=0)]))
      >>> print(ast.dump(
      ...     ast.parse('{x for x in numbers}', mode='eval'),
      ...     indent=4,
      ... ))
      Expression(
          body=SetComp(
              elt=Name(id='x', ctx=Load()),
              generators=[
                  comprehension(
                      target=Name(id='x', ctx=Store()),
                      iter=Name(id='numbers', ctx=Load()),
                      is_async=0)]))

class ast.comprehension(target, iter, ifs, is_async)

   Una cláusula "for" en una comprensión. "target" es la referencia a
   usarse por cada elemento - típicamente un nodo "Name" o "Tuple".
   "iter" es el objeto por el cual se itera. "ifs" es una lista de
   expresiones de prueba: cada cláusula "for" puede tener múltiples
   "ifs".

   "is_async" indica que una compresión es asíncrona (usando "async
   for" en lugar de "for"). El valor es un entero (0 o 1).

      >>> print(ast.dump(ast.parse('[ord(c) for line in file for c in line]', mode='eval'),
      ...                indent=4)) # Multiple comprehensions in one.
      Expression(
          body=ListComp(
              elt=Call(
                  func=Name(id='ord', ctx=Load()),
                  args=[
                      Name(id='c', ctx=Load())]),
              generators=[
                  comprehension(
                      target=Name(id='line', ctx=Store()),
                      iter=Name(id='file', ctx=Load()),
                      is_async=0),
                  comprehension(
                      target=Name(id='c', ctx=Store()),
                      iter=Name(id='line', ctx=Load()),
                      is_async=0)]))

      >>> print(ast.dump(ast.parse('(n**2 for n in it if n>5 if n<10)', mode='eval'),
      ...                indent=4)) # generator comprehension
      Expression(
          body=GeneratorExp(
              elt=BinOp(
                  left=Name(id='n', ctx=Load()),
                  op=Pow(),
                  right=Constant(value=2)),
              generators=[
                  comprehension(
                      target=Name(id='n', ctx=Store()),
                      iter=Name(id='it', ctx=Load()),
                      ifs=[
                          Compare(
                              left=Name(id='n', ctx=Load()),
                              ops=[
                                  Gt()],
                              comparators=[
                                  Constant(value=5)]),
                          Compare(
                              left=Name(id='n', ctx=Load()),
                              ops=[
                                  Lt()],
                              comparators=[
                                  Constant(value=10)])],
                      is_async=0)]))

      >>> print(ast.dump(ast.parse('[i async for i in soc]', mode='eval'),
      ...                indent=4)) # Async comprehension
      Expression(
          body=ListComp(
              elt=Name(id='i', ctx=Load()),
              generators=[
                  comprehension(
                      target=Name(id='i', ctx=Store()),
                      iter=Name(id='soc', ctx=Load()),
                      is_async=1)]))

### Declaraciones

class ast.Assign(targets, value, type_comment)

   Una asignación. "targets" es una lista de nodos, y "value" es un
   nodo único.

   Nodos múltiples en "targets" representa asignar el mismo valor a
   cada uno. El desempaquetado se representa poniendo una "Tuple" o
   "List" en "targets".

   type_comment

      "type_comment" es una cadena de caracteres opcional con la
      anotación de tipos como comentario.

      >>> print(ast.dump(ast.parse('a = b = 1'), indent=4)) # Multiple assignment
      Module(
          body=[
              Assign(
                  targets=[
                      Name(id='a', ctx=Store()),
                      Name(id='b', ctx=Store())],
                  value=Constant(value=1))])

      >>> print(ast.dump(ast.parse('a,b = c'), indent=4)) # Unpacking
      Module(
          body=[
              Assign(
                  targets=[
                      Tuple(
                          elts=[
                              Name(id='a', ctx=Store()),
                              Name(id='b', ctx=Store())],
                          ctx=Store())],
                  value=Name(id='c', ctx=Load()))])

class ast.AnnAssign(target, annotation, value, simple)

   An assignment with a type annotation. "target" is a single node and
   can be a "Name", an "Attribute" or a "Subscript". "annotation" is
   the annotation, such as a "Constant" or "Name" node. "value" is a
   single optional node.

   "simple" is always either 0 (indicating a "complex" target) or 1
   (indicating a "simple" target). A "simple" target consists solely
   of a "Name" node that does not appear between parentheses; all
   other targets are considered complex. Only simple targets appear in
   the "__annotations__" dictionary of modules and classes.

      >>> print(ast.dump(ast.parse('c: int'), indent=4))
      Module(
          body=[
              AnnAssign(
                  target=Name(id='c', ctx=Store()),
                  annotation=Name(id='int', ctx=Load()),
                  simple=1)])

      >>> print(ast.dump(ast.parse('(a): int = 1'), indent=4)) # Annotation with parenthesis
      Module(
          body=[
              AnnAssign(
                  target=Name(id='a', ctx=Store()),
                  annotation=Name(id='int', ctx=Load()),
                  value=Constant(value=1),
                  simple=0)])

      >>> print(ast.dump(ast.parse('a.b: int'), indent=4)) # Attribute annotation
      Module(
          body=[
              AnnAssign(
                  target=Attribute(
                      value=Name(id='a', ctx=Load()),
                      attr='b',
                      ctx=Store()),
                  annotation=Name(id='int', ctx=Load()),
                  simple=0)])

      >>> print(ast.dump(ast.parse('a[1]: int'), indent=4)) # Subscript annotation
      Module(
          body=[
              AnnAssign(
                  target=Subscript(
                      value=Name(id='a', ctx=Load()),
                      slice=Constant(value=1),
                      ctx=Store()),
                  annotation=Name(id='int', ctx=Load()),
                  simple=0)])

class ast.AugAssign(target, op, value)

   Asignación aumentada, como "a+=1". En el siguiente ejemplo,
   "target" es un nodo "Name" para "x" (con el contexto "Store"), "op"
   es "Add" y "value" es un "Constant" con valor 1.

   El atributo "target" no puede ser de clase "Tuple" o "List", a
   diferencia de los objetivos de "Assign".

      >>> print(ast.dump(ast.parse('x += 2'), indent=4))
      Module(
          body=[
              AugAssign(
                  target=Name(id='x', ctx=Store()),
                  op=Add(),
                  value=Constant(value=2))])

class ast.Raise(exc, cause)

   Una declaración "raise". "exc" es el objeto de excepción a ser
   lanzado, normalmente un "Call" or "Name", o "None" para un "raise"
   solo. "cause" es la parte opcional para "y" en "raise x from y".

      >>> print(ast.dump(ast.parse('raise x from y'), indent=4))
      Module(
          body=[
              Raise(
                  exc=Name(id='x', ctx=Load()),
                  cause=Name(id='y', ctx=Load()))])

class ast.Assert(test, msg)

   Una aserción. "test" contiene la condición, como un nodo "Compare".
   "msg" contiene el mensaje de fallo.

      >>> print(ast.dump(ast.parse('assert x,y'), indent=4))
      Module(
          body=[
              Assert(
                  test=Name(id='x', ctx=Load()),
                  msg=Name(id='y', ctx=Load()))])

class ast.Delete(targets)

   Contiene una declaración "del". "targets" es una lista de nodos,
   como nodos "Name", "Attribute" o "Subscript".

      >>> print(ast.dump(ast.parse('del x,y,z'), indent=4))
      Module(
          body=[
              Delete(
                  targets=[
                      Name(id='x', ctx=Del()),
                      Name(id='y', ctx=Del()),
                      Name(id='z', ctx=Del())])])

class ast.Pass

   Una declaración "pass".

      >>> print(ast.dump(ast.parse('pass'), indent=4))
      Module(
          body=[
              Pass()])

class ast.TypeAlias(name, type_params, value)

   Un alias type alias creado mediante la sentencia "type". "name" es
   el nombre del alias, "type_params" es una lista de parámetros type,
   y "value" es el valor del alias de tipo.

      >>> print(ast.dump(ast.parse('type Alias = int'), indent=4))
      Module(
          body=[
              TypeAlias(
                  name=Name(id='Alias', ctx=Store()),
                  value=Name(id='int', ctx=Load()))])

   Added in version 3.12.

Otras declaraciones que solo son aplicables dentro de funciones o
bucles descritos en otras secciones.

#### Importaciones

class ast.Import(names)

   Una declaración de importación. "names" es una lista de nodos
   "alias".

      >>> print(ast.dump(ast.parse('import x,y,z'), indent=4))
      Module(
          body=[
              Import(
                  names=[
                      alias(name='x'),
                      alias(name='y'),
                      alias(name='z')])])

class ast.ImportFrom(module, names, level)

   Representa "form x import y". "module" es una cadena de caracteres
   sin formato del nombre 'from', sin puntos, o "None" para
   declaraciones como "from . import foo". "level" es un entero que
   contiene el nivel relativo de la importación (0 significa una
   importación absoluta).

      >>> print(ast.dump(ast.parse('from y import x,y,z'), indent=4))
      Module(
          body=[
              ImportFrom(
                  module='y',
                  names=[
                      alias(name='x'),
                      alias(name='y'),
                      alias(name='z')],
                  level=0)])

class ast.alias(name, asname)

   Ambos parámetros son cadenas de caracteres sin formato para los
   nombres. "asname" puede ser "None" si se va a usar el nombre
   regular.

      >>> print(ast.dump(ast.parse('from ..foo.bar import a as b, c'), indent=4))
      Module(
          body=[
              ImportFrom(
                  module='foo.bar',
                  names=[
                      alias(name='a', asname='b'),
                      alias(name='c')],
                  level=2)])

### Control de flujo

Nota:

  Cláusulas opcionales como "else" se guardan como una lista vacía si
  no están presentes.

class ast.If(test, body, orelse)

   Una declaración "if". "test" contiene un único nodo, como un nodo
   "Compare". "body" y "orelse" contiene cada uno una lista de nodos.

   Cláusulas "elif" no tienen una representación especial en AST, pero
   pueden aparecer como nodos extra "If" dentro de la sección "orelse"
   del nodo anterior.

      >>> print(ast.dump(ast.parse("""
      ... if x:
      ...    ...
      ... elif y:
      ...    ...
      ... else:
      ...    ...
      ... """), indent=4))
      Module(
          body=[
              If(
                  test=Name(id='x', ctx=Load()),
                  body=[
                      Expr(
                          value=Constant(value=Ellipsis))],
                  orelse=[
                      If(
                          test=Name(id='y', ctx=Load()),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))],
                          orelse=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

class ast.For(target, iter, body, orelse, type_comment)

   Un bucle "for". "target" contiene las variables a las que asigna el
   bucle, como un único nodo "Name", "Tuple", "List", "Attribute" o
   "Subscript". "iter" contiene el elemento sobre el que se realizará
   el bucle, nuevamente como un solo nodo. "body" y "orelse" contienen
   listas de nodos para ejecutar. Los de "orelse" se ejecutan si el
   ciclo finaliza normalmente, en lugar de mediante una instrucción
   "break".

   type_comment

      "type_comment" es una cadena de caracteres opcional con la
      anotación de tipos como comentario.

      >>> print(ast.dump(ast.parse("""
      ... for x in y:
      ...     ...
      ... else:
      ...     ...
      ... """), indent=4))
      Module(
          body=[
              For(
                  target=Name(id='x', ctx=Store()),
                  iter=Name(id='y', ctx=Load()),
                  body=[
                      Expr(
                          value=Constant(value=Ellipsis))],
                  orelse=[
                      Expr(
                          value=Constant(value=Ellipsis))])])

class ast.While(test, body, orelse)

   Un bucle "while". "test" contiene la condición, como un nodo
   "Compare".

      >>> print(ast.dump(ast.parse("""
      ... while x:
      ...    ...
      ... else:
      ...    ...
      ... """), indent=4))
      Module(
          body=[
              While(
                  test=Name(id='x', ctx=Load()),
                  body=[
                      Expr(
                          value=Constant(value=Ellipsis))],
                  orelse=[
                      Expr(
                          value=Constant(value=Ellipsis))])])

class ast.Break
class ast.Continue

   Las declaraciones "break" y "continue".

      >>> print(ast.dump(ast.parse("""\
      ... for a in b:
      ...     if a > 5:
      ...         break
      ...     else:
      ...         continue
      ...
      ... """), indent=4))
      Module(
          body=[
              For(
                  target=Name(id='a', ctx=Store()),
                  iter=Name(id='b', ctx=Load()),
                  body=[
                      If(
                          test=Compare(
                              left=Name(id='a', ctx=Load()),
                              ops=[
                                  Gt()],
                              comparators=[
                                  Constant(value=5)]),
                          body=[
                              Break()],
                          orelse=[
                              Continue()])])])

class ast.Try(body, handlers, orelse, finalbody)

   Bloques "try". Todos los atributos son listas de nodos a ejecutar,
   excepto para "handlers", el cual es una lista de nodos
   "ExceptHandler".

      >>> print(ast.dump(ast.parse("""
      ... try:
      ...    ...
      ... except Exception:
      ...    ...
      ... except OtherException as e:
      ...    ...
      ... else:
      ...    ...
      ... finally:
      ...    ...
      ... """), indent=4))
      Module(
          body=[
              Try(
                  body=[
                      Expr(
                          value=Constant(value=Ellipsis))],
                  handlers=[
                      ExceptHandler(
                          type=Name(id='Exception', ctx=Load()),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))]),
                      ExceptHandler(
                          type=Name(id='OtherException', ctx=Load()),
                          name='e',
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])],
                  orelse=[
                      Expr(
                          value=Constant(value=Ellipsis))],
                  finalbody=[
                      Expr(
                          value=Constant(value=Ellipsis))])])

class ast.TryStar(body, handlers, orelse, finalbody)

   "try" blocks which are followed by "except*" clauses. The
   attributes are the same as for "Try" but the "ExceptHandler" nodes
   in "handlers" are interpreted as "except*" blocks rather than
   "except".

      >>> print(ast.dump(ast.parse("""
      ... try:
      ...    ...
      ... except* Exception:
      ...    ...
      ... """), indent=4))
      Module(
          body=[
              TryStar(
                  body=[
                      Expr(
                          value=Constant(value=Ellipsis))],
                  handlers=[
                      ExceptHandler(
                          type=Name(id='Exception', ctx=Load()),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Added in version 3.11.

class ast.ExceptHandler(type, name, body)

   Una sola cláusula "except". "type" es el tipo de excepción con el
   que coincidirá, normalmente un nodo "Name" (o "None" para una
   cláusula "except:" generalizada). "name" es una cadena sin formato
   para que el nombre contenga la excepción, o "None" si la cláusula
   no tiene "as foo". "body" es una lista de nodos.

      >>> print(ast.dump(ast.parse("""\
      ... try:
      ...     a + 1
      ... except TypeError:
      ...     pass
      ... """), indent=4))
      Module(
          body=[
              Try(
                  body=[
                      Expr(
                          value=BinOp(
                              left=Name(id='a', ctx=Load()),
                              op=Add(),
                              right=Constant(value=1)))],
                  handlers=[
                      ExceptHandler(
                          type=Name(id='TypeError', ctx=Load()),
                          body=[
                              Pass()])])])

class ast.With(items, body, type_comment)

   Un bloque "with". "items" es una lista de nodos "withitem" que
   representan los administradores de contexto, y "body" es el bloque
   con sangría dentro del contexto.

   type_comment

      "type_comment" es una cadena de caracteres opcional con la
      anotación de tipos como comentario.

class ast.withitem(context_expr, optional_vars)

   Un administrador de contexto único en un bloque "with".
   "context_expr" es el administrador de contexto, a menudo un nodo
   "Call". "optional_vars" es un "Name", "Tuple" o "List" para la
   parte "as foo", o "None" si no se usa.

      >>> print(ast.dump(ast.parse("""\
      ... with a as b, c as d:
      ...    something(b, d)
      ... """), indent=4))
      Module(
          body=[
              With(
                  items=[
                      withitem(
                          context_expr=Name(id='a', ctx=Load()),
                          optional_vars=Name(id='b', ctx=Store())),
                      withitem(
                          context_expr=Name(id='c', ctx=Load()),
                          optional_vars=Name(id='d', ctx=Store()))],
                  body=[
                      Expr(
                          value=Call(
                              func=Name(id='something', ctx=Load()),
                              args=[
                                  Name(id='b', ctx=Load()),
                                  Name(id='d', ctx=Load())]))])])

### La coincidencia de patrones

class ast.Match(subject, cases)

   Una declaración "match". "subject" contiene el sujeto de la
   coincidencia (el objeto que se compara con los casos) y "cases"
   contiene un iterable de nodos "match_case" con los diferentes
   casos.

   Added in version 3.10.

class ast.match_case(pattern, guard, body)

   Un patrón de caso único en una declaración "match". "pattern"
   contiene el patrón de coincidencia con el que se comparará el
   sujeto. Tenga en cuenta que los nodos "AST" producidos para
   patrones difieren de los producidos para expresiones, incluso
   cuando comparten la misma sintaxis.

   El atributo "guard" contiene una expresión que se evaluará si el
   patrón coincide con el sujeto.

   "body" contiene una lista de nodos para ejecutar si el patrón
   coincide y el resultado de evaluar la expresión de protección es
   verdadero.

      >>> print(ast.dump(ast.parse("""
      ... match x:
      ...     case [x] if x>0:
      ...         ...
      ...     case tuple():
      ...         ...
      ... """), indent=4))
      Module(
          body=[
              Match(
                  subject=Name(id='x', ctx=Load()),
                  cases=[
                      match_case(
                          pattern=MatchSequence(
                              patterns=[
                                  MatchAs(name='x')]),
                          guard=Compare(
                              left=Name(id='x', ctx=Load()),
                              ops=[
                                  Gt()],
                              comparators=[
                                  Constant(value=0)]),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))]),
                      match_case(
                          pattern=MatchClass(
                              cls=Name(id='tuple', ctx=Load())),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Added in version 3.10.

class ast.MatchValue(value)

   Un patrón de valor o literal de coincidencia que se compara por
   igualdad. "value" es un nodo de expresión. Los nodos de valores
   permitidos están restringidos como se describe en la documentación
   de la declaración de coincidencia. Este patrón tiene éxito si el
   sujeto de la coincidencia es igual al valor evaluado.

      >>> print(ast.dump(ast.parse("""
      ... match x:
      ...     case "Relevant":
      ...         ...
      ... """), indent=4))
      Module(
          body=[
              Match(
                  subject=Name(id='x', ctx=Load()),
                  cases=[
                      match_case(
                          pattern=MatchValue(
                              value=Constant(value='Relevant')),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Added in version 3.10.

class ast.MatchSingleton(value)

   Un patrón literal de coincidencia que se compara por identidad.
   "value" es el singleton que se va a comparar con: "None", "True" o
   "False". Este patrón tiene éxito si el sujeto de la coincidencia es
   la constante dada.

      >>> print(ast.dump(ast.parse("""
      ... match x:
      ...     case None:
      ...         ...
      ... """), indent=4))
      Module(
          body=[
              Match(
                  subject=Name(id='x', ctx=Load()),
                  cases=[
                      match_case(
                          pattern=MatchSingleton(value=None),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Added in version 3.10.

class ast.MatchSequence(patterns)

   Un patrón de secuencia de coincidencia. "patterns" contiene los
   patrones que se compararán con los elementos del sujeto si el
   sujeto es una secuencia. Coincide con una secuencia de longitud
   variable si uno de los subpatrones es un nodo "MatchStar"; de lo
   contrario, coincide con una secuencia de longitud fija.

      >>> print(ast.dump(ast.parse("""
      ... match x:
      ...     case [1, 2]:
      ...         ...
      ... """), indent=4))
      Module(
          body=[
              Match(
                  subject=Name(id='x', ctx=Load()),
                  cases=[
                      match_case(
                          pattern=MatchSequence(
                              patterns=[
                                  MatchValue(
                                      value=Constant(value=1)),
                                  MatchValue(
                                      value=Constant(value=2))]),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Added in version 3.10.

class ast.MatchStar(name)

   Coincide con el resto de la secuencia en un patrón de secuencia de
   coincidencia de longitud variable. Si "name" no es "None", una
   lista que contiene los elementos de secuencia restantes está
   vinculada a ese nombre si el patrón de secuencia general es
   exitoso.

      >>> print(ast.dump(ast.parse("""
      ... match x:
      ...     case [1, 2, *rest]:
      ...         ...
      ...     case [*_]:
      ...         ...
      ... """), indent=4))
      Module(
          body=[
              Match(
                  subject=Name(id='x', ctx=Load()),
                  cases=[
                      match_case(
                          pattern=MatchSequence(
                              patterns=[
                                  MatchValue(
                                      value=Constant(value=1)),
                                  MatchValue(
                                      value=Constant(value=2)),
                                  MatchStar(name='rest')]),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))]),
                      match_case(
                          pattern=MatchSequence(
                              patterns=[
                                  MatchStar()]),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Added in version 3.10.

class ast.MatchMapping(keys, patterns, rest)

   Un patrón de mapeo de coincidencias. "keys" es una secuencia de
   nodos de expresión. "patterns" es una secuencia correspondiente de
   nodos de patrón. "rest" es un nombre opcional que se puede
   especificar para capturar los elementos de mapeo restantes. Las
   expresiones clave permitidas están restringidas como se describe en
   la documentación de la declaración de coincidencia.

   Este patrón tiene éxito si el sujeto es un mapeo, todas las
   expresiones clave evaluadas están presentes en el mapeo y el valor
   correspondiente a cada clave coincide con el subpatrón
   correspondiente. Si "rest" no es "None", un dict que contiene los
   elementos de mapeo restantes se vincula a ese nombre si el patrón
   de mapeo general es exitoso.

      >>> print(ast.dump(ast.parse("""
      ... match x:
      ...     case {1: _, 2: _}:
      ...         ...
      ...     case {**rest}:
      ...         ...
      ... """), indent=4))
      Module(
          body=[
              Match(
                  subject=Name(id='x', ctx=Load()),
                  cases=[
                      match_case(
                          pattern=MatchMapping(
                              keys=[
                                  Constant(value=1),
                                  Constant(value=2)],
                              patterns=[
                                  MatchAs(),
                                  MatchAs()]),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))]),
                      match_case(
                          pattern=MatchMapping(rest='rest'),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Added in version 3.10.

class ast.MatchClass(cls, patterns, kwd_attrs, kwd_patterns)

   Un patrón de clase coincidente. "cls" es una expresión que da la
   clase nominal que se va a emparejar. "patterns" es una secuencia de
   nodos de patrón que se compararán con la secuencia definida por la
   clase de atributos de coincidencia de patrones. "kwd_attrs" es una
   secuencia de atributos adicionales que deben coincidir
   (especificados como argumentos de palabra clave en el patrón de
   clase), "kwd_patterns" son los patrones correspondientes
   (especificados como valores de palabras clave en el patrón de
   clase).

   Este patrón tiene éxito si el sujeto es una instancia de la clase
   nominada, todos los patrones posicionales coinciden con los
   atributos definidos por la clase correspondientes y cualquier
   atributo de palabra clave especificado coincide con su patrón
   correspondiente.

   Nota: las clases pueden definir una propiedad que retorna self para
   hacer coincidir un nodo de patrón con la instancia que se está
   comparando. Varios tipos incorporados también se combinan de esa
   manera, como se describe en la documentación de la declaración de
   coincidencia.

      >>> print(ast.dump(ast.parse("""
      ... match x:
      ...     case Point2D(0, 0):
      ...         ...
      ...     case Point3D(x=0, y=0, z=0):
      ...         ...
      ... """), indent=4))
      Module(
          body=[
              Match(
                  subject=Name(id='x', ctx=Load()),
                  cases=[
                      match_case(
                          pattern=MatchClass(
                              cls=Name(id='Point2D', ctx=Load()),
                              patterns=[
                                  MatchValue(
                                      value=Constant(value=0)),
                                  MatchValue(
                                      value=Constant(value=0))]),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))]),
                      match_case(
                          pattern=MatchClass(
                              cls=Name(id='Point3D', ctx=Load()),
                              kwd_attrs=[
                                  'x',
                                  'y',
                                  'z'],
                              kwd_patterns=[
                                  MatchValue(
                                      value=Constant(value=0)),
                                  MatchValue(
                                      value=Constant(value=0)),
                                  MatchValue(
                                      value=Constant(value=0))]),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Added in version 3.10.

class ast.MatchAs(pattern, name)

   Una coincidencia "como patrón", patrón de captura o patrón comodín.
   "pattern" contiene el patrón de coincidencia con el que se
   comparará el sujeto. Si el patrón es "None", el nodo representa un
   patrón de captura (es decir, un nombre simple) y siempre tendrá
   éxito.

   El atributo "name" contiene el nombre que se vinculará si el patrón
   tiene éxito. Si "name" es "None", "pattern" también debe ser "None"
   y el nodo representa el patrón comodín.

      >>> print(ast.dump(ast.parse("""
      ... match x:
      ...     case [x] as y:
      ...         ...
      ...     case _:
      ...         ...
      ... """), indent=4))
      Module(
          body=[
              Match(
                  subject=Name(id='x', ctx=Load()),
                  cases=[
                      match_case(
                          pattern=MatchAs(
                              pattern=MatchSequence(
                                  patterns=[
                                      MatchAs(name='x')]),
                              name='y'),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))]),
                      match_case(
                          pattern=MatchAs(),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Added in version 3.10.

class ast.MatchOr(patterns)

   Una coincidencia "o patrón". Un patrón-o hace coincidir cada uno de
   sus subpatrones con el sujeto, hasta que uno tiene éxito. Entonces
   se considera que el patrón-o tiene éxito. Si ninguno de los
   subpatrones tiene éxito, el patrón o falla. El atributo "patterns"
   contiene una lista de nodos de patrones de coincidencia que se
   compararán con el sujeto.

      >>> print(ast.dump(ast.parse("""
      ... match x:
      ...     case [x] | (y):
      ...         ...
      ... """), indent=4))
      Module(
          body=[
              Match(
                  subject=Name(id='x', ctx=Load()),
                  cases=[
                      match_case(
                          pattern=MatchOr(
                              patterns=[
                                  MatchSequence(
                                      patterns=[
                                          MatchAs(name='x')]),
                                  MatchAs(name='y')]),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Added in version 3.10.

### Type annotations

class ast.TypeIgnore(lineno, tag)

   A "# type: ignore" comment located at *lineno*. *tag* is the
   optional tag specified by the form "# type: ignore <tag>".

      >>> print(ast.dump(ast.parse('x = 1 # type: ignore', type_comments=True), indent=4))
      Module(
          body=[
              Assign(
                  targets=[
                      Name(id='x', ctx=Store())],
                  value=Constant(value=1))],
          type_ignores=[
              TypeIgnore(lineno=1, tag='')])
      >>> print(ast.dump(ast.parse('x: bool = 1 # type: ignore[assignment]', type_comments=True), indent=4))
      Module(
          body=[
              AnnAssign(
                  target=Name(id='x', ctx=Store()),
                  annotation=Name(id='bool', ctx=Load()),
                  value=Constant(value=1),
                  simple=1)],
          type_ignores=[
              TypeIgnore(lineno=1, tag='[assignment]')])

   Nota:

     "TypeIgnore" nodes are not generated when the *type_comments*
     parameter is set to "False" (default).  See "ast.parse()" for
     more details.

   Added in version 3.8.

### Tipos de parámetro

"Parámetros de tipo pueden existir en clases, funciones y tipos de
alias"

class ast.TypeVar(name, bound, default_value)

   A "typing.TypeVar". "name" is the name of the type variable.
   "bound" is the bound or constraints, if any. If "bound" is a
   "Tuple", it represents constraints; otherwise it represents the
   bound. "default_value" is the default value; if the "TypeVar" has
   no default, this attribute will be set to "None".

      >>> print(ast.dump(ast.parse("type Alias[T: int = bool] = list[T]"), indent=4))
      Module(
          body=[
              TypeAlias(
                  name=Name(id='Alias', ctx=Store()),
                  type_params=[
                      TypeVar(
                          name='T',
                          bound=Name(id='int', ctx=Load()),
                          default_value=Name(id='bool', ctx=Load()))],
                  value=Subscript(
                      value=Name(id='list', ctx=Load()),
                      slice=Name(id='T', ctx=Load()),
                      ctx=Load()))])

   Added in version 3.12.

   Distinto en la versión 3.13: Added the *default_value* parameter.

class ast.ParamSpec(name, default_value)

   A "typing.ParamSpec". "name" is the name of the parameter
   specification. "default_value" is the default value; if the
   "ParamSpec" has no default, this attribute will be set to "None".

      >>> print(ast.dump(ast.parse("type Alias[**P = [int, str]] = Callable[P, int]"), indent=4))
      Module(
          body=[
              TypeAlias(
                  name=Name(id='Alias', ctx=Store()),
                  type_params=[
                      ParamSpec(
                          name='P',
                          default_value=List(
                              elts=[
                                  Name(id='int', ctx=Load()),
                                  Name(id='str', ctx=Load())],
                              ctx=Load()))],
                  value=Subscript(
                      value=Name(id='Callable', ctx=Load()),
                      slice=Tuple(
                          elts=[
                              Name(id='P', ctx=Load()),
                              Name(id='int', ctx=Load())],
                          ctx=Load()),
                      ctx=Load()))])

   Added in version 3.12.

   Distinto en la versión 3.13: Added the *default_value* parameter.

class ast.TypeVarTuple(name, default_value)

   A "typing.TypeVarTuple". "name" is the name of the type variable
   tuple. "default_value" is the default value; if the "TypeVarTuple"
   has no default, this attribute will be set to "None".

      >>> print(ast.dump(ast.parse("type Alias[*Ts = ()] = tuple[*Ts]"), indent=4))
      Module(
          body=[
              TypeAlias(
                  name=Name(id='Alias', ctx=Store()),
                  type_params=[
                      TypeVarTuple(
                          name='Ts',
                          default_value=Tuple(ctx=Load()))],
                  value=Subscript(
                      value=Name(id='tuple', ctx=Load()),
                      slice=Tuple(
                          elts=[
                              Starred(
                                  value=Name(id='Ts', ctx=Load()),
                                  ctx=Load())],
                          ctx=Load()),
                      ctx=Load()))])

   Added in version 3.12.

   Distinto en la versión 3.13: Added the *default_value* parameter.

### Definiciones de función y clase

class ast.FunctionDef(name, args, body, decorator_list, returns, type_comment, type_params)

   Una definición de función.

   * "name" es una cadena de caracteres sin formato del nombre de la
     función.

   * "args" es un nodo "arguments".

   * "body" es la lista de nodos dentro de la función.

   * "decorator_list" es la lista de decoradores que se aplicarán,
     almacenados en el exterior primero (es decir, el primero de la
     lista se aplicará al final).

   * "returns" es la anotación de retorno.

   * "type_params" es una lista de  parametros de tipo.

   type_comment

      "type_comment" es una cadena de caracteres opcional con la
      anotación de tipos como comentario.

   Distinto en la versión 3.12: Se ha añadido "type_params".

class ast.Lambda(args, body)

   "lambda" es una definición de función mínima que se puede utilizar
   dentro de una expresión. A diferencia de "FunctionDef", "body"
   tiene un solo nodo.

      >>> print(ast.dump(ast.parse('lambda x,y: ...'), indent=4))
      Module(
          body=[
              Expr(
                  value=Lambda(
                      args=arguments(
                          args=[
                              arg(arg='x'),
                              arg(arg='y')]),
                      body=Constant(value=Ellipsis)))])

class ast.arguments(posonlyargs, args, vararg, kwonlyargs, kw_defaults, kwarg, defaults)

   Los argumentos para una función.

   * "posonlyargs", "args" y "kwonlyargs" son listas de nodos "arg".

   * "vararg" y "kwarg" son nodos "arg" únicos, en referencia a los
     parámetros "*args, **kwargs".

   * "kw_defaults" es una lista de valores predeterminados para
     argumentos de solo palabras clave. Si uno es "None", se requiere
     el argumento correspondiente.

   * "defaults" es una lista de valores predeterminados para
     argumentos que se pueden pasar posicionalmente. Si hay menos
     valores predeterminados, corresponden a los últimos n argumentos.

class ast.arg(arg, annotation, type_comment)

   A single argument in a list. "arg" is a raw string of the argument
   name; "annotation" is its annotation, such as a "Name" node.

   type_comment

      "type_comment" es una cadena opcional con la anotación de tipo
      como comentario

      >>> print(ast.dump(ast.parse("""\
      ... @decorator1
      ... @decorator2
      ... def f(a: 'annotation', b=1, c=2, *d, e, f=3, **g) -> 'return annotation':
      ...     pass
      ... """), indent=4))
      Module(
          body=[
              FunctionDef(
                  name='f',
                  args=arguments(
                      args=[
                          arg(
                              arg='a',
                              annotation=Constant(value='annotation')),
                          arg(arg='b'),
                          arg(arg='c')],
                      vararg=arg(arg='d'),
                      kwonlyargs=[
                          arg(arg='e'),
                          arg(arg='f')],
                      kw_defaults=[
                          None,
                          Constant(value=3)],
                      kwarg=arg(arg='g'),
                      defaults=[
                          Constant(value=1),
                          Constant(value=2)]),
                  body=[
                      Pass()],
                  decorator_list=[
                      Name(id='decorator1', ctx=Load()),
                      Name(id='decorator2', ctx=Load())],
                  returns=Constant(value='return annotation'))])

class ast.Return(value)

   Una declaración "return".

      >>> print(ast.dump(ast.parse('return 4'), indent=4))
      Module(
          body=[
              Return(
                  value=Constant(value=4))])

class ast.Yield(value)
class ast.YieldFrom(value)

   A "yield" or "yield from" expression. Because these are
   expressions, they must be wrapped in an "Expr" node if the value
   sent back is not used.

      >>> print(ast.dump(ast.parse('yield x'), indent=4))
      Module(
          body=[
              Expr(
                  value=Yield(
                      value=Name(id='x', ctx=Load())))])

      >>> print(ast.dump(ast.parse('yield from x'), indent=4))
      Module(
          body=[
              Expr(
                  value=YieldFrom(
                      value=Name(id='x', ctx=Load())))])

class ast.Global(names)
class ast.Nonlocal(names)

   Declaraciones "global" y "nonlocal". "names" es una lista de
   cadenas sin formato.

      >>> print(ast.dump(ast.parse('global x,y,z'), indent=4))
      Module(
          body=[
              Global(
                  names=[
                      'x',
                      'y',
                      'z'])])

      >>> print(ast.dump(ast.parse('nonlocal x,y,z'), indent=4))
      Module(
          body=[
              Nonlocal(
                  names=[
                      'x',
                      'y',
                      'z'])])

class ast.ClassDef(name, bases, keywords, body, decorator_list, type_params)

   Una definición de clase.

   * "name" es una cadena sin formato para el nombre de la clase

   * "bases" es una lista de nodos para clases base especificadas
     explícitamente.

   * "keywords" is a list of "keyword" nodes, principally for
     'metaclass'. Other keywords will be passed to the metaclass, as
     per **PEP 3115**.

   * "body" es una lista de nodos que representan el código dentro de
     la definición de clase.

   * "decorator_list" es una lista de nodos, como en "FunctionDef".

   * "type_params" es una lista de  parametros de tipo.

      >>> print(ast.dump(ast.parse("""\
      ... @decorator1
      ... @decorator2
      ... class Foo(base1, base2, metaclass=meta):
      ...     pass
      ... """), indent=4))
      Module(
          body=[
              ClassDef(
                  name='Foo',
                  bases=[
                      Name(id='base1', ctx=Load()),
                      Name(id='base2', ctx=Load())],
                  keywords=[
                      keyword(
                          arg='metaclass',
                          value=Name(id='meta', ctx=Load()))],
                  body=[
                      Pass()],
                  decorator_list=[
                      Name(id='decorator1', ctx=Load()),
                      Name(id='decorator2', ctx=Load())])])

   Distinto en la versión 3.12: Se ha añadido "type_params".

### Async y await

class ast.AsyncFunctionDef(name, args, body, decorator_list, returns, type_comment, type_params)

   Una definición de función "async def". Tiene los mismos campos que
   "FunctionDef".

   Distinto en la versión 3.12: Se ha añadido "type_params".

class ast.Await(value)

   Una expresión "await". "value" es lo que espera. Solo válido en el
   cuerpo de un "AsyncFunctionDef".

   >>> print(ast.dump(ast.parse("""\
   ... async def f():
   ...     await other_func()
   ... """), indent=4))
   Module(
       body=[
           AsyncFunctionDef(
               name='f',
               args=arguments(),
               body=[
                   Expr(
                       value=Await(
                           value=Call(
                               func=Name(id='other_func', ctx=Load()))))])])

class ast.AsyncFor(target, iter, body, orelse, type_comment)
class ast.AsyncWith(items, body, type_comment)

   Bucles "async for" y administradores de contexto "async with".
   Tienen los mismos campos que "For" y "With", respectivamente. Solo
   válido en el cuerpo de un "AsyncFunctionDef".

Nota:

  When a string is parsed by "ast.parse()", operator nodes (subclasses
  of "ast.operator", "ast.unaryop", "ast.cmpop", "ast.boolop" and
  "ast.expr_context") on the returned tree will be singletons. Changes
  to one will be reflected in all other occurrences of the same value
  (for example, "ast.Add").

## "ast" helpers

Apart from the node classes, the "ast" module defines these utility
functions and classes for traversing abstract syntax trees:

ast.parse(source, filename='<unknown>', mode='exec', *, type_comments=False, feature_version=None, optimize=-1)

   Parse the source into an AST node.  Equivalent to "compile(source,
   filename, mode, flags=FLAGS_VALUE, optimize=optimize)", where
   "FLAGS_VALUE" is "ast.PyCF_ONLY_AST" if "optimize <= 0" and
   "ast.PyCF_OPTIMIZED_AST" otherwise.

   If "type_comments=True" is given, the parser is modified to check
   and return type comments as specified by **PEP 484** and **PEP
   526**. This is equivalent to adding "ast.PyCF_TYPE_COMMENTS" to the
   flags passed to "compile()".  This will report syntax errors for
   misplaced type comments.  Without this flag, type comments will be
   ignored, and the "type_comment" field on selected AST nodes will
   always be "None".  In addition, the locations of "# type: ignore"
   comments will be returned as the "type_ignores" attribute of
   "Module" (otherwise it is always an empty list).

   Además, si "modo" es "'func_type'", la sintaxis de entrada se
   modifica para corresponder a **PEP 484** "comentarios de tipo de
   firma", por ejemplo "(str, int) -> List[str]".

   Setting "feature_version" to a tuple "(major, minor)" will result
   in a "best-effort" attempt to parse using that Python version's
   grammar. For example, setting "feature_version=(3, 9)" will attempt
   to disallow parsing of "match" statements. Currently "major" must
   equal to "3". The lowest supported version is "(3, 7)" (and this
   may increase in future Python versions); the highest is
   "sys.version_info[0:2]". "Best-effort" attempt means there is no
   guarantee that the parse (or success of the parse) is the same as
   when run on the Python version corresponding to "feature_version".

   If source contains a null character ("\0"), "ValueError" is raised.

   Advertencia:

     Tenga en cuenta que analizar correctamente el código fuente en un
     objeto AST no garantiza que el código fuente proporcionado sea un
     código Python válido que se pueda ejecutar, ya que el paso de
     compilación puede lanzar más excepciones "SyntaxError". Por
     ejemplo, la fuente "return 42" genera un nodo AST válido para una
     declaración de retorno, pero no se puede compilar solo (debe
     estar dentro de un nodo de función).En particular, "ast.parse()"
     no realizará ninguna verificación de alcance, lo que hace el paso
     de compilación.

   Advertencia:

     Es posible bloquear el intérprete de Python con una cadena de
     caracteres suficientemente grande/compleja debido a las
     limitaciones de profundidad de pila en el compilador AST de
     Python.

   Distinto en la versión 3.8: Se agregaron "type_comments",
   "mode='func_type'" y "feature_version".

   Distinto en la versión 3.13: The minimum supported version for
   "feature_version" is now "(3, 7)". The "optimize" argument was
   added.

ast.unparse(ast_obj)

   Analice un objeto "ast.AST" y genere una cadena con código que
   produciría un objeto "ast.AST" equivalente si se analiza con
   "ast.parse()".

   Advertencia:

     La cadena de código producida no será necesariamente igual al
     código original que generó el objeto "ast.AST" (sin ninguna
     optimización del compilador, como tuplas constantes /
     frozensets).

   Advertencia:

     Intentar descomprimir una expresión muy compleja daría como
     resultado "RecursionError".

   Added in version 3.9.

ast.literal_eval(node_or_string)

   Evalúa un nodo de expresión o una cadena de caracteres que contenga
   únicamente un literal de Python o visualizador de contenedor.  La
   cadena o nodo proporcionado sólo puede consistir en las siguientes
   estructuras literales de Python: cadenas de caracteres, bytes,
   números, tuplas, listas, diccionarios, conjuntos, booleanos, "None"
   y "Ellipsis".

   Esto se puede usar para evaluar de forma segura las cadenas de
   caracteres que contienen valores de Python sin la necesidad de
   analizar los valores uno mismo.  No es capaz de evaluar expresiones
   complejas arbitrariamente, por ejemplo, que involucran operadores o
   indexación.

   Esta función había sido documentada como "segura" en el pasado sin
   definir lo que eso significaba. Eso era engañoso. Está diseñada
   específicamente no para ejecutar código Python, a diferencia de la
   más general "eval()". No hay espacio de nombres, ni búsqueda de
   nombres, ni capacidad de llamada. Pero no está libre de ataques:
   Una entrada relativamente pequeña puede llevar a un agotamiento de
   la memoria o de la pila de C, haciendo colapsar el proceso. También
   existe la posibilidad de denegación de servicio por consumo
   excesivo de CPU en algunas entradas. Por lo tanto, no se recomienda
   llamarlo con datos no confiables.

   Advertencia:

     Es posible bloquear el intérprete de Python debido a las
     limitaciones de profundidad de pila en el compilador AST de
     Python.Puede generar "ValueError", "TypeError", "SyntaxError",
     "MemoryError" y "RecursionError" dependiendo de la entrada mal
     formada.

   Distinto en la versión 3.2: Ahora permite bytes y establece
   literales.

   Distinto en la versión 3.9: Ahora admite la creación de conjuntos
   vacíos con "'set()'".

   Distinto en la versión 3.10: Para las entradas de cadena, los
   espacios iniciales y las tabulaciones ahora se eliminan.

ast.get_docstring(node, clean=True)

   Retorna la cadena de caracteres de documentación del *node* dado
   (que debe ser un nodo "FunctionDef", "AsyncFunctionDef",
   "ClassDef", o "Module"), o "None" si no tiene docstring. Si *clean*
   es verdadero, limpia la sangría del docstring con
   "inspect.cleandoc()".

   Distinto en la versión 3.5: "AsyncFunctionDef" ahora está
   soportada.

ast.get_source_segment(source, node, *, padded=False)

   Get source code segment of the *source* that generated *node*. If
   some location information ("lineno", "end_lineno", "col_offset", or
   "end_col_offset") is missing, return "None".

   Si *padded* es "True", la primera línea de una declaración de
   varias líneas se rellenará con espacios para que coincidan con su
   posición original.

   Added in version 3.8.

ast.fix_missing_locations(node)

   When you compile a node tree with "compile()", the compiler expects
   "lineno" and "col_offset" attributes for every node that supports
   them.  This is rather tedious to fill in for generated nodes, so
   this helper adds these attributes recursively where not already
   set, by setting them to the values of the parent node.  It works
   recursively starting at *node*.

ast.increment_lineno(node, n=1)

   Incremente el número de línea y el número de línea final de cada
   nodo en el árbol comenzando en *node* por *n*. Esto es útil para
   "mover código" a una ubicación diferente en un archivo.

ast.copy_location(new_node, old_node)

   Copy source location ("lineno", "col_offset", "end_lineno", and
   "end_col_offset") from *old_node* to *new_node* if possible, and
   return *new_node*.

ast.iter_fields(node)

   Produce (*yield*) una tupla de "(fieldname, value)" para cada campo
   en "node._fields" que está presente en *node*.

ast.iter_child_nodes(node)

   Cede todos los nodos secundarios directos de *node*, es decir,
   todos los campos que son nodos y todos los elementos de campos que
   son listas de nodos.

ast.walk(node)

   Recursivamente produce todos los nodos descendientes en el árbol
   comenzando en *node* (incluido *node* en sí mismo), en ningún orden
   especificado. Esto es útil si solo desea modificar los nodos en su
   lugar y no le importa el contexto.

class ast.NodeVisitor

   Una clase base de visitante de nodo que recorre el árbol de
   sintaxis abstracta y llama a una función de visitante para cada
   nodo encontrado. Esta función puede retornar un valor que se
   reenvía mediante el método "visit()".

   Esta clase está destinada a ser subclase, con la subclase agregando
   métodos de visitante.

   visit(node)

      Visita un nodo. La implementación predeterminada llama al método
      llamado "self.visit_*classname*" donde *classname* es el nombre
      de la clase de nodo, o "generic_visit()" si ese método no
      existe.

   generic_visit(node)

      Este visitante llama "visit()" en todos los hijos del nodo.

      Tenga en cuenta que los nodos secundarios de los nodos que
      tienen un método de visitante personalizado no se visitarán a
      menos que el visitante llame "generic_visit()" o los visite a sí
      mismo.

   visit_Constant(node)

      Handles all constant nodes.

   No use "NodeVisitor" si desea aplicar cambios a los nodos durante
   el recorrido. Para esto existe un visitante especial
   ("NodeTransformer") que permite modificaciones.

   Deprecated since version 3.8, removed in version 3.14: Methods
   "visit_Num()", "visit_Str()", "visit_Bytes()",
   "visit_NameConstant()" and "visit_Ellipsis()" will not be called in
   Python 3.14+.  Add the "visit_Constant()" method instead to handle
   all constant nodes.

class ast.NodeTransformer

   Una subclase de "NodeVisitor" que recorre el árbol de sintaxis
   abstracta y permite la modificación de nodos.

   La clase "NodeTransformer" recorrerá el AST y usará el valor de
   retorno de los métodos del visitante para reemplazar o eliminar el
   nodo anterior. Si el valor de retorno del método de visitante es
   "None", el nodo se eliminará de su ubicación; de lo contrario, se
   reemplazará con el valor de retorno. El valor de retorno puede ser
   el nodo original, en cuyo caso no se realiza ningún reemplazo.

   Aquí hay un transformador de ejemplo que reescribe todas las
   apariciones de búsquedas de nombres ("foo") en "data['foo']":

      class RewriteName(NodeTransformer):

          def visit_Name(self, node):
              return Subscript(
                  value=Name(id='data', ctx=Load()),
                  slice=Constant(value=node.id),
                  ctx=node.ctx
              )

   Keep in mind that if the node you're operating on has child nodes
   you must either transform the child nodes yourself or call the
   "generic_visit()" method for the node first.

   Para los nodos que formaban parte de una colección de declaraciones
   (que se aplica a todos los nodos de declaración), el visitante
   también puede retornar una lista de nodos en lugar de solo un nodo.

   If "NodeTransformer" introduces new nodes (that weren't part of
   original tree) without giving them location information (such as
   "lineno"), "fix_missing_locations()" should be called with the new
   sub-tree to recalculate the location information:

      tree = ast.parse('foo', mode='eval')
      new_tree = fix_missing_locations(RewriteName().visit(tree))

   Usualmente usas el transformador así:

      node = YourTransformer().visit(node)

ast.dump(node, annotate_fields=True, include_attributes=False, *, indent=None, show_empty=False)

   Retorna un volcado formateado del árbol en *node*. Esto es
   principalmente útil para propósitos de depuración. Si
   *annotate_fields* es verdadero (por defecto), la cadena de
   caracteres retornada mostrará los nombres y los valores de los
   campos. Si *annotate_fields* es falso, la cadena de resultados será
   más compacta omitiendo nombres de campo no ambiguos. Los atributos
   como los números de línea y las compensaciones de columna no se
   vuelcan de forma predeterminada. Si esto se desea,
   *include_attributes* se puede establecer en verdadero.

   Si *indent* es un entero no negativo o una cadena de caracteres,
   entonces el árbol será impreso de forma linda con ese nivel de
   sangría.  Un nivel de sangría de 0, negativo, o """" solo insertará
   nuevas líneas. "None" (el valor por defecto) selecciona la
   representación de línea simple. Al usar un entero positivo se
   sangrará esa cantidad de espacios como sangría.  Si *indent* es una
   cadena de caracteres (como ""\t""), esa cadena se usa para sangrar
   cada nivel.

   If *show_empty* is false (the default), optional empty lists will
   be omitted from the output. Optional "None" values are always
   omitted.

   Distinto en la versión 3.9: Añadida la opción *indent*.

   Distinto en la versión 3.13: Added the *show_empty* option.

      >>> print(ast.dump(ast.parse("""\
      ... async def f():
      ...     await other_func()
      ... """), indent=4, show_empty=True))
      Module(
          body=[
              AsyncFunctionDef(
                  name='f',
                  args=arguments(
                      posonlyargs=[],
                      args=[],
                      kwonlyargs=[],
                      kw_defaults=[],
                      defaults=[]),
                  body=[
                      Expr(
                          value=Await(
                              value=Call(
                                  func=Name(id='other_func', ctx=Load()),
                                  args=[],
                                  keywords=[])))],
                  decorator_list=[],
                  type_params=[])],
          type_ignores=[])

ast.compare(a, b, /, *, compare_attributes=False)

   Recursively compares two ASTs.

   *compare_attributes* affects whether AST attributes are considered
   in the comparison. If *compare_attributes* is "False" (default),
   then attributes are ignored. Otherwise they must all be equal. This
   option is useful to check whether the ASTs are structurally equal
   but differ in whitespace or similar details. Attributes include
   line numbers and column offsets.

   Added in version 3.14.

## Compiler flags

Los siguientes indicadores pueden pasarse a "compile()" para cambiar
los efectos en la compilación de un programa:

ast.PyCF_ALLOW_TOP_LEVEL_AWAIT

   Habilita el soporte para "await", "async for", "async with" y
   comprensiones asíncronas de nivel superior.

   Added in version 3.8.

ast.PyCF_ONLY_AST

   Genera y retorna un árbol de sintaxis abstracto en lugar de
   retornar un objeto de código compilado.

ast.PyCF_OPTIMIZED_AST

   The returned AST is optimized according to the *optimize* argument
   in "compile()" or "ast.parse()".

   Added in version 3.13.

ast.PyCF_TYPE_COMMENTS

   Habilita el soporte para comentarios de tipo de estilo **PEP 484**
   y **PEP 526** ("# type: <type>", "# type: ignore <stuff>").

   Added in version 3.8.

## Command-line usage

Added in version 3.9.

The "ast" module can be executed as a script from the command line. It
is as simple as:

   python -m ast [-m <mode>] [-a] [infile]

Las siguientes opciones son aceptadas:

-h, --help

   Muestra el mensaje de ayuda y sale.

-m <mode>
--mode <mode>

   Especifica qué tipo de código debe ser compilado, como el argumento
   *mode* en "parse()".

--no-type-comments

   No analizar los comentarios de tipo.

-a, --include-attributes

   Incluye atributos como números de línea y sangrías.

-i <indent>
--indent <indent>

   Sangría de nodos en AST (número de espacios).

--feature-version <version>

   Python version in the format 3.x (for example, 3.10). Defaults to
   the current version of the interpreter.

   Added in version 3.14.

-O <level>
--optimize <level>

   Optimization level for parser. Defaults to no optimization.

   Added in version 3.14.

--show-empty

   Show empty lists and fields that are "None". Defaults to not
   showing empty objects.

   Added in version 3.14.

Si "infile" es especificado, su contenido es analizado a AST y
mostrado en stdout. De otra forma, el contenido es leído desde stdin.

Ver también:

  Green Tree Snakes, un recurso de documentación externo, tiene buenos
  detalles sobre cómo trabajar con Python AST.

  ASTTokens anota ASTs de Python con la posición de tokens y texto en
  el código fuente que los genera. Esto es de ayuda para herramientas
  que hacen transformaciones de código fuente.

  leoAst.py unifies the token-based and parse-tree-based views of
  python programs by inserting two-way links between tokens and ast
  nodes.

  LibCST analiza código como Árboles de Sintaxis Concreta que se ven
  como ASTs y mantienen todos los detalles de formato. Es útil para
  construir herramientas de refactor automáticas y linters.

  Parso is a Python parser that supports error recovery and round-trip
  parsing for different Python versions (in multiple Python versions).
  Parso is also able to list multiple syntax errors in your Python
  file.
