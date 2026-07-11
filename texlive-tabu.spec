%global tl_name tabu
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.9
Release:	%{tl_revision}.1
Summary:	Flexible LaTeX tabulars
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tabu
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabu.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabu.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabu.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(varwidth)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an environment, tabu, which will make any sort of
tabular (that doesn't need to split across pages), and an environment
longtabu which provides the facilities of tabu in a modified longtable
environment. (Note that this latter offers an enhancement of ltxtable.)
The package requires the array package, and needs e-TeX to run (since
array.sty is present in every conforming distribution of LaTeX, and
since every publicly available LaTeX format is built using e-TeX, the
requirements are provided by default on any reasonable system). The
package also requires xcolor for coloured rules in tables, and colortbl
for coloured cells. The longtabu environment further requires that
longtable be loaded. The package itself does not load any of these
packages for the user. The tabu environment may be used in place of
tabular, tabular* and tabularx environments, as well as the array
environment in maths mode. It overloads tabularx's X-column
specification, allowing a width specification, alignment (l, r, c and j)
and column type indication (p, m and b). \begin{tabu} to <dimen>
specifies a target width, and \begin{tabu} spread <dimen> enlarges the
environment's "natural" width.

