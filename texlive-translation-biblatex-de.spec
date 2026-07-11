%global tl_name translation-biblatex-de
%global tl_revision 59382

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.15b
Release:	%{tl_revision}.1
Summary:	German translation of the User Guide for BibLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/translations/biblatex/de
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-biblatex-de.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-biblatex-de.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A German translation of the User Guide for BibLaTeX.

