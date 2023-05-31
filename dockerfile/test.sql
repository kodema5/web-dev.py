-- designed for individual file test
-- psql --quiet -v ON_ERROR_STOP=1 -U postgres -d postgres -f /test.sql -v test_file=file-to-test.sql

---------------------------------------------------------------------------

set client_min_messages to warning;
-- \echo '-- test for' :test_file

---------------------------------------------------------------------------
-- setup tests schema for test functions
-- install pg-tap https://pgtap.org/

drop schema if exists tests cascade;
create schema if not exists tests;

create extension if not exists pgtap;

\set drop :drop
\set test true

---------------------------------------------------------------------------
-- prevent drops when not local

\if :drop
\else
create or replace function tests.web_dev_no_sql_drops()
    returns event_trigger
    language plpgsql
as $$
declare
    r record;
    f boolean;
begin
    for r in
        select *
        from pg_event_trigger_dropped_objects()
    loop
        if r.object_type='schema' and right(r.object_identity,1) = '_'
        or right(r.schema_name,1) = '_'
        then
            -- raise warning '---- % (%) % %'
            --     , tg_tag
            --     , r.object_type
            --     , r.schema_name
            --     , r.object_identity;
            raise exception 'web_dev_sql_drops cancels % %'
                , tg_tag
                , r.object_identity;
        end if;
    end loop;
end;
$$;

drop event trigger if exists web_dev_no_sql_drops;
create event trigger web_dev_no_sql_drops
    on sql_drop
    execute function tests.web_dev_no_sql_drops();

\endif


---------------------------------------------------------------------------
-- save current search_path

create or replace function tests.last(a anyarray)
returns anyelement as $$
    select a[array_upper(a,1)]
$$ language sql immutable strict;

select current_setting('search_path')  as old_search_path,
    tests.last(string_to_array(:'test_file', '/')) as test_filename
\gset


---------------------------------------------------------------------------
-- setup dev schema for default temporary schema

-- drop schema if exists dev cascade;
-- create schema dev;
-- \set dev true
-- set schema 'dev';

---------------------------------------------------------------------------
-- include combinations of files
-- from -v test_file=..... parameter

\set ON_ERROR_STOP 0
\i :test_file
\set ON_ERROR_STOP 1


---------------------------------------------------------------------------
-- set search_path for tests
-- it will be reset in next session
--
select set_config('search_path',
    :'old_search_path' || ',tests',
    false) as new_search_path
\gset


---------------------------------------------------------------------------
-- run tests

\set test_pattern :test_pattern
select case
    when :'test_pattern' = ':test_pattern' then '^test'
    else :'test_pattern'
end as test_pattern \gset

set client_min_messages to notice;
select * from runtests('tests'::name, :'test_pattern');
set client_min_messages to warning;


---------------------------------------------------------------------------
-- clean-up event-trigger and tests schema

drop event trigger if exists web_dev_no_sql_drops;
drop schema if exists tests cascade;

