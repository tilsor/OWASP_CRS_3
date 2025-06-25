Summary: ModSecurity Rules
Name: mod_security_crs
Version: 3.3.7
Release: 1%{?dist}
License: ASL 2.0
URL: https://coreruleset.org
Group: System Environment/Daemons
Source: https://github.com/coreruleset/coreruleset/archive/refs/tags/v%{version}.tar.gz
BuildArch: noarch
Requires: mod_security >= 2.9.6
Obsoletes: mod_security_crs-extras < 3.0.0

%description
This package provides the base rules for mod_security.

%prep
%setup -q -n coreruleset-%{version}

%build

%install

install -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/
install -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules
install -d %{buildroot}%{_datarootdir}/mod_modsecurity_crs/rules

# To exclude rules (pre/post)
mv rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf.example %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf
mv rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf.example %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf

install -m0644 rules/* %{buildroot}%{_datarootdir}/mod_modsecurity_crs/rules/
mv crs-setup.conf.example %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/crs-setup.conf

# activate base_rules
for f in `ls %{buildroot}%{_datarootdir}/mod_modsecurity_crs/rules/` ; do
    ln -s %{_datarootdir}/mod_modsecurity_crs/rules/$f %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/$f;
done
crs_version=$(echo %{version} | tr -d '.')
sed -i "s/crs_setup_version=.*/crs_setup_version=%{crs_version}\"/g" %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/crs-setup.conf

%files
%license LICENSE
%doc SECURITY.md SPONSORS.md CHANGES.md README.md
%config(noreplace) %{_sysconfdir}/httpd/modsecurity.d/activated_rules/*
%config(noreplace) %{_sysconfdir}/httpd/modsecurity.d/crs-setup.conf
%{_datarootdir}/mod_modsecurity_crs


%changelog
* Wed Jun 25 2025 German Gonzalez <ggonzalez@tilsor.com.uy> - 3.3.7-1
- Automate version change when crs-setup.conf has custom updates

* Fri Nov 01 2024 German Gonzalez <ggonzalez@tilsor.com.uy> - 3.3.7
- Update to last release

* Wed Aug 28 2024 German Gonzalez <ggonzalez@tilsor.com.uy> - 3.3.6
- Update to last release

* Wed Nov 08 2023 German Gonzalez <ggonzalez@tilsor.com.uy> - 3.3.5
- Update to final release

* Mon Oct 03 2022 German Gonzalez <ggonzalez@tilsor.com.uy> - 3.3.4
- Update to final release

* Mon Sep 19 2022 German Gonzalez <ggonzalez@tilsor.com.uy> - 3.3.3
- Update to final release

* Mon Aug 30 2021 Rodrigo Martinez <rmartinez@tilsor.com.uy> - 3.3.2
- Update to last version for bug in Drupal rules in branch 3.3

* Tue Jul 13 2021 Rodrigo Martinez <rmartinez@tilsor.com.uy> - 3.1.2
- Update to last version for bug in Drupal rules

* Wed Nov 06 2019 Mario del Riego <mdelriego@tilsor.com.uy> - 3.2.0
- Update to final release

* Thu Dec 13 2018 <mdelriego@tilsor.com.uy> - 3.1.0
- Update to final release

* Tue Sep 11 2018 <fzipitria@tilsor.com.uy> - 3.1.0-RC1
- Update to release candidate

