Name: lesspipe
Version: 2.06
Release: 2
Source0: https://github.com/wofr06/lesspipe/archive/refs/tags/v%{version}.tar.gz
Summary: Input filter making the "less" file viewer far more powerful
URL: https://github.com/wofr06/lesspipe
License: GPLv2
Group: File tools
BuildArch: noarch
Requires: less
Supplements: less
Requires: file
Suggests: html2text
Suggests: odt2txt

%description
Input filter making the "less" file viewer far more powerful.

It is able to process a wide variety of file formats. It
enables users to deeply inspect archives and to display the contents
of files in archives without having to unpack them before.

That means file contents can be properly interpreted even if the
files are compressed and contained in a hierarchy of archives
(often found in RPM or DEB archives containing source tarballs).

The filter is easily extensible for new formats.

%prep
%autosetup -p1
./configure --yes

%build
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}

# Use it by default...
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
echo 'export LESSOPEN="|%{_bindir}/lesspipe.sh %s"' >%{buildroot}%{_sysconfdir}/profile.d/21lesspipe.sh
echo 'setenv LESSOPEN "|%{_bindir}/lesspipe.sh %s"' >%{buildroot}%{_sysconfdir}/profile.d/21lesspipe.csh

%files
%{_bindir}/archive_color
%{_bindir}/code2color
%{_bindir}/lesscomplete
%{_bindir}/sxw2txt
%{_bindir}/vimcolor
%{_bindir}/lesspipe.sh
%{_sysconfdir}/profile.d/21lesspipe.*
%{_sysconfdir}/bashcompletion.d/less_completion
%{_datadir}/zsh/site-functions/_less
%doc %{_mandir}/man1/lesspipe.1*
