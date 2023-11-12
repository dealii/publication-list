#!/usr/bin/python

import requests


def bibtex_from_dois(dois):
  """
  Create BibTeX entries from a given list of DOIs.

  Parameters
  ----------
  dois : container -> string
    Collection of DOIs.

  Returns
  -------
  resolved : list -> string
    BibTeX entries of DOIs that could be resolved.
  unresolved : list -> string
    DOIs that could not be resolved.
  """
  resolved, unresolved = [], []
  for doi in dois:
    if doi.isspace():
      continue
    # For DOI content negotiation, see https://citation.crosscite.org/docs.html
    try:
      response = requests.get("https://doi.org/{}".format(doi.strip()),
                              headers={"accept": "application/x-bibtex"},
                              timeout=5)
      if (response.status_code == 200):
        resolved.append(response.text)
      else:
        unresolved.append(doi)
    except requests.exceptions.Timeout:
      unresolved.append(doi)
  return resolved, unresolved


if __name__ == "__main__":
  """
  Creates BibTeX entries from multiple DOIs passed as separate arguments,
  or as part of a single textfile.

  Outputs BibTeX entries of resolved DOIs to stdout and directs
  unresolved DOIs to stderr.
  """
  import sys

  argc = len(sys.argv)
  if (argc < 2):
    print("Usage:\n{s} <doi1> <doi2> ...\n{s} <file>.txt".format(s=sys.argv[0]))
    sys.exit(1)

  if (argc == 2 and sys.argv[1].endswith(".txt")):
    dois = open(sys.argv[1], mode='r')
  else:
    dois = sys.argv[1:]

  resolved, unresolved = bibtex_from_dois(dois)

  for bib in resolved:
    print(bib)
  for doi in unresolved:
    print(doi, file=sys.stderr)
