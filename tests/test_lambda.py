from src.lambda_function import lambda_handler


def test_lambda_handler():
    assert lambda_handler({}, None) == 'OK'
