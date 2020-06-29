# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class PyAzuremlCore(Package):
    """The azureml-core contains functionality for creating and managing:
    * Azure Machine Learning workspaces, experiments and runs;
    * Machine learning compute respources;
    * Models, images and web services.
    """

    homepage = "https://docs.microsoft.com/en-us/azure/machine-learning/service/"
    url      = "https://pypi.io/packages/py3/a/azureml_core/azureml_core-1.8.0-py3-none-any.whl"

    version('1.8.0', sha256='a0f2b0977f18fb7dcb88c314594a4a85c636a36be3d582be1cae25655fea6105', expand=False)

    extends('python')
    depends_on('python@3.5:3.8', type=('build', 'run'))
    depends_on('py-pip', type='build')
    depends_on('py-pytz', type=('build', 'run'))
    depends_on('py-backports-tempfile', type=('build', 'run'))
    depends_on('py-pathspec', type=('build', 'run'))
    depends_on('py-requests@2.19.1:', type=('build', 'run'))
    depends_on('py-azure-mgmt-resource@1.2.1:', type=('build', 'run'))
    depends_on('py-azure-mgmt-containerregistry@2.0.0:', type=('build', 'run'))
    depends_on('py-azure-mgmt-storage@1.5.0:', type=('build', 'run'))
    depends_on('py-azure-mgmt-keyvault@0.40.0:', type=('build', 'run'))
    depends_on('py-azure-mgmt-authorization@0.40.0:', type=('build', 'run'))
    depends_on('py-azure-mgmt-network@10.0:10.999', type=('build', 'run'))
    depends_on('py-azure-graphrbac@0.40.0:', type=('build', 'run'))
    depends_on('py-azure-common@1.1.12:', type=('build', 'run'))
    depends_on('py-msrest@0.5.1:', type=('build', 'run'))
    depends_on('py-msrestazure@0.4.33:', type=('build', 'run'))
    depends_on('py-urllib3@1.23:', type=('build', 'run'))
    depends_on('py-cryptography@:1.8,2.3:', type=('build', 'run'))
    depends_on('py-python-dateutil@2.7.3:', type=('build', 'run'))
    depends_on('py-ndg-httpsclient', type=('build', 'run'))
    depends_on('py-secretstorage', type=('build', 'run'))
    depends_on('py-ruamel-yaml@0.16.8:', type=('build', 'run'))
    depends_on('py-jsonpickle', type=('build', 'run'))
    depends_on('py-contextlib2', type=('build', 'run'))
    depends_on('py-docker', type=('build', 'run'))
    depends_on('py-pyjwt', type=('build', 'run'))
    depends_on('py-adal@1.2.0:', type=('build', 'run'))
    depends_on('py-pyopenssl', type=('build', 'run'))
    depends_on('py-jmespath', type=('build', 'run'))

    def install(self, spec, prefix):
        pip = which('pip')
        pip('install', self.stage.archive_file, '--prefix={0}'.format(prefix))
