%global php_base php56u
%global php_basever 5.6
%global _php5_mod_dir %{_libdir}/php/modules


# [ionCube Loader] The Loader must appear as the first entry in the php.ini file
%global ininame 01-ioncube-loader.ini

Name:       %{php_base}-ioncube-loader
Summary:    IonCube Loader provides PHP Modules to read IonCube Encoded Files
Version:    5.1.1
Release:    1.ius%{?dist}
License:    Redistributable, no modification permitted
URL:        http://www.ioncube.com
Group:      Development/Languages
# the files in the source are pre-complied for 32bit and 64bit
# we must include both sources so the resulting srpm can build for either arch
Source0:    http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86.tar.gz
Source1:    http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
BuildRequires: %{php_base}-devel
Requires:   %{php_base}(api) = %{php_core_api}
Conflicts:  php-ioncube-loader < %{version}
Provides:   php-ioncube-loader = %{version}-%{release}


%description
IonCube Loader provides PHP Modules to read IonCube Encoded Files


%prep 
%ifarch %{ix86}
%setup -q -T -b 0 -n ioncube
%endif
%ifarch x86_64
%setup -q -T -b 1 -n ioncube
%endif


%build
# Nothing to do here


%install
%{__mkdir_p} %{buildroot}%{_php5_mod_dir} \
             %{buildroot}/%{_sysconfdir}/php.d

# Install the shared objects
install -m 755 ioncube_loader_lin_%{php_basever}.so %{buildroot}%{_php5_mod_dir}
install -m 755 ioncube_loader_lin_%{php_basever}_ts.so %{buildroot}%{_php5_mod_dir}

%{__cat} >> %{buildroot}/%{_sysconfdir}/php.d/%{ininame} <<EOF

; Configured for PHP ${php_basever}
zend_extension=%{_php5_mod_dir}/ioncube_loader_lin_%{php_basever}.so

; For threaded Apache/PHP Implementations comment out the above
; and un-comment the following:
;
; zend_extension=%{_php5_mod_dir}/ioncube_loader_lin_%{php_basever}_ts.so
;
EOF


%files
%doc README.txt LICENSE.txt
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.d/%{ininame}
%{_php5_mod_dir}/ioncube_loader_lin_%{php_basever}.so
%{_php5_mod_dir}/ioncube_loader_lin_%{php_basever}_ts.so


%changelog
* Mon Feb 08 2016 Ben Harper <ben.harper@rackspace.com> - 5.1.1-1.ius
- Latest upstream

* Fri Jan 22 2016 Ben Harper <ben.harper@rackspace.com> - 5.0.22-1.ius
- Latest upstream

* Wed Jan 20 2016 Ben Harper <ben.harper@rackspace.com> - 5.0.21-1.ius
- Latest upstream

* Mon Jan 18 2016 Ben Harper <ben.harper@rackspace.com> - 5.0.20-1.ius
- Latest upstream

* Tue Oct 20 2015 Carl George <carl.george@rackspace.com> - 5.0.19-1.ius
- Latest upstream

* Tue Sep 15 2015 Carl George <carl.george@rackspace.com> - 5.0.18-1.ius
- Latest upstream

* Thu Aug 27 2015 Carl George <carl.george@rackspace.com> - 5.0.16-1.ius
- Latest upstream

* Wed Aug 12 2015 Ben Harper <ben.harper@rackspace.com> - 5.0.14-1.ius
- Latest upstream

* Tue Jul 28 2015 Ben Harper <ben.harper@rackspace.com> - 5.0.13.-1.ius
- Latest upstream

* Wed Jul 15 2015 Carl George <carl.george@rackspace.com> - 5.0.12-1.ius
- Latest upstream

* Tue Jun 30 2015 Carl George <carl.george@rackspace.com> - 5.0.11-1.ius
- Latest upstream
- Port from php55u-ioncube-loader

* Tue Jun 16 2015 Ben Harper <ben.harper@rackspace.com> - 5.0.8-1.ius
- Latest upstream

* Tue May 26 2015 Ben Harper <ben.harper@rackspace.com> - 5.0.7-1.ius
- Latest upstream

* Fri May 08 2015 Ben Harper <ben.harper@rackspace.com> - 5.0.4-1.ius
- Latest upstream
- disable debuginfo

* Tue Mar 24 2015 Carl George <carl.george@rackspace.com> - 4.7.5-2.ius
- Depend on php(api), not mod_php
- Prefix ini file with '01-' to ensure it loads first

* Mon Mar 02 2015 Carl George <carl.george@rackspace.com> - 4.7.5-1.ius
- Latest upstream
- Re-added README.txt and LICENSE.txt

* Tue Feb 17 2015 Carl George <carl.george@rackspace.com> - 4.7.4-1.ius
- Latest upstream

* Thu Feb 05 2015 Ben Harper <ben.harper@rackspace.com> - 4.7.3-1.ius
- Latest sources from upstream

* Wed Nov 26 2014 Carl George <carl.george@rackspace.com> - 4.7.2-2.ius
- Port from php54 to php55u

* Tue Nov 25 2014 Carl George <carl.george@rackspace.com> - 4.7.2-1.ius
- Latest upstream

* Mon Nov 03 2014 Carl George <carl.george@rackspace.com> - 4.7.1-1.ius
- Latest upstream

* Mon Oct 20 2014 Ben Harper <ben.harper@rackspace.com> - 4.7.0-1.ius
- Latest upstream

* Thu Oct 16 2014 Carl George <carl.george@rackspace.com> - 4.6.2-1.ius
- Latest upstream

* Wed Apr 23 2014 Carl George <carl.george@rackspace.com> - 4.6.1-1.ius
- docs are back in tarball
- add noreplace option to ioncube-loader.ini
- latest sources from upstream

* Mon Apr 07 2014 Ben Harper <ben.harper@rackspace.com> - 4.6.0-1.ius
- Latest sources from upstream

* Wed Feb 12 2014 Ben Harper <ben.harper@rackspace.com> - 4.5.3-1.ius
- Latest sources from upstream

* Mon Jan 20 2014 Ben Harper <ben.harper@rackspace.com> - 4.5.2-1.ius
- Latest sources from upstream

* Mon Jan 06 2014 Ben Harper <ben.harper@rackspace.com> - 4.5.1-1.ius
- Latest sources from upstream

* Fri Dec 13 2013 Ben Harper <ben.harper@rackspace.com> - 4.5.0-1.ius
- Latest sources from upstream

* Wed Oct 16 2013 Ben Harper <ben.harper@rackspace.com> - 4.4.4-1.ius
- Latest sources from upstream

* Tue Sep 10 2013 Ben Harper <ben.harper@rackspace.com> - 4.4.3-1.ius
- Latest sources from upstream

* Thu Aug 29 2013 Ben Harper <ben.harper@rackspace.com> - 4.4.2-1.ius
- Latest sources from upstream

* Fri Jun 14 2013 Ben Harper <ben.harper@rackspace.com> - 4.4.1-1.ius
- Latest sources from upstream

* Mon May 06 2013 Ben Harper <ben.harper@rackspace.com> - 4.4.0-1.ius
- Latest upstream source

* Tue Aug 21 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.2.2-2.ius
- Rebuilding against php54-5.4.6-2.ius as it is now using bundled PCRE.

* Wed Jun 27 2012 D. H. Offutt <dustin.offutt@rackspace.com> - 4.2.2-1.ius
- Latest upstream source

* Wed May 23 2012 D. H. Offutt <dustin.offutt@rackspace.com> - 4.2.1-1.ius
- Latest upstream source

* Wed May 16 2012 D. H. Offutt <dustin.offutt@rackspace.com> - 4.2.0-1.ius
- Rebuild for php54 and latest ioncube-loader sources
- {README,LICENSE}.txt not included in tarball this release. Commented out.

* Tue Mar 13 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.0.14-1.ius
- Latest sources

* Mon Jan 23 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.0.12-2.ius
- Fixing Provides and Conflicts, reported in
  https://bugs.launchpad.net/ius/+bug/920178

* Tue Jan 03 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.0.12-1.ius
- Latest sources from upstream

* Mon Dec 12 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.0.11-1.ius
- Latest sources from upstream

* Fri Aug 19 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.0.10-3.ius
- Rebuilding

* Fri Aug 12 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.0.10-2.ius
- Rebuilding for EL6

* Tue Jul 19 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.0.10-1.ius
- Latest sources from upstream

* Tue Jun 07 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.0.9-1.ius
- Latest sources from upstream

* Thu Apr 21 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.0.8-1.ius
- Latest sources from upstream

* Mon Mar 21 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 4.0.7-1.ius
- Latest sources from upstream

* Thu Feb 03 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 3.3.17-3.ius
- Removed Obsoletes: php53*

* Mon Jan 03 2011 BJ Dierkes <wdierkes@rackspace.com> - 3.3.17-2.ius
- Rebuild for php53u
- Obsoletes: php53-ioncube-loader < 3.3.17-2

* Thu May 20 2010 BJ Dierkes <wdierkes@rackspace.com> - 3.3.17-1.ius
- Porting to IUS for the php53 package
- Removed files for other versions of PHP
 
* Thu Feb 05 2009 BJ Dierkes <wdierkes@rackspace.com> 3.1.32-2.rs
- Cleaned up trigger scripts a bit
- Changed Vendor tag to Rackspace US, Inc.
- Moved configuration file to /etc/php.d/01a-ioncube-loader.ini
- Added noreplace configuration file to /etc/php.d/01b-ioncube-loader.ini
- Requires: php-devel

* Sun May 18 2008 BJ Dierkes <wdierkes@rackspace.com> 3.1.32-1.rs
- Latest sources.
- Added a regex check for ioncube loader config in php.ini before
  setting up the ioncube-loader.ini (triggerin).  Resolves Rackspace 
  Bugs [#493] and [#393].

* Fri Jun 01 2007 BJ Dierkes <wdierkes@rackspace.com> 3.1.31-1.rs
- Latest sources

* Wed May 02 2007 BJ Dierkes <wdierkes@rackspace.com> 3.1.30-1.rs
- Latest sources

* Wed Apr 18 2007 BJ Dierkes <wdierkes@rackspace.com> 3.1.29-1.rs
- Latest sources
- Replace post script with triggerin script to always overwrite /etc/php.d/ioncube-loader.ini when php is upgraded
  to keep the right configuration.

* Fri Feb 23 2007 BJ Dierkes <wdierkes@rackspace.com> 3.1.28-1.1.rs
- Set 'replace' on config file
- Set PreReq php (PHP must install/upgrade first, as post script check 
  PHP version

* Wed Feb 21 2007 BJ Dierkes <wdierkes@rackspace.com> 3.1.28-1.rs
- Inital spec build
- Rewritten from partial spec submitted by Samuel Stringham
