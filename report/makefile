pdf: report.tex 
	pdflatex report.tex
	open report.pdf

pdfwithbib: report.tex bibdb.bib
	pdflatex report.tex
	bibtex report
	pdflatex report.tex
	pdflatex report.tex
	open report.pdf
