def get_google_place(key_word,zip_list,city,state):
    #google places API 
    api_key='AIzaSyB_i6T2QOcNmKeJUxF6FC5B1XN1j-mixjI'

#     key_word='chinese'
    search_type='restaurant'
    root_url='https://maps.googleapis.com/maps/api/place/textsearch/json?'
    try:
        output_folder=os.makedirs('output_{}_in_{}_{}'.format(key_word,city,state))
    except OSError as e:
        output_folder='output_{}_in_{}_{}'.format(key_word,city,state)
        
    info_list=[]
    #loop in zip_code list
    for i in zip_list:
        #set up a page counter
        page=1
        # print(page)
        #set up url for the first call 
        initial_url=root_url+'query={}+in+{}'.format(key_word,i)+'&type='+search_type+'&key='+api_key
        response=requests.get(initial_url).json()
        
        #extract results in a variable called results
        results=response['results']
        
        print('zip_code:{} page:{}/n {}/n/n'.format(i,page,initial_url))
        print('debug hey i have {} restaurants'.format(len(results)))
        
        #assign a variable to store nextpage token
        next_page=response.get("next_page_token")
        
        #sometimes it give me empty results if I make calls too often 
        sleep(5)
        
        #use a while loop for flipping pages, google allows a maximum of 3 pages 
        while bool(next_page)==True: 
            # print('debug hey I am under the while loop')
            #update page counter
            page+=1
            # print('debug the current page is {}'.format(page))
            #set up API call for the next page and logging it
            next_page_url=root_url+"pagetoken="+next_page+'&key='+api_key
            # print('zip_code:{} page:{}/n {}/n/n'.format(i,page,next_page_url))
            response=requests.get(next_page_url).json()
            # print('debug current page has {} restaurants'.format(len(response['results'])))
            
            #Add the new results to results here using + NOT append because:
            #list_1=[1,2,3] list_2=[4,5,6] list_1+list_2=[1,2,3,4,5,6]
            #list_1.append(list2)------[1,2,3,[4,5,6]]
            results=results+response["results"]
            # print('debug now i have a total of {} restaurants'.format(len(results)))
            sleep(2)
            #update next_page token
            next_page=response.get("next_page_token")
            # print('debug the current token is {}'.format(next_page))
            
        #__________________________________________________________ 
        #output restaurant results for each zipcode as a txt file text
        #__________________________________________________________
        info_list=info_list+results
        output_name='google_place_API_{}_{}_{}_{}.txt'.format(key_word,i,city,state)
        output_path=os.path.join(output_folder, output_name)
        with open(output_path,'w') as output:
            json.dump(results,output,indent=4)
    return info_list