{{ cookiecutter.project_slug|replace('-', '_') }}
{{ "=" * cookiecutter.project_slug|length }}

.. testsetup::

    from {{ cookiecutter.project_slug|replace('-', '_') }} import *

.. automodule:: {{ cookiecutter.project_slug|replace('-', '_') }}
    :members:
