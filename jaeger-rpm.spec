%global _prefix /usr/local

Name:    jaeger
Version: 1.11.0
Release: 1
Summary: CNCF Jaeger, a Distributed Tracing System

Group:   Development Tools
License: ASL 2.0
URL: https://github.com/jaegertracing/jaeger/releases/download/v%{version}/jaeger-%{version}-linux-amd64.tar.gz

%description
Jaeger, inspired by Dapper and OpenZipkin, is a distributed tracing system released as open source by Uber Technologies.

%prep
curl -L %{url} > jaeger-linux-amd64.tar.gz
tar -zxf jaeger-linux-amd64.tar.gz

%package agent
Summary: jaeger agent

%package all-in-one
Summary: jaeger all in one

%package collector
Summary: jaeger collector

%package ingester
Summary: jaeger ingester

%package query
Summary: jaeger query

%install
# agent
install jaeger-agent %{buildroot}/%{_bindir}

# all-in-one
install jaeger-all-in-one %{buildroot}/%{_bindir}

# collector
install jaeger-collector %{buildroot}/%{_bindir}

# ingester
install jaeger-ingester %{buildroot}/%{_bindir}

# query
install jaeger-query %{buildroot}/%{_bindir}


%files agent
%attr(755, root, root) %{_bindir}/agent

%files all-in-one
%attr(755, root, root) %{_bindir}/all-in-one

%files collector
%attr(755, root, root) %{_bindir}/collector

%files ingester
%attr(755, root, root) %{_bindir}/ingester

%files query
%attr(755, root, root) %{_bindir}/query
