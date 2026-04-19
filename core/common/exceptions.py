from rest_framework.views import exception_handler
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        return Response(
            {
                "success": False,
                "message": "Erro interno do servidor.",
                "errors": None,
            },
            status=500,
        )

    return Response(
        {
            "success": False,
            "message": "Requisição inválida.",
            "errors": response.data,
        },
        status=response.status_code,
    )