Summary:	Tools to manipulate ELF files
Summary(pl.UTF-8):	Narzędzia do obróbki plików ELF
Name:		findsym
Version:	1.1
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://meatloop.andover.net/~count/src/%{name}-%{version}.tar.gz
# Source0-md5:	406cbeb14b87b419b25593e1a4199e18
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

%description -l pl.UTF-8
Ten program próbuje szukać określonego symbolu we wszystkich
bibliotekach współdzielonych. Jest przydatny, kiedy próbujemy coś
skompilować, a kompilator narzeka na niezdefiniowany symbol w sposób
podobny do: /tmp/cceuy0nE.o(.text+0x7): undefined reference to `foo'.
Uruchomienie "findsym foo" spróbuje odnaleźć symbol foo i
zidentyfikować bibliotekę, z którą program powinien być konsolidowany.

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
%doc CHANGES
%attr(755,root,root) %{_bindir}/*
