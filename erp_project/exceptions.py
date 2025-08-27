import logging
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    """
    Centralized exception handler for all apps.
    """
    response = exception_handler(exc, context)
    view_name = context.get('view', None)
    view_name_str = view_name.__class__.__name__ if view_name else "UnknownView"


    if response is not None:
        # Log DRF-handled exceptions
        logger.error(f"[{view_name_str}] {exc.__class__.__name__}: {response.data}")
        return Response({
            "success": False,
            "error_type": exc.__class__.__name__,
            "details": response.data
        }, status=response.status_code)
    
    # Log unhandled exceptions (500)
    logger.critical(f"[{view_name_str}] Unhandled Exception: {str(exc)}", exc_info=True)

    # Non-DRF exceptions (500 errors)
    return Response({
        "success": False,
        "error_type": "ServerError",
        "details": "Something went wrong. Please try again later."
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
