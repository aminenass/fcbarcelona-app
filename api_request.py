import requests    
from typing import Any, List, Dict
from dotenv import dotenv_values


API_KEY = dotenv_values(".env").get("X_Auth_Token")
 
headers = { 'X-Auth-Token': API_KEY}    
 

def data_fetch(uri : str , query : str ) -> Any :
    response = requests.get(uri,headers=headers)
    try :  
        response = requests.get(uri,headers=headers) 
        response.raise_for_status()  # Raise an error if fails  
        if query == "matches" : 
            data = [] 
            for match in response.json().get(query,[]):  
                data.append(match)
            return data
        else: 
            for data in response.json().get(query,[]):
                return data 
            return data
      
    
    except requests.RequestException as e:
        print(f"Error fetching data from {uri}: {e}")
        return None

def data_matches() -> List[Dict]:
   return data_fetch(uri="https://api.football-data.org/v4/teams/81/matches",query="matches")

def data_standing_ucl() -> Dict: 
    return data_fetch(uri="http://api.football-data.org/v4/competitions/CL/standings",query="standings")
    
def data_standing_liga() -> Dict:
    return data_fetch(uri="http://api.football-data.org/v4/competitions/PD/standings",query="standings")

