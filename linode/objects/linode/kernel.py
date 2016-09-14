from linode.objects import Base, Property

class Kernel(Base):
    api_name = 'kernels'
    api_endpoint="/linode/kernels/{id}"
    properties = {
        "created": Property(is_datetime=True),
        "deprecated": Property(filterable=True),
        "description": Property(),
        "id": Property(identifier=True),
        "kvm": Property(filterable=True),
        "label": Property(filterable=True),
        "updates": Property(),
        "version": Property(filterable=True),
        "x64": Property(filterable=True),
        "xen": Property(filterable=True),
    }