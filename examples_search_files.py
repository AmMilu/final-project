from github import Github
#set up
ACCESS_TOKEN = '1fed526d5b1be50ab11c9f159abab6ae0214dfd6'
g = Github(ACCESS_TOKEN)

def search_github(keyword):
    rate_limit = g.get_rate_limit()
    rate = rate_limit.search
    if rate.remaining == 0:
        print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}')
        return
    else:
        print(f'You have {rate.remaining}/{rate.limit} API calls remaining')
 
    query = f'"{keyword} english" in:file extension:po'
    result = g.search_code(query, order='desc')
 
    max_size = 100
    print(f'Found {result.totalCount} file(s)')
    if result.totalCount > max_size:
        result = result[:max_size]
 
    for file in result:
        print(f'{file.download_url}')
 
 
if __name__ == '__main__':
    keyword = input('Enter keyword[e.g french, german etc]: ')
    search_github(keyword)