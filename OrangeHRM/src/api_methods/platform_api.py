
from src.configs.global_params import BASE_URL
from src.helpers.helper_methods import validate_response_status
from playwright.async_api import APIRequestContext,APIResponse

class PlatformAPI :
    def __init__(self, api_context: APIRequestContext) -> None:
        self.api_context = api_context
    

    # The auth-token generation request API call isn't publicly accessed. It's just a high level mock up
    async def generate_auth_token(self, request_endpoint: str, expected_status: int, expected_status_text: str):
        response: APIResponse = self.api_context.post() 

        validate_response_status(response,expected_status,expected_status_text)

    
    async def post_api(self, request_endpoint: str, request_data: any, expected_status:int, expected_status_text: str):
        response: APIResponse = self.api_context.post(url= f"{BASE_URL}{request_endpoint}",
                                          data=request_data,
                                          headers={'Content-Type': 'application/x-www-form-urlencoded'})
        
        validate_response_status(response,expected_status,expected_status_text)

    
    async def get_page_info(self, request_endpoint: str, expected_status: int, expected_status_text: str):
        response : APIResponse = self.api_context.get(url=f"{BASE_URL}{request_endpoint}")

        validate_response_status(response,expected_status,expected_status_text)

        
        
        
