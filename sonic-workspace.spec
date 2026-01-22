%define devname %mklibname -d %{name}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.5
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

# filter qml/plugins provides
%global __provides_exclude_from ^(/usr/lib(64)?/qt6/(qml|plugins)/.*\.so)$
%global __provides_exclude_from ^/usr/share/locale/.*\.mo$
# Prevent auto-generated znver1 HEIF dependencies
%global __requires_exclude ^lib(heif|de265).*

%define libname %mklibname kworkspace6

Name: sonic-workspace
Version: 6.5.5
Release: %{?git:0.%{git}.}1
URL: https://github.com/Sonic-DE/sonic-workspace
License: GPL
Group: System/Libraries

# Use Sonic-DE GitHub branch archive as source (requested)
Source0: https://github.com/Sonic-DE/sonic-workspace/archive/refs/heads/%{gitbranch}.tar.gz#/sonic-workspace-%{version}.tar.gz
Summary: Various components needed to run a Plasma-based environment. Including fixes and improvements for X11 sessions.
Obsoletes: simplesystray < %{EVRD}
BuildRequires: cmake(Breeze)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(PlasmaActivitiesStats)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6TextEditor)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6FileMetaData)
BuildRequires: cmake(Wayland) >= 5.90.0
BuildRequires: cmake(KWayland) >= 5.90.0
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: pkgconfig(libnm) >= 1.4.0
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6People)
BuildRequires: cmake(KF6KDED)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(Plasma) >= 5.90.0
BuildRequires: cmake(PlasmaQuick) >= 5.90.0
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Prison)
BuildRequires: cmake(Phonon4Qt6)
BuildRequires: cmake(KF6Runner)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Su)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6IdleTime)
BuildRequires: cmake(KF6Screen)
BuildRequires: cmake(KF6Baloo)
BuildRequires: cmake(KF6Prison)
BuildRequires: cmake(KScreenLocker)
BuildRequires: cmake(KF6Holidays)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6QuickCharts)
BuildRequires: cmake(KF6UnitConversion)
BuildRequires: cmake(Plasma5Support)
BuildRequires: cmake(KExiv2Qt6)
BuildRequires: cmake(KF6Svg)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KNightTime)
BuildRequires: cmake(VulkanHeaders)
BuildRequires: %mklibname -d KF6IconWidgets
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6UserFeedback)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: cmake(Qt6WaylandCompositor)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(LayerShellQt)
BuildRequires: cmake(WaylandProtocols)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(dbusmenu-qt6)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libqalculate)
BuildRequires: pkgconfig(libgps) >= 3.15
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(xft)
BuildRequires: pkgconfig(systemd)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Location)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6ShaderTools)
BuildRequires: cmake(QCoro6)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols) >= 1.24
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libqalculate)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pam-devel
BuildRequires: pkgconfig(iso-codes)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(PolkitQt6-1)
BuildRequires: cmake(AppStreamQt) >= 1.0.3
BuildRequires: cmake(packagekitqt6)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(libudev)
BuildRequires: spirv-tools
BuildRequires: gettext
# for DBus interfaces
# Both Plasma 5 and Plasma 6 provide
# cmake(KPipeWire), cmake(KSysGuard) and friends
BuildRequires: cmake(KPipeWire) >= 5.27.80
BuildRequires: kwin-devel
BuildRequires: cmake(KWinDBusInterface) >= 5.27.80
BuildRequires: cmake(KSysGuard) >= 5.27.80
BuildRequires: xdotool
# needed for backgrounds and patch 2
Requires: distro-release-theme
Requires: qt6-qttools-dbus
Requires: plasma6-kactivitymanagerd
Requires: kf6-qqc2-desktop-style
Requires: qt6-qtimageformats
# For dbus-send, used by plasma-ksplash-ready.service
Requires: dbus-tools
Requires: qml-org.kde.breeze.components = %{EVRD}
Requires: qml-org.kde.plasma.private.sessions = %{EVRD}
Requires: qml-org.kde.plasma.workspace = %{EVRD}
Requires: qml-org.kde.plasma.private.clipboard = %{EVRD}
# for nightlight
Requires: qml(QtPositioning)
Requires: accountsservice
Recommends: kf6-kimageformats
Provides: virtual-notification-daemon
Requires: iso-codes

# No backend subpackages in Sonic-Workspace

# Because of pam file
Conflicts: kdm < 2:4.11.22-1.1
Conflicts: kio-extras < 15.08.0
Obsoletes: %{mklibname plasma-geolocation-interface} = 5.240.0
Obsoletes: %{mklibname colorcorrect} = 5.240.0
Obsoletes: %{mklibname weather_ion} = 5.240.0
Obsoletes: %{mklibname taskmanager} = 5.240.0
Obsoletes: %{mklibname notificationmanager} = 5.240.0
# Image/codec stack required by KImageFormats, Baloo, and Plasma
Requires: lib64openexrcore
Requires: lib64openjph

# Renamed 2025-05-02 after 6.0
%rename plasma6-workspace
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption: -DINSTALL_SDDM_WAYLAND_SESSION:BOOL=ON
BuildOption: -DPLASMA_SYSTEMD_BOOT:BOOL=ON

# Disable all autotests (prevents Qt6Test, bitaptest, znver1 LTO freeze)
BuildOption: -DBUILD_TESTING:BOOL=OFF
BuildOption: -DKDE_SKIP_TEST_SETTINGS:BOOL=ON
BuildOption: -DKDE_SKIP_TESTS:BOOL=ON

%description
The Sonic Desktop workspace.

# Split out because it's used by both plasma-workspace
# and sddm-theme-breeze
%package -n %{libname}
Summary: The Plasma 6 workspace library
Group: System/Libraries

%description -n %{libname}
The Plasma 6 workspace library

%package -n %{devname}
Summary: Development files for the KDE Plasma workspace
Group: Development/KDE and Qt
Requires: %{name} = %{EVRD}
Requires: %{libname} = %{EVRD}
# Renamed 2025-05-02 after 6.0
%rename sonic-workspace-devel

%description -n %{devname}
Development files for the KDE Plasma workspace.

%package x11
Summary: X11 support for Sonic Desktop Workspace
Group: Graphical desktop/KDE
Provides: %{name}-backend = %{EVRD}
# needed if anything will fail on startkde
Requires: xmessage
Requires: xprop
Requires: xset
Requires: xrdb
Requires: iso-codes
Requires: sonic-win
Requires: kf6-kidletime-x11
Requires: libkscreen-x11
# Renamed 2025-05-02 after 6.0
%rename sonic-workspace
%package -n lib64klipper6
Summary: Klipper library from Sonic Workspace
Group: System/Libraries

%description -n lib64klipper6
The Klipper shared library used by Sonic Workspace and related components.
%files -n lib64klipper6
%{_libdir}/libklipper.so.6*

%description x11
X11 support for Plasma Workspace.

%package -n qml-org.kde.breeze.components
Summary: The org.kde.breeze.components QML component
Group: Graphical desktop/KDE
Requires: plasma6-qqc2-breeze-style

%description -n qml-org.kde.breeze.components
The org.kde.breeze.components QML component contains QML
components used by Plasma Workspace and the SDDM Breeze theme

%package -n qml-org.kde.plasma.private.clipboard
Summary: The org.kde.plasma.private.clipboard QML component
Group: Graphical desktop/KDE
Requires: %{libname} = %{EVRD}

%description -n qml-org.kde.plasma.private.clipboard
The org.kde.plasma.private.clipboard QML component contains QML
components used by Plasma Workspace and the SDDM Breeze theme

%package -n qml-org.kde.plasma.private.sessions
Summary: The org.kde.plasma.private.sessions QML component
Group: Graphical desktop/KDE
Requires: %{libname} = %{EVRD}

%description -n qml-org.kde.plasma.private.sessions
The org.kde.plasma.private.sessions QML component contains QML
components used by Plasma Workspace and the SDDM Breeze theme

%package -n qml-org.kde.plasma.workspace
Summary: The org.kde.plasma.workspace QML component
Group: Graphical desktop/KDE
Requires: %{libname} = %{EVRD}

%description -n qml-org.kde.plasma.workspace
The org.kde.plasma.workspace QML component contains QML
components used by Plasma Workspace and the SDDM Breeze theme

%install -a

# (tpg) fix autostart permissions
chmod 644 %{buildroot}%{_sysconfdir}/xdg/autostart/*

# Bogus install of a test
rm -rf %{buildroot}%{_builddir}

%files -f %{name}.lang
%{_bindir}/plasma-apply-colorscheme
%{_bindir}/plasma-apply-cursortheme
%{_bindir}/plasma-apply-desktoptheme
%{_bindir}/plasma-apply-lookandfeel
%{_bindir}/plasma-apply-wallpaperimage
%{_bindir}/plasma-shutdown
%{_sysconfdir}/xdg/autostart/gmenudbusmenuproxy.desktop
%{_sysconfdir}/xdg/autostart/org.kde.plasmashell.desktop
%{_sysconfdir}/xdg/autostart/org.kde.plasma-fallback-session-restore.desktop
%{_sysconfdir}/xdg/autostart/xembedsniproxy.desktop
%{_sysconfdir}/xdg/taskmanagerrulesrc
%{_sysconfdir}/xdg/menus/plasma-applications.menu
%{_bindir}/gmenudbusmenuproxy
%{_bindir}/kcminit
%{_bindir}/kcminit_startup
%{_bindir}/krunner
%{_bindir}/ksmserver
%{_bindir}/ksplashqml
%{_bindir}/plasmashell
%{_bindir}/plasma_waitforname
%{_bindir}/plasmawindowed
%{_bindir}/plasma_session
%{_bindir}/xembedsniproxy
%{_bindir}/kde-systemd-start-condition
%{_libdir}/libkfontinst.so.*
%{_libdir}/libkfontinstui.so.*
%{_libdir}/libexec/baloorunner
%{_libdir}/libexec/ksmserver-logout-greeter
%dir %{_qtdir}/plugins/plasma
%dir %{_qtdir}/plugins/plasma/applets
%dir %{_qtdir}/plugins/kf6/krunner
%{_qtdir}/plugins/kf6/kded/*.so
%{_qtdir}/plugins/kf6/kio/*.so
%{_qtdir}/plugins/kf6/krunner/*.so
%{_qtdir}/plugins/plasma/containmentactions
%{_qtdir}/plugins/phonon_platform
%{_qtdir}/plugins/plasma/applets/*.so
%{_qtdir}/plugins/plasmacalendarplugins
%{_qtdir}/qml/org/kde/plasma/workspace/calendar
%{_qtdir}/qml/org/kde/plasma/workspace/dialogs
%{_qtdir}/qml/org/kde/plasma/workspace/trianglemousefilter
%dir %{_qtdir}/qml/org/kde/plasma/private
%{_qtdir}/qml/org/kde/plasma/private/digitalclock
%{_qtdir}/qml/org/kde/plasma/private/shell
%{_qtdir}/qml/org/kde/plasma/wallpapers
%{_qtdir}/qml/org/kde/plasma/private/appmenu
%{_qtdir}/qml/org/kde/plasma/private/holidayevents
%{_qtdir}/qml/org/kde/plasma/private/systemtray
%{_qtdir}/qml/org/kde/plasma/workspace/dbus
%{_datadir}/applications/org.kde.plasmashell.desktop
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/dbus-1/services/*.service
%{_datadir}/desktop-directories
%{_datadir}/kio_desktop/*.desktop
%{_datadir}/kio_desktop/*.trash
%{_datadir}/knotifications6/*.notifyrc
%{_datadir}/kstyle
%{_datadir}/plasma/look-and-feel
%{_datadir}/applications/org.kde.klipper.desktop
%{_datadir}/solid/actions/openWithFileManager.desktop
%{_datadir}/xdg-desktop-portal/kde-portals.conf
%dir %{_datadir}/plasma/plasmoids
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar
%{_datadir}/plasma/plasmoids/org.kde.plasma.cameraindicator
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard
%{_datadir}/plasma/plasmoids/org.kde.plasma.icon
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpucore
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu
%dir %{_datadir}/plasma/wallpapers
%{_datadir}/plasma/wallpapers/org.kde.color
%{_datadir}/plasma/wallpapers/org.kde.image
%{_datadir}/plasma/wallpapers/org.kde.slideshow
%{_qtdir}/qml/org/kde/taskmanager
%{_datadir}/qlogging-categories6/*.categories
%{_sysconfdir}/xdg/plasmanotifyrc
%{_qtdir}/qml/org/kde/notificationmanager
%{_qtdir}/qml/org/kde/plasma/private/containmentlayoutmanager
%{_qtdir}/qml/org/kde/plasma/private/kicker
%{_libdir}/libexec/plasma-sourceenv.sh
%{_bindir}/kcolorschemeeditor
%{_bindir}/kfontinst
%{_datadir}/kio/servicemenus/installfont.desktop
%{_bindir}/kfontview
%{_bindir}/lookandfeeltool
%{_libdir}/libexec/kf6/kauth/fontinst*
%{_datadir}/polkit-1/actions/org.kde.fontinst.policy
%{_libdir}/libexec/kfontprint
%{_libdir}/libexec/plasma-changeicons
%{_libdir}/libexec/plasma-dbus-run-session-if-needed
%{_userunitdir}/*.service
%{_userunitdir}/*.target
%{_datadir}/applications/org.kde.kcolorschemeeditor.desktop
%{_datadir}/applications/org.kde.kfontview.desktop
%{_datadir}/dbus-1/system-services/org.kde.fontinst.service
%{_datadir}/dbus-1/system.d/org.kde.fontinst.conf
%{_datadir}/icons/hicolor/*/mimetypes/fonts-package.*
%{_datadir}/icons/hicolor/*/apps/kfontview.*
%{_datadir}/icons/hicolor/scalable/apps/preferences-desktop-font-installer.svgz
%{_datadir}/kfontinst/icons/hicolor/*/actions/*.png
%{_datadir}/knsrcfiles/*.knsrc
%{_datadir}/konqsidebartng/virtual_folders/services/fonts.desktop
%{_datadir}/krunner/dbusplugins/plasma-runner-baloosearch.desktop
%{_datadir}/kglobalaccel/org.kde.krunner.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.manage-inputmethod
%{_qtdir}/plugins/kf6/parts/kfontviewpart.so
%{_datadir}/kxmlgui5/kfontviewpart/kfontviewpart.rc
%{_bindir}/plasma-interactiveconsole
%{_qtdir}/plugins/kf6/krunner/kcms/kcm_krunner_kill.so
%{_qtdir}/plugins/plasma/kcminit/kcm_fonts_init.so
%{_qtdir}/plugins/plasma/kcminit/kcm_style_init.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_autostart.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_colors.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_cursortheme.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_desktoptheme.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_feedback.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_fonts.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_icons.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_lookandfeel.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_notifications.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_regionandlang.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_soundtheme.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_style.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_users.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_fontinst.so
%{_qtdir}/qml/org/kde/plasma/lookandfeel
%{_datadir}/applications/kcm_autostart.desktop
%{_datadir}/applications/kcm_colors.desktop
%{_datadir}/applications/kcm_cursortheme.desktop
%{_datadir}/applications/kcm_desktoptheme.desktop
%{_datadir}/applications/kcm_feedback.desktop
%{_datadir}/applications/kcm_fontinst.desktop
%{_datadir}/applications/kcm_fonts.desktop
%{_datadir}/applications/kcm_icons.desktop
%{_datadir}/applications/kcm_lookandfeel.desktop
%{_datadir}/applications/kcm_notifications.desktop
%{_datadir}/applications/kcm_soundtheme.desktop 
%{_datadir}/applications/kcm_style.desktop
%{_datadir}/applications/kcm_users.desktop
%{_datadir}/applications/org.kde.plasmawindowed.desktop
%{_datadir}/plasma/avatars
%{_datadir}/kxmlgui5/kfontview
%{_bindir}/plasma-localegen-helper
%{_datadir}/applications/kcm_regionandlang.desktop
%{_datadir}/dbus-1/system-services/org.kde.localegenhelper.service
%{_datadir}/dbus-1/system.d/org.kde.localegenhelper.conf
%{_datadir}/polkit-1/actions/org.kde.localegenhelper.policy
%{_qtdir}/plugins/kf6/thumbcreator/fontthumbnail.so
%{_datadir}/zsh/site-functions/_plasmashell
%{_qtdir}/plugins/plasma5support/dataengine
%{_qtdir}/plugins/kf6/kfileitemaction/wallpaperfileitemaction.so
%{_qtdir}/plugins/kf6/packagestructure/plasma_*.so
%{_qtdir}/plugins/kf6/packagestructure/wallpaper_images.so
%{_datadir}/plasma5support/services/*.operations
%{_libdir}/libkmpris.so*
%{_libdir}/qt6/qml/org/kde/plasma/private/mpris
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_wallpaper.so
%{_datadir}/applications/kcm_wallpaper.desktop
%{_libdir}/kconf_update_bin/plasma6.0-remove-dpi-settings
%{_libdir}/kconf_update_bin/plasma6.0-remove-old-shortcuts
%{_libdir}/kconf_update_bin/plasmashell-6.0-keep-default-floating-setting-for-plasma-5-panels
%{_libdir}/kconf_update_bin/plasmashell-6.0-keep-custom-position-of-panels
%{_libdir}/kconf_update_bin/plasma6.3-update-clipboard-database-2-to-3
%{_datadir}/kconf_update/plasmashell-6.0-keep-custom-position-of-panels.upd
%{_datadir}/kconf_update/plasma6.0-remove-dpi-settings.upd
%{_datadir}/kconf_update/plasma6.0-remove-old-shortcuts.upd
%{_datadir}/kconf_update/plasmashell-6.0-keep-default-floating-setting-for-plasma-5-panels.upd
%{_datadir}/zsh/site-functions/_krunner
%{_datadir}/kconf_update/migrate-calendar-to-plugin-id.py
%{_datadir}/kconf_update/migrate-calendar-to-plugin-id.upd
%{_datadir}/kconf_update/plasma6.3-update-clipboard-database-2-to-3.upd
%{_libdir}/libexec/plasma-fallback-session-restore
%{_libdir}/libexec/plasma-fallback-session-save
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_nightlight.so
%{_datadir}/applications/kcm_nightlight.desktop
%{_datadir}/applications/org.kde.kfontinst.desktop
%{_datadir}/applications/org.kde.plasma-fallback-session-save.desktop
# Please do NOT split those into separate libpackages. They're used only
# internally.
%{_libdir}/libtaskmanager.so*
%{_libdir}/libnotificationmanager.so*
%{_libdir}/kconf_update_bin/plasma6.4-migrate-fullscreen-notifications-to-dnd
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_componentchooser.so
%{_datadir}/applications/kcm_componentchooser.desktop
%{_datadir}/kconf_update/plasma6.4-migrate-fullscreen-notifications-to-dnd.upd
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray
%{_datadir}/timezonefiles/timezones.json
%{_libdir}/kconf_update_bin/plasmashell-6.5-remove-stop-activity-shortcut
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_nighttime.so
%{_datadir}/applications/kcm_nighttime.desktop
%{_datadir}/applications/org.kde.plasma-interactiveconsole.desktop
%{_datadir}/kconf_update/plasmashell-6.5-remove-stop-activity-shortcut.upd

%files -n %{libname}
%{_libdir}/libklookandfeel.so.*
%{_libdir}/libkworkspace6.so*
%{_libdir}/libbatterycontrol.so*
%{_libdir}/libkrdb.so

%files -n qml-org.kde.plasma.workspace
%dir %{_qtdir}/qml/org/kde/plasma/workspace
%{_qtdir}/qml/org/kde/plasma/workspace/components
%{_qtdir}/qml/org/kde/plasma/workspace/keyboardlayout
%{_qtdir}/qml/org/kde/plasma/workspace/osd
%{_qtdir}/qml/org/kde/plasma/workspace/timezoneselector
%{_qtdir}/qml/org/kde/plasma/private/battery
%{_qtdir}/qml/org/kde/plasma/private/keyboardindicator

%files -n qml-org.kde.breeze.components
%{_qtdir}/qml/org/kde/breeze/components

%files -n qml-org.kde.plasma.private.clipboard
%{_qtdir}/qml/org/kde/plasma/private/clipboard

%files -n qml-org.kde.plasma.private.sessions
%{_qtdir}/qml/org/kde/plasma/private/sessions

%files x11
%{_bindir}/startplasma-x11
%{_datadir}/xsessions/plasmax11.desktop

%package wayland
Summary: Wayland session support for Sonic Desktop Workspace
Group: Graphical desktop/KDE
Requires: %{name} = %{EVRD}

%description wayland
Wayland session support for the Sonic Desktop Workspace.

%files wayland
# Plasma Wayland session
/usr/bin/startplasma-wayland
/usr/share/wayland-sessions/plasma.desktop
%config(noreplace) /etc/sddm.conf.d/plasma-wayland.conf

%files -n %{devname}
%{_includedir}/*
%{_libdir}/lib*.so
%exclude %{_libdir}/libkrdb.so
%{_libdir}/cmake/KRunnerAppDBusInterface
%{_libdir}/cmake/KSMServerDBusInterface
%{_libdir}/cmake/LibKWorkspace
%{_libdir}/cmake/LibTaskManager
%{_libdir}/cmake/Krdb
%{_libdir}/cmake/LibKLookAndFeel
%{_datadir}/dbus-1/interfaces/*.xml
%{_libdir}/cmake/LibNotificationManager
