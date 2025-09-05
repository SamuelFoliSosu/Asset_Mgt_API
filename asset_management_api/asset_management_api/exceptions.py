# asset_management_api/exceptions.py
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first
    response = exception_handler(exc, context)

    if response is not None:
        # Standardize error response
        return Response(
            {
                "error": True,
                "status_code": response.status_code,
                "details": response.data
            },
            status=response.status_code
        )

    # Handle cases like 500 server errors
    return Response(
        {
            "error": True,
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "details": "An unexpected error occurred. Please try again later."
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
