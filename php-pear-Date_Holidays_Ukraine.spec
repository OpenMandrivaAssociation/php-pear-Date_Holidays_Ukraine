%define		_class		Date
%define		_subclass	Holidays
%define		_region		Ukraine
%define		upstream_name	%{_class}_%{_subclass}_%{_region}

Name:		php-pear-%{upstream_name}
Version:	0.1.2
Release:	7
Summary:	Driver based class to calculate holidays in %{_region}
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/%{upstream_name}/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-pear-Date_Holidays >= 0.21.1
BuildArch:	noarch
BuildRequires:	php-pear

%description
%{upstream_name} is the Date_Holidays driver for %{_region} region.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.2-5mdv2012.0
+ Revision: 741930
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.2-4
+ Revision: 679312
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.2-3mdv2011.0
+ Revision: 613652
- the mass rebuild of 2010.1 packages

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.2-2mdv2010.1
+ Revision: 479281
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.1.2-1mdv2009.1
+ Revision: 368153
- Add spec and source files for php-pear-Date_Holidays_Ukraine
- Update inscorrect package name
- Add new splited php-pear-Date_Holidays package upstream structure

