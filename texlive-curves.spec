%global tl_name curves
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.55
Release:	%{tl_revision}.1
Summary:	Curves for LaTeX picture environment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/curves
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/curves.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/curves.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/curves.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package draws curves in the standard LaTeX picture environment
using parabolas between data points with continuous slope at joins; for
circles and arcs, it uses up to 16 parabolas. The package can also draw
symbols or dash patterns along curves. The package provides facilities
equivalent to technical pens with compasses and French curves. Curves
consist of short secants drawn by overlapping disks or line-drawing
\special commands selected by package options.

