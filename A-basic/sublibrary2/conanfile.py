import os
from conan import ConanFile
from conan.tools.files import load, copy
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps

class helloRecipe(ConanFile):
    name = "sublibrary2"
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
        self.folders.root = ".."
        self.folders.source = "."
        self.folders.build = "build"
        self.cpp.package.libs = ["sublibrary2"]
        self.cpp.package.includedirs = ["include"]
        self.cpp.package.libdirs = ["lib/sublibrary2"]

    def export_sources(self):
        folder = os.path.join(self.recipe_folder, "..")
        copy(self, "CMakeLists.txt", folder, self.export_sources_folder)
        copy(self, "sublibrary2/*", folder, self.export_sources_folder)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.variables["SUBLIBRARY2_RUN"] = True
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self, "include/sublib2/*.h", os.path.join(self.build_folder, "../sublibrary2"), self.package_folder, keep_path=True)
        copy(self, "sublibrary2/*.a", self.build_folder, os.path.join(self.package_folder, "lib"), keep_path=True)

    def package_info(self):
        self.cpp_info.libs = ["sublibrary2"]
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libdirs = ["lib/sublibrary2"]
        self.cpp_info.set_property("cmake_target_name", "sub::lib2")

