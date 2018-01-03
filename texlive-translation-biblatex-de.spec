Name:		texlive-translation-biblatex-de
Version:	3.0
Release:	1
Summary:	German translation of the documentation of biblatex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/biblatex/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-biblatex-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-biblatex-de.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A German translation of the documentation of biblatex.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/translation-biblatex-de

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
