latex: Makefile
	cd offline && pdflatex -interaction=nonstopmode publication_list.tex || true
	cd offline && biber publication_list
	cd offline && pdflatex -interaction=nonstopmode publication_list.tex || true
	cd offline && pdflatex -interaction=nonstopmode publication_list.tex

publications.html: Makefile
	rm -rf temp/ publications.html
	mkdir temp
	cat publications-????.bib >temp/aspect.bib
	cp jabref-template/* temp/
	docker run --rm -v "$(PWD)/temp:/home/bob/source" tjhei/dealii-java-jabref
	sed '/publications.include/q' temp/output.html >publications.html
	cat publications.include >>publications.html
	sed -n '/publications.include/,$$p' temp/output.html >>publications.html
	sed -i '/publications.include/d' publications.html
	rm -rf temp/

# remove jabref strings before calling bibtool to suppress warnings
sort: Makefile
	@if ! command -v bibtool > /dev/null ; then \
		echo "ERROR. Install bibtool to use this feature." >&2 ; \
		echo "Consult the README for instructions:" >&2 ; \
		echo "  https://github.com/dealii/publication-list#installing-bibtool" >&2 ; \
		exit 1 ; \
	fi ; \
	for f in publications-*.bib ; do \
		sed -i 's/% Encoding: US-ASCII//' $$f ; \
		bibtool -r bibtool.rsc -i $$f -o $$f ; \
		sed -i '1s/^/% Encoding: US-ASCII\n/' $$f ; \
		sed -i '$$s/$$/\n\n@Comment{jabref-meta: databaseType:bibtex;}/' $$f ; \
	done

# for now always force a rebuild:
.PHONY: publications.html latex
