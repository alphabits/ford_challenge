pdf: report.tex 
	pdflatex report.tex

pdfwithbib: report.tex bibdb.bib
	pdflatex report.tex
	bibtex report
	pdflatex report.tex
	pdflatex report.tex
