Summary:        Theme engines for GTK+ 2.0
Name:           gtk2-engines
Version:        2.18.4
Release:	5%{?dist}
# for details on which engines are GPL vs LGPL, see COPYING
License:        LGPLv2+
Group:          System Environment/Libraries
Source:         http://download.gnome.org/sources/gtk-engines/2.18/gtk-engines-%{version}.tar.bz2

Conflicts:  	gnome-themes < 2.9.0
Obsoletes:      gnome-theme-clearlooks <= 0.5

BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  gettext
BuildRequires:  pkgconfig

URL:           	http://download.gnome.org/sources/gtk-engines
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# http://bugzilla.gnome.org/show_bug.cgi?id=593030
Patch0: gtk-engines-2.18.2-change-bullet.patch

Patch1: tooltips.patch

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
The gtk2-engines-devel package contains files needed to develop
software that uses the theme engines in the gtk2-engines package.


%description
The gtk2-engines package contains shared objects and configuration
files that implement a number of GTK+ theme engines. Theme engines
provide different looks for GTK+, some of which resemble other
toolkits or operating systems.

%prep
%setup -q -n gtk-engines-%{version}

%patch0 -p1 -b .change-bullet
%patch1 -p1 -b .tooltips

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# no .la, please
find $RPM_BUILD_ROOT%{_libdir} -name "*.la" | xargs rm

# sanitize permissions
find $RPM_BUILD_ROOT%{_datadir}/themes -type d -exec chmod 755 {} \;
find $RPM_BUILD_ROOT%{_datadir}/themes -type f -name "*.png" -exec chmod 644 {} \;
find $RPM_BUILD_ROOT%{_datadir}/themes -name "gtkrc*" -perm +111 -exec chmod 644 {} \;

# no thanks
rm -rf $RPM_BUILD_ROOT%{_datadir}/themes/Redmond
rm -rf $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.4.0/engines/libredmond95.so

%find_lang gtk-engines

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gtk-engines.lang
%defattr(644, root, root, 755)
%doc README AUTHORS NEWS COPYING
%attr (755, root, root) %{_libdir}/gtk-2.0/2.10.0/engines/*.so
%{_datadir}/themes/*
%{_datadir}/gtk-engines

%files devel
%defattr(644, root, root, 755)
%{_libdir}/pkgconfig/gtk-engines-2.pc

%changelog
* Fri Jun 18 2010 Matthias Clasen <mclasen@redhat.com> - 2.18.4-5
- Remove a bogus Requires
Resolves: #605055

* Fri Oct 23 2009 Matthias Clasen <mclasen@redhat.com> - 2.18.4-4
- Make Clearlooks opt-in to new tooltips style

* Wed Oct 21 2009 Matthias Clasen <mclasen@redhat.com> - 2.18.4-3
- Tweak tooltip appearance

* Tue Oct 20 2009 Matthias Clasen <mclasen@redhat.com> - 2.18.4-2
- New tooltip appearance

* Tue Sep 29 2009 Matthias Clasen <mclasen@redhat.com> - 2.18.4-1
- Update to 2.18.4

* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 2.18.3-1
- Update to 2.18.3

* Tue Aug 25 2009 Ray Strode <rstrode@redhat.com> - 2.18.2-5
- Change password asterisk character to be '•' instead of '●'

* Sun Aug  2 2009 Matthias Clasen <mclasen@redhat.com> - 2.18.2-4
- Drop pkgconfig dep from the main package

* Wed Jul 29 2009 Matthias Clasen <mclasen@redhat.com> - 2.18.2-3
- Fix the build

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 20 2009 Ray Strode <rstrode@redhat.com> - 2.18.2-1
- Update to 2.18.2
- See http://download.gnome.org/sources/gtk-engines/2.18/gtk-engines-2.18.2.news

* Mon Apr 13 2009 Matthias Clasen <mclasen@redhat.com> - 2.18.1-1
- Update to 2.18.1
- See http://download.gnome.org/sources/gtk-engines/2.18/gtk-engines-2.18.1.news

* Mon Mar 16 2009 Matthias Clasen <mclasen@redhat.com> - 2.18.0-1
- Update to 2.18.0

* Mon Mar  2 2009 Matthias Clasen <mclasen@redhat.com> - 2.17.4-1
- Update to 2.17.4

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Matthias Clasen <mclasen@redhat.com> - 2.17.3-1
- Update to 2.17.3

* Sat Dec 13 2008 Matthias Clasen <mclasen@redhat.com> - 2.17.2-1
- Update to 2.17.2

* Mon Dec  8 2008 Matthias Clasen <mclasen@redhat.com> - 2.17.1-2
- Add a -devel package to trim excessive pkg-config autodeps

* Wed Dec  3 2008 Matthias Clasen <mclasen@redhat.com> - 2.17.1-1
- Update to 2.17.1

* Wed Nov 12 2008 Matthias Clasen <mclasen@redhat.com> - 2.17.0-1
- Update to 2.17.0

* Mon Oct 20 2008 Matthias Clasen <mclasen@redhat.com> - 2.16.1-1
- Update to 2.16.1

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.16.0-1
- Update to 2.16.0

* Tue Sep  2 2008 Matthias Clasen <mclasen@redhat.com> - 2.15.4-1
- Update to 2.15.4

* Fri Aug 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.15.3-1
- Update to 2.15.3

* Mon Aug  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.15.2-1
- Update to 2.15.2

* Tue May 13 2008 Matthias Clasen <mclasen@redhat.com> - 2.15.1-1
- Update to 2.15.1

* Fri Apr 25 2008 Matthias Clasen <mclasen@redhat.com> - 2.15.0-1
- Update to 2.15.0

* Mon Apr  7 2008 Matthias Clasen <mclasen@redhat.com> - 2.14.1-1
- Update to 2.14.1

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.14.0-1
- Update to 2.14.0

* Mon Feb 25 2008 Matthias Clasen <mclasen@redhat.com> - 2.13.6-1
- Update to 2.13.6

* Tue Feb 12 2008 Matthias Clasen <mclasen@redhat.com> - 2.13.5-1
- Update to 2.13.5

* Mon Jan 28 2008 Matthias Clasen <mclasen@redhat.com> - 2.13.4-1
- Update to 2.13.4

* Tue Jan 08 2008 - Bastien Nocera <bnocera@redhat.com> - 2.13.3-1
- Update to 2.13.3

* Tue Dec 18 2007 Matthias Clasen <mclasen@redhat.com> - 2.13.2-1
- Update to 2.13.2

* Wed Dec  5 2007 Matthias Clasen <mclasen@redhat.com> - 2.13.1-1
- Update to 2.13.1

* Mon Nov 12 2007 Matthias Clasen <mclasen@redhat.com> - 2.13.0-1
- Update to 2.13.0 

* Mon Oct 15 2007 Matthias Clasen <mclasen@redhat.com> - 2.12.2-1
- Update to 2.12.2 (bug fixes and translation updates)

* Thu Sep 20 2007 Matthias Clasen <mclasen@redhat.com> - 2.12.0-2
- Fix a typo in the Crux gtkrc

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.12.0-1
- Update to 2.12.0

* Mon Sep  3 2007 Matthias Clasen <mclasen@redhat.com> - 2.11.7-1
- Update to 2.11.7

* Thu Aug 16 2007 Matthias Clasen <mclasen@redhat.com> - 2.11.6-1
- Update to 2.11.6

* Mon Aug 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.11.5-1
- Update to 2.11.5

* Fri Aug  3 2007 Matthias Clasen <mclasen@redhat.com> - 2.11.4-2
- Update the license field

* Mon Jul 30 2007 Matthias Clasen <mclasen@redhat.com> - 2.11.4-1
- Update to 2.11.4

* Tue Jul 10 2007 Matthias Clasen <mclasen@redhat.com> - 2.11.3-1
- Update to 2.11.3

* Thu Jun 21 2007 Matthias Clasen <mclasen@redhat.com> - 2.11.2-2
- Make the new tooltip api yellow, too

* Mon Jun 18 2007 Matthias Clasen <mclasen@redhat.com> - 2.11.2-1
- Update to 2.11.2

* Thu Jun  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.11.1-2
- Keep the default tooltip color for Clearlooks
- Fix up directory ownership 

* Mon Jun  4 2007 Matthias Clasen <mclasen@redhat.com> - 2.11.1-1
- Update to 2.11.1

* Sat May 19 2007 Matthias Clasen <mclasen@redhat.com> - 2.11.0-1
- Update to 2.11.0
- Drop obsolete patches

* Tue May 15 2007 Matthias Clasen <mclasen@redhat.com> - 2.10.0-3
- Fix some memory corruption errors 

* Wed Apr 25 2007 Matthias Clasen <mclasen@redhat.com> - 2.10.0-2
- Remove and undefined macro (#237810)

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.10.0-1
- Update to 2.10.0

* Tue Feb 27 2007 Matthias Clasen <mclasen@redhat.com> - 2.9.4-2
- Add a knob to Clearlooks to make scrollbars work better 
  in dark themes, needed for the gdm theme

* Mon Feb 26 2007 Matthias Clasen <mclasen@redhat.com> - 2.9.4-1
- Update to 2.9.4

* Wed Feb 21 2007 Matthias Clasen <mclasen@redhat.com> - 2.9.3-2
- Fix the active checkbox drawing bug

* Mon Feb 12 2007 Matthias Clasen <mclasen@redhat.com> - 2.9.3-1
- Update to 2.9.3

* Mon Jan 22 2007 Matthias Clasen <mclasen@redhat.com> - 2.9.2-1
- Update to 2.9.2

* Wed Jan 10 2007 Matthias Clasen <mclasen@redhat.com> - 2.9.1-1
- Update to 2.9.1

* Tue Dec  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.9.0-1
- Update to 2.9.0

* Thu Nov 16 2006 Matthias Clasen <mclasen@redhat.com> - 2.8.2-1
- Update to 2.8.2

* Sat Oct 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.8.1-1
- Update to 2.8.1

* Mon Sep  4 2006 Matthias Clasen <mclasen@redhat.com> - 2.8.0-1.fc6
- Update to 2.8.0

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.7.8-1.fc6
- Update to 2.7.8

* Sat Aug 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.7.7-1.fc6
- Update to 2.7.7

* Wed Aug  2 2006 Matthias Clasen <mclasen@redhat.com> - 2.7.6-1.fc6
- Update to 2.7.6

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.7.5-1.1
- rebuild

* Wed Jul 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.7.5-1
- Update to 2.7.5

* Fri May  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.7.4-4
- Rebuild against GTK+ 2.9.0
- Require GTK+ 2.9.0

* Mon Apr 19 2006 Soren Sandmann <sandmann@redhat.com> - 2.7.4-6
- It was in fact a missing copy method. See gnome bug 338826.

* Tue Apr 18 2006 Kristian Høgsberg <krh@redhat.com> 2.7.4-5
- Bump for fc5-blig repo build.

* Mon Apr 17 2006 Soren Sandmann <sandmann@redhat.com> - 2.7.4-4
- Add missing clone method in the Clearlooks engine

* Sun Feb 26 2006 Matthias Clasen <mclasen@redhat.com> - 2.7.4-3
- Fix memory leaks in the Clearlooks engine

* Fri Feb 24 2006 Matthias Clasen <mclasen@redhat.com> - 2.7.4-2
- Backport patches to draw default buttons and
  inconsistent checkboxes

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.7.4-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.7.4-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 30 2006 Matthias Clasen <mclasen@redhat.com> 2.7.4-1
- Update to 2.7.4

* Thu Jan 19 2006 Matthias Clasen <mclasen@redhat.com> 2.7.3-1
- Update to 2.7.3

* Tue Jan 10 2006 Ray Strode <rstrode@redhat.com> 2.7.2-2
- fix handle drawing bugs from F-Spot and gnome-panel
- change %%makeinstall to make install DESTDIR=...

* Tue Jan 03 2006 Matthias Clasen <mclasen@redhat.com> 2.7.2-1
- Update to 2.7.2

* Wed Dec 14 2005 Matthias Clasen <mclasen@redhat.com> 2.7.1-1
- Update to 2.7.1

* Sun Dec 11 2005 Matthias Clasen <mclasen@redhat.com> 2.7.0-2
- Backport some fixes from upstream 

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 30 2005 Matthias Clasen <mclasen@redhat.com> 2.7.0-1
- Update to 2.7.0

* Wed Sep  7 2005 Matthias Clasen <mclasen@redhat.com> 2.6.5-1
- Update to 2.6.5

* Tue Aug 16 2005 Matthias Clasen <mclasen@redhat.com> 
- Rebuilt

* Thu Aug  4 2005 Matthias Clasen <mclasen@redhat.com> 2.6.4-1
- New upstream version

* Tue Jun 28 2005 Matthias Clasen <mclasen@redhat.com> 2.6.3-3
- Update Clearlooks to 0.6.1

* Fri May 20 2005 Matthias Clasen <mclasen@redhat.com> 2.6.3-2
- Don't ship Redmond

* Tue Apr 19 2005 Matthias Clasen <mclasen@redhat.com> 2.6.3-1
- Update to 2.6.3
- Clearlooks engine is now integrated

* Sun Apr 03 2005 Warren Togami <wtogami@redhat.com> 2.6.2-4
- obsolete FE3 gnome-theme-clearlooks to ensure smooth upgrade

* Tue Mar 29 2005 Matthias Clasen <mclasen@redhat.com> 2.6.2-3
- Update to Clearlooks 0.5

* Thu Mar 17 2005 Matthias Clasen <mclasen@redhat.com> 2.6.2-2
- Include the Clearlooks engine, version 0.4

* Mon Mar 14 2005 Matthias Clasen <mclasen@redhat.com> 2.6.2-1
- Update to 2.6.2

* Wed Mar  2 2005 Matthias Clasen <mclasen@redhat.com> 2.6.1-2
- Rebuild with gcc4

* Wed Feb  9 2005 Matthias Clasen <mclasen@redhat.com> 2.6.1-1
- Update to 2.6.1

* Wed Jan 26 2005 Matthias Clasen <mclasen@redhat.com> 2.6.0-1
- update to 2.6.0

* Tue Dec 21 2004 Matthias Clasen <mclasen@redhat.com> 2.2.0-6
- remove pixbuf engine which is integrated in gtk+ 2.6

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Mar 17 2004 Alex Larsson <alexl@redhat.com> 2.2.0-5
- rebuilt to get new gtk binary age

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jan 17 2003 Owen Taylor <otaylor@redhat.com>
- Upgrade to 2.2.0 (Fixes #65985, #73475)
- Add the .pc file to the package

* Tue Dec 17 2002 Owen Taylor <otaylor@redhat.com>
- Rebuild for new GTK+

* Mon Dec  9 2002 Havoc Pennington <hp@redhat.com>
- rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 02 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Thu Apr 25 2002 Havoc Pennington <hp@redhat.com>
- converted to gtk2-engines package

* Mon Apr 15 2002 Alex Larsson <alexl@redhat.com>
- Added Adept-Raleigh theme

* Thu Apr 11 2002 Owen Taylor <otaylor@redhat.com>
- Fix major pixmap leak that occurred with certain theme/app 
  combinations (#59528)

* Wed Mar 13 2002 Owen Taylor <otaylor@redhat.com>
- Add gtk-hicontrast theme
- Un-automake-1.4

* Thu Jan 24 2002 Havoc Pennington <hp@redhat.com>
- remove acinclude.m4 to avoid funky libtool crackrock

* Tue Jan 22 2002 Havoc Pennington <hp@redhat.com>
- automake14

* Thu Aug  9 2001 Owen Taylor <otaylor@redhat.com>
- Install %{_sysconfdir}/skel/.gtkrc as /root/.gtkrc as well, or we 
  don't get Raleigh for our nice config tools

* Sat Jul 21 2001 Owen Taylor <otaylor@redhat.com>
- Add BuildPrereq on imlib-devel (#49478)

* Tue Jul 10 2001 Owen Taylor <otaylor@redhat.com>
- Version 0.11
- Install a %{_sysconfdir}/skel/.gtkrc

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Sat Feb 10 2001 Owen Taylor <otaylor@redhat.com>
- New, slightly improved version of Raleigh

* Sun Feb 04 2001 Owen Taylor <otaylor@redhat.com>
- Require as well as BuildPrereq a sufficiently new GTK+ package.

* Wed Jan 17 2001 Owen Taylor <otaylor@redhat.com>
- remove references to /home/raster from a couple of themes

* Tue Nov 21 2000 Owen Taylor <otaylor@redhat.com>
- Add 'Raleigh' theme

* Fri Aug 11 2000 Jonathan Blandford <jrb@redhat.com>
- Up Epoch and release

* Thu Jul 13 2000 Owen Taylor <otaylor@redhat.com>
- Go back to real gtk-engines-0.10.tar.gz instead of hosed
  cvs snapshot that someone had inserted.

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 19 2000 Dave Mason <dcm@redhat.com>
- Removed many themes to speed up control center and get rid of ugly themes

* Sat Jun 17 2000 Matt Wilson <msw@redhat.com>
- defattr files 644 and dirs 755, list attr of 755 for libraries explicitly
- use %%makeinstall
- remove spec file stupidism (defining docdir, using own prefix macro, rel, ver, etc)

* Tue May 16 2000 Dave Mason <dcm@redhat.com>
- fixed Tiger, RatsTheme, OldWood, and LCD themes as they had no gtk subdirectory

* Tue Feb 22 2000 Bill Nottingham <notting@redhat.com>
- sanitize various things (permissions, .xv thumbnails)

* Thu Feb 10 2000 Preston Brown <pbrown@redhat.com>
- remove backup files from package

* Tue Jan 25 2000 Owen Taylor <otaylor@redhat.com>
- Update to 0.10 (fixing problem with text in eventboxes
  becoming garbled)

* Wed Sep 15 1999 Elliot Lee <sopwith@redhat.com>
- Misc fixes from DrMike suggestions

* Thu Sep 09 1999 Elliot Lee <sopwith@redhat.com>
- Update to 0.6, etc.

* Wed Apr 14 1999 Michael Fulbright <drmike@redhat.com>
- removed Odo (has issues)

* Fri Apr 9 1999 The Rasterman <raster@redhat.com>
- patched metal theme - fixed handlebox redraw.

* Wed Mar 31 1999 Michael Fulbright <drmike@redhat.com>
- removed some themes that were misbehaving

* Tue Mar 16 1999 Michael Fulbright <drmike@redhat.com>
- removed enlightened themes, seems to be defective

* Thu Mar 11 1999 Michael Fulbright <drmike@redhat.com>
- removed Default theme data, this comes with gtk+ package

* Wed Mar 10 1999 Michael Fulbright <drmike@redhat.com>
- added extra gtk themes

* Thu Mar 04 1999 Michael Fulbright <drmike@redhat.com>
- version 0.5

* Fri Feb 12 1999 Michael Fulbright <drmike@redhat.com>
- version 0.4

* Wed Feb 03 1999 Michael Fulbright <drmike@redhat.com>
- version 0.3

* Mon Dec 18 1998 Michael Fulbright <drmike@redhat.com>
- version 0.2

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- rebuild because gtk+ version changed

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- in preparation for GNOME freeze

* Fri Nov 20 1998 Michael Fulbright <drmike@redhat.com>
- First try at a spec file
