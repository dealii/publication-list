# deal.II publication list
This repository contains a list of known publications that use or cite the [deal.II](https://www.dealii.org) finite element library. 
Its contents are used to generate the publications mentioned on the [deal.II website](https://www.dealii.org/publications.html).

Our institutes are evaluated at regular intervals. 
Consequently, we are interested in documenting the use of the programs and libraries we create. 
This page collects publications written on or with the help of deal.II.
If you have published anything, including Diploma, Masters or PhD theses, please let us know about it.
The more comprehensive this list is, the simpler it is for us to justify to our departments and sponsors the effort we put into the library — something that helps all of us in the end! 

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

Thank you very much for your contribution! We appreciate any entries to the list, as well as maintenance for the existing entries.
