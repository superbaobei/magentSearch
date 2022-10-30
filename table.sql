create database if not exists av_id_magnet;
use av_id_magnet;
create  table id_hash_map(
    id int auto_increment primary key comment '主键',
    fanhao varchar(100) not null comment '番号',
    hash varchar(100) not null  comment '磁力',
    used boolean not null default  false comment '是否使用过',
    download_success boolean not null  default true comment '是否下载成功'
)