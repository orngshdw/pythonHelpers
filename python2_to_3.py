def unicode_to_str(unicode_str):
    """
    Takes a unicode object and coverts it to a str (utf-8).
    If the arg is already a str, returns unicode_str (i.e. if run with python 3).
    Needed to support python 2/3 with unicode_literals.
    
    py2: type<unicode> -> type<str utf-8>
    py3: type<str utf-8> (no unicode tdype exists)

    :type unicode_str: unicode (py2) or str (py3)
    :param unicode_str: the unicode that potentially needs converting (i.e. if run with python 2)

    :return: str
    """
    if isinstance(unicode_str, str):
        return unicode_str

    return unicode_str.encode('utf-8')
