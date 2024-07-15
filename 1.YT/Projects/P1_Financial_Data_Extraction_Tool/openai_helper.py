import openai
from secret_key import openai_key
import json
import pandas as pd

## Setting up the Open AI API key in openai.api_key variable
openai.api_key = openai_key


'''
def poem_on_taj_mahal():
    prompt = 'Write a poem on Taj Mahal . Only 4 lines please'
    ## OpenAI Chat Completion API Overview 
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role":"user","content":"Write a poem on Taj Mahal . Only 4 lines please"}
        ]
    )

    ## Ans is stored in reponse - choices[0] - message - content 
    print(response.choices[0]['message']['content'])

'''

def get_prompt_financial():
    return '''Please retrieve company name, revenue, net income and earnings per share (a.k.a. EPS)
    from the following news article. If you can't find the information from this article 
    then return "". Do not make things up.    
    Then retrieve a stock symbol corresponding to that company. For this you can use
    your general knowledge (it doesn't have to be from this article). Always return your
    response as a valid JSON string. The format of that string should be this, 
    {
        "Company Name": "Walmart",
        "Stock Symbol": "WMT",
        "Revenue": "12.34 million",
        "Net Income": "34.78 million",
        "EPS": "2.1 $"
    }
    News Article:
    ============

    '''

## This function will take news article as input 
def extract_financial_data(text):
    prompt = get_prompt_financial() + text 
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages=[
            {"role":"user","content":prompt}
        ]
    )
    ## In prompt we have said that we want our repsonse in JSON.
    content = response.choices[0]['message']['content']
    ## loads - loadstring will convert the string into dict formal 
    try : 
        data = json.loads(content)
        ## Pandas data.items will create rows and columns 
        ## We will use streamlit . And in streamlit . You can directly render Dataframe
        return pd.DataFrame(data.items(),columns=['Measure','Value'])
    
    except(json.JSONDecodeError,IndexError):
        pass

    ## If we code fails in try . we will return following message
    return pd.DataFrame({
        "Measure":["Company Name","Stock Symbol","Revenue","Net Income","EPS"],
        "Value":["","","","",""]
    })



if __name__ == "__main__":
    ##poem_on_taj_mahal()
    text = '''Tesla's Earning news in text format: Tesla's earning this quarter blew all the estimates. They reported 4.5 billion $ profit against a revenue of 30 billion $. Their earnings per share was 2.3 $'''
    df = extract_financial_data(text)
    print(df.to_string())
