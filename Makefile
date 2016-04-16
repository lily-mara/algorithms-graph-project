report.pdf : report.rst
	pandoc -o report.pdf report.rst -Vgeometry:margin=1in
