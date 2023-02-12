FROM ubuntu:22.04

MAINTAINER timo.heister@gmail.com

USER root


RUN apt-get update && DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -yq install \
    graphviz python3 flex bison make git cmake g++ wget \
    texlive biber bibtool \
    texlive-latex-extra texlive-fonts-recommended latexmk cm-super

# fix weird biber warnings about uninitialized values:
RUN sed -i '1s|.*|#!/usr/bin/perl|' /usr/bin/biber

ENV doxygen_version Release_1_8_12
#ENV doxygen_version Release_1_8_13 version produces a segfault

RUN \
    git clone -b ${doxygen_version} --depth 1 https://github.com/doxygen/doxygen.git && \
    cd doxygen && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    make install && \
    cd ../.. && \
    rm -rf doxygen

# make a user

ARG USER=bob
RUN adduser --disabled-password --gecos '' $USER
RUN adduser $USER sudo; echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
RUN chown -R $USER:$USER /home/$USER
USER $USER
ENV HOME /home/$USER
ENV USER $USER
WORKDIR $HOME
