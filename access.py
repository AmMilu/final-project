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
ACCESS_TOKEN = '43fa63c2ef98b7dd8e0c76ee4560aee7686960f'
g = Github(ACCESS_TOKEN+'6')

def search_user():
    user = g.get_user(login='jquery')
    i = vars(user)
    p = i["_rawData"]
    print('\n'.join("%s: %s" % item for item in p.items()))

def search_repo():
    repo = g.get_user(login='jquery').get_repos()
    for i in repo:
        print(i)

def search_sepcific_repo():
    repo = g.get_user(login='jquery').get_repo('jquery')
    print(repo)

def search_commit():
    commit = g.get_user(login='jquery').search_commit(query='jquery')
    print(commit)

if __name__ == '__main__':
    search_user()