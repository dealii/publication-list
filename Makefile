
publications.html: Makefile
	rm -rf temp/ publications.html
	mkdir temp
	cat publications-*.bib >temp/aspect.bib
	cp jabref-template/* temp/
	docker run --rm -v "$(PWD)/temp:/home/bob/source" tjhei/dealii-java-jabref
	cp temp/output.html publications.html
	rm -rf temp/

# for now always force a rebuild:
.PHONY: publications.html
