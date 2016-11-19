drop table if exists representatives;
create table representatives (
    id integer primary key autoincrement,
    first_name text not null,
    last_name text not null,
    state text not null,
    district text not null,
    phone text not null
);
