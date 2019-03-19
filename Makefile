
publications.html: Makefile
	rm -rf temp/ publications.html
	mkdir temp
	cat publications-*.bib >temp/aspect.bib
	cp jabref-template/* temp/
	docker run --rm -v "$(PWD)/temp:/home/bob/source" tjhei/dealii-java-jabref
	sed '/publications.include/q' temp/output.html >publications.html
	cat publications.include >>publications.html
	sed -n '/publications.include/,$$p' temp/output.html >>publications.html
	sed -i '/publications.include/d' publications.html
	rm -rf temp/

# for now always force a rebuild:
.PHONY: publications.html
