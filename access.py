#this file is used to access Github API


#this is just an example about how to get data from JSON
#some JSON:
#x = '{"name":"John"."age":30,"city":"New York"}'
#parse x:
#y = json.loads(x)
#the result is a python dictionary
#print(y["age"])

from github import Github
#set up
ACCESS_TOKEN = '1fed526d5b1be50ab11c9f159abab6ae0214dfd6'
g = Github(ACCESS_TOKEN)
    

if __name__ == '__main__':
    repo = g.get_repos("jquery")