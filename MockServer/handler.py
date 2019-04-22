# from flask import request, json
# from sqlalchemy import Column, String, create_engine, Integer
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from config import SQLALCHEMY_DATABASE_URI
#
#
# Base = declarative_base()
#
# class Api(Base):
#
#     # 表的名字:
#     __tablename__ = 'api'
#
#     id = Column(Integer(), primary_key=True)
#     url = Column(String(100))
#
# engine = create_engine(SQLALCHEMY_DATABASE_URI)
#
# DBSession = sessionmaker(bind=engine)
#
#
# def get_response(response, actual):
#     return json.dumps(response, ensure_ascii=False) if response else json.dumps(actual, ensure_ascii=False)
#
#
# def domain_server(**kwargs):
#     """
#     根据传入的api地址,从db里查询到对应的response
#     """
#     url = kwargs.get('url', {})
#
#     # todo 添加request当做过滤参数
#
#     session = DBSession()
#     res = session.query(Api).filter(Api.url == url).one()
#     return res.response

