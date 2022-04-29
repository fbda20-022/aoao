#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import os
from os import getcwd
import pickle
from flask import Flask

directory = getcwd()


# In[4]:


#load the directory
vacancy = (r"C:\Users\EMPIRE\OneDrive - Botswana Accountancy College\Desktop\RnI dataset\vacancy.csv")
candidates = (r"C:\Users\EMPIRE\OneDrive - Botswana Accountancy College\Desktop\RnI dataset\candidates.csv")


# In[43]:


#html
def html_code_table(prod_df,table_name,file_name,side):
    table_style = "<table style='border: 2px solid; float: ' + side + '; width: 40%;'>"
    table_head = "<caption style='text-align: center; caption-side: top; font-size: 140%; font-weight: bold; color:black;'>"+ table_name +'</strong></caption>'
    table_head_row ="<tr><th>jobtitle</th><th>skills (in Rs.)</th><tr>"
                        
    html_code = table_style + table_head_row
            
    for i in range(len(vacancy_df.index)):
        row = "<tr><td>" + str(vacancy_df["jobtitle"][i] + str(vacancy_df["skills"])[i]) + "</td></tr>"
                         
        html_code = html_code + row
                        
    html_code = html_code + "</table>"
                        
    file_path = os.path.join(directory,"templates/")
                        
    hs = open(r"C:\Users\EMPIRE\OneDrive - Botswana Accountancy College\Desktop\RnI dataset\vacancy.csv" + '.html', 'w')
    hs.write(html_code)
                        
    #print(html_code)
                        


# In[25]:


def most_popular_table():
    most_popular_jobtitle = jobtitle_ranking_model.sort_values("Popularity_Rank",ascending = True)[['jobtitle','skills']].head(10)
    
    html_code_table(most_popular_jobtitle,"Most popular jobtitle","mostpopulartable",'left')
    
    #this function calls the html_code_table function to create a .html file for the jobs in demand
    def top_skills_table():
        top_skills_jobtitle = jobtitle_ranking_model.sort_value("Top_skills_Ranks",ascending=True)[['jobtitle','skills']].head(10).reset_index(drop=True)
        
        html_code_table(top_skills,'Top skills in demand',"topskillstable",'right')


# In[29]:


def cand_most_popular_table(Respondent):
    cand_most_popular_skills = cand_jobtitle_ranking_model[cand_jobtitle_ranking_model['Party'] == cand_name]
    cand_most_popular_skills = cand_jobtitle_ranking_model.sort_values("Popularity_Rank",ascending = True)[['jobtitle','skills']].head(10).reset_index(drop=True)
   
    html_code_table(cand_most_popular_jobtitle,"jobtitle frequently applied",'candidatespopulartable','left')
#html_code
def cand_top_skills_table(Respondent):
    cand_top_skills_jobtitle = cand_jobtitle_ranking_model[cand_jobtitle_ranking_model['Party'] == cand_name]
    cand_most_popular_skills = cand_jobtitle_ranking_model.sort_values("Popularity_Rank",ascending = True)[['jobtitle','skills']]
    
#print cand_top_skills
    html_code_table(cand_most_popular_jobtitle,"jobtitle frequently applied",'candidatespopulartable','left')


# In[132]:


def home():
    most_popular_table()
    top_skills_table()
    
    return render_template("home.html")

def login():
    most_popular_table()
    top_skills_table()
    
    cand_name = str(request.args.get('Respondent')).upper()
    
    if cand_name is cand_jobtitle_ranking_model["Party"].unique():
        cand_name_popular_table(cand_name)
        cand_top_skills_table(cand_name)
        recommend_jobtitle_cand_name(cand_name)
        return render_template("cand_home.html",name=cand_name,new='n')
    else:
                           return render_templates("cand_home.html",name=cand, new='y')
        
    
def view():
    
    jobtitle = str(request.args.get('jobtitle')).upper()
    
    if jobtitle is jobtitle_ranking_model["jobtitle"].unique():
        jobtitle_popular_table(jobtitle)
                       


# In[ ]:





# In[ ]:




