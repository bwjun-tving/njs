%define name nginx-mod-njs
%define version 0.7.12
%define release 1


Summary: njs scripting language module for nginx
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: Proprietary
Group: System Environment/Daemons
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64
Vendor: Byungwan Jun <bw.jun@cj.net>
Requires: nginx >= 1.22.1


%description
njs scripting language module for nginx


%prep
cd %{_builddir}
curl -o nginx-1.22.1.tar.gz  http://nginx.org/download/nginx-1.22.1.tar.gz
tar zxf nginx-1.22.1.tar.gz


%setup
cd %{_builddir}/nginx-1.22.1; ./configure --with-compat --add-dynamic-module=%{_builddir}/%{name}-%{version}/nginx


%build
cd %{_builddir}/nginx-1.22.1; make modules


%install
install -d %{buildroot}/usr/share/nginx/modules
install -m 644 %{_builddir}/nginx-1.22.1/objs/ngx_http_js_module.so %{buildroot}/usr/share/nginx/modules/ngx_http_js_module.so
install -m 644 amazon2/mod-njs.conf %{buildroot}/usr/share/nginx/modules/mod-njs.conf


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,0644)
/usr/share/nginx/modules/ngx_http_js_module.so
/usr/share/nginx/modules/mod-njs.conf


%changelog
* Tue Apr 11 2023 Byungwan Jun <bw.jun@cj.net> - 0.7.12-1
- Initial release
