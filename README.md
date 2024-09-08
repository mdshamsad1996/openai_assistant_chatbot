# openai_assistant_chatbot

#### Steps to Exceute the project
##### 1.Check your python version 
-   ```Python --version```

#####   2.Create virtual environment 
-   ```create -n openai_assitannt_chatbot_env python=<python version> -y```

-   ```create -n openai_assitannt_chatbot_env python=3.11 -y```

#####   3. Activate the virtual environment with the following command

-   ```conda activate openai_assitannt_chatbot_env```

##### 4. Install Dependencies
-   ```pip install -r requirements.text```

#### 5. Create .env file and add below key

-   ```PINECONE_API_KEY = "****************************************************************"```
-   ```OPENAI_API_KEY = "****************************************************************```

####    6. Command to run the porjcet
-   ```streamlit run app.py```