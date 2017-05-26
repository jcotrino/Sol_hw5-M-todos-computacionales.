
all: canal_ionico.c

Resultados_hw5.pdf: Resultados_hw5.tex Figure_*.pdf
	latexmk -pdf -pdflatex="pdflatex -interaction=monostopmode" -use-make $<

Figure_*.pdf: plots_canal_ionico.py Data.txt 
	python $<

Data*.txt: canal_ionico.x
	./canal_ionico.x > Data.dat

DifusionTemperature: canal_ionico.c
	cc canal_ionico.c -lm -o canal_ionico.x
