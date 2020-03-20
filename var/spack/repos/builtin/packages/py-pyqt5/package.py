# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class PyPyqt5(SIPPackage):
    """PyQt is a set of Python v2 and v3 bindings for The Qt Company's Qt
    application framework and runs on all platforms supported by Qt including
    Windows, OS X, Linux, iOS and Android. PyQt5 supports Qt v5."""

    homepage = "https://www.riverbankcomputing.com/software/pyqt/intro"
    url      = "https://www.riverbankcomputing.com/static/Downloads/PyQt5/5.13.0/PyQt5_gpl-5.13.0.tar.gz"
    list_url = "https://www.riverbankcomputing.com/software/pyqt/download5"

    sip_module = 'PyQt5.sip'
    import_modules = [
        'PyQt5', 'PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtHelp',
        'PyQt5.QtMultimedia', 'PyQt5.QtMultimediaWidgets', 'PyQt5.QtNetwork',
        'PyQt5.QtOpenGL', 'PyQt5.QtPrintSupport', 'PyQt5.QtQml',
        'PyQt5.QtQuick', 'PyQt5.QtSvg', 'PyQt5.QtTest', 'PyQt5.QtWebChannel',
        'PyQt5.QtWebSockets', 'PyQt5.QtWidgets', 'PyQt5.QtXml',
        'PyQt5.QtXmlPatterns'
    ]

    version('5.13.1', sha256='54b7f456341b89eeb3930e786837762ea67f235e886512496c4152ebe106d4af')
    version('5.13.0', sha256='0cdbffe5135926527b61cc3692dd301cd0328dd87eeaf1313e610787c46faff9')
    version('5.12.3', sha256='0db0fa37debab147450f9e052286f7a530404e2aaddc438e97a7dcdf56292110')


    # Without opengl support, I got the following error:
    # sip: QOpenGLFramebufferObject is undefined
    depends_on('qt@5:+opengl')
    depends_on('python@2.6:', type=('build', 'run'))
    depends_on('py-enum34', type=('build', 'run'), when='^python@:3.3')
    depends_on('py-sip module=PyQt5.sip', type=('build', 'run'))
    depends_on('py-sip@:4.19.18 module=PyQt5.sip', type=('build', 'run'), when='@:5.13.0')

    # https://www.riverbankcomputing.com/static/Docs/PyQt5/installation.html
    def configure_args(self):
        args = [
            '--pyuic5-interpreter', self.spec['python'].command.path,
            '--sipdir', self.prefix.share.sip.PyQt5,
            '--stubsdir', join_path(
                self.prefix,
                self.spec['python'].package.site_packages_dir,
                'PyQt5'),
        ]
        # TODO Is the following still necessary now that 
        # Qsci python bindings are built with Qscintilla package
        if '+qsci' in self.spec:
            args.extend(['--qsci-api-destdir', self.prefix.share.qsci])
        return args
