import sys

from knapsack import celery_app

TASK_PREFIX = 'resolv_'

@celery_app.task
def resolv_greedy_heuristic(ks_id):
    """Greedy Heuristic"""

    return


@celery_app.task
def resolv_dynamic(ks_id):
    """Dynamic Programming"""

    return


@celery_app.task
def resolv_branch_bound(ks_id):
    """Branch & Bound"""

    return


class ResolverChoices(object):

    def __init__(self):
        module = sys.modules[self.__module__]

        self.available_resolver_names = []
        self.available_resolvers = {}

        for item in module.__dir__():
            if item.startswith(TASK_PREFIX):
                task = getattr(module, item)
                self.available_resolver_names.append((item.replace(module.TASK_PREFIX, ''), task.__doc__))
                self.available_resolvers[item] = task

    def __iter__(self):
        for x in self.available_resolver_names:
            yield x

    @property
    def default_resolver(self):
        return self.available_resolver_names[0][0]

    @property
    def resolver(self, name):
        return self.available_resolvers["%s%s" % (TASK_PREFIX, name)]

resolver_choices = ResolverChoices()