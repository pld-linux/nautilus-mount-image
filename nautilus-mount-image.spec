Summary:	Mount and unmount the selected CD or DVD image from Nautilus
Summary(pl.UTF-8):	Zamontuj i odmontuj wskazany obraz CD albo DVD z Nautilusa
Name:		nautilus-mount-image
Version:	0.1.0
Release:	0.1
License:	GPL v2
Group:		X11/Libraries
Source0:	http://mundogeek.net/repo/pool/ubuntu/all/%{name}_%{version}-1.tar.gz
# Source0-md5:	e8c0508a53f3d665915109927b08ea89
URL:		http://mundogeek.net/nautilus-scripts/#nautilus-mount-image
Requires:	nautilus-python >= 0.4.3
Requires:   python-pygtk >= 2.12.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program adds a new entry to the contextual menu which allows us to
mount and unmount the selected CD or DVD image.

%description -l pl.UTF-8
Ten program dodaje nowy wpis do menu kontekstowego który pozwala nam
zmaontować i odmontować wskazany obraz CD i DVD.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/nautilus/extensions-1.0/python/*
