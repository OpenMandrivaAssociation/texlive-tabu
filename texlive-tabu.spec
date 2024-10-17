Name:		texlive-tabu
Version:	61719
Release:	2
Summary:	Flexible LaTeX tabulars
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tabu
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabu.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabu.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabu.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/tabu
%doc %{_texmfdistdir}/doc/latex/tabu
#- source
%doc %{_texmfdistdir}/source/latex/tabu

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
