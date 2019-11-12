from github import Github
#set up
ACCESS_TOKEN = '1fed526d5b1be50ab11c9f159abab6ae0214dfd6'
g = Github(ACCESS_TOKEN)

def search_github(keywords):
    query = '+'.join(keywords) + '+in:readme+in:description'
    result = g.search_repositories(query, 'stars', 'desc')
 
    print(f'Found {result.totalCount} repo(s)')
 
    for repo in result:
        print(f'{repo.clone_url}, {repo.stargazers_count} stars')
 
 
if __name__ == '__main__':
    keywords = input('Enter keyword(s)[e.g python, flask, postgres]: ')
    keywords = [keyword.strip() for keyword in keywords.split(',')]
    search_github(keywords)