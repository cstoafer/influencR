drop table if exists representatives;
create table representatives (
    id integer primary key autoincrement,
    first_name text not null,
    last_name text not null,
    district real not null,
    phone real not null
);
