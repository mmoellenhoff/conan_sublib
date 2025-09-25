import os
from conan import ConanFile
from conan.tools.files import load, copy
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps

class helloRecipe(ConanFile):
    name = "sublibrary1"
    version = "1.0"
    package_type = "library"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of hello package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)
        #self.folders.root = ".."
        #self.folders.source = "."
        #self.folders.build = "build"
        #self.cpp.package.libs = ["sublibrary1"]
        #self.cpp.package.includedirs = ["include"]
        #self.cpp.package.libdirs = ["lib/sublibrary1"]

    def export_sources(self):
        folder = os.path.join(self.recipe_folder, "..")
        copy(self, "CMakeLists.txt", folder, self.export_sources_folder)
        copy(self, "sublibrary1/*", folder, self.export_sources_folder)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.variables["SUBLIBRARY1_RUN"] = True
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self, "include/sublib1/*.h", os.path.join(self.build_folder, "../sublibrary1"), self.package_folder)
        copy(self, "sublibrary1/*.a", self.build_folder, os.path.join(self.package_folder, "lib"))

    def package_info(self):
        self.cpp_info.libs = ["sublibrary1"]
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libdirs = ["lib/sublibrary1"]
        self.cpp_info.set_property("cmake_target_name", "sub::lib1")

