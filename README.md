Idris to Python back end
------------------------

This is technically a fork of https://github.com/edwinb/idris-php.

Example
-------

    $ cat pythag.idr 
    module Main

    pythag : Int -> List (Int, Int, Int)
    pythag max = [(x, y, z) | z <- [1..max], y <- [1..z], x <- [1..y],
                              x * x + y *y == z * z]

    main : IO ()
    main = print (pythag 50)

    $ idris pythag.idr --codegen py -o pythag.py
    $ python pythag.py
    [(3, (4, 5)), (6, (8, 10)), (5, (12, 13)), (9, (12, 15)), (8, (15, 17)), 
     (12, (16, 20)), (15, (20, 25)), (7, (24, 25)), (10, (24, 26)), (20, (21, 29)), 
     (18, (24, 30)), (16, (30, 34)), (21, (28, 35)), (12, (35, 37)), (15, (36, 39)), 
     (24, (32, 40)), (9, (40, 41)), (27, (36, 45)), (30, (40, 50)), (14, (48, 50))]
