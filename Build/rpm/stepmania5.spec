Name:       stepmania5
Version:    0
Release:    12
Summary:    A dance and rhythm game
License:    GPL
BuildRequires: gcc-c++ cmake libmad-devel libvorbis-devel libbz2-devel libX11-devel libjpeg62-devel libXtst-devel libpulse-devel alsa-devel libva-devel glew-devel libXrandr-devel libXinerama-devel
Requires:      glibc libasound2 libbz2-1 libdbus-1-3 libFLAC8 libgcc_s1 libgcrypt20 libGLEW2_2 libGLU1 libglvnd libgpg-error0 libjpeg62 liblz4-1 liblzma5 libmad0 libogg0 libpulse0 libsndfile1 libspeex1 libstdc++6 libsystemd0 libva2 libvorbis0 libvorbisenc2 libvorbisfile3 libX11-6 libXau6 libxcb1 libXext6 libXinerama1 libXrandr2 libXrender1 libXtst6
%description
StepMania is a free dance and rhythm game. It features 3D graphics, keyboard and "dance pad" support, and an editor for creating your own steps.

%prep
#--------------------------------------------------------------------------------
#--- If repo exists locally on ~/git/stepmania it will be checkout from there ---
#--- Otherwise it will be checked-out from the official repository URL        ---
#--------------------------------------------------------------------------------
rm -rf %{_sourcedir}/*
git clone ~/git/stepmania %{_sourcedir} || git clone https://github.com/stepmania/stepmania.git %{_sourcedir}

%build
cd %{_builddir}
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{buildroot}/opt %{_sourcedir}
make -j5

%install
# --- Install binaries ---
cd %{_builddir}
make install
# --- Install start menu entry ---
install -D %{_sourcedir}/Build/rpm/stepmania5.desktop %{buildroot}/usr/share/applications/stepmania5.desktop

%files
/opt/stepmania-5.1
/usr/share/applications/stepmania5.desktop

%changelog
# let's skip this for now
