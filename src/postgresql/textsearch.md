---
title: Full Text Search
source_url: https://www.postgresql.org/docs/17/textsearch.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: textsearch.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 3660
---

## Full Text Search

full text search

text search

## Introduction

Full Text Searching (or just text search) provides the capability to identify natural-language documents that satisfy a query, and optionally to sort them by relevance to the query. The most common type of search is to find all documents containing given query terms and return them in order of their similarity to the query. Notions of `query` and `similarity` are very flexible and depend on the specific application. The simplest search considers `query` as a set of words and `similarity` as the frequency of query words in the document.

Textual search operators have existed in databases for years. PostgreSQL has `~`, `~*`, `LIKE`, and `ILIKE` operators for textual data types, but they lack many essential properties required by modern information systems:

- There is no linguistic support, even for English. Regular expressions are not sufficient because they cannot easily handle derived words, e.g., `satisfies` and `satisfy`. You might miss documents that contain `satisfies`, although you probably would like to find them when searching for `satisfy`. It is possible to use `OR` to search for multiple derived forms, but this is tedious and error-prone (some words can have several thousand derivatives).
- They provide no ordering (ranking) of search results, which makes them ineffective when thousands of matching documents are found.
- They tend to be slow because there is no index support, so they must process all documents for every search.

Full text indexing allows documents to be *preprocessed* and an index saved for later rapid searching. Preprocessing includes:

- *Parsing documents into tokens*. It is useful to identify various classes of tokens, e.g., numbers, words, complex words, email addresses, so that they can be processed differently. In principle token classes depend on the specific application, but for most purposes it is adequate to use a predefined set of classes. PostgreSQL uses a parser to perform this step. A standard parser is provided, and custom parsers can be created for specific needs.

- *Converting tokens into lexemes*. A lexeme is a string, just like a token, but it has been normalized so that different forms of the same word are made alike. For example, normalization almost always includes folding upper-case letters to lower-case, and often involves removal of suffixes (such as `s` or `es` in English). This allows searches to find variant forms of the same word, without tediously entering all the possible variants. Also, this step typically eliminates stop words, which are words that are so common that they are useless for searching. (In short, then, tokens are raw fragments of the document text, while lexemes are words that are believed useful for indexing and searching.) PostgreSQL uses dictionaries to perform this step. Various standard dictionaries are provided, and custom ones can be created for specific needs.

- *Storing preprocessed documents optimized for searching*. For example, each document can be represented as a sorted array of normalized lexemes. Along with the lexemes it is often desirable to store positional information to use for proximity ranking, so that a document that contains a more “dense” region of query words is assigned a higher rank than one with scattered query words.

Dictionaries allow fine-grained control over how tokens are normalized. With appropriate dictionaries, you can:

- Define stop words that should not be indexed.
- Map synonyms to a single word using Ispell.
- Map phrases to a single word using a thesaurus.
- Map different variations of a word to a canonical form using an Ispell dictionary.
- Map different variations of a word to a canonical form using Snowball stemmer rules.

A data type `tsvector` is provided for storing preprocessed documents, along with a type `tsquery` for representing processed queries ([???](#datatype-textsearch)). There are many functions and operators available for these data types ([???](#functions-textsearch)), the most important of which is the match operator `@@`, which we introduce in [Basic Text Matching](#textsearch-matching). Full text searches can be accelerated using indexes ([Preferred Index Types for Text Search](#textsearch-indexes)).

### What Is a Document?

document

text search

A document is the unit of searching in a full text search system; for example, a magazine article or email message. The text search engine must be able to parse documents and store associations of lexemes (key words) with their parent document. Later, these associations are used to search for documents that contain query words.

For searches within PostgreSQL, a document is normally a textual field within a row of a database table, or possibly a combination (concatenation) of such fields, perhaps stored in several tables or obtained dynamically. In other words, a document can be constructed from different parts for indexing and it might not be stored anywhere as a whole. For example:

    SELECT title || ' ' ||  author || ' ' ||  abstract || ' ' || body AS document
    FROM messages
    WHERE mid = 12;

    SELECT m.title || ' ' || m.author || ' ' || m.abstract || ' ' || d.body AS document
    FROM messages m, docs d
    WHERE m.mid = d.did AND m.mid = 12;

> [!NOTE]
> Actually, in these example queries, `coalesce` should be used to prevent a single `NULL` attribute from causing a `NULL` result for the whole document.

Another possibility is to store the documents as simple text files in the file system. In this case, the database can be used to store the full text index and to execute searches, and some unique identifier can be used to retrieve the document from the file system. However, retrieving files from outside the database requires superuser permissions or special function support, so this is usually less convenient than keeping all the data inside PostgreSQL. Also, keeping everything inside the database allows easy access to document metadata to assist in indexing and display.

For text search purposes, each document must be reduced to the preprocessed `tsvector` format. Searching and ranking are performed entirely on the `tsvector` representation of a document the original text need only be retrieved when the document has been selected for display to a user. We therefore often speak of the `tsvector` as being the document, but of course it is only a compact representation of the full document.

### Basic Text Matching

Full text searching in PostgreSQL is based on the match operator `@@`, which returns `true` if a `tsvector` (document) matches a `tsquery` (query). It doesn't matter which data type is written first:

    SELECT 'a fat cat sat on a mat and ate a fat rat'::tsvector @@ 'cat & rat'::tsquery;
     ?column?
    ----------
     t

    SELECT 'fat & cow'::tsquery @@ 'a fat cat sat on a mat and ate a fat rat'::tsvector;
     ?column?
    ----------
     f

As the above example suggests, a `tsquery` is not just raw text, any more than a `tsvector` is. A `tsquery` contains search terms, which must be already-normalized lexemes, and may combine multiple terms using AND, OR, NOT, and FOLLOWED BY operators. (For syntax details see [???](#datatype-tsquery).) There are functions `to_tsquery`, `plainto_tsquery`, and `phraseto_tsquery` that are helpful in converting user-written text into a proper `tsquery`, primarily by normalizing words appearing in the text. Similarly, `to_tsvector` is used to parse and normalize a document string. So in practice a text search match would look more like this:

    SELECT to_tsvector('fat cats ate fat rats') @@ to_tsquery('fat & rat');
     ?column?
    ----------
     t

Observe that this match would not succeed if written as

    SELECT 'fat cats ate fat rats'::tsvector @@ to_tsquery('fat & rat');
     ?column?
    ----------
     f

since here no normalization of the word `rats` will occur. The elements of a `tsvector` are lexemes, which are assumed already normalized, so `rats` does not match `rat`.

The `@@` operator also supports `text` input, allowing explicit conversion of a text string to `tsvector` or `tsquery` to be skipped in simple cases. The variants available are:

    tsvector @@ tsquery
    tsquery  @@ tsvector
    text @@ tsquery
    text @@ text

The first two of these we saw already. The form `text` `@@` `tsquery` is equivalent to `to_tsvector(x) @@ y`. The form `text` `@@` `text` is equivalent to `to_tsvector(x) @@ plainto_tsquery(y)`.

Within a `tsquery`, the `&` (AND) operator specifies that both its arguments must appear in the document to have a match. Similarly, the `|` (OR) operator specifies that at least one of its arguments must appear, while the `!` (NOT) operator specifies that its argument must *not* appear in order to have a match. For example, the query `fat & ! rat` matches documents that contain `fat` but not `rat`.

Searching for phrases is possible with the help of the `<->` (FOLLOWED BY) `tsquery` operator, which matches only if its arguments have matches that are adjacent and in the given order. For example:

    SELECT to_tsvector('fatal error') @@ to_tsquery('fatal <-> error');
     ?column?
    ----------
     t

    SELECT to_tsvector('error is not fatal') @@ to_tsquery('fatal <-> error');
     ?column?
    ----------
     f

There is a more general version of the FOLLOWED BY operator having the form `<N>`, where \<N\> is an integer standing for the difference between the positions of the matching lexemes. `<1>` is the same as `<->`, while `<2>` allows exactly one other lexeme to appear between the matches, and so on. The `phraseto_tsquery` function makes use of this operator to construct a `tsquery` that can match a multi-word phrase when some of the words are stop words. For example:

    SELECT phraseto_tsquery('cats ate rats');
           phraseto_tsquery
    -------------------------------
     'cat' <-> 'ate' <-> 'rat'

    SELECT phraseto_tsquery('the cats ate the rats');
           phraseto_tsquery
    -------------------------------
     'cat' <-> 'ate' <2> 'rat'

A special case that's sometimes useful is that `<0>` can be used to require that two patterns match the same word.

Parentheses can be used to control nesting of the `tsquery` operators. Without parentheses, `|` binds least tightly, then `&`, then `<->`, and `!` most tightly.

It's worth noticing that the AND/OR/NOT operators mean something subtly different when they are within the arguments of a FOLLOWED BY operator than when they are not, because within FOLLOWED BY the exact position of the match is significant. For example, normally `!x` matches only documents that do not contain `x` anywhere. But `!x <-> y` matches `y` if it is not immediately after an `x`; an occurrence of `x` elsewhere in the document does not prevent a match. Another example is that `x & y` normally only requires that `x` and `y` both appear somewhere in the document, but `(x & y) <-> z` requires `x` and `y` to match at the same place, immediately before a `z`. Thus this query behaves differently from `x <-> z & y <-> z`, which will match a document containing two separate sequences `x z` and `y z`. (This specific query is useless as written, since `x` and `y` could not match at the same place; but with more complex situations such as prefix-match patterns, a query of this form could be useful.)

### Configurations

The above are all simple text search examples. As mentioned before, full text search functionality includes the ability to do many more things: skip indexing certain words (stop words), process synonyms, and use sophisticated parsing, e.g., parse based on more than just white space. This functionality is controlled by text search configurations. PostgreSQL comes with predefined configurations for many languages, and you can easily create your own configurations. (psql's `\dF` command shows all available configurations.)

During installation an appropriate configuration is selected and [???](#guc-default-text-search-config) is set accordingly in `postgresql.conf`. If you are using the same text search configuration for the entire cluster you can use the value in `postgresql.conf`. To use different configurations throughout the cluster but the same configuration within any one database, use `ALTER DATABASE ... SET`. Otherwise, you can set `default_text_search_config` in each session.

Each text search function that depends on a configuration has an optional `regconfig` argument, so that the configuration to use can be specified explicitly. `default_text_search_config` is used only when this argument is omitted.

To make it easier to build custom text search configurations, a configuration is built up from simpler database objects. PostgreSQL's text search facility provides four types of configuration-related database objects:

- Text search parsers break documents into tokens and classify each token (for example, as words or numbers).
- Text search dictionaries convert tokens to normalized form and reject stop words.
- Text search templates provide the functions underlying dictionaries. (A dictionary simply specifies a template and a set of parameters for the template.)
- Text search configurations select a parser and a set of dictionaries to use to normalize the tokens produced by the parser.

Text search parsers and templates are built from low-level C functions; therefore it requires C programming ability to develop new ones, and superuser privileges to install one into a database. (There are examples of add-on parsers and templates in the `contrib/` area of the PostgreSQL distribution.) Since dictionaries and configurations just parameterize and connect together some underlying parsers and templates, no special privilege is needed to create a new dictionary or configuration. Examples of creating custom dictionaries and configurations appear later in this chapter.

## Tables and Indexes

The examples in the previous section illustrated full text matching using simple constant strings. This section shows how to search table data, optionally using indexes.

### Searching a Table

It is possible to do a full text search without an index. A simple query to print the title of each row that contains the word `friend` in its body field is:

    SELECT title
    FROM pgweb
    WHERE to_tsvector('english', body) @@ to_tsquery('english', 'friend');

This will also find related words such as `friends` and `friendly`, since all these are reduced to the same normalized lexeme.

The query above specifies that the `english` configuration is to be used to parse and normalize the strings. Alternatively we could omit the configuration parameters:

    SELECT title
    FROM pgweb
    WHERE to_tsvector(body) @@ to_tsquery('friend');

This query will use the configuration set by [???](#guc-default-text-search-config).

A more complex example is to select the ten most recent documents that contain `create` and `table` in the title or body:

    SELECT title
    FROM pgweb
    WHERE to_tsvector(title || ' ' || body) @@ to_tsquery('create & table')
    ORDER BY last_mod_date DESC
    LIMIT 10;

For clarity we omitted the `coalesce` function calls which would be needed to find rows that contain `NULL` in one of the two fields.

Although these queries will work without an index, most applications will find this approach too slow, except perhaps for occasional ad-hoc searches. Practical use of text searching usually requires creating an index.

### Creating Indexes

We can create a GIN index ([Preferred Index Types for Text Search](#textsearch-indexes)) to speed up text searches:

    CREATE INDEX pgweb_idx ON pgweb USING GIN (to_tsvector('english', body));

Notice that the 2-argument version of `to_tsvector` is used. Only text search functions that specify a configuration name can be used in expression indexes ([???](#indexes-expressional)). This is because the index contents must be unaffected by [???](#guc-default-text-search-config). If they were affected, the index contents might be inconsistent because different entries could contain `tsvector`s that were created with different text search configurations, and there would be no way to guess which was which. It would be impossible to dump and restore such an index correctly.

Because the two-argument version of `to_tsvector` was used in the index above, only a query reference that uses the 2-argument version of `to_tsvector` with the same configuration name will use that index. That is, `WHERE to_tsvector('english', body) @@ 'a & b'` can use the index, but `WHERE to_tsvector(body) @@ 'a & b'` cannot. This ensures that an index will be used only with the same configuration used to create the index entries.

It is possible to set up more complex expression indexes wherein the configuration name is specified by another column, e.g.:

    CREATE INDEX pgweb_idx ON pgweb USING GIN (to_tsvector(config_name, body));

where `config_name` is a column in the `pgweb` table. This allows mixed configurations in the same index while recording which configuration was used for each index entry. This would be useful, for example, if the document collection contained documents in different languages. Again, queries that are meant to use the index must be phrased to match, e.g., `WHERE to_tsvector(config_name, body) @@ 'a & b'`.

Indexes can even concatenate columns:

    CREATE INDEX pgweb_idx ON pgweb USING GIN (to_tsvector('english', title || ' ' || body));

Another approach is to create a separate `tsvector` column to hold the output of `to_tsvector`. To keep this column automatically up to date with its source data, use a stored generated column. This example is a concatenation of `title` and `body`, using `coalesce` to ensure that one field will still be indexed when the other is `NULL`:

    ALTER TABLE pgweb
        ADD COLUMN textsearchable_index_col tsvector
                   GENERATED ALWAYS AS (to_tsvector('english', coalesce(title, '') || ' ' || coalesce(body, ''))) STORED;

Then we create a GIN index to speed up the search:

    CREATE INDEX textsearch_idx ON pgweb USING GIN (textsearchable_index_col);

Now we are ready to perform a fast full text search:

    SELECT title
    FROM pgweb
    WHERE textsearchable_index_col @@ to_tsquery('create & table')
    ORDER BY last_mod_date DESC
    LIMIT 10;

One advantage of the separate-column approach over an expression index is that it is not necessary to explicitly specify the text search configuration in queries in order to make use of the index. As shown in the example above, the query can depend on `default_text_search_config`. Another advantage is that searches will be faster, since it will not be necessary to redo the `to_tsvector` calls to verify index matches. (This is more important when using a GiST index than a GIN index; see [Preferred Index Types for Text Search](#textsearch-indexes).) The expression-index approach is simpler to set up, however, and it requires less disk space since the `tsvector` representation is not stored explicitly.

## Controlling Text Search

To implement full text searching there must be a function to create a `tsvector` from a document and a `tsquery` from a user query. Also, we need to return results in a useful order, so we need a function that compares documents with respect to their relevance to the query. It's also important to be able to display the results nicely. PostgreSQL provides support for all of these functions.

### Parsing Documents

PostgreSQL provides the function `to_tsvector` for converting a document to the `tsvector` data type.

to_tsvector

to_tsvector(

config

regconfig

,

document

text

) returns

tsvector

`to_tsvector` parses a textual document into tokens, reduces the tokens to lexemes, and returns a `tsvector` which lists the lexemes together with their positions in the document. The document is processed according to the specified or default text search configuration. Here is a simple example:

    SELECT to_tsvector('english', 'a fat  cat sat on a mat - it ate a fat rats');
                      to_tsvector
    -----------------------------------------------------
     'ate':9 'cat':3 'fat':2,11 'mat':7 'rat':12 'sat':4

In the example above we see that the resulting `tsvector` does not contain the words `a`, `on`, or `it`, the word `rats` became `rat`, and the punctuation sign `-` was ignored.

The `to_tsvector` function internally calls a parser which breaks the document text into tokens and assigns a type to each token. For each token, a list of dictionaries ([Dictionaries](#textsearch-dictionaries)) is consulted, where the list can vary depending on the token type. The first dictionary that recognizes the token emits one or more normalized lexemes to represent the token. For example, `rats` became `rat` because one of the dictionaries recognized that the word `rats` is a plural form of `rat`. Some words are recognized as stop words ([Stop Words](#textsearch-stopwords)), which causes them to be ignored since they occur too frequently to be useful in searching. In our example these are `a`, `on`, and `it`. If no dictionary in the list recognizes the token then it is also ignored. In this example that happened to the punctuation sign `-` because there are in fact no dictionaries assigned for its token type (`Space symbols`), meaning space tokens will never be indexed. The choices of parser, dictionaries and which types of tokens to index are determined by the selected text search configuration ([Configuration Example](#textsearch-configuration)). It is possible to have many different configurations in the same database, and predefined configurations are available for various languages. In our example we used the default configuration `english` for the English language.

The function `setweight` can be used to label the entries of a `tsvector` with a given weight, where a weight is one of the letters `A`, `B`, `C`, or `D`. This is typically used to mark entries coming from different parts of a document, such as title versus body. Later, this information can be used for ranking of search results.

Because `to_tsvector`(`NULL`) will return `NULL`, it is recommended to use `coalesce` whenever a field might be null. Here is the recommended method for creating a `tsvector` from a structured document:

    UPDATE tt SET ti =
        setweight(to_tsvector(coalesce(title,'')), 'A')    ||
        setweight(to_tsvector(coalesce(keyword,'')), 'B')  ||
        setweight(to_tsvector(coalesce(abstract,'')), 'C') ||
        setweight(to_tsvector(coalesce(body,'')), 'D');

Here we have used `setweight` to label the source of each lexeme in the finished `tsvector`, and then merged the labeled `tsvector` values using the `tsvector` concatenation operator `||`. ([Manipulating Documents](#textsearch-manipulate-tsvector) gives details about these operations.)

### Parsing Queries

PostgreSQL provides the functions `to_tsquery`, `plainto_tsquery`, `phraseto_tsquery` and `websearch_to_tsquery` for converting a query to the `tsquery` data type. `to_tsquery` offers access to more features than either `plainto_tsquery` or `phraseto_tsquery`, but it is less forgiving about its input. `websearch_to_tsquery` is a simplified version of `to_tsquery` with an alternative syntax, similar to the one used by web search engines.

to_tsquery

to_tsquery(

config

regconfig

,

querytext

text

) returns

tsquery

`to_tsquery` creates a `tsquery` value from \<querytext\>, which must consist of single tokens separated by the `tsquery` operators `&` (AND), `|` (OR), `!` (NOT), and `<->` (FOLLOWED BY), possibly grouped using parentheses. In other words, the input to `to_tsquery` must already follow the general rules for `tsquery` input, as described in [???](#datatype-tsquery). The difference is that while basic `tsquery` input takes the tokens at face value, `to_tsquery` normalizes each token into a lexeme using the specified or default configuration, and discards any tokens that are stop words according to the configuration. For example:

    SELECT to_tsquery('english', 'The & Fat & Rats');
      to_tsquery
    ---------------
     'fat' & 'rat'

As in basic `tsquery` input, weight(s) can be attached to each lexeme to restrict it to match only `tsvector` lexemes of those weight(s). For example:

    SELECT to_tsquery('english', 'Fat | Rats:AB');
        to_tsquery
    ------------------
     'fat' | 'rat':AB

Also, `*` can be attached to a lexeme to specify prefix matching:

    SELECT to_tsquery('supern:*A & star:A*B');
            to_tsquery
    --------------------------
     'supern':*A & 'star':*AB

Such a lexeme will match any word in a `tsvector` that begins with the given string.

`to_tsquery` can also accept single-quoted phrases. This is primarily useful when the configuration includes a thesaurus dictionary that may trigger on such phrases. In the example below, a thesaurus contains the rule `supernovae stars : sn`:

    SELECT to_tsquery('''supernovae stars'' & !crab');
      to_tsquery
    ---------------
     'sn' & !'crab'

Without quotes, `to_tsquery` will generate a syntax error for tokens that are not separated by an AND, OR, or FOLLOWED BY operator.

plainto_tsquery

plainto_tsquery(

config

regconfig

,

querytext

text

) returns

tsquery

`plainto_tsquery` transforms the unformatted text \<querytext\> to a `tsquery` value. The text is parsed and normalized much as for `to_tsvector`, then the `&` (AND) `tsquery` operator is inserted between surviving words.

Example:

    SELECT plainto_tsquery('english', 'The Fat Rats');
     plainto_tsquery
    -----------------
     'fat' & 'rat'

Note that `plainto_tsquery` will not recognize `tsquery` operators, weight labels, or prefix-match labels in its input:

    SELECT plainto_tsquery('english', 'The Fat & Rats:C');
       plainto_tsquery
    ---------------------
     'fat' & 'rat' & 'c'

Here, all the input punctuation was discarded.

phraseto_tsquery

phraseto_tsquery(

config

regconfig

,

querytext

text

) returns

tsquery

`phraseto_tsquery` behaves much like `plainto_tsquery`, except that it inserts the `<->` (FOLLOWED BY) operator between surviving words instead of the `&` (AND) operator. Also, stop words are not simply discarded, but are accounted for by inserting `<N>` operators rather than `<->` operators. This function is useful when searching for exact lexeme sequences, since the FOLLOWED BY operators check lexeme order not just the presence of all the lexemes.

Example:

    SELECT phraseto_tsquery('english', 'The Fat Rats');
     phraseto_tsquery
    ------------------
     'fat' <-> 'rat'

Like `plainto_tsquery`, the `phraseto_tsquery` function will not recognize `tsquery` operators, weight labels, or prefix-match labels in its input:

    SELECT phraseto_tsquery('english', 'The Fat & Rats:C');
          phraseto_tsquery
    -----------------------------
     'fat' <-> 'rat' <-> 'c'

websearch_to_tsquery(

config

regconfig

,

querytext

text

) returns

tsquery

`websearch_to_tsquery` creates a `tsquery` value from \<querytext\> using an alternative syntax in which simple unformatted text is a valid query. Unlike `plainto_tsquery` and `phraseto_tsquery`, it also recognizes certain operators. Moreover, this function will never raise syntax errors, which makes it possible to use raw user-supplied input for search. The following syntax is supported:

- `unquoted text`: text not inside quote marks will be converted to terms separated by `&` operators, as if processed by `plainto_tsquery`.
- `"quoted text"`: text inside quote marks will be converted to terms separated by `<->` operators, as if processed by `phraseto_tsquery`.
- `OR`: the word “or” will be converted to the `|` operator.
- `-`: a dash will be converted to the `!` operator.

Other punctuation is ignored. So like `plainto_tsquery` and `phraseto_tsquery`, the `websearch_to_tsquery` function will not recognize `tsquery` operators, weight labels, or prefix-match labels in its input.

Examples:

    SELECT websearch_to_tsquery('english', 'The fat rats');
     websearch_to_tsquery
    ----------------------
     'fat' & 'rat'
    (1 row)

    SELECT websearch_to_tsquery('english', '"supernovae stars" -crab');
           websearch_to_tsquery
    ----------------------------------
     'supernova' <-> 'star' & !'crab'
    (1 row)

    SELECT websearch_to_tsquery('english', '"sad cat" or "fat rat"');
           websearch_to_tsquery
    -----------------------------------
     'sad' <-> 'cat' | 'fat' <-> 'rat'
    (1 row)

    SELECT websearch_to_tsquery('english', 'signal -"segmentation fault"');
             websearch_to_tsquery
    ---------------------------------------
     'signal' & !( 'segment' <-> 'fault' )
    (1 row)

    SELECT websearch_to_tsquery('english', '""" )( dummy \\ query <->');
     websearch_to_tsquery
    ----------------------
     'dummi' & 'queri'
    (1 row)

### Ranking Search Results

Ranking attempts to measure how relevant documents are to a particular query, so that when there are many matches the most relevant ones can be shown first. PostgreSQL provides two predefined ranking functions, which take into account lexical, proximity, and structural information; that is, they consider how often the query terms appear in the document, how close together the terms are in the document, and how important is the part of the document where they occur. However, the concept of relevancy is vague and very application-specific. Different applications might require additional information for ranking, e.g., document modification time. The built-in ranking functions are only examples. You can write your own ranking functions and/or combine their results with additional factors to fit your specific needs.

The two ranking functions currently available are:

<span class="indexterm"></span> `ts_rank( weights float4[], vector tsvector, query tsquery , normalization integer ) returns float4`  
Ranks vectors based on the frequency of their matching lexemes.

<span class="indexterm"></span> `ts_rank_cd( weights float4[], vector tsvector, query tsquery , normalization integer ) returns float4`  
This function computes the cover density ranking for the given document vector and query, as described in Clarke, Cormack, and Tudhope's "Relevance Ranking for One to Three Term Queries" in the journal "Information Processing and Management", 1999. Cover density is similar to `ts_rank` ranking except that the proximity of matching lexemes to each other is taken into consideration.

This function requires lexeme positional information to perform its calculation. Therefore, it ignores any “stripped” lexemes in the `tsvector`. If there are no unstripped lexemes in the input, the result will be zero. (See [Manipulating Documents](#textsearch-manipulate-tsvector) for more information about the `strip` function and positional information in `tsvector`s.)

For both these functions, the optional \<weights\> argument offers the ability to weigh word instances more or less heavily depending on how they are labeled. The weight arrays specify how heavily to weigh each category of word, in the order: {D-weight, C-weight, B-weight, A-weight} If no \<weights\> are provided, then these defaults are used:

    {0.1, 0.2, 0.4, 1.0}

Typically weights are used to mark words from special areas of the document, like the title or an initial abstract, so they can be treated with more or less importance than words in the document body.

Since a longer document has a greater chance of containing a query term it is reasonable to take into account document size, e.g., a hundred-word document with five instances of a search word is probably more relevant than a thousand-word document with five instances. Both ranking functions take an integer \<normalization\> option that specifies whether and how a document's length should impact its rank. The integer option controls several behaviors, so it is a bit mask: you can specify one or more behaviors using `|` (for example, `2|4`).

- 0 (the default) ignores the document length
- 1 divides the rank by 1 + the logarithm of the document length
- 2 divides the rank by the document length
- 4 divides the rank by the mean harmonic distance between extents (this is implemented only by `ts_rank_cd`)
- 8 divides the rank by the number of unique words in document
- 16 divides the rank by 1 + the logarithm of the number of unique words in document
- 32 divides the rank by itself + 1

If more than one flag bit is specified, the transformations are applied in the order listed.

It is important to note that the ranking functions do not use any global information, so it is impossible to produce a fair normalization to 1% or 100% as sometimes desired. Normalization option 32 (`rank/(rank+1)`) can be applied to scale all ranks into the range zero to one, but of course this is just a cosmetic change; it will not affect the ordering of the search results.

Here is an example that selects only the ten highest-ranked matches:

    SELECT title, ts_rank_cd(textsearch, query) AS rank
    FROM apod, to_tsquery('neutrino|(dark & matter)') query
    WHERE query @@ textsearch
    ORDER BY rank DESC
    LIMIT 10;
                         title                     |   rank
    -----------------------------------------------+----------
     Neutrinos in the Sun                          |      3.1
     The Sudbury Neutrino Detector                 |      2.4
     A MACHO View of Galactic Dark Matter          |  2.01317
     Hot Gas and Dark Matter                       |  1.91171
     The Virgo Cluster: Hot Plasma and Dark Matter |  1.90953
     Rafting for Solar Neutrinos                   |      1.9
     NGC 4650A: Strange Galaxy and Dark Matter     |  1.85774
     Hot Gas and Dark Matter                       |   1.6123
     Ice Fishing for Cosmic Neutrinos              |      1.6
     Weak Lensing Distorts the Universe            | 0.818218

This is the same example using normalized ranking:

    SELECT title, ts_rank_cd(textsearch, query, 32 /* rank/(rank+1) */ ) AS rank
    FROM apod, to_tsquery('neutrino|(dark & matter)') query
    WHERE  query @@ textsearch
    ORDER BY rank DESC
    LIMIT 10;
                         title                     |        rank
    -----------------------------------------------+-------------------
     Neutrinos in the Sun                          | 0.756097569485493
     The Sudbury Neutrino Detector                 | 0.705882361190954
     A MACHO View of Galactic Dark Matter          | 0.668123210574724
     Hot Gas and Dark Matter                       |  0.65655958650282
     The Virgo Cluster: Hot Plasma and Dark Matter | 0.656301290640973
     Rafting for Solar Neutrinos                   | 0.655172410958162
     NGC 4650A: Strange Galaxy and Dark Matter     | 0.650072921219637
     Hot Gas and Dark Matter                       | 0.617195790024749
     Ice Fishing for Cosmic Neutrinos              | 0.615384618911517
     Weak Lensing Distorts the Universe            | 0.450010798361481

Ranking can be expensive since it requires consulting the `tsvector` of each matching document, which can be I/O bound and therefore slow. Unfortunately, it is almost impossible to avoid since practical queries often result in large numbers of matches.

### Highlighting Results

To present search results it is ideal to show a part of each document and how it is related to the query. Usually, search engines show fragments of the document with marked search terms. PostgreSQL provides a function `ts_headline` that implements this functionality.

ts_headline

ts_headline(

config

regconfig

,

document

text

,

query

tsquery

,

options

text

) returns

text

`ts_headline` accepts a document along with a query, and returns an excerpt from the document in which terms from the query are highlighted. Specifically, the function will use the query to select relevant text fragments, and then highlight all words that appear in the query, even if those word positions do not match the query's restrictions. The configuration to be used to parse the document can be specified by \<config\>; if \<config\> is omitted, the `default_text_search_config` configuration is used.

If an \<options\> string is specified it must consist of a comma-separated list of one or more \<option\>`=`\<value\> pairs. The available options are:

- `MaxWords`, `MinWords` (integers): these numbers determine the longest and shortest headlines to output. The default values are 35 and 15.
- `ShortWord` (integer): words of this length or less will be dropped at the start and end of a headline, unless they are query terms. The default value of three eliminates common English articles.
- `HighlightAll` (boolean): if `true` the whole document will be used as the headline, ignoring the preceding three parameters. The default is `false`.
- `MaxFragments` (integer): maximum number of text fragments to display. The default value of zero selects a non-fragment-based headline generation method. A value greater than zero selects fragment-based headline generation (see below).
- `StartSel`, `StopSel` (strings): the strings with which to delimit query words appearing in the document, to distinguish them from other excerpted words. The default values are “`<b>`” and “`</b>`”, which can be suitable for HTML output (but see the warning below).
- `FragmentDelimiter` (string): When more than one fragment is displayed, the fragments will be separated by this string. The default is “`...`”.

> [!WARNING]
> The output from `ts_headline` is not guaranteed to be safe for direct inclusion in web pages. When `HighlightAll` is `false` (the default), some simple XML tags are removed from the document, but this is not guaranteed to remove all HTML markup. Therefore, this does not provide an effective defense against attacks such as cross-site scripting (XSS) attacks, when working with untrusted input. To guard against such attacks, all HTML markup should be removed from the input document, or an HTML sanitizer should be used on the output.

These option names are recognized case-insensitively. You must double-quote string values if they contain spaces or commas.

In non-fragment-based headline generation, `ts_headline` locates matches for the given \<query\> and chooses a single one to display, preferring matches that have more query words within the allowed headline length. In fragment-based headline generation, `ts_headline` locates the query matches and splits each match into “fragments” of no more than `MaxWords` words each, preferring fragments with more query words, and when possible “stretching” fragments to include surrounding words. The fragment-based mode is thus more useful when the query matches span large sections of the document, or when it's desirable to display multiple matches. In either mode, if no query matches can be identified, then a single fragment of the first `MinWords` words in the document will be displayed.

For example:

    SELECT ts_headline('english',
      'The most common type of search
    is to find all documents containing given query terms
    and return them in order of their similarity to the
    query.',
      to_tsquery('english', 'query & similarity'));
                            ts_headline
    ------------------------------------------------------------
     containing given <b>query</b> terms                       +
     and return them in order of their <b>similarity</b> to the+
     <b>query</b>.

    SELECT ts_headline('english',
      'Search terms may occur
    many times in a document,
    requiring ranking of the search matches to decide which
    occurrences to display in the result.',
      to_tsquery('english', 'search & term'),
      'MaxFragments=10, MaxWords=7, MinWords=3, StartSel=<<, StopSel=>>');
                            ts_headline
    ------------------------------------------------------------
     <<Search>> <<terms>> may occur                            +
     many times ... ranking of the <<search>> matches to decide

`ts_headline` uses the original document, not a `tsvector` summary, so it can be slow and should be used with care.

## Additional Features

This section describes additional functions and operators that are useful in connection with text search.

### Manipulating Documents

[Parsing Documents](#textsearch-parsing-documents) showed how raw textual documents can be converted into `tsvector` values. PostgreSQL also provides functions and operators that can be used to manipulate documents that are already in `tsvector` form.

<span class="indexterm"></span> `tsvector || tsvector`  
The `tsvector` concatenation operator returns a vector which combines the lexemes and positional information of the two vectors given as arguments. Positions and weight labels are retained during the concatenation. Positions appearing in the right-hand vector are offset by the largest position mentioned in the left-hand vector, so that the result is nearly equivalent to the result of performing `to_tsvector` on the concatenation of the two original document strings. (The equivalence is not exact, because any stop-words removed from the end of the left-hand argument will not affect the result, whereas they would have affected the positions of the lexemes in the right-hand argument if textual concatenation were used.)

One advantage of using concatenation in the vector form, rather than concatenating text before applying `to_tsvector`, is that you can use different configurations to parse different sections of the document. Also, because the `setweight` function marks all lexemes of the given vector the same way, it is necessary to parse the text and do `setweight` before concatenating if you want to label different parts of the document with different weights.

<span class="indexterm"></span> `setweight(vector tsvector, weight "char") returns tsvector`  
`setweight` returns a copy of the input vector in which every position has been labeled with the given \<weight\>, either `A`, `B`, `C`, or `D`. (`D` is the default for new vectors and as such is not displayed on output.) These labels are retained when vectors are concatenated, allowing words from different parts of a document to be weighted differently by ranking functions.

Note that weight labels apply to *positions*, not *lexemes*. If the input vector has been stripped of positions then `setweight` does nothing.

<span class="indexterm"></span> `length(vector tsvector) returns integer`  
Returns the number of lexemes stored in the vector.

<span class="indexterm"></span> `strip(vector tsvector) returns tsvector`  
Returns a vector that lists the same lexemes as the given vector, but lacks any position or weight information. The result is usually much smaller than an unstripped vector, but it is also less useful. Relevance ranking does not work as well on stripped vectors as unstripped ones. Also, the `<->` (FOLLOWED BY) `tsquery` operator will never match stripped input, since it cannot determine the distance between lexeme occurrences.

A full list of `tsvector`-related functions is available in [???](#textsearch-functions-table).

### Manipulating Queries

[Parsing Queries](#textsearch-parsing-queries) showed how raw textual queries can be converted into `tsquery` values. PostgreSQL also provides functions and operators that can be used to manipulate queries that are already in `tsquery` form.

`tsquery && tsquery`  
Returns the AND-combination of the two given queries.

`tsquery || tsquery`  
Returns the OR-combination of the two given queries.

`!! tsquery`  
Returns the negation (NOT) of the given query.

`tsquery <-> tsquery`  
Returns a query that searches for a match to the first given query immediately followed by a match to the second given query, using the `<->` (FOLLOWED BY) `tsquery` operator. For example:

    SELECT to_tsquery('fat') <-> to_tsquery('cat | rat');
              ?column?
    ----------------------------
     'fat' <-> ( 'cat' | 'rat' )

<span class="indexterm"></span> `tsquery_phrase(query1 tsquery, query2 tsquery [, distance integer ]) returns tsquery`  
Returns a query that searches for a match to the first given query followed by a match to the second given query at a distance of exactly \<distance\> lexemes, using the `<N>` `tsquery` operator. For example:

    SELECT tsquery_phrase(to_tsquery('fat'), to_tsquery('cat'), 10);
      tsquery_phrase
    ------------------
     'fat' <10> 'cat'

<span class="indexterm"></span> `numnode(query tsquery) returns integer`  
Returns the number of nodes (lexemes plus operators) in a `tsquery`. This function is useful to determine if the \<query\> is meaningful (returns \> 0), or contains only stop words (returns 0). Examples:

    SELECT numnode(plainto_tsquery('the any'));
    NOTICE:  query contains only stopword(s) or doesn't contain lexeme(s), ignored
     numnode
    ---------
           0

    SELECT numnode('foo & bar'::tsquery);
     numnode
    ---------
           3

<span class="indexterm"></span> `querytree(query tsquery) returns text`  
Returns the portion of a `tsquery` that can be used for searching an index. This function is useful for detecting unindexable queries, for example those containing only stop words or only negated terms. For example:

    SELECT querytree(to_tsquery('defined'));
     querytree
    -----------
     'defin'

    SELECT querytree(to_tsquery('!defined'));
     querytree
    -----------
     T

#### Query Rewriting

ts_rewrite

The `ts_rewrite` family of functions search a given `tsquery` for occurrences of a target subquery, and replace each occurrence with a substitute subquery. In essence this operation is a `tsquery`-specific version of substring replacement. A target and substitute combination can be thought of as a query rewrite rule. A collection of such rewrite rules can be a powerful search aid. For example, you can expand the search using synonyms (e.g., `new york`, `big apple`, `nyc`, `gotham`) or narrow the search to direct the user to some hot topic. There is some overlap in functionality between this feature and thesaurus dictionaries ([Thesaurus Dictionary](#textsearch-thesaurus)). However, you can modify a set of rewrite rules on-the-fly without reindexing, whereas updating a thesaurus requires reindexing to be effective.

`ts_rewrite (query tsquery, target tsquery, substitute tsquery) returns tsquery`  
This form of `ts_rewrite` simply applies a single rewrite rule: \<target\> is replaced by \<substitute\> wherever it appears in \<query\>. For example:

    SELECT ts_rewrite('a & b'::tsquery, 'a'::tsquery, 'c'::tsquery);
     ts_rewrite
    ------------
     'b' & 'c'

`ts_rewrite (query tsquery, select text) returns tsquery`  
This form of `ts_rewrite` accepts a starting \<query\> and an SQL \<select\> command, which is given as a text string. The \<select\> must yield two columns of `tsquery` type. For each row of the \<select\> result, occurrences of the first column value (the target) are replaced by the second column value (the substitute) within the current \<query\> value. For example:

    CREATE TABLE aliases (t tsquery PRIMARY KEY, s tsquery);
    INSERT INTO aliases VALUES('a', 'c');

    SELECT ts_rewrite('a & b'::tsquery, 'SELECT t,s FROM aliases');
     ts_rewrite
    ------------
     'b' & 'c'

Note that when multiple rewrite rules are applied in this way, the order of application can be important; so in practice you will want the source query to `ORDER BY` some ordering key.

Let's consider a real-life astronomical example. We'll expand query `supernovae` using table-driven rewriting rules:

    CREATE TABLE aliases (t tsquery primary key, s tsquery);
    INSERT INTO aliases VALUES(to_tsquery('supernovae'), to_tsquery('supernovae|sn'));

    SELECT ts_rewrite(to_tsquery('supernovae & crab'), 'SELECT * FROM aliases');
               ts_rewrite
    ---------------------------------
     'crab' & ( 'supernova' | 'sn' )

We can change the rewriting rules just by updating the table:

    UPDATE aliases
    SET s = to_tsquery('supernovae|sn & !nebulae')
    WHERE t = to_tsquery('supernovae');

    SELECT ts_rewrite(to_tsquery('supernovae & crab'), 'SELECT * FROM aliases');
                     ts_rewrite
    ---------------------------------------------
     'crab' & ( 'supernova' | 'sn' & !'nebula' )

Rewriting can be slow when there are many rewriting rules, since it checks every rule for a possible match. To filter out obvious non-candidate rules we can use the containment operators for the `tsquery` type. In the example below, we select only those rules which might match the original query:

    SELECT ts_rewrite('a & b'::tsquery,
                      'SELECT t,s FROM aliases WHERE ''a & b''::tsquery @> t');
     ts_rewrite
    ------------
     'b' & 'c'

### Triggers for Automatic Updates

trigger

for updating a derived tsvector column

> [!NOTE]
> The method described in this section has been obsoleted by the use of stored generated columns, as described in [Creating Indexes](#textsearch-tables-index).

When using a separate column to store the `tsvector` representation of your documents, it is necessary to create a trigger to update the `tsvector` column when the document content columns change. Two built-in trigger functions are available for this, or you can write your own.

tsvector_update_trigger(

tsvector_column_name

,​

config_name

,

text_column_name

, ...

) tsvector_update_trigger_column(

tsvector_column_name

,​

config_column_name

,

text_column_name

, ...

)

These trigger functions automatically compute a `tsvector` column from one or more textual columns, under the control of parameters specified in the `CREATE TRIGGER` command. An example of their use is:

    CREATE TABLE messages (
        title       text,
        body        text,
        tsv         tsvector
    );

    CREATE TRIGGER tsvectorupdate BEFORE INSERT OR UPDATE
    ON messages FOR EACH ROW EXECUTE FUNCTION
    tsvector_update_trigger(tsv, 'pg_catalog.english', title, body);

    INSERT INTO messages VALUES('title here', 'the body text is here');

    SELECT * FROM messages;
       title    |         body          |            tsv
    ------------+-----------------------+----------------------------
     title here | the body text is here | 'bodi':4 'text':5 'titl':1

    SELECT title, body FROM messages WHERE tsv @@ to_tsquery('title & body');
       title    |         body
    ------------+-----------------------
     title here | the body text is here

Having created this trigger, any change in title or body will automatically be reflected into tsv, without the application having to worry about it.

The first trigger argument must be the name of the `tsvector` column to be updated. The second argument specifies the text search configuration to be used to perform the conversion. For `tsvector_update_trigger`, the configuration name is simply given as the second trigger argument. It must be schema-qualified as shown above, so that the trigger behavior will not change with changes in `search_path`. For `tsvector_update_trigger_column`, the second trigger argument is the name of another table column, which must be of type `regconfig`. This allows a per-row selection of configuration to be made. The remaining argument(s) are the names of textual columns (of type `text`, `varchar`, or `char`). These will be included in the document in the order given. NULL values will be skipped (but the other columns will still be indexed).

A limitation of these built-in triggers is that they treat all the input columns alike. To process columns differently for example, to weight title differently from body it is necessary to write a custom trigger. Here is an example using PL/pgSQL as the trigger language:

    CREATE FUNCTION messages_trigger() RETURNS trigger AS $$
    begin
      new.tsv :=
         setweight(to_tsvector('pg_catalog.english', coalesce(new.title,'')), 'A') ||
         setweight(to_tsvector('pg_catalog.english', coalesce(new.body,'')), 'D');
      return new;
    end
    $$ LANGUAGE plpgsql;

    CREATE TRIGGER tsvectorupdate BEFORE INSERT OR UPDATE
        ON messages FOR EACH ROW EXECUTE FUNCTION messages_trigger();

Keep in mind that it is important to specify the configuration name explicitly when creating `tsvector` values inside triggers, so that the column's contents will not be affected by changes to `default_text_search_config`. Failure to do this is likely to lead to problems such as search results changing after a dump and restore.

### Gathering Document Statistics

ts_stat

The function `ts_stat` is useful for checking your configuration and for finding stop-word candidates.

ts_stat(

sqlquery

text

,

weights

text

,

OUT

word

text

, OUT

ndoc

integer

, OUT

nentry

integer

) returns

setof record

\<sqlquery\> is a text value containing an SQL query which must return a single `tsvector` column. `ts_stat` executes the query and returns statistics about each distinct lexeme (word) contained in the `tsvector` data. The columns returned are

- \<word\> `text` the value of a lexeme
- \<ndoc\> `integer` number of documents (`tsvector`s) the word occurred in
- \<nentry\> `integer` total number of occurrences of the word

If \<weights\> is supplied, only occurrences having one of those weights are counted.

For example, to find the ten most frequent words in a document collection:

    SELECT * FROM ts_stat('SELECT vector FROM apod')
    ORDER BY nentry DESC, ndoc DESC, word
    LIMIT 10;

The same, but counting only word occurrences with weight `A` or `B`:

    SELECT * FROM ts_stat('SELECT vector FROM apod', 'ab')
    ORDER BY nentry DESC, ndoc DESC, word
    LIMIT 10;

## Parsers

Text search parsers are responsible for splitting raw document text into tokens and identifying each token's type, where the set of possible types is defined by the parser itself. Note that a parser does not modify the text at all it simply identifies plausible word boundaries. Because of this limited scope, there is less need for application-specific custom parsers than there is for custom dictionaries. At present PostgreSQL provides just one built-in parser, which has been found to be useful for a wide range of applications.

The built-in parser is named `pg_catalog.default`. It recognizes 23 token types, shown in [Default Parser's Token Types](#textsearch-default-parser).

| Alias | Description | Example |
|----|----|----|
| `asciiword` | Word, all ASCII letters | `elephant` |
| `word` | Word, all letters | `maana` |
| `numword` | Word, letters and digits | `beta1` |
| `asciihword` | Hyphenated word, all ASCII | `up-to-date` |
| `hword` | Hyphenated word, all letters | `lgico-matemtica` |
| `numhword` | Hyphenated word, letters and digits | `postgresql-beta1` |
| `hword_asciipart` | Hyphenated word part, all ASCII | `postgresql` in the context `postgresql-beta1` |
| `hword_part` | Hyphenated word part, all letters | `lgico` or `matemtica` in the context `lgico-matemtica` |
| `hword_numpart` | Hyphenated word part, letters and digits | `beta1` in the context `postgresql-beta1` |
| `email` | Email address | `foo@example.com` |
| `protocol` | Protocol head | `http://` |
| `url` | URL | `example.com/stuff/index.html` |
| `host` | Host | `example.com` |
| `url_path` | URL path | `/stuff/index.html`, in the context of a URL |
| `file` | File or path name | `/usr/local/foo.txt`, if not within a URL |
| `sfloat` | Scientific notation | `-1.234e56` |
| `float` | Decimal notation | `-1.234` |
| `int` | Signed integer | `-1234` |
| `uint` | Unsigned integer | `1234` |
| `version` | Version number | `8.3.0` |
| `tag` | XML tag | `<a href="dictionaries.html">` |
| `entity` | XML entity | `&amp;` |
| `blank` | Space symbols | (any whitespace or punctuation not otherwise recognized) |

Default Parser's Token Types {#textsearch-default-parser}

> [!NOTE]
> The parser's notion of a “letter” is determined by the database's locale setting, specifically `lc_ctype`. Words containing only the basic ASCII letters are reported as a separate token type, since it is sometimes useful to distinguish them. In most European languages, token types `word` and `asciiword` should be treated alike.
>
> `email` does not support all valid email characters as defined by [RFC 5322](https://datatracker.ietf.org/doc/html/rfc5322). Specifically, the only non-alphanumeric characters supported for email user names are period, dash, and underscore.
>
> `tag` does not support all valid tag names as defined by [W3C Recommendation, XML](https://www.w3.org/TR/xml/). Specifically, the only tag names supported are those starting with an ASCII letter, underscore, or colon, and containing only letters, digits, hyphens, underscores, periods, and colons. `tag` also includes XML comments starting with `<!--` and ending with `-->`, and XML declarations (but note that this includes anything starting with `<?x` and ending with `>`).

It is possible for the parser to produce overlapping tokens from the same piece of text. As an example, a hyphenated word will be reported both as the entire word and as each component:

    SELECT alias, description, token FROM ts_debug('foo-bar-beta1');
          alias      |               description                |     token
    -----------------+------------------------------------------+---------------
     numhword        | Hyphenated word, letters and digits      | foo-bar-beta1
     hword_asciipart | Hyphenated word part, all ASCII          | foo
     blank           | Space symbols                            | -
     hword_asciipart | Hyphenated word part, all ASCII          | bar
     blank           | Space symbols                            | -
     hword_numpart   | Hyphenated word part, letters and digits | beta1

This behavior is desirable since it allows searches to work for both the whole compound word and for components. Here is another instructive example:

    SELECT alias, description, token FROM ts_debug('http://example.com/stuff/index.html');
      alias   |  description  |            token
    ----------+---------------+------------------------------
     protocol | Protocol head | http://
     url      | URL           | example.com/stuff/index.html
     host     | Host          | example.com
     url_path | URL path      | /stuff/index.html

## Dictionaries

Dictionaries are used to eliminate words that should not be considered in a search (stop words), and to normalize words so that different derived forms of the same word will match. A successfully normalized word is called a lexeme. Aside from improving search quality, normalization and removal of stop words reduce the size of the `tsvector` representation of a document, thereby improving performance. Normalization does not always have linguistic meaning and usually depends on application semantics.

Some examples of normalization:

- Linguistic Ispell dictionaries try to reduce input words to a normalized form; stemmer dictionaries remove word endings
- URL locations can be canonicalized to make equivalent URLs match:
  - http://www.pgsql.ru/db/mw/index.html
  - http://www.pgsql.ru/db/mw/
  - http://www.pgsql.ru/db/../db/mw/index.html
- Color names can be replaced by their hexadecimal values, e.g., `red, green, blue, magenta -> FF0000, 00FF00, 0000FF, FF00FF`
- If indexing numbers, we can remove some fractional digits to reduce the range of possible numbers, so for example *3.14*159265359, *3.14*15926, *3.14* will be the same after normalization if only two digits are kept after the decimal point.

A dictionary is a program that accepts a token as input and returns:

- an array of lexemes if the input token is known to the dictionary (notice that one token can produce more than one lexeme)
- a single lexeme with the `TSL_FILTER` flag set, to replace the original token with a new token to be passed to subsequent dictionaries (a dictionary that does this is called a filtering dictionary)
- an empty array if the dictionary knows the token, but it is a stop word
- `NULL` if the dictionary does not recognize the input token

PostgreSQL provides predefined dictionaries for many languages. There are also several predefined templates that can be used to create new dictionaries with custom parameters. Each predefined dictionary template is described below. If no existing template is suitable, it is possible to create new ones; see the `contrib/` area of the PostgreSQL distribution for examples.

A text search configuration binds a parser together with a set of dictionaries to process the parser's output tokens. For each token type that the parser can return, a separate list of dictionaries is specified by the configuration. When a token of that type is found by the parser, each dictionary in the list is consulted in turn, until some dictionary recognizes it as a known word. If it is identified as a stop word, or if no dictionary recognizes the token, it will be discarded and not indexed or searched for. Normally, the first dictionary that returns a non-`NULL` output determines the result, and any remaining dictionaries are not consulted; but a filtering dictionary can replace the given word with a modified word, which is then passed to subsequent dictionaries.

The general rule for configuring a list of dictionaries is to place first the most narrow, most specific dictionary, then the more general dictionaries, finishing with a very general dictionary, like a Snowball stemmer or `simple`, which recognizes everything. For example, for an astronomy-specific search (`astro_en` configuration) one could bind token type `asciiword` (ASCII word) to a synonym dictionary of astronomical terms, a general English dictionary and a Snowball English stemmer:

    ALTER TEXT SEARCH CONFIGURATION astro_en
        ADD MAPPING FOR asciiword WITH astrosyn, english_ispell, english_stem;

A filtering dictionary can be placed anywhere in the list, except at the end where it'd be useless. Filtering dictionaries are useful to partially normalize words to simplify the task of later dictionaries. For example, a filtering dictionary could be used to remove accents from accented letters, as is done by the [???](#unaccent) module.

### Stop Words

Stop words are words that are very common, appear in almost every document, and have no discrimination value. Therefore, they can be ignored in the context of full text searching. For example, every English text contains words like `a` and `the`, so it is useless to store them in an index. However, stop words do affect the positions in `tsvector`, which in turn affect ranking:

    SELECT to_tsvector('english', 'in the list of stop words');
            to_tsvector
    ----------------------------
     'list':3 'stop':5 'word':6

The missing positions 1,2,4 are because of stop words. Ranks calculated for documents with and without stop words are quite different:

    SELECT ts_rank_cd (to_tsvector('english', 'in the list of stop words'), to_tsquery('list & stop'));
     ts_rank_cd
    ------------
           0.05

    SELECT ts_rank_cd (to_tsvector('english', 'list stop words'), to_tsquery('list & stop'));
     ts_rank_cd
    ------------
            0.1

It is up to the specific dictionary how it treats stop words. For example, `ispell` dictionaries first normalize words and then look at the list of stop words, while `Snowball` stemmers first check the list of stop words. The reason for the different behavior is an attempt to decrease noise.

### Simple Dictionary

The `simple` dictionary template operates by converting the input token to lower case and checking it against a file of stop words. If it is found in the file then an empty array is returned, causing the token to be discarded. If not, the lower-cased form of the word is returned as the normalized lexeme. Alternatively, the dictionary can be configured to report non-stop-words as unrecognized, allowing them to be passed on to the next dictionary in the list.

Here is an example of a dictionary definition using the `simple` template:

    CREATE TEXT SEARCH DICTIONARY public.simple_dict (
        TEMPLATE = pg_catalog.simple,
        STOPWORDS = english
    );

Here, `english` is the base name of a file of stop words. The file's full name will be `$SHAREDIR/tsearch_data/english.stop`, where `$SHAREDIR` means the PostgreSQL installation's shared-data directory, often `/usr/local/share/postgresql` (use `pg_config --sharedir` to determine it if you're not sure). The file format is simply a list of words, one per line. Blank lines and trailing spaces are ignored, and upper case is folded to lower case, but no other processing is done on the file contents.

Now we can test our dictionary:

    SELECT ts_lexize('public.simple_dict', 'YeS');
     ts_lexize
    -----------
     {yes}

    SELECT ts_lexize('public.simple_dict', 'The');
     ts_lexize
    -----------
     {}

We can also choose to return `NULL`, instead of the lower-cased word, if it is not found in the stop words file. This behavior is selected by setting the dictionary's `Accept` parameter to `false`. Continuing the example:

    ALTER TEXT SEARCH DICTIONARY public.simple_dict ( Accept = false );

    SELECT ts_lexize('public.simple_dict', 'YeS');
     ts_lexize
    -----------

    SELECT ts_lexize('public.simple_dict', 'The');
     ts_lexize
    -----------
     {}

With the default setting of `Accept` = `true`, it is only useful to place a `simple` dictionary at the end of a list of dictionaries, since it will never pass on any token to a following dictionary. Conversely, `Accept` = `false` is only useful when there is at least one following dictionary.

> [!CAUTION]
> Most types of dictionaries rely on configuration files, such as files of stop words. These files *must* be stored in UTF-8 encoding. They will be translated to the actual database encoding, if that is different, when they are read into the server.

> [!CAUTION]
> Normally, a database session will read a dictionary configuration file only once, when it is first used within the session. If you modify a configuration file and want to force existing sessions to pick up the new contents, issue an `ALTER TEXT SEARCH DICTIONARY` command on the dictionary. This can be a “dummy” update that doesn't actually change any parameter values.

### Synonym Dictionary

This dictionary template is used to create dictionaries that replace a word with a synonym. Phrases are not supported (use the thesaurus template ([Thesaurus Dictionary](#textsearch-thesaurus)) for that). A synonym dictionary can be used to overcome linguistic problems, for example, to prevent an English stemmer dictionary from reducing the word “Paris” to “pari”. It is enough to have a `Paris paris` line in the synonym dictionary and put it before the `english_stem` dictionary. For example:

    SELECT * FROM ts_debug('english', 'Paris');
       alias   |   description   | token |  dictionaries  |  dictionary  | lexemes
    -----------+-----------------+-------+----------------+--------------+---------
     asciiword | Word, all ASCII | Paris | {english_stem} | english_stem | {pari}

    CREATE TEXT SEARCH DICTIONARY my_synonym (
        TEMPLATE = synonym,
        SYNONYMS = my_synonyms
    );

    ALTER TEXT SEARCH CONFIGURATION english
        ALTER MAPPING FOR asciiword
        WITH my_synonym, english_stem;

    SELECT * FROM ts_debug('english', 'Paris');
       alias   |   description   | token |       dictionaries        | dictionary | lexemes
    -----------+-----------------+-------+---------------------------+------------+---------
     asciiword | Word, all ASCII | Paris | {my_synonym,english_stem} | my_synonym | {paris}

The only parameter required by the `synonym` template is `SYNONYMS`, which is the base name of its configuration file `my_synonyms` in the above example. The file's full name will be `$SHAREDIR/tsearch_data/my_synonyms.syn` (where `$SHAREDIR` means the PostgreSQL installation's shared-data directory). The file format is just one line per word to be substituted, with the word followed by its synonym, separated by white space. Blank lines and trailing spaces are ignored.

The `synonym` template also has an optional parameter `CaseSensitive`, which defaults to `false`. When `CaseSensitive` is `false`, words in the synonym file are folded to lower case, as are input tokens. When it is `true`, words and tokens are not folded to lower case, but are compared as-is.

An asterisk (`*`) can be placed at the end of a synonym in the configuration file. This indicates that the synonym is a prefix. The asterisk is ignored when the entry is used in `to_tsvector()`, but when it is used in `to_tsquery()`, the result will be a query item with the prefix match marker (see [Parsing Queries](#textsearch-parsing-queries)). For example, suppose we have these entries in `$SHAREDIR/tsearch_data/synonym_sample.syn`:

    postgres        pgsql
    postgresql      pgsql
    postgre pgsql
    gogle   googl
    indices index*

Then we will get these results:

    mydb=# CREATE TEXT SEARCH DICTIONARY syn (template=synonym, synonyms='synonym_sample');
    mydb=# SELECT ts_lexize('syn', 'indices');
     ts_lexize
    -----------
     {index}
    (1 row)

    mydb=# CREATE TEXT SEARCH CONFIGURATION tst (copy=simple);
    mydb=# ALTER TEXT SEARCH CONFIGURATION tst ALTER MAPPING FOR asciiword WITH syn;
    mydb=# SELECT to_tsvector('tst', 'indices');
     to_tsvector
    -------------
     'index':1
    (1 row)

    mydb=# SELECT to_tsquery('tst', 'indices');
     to_tsquery
    ------------
     'index':*
    (1 row)

    mydb=# SELECT 'indexes are very useful'::tsvector;
                tsvector
    ---------------------------------
     'are' 'indexes' 'useful' 'very'
    (1 row)

    mydb=# SELECT 'indexes are very useful'::tsvector @@ to_tsquery('tst', 'indices');
     ?column?
    ----------
     t
    (1 row)

### Thesaurus Dictionary

A thesaurus dictionary (sometimes abbreviated as TZ) is a collection of words that includes information about the relationships of words and phrases, i.e., broader terms (BT), narrower terms (NT), preferred terms, non-preferred terms, related terms, etc.

Basically a thesaurus dictionary replaces all non-preferred terms by one preferred term and, optionally, preserves the original terms for indexing as well. PostgreSQL's current implementation of the thesaurus dictionary is an extension of the synonym dictionary with added phrase support. A thesaurus dictionary requires a configuration file of the following format:

    # this is a comment
    sample word(s) : indexed word(s)
    more sample word(s) : more indexed word(s)
    ...

where the colon (`:`) symbol acts as a delimiter between a phrase and its replacement.

A thesaurus dictionary uses a subdictionary (which is specified in the dictionary's configuration) to normalize the input text before checking for phrase matches. It is only possible to select one subdictionary. An error is reported if the subdictionary fails to recognize a word. In that case, you should remove the use of the word or teach the subdictionary about it. You can place an asterisk (`*`) at the beginning of an indexed word to skip applying the subdictionary to it, but all sample words *must* be known to the subdictionary.

The thesaurus dictionary chooses the longest match if there are multiple phrases matching the input, and ties are broken by using the last definition.

Specific stop words recognized by the subdictionary cannot be specified; instead use `?` to mark the location where any stop word can appear. For example, assuming that `a` and `the` are stop words according to the subdictionary:

    ? one ? two : swsw

matches `a one the two` and `the one a two`; both would be replaced by `swsw`.

Since a thesaurus dictionary has the capability to recognize phrases it must remember its state and interact with the parser. A thesaurus dictionary uses these assignments to check if it should handle the next word or stop accumulation. The thesaurus dictionary must be configured carefully. For example, if the thesaurus dictionary is assigned to handle only the `asciiword` token, then a thesaurus dictionary definition like `one 7` will not work since token type `uint` is not assigned to the thesaurus dictionary.

> [!CAUTION]
> Thesauruses are used during indexing so any change in the thesaurus dictionary's parameters *requires* reindexing. For most other dictionary types, small changes such as adding or removing stopwords does not force reindexing.

#### Thesaurus Configuration

To define a new thesaurus dictionary, use the `thesaurus` template. For example:

    CREATE TEXT SEARCH DICTIONARY thesaurus_simple (
        TEMPLATE = thesaurus,
        DictFile = mythesaurus,
        Dictionary = pg_catalog.english_stem
    );

Here:

- `thesaurus_simple` is the new dictionary's name
- `mythesaurus` is the base name of the thesaurus configuration file. (Its full name will be `$SHAREDIR/tsearch_data/mythesaurus.ths`, where `$SHAREDIR` means the installation shared-data directory.)
- `pg_catalog.english_stem` is the subdictionary (here, a Snowball English stemmer) to use for thesaurus normalization. Notice that the subdictionary will have its own configuration (for example, stop words), which is not shown here.

Now it is possible to bind the thesaurus dictionary `thesaurus_simple` to the desired token types in a configuration, for example:

    ALTER TEXT SEARCH CONFIGURATION russian
        ALTER MAPPING FOR asciiword, asciihword, hword_asciipart
        WITH thesaurus_simple;

#### Thesaurus Example

Consider a simple astronomical thesaurus `thesaurus_astro`, which contains some astronomical word combinations:

    supernovae stars : sn
    crab nebulae : crab

Below we create a dictionary and bind some token types to an astronomical thesaurus and English stemmer:

    CREATE TEXT SEARCH DICTIONARY thesaurus_astro (
        TEMPLATE = thesaurus,
        DictFile = thesaurus_astro,
        Dictionary = english_stem
    );

    ALTER TEXT SEARCH CONFIGURATION russian
        ALTER MAPPING FOR asciiword, asciihword, hword_asciipart
        WITH thesaurus_astro, english_stem;

Now we can see how it works. `ts_lexize` is not very useful for testing a thesaurus, because it treats its input as a single token. Instead we can use `plainto_tsquery` and `to_tsvector` which will break their input strings into multiple tokens:

    SELECT plainto_tsquery('supernova star');
     plainto_tsquery
    -----------------
     'sn'

    SELECT to_tsvector('supernova star');
     to_tsvector
    -------------
     'sn':1

In principle, one can use `to_tsquery` if you quote the argument:

    SELECT to_tsquery('''supernova star''');
     to_tsquery
    ------------
     'sn'

Notice that `supernova star` matches `supernovae stars` in `thesaurus_astro` because we specified the `english_stem` stemmer in the thesaurus definition. The stemmer removed the `e` and `s`.

To index the original phrase as well as the substitute, just include it in the right-hand part of the definition:

    supernovae stars : sn supernovae stars

    SELECT plainto_tsquery('supernova star');
           plainto_tsquery
    -----------------------------
     'sn' & 'supernova' & 'star'

### Ispell Dictionary

The Ispell dictionary template supports morphological dictionaries, which can normalize many different linguistic forms of a word into the same lexeme. For example, an English Ispell dictionary can match all declensions and conjugations of the search term `bank`, e.g., `banking`, `banked`, `banks`, `banks'`, and `bank's`.

The standard PostgreSQL distribution does not include any Ispell configuration files. Dictionaries for a large number of languages are available from [Ispell](https://www.cs.hmc.edu/~geoff/ispell.html). Also, some more modern dictionary file formats are supported [MySpell](https://en.wikipedia.org/wiki/MySpell) (OO \< 2.0.1) and [Hunspell](https://hunspell.github.io/) (OO \>= 2.0.2). A large list of dictionaries is available on the [OpenOffice Wiki](https://wiki.openoffice.org/wiki/Dictionaries).

To create an Ispell dictionary perform these steps:

- download dictionary configuration files. OpenOffice extension files have the `.oxt` extension. It is necessary to extract `.aff` and `.dic` files, change extensions to `.affix` and `.dict`. For some dictionary files it is also needed to convert characters to the UTF-8 encoding with commands (for example, for a Norwegian language dictionary):
      iconv -f ISO_8859-1 -t UTF-8 -o nn_no.affix nn_NO.aff
      iconv -f ISO_8859-1 -t UTF-8 -o nn_no.dict nn_NO.dic
- copy files to the `$SHAREDIR/tsearch_data` directory
- load files into PostgreSQL with the following command:
      CREATE TEXT SEARCH DICTIONARY english_hunspell (
          TEMPLATE = ispell,
          DictFile = en_us,
          AffFile = en_us,
          Stopwords = english);

Here, `DictFile`, `AffFile`, and `StopWords` specify the base names of the dictionary, affixes, and stop-words files. The stop-words file has the same format explained above for the `simple` dictionary type. The format of the other files is not specified here but is available from the above-mentioned web sites.

Ispell dictionaries usually recognize a limited set of words, so they should be followed by another broader dictionary; for example, a Snowball dictionary, which recognizes everything.

The `.affix` file of Ispell has the following structure:

    prefixes
    flag *A:
        .           >   RE      # As in enter > reenter
    suffixes
    flag T:
        E           >   ST      # As in late > latest
        [^AEIOU]Y   >   -Y,IEST # As in dirty > dirtiest
        [AEIOU]Y    >   EST     # As in gray > grayest
        [^EY]       >   EST     # As in small > smallest

And the `.dict` file has the following structure:

    lapse/ADGRS
    lard/DGRS
    large/PRTY
    lark/MRS

Format of the `.dict` file is:

    basic_form/affix_class_name

In the `.affix` file every affix flag is described in the following format:

    condition > [-stripping_letters,] adding_affix

Here, condition has a format similar to the format of regular expressions. It can use groupings `[...]` and `[^...]`. For example, `[AEIOU]Y` means that the last letter of the word is `"y"` and the penultimate letter is `"a"`, `"e"`, `"i"`, `"o"` or `"u"`. `[^EY]` means that the last letter is neither `"e"` nor `"y"`.

Ispell dictionaries support splitting compound words; a useful feature. Notice that the affix file should specify a special flag using the `compoundwords controlled` statement that marks dictionary words that can participate in compound formation:

    compoundwords  controlled z

Here are some examples for the Norwegian language:

    SELECT ts_lexize('norwegian_ispell', 'overbuljongterningpakkmesterassistent');
       {over,buljong,terning,pakk,mester,assistent}
    SELECT ts_lexize('norwegian_ispell', 'sjokoladefabrikk');
       {sjokoladefabrikk,sjokolade,fabrikk}

MySpell format is a subset of Hunspell. The `.affix` file of Hunspell has the following structure:

    PFX A Y 1
    PFX A   0     re         .
    SFX T N 4
    SFX T   0     st         e
    SFX T   y     iest       [^aeiou]y
    SFX T   0     est        [aeiou]y
    SFX T   0     est        [^ey]

The first line of an affix class is the header. Fields of an affix rules are listed after the header:

- parameter name (PFX or SFX)
- flag (name of the affix class)
- stripping characters from beginning (at prefix) or end (at suffix) of the word
- adding affix
- condition that has a format similar to the format of regular expressions.

The `.dict` file looks like the `.dict` file of Ispell:

    larder/M
    lardy/RT
    large/RSPMYT
    largehearted

> [!NOTE]
> MySpell does not support compound words. Hunspell has sophisticated support for compound words. At present, PostgreSQL implements only the basic compound word operations of Hunspell.

### Snowball Dictionary

The Snowball dictionary template is based on a project by Martin Porter, inventor of the popular Porter's stemming algorithm for the English language. Snowball now provides stemming algorithms for many languages (see the [Snowball site](https://snowballstem.org/) for more information). Each algorithm understands how to reduce common variant forms of words to a base, or stem, spelling within its language. A Snowball dictionary requires a `language` parameter to identify which stemmer to use, and optionally can specify a `stopword` file name that gives a list of words to eliminate. (PostgreSQL's standard stopword lists are also provided by the Snowball project.) For example, there is a built-in definition equivalent to

    CREATE TEXT SEARCH DICTIONARY english_stem (
        TEMPLATE = snowball,
        Language = english,
        StopWords = english
    );

The stopword file format is the same as already explained.

A Snowball dictionary recognizes everything, whether or not it is able to simplify the word, so it should be placed at the end of the dictionary list. It is useless to have it before any other dictionary because a token will never pass through it to the next dictionary.

## Configuration Example

A text search configuration specifies all options necessary to transform a document into a `tsvector`: the parser to use to break text into tokens, and the dictionaries to use to transform each token into a lexeme. Every call of `to_tsvector` or `to_tsquery` needs a text search configuration to perform its processing. The configuration parameter [???](#guc-default-text-search-config) specifies the name of the default configuration, which is the one used by text search functions if an explicit configuration parameter is omitted. It can be set in `postgresql.conf`, or set for an individual session using the `SET` command.

Several predefined text search configurations are available, and you can create custom configurations easily. To facilitate management of text search objects, a set of SQL commands is available, and there are several psql commands that display information about text search objects ([ Support](#textsearch-psql)).

As an example we will create a configuration `pg`, starting by duplicating the built-in `english` configuration:

    CREATE TEXT SEARCH CONFIGURATION public.pg ( COPY = pg_catalog.english );

We will use a PostgreSQL-specific synonym list and store it in `$SHAREDIR/tsearch_data/pg_dict.syn`. The file contents look like:

    postgres    pg
    pgsql       pg
    postgresql  pg

We define the synonym dictionary like this:

    CREATE TEXT SEARCH DICTIONARY pg_dict (
        TEMPLATE = synonym,
        SYNONYMS = pg_dict
    );

Next we register the Ispell dictionary `english_ispell`, which has its own configuration files:

    CREATE TEXT SEARCH DICTIONARY english_ispell (
        TEMPLATE = ispell,
        DictFile = english,
        AffFile = english,
        StopWords = english
    );

Now we can set up the mappings for words in configuration `pg`:

    ALTER TEXT SEARCH CONFIGURATION pg
        ALTER MAPPING FOR asciiword, asciihword, hword_asciipart,
                          word, hword, hword_part
        WITH pg_dict, english_ispell, english_stem;

We choose not to index or search some token types that the built-in configuration does handle:

    ALTER TEXT SEARCH CONFIGURATION pg
        DROP MAPPING FOR email, url, url_path, sfloat, float;

Now we can test our configuration:

    SELECT * FROM ts_debug('public.pg', '
    PostgreSQL, the highly scalable, SQL compliant, open source object-relational
    database management system, is now undergoing beta testing of the next
    version of our software.
    ');

The next step is to set the session to use the new configuration, which was created in the `public` schema:

    => \dF
       List of text search configurations
     Schema  | Name | Description
    ---------+------+-------------
     public  | pg   |

    SET default_text_search_config = 'public.pg';
    SET

    SHOW default_text_search_config;
     default_text_search_config
    ----------------------------
     public.pg

## Testing and Debugging Text Search

The behavior of a custom text search configuration can easily become confusing. The functions described in this section are useful for testing text search objects. You can test a complete configuration, or test parsers and dictionaries separately.

### Configuration Testing

The function `ts_debug` allows easy testing of a text search configuration.

ts_debug

ts_debug(

config

regconfig

,

document

text

, OUT

alias

text

, OUT

description

text

, OUT

token

text

, OUT

dictionaries

regdictionary\[\]

, OUT

dictionary

regdictionary

, OUT

lexemes

text\[\]

) returns setof record

`ts_debug` displays information about every token of \<document\> as produced by the parser and processed by the configured dictionaries. It uses the configuration specified by \<config\>, or `default_text_search_config` if that argument is omitted.

`ts_debug` returns one row for each token identified in the text by the parser. The columns returned are

- \<alias\> `text` short name of the token type
- \<description\> `text` description of the token type
- \<token\> `text` text of the token
- \<dictionaries\> `regdictionary[]` the dictionaries selected by the configuration for this token type
- \<dictionary\> `regdictionary` the dictionary that recognized the token, or `NULL` if none did
- \<lexemes\> `text[]` the lexeme(s) produced by the dictionary that recognized the token, or `NULL` if none did; an empty array (`{}`) means it was recognized as a stop word

Here is a simple example:

    SELECT * FROM ts_debug('english', 'a fat  cat sat on a mat - it ate a fat rats');
       alias   |   description   | token |  dictionaries  |  dictionary  | lexemes
    -----------+-----------------+-------+----------------+--------------+---------
     asciiword | Word, all ASCII | a     | {english_stem} | english_stem | {}
     blank     | Space symbols   |       | {}             |              |
     asciiword | Word, all ASCII | fat   | {english_stem} | english_stem | {fat}
     blank     | Space symbols   |       | {}             |              |
     asciiword | Word, all ASCII | cat   | {english_stem} | english_stem | {cat}
     blank     | Space symbols   |       | {}             |              |
     asciiword | Word, all ASCII | sat   | {english_stem} | english_stem | {sat}
     blank     | Space symbols   |       | {}             |              |
     asciiword | Word, all ASCII | on    | {english_stem} | english_stem | {}
     blank     | Space symbols   |       | {}             |              |
     asciiword | Word, all ASCII | a     | {english_stem} | english_stem | {}
     blank     | Space symbols   |       | {}             |              |
     asciiword | Word, all ASCII | mat   | {english_stem} | english_stem | {mat}
     blank     | Space symbols   |       | {}             |              |
     blank     | Space symbols   | -     | {}             |              |
     asciiword | Word, all ASCII | it    | {english_stem} | english_stem | {}
     blank     | Space symbols   |       | {}             |              |
     asciiword | Word, all ASCII | ate   | {english_stem} | english_stem | {ate}
     blank     | Space symbols   |       | {}             |              |
     asciiword | Word, all ASCII | a     | {english_stem} | english_stem | {}
     blank     | Space symbols   |       | {}             |              |
     asciiword | Word, all ASCII | fat   | {english_stem} | english_stem | {fat}
     blank     | Space symbols   |       | {}             |              |
     asciiword | Word, all ASCII | rats  | {english_stem} | english_stem | {rat}

For a more extensive demonstration, we first create a `public.english` configuration and Ispell dictionary for the English language:

    CREATE TEXT SEARCH CONFIGURATION public.english ( COPY = pg_catalog.english );

    CREATE TEXT SEARCH DICTIONARY english_ispell (
        TEMPLATE = ispell,
        DictFile = english,
        AffFile = english,
        StopWords = english
    );

    ALTER TEXT SEARCH CONFIGURATION public.english
       ALTER MAPPING FOR asciiword WITH english_ispell, english_stem;

    SELECT * FROM ts_debug('public.english', 'The Brightest supernovaes');
       alias   |   description   |    token    |         dictionaries          |   dictionary   |   lexemes
    -----------+-----------------+-------------+-------------------------------+----------------+-------------
     asciiword | Word, all ASCII | The         | {english_ispell,english_stem} | english_ispell | {}
     blank     | Space symbols   |             | {}                            |                |
     asciiword | Word, all ASCII | Brightest   | {english_ispell,english_stem} | english_ispell | {bright}
     blank     | Space symbols   |             | {}                            |                |
     asciiword | Word, all ASCII | supernovaes | {english_ispell,english_stem} | english_stem   | {supernova}

In this example, the word `Brightest` was recognized by the parser as an `ASCII word` (alias `asciiword`). For this token type the dictionary list is `english_ispell` and `english_stem`. The word was recognized by `english_ispell`, which reduced it to the noun `bright`. The word `supernovaes` is unknown to the `english_ispell` dictionary so it was passed to the next dictionary, and, fortunately, was recognized (in fact, `english_stem` is a Snowball dictionary which recognizes everything; that is why it was placed at the end of the dictionary list).

The word `The` was recognized by the `english_ispell` dictionary as a stop word ([Stop Words](#textsearch-stopwords)) and will not be indexed. The spaces are discarded too, since the configuration provides no dictionaries at all for them.

You can reduce the width of the output by explicitly specifying which columns you want to see:

    SELECT alias, token, dictionary, lexemes
    FROM ts_debug('public.english', 'The Brightest supernovaes');
       alias   |    token    |   dictionary   |   lexemes
    -----------+-------------+----------------+-------------
     asciiword | The         | english_ispell | {}
     blank     |             |                |
     asciiword | Brightest   | english_ispell | {bright}
     blank     |             |                |
     asciiword | supernovaes | english_stem   | {supernova}

### Parser Testing

The following functions allow direct testing of a text search parser.

ts_parse

ts_parse(

parser_name

text

,

document

text

, OUT

tokid

integer

, OUT

token

text

) returns

setof record

ts_parse(

parser_oid

oid

,

document

text

, OUT

tokid

integer

, OUT

token

text

) returns

setof record

`ts_parse` parses the given \<document\> and returns a series of records, one for each token produced by parsing. Each record includes a `tokid` showing the assigned token type and a `token` which is the text of the token. For example:

    SELECT * FROM ts_parse('default', '123 - a number');
     tokid | token
    -------+--------
        22 | 123
        12 |
        12 | -
         1 | a
        12 |
         1 | number

ts_token_type

ts_token_type(

parser_name

text

, OUT

tokid

integer

, OUT

alias

text

, OUT

description

text

) returns

setof record

ts_token_type(

parser_oid

oid

, OUT

tokid

integer

, OUT

alias

text

, OUT

description

text

) returns

setof record

`ts_token_type` returns a table which describes each type of token the specified parser can recognize. For each token type, the table gives the integer `tokid` that the parser uses to label a token of that type, the `alias` that names the token type in configuration commands, and a short `description`. For example:

    SELECT * FROM ts_token_type('default');
     tokid |      alias      |               description
    -------+-----------------+------------------------------------------
         1 | asciiword       | Word, all ASCII
         2 | word            | Word, all letters
         3 | numword         | Word, letters and digits
         4 | email           | Email address
         5 | url             | URL
         6 | host            | Host
         7 | sfloat          | Scientific notation
         8 | version         | Version number
         9 | hword_numpart   | Hyphenated word part, letters and digits
        10 | hword_part      | Hyphenated word part, all letters
        11 | hword_asciipart | Hyphenated word part, all ASCII
        12 | blank           | Space symbols
        13 | tag             | XML tag
        14 | protocol        | Protocol head
        15 | numhword        | Hyphenated word, letters and digits
        16 | asciihword      | Hyphenated word, all ASCII
        17 | hword           | Hyphenated word, all letters
        18 | url_path        | URL path
        19 | file            | File or path name
        20 | float           | Decimal notation
        21 | int             | Signed integer
        22 | uint            | Unsigned integer
        23 | entity          | XML entity

### Dictionary Testing

The `ts_lexize` function facilitates dictionary testing.

ts_lexize

ts_lexize(

dict

regdictionary

,

token

text

) returns

text\[\]

`ts_lexize` returns an array of lexemes if the input \<token\> is known to the dictionary, or an empty array if the token is known to the dictionary but it is a stop word, or `NULL` if it is an unknown word.

Examples:

    SELECT ts_lexize('english_stem', 'stars');
     ts_lexize
    -----------
     {star}

    SELECT ts_lexize('english_stem', 'a');
     ts_lexize
    -----------
     {}

> [!NOTE]
> The `ts_lexize` function expects a single *token*, not text. Here is a case where this can be confusing:
>
>     SELECT ts_lexize('thesaurus_astro', 'supernovae stars') is null;
>      ?column?
>     ----------
>      t
>
> The thesaurus dictionary `thesaurus_astro` does know the phrase `supernovae stars`, but `ts_lexize` fails since it does not parse the input text but treats it as a single token. Use `plainto_tsquery` or `to_tsvector` to test thesaurus dictionaries, for example:
>
>     SELECT plainto_tsquery('supernovae stars');
>      plainto_tsquery
>     -----------------
>      'sn'

## Preferred Index Types for Text Search

text search

indexes

There are two kinds of indexes that can be used to speed up full text searches: [GIN](#gin) and [GiST](#gist). Note that indexes are not mandatory for full text searching, but in cases where a column is searched on a regular basis, an index is usually desirable.

To create such an index, do one of:

<span class="indexterm"></span> `CREATE INDEX name ON table USING GIN (column);`  
Creates a GIN (Generalized Inverted Index)-based index. The \<column\> must be of `tsvector` type.

<span class="indexterm"></span> `CREATE INDEX name ON table USING GIST (column [ { DEFAULT | tsvector_ops } (siglen = number) ] );`  
Creates a GiST (Generalized Search Tree)-based index. The \<column\> can be of `tsvector` or `tsquery` type. Optional integer parameter `siglen` determines signature length in bytes (see below for details).

GIN indexes are the preferred text search index type. As inverted indexes, they contain an index entry for each word (lexeme), with a compressed list of matching locations. Multi-word searches can find the first match, then use the index to remove rows that are lacking additional words. GIN indexes store only the words (lexemes) of `tsvector` values, and not their weight labels. Thus a table row recheck is needed when using a query that involves weights.

A GiST index is lossy, meaning that the index might produce false matches, and it is necessary to check the actual table row to eliminate such false matches. (PostgreSQL does this automatically when needed.) GiST indexes are lossy because each document is represented in the index by a fixed-length signature. The signature length in bytes is determined by the value of the optional integer parameter `siglen`. The default signature length (when `siglen` is not specified) is 124 bytes, the maximum signature length is 2024 bytes. The signature is generated by hashing each word into a single bit in an n-bit string, with all these bits OR-ed together to produce an n-bit document signature. When two words hash to the same bit position there will be a false match. If all words in the query have matches (real or false) then the table row must be retrieved to see if the match is correct. Longer signatures lead to a more precise search (scanning a smaller fraction of the index and fewer heap pages), at the cost of a larger index.

A GiST index can be covering, i.e., use the `INCLUDE` clause. Included columns can have data types without any GiST operator class. Included attributes will be stored uncompressed.

Lossiness causes performance degradation due to unnecessary fetches of table records that turn out to be false matches. Since random access to table records is slow, this limits the usefulness of GiST indexes. The likelihood of false matches depends on several factors, in particular the number of unique words, so using dictionaries to reduce this number is recommended.

Note that GIN index build time can often be improved by increasing [???](#guc-maintenance-work-mem), while GiST index build time is not sensitive to that parameter.

Partitioning of big collections and the proper use of GIN and GiST indexes allows the implementation of very fast searches with online update. Partitioning can be done at the database level using table inheritance, or by distributing documents over servers and collecting external search results, e.g., via [Foreign Data](#ddl-foreign-data) access. The latter is possible because ranking functions use only local information.

## psql Support

Information about text search configuration objects can be obtained in psql using a set of commands: \dF{d,p,t}\[+\] \[PATTERN\] An optional `+` produces more details.

The optional parameter \<PATTERN\> can be the name of a text search object, optionally schema-qualified. If \<PATTERN\> is omitted then information about all visible objects will be displayed. \<PATTERN\> can be a regular expression and can provide *separate* patterns for the schema and object names. The following examples illustrate this:

    => \dF *fulltext*
           List of text search configurations
     Schema |  Name        | Description
    --------+--------------+-------------
     public | fulltext_cfg |

    => \dF *.fulltext*
           List of text search configurations
     Schema   |  Name        | Description
    ----------+----------------------------
     fulltext | fulltext_cfg |
     public   | fulltext_cfg |

The available commands are:

`\dF+ PATTERN`  
List text search configurations (add `+` for more detail).

    => \dF russian
                List of text search configurations
       Schema   |  Name   |            Description
    ------------+---------+------------------------------------
     pg_catalog | russian | configuration for russian language

    => \dF+ russian
    Text search configuration "pg_catalog.russian"
    Parser: "pg_catalog.default"
          Token      | Dictionaries
    -----------------+--------------
     asciihword      | english_stem
     asciiword       | english_stem
     email           | simple
     file            | simple
     float           | simple
     host            | simple
     hword           | russian_stem
     hword_asciipart | english_stem
     hword_numpart   | simple
     hword_part      | russian_stem
     int             | simple
     numhword        | simple
     numword         | simple
     sfloat          | simple
     uint            | simple
     url             | simple
     url_path        | simple
     version         | simple
     word            | russian_stem

`\dFd+ PATTERN`  
List text search dictionaries (add `+` for more detail).

    => \dFd
                                 List of text search dictionaries
       Schema   |      Name       |                        Description
    ------------+-----------------+-----------------------------------------------------------
     pg_catalog | arabic_stem     | snowball stemmer for arabic language
     pg_catalog | armenian_stem   | snowball stemmer for armenian language
     pg_catalog | basque_stem     | snowball stemmer for basque language
     pg_catalog | catalan_stem    | snowball stemmer for catalan language
     pg_catalog | danish_stem     | snowball stemmer for danish language
     pg_catalog | dutch_stem      | snowball stemmer for dutch language
     pg_catalog | english_stem    | snowball stemmer for english language
     pg_catalog | finnish_stem    | snowball stemmer for finnish language
     pg_catalog | french_stem     | snowball stemmer for french language
     pg_catalog | german_stem     | snowball stemmer for german language
     pg_catalog | greek_stem      | snowball stemmer for greek language
     pg_catalog | hindi_stem      | snowball stemmer for hindi language
     pg_catalog | hungarian_stem  | snowball stemmer for hungarian language
     pg_catalog | indonesian_stem | snowball stemmer for indonesian language
     pg_catalog | irish_stem      | snowball stemmer for irish language
     pg_catalog | italian_stem    | snowball stemmer for italian language
     pg_catalog | lithuanian_stem | snowball stemmer for lithuanian language
     pg_catalog | nepali_stem     | snowball stemmer for nepali language
     pg_catalog | norwegian_stem  | snowball stemmer for norwegian language
     pg_catalog | portuguese_stem | snowball stemmer for portuguese language
     pg_catalog | romanian_stem   | snowball stemmer for romanian language
     pg_catalog | russian_stem    | snowball stemmer for russian language
     pg_catalog | serbian_stem    | snowball stemmer for serbian language
     pg_catalog | simple          | simple dictionary: just lower case and check for stopword
     pg_catalog | spanish_stem    | snowball stemmer for spanish language
     pg_catalog | swedish_stem    | snowball stemmer for swedish language
     pg_catalog | tamil_stem      | snowball stemmer for tamil language
     pg_catalog | turkish_stem    | snowball stemmer for turkish language
     pg_catalog | yiddish_stem    | snowball stemmer for yiddish language

`\dFp+ PATTERN`  
List text search parsers (add `+` for more detail).

    => \dFp
            List of text search parsers
       Schema   |  Name   |     Description
    ------------+---------+---------------------
     pg_catalog | default | default word parser
    => \dFp+
        Text search parser "pg_catalog.default"
         Method      |    Function    | Description
    -----------------+----------------+-------------
     Start parse     | prsd_start     |
     Get next token  | prsd_nexttoken |
     End parse       | prsd_end       |
     Get headline    | prsd_headline  |
     Get token types | prsd_lextype   |

            Token types for parser "pg_catalog.default"
       Token name    |               Description
    -----------------+------------------------------------------
     asciihword      | Hyphenated word, all ASCII
     asciiword       | Word, all ASCII
     blank           | Space symbols
     email           | Email address
     entity          | XML entity
     file            | File or path name
     float           | Decimal notation
     host            | Host
     hword           | Hyphenated word, all letters
     hword_asciipart | Hyphenated word part, all ASCII
     hword_numpart   | Hyphenated word part, letters and digits
     hword_part      | Hyphenated word part, all letters
     int             | Signed integer
     numhword        | Hyphenated word, letters and digits
     numword         | Word, letters and digits
     protocol        | Protocol head
     sfloat          | Scientific notation
     tag             | XML tag
     uint            | Unsigned integer
     url             | URL
     url_path        | URL path
     version         | Version number
     word            | Word, all letters
    (23 rows)

`\dFt+ PATTERN`  
List text search templates (add `+` for more detail).

    => \dFt
                               List of text search templates
       Schema   |   Name    |                        Description
    ------------+-----------+-----------------------------------------------------------
     pg_catalog | ispell    | ispell dictionary
     pg_catalog | simple    | simple dictionary: just lower case and check for stopword
     pg_catalog | snowball  | snowball stemmer
     pg_catalog | synonym   | synonym dictionary: replace word by its synonym
     pg_catalog | thesaurus | thesaurus dictionary: phrase by phrase substitution

## Limitations

The current limitations of PostgreSQL's text search features are:

- The length of each lexeme must be less than 2 kilobytes
- No more than 256 positions per lexeme
- Position values in `tsvector` must be greater than 0 and no more than 16,383
- The length of a `tsvector`'s data (lexemes + positions) must be less than 1 megabyte
- The length of a `tsquery`'s data (lexemes only) must be less than 1 megabyte
- The match distance in a `<N>` (FOLLOWED BY) `tsquery` operator cannot be more than 16,384

For comparison, the PostgreSQL 8.1 documentation contained 10,441 unique words, a total of 335,420 words, and the most frequent word “postgresql” was mentioned 6,127 times in 655 documents.

Another example the PostgreSQL mailing list archives contained 910,989 unique words with 57,491,343 lexemes in 461,020 messages.
