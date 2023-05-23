class ProjectInfo(object):
    def __init__(self, name: str, description: str = ''):
        self.name = name
        self.description = description


project_info = ProjectInfo('DjangoStarter')


def config_django_starter():
    return {
        # 管理后台的配置
        'admin': {
            'site_header': '提瓦特爱好家协会导航站后台',
            'site_title': '提瓦特爱好家协会导航站后台',
            'index_title': '提瓦特爱好家协会导航站后台',
            'list_per_page': 20
        },
        # 第三方登录配置
        'oauth': {
            # 微信企业号配置
            'wechat_work_config': {
                'corp_id': '',
                'secret': ''
            },
        }
    }
