workspace(name = "perlrulesbug")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "954aa89b491be4a083304a2cb838019c8b8c3720a7abb9c4cb81ac7a24230cea",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.4.0/rules_python-0.4.0.tar.gz",
)


http_archive(
    name = "rules_perl",
    sha256 = "9661de92edd38cc878010a4e42088f5ffda3f1e8b7d1124a5cea943e2fb03c0f",
    strip_prefix = "rules_perl-03de09c1dff31920d7bedda0d519e178dd1f1448",
    url = "https://github.com/bazelbuild/rules_perl/archive/03de09c1dff31920d7bedda0d519e178dd1f1448.zip",
)

load("@rules_perl//perl:deps.bzl", "perl_register_toolchains", "perl_rules_dependencies")

perl_rules_dependencies()

perl_register_toolchains()


