from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard


class CustomIndexDashboard(Dashboard):
    columns = 3

    def init_with_context(self, context):
        self.available_children.append(modules.LinkList)
        self.children.append(modules.LinkList(
            _('Fill Questionnaire'),
            children=[
                {
                    'title': _('Questionnaire'),
                    'url': '/'
                },
            ],
            column=0,
            order=0
        ))

        self.children.append(modules.AppList(
            _('Survey Application'),
            exclude=('auth.*',),
            column=0,
            order=0
        ))
