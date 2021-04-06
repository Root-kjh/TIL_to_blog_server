# TIL_to_blog_server
TIL Repo를 React Blog로 변환


# API Docs

## TIL posts

### explorer

Request GET: /TIL/explorer/:path

Response json: {file_type, file_context}

```
{
    file_type: file,
    file_context: readme_context
}

{
    file_type: folder,
    file_context: file_list
}
```

### search

Request GET: /TIL/search/:keyword

Response json: {file_list(file_name, file_path)}

```
{
    file_list:[
        {file_name: file_a, file_path: /test/file_a},
        {file_name: file_b, file_path: /test/file_b},
        {file_name: file_c, file_path: /test/file_c}
    ]
}
```