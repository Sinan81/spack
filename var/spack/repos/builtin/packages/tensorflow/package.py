# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Tensorflow(Package):
    """This package file installs a custom built gpu enabled tensorflow"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
#    url      = "https://files.pythonhosted.org/packages/f4/28/96efba1a516cdacc2e2d6d081f699c001d414cc8ca3250e6d59ae657eb2b/tensorflow-1.14.0-cp37-cp37m-manylinux1_x86_64.whl"
    url      = "file:///disk/software/lib/hpcpm/tensorflow_python/tensorflow-1.12.3-cp27-cp27m-linux_x86_64.whl"
    # below: expand false is necessary for *.whl files
    version('1.12.3', sha256='49717f002b5c98665047a09b5e988342859700769d3197679f6a7a2e8b7f77b1', expand=False)

    depends_on('py-pip', type='build')
    # yep! setuptools is also a run dependency!
    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('python@2.7.16', type=('build', 'run'))
    depends_on('py-keras-applications@1.0.6', type=('build', 'run'))
    depends_on('py-keras-preprocessing@1.0.5', type=('build', 'run'))
    depends_on('py-six', type=('build', 'run'))
    depends_on('cuda@9.2.88', type=('build', 'run'))
    depends_on('cudnn@7.3.0', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-future@0.17.1:', type=('build', 'run'))

    # run dependencies
    depends_on('py-protobuf', type='run')
    depends_on('py-absl-py', type='run')
    depends_on('py-enum34', type='run')
    depends_on('py-pbr', type='run')
    depends_on('py-funcsigs', type='run')
    depends_on('py-mock', type='run')


    def setup_environment(self, spack_env, run_env):
        pver = str(self.spec['python'].version.up_to(2))
        sp_dir = join_path(self.prefix, 'lib/python'+pver+'/site-packages')
        run_env.prepend_path('PYTHONPATH', sp_dir)


    def install(self, spec, prefix):
        pver = str(self.spec['python'].version.up_to(2))
        sp_dir = join_path(self.prefix, 'lib/python'+pver+'/site-packages')
        mkdirp(sp_dir)
        pip = which('pip')
        pip('install', '--no-deps', '--target=' + sp_dir, self.stage.source_path+'/tensorflow-1.12.3-cp27-cp27m-linux_x86_64.whl')
        move(sp_dir+'/bin', self.prefix.bin)

