print("%(lang)s is fun!" % {"lang":"Python"})

print("%(x)i + %(y)i = %(z)i" % {"x":1, "y":2, "z":3})

language={"lang1":"Python","lang2":"Lisp"}

print("%(lang1)s is simpliest than %(lang2)s"  %{"lang1":"Python","lang2":"Lisp"})

print("{lang2} is harder than {lang1}".format(**language))
