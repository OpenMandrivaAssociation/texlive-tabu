# revision 21534
# category Package
# catalog-ctan /macros/latex/contrib/tabu
# catalog-date 2011-02-27 12:23:54 +0100
# catalog-license lppl1.3
# catalog-version 2.8
Name:		texlive-tabu
Version:	2.8
Release:	6
Summary:	Flexible LaTeX tabulars
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tabu
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabu.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabu.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabu.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an environment, tabu, which will make any
sort of tabular (that doesn't need to split across pages), and
an environment longtabu which provides the facilities of tabu
in a modified longtable environment. (Note that this latter
offers an enhancement of ltxtable.) The package requires the
array package, and needs e-TeX to run (since array.sty is
present in every conforming distribution of LaTeX, and since
every publicly available LaTeX format is built using e-TeX, the
requirements are provided by default on any reasonable system).
The package also requires xcolor for coloured rules in tables,
and colortbl for coloured cells. The longtabu environment
further requires that longtable be loaded. The package itself
does not load any of these packages for the user. The tabu
environment may be used in place of tabular, tabular* and
tabularx environments, as well as the array environment in
maths mode. It overloads tabularx's X-column specification,
allowing a width specification, alignment (l, r, c and j) and
column type indication (p, m and b). \begin{tabu} to <dimen>
specifies a target width, and \begin{tabu} spread <dimen>
enlarges the environment's "natural" width.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tabu/tabu.sty
%doc %{_texmfdistdir}/doc/latex/tabu/README
%doc %{_texmfdistdir}/doc/latex/tabu/tabu.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tabu/tabu.drv
%doc %{_texmfdistdir}/source/latex/tabu/tabu.dtx
%doc %{_texmfdistdir}/source/latex/tabu/tabu.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
