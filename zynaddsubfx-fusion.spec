#
# This package provides ZynAddSubFX syntethizer with the new 'Zyn-Fusion' UI
# Source code for the UI is available in the https://github.com/mruby-zest/mruby-zest-build
# repository and contains many submodules and no unified source archive
#
# Use the provided 'get-fusion.sh' script to generate the Source1 archive

%define fusion_version 3.0.2_59_gc4c9221

%define mruby_pack_version 383a9c79e191d524a9a2b4107cc5043ecbf6190b
%define mruby_process_version bd288a930d4f61fbda1865deb8997245dc5fd38c
%define mruby_file_stat_version 12871584f2e5e2d24f5c54325d3ba3338414e2a4
%define mruby_errno_version b4415207ff6ea62360619c89a1cff83259dc4db0
%define mruby_dir_version 14bc5c3e51eac16ebc9075b7b62132a0cf5ae724

Summary:	Realtime software synthesizer
Summary(pl.UTF-8):	Syntezator programowy działający w czasie rzeczywistym
Name:		zynaddsubfx-fusion
Version:	3.0.3
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/zynaddsubfx/zynaddsubfx-%{version}.tar.bz2
# Source0-md5:	66acae0913108f129aa979f3c4b65473
Source1:	mruby-zest-build-%{fusion_version}.tar.xz
# Source1-md5:	fa7c3b4c46e6155df19cb00d9dc6db0f
Source2:	https://github.com/iij/mruby-pack/archive/%{mruby_pack_version}/mruby-pack-%{mruby_pack_version}.tar.gz
# Source2-md5:	b77f2dea16857e64624730ec94beb778
Source3:	https://github.com/iij/mruby-process/archive/%{mruby_process_version}/mruby-process-%{mruby_process_version}.tar.gz
# Source3-md5:	7c3881decb19930175b1f9520216d133
Source4:	https://github.com/ksss/mruby-file-stat/archive/%{mruby_file_stat_version}/mruby-file-stat-%{mruby_file_stat_version}.tar.gz
# Source4-md5:	8bad3f085f86cdc5d065c36b4ca3850d
Source5:	https://github.com/iij/mruby-errno/archive/%{mruby_errno_version}/mruby-errno-%{mruby_errno_version}.tar.gz
# Source5-md5:	2696ab2c434d1779e96fed50ed4a77c4
Source6:	https://github.com/iij/mruby-dir/archive/%{mruby_dir_version}/mruby-dir-%{mruby_dir_version}.tar.gz
# Source6-md5:	c0fd8162728821361e38ccec87677397
Patch0:		cxx_flags.patch
Patch1:		system_libuv.patch
Patch2:		external_mruby_gems.patch
URL:		http://zynaddsubfx.sourceforge.net/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	Mesa-libGLU-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	cairo-devel
BuildRequires:	cmake
#BuildRequires:	doxygen
BuildRequires:	dssi-devel >= 0.9.0
BuildRequires:	fftw3-devel
BuildRequires:	jack-audio-connection-kit-devel >= 0.66.3
BuildRequires:	lash-devel
BuildRequires:	liblo-devel >= 0.28
BuildRequires:	libuv-devel >= 1.9.1
BuildRequires:	mxml-devel >= 2.2
BuildRequires:	pkgconfig
BuildRequires:	portaudio >= 19
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	ruby
BuildRequires:	ruby-rake
BuildRequires:	sed >= 4.0
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
Obsoletes:	ZynAddSubFX
Obsoletes:	zynaddsubfx
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/(dssi|lv2|vst)

%description
ZynAddSubFX is a software synthesizer capable of making a countless
number of instruments.

Zyn-Fusion is the modern external GUI for the synthesizer.

%description -l pl.UTF-8
ZynAddSubFX jest programowym syntezatorem zdolnym do tworzenia
niezliczonej ilości instrumentów.

Zyn-Fusion do nowoczesny interfejs użytkownika dla tego syntezatora.

%package dssi
Summary:	Realtime software synthesizer - DSSI plugin
Summary(pl.UTF-8):	Syntezator programowy działający w czasie rzeczywistym, plugin DSSI
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ZynAddSubFX-dssi
Obsoletes:	zynaddsubfx-dssi

%description dssi
ZynAddSubFX software synthesizer as a DSSI plugin.

%description dssi -l pl.UTF-8
Syntezator ZynAddSubFX jako wtyczka DSSI.

%package lv2
Summary:	Realtime software synthesizer - LV2 plugin
Summary(pl.UTF-8):	Syntezator programowy działający w czasie rzeczywistym, plugin LV2
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ZynAddSubFX-lv2
Obsoletes:	zynaddsubfx-lv2

%description lv2
ZynAddSubFX software synthesizer as a LV2 plugin.

%description lv2 -l pl.UTF-8
Syntezator ZynAddSubFX jako wtyczka LV2.

%package vst
Summary:	Realtime software synthesizer - VST plugin
Summary(pl.UTF-8):	Syntezator programowy działający w czasie rzeczywistym, plugin VST
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ZynAddSubFX-vst
Obsoletes:	zynaddsubfx-vst

%description vst
ZynAddSubFX software synthesizer as a VST plugin.

%description vst -l pl.UTF-8
Syntezator ZynAddSubFX jako wtyczka VST.

%prep
%setup -qn zynaddsubfx-%{version} -a 1 -a 2 -a 3 -a 4 -a 5 -a 6

for module in pack process file-stat errno dir ; do
	mv mruby-${module}-* mruby-zest-build/deps/mruby-${module}
done

%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i -e's@/opt/zyn-fusion@%{_libdir}/zyn-fusion@g' \
	mruby-zest-build/test-libversion.c \
	src/Plugin/ZynAddSubFX/ZynAddSubFX-UI-Zest.cpp

%build

# See https://github.com/zynaddsubfx/zyn-fusion-build/blob/master/build-linux.rb
# for the build instructions

[ -d build ] || mkdir build
cd build
%cmake .. \
		-DGuiModule=zest \
	-DPluginLibDir=%{_lib} \
	-DCMAKE_CXX_FLAGS_RELEASE="%{rpmcxxflags}"

%{__make}
cd ..

cd mruby-zest-build
export LC_ALL=C.utf-8
ruby rebuild-fcache.rb
%{__make} setup
%{__make} builddep
export VERSION="%{version}"
export BUILD_MODE="release"
%{__make}
%{__make} pack

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_libdir}/zyn-fusion} \
	$RPM_BUILD_ROOT%{_desktopdir}

%{__make} -C build install \
	DESTDIR="$RPM_BUILD_ROOT"

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}

cp -a mruby-zest-build/package/* $RPM_BUILD_ROOT%{_libdir}/zyn-fusion
ln -s %{_libdir}/zyn-fusion/zest $RPM_BUILD_ROOT%{_bindir}/zyn-fusion
%{__rm} $RPM_BUILD_ROOT%{_libdir}/zyn-fusion/mruby

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt HISTORY.txt README.adoc
%attr(755,root,root) %{_bindir}/zynaddsubfx
%attr(755,root,root) %{_bindir}/zyn-fusion
%{_datadir}/zynaddsubfx
%{_pixmapsdir}/zynaddsubfx.svg
%{_desktopdir}/zynaddsubfx-*.desktop
%dir %{_libdir}/zyn-fusion
%attr(755,root,root) %{_libdir}/zyn-fusion/zest
%attr(755,root,root) %{_libdir}/zyn-fusion/libzest.so
%{_libdir}/zyn-fusion/VERSION
%{_libdir}/zyn-fusion/font
%{_libdir}/zyn-fusion/qml
%{_libdir}/zyn-fusion/schema

%files dssi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/dssi/libzynaddsubfx_dssi.so

%files lv2
%defattr(644,root,root,755)
%dir %{_libdir}/lv2/*.lv2
%dir %{_libdir}/lv2/ZynAddSubFX.lv2presets
%attr(755,root,root) %{_libdir}/lv2/*.lv2/*.so
%{_libdir}/lv2/*.lv2/*.ttl
%{_libdir}/lv2/ZynAddSubFX.lv2presets/*.ttl

%files vst
%defattr(644,root,root,755)
%dir %{_libdir}/vst
%attr(755,root,root) %{_libdir}/vst/*.so
