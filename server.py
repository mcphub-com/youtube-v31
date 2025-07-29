import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/ytdlfree/api/youtube-v31'

mcp = FastMCP('youtube-v31')

@mcp.tool()
def captions_list(part: Annotated[str, Field(description='')],
                  videoId: Annotated[str, Field(description='')]) -> dict: 
    '''Returns a list of caption tracks that are associated with a specified video'''
    url = 'https://youtube-v31.p.rapidapi.com/captions'
    headers = {'x-rapidapi-host': 'youtube-v31.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'part': part,
        'videoId': videoId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def suggested_videos(relatedToVideoId: Annotated[str, Field(description='')],
                     part: Annotated[str, Field(description='')],
                     type: Annotated[str, Field(description='')],
                     maxResults: Annotated[Union[int, float, None], Field(description='Default: 50')] = None) -> dict: 
    '''Get Similar videos. Original version **deprecated** . Response provided by [Lite version](https://rapidapi.com/genapi/api/youtube-v3-lite) For support, [contact ](https://t.me/api_chat_support)'''
    url = 'https://youtube-v31.p.rapidapi.com/search'
    headers = {'x-rapidapi-host': 'youtube-v31.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'relatedToVideoId': relatedToVideoId,
        'part': part,
        'type': type,
        'maxResults': maxResults,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search(q: Annotated[str, Field(description='')],
           part: Annotated[str, Field(description='')],
           regionCode: Annotated[Union[str, None], Field(description='')] = None,
           maxResults: Annotated[Union[int, float, None], Field(description='Default: 50')] = None,
           order: Annotated[Union[str, None], Field(description='')] = None,
           pageToken: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Search from YouTube'''
    url = 'https://youtube-v31.p.rapidapi.com/search'
    headers = {'x-rapidapi-host': 'youtube-v31.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
        'part': part,
        'regionCode': regionCode,
        'maxResults': maxResults,
        'order': order,
        'pageToken': pageToken,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def video_comments(part: Annotated[str, Field(description='')],
                   videoId: Annotated[str, Field(description='')],
                   maxResults: Annotated[Union[int, float], Field(description='Default: 100')]) -> dict: 
    '''Get YouTube video comments.'''
    url = 'https://youtube-v31.p.rapidapi.com/commentThreads'
    headers = {'x-rapidapi-host': 'youtube-v31.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'part': part,
        'videoId': videoId,
        'maxResults': maxResults,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def comment_info(part: Annotated[str, Field(description='')],
                 id: Annotated[str, Field(description='')],
                 parentId: Annotated[Union[str, None], Field(description='')] = None,
                 maxResults: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''Get comments info.'''
    url = 'https://youtube-v31.p.rapidapi.com/comments'
    headers = {'x-rapidapi-host': 'youtube-v31.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'part': part,
        'id': id,
        'parentId': parentId,
        'maxResults': maxResults,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def video_details(part: Annotated[str, Field(description='')],
                  id: Annotated[str, Field(description='')]) -> dict: 
    '''Get YouTube video details. Note: **topicDetails** part is not enabled. If you want this part to be included in the API response then please contact us.'''
    url = 'https://youtube-v31.p.rapidapi.com/videos'
    headers = {'x-rapidapi-host': 'youtube-v31.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'part': part,
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def channel_details(part: Annotated[str, Field(description='')],
                    id: Annotated[str, Field(description='')]) -> dict: 
    '''Get channel details'''
    url = 'https://youtube-v31.p.rapidapi.com/channels'
    headers = {'x-rapidapi-host': 'youtube-v31.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'part': part,
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def channel_videos(channelId: Annotated[str, Field(description='')],
                   part: Annotated[str, Field(description='')],
                   order: Annotated[Union[str, None], Field(description='')] = None,
                   maxResults: Annotated[Union[str, None], Field(description='')] = None,
                   pageToken: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get channel videos'''
    url = 'https://youtube-v31.p.rapidapi.com/search'
    headers = {'x-rapidapi-host': 'youtube-v31.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'channelId': channelId,
        'part': part,
        'order': order,
        'maxResults': maxResults,
        'pageToken': pageToken,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def playlist_videos(playlistId: Annotated[str, Field(description='')],
                    part: Annotated[str, Field(description='')],
                    maxResults: Annotated[Union[str, None], Field(description='')] = None,
                    pageToken: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get playlist videos'''
    url = 'https://youtube-v31.p.rapidapi.com/playlistItems'
    headers = {'x-rapidapi-host': 'youtube-v31.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'playlistId': playlistId,
        'part': part,
        'maxResults': maxResults,
        'pageToken': pageToken,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def playlist_details(id: Annotated[str, Field(description='')],
                     part: Annotated[str, Field(description='')]) -> dict: 
    '''Get playlist details'''
    url = 'https://youtube-v31.p.rapidapi.com/playlists'
    headers = {'x-rapidapi-host': 'youtube-v31.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'part': part,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
