import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def prepocess_hydrodata():
    # 读取Excel文件
    df = pd.read_excel('hydrodata.xlsx')

    # 将'--'替换为np.nan
    df[['dissolved_oxygen', 'conductivity', 'permanganate_index']] = \
        df[['dissolved_oxygen', 'conductivity', 'permanganate_index']].replace('--', np.nan)
    # 删除包含缺失值的行
    df = df.dropna()

    # 将"date"列转换为日期类型
    df['date'] = pd.to_datetime(df['date'], origin='1899-12-30', unit='D')

    # 将"water_quality"列的数据按照给定的映射进行转换
    quality_type = {'Ⅰ': 1, 'Ⅱ': 2, 'Ⅲ': 3, 'Ⅳ': 4, '劣Ⅴ': 5, 'Ⅴ': 5}
    df['water_quality'] = df['water_quality'].replace(quality_type)

    # 添加新的索引列，并将其名字设为"id"
    df = df.reset_index()
    df = df.rename(columns={'index': 'id'})

    # 将"id"列的值从1开始
    df['id'] = df['id'] + 1

    # 创建数据库引擎
    engine = create_engine('mysql+pymysql://root:root@localhost/oceaninfo2?charset=utf8mb4')

    # 将数据存入指定的数据库
    df.to_sql('hydrodata', engine, if_exists='replace', index=False)

    # 将数据存入新的Excel表格
    # df.to_excel('new_hydrodata.xlsx', index=False)


def preprocess_fish():
    df = pd.read_csv('Fish.csv')

    # 删除包含缺失值的行
    df = df.dropna()

    # 计算length1、length2、length3列的平均值作为新的一列
    df['length'] = df[['length1', 'length2', 'length3']].mean(axis=1)

    index = df.columns.get_loc('length1')
    # 将length列插入到原来length1列的位置
    df.insert(index, 'length', df.pop('length'))

    # 删除length1、length2、length3列
    df = df.drop(['length1', 'length2', 'length3'], axis=1)

    # 添加新的索引列，并将其名字设为"id"
    df = df.reset_index()
    df = df.rename(columns={'index': 'id'})

    # 将"id"列的值从1开始
    df['id'] = df['id'] + 1
    
    # 创建数据库引擎
    engine = create_engine('mysql+pymysql://root:root@localhost/oceaninfo2?charset=utf8mb4')

    # 将数据存入指定的数据库
    df.to_sql('fish', engine, if_exists='replace', index=False)

# prepocess_hydrodata()
# preprocess_fish()
