from conan import ConanFile
from conan.tools.cmake import CMakeDeps, CMakeToolchain

class PALRecipe(ConanFile):
    settings = "os", "build_type"

    def requirements(self):
        self.requires("assimp/5.4.2")
        self.requires("stb/cci.20230920")
        self.requires("sdl/2.30.7")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.user_presets_path = False
        tc.generate()
        cd = CMakeDeps(self)
        cd.generate()