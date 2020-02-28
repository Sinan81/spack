# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Qgis(CMakePackage):
    """QGIS is a free and open-source cross-platform desktop geographic
    information system application that supports viewing, editing, and
    analysis of geospatial data.
    """

    homepage = "https://qgis.org"
    url      = "https://qgis.org/downloads/qgis-3.8.1.tar.bz2"

    maintainers = ['adamjstewart', 'Sinan81']

    version('3.12.0', sha256='19e9c185dfe88cad7ee6e0dcf5ab7b0bbfe1672307868a53bf771e0c8f9d5e9c')
    version('3.10.3', sha256='0869704df9120dd642996ff1ed50213ac8247650aa0640b62f8c9c581c05d7a7')
    version('3.10.2', sha256='381cb01a8ac2f5379a915b124e9c830d727d2c67775ec49609c7153fe765a6f7')
    version('3.10.1', sha256='466ac9fad91f266cf3b9d148f58e2adebd5b9fcfc03e6730eb72251e6c34c8ab')
    version('3.10.0', sha256='25eb1c41d9fb922ffa337a720dfdceee43cf2d38409923f087c2010c9742f012')
    version('3.8.3', sha256='3cca3e8483bc158cb8e972eb819a55a5734ba70f2c7da28ebc485864aafb17bd')
    version('3.8.2', sha256='4d682f7625465a5b3596b3f7e83eddad86a60384fead9c81a6870704baffaddd')
    # Prefer v3.8.1 for now as we haven't checked if newer versions compile
    version('3.8.1', sha256='d65c8e1c7471bba46f5017f261ebbef81dffb5843a24f0e7713a00f70785ea99', preferred=True)
    # Latest long term release
    version('3.4.14', sha256='e138716c7ea84011d3b28fb9c75e6a79322fb66f532246393571906a595d7261')

    variant('3d',               default=False, description='')
    variant('analysis',         default=True, description='')
    variant('astyle',           default=False, description='')
    variant('bindings',         default=True, description='')
    variant('clang_tidy',       default=False, description='')
    variant('core',             default=True, description='')
    variant('custom_widgets',   default=False, description='')
    variant('desktop',          default=True, description='')
    variant('georeferencer',    default=True, description='')
    variant('globe',            default=False, description='')
    variant('grass7',           default=False, description='Build with GRASS providers and plugin')
    variant('gui',              default=True, description='')
    variant('internal_mdal',    default=True, description='')
    variant('internal_o2',      default=True, description='')
    variant('oauth2_plugin',    default=True, description='')
    variant('oracle',           default=False, description='')
    variant('postgresql',       default=True, description='')
    variant('py_compile',       default=False, description='')
    variant('qsciapi',          default=True, description='')
    variant('qspatialite',      default=False, description='')
    variant('qt5serialport',    default=True, description='')
    variant('qtmobility',       default=False, description='')
    variant('qtwebkit',         default=False, description='')
    variant('quick',            default=False, description='')
    variant('qwtpolar',         default=False, description='')
    variant('server',           default=False, description='')
    variant('staged_plugins',   default=True, description='')
    variant('thread_local',     default=True, description='')
    variant('txt2tags',         default=False, description='')

    # Ref. for dependencies:
    # http://htmlpreview.github.io/?https://raw.github.com/qgis/QGIS/master/doc/INSTALL.html
    depends_on('qt+dbus')
    depends_on('proj@4.4.0:')
    depends_on('geos@3.4.0:')
    depends_on('sqlite@3.0.0: +column_metadata')
    depends_on('libspatialite@4.2.0:')
    depends_on('libspatialindex')
    depends_on('gdal@2.1.0: +python', type=('build', 'link', 'run'))
    depends_on('qwt@5:')
    depends_on('qwtpolar')
    depends_on('expat@1.95:')
    depends_on('qca@2.2.1') # need to pass CMAKE_CXX_STANDARD=11 option
    depends_on('py-pyqt4 +qsci', when='@2')
    depends_on('py-pyqt5@5.3: +qsci', when='@3')
    depends_on('qscintilla')
    depends_on('qjson')
    depends_on('py-requests', type=('build', 'run')) # TODO: is build dependency necessary?
    depends_on('py-psycopg2', type=('build', 'run')) # TODO: is build dependency necessary?
    depends_on('qtkeychain@0.5:', when='@3:')
    depends_on('libzip')
    depends_on('exiv2')
    depends_on('python@3.0.0:', type=('build', 'run'), when='@3')
    depends_on('python@2.7:2.8', type=('build', 'run'), when='@2')

    # Runtime python dependencies, not mentioned in install instructions
    depends_on('py-pyyaml', type='run')
    depends_on('py-owslib', type='run')
    depends_on('py-jinja2', type='run')
    depends_on('py-pygments', type='run')

    # optionals
    depends_on('postgresql@8:') # for PostGIS support
    depends_on('gsl') # for georeferencer
    depends_on('grass@7.0.0', type=('build', 'link', 'run'), when='+grass7') # for georeferencer

    # the below dependencies are shown in cmake config
    depends_on('hdf5')
    depends_on('netcdf-c')

    # build
    depends_on('cmake@3.0.0:', type='build')
    depends_on('flex@2.5.6:', type='build')
    depends_on('bison@2.4:', type='build')
    depends_on('pkg-config', type='build')

    # Conflicts for newer versions
    conflicts('proj@:4.9.2', when='@3.8.2:')

    # v3.8.1, Qt >= 5.9.0 is required
    conflicts('qt@:5.8.99', when='@3.8.1:')

    # conflicts for qgis@2, qt@4, python@2
    conflicts('qtkeychain@0.6.0:', when='^qt@4')
    conflicts('qt@5:', when='@2')

    # TODO: expose all cmake options available
#    WITH_3D:BOOL=FALSE
#    WITH_ANALYSIS:BOOL=TRUE
#    WITH_APIDOC:BOOL=FALSE
#    WITH_ASTYLE:BOOL=FALSE
#    WITH_BINDINGS:BOOL=TRUE
#    WITH_CLANG_TIDY:BOOL=FALSE
#    WITH_CORE:BOOL=TRUE
#    WITH_CUSTOM_WIDGETS:BOOL=FALSE
#    WITH_DESKTOP:BOOL=TRUE
#    WITH_GEOREFERENCER:BOOL=TRUE
#    WITH_GLOBE:BOOL=FALSE
#    WITH_GRASS7:BOOL=OFF
#    WITH_GUI:BOOL=TRUE
#    WITH_INTERNAL_MDAL:BOOL=TRUE
#    WITH_INTERNAL_O2:BOOL=ON
#    WITH_OAUTH2_PLUGIN:BOOL=TRUE
#    WITH_ORACLE:BOOL=FALSE
#    WITH_POSTGRESQL:BOOL=TRUE
#    WITH_PY_COMPILE:BOOL=FALSE
#    WITH_QSCIAPI:BOOL=TRUE
#    WITH_QSPATIALITE:BOOL=OFF
#    WITH_QT5SERIALPORT:BOOL=TRUE
#    WITH_QTMOBILITY:BOOL=FALSE
#    WITH_QTWEBKIT:BOOL=OFF
#    WITH_QUICK:BOOL=FALSE
#    WITH_QWTPOLAR:BOOL=FALSE
#    WITH_SERVER:BOOL=FALSE
#    WITH_STAGED_PLUGINS:BOOL=TRUE
#    WITH_THREAD_LOCAL:BOOL=TRUE
#    WITH_TXT2TAGS_PDF:BOOL=FALSE

    def cmake_args(self):
        args = []
        # qtwebkit module was removed from qt as of version 5.6
        # needs to be compiled as a separate package
        args.extend(['-DWITH_QTWEBKIT=OFF',
            '-DWITH_QSPATIALITE=OFF',
            '-DUSE_OPENCL=OFF',
            # cmake couldn't determine the following paths
            '-DEXPAT_LIBRARY={0}'.format(self.spec['expat'].libs),
            '-DPOSTGRESQL_PREFIX={0}'.format(self.spec['postgresql'].prefix),
            '-DQSCINTILLA_INCLUDE_DIR='+str(self.spec['qscintilla'].prefix)+'/include',
            '-DQSCINTILLA_LIBRARY='+str(self.spec['qscintilla'].prefix)+'/lib/libqscintilla2_qt5.so',
            '-DLIBZIP_INCLUDE_DIR='+str(self.spec['libzip'].prefix)+'/include',
            '-DLIBZIP_CONF_INCLUDE_DIR='+str(self.spec['libzip'].prefix)+'/lib/libzip/include',
            '-DGDAL_CONFIG_PREFER_PATH='+str(self.spec['gdal'].prefix.bin),
            '-DGEOS_CONFIG_PREFER_PATH='+str(self.spec['geos'].prefix.bin),
            '-DGSL_CONFIG_PREFER_PATH='+str(self.spec['gsl'].prefix.bin),
            '-DPOSTGRES_CONFIG_PREFER_PATH='+str(self.spec['postgresql'].prefix.bin)
        ])

        if '+grass7' in self.spec:
            args.extend(['-DWITH_GRASS7=ON',
                '-DGRASS_PREFIX7={0}'.format(self.spec['grass'].prefix),
                '-DGRASS_INCLUDE_DIR7={0}'.format(self.spec['grass'].prefix.include)
            ])
        else:
            args.append('-DWITH_GRASS7=OFF')
        return args
