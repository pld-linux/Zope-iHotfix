
%define		zope_subname	iHotfix
Summary:	Dynamically applying several patches to Zope
Summary(pl):	Dodatek aplikuj±cy wiele poprawek dla Zope
Name:		Zope-%{zope_subname}
Version:	0.5.0
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/lleu/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	d6d7f44965e4643de3a6f46fab24b3c9
URL:		http://www.ikaaro.org/
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope >= 2.6
Requires:	python-itools >= 0.5.0
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
cp -af *.py $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc TODO.txt README.txt
%{_datadir}/%{name}
