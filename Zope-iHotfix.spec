
%define		zope_subname	iHotfix
Summary:	Dynamically applying several patches to Zope
Summary(pl):	Dodatek aplikuj±cy wiele poprawek dla Zope
Name:		Zope-%{zope_subname}
Version:	0.4.0
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/lleu/%{zope_subname}-%{version}.tgz
# Source0-md5:	773ba7f4202c9230019622fbb67dbd1d
URL:		http://sourceforge.net/projects/lleu/
BuildRequires:	python >= 2.2
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope >= 2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It dynamically applies several patches to Zope.

%description -l pl
Dodatek aplikuj±cy wiele poprawek dla Zope.

%prep
%setup -q -n %{zope_subname}

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
%doc TODO.txt
%{_datadir}/%{name}
