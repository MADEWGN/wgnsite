
# membiat sebuah direktori web baru    
def newweb(root_path):
    os.mkdir(root_path)
    
  
    list = ['output', 'content', 'templates'] 

    for items in list: 
        path = os.path.join(root_path, items) 
        os.mkdir(path)
        
    
    
    # ini file html untuk tema

    layout = """


    """
    
    home = """

    """

    postingan = """


    """











    tulissan = """Congratulations! Your new site is created !!
"""        

    print(tulissan)
    exit()

