Name     : jdk-plexus-components
Version  : 1.3.1
Release  : 3
URL      : http://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-components/1.3.1/plexus-components-1.3.1.pom
Source0  : http://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-components/1.3.1/plexus-components-1.3.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : apache-maven
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-wagon
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn
BuildRequires : jdk-plexus
BuildRequires : jdk-forge-parent
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-junit4
BuildRequires : jdk-hamcrest
BuildRequires : jdk-xbean
BuildRequires : jdk-jdom
BuildRequires : jdk-qdox
BuildRequires : apache-maven2
BuildRequires : jdk-plexus-cli
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-doxia
BuildRequires : jdk-log4j
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-io
BuildRequires : jdk-commons-compress
BuildRequires : jdk-snappy-java
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-xmlunit
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-velocity
BuildRequires : jdk-commons-collections

%description
No detailed description available

%prep
cp -p %{SOURCE0} pom.xml

%build
python3 /usr/share/java-utils/mvn_build.py

%install
xmvn-install  -R .xmvn-reactor -n plexus-components-pom -d %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/maven-metadata/plexus-components-pom.xml
/usr/share/maven-poms/plexus-components-pom/plexus-components.pom
