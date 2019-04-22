import traceback

from flask import json
from sqlalchemy.exc import IntegrityError
from MockServer import models, db


def insert_project(**kwargs):
    try:
        name = kwargs.pop('name')
        desc = kwargs.pop('desc')
    except KeyError:
        return {
            'success': False,
            'code': '0001',
            'msg': '名称或者描述没有填写'
        }

    if name == '' or desc == '':
        return {
            'success': False,
            'code': '0002',
            'msg': '名称或者描述不能为空'
        }

    elif models.Project.query.filter_by(name=name).count() > 0:
        return {
            'success': False,
            'code': '0003',
            'msg': '{name} 已经存在'.format(name=name)
        }
    else:
        p = models.Project(name=name, desc=desc)
        db.session.add(p)
        try:
            db.session.commit()
            return {
                'success': True,
                'code': '0000',
                'msg': 'success'
            }
        except Exception:
            return {
                'success': False,
                'code': '0004',
                'msg': '系统异常',
                'traceback': traceback.format_exc()
            }


def insert_mock_data(**kwargs):
    try:
        name = kwargs.pop('name')
        project = kwargs.pop('project')
        url = kwargs.pop('url')
        method = kwargs.pop("method")
        request = kwargs.pop("request")
        response = kwargs.pop("response")
    except KeyError:
        return {
            'success': False,
            'code': '1005',
            'msg': 'name或者path没有填写'
        }

    if project == '':
        return {
            'success': False,
            'code': '0006',
            'msg': '请选择项目'
        }

    if name == '' or url == '':
        return {
            'success': False,
            'code': '0007',
            'msg': 'name或者path不能为空'
        }

    args = ['GET', 'POST', 'PUT', 'DELETE']

    if method.upper() not in args:
        return {
            'success': False,
            'code': '0008',
            'msg': '方法必须是 {args} 其中一个'.format(args=args)
        }

    else:
        body = {
            "name": name,
            "url": url,
            "method": method.upper(),
            "request": request,
            "response": response
        }

        body = json.dumps(body, encoding='utf-8', ensure_ascii=False, indent=4, separators=(',', ': '))

        m = models.Api(name=name, request=request, response=response, method=method, url=url, project_id=project, body=body)
        db.session.add(m)
        try:
            db.session.commit()
            return {
                'success': True,
                'code': '0000',
                'msg': 'success'
            }
        except IntegrityError:
            return {
                'success': False,
                'code': '0009',
                'msg': '接口地址 {url} 已经存在'.format(url=url),
            }

        except Exception:
            return {
                'success': False,
                'code': '0004',
                'msg': '系统异常',
                'traceback': traceback.format_exc()
            }


def update_mock_data(index, **kwargs):
    name = kwargs.get('name')
    url = kwargs.get('url')
    method = kwargs.get("method")
    request = kwargs.get("request")
    response = kwargs.get("response")

    if name is None:
        return {
            'success': False,
            'code': '0010',
            'msg': 'mock接口名字必填'
        }

    if url is None:
        return {
            'success': False,
            'code': '0011',
            'msg': 'mock接口地址必填'
        }

    if method is None:
        return {
            'success': False,
            'code': '0012',
            'msg': 'mock接口方法必填'
        }

    if name == '' or url == '':
        return {
            'success': False,
            'code': '0007',
            'msg': 'name或者path不能为空'
        }

    args = ['GET', 'POST', 'PUT', 'DELETE']

    if method.upper() not in args:
        return {
            'success': False,
            'code': '0008',
            'msg': '方法必须是 {args} 其中一个'.format(args=args)
        }

    else:
        m = models.Api.query.get(index)
        m.name = name
        m.url = url
        m.method = method.upper()
        m.request = request
        m.response = response
        m.body = json.dumps(kwargs, encoding='utf-8', ensure_ascii=False, indent=4, separators=(',', ': '))
        # m = models.Api(name=m.name, url=m.url, request=m.request, response=m.response, method=m.method,
        #                body=m.body)
        db.session.add(m)
        try:
            db.session.commit()
            return {
                'success': True,
                'code': '0000',
                'msg': 'success'
            }
        except IntegrityError:
            return {
                'success': False,
                'code': '0009',
                'msg': '接口地址 {url} 已经存在'.format(url=url),
            }

        except Exception:
            return {
                'success': False,
                'code': '0004',
                'msg': '系统异常',
                'traceback': traceback.format_exc()
            }
