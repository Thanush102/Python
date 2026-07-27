import keyword
identifiers = [
    "2value",
    "value_2",
    "_hidden",
    "class",
    "my-var",
    "MyClass",
    "total$"
    ]
for identifier in identifiers:
    if identifier.isidentifier() and not keyword.iskeyword(identifier):
        print(identifier," valid ")
    else:
            print(identifier," invalid ")


#output:2value  invalid    //identifier cannot strt with number//
        #value_2  valid 
        #_hidden  valid 
        #class  invalid    //keywords are not identifiers//
        #my-var  invalid   //symbols are not allowed in identifiers//
        #MyClass  valid 
        #total$  invalid   //symbols are not allowed in identifiers//
