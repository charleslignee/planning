
#%%
input_data = {}
lign = "Jan4=bibliographie:6.5h;code_articlereview:1h|appropriation du code & de l'outil git #2e journée de travail"
if "=" in lign:
    list_content = []                      
    for content in lign.split('=')[1].split('#')[0].split(';'):
        list_content.append(content.split('|')[0].split(':'))
    input_data.update({lign.split('=')[0]:list_content})

# %%
