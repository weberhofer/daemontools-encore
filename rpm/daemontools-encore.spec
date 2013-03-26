#
# spec file for package daemontools-encore
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2008-2009 Exata T.I., Maringa, PR, Brasil,
#               2008-2009, Weberhofer GmbH, Austria.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           daemontools-encore
Version:        1.05
Release:        0
Summary:        Tools for managing UNIX services
License:        BSD-3-Clause
Group:          System/Base
Url:            http://untroubled.org/daemontools-encore/
Source:         %{name}-%{version}.tar.bz2
Provides:       daemontools = %{version}
Provides:       daemontools-toaster = %{version}
Provides:       daemontools-toaster-doc = %{version}
Obsoletes:      daemontools < %{version}
Obsoletes:      daemontools-toaster < %{version}
Obsoletes:      daemontools-toaster-doc < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
daemontools-encore is a collection of tools for managing UNIX services.
It is derived from the public-domain release of daemontools by D. J.
Bernstein

%prep
%setup -q -n %{name}-%{version}

%build
echo 'cc %{optflags}' > conf-cc
echo 'cc -s %{optflags}' > conf-ld
echo '%{buildroot}/%{_bindir}' > conf-bin
echo '%{buildroot}/%{_mandir}' > conf-man
echo "%{buildroot}/%{_prefix}" > home

#chmod 0755 makemake
#./makemake

%{__make}

%install
%{__mkdir_p} %{buildroot}/%{_bindir}
%{__mkdir_p} %{buildroot}/%{_mandir}/man8
make install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0755,root,root)
%{_bindir}/*

%defattr(0644,root,root,0755)
%doc CHANGES CHANGES.djb LICENSE README TODO
%{_mandir}/man8/*

%changelog
