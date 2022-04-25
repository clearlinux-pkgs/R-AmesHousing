#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-AmesHousing
Version  : 0.0.4
Release  : 38
URL      : https://cran.r-project.org/src/contrib/AmesHousing_0.0.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/AmesHousing_0.0.4.tar.gz
Summary  : The Ames Iowa Housing Data
Group    : Development/Tools
License  : GPL-2.0
Requires: R-dplyr
Requires: R-magrittr
BuildRequires : R-dplyr
BuildRequires : R-magrittr
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n AmesHousing
cd %{_builddir}/AmesHousing

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640969507

%install
export SOURCE_DATE_EPOCH=1640969507
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library AmesHousing
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library AmesHousing
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library AmesHousing
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc AmesHousing || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/AmesHousing/DESCRIPTION
/usr/lib64/R/library/AmesHousing/INDEX
/usr/lib64/R/library/AmesHousing/Meta/Rd.rds
/usr/lib64/R/library/AmesHousing/Meta/data.rds
/usr/lib64/R/library/AmesHousing/Meta/features.rds
/usr/lib64/R/library/AmesHousing/Meta/hsearch.rds
/usr/lib64/R/library/AmesHousing/Meta/links.rds
/usr/lib64/R/library/AmesHousing/Meta/nsInfo.rds
/usr/lib64/R/library/AmesHousing/Meta/package.rds
/usr/lib64/R/library/AmesHousing/NAMESPACE
/usr/lib64/R/library/AmesHousing/NEWS.md
/usr/lib64/R/library/AmesHousing/R/AmesHousing
/usr/lib64/R/library/AmesHousing/R/AmesHousing.rdb
/usr/lib64/R/library/AmesHousing/R/AmesHousing.rdx
/usr/lib64/R/library/AmesHousing/data/Rdata.rdb
/usr/lib64/R/library/AmesHousing/data/Rdata.rds
/usr/lib64/R/library/AmesHousing/data/Rdata.rdx
/usr/lib64/R/library/AmesHousing/data/datalist
/usr/lib64/R/library/AmesHousing/help/AmesHousing.rdb
/usr/lib64/R/library/AmesHousing/help/AmesHousing.rdx
/usr/lib64/R/library/AmesHousing/help/AnIndex
/usr/lib64/R/library/AmesHousing/help/aliases.rds
/usr/lib64/R/library/AmesHousing/help/paths.rds
/usr/lib64/R/library/AmesHousing/html/00Index.html
/usr/lib64/R/library/AmesHousing/html/R.css
