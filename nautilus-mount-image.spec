Summary:	Mount and unmount the selected CD or DVD image from Nautilus
Summary(pl.UTF-8):	Zamontuj i odmontuj wskazany obraz CD albo DVD z Nautilusa
Name:		nautilus-mount-image
Version:	0.2.0
Release:	2
License:	GPL v2
Group:		X11/Libraries
Source0:	http://ppa.launchpad.net/zootropo/ubuntu/pool/main/n/nautilus-mount-image/%{name}_%{version}-1.tar.gz
# Source0-md5:	0f7abcdec72c34c235945421607ee078
Patch0:		%{name}-libdir.patch
URL:		http://mundogeek.net/nautilus-scripts/#nautilus-mount-image
Requires:	nautilus-python >= 0.4.3
Requires:	python-pygtk >= 2.12.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program adds a new entry to the contextual menu which allows us
to mount and unmount the selected CD or DVD image.

%description -l pl.UTF-8
Ten program dodaje nowy wpis do menu kontekstowego który pozwala nam
zmaontować i odmontować wskazany obraz CD i DVD.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	LIBDIR="%{_libdir}" \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc changelog
%{_libdir}/nautilus/extensions-2.0/python/%{name}.py
%{_pixmapsdir}/nautilus-mount-image.png
