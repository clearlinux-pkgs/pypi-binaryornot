#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-binaryornot
Version  : 0.4.4
Release  : 12
URL      : https://files.pythonhosted.org/packages/a7/fe/7ebfec74d49f97fc55cd38240c7a7d08134002b1e14be8c3897c0dd5e49b/binaryornot-0.4.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/a7/fe/7ebfec74d49f97fc55cd38240c7a7d08134002b1e14be8c3897c0dd5e49b/binaryornot-0.4.4.tar.gz
Summary  : Ultra-lightweight pure Python package to check if a file is binary or text.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-binaryornot-license = %{version}-%{release}
Requires: pypi-binaryornot-python = %{version}-%{release}
Requires: pypi-binaryornot-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(chardet)

%description
BinaryOrNot
        =============================

%package license
Summary: license components for the pypi-binaryornot package.
Group: Default

%description license
license components for the pypi-binaryornot package.


%package python
Summary: python components for the pypi-binaryornot package.
Group: Default
Requires: pypi-binaryornot-python3 = %{version}-%{release}

%description python
python components for the pypi-binaryornot package.


%package python3
Summary: python3 components for the pypi-binaryornot package.
Group: Default
Requires: python3-core
Provides: pypi(binaryornot)
Requires: pypi(chardet)

%description python3
python3 components for the pypi-binaryornot package.


%prep
%setup -q -n binaryornot-0.4.4
cd %{_builddir}/binaryornot-0.4.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641507366
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-binaryornot
cp %{_builddir}/binaryornot-0.4.4/LICENSE %{buildroot}/usr/share/package-licenses/pypi-binaryornot/3a9052b4cf583cf56f81ceec5e688aa475b97032
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-binaryornot/3a9052b4cf583cf56f81ceec5e688aa475b97032

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
