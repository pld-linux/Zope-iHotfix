
%define		zope_subname	iHotfix
Summary:	Dynamically applying several patches to Zope
Summary(pl):	Dodatek aplikuj±cy wiele poprawek dla Zope
Name:		Zope-%{zope_subname}
Version:	0.7.0
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://download.ikaaro.org/ihotfix/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	07a438b14e550e6e37271f34e098bbd6
URL:		http://www.ikaaro.org/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope >= 2.6
Requires:	python-itools >= 0.9.0
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It dynamically applies several patches to Zope.

%description -l pl
Dodatek aplikuj±cy wiele poprawek dla Zope.

%prep
%setup -q -n %{zope_subname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

# should tests be included or not?
cp -af *.py version.txt $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt Changelog
%{_datadir}/%{name}
