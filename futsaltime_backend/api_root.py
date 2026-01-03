from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'auth': reverse('auth-root', request=request, format=format),
        'fields': reverse('field-list', request=request, format=format),
        'reservations': reverse('reservation-list', request=request, format=format),
        'docs': reverse('swagger-ui', request=request, format=format),
    })
