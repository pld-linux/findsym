Summary:	Tools to manipulate ELF files
Summary(pl):	Narz�dzia do obr�bki plik�w ELF
Name:		findsym
Version:	1.1
Release:	1
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Source0:	http://meatloop.andover.net/~count/src/%{name}-%{version}.tar.gz
URL:		http://freshmeat.net/projects/findsym/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program will attempt to search through all your shared libraries
for a specific symbol. This is useful when trying to compile something
and the compiler complains about an undefined reference similar to
this: /tmp/cceuy0nE.o(.text+0x7): undefined reference to `foo' Running
"findsym foo" would try to locate the symbol foo and indicate what
library you should be linking with.

%description -l pl
Ten program pr�buje szuka� okre�lonego symbolu we wszystkich
bibliotekach wsp�dzielonych. Jest przydatny, kiedy pr�bujemy co�
skompilowa�, a kompilator narzeka na niezdefiniowny symbol w spos�b
podobny do: /tmp/cceuy0nE.o(.text+0x7): undefined reference to `foo'.
Uruchomienie "findsym foo" spr�buje odnale�� symbol foo i
zidentyfikowa� bibliotek�, z kt�r� program powinien by� linkowany.

%prep
%setup -q -n findsym

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install findsym $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
