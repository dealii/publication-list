[![Build Status](https://jenkins.tjhei.info/job/publication-list/job/master/badge/icon)](https://jenkins.tjhei.info/job/publication-list/job/master/)
[![download pdf](https://img.shields.io/badge/get-PDF-blue.svg)](https://tjhei.info/jenkins/publications.pdf)
[![view html](https://img.shields.io/badge/view-HTML-blue.svg)](https://tjhei.info/jenkins/output.html)

# deal.II publication list
This repository contains a list of known publications that use or cite the [deal.II](https://www.dealii.org) finite element library. 
Its contents are used to generate the publications mentioned on the [deal.II website](https://www.dealii.org/publications.html).

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
5. Commit your changes to your local copy of the git repository.
```
$ git commit -m "Added entry <bibtex key>"
```
6. Push the changes to your fork of this repository
```
$ git push origin my_awesome_new_publication
```
7. Setup a pull request for your addition(s) within GitHub.

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
  booktitle = {},
  year      = {},
  volume    = {},
  number    = {},
  pages     = {},
  doi       = {},
  url       = {},
}
```
- Bachelor's / Diploma thesis
```
@MastersThesis{<bibtex key>,
  author    = {},
  title     = {},
  school    = {},
  year      = {},
  month     = {},
  url       = {},
  note      = {<Bachelor Thesis/Diploma Thesis/Honors thesis/Project thesis/...>},
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

## A final word...

Thank you very much for your contribution! We appreciate any entries to the list, as well as maintenance for the existing entries.
