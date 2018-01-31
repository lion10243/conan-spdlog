#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class spdlogConan(ConanFile):
    name = "spdlog"
    version = "0.16.3"
    license = "MIT"
    exports = ["LICENSE.md"]    
    description = "Very fast, header only, C++ logging library."
    url = "https://github.com/lion10243/conan-spdlog"
    options = {"fmt_external": [True, False]}
    default_options = "fmt_external=False"

    def requirements(self):
        if self.options.fmt_external:
            self.requires("fmt/[>=4.0.0]@bincrafters/stable")

    def source(self):
        base_url = "https://github.com/gabime/spdlog"
        archive_prefix = "/archive/v"
        archive_ext = ".tar.gz"
        tools.get(base_url + archive_prefix + self.version + archive_ext)

    def package(self):
        self.copy("*.h", dst="include", src="spdlog-%s/include" % (self.version))
        self.copy("*ostream.cc", dst="include", src="spdlog-%s/include" % (self.version))
        if not self.options.fmt_external:
            self.copy("*format.cc", dst="include", src="spdlog-%s/include" % (self.version))

    def package_info(self):
        if self.options.fmt_external:
            self.cpp_info.defines.append("SPDLOG_FMT_EXTERNAL")

    def package_id(self):
        self.info.header_only()
