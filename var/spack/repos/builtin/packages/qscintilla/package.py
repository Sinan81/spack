# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os

class Qscintilla(QMakePackage):
    """
    QScintilla is a port to Qt of Neil Hodgson's Scintilla C++ editor control.
    """

    homepage = "https://www.riverbankcomputing.com/software/qscintilla/intro"
    url      = "https://www.riverbankcomputing.com/static/Downloads/QScintilla/2.11.2/QScintilla_gpl-2.11.2.tar.gz"

    version('2.11.2', sha256='029bdc476a069fda2cea3cd937ba19cc7fa614fb90578caef98ed703b658f4a1')
    # Newer versions of Qscintilla won't build, so prefer the following version
    version('2.10.2', sha256='14b31d20717eed95ea9bea4cd16e5e1b72cee7ebac647cba878e0f6db6a65ed0', preferred=True)


    variant('designer', default=False, description="Enable pluging for Qt-Designer")
    # No 'python' variant, since Python bindings will be
    # built by PyQt5+qsci instead

    depends_on('qt')


    @run_before('qmake')
    def chdir(self):
        os.chdir(str(self.stage.source_path)+'/Qt4Qt5')


    def qmake_args(self):
        # below, DEFINES ... gets rid of ...regex...errors during build
        # although, there shouldn't be such errors since we use '-std=c++11'
        args = ['CONFIG+=-std=c++11', 'DEFINES+=NO_CXX11_REGEX=1']
        return args


    # When INSTALL_ROOT is unset, qscintilla is installed under qt_prefix
    # giving 'Nothing Installed Error'
    def setup_environment(self, spack_env, run_env):
        spack_env.set('INSTALL_ROOT', self.prefix)


    # Fix install prefix
    @run_after('qmake')
    def fix_install_path(self):
        makefile = FileFilter('Makefile')
        makefile.filter(r'\$\(INSTALL_ROOT\)' + self.spec['qt'].prefix, '$(INSTALL_ROOT)')


    # Install source under prefix so that
    # Python bindings can be built by PyQt5 later on.
    @run_after('install')
    def postinstall(self):
        keep_src()
        make_designer()


    def keep_src(self):
        install_tree(self.stage.source_path, prefix.share+'/qscintilla/src')


    def make_designer(self):
        if '+designer' in self.spec:
            os.chdir(str(self.stage.source_path)+'/designer-Qt4Qt5')
            qmake()
            make()
            make('install')
