Name:           ros-indigo-cob-android
Version:        0.1.3
Release:        0%{?dist}
Summary:        ROS cob_android package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_android
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-cob-android-msgs
Requires:       ros-indigo-cob-android-resource-server
Requires:       ros-indigo-cob-android-script-server
Requires:       ros-indigo-cob-android-settings
BuildRequires:  ros-indigo-catkin

%description
cob_android package provides tools for android apps operation.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jul 18 2017 Benjamin Maidel <bnm@ipa.fhg.de> - 0.1.3-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Benjamin Maidel <bnm@ipa.fhg.de> - 0.1.2-0
- Autogenerated by Bloom

* Sat Aug 29 2015 Benjamin Maidel <bnm@ipa.fhg.de> - 0.1.1-0
- Autogenerated by Bloom

