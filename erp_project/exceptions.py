from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    """
    Centralized exception handler for all apps.
    """
    response = exception_handler(exc, context)

    if response is not None:
        return Response({
            "success": False,
            "error_type": exc.__class__.__name__,
            "details": response.data
        }, status=response.status_code)

    # Non-DRF exceptions (500 errors)
    return Response({
        "success": False,
        "error_type": "ServerError",
        "details": "Something went wrong. Please try again later."
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
