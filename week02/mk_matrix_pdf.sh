python2 ./matrix_mult.py > $1.tex
pdflatex $1.tex
rm $1.log $1.tex $1.aux
