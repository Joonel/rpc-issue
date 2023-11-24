# rpc-issue

The repo demonstates the [issue]([url](https://github.com/supabase-community/supabase-py/issues/405)https://github.com/supabase-community/supabase-py/issues/405) with supabase-py rpc method.

DB function code:
```
begin
  return query
  select
    docs.id,
    docs.content,
    1 - (docs.embedding <=> query_embedding) as similarity
  from docs
  where 1 - (docs.embedding <=> query_embedding) > match_threshold
  order by similarity desc
  limit match_count;
end;
```
Look in the SB interface:
![image](https://github.com/Joonel/rpc-issue/assets/69682842/edbe014a-2fee-44f0-9cec-b8c13c87ceeb)
