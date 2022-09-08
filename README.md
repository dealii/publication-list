[![Build Status](https://ci.tjhei.info/job/publication-list/job/master/badge/icon)](https://ci.tjhei.info/job/publication-list/job/master/)
[![download pdf](https://img.shields.io/badge/get-PDF-blue.svg)](https://ci.tjhei.info/job/publication-list/job/master/lastSuccessfulBuild/artifact/offline/publication_list.pdf)
[![view html](https://img.shields.io/badge/view-HTML-blue.svg)](https://ci.tjhei.info/job/publication-list/job/master/lastSuccessfulBuild/artifact/output.html)

# deal.II publication list
This repository contains a list of known publications that use or cite the [deal.II](https://www.dealii.org) finite element library. 
Its contents are used to generate the [publications mentioned on the deal.II website](https://www.dealii.org/publications.html).

Our institutes are evaluated at regular intervals. 
Consequently, we are interested in documenting the use of the programs and libraries we create. 
This page collects publications written on or with the help of deal.II.
If you have published anything, including Diploma, Masters or PhD theses, please let us know about it.
The more comprehensive this list is, the simpler it is for us to justify to our departments and sponsors the effort we put into the library — something that helps all of us in the end! 

## Adding a new publication

If you'd like to add a bibliographic entry to our `bibtex` list, this can be done by one of two means.
Firstly, you could email the details of your publication to one of the [principal developers or administrators](https://www.dealii.org/authors.html) of the deal.II library and we'll do it for you.
Alternatively, you could set up a pull request to this repository that adds the details of your awesome work.
This can be done online using [Github's built in editor](https://help.github.com/articles/editing-files-in-your-repository/) or with these easy steps (these steps are also detailed more thoroughly for our main repository on our [wiki page](https://github.com/dealii/dealii/wiki/Contributing)):
1. Fork this repository, thereby adding it to your own GitHub account.
2. Make a local clone of your repository.
```
$ git clone https://github.com/<github username>/publication-list
$ cd publication-list
```
If you already have a cloned version of the repository at hand, then synchronise the master branch of your fork with our repository
```
$ git checkout master
$ git remote add dealii git@github.com:dealii/publication-list.git
$ git fetch dealii
$ git rebase dealii master
$ git push origin master
```
3. Create a new branch on which to make your additions.
```
$ git checkout -b my_awesome_new_publication
```
4. Edit the file appropriate for the year of the publication.
Please try to select the correct entry type and to fill in as much of the mandatory fields for that selection.
You can see find more information about this point in this [Wikipedia entry](https://en.wikipedia.org/wiki/BibTeX#Entry_types).
If your publication has a URL or DOI number assigned to it, then it would be nice to enter that information as we will then generate a link straight to your publication.
5. Make sure that your entry is in the correct order and your citation key conforms to our style.
This step helps us to maintain the publication list and is completely automized.
You will need [bibtool](#installing-bibtool) and only have to call
```
$ make sort
```
6. Commit your changes to your local copy of the git repository.
```
$ git commit -m "Added entry <bibtex key>"
```
7. Push the changes to your fork of this repository
```
$ git push origin my_awesome_new_publication
```
8. Setup a pull request for your addition(s) within GitHub.

## Commonly used entry templates

To help you out, here are some templates for common entries:
- Article
```
@Article{<bibtex key>,
  author    = {},
  title     = {},
  journal   = {},
  year      = {},
  volume    = {},
  number    = {},
  pages     = {},
  doi       = {},
  url       = {},
}
```
- Article submitted to [arXiv.org](https://arxiv.org/)
```
@Article{<bibtex key>,
  author        = {},
  title         = {},
  journal       = {ArXiv e-prints}
  year          = {},
  volume        = {},
  number        = {},
  pages         = {},
  archiveprefix = {arXiv},
  eprint        = {<xxxx.xxxxx>},
  doi           = {},
  url           = {},
}
```
- Paper in conference proceedings
```
@InProceedings{<bibtex key>,
  author    = {},
  title     = {},
  editor    = {},
  booktitle = {},
  year      = {},
  volume    = {},
  series    = {},
  publisher = {},
  pages     = {},
  doi       = {},
  url       = {},
}
```
- Master's thesis
```
@MastersThesis{<bibtex key>,
  author    = {},
  title     = {},
  school    = {},
  year      = {},
  month     = {},
  url       = {},
}
```
- Bachelor's/Diploma thesis
We also use the `@MastersThesis` tag for all other kinds of theses
other than PhD theses, for example for Bachelor's or Honors theses in
the United States and similar university systems, and for Diploma
theses in universities that have them. In those case, simply fill in
the `note` tag as in the following example:
```
@MastersThesis{<bibtex key>,
  author    = {},
  title     = {},
  school    = {},
  year      = {},
  month     = {},
  url       = {},
  note      = {Bachelor's Thesis},
}
```
- PhD thesis
```
@PhdThesis{<bibtex key>,
  author    = {},
  title     = {},
  school    = {},
  year      = {},
  month     = {},
  url       = {},
}
```
- Technical report
```
@TechReport{<bibtex key>,
  author      = {},
  title       = {},
  institution = {},
  year        = {},
  url         = {},
}
```
- Chapter in a book
```
@InBook{<bibtex key>,
  chapter   = {},
  pages     = {},
  title     = {},
  publisher = {},
  year      = {},
  author    = {},
  volume    = {},
  number    = {},
  series    = {},
  edition   = {},
  isbn      = {},
  doi       = {},
  url       = {},
}
```
- Book
```
@Book{<bibtex key>,
  title     = {},
  publisher = {},
  year      = {},
  author    = {},
  volume    = {},
  number    = {},
  series    = {},
  edition   = {},
  isbn      = {},
  doi       = {},
  url       = {},
}
```
Please make sure that you complete as many of these fields as possible. 
It is a particular help to us to get the [DOI number](http://www.doi.org/) or a URL corresponding to your contribution.
A really useful resource that can be used to generate complete (or near complete) bibtex entries from DOI numbers and arXiv IDs is https://doi2bib.org.

#### Adding notes to publications
If you would like to add a contribution that has not yet been formally accepted, please add a comment to the note field indicating the status of your contribution.
This may be one of the following:
- for items that have been submitted but not yet reviewed:
```
note = {Submitted},
```
- for items that are currently undergoing peer review:
```
note = {In review},
```
- for items that have undergone review but are not yet at the publication stage:
```
note = {Accepted},
```
- for items that are in the final stages of publication (at this point they might have been assigned a DOI number):
```
note = {In press},
```
By adding these fields to your contribution, it will help us better maintain our database and help us determine when to update the status of your entry as it moves through the publication stage.
We would like to keep the status of your manuscripts as up-to-date as possible.

## Installing `bibtool`
[`bibtool`](http://www.gerd-neugebauer.de/software/TeX/BibTool/en/) is a tool for manipulating BibTeX databases, i.e., the actual `*.bib` files in which you store all literature entries.
We use it to format the publication list to keep it maintained. After installing `bibtool`, you can format the publication list.
```
make sort
```

### Installation via repositories
#### Linux
`bibtool` is available as a package in most [Linux distributions](https://pkgs.org/search/?q=bibtool).
#### macOS
You can install `bibtool` via [homebrew](https://formulae.brew.sh/formula/bib-tool) or [macports](https://ports.macports.org/port/BibTool/).
#### Windows
Use Windows WSL and follow the Linux instructions.

### Manual installation
If you need to install `bibtool` manually, follow these instructions.
1. Download and extract the [latest release tarball](http://www.gerd-neugebauer.de/software/TeX/BibTool/BibTool-2.68.tar.gz).
2. Autoconfigure the package and provide the directory where you want to install `bibtool`.
3. Compile and install the package.
4. Make sure `bibtool` is accessible in your system path variable.
```
wget http://www.gerd-neugebauer.de/software/TeX/BibTool/BibTool-2.68.tar.gz
tar xfz BibTool-2.68.tar.gz
cd BibTool
./configure --prefix=/path/to/bibtool
make install
echo "export PATH=$PATH:/path/to/bibtool/bin" >> ~/.bashrc
```
After the installation succeeded, make sure that you can call `bibtool` from your terminal.
```
$ bibtool -V
BibTool Vers. 2.68 (C) 1996-2019 Gerd Neugebauer

Library path: .:/path/to/bibtool/lib/BibTool
Special configuration options: none
```

## A final word...

Thank you very much for your contribution! We appreciate any entries to the list, as well as maintenance for the existing entries.
