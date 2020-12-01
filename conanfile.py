from conans import ConanFile


class ParticlePackage(ConanFile):
    name = 'OneWire'
    version = 'c5007f4'
    url = 'https://github.com/hicktech/conan-OneWire'
    repo_url = 'https://github.com/particle-iot/OneWireLibrary.git'
    generators = 'cmake'
    settings = []
    requires = []

    def package(self):
        self.copy('*.c*', dst='src', src='src')
        self.copy('*.h*', dst='include', src='src')

    def source(self):
        self.run(f'git clone {self.repo_url} .')
        self.run(f'git checkout {self.version}')

    def package_info(self):
        self.cpp_info.srcdirs = ['src']
