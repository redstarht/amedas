import requests

class Amedas_Api():
    #なかったらアメダスへアクセスして、取ってくる

    DEFAULT_BASE_URL = "https://api.cultivationdata.net/" #インスタンスする前に使える

    def __init__(self,url: str=DEFAULT_BASE_URL) -> None: #return で帰ってくるのはNone
        # url = DEFAULT_BASE_URL でurlに引数として何も渡されない場合は DEFAULT_BASE_URLをいれてくれる
        self.base_url=url #self = インスタンス インスタンス生成時にurlを持たせるようにする

    def fetch_kako_data(self,index_nbr:int,year:int,month:int):
        targer_url=self.base_url+"past"
        params={
            "no": index_nbr,
            "year":year,
            "month":month
        }

        response = requests.get(targer_url,params=params)
        print(response.status_code)
        if response.status_code == 200:
            return response.json()
        else:
            return[]
            # raise xxxxError