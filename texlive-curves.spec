Name:		texlive-curves
Version:	1.53
Release:	1
Summary:	Curves for LaTeX picture environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/curves
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/curves.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/curves.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/curves.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The draws curves in the standard LaTeX picture environment
using parabolas between data points with continuous slope at
joins; for circles and arcs, it uses up to 16 parabolas. The
package also draws symbols or dash patterns along curves. The
package provides facilities equivalent to technical pens with
compasses and French curves. Curves consist of short secants
drawn by overlapping disks or line-drawing \special commands
selected by package options.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/curves/curves.sty
%{_texmfdistdir}/tex/latex/curves/curvesls.sty
%doc %{_texmfdistdir}/doc/latex/curves/README
%doc %{_texmfdistdir}/doc/latex/curves/curves.pdf
%doc %{_texmfdistdir}/doc/latex/curves/latex2pdf
#- source
%doc %{_texmfdistdir}/source/latex/curves/curves.dtx
%doc %{_texmfdistdir}/source/latex/curves/curves.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
