%global global_desc\
which.py is a small which replacement. It has the following features:\
\
 * it is portable (Windows, Linux, Mac OS X, Un*x);\
 * it understands PATHEXT and "App Paths" registration on Windows (i.e. it\
   will find everything that `start` does from the command shell);\
 * it can print all matches on the PATH;\
 * it can note "near misses" on the PATH (e.g. files that match but may not,\
   may not, say, have execute permissions); and\
 * it can be used as a Python module.\

Name:           python-which
Version:        1.1.0
Release:        23
Summary:        A small GNU-which replacement

License:        MIT
URL:            https://code.google.com/archive/p/which/ 
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/which/which-1.1.0.zip

BuildArch:      noarch
BuildRequires:  python2-devel

%description
%{global_desc}

%package -n python2-which
Summary: %{summary}
%{?python_provide:%python_provide python2-which}

%description -n python2-which
%{global_desc}

%package_help


%prep
%autosetup -p1 -n which-%{version}


%build
%py2_build


%install
%py2_install
cat << \EOF > which-python
#!/bin/sh
python -m which $@
EOF
install -d %{buildroot}%{_bindir}
install -m 0755 -p which-python %{buildroot}%{_bindir}


%files -n python2-which
%license LICENSE.txt
%{_bindir}/which-python
%{python2_sitelib}/which*

%files help
%doc README.txt TODO.txt

%changelog
* Tue Dec 3 2019 mengxian <mengxian@huawei.com> - 1.1.0-23
- Package init
