docker run --rm -v $PWD/..:/src/ tjhei/dealii-doc-gen:v4 /bin/bash -c \
       " mkdir offline;
         cp /src/offline/publication_list.tex offline/
	 cp /src/publications-????.bib .
              cd offline
	      latexmk -f -pdf publication_list.tex || echo 'NOOO'
               grep WARN publication_list.blg && exit 1
	       echo ok"


